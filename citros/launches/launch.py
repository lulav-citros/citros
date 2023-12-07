import os
from typing import cast

from citros import Citros

################################
# Entrypoint        
################################
def generate_launch_description(citros : Citros):
    """
    Generates a ROS2 LaunchDescription for a simulation run.

    Args:
        citros (Citros): An instance of Citros class which manages interaction with the CiTROS service.

    Returns:
        launch.LaunchDescription: A launch description that ROS2 can execute.
    """
    # running inside ROS workspace context.  
    from ament_index_python.packages import get_package_share_directory
    from launch import LaunchDescription, Event
    from launch.actions import EmitEvent, ExecuteProcess, IncludeLaunchDescription, DeclareLaunchArgument, OpaqueFunction, RegisterEventHandler, LogInfo, TimerAction
    from launch.launch_description_sources import PythonLaunchDescriptionSource
    from launch_ros.actions import Node
    from launch.substitutions import LaunchConfiguration, LocalSubstitution, TextSubstitution
    from launch.event_handlers import (OnExecutionComplete, OnProcessExit,
                                    OnProcessIO, OnProcessStart, OnShutdown)
    from launch.events import Shutdown, process
    from launch.actions import SetLaunchConfiguration

    simulation_name = str(citros._sim_name)
    simulation_run_dir = str(citros.SIM_RUN_DIR)
    batch_run_id = str(citros._batch_id)    
    simulation_run_id = str(citros._run_id)
    
    citros.log.debug(f"generate_launch_description. batch_run_id: {batch_run_id}, simulation_run_id: {simulation_run_id}.")
    
    citros.events.init(batch_run_id=batch_run_id, sid=simulation_run_id, tag="INIT", message="initializing launch", metadata=None)

    ld = LaunchDescription([LogInfo(msg='CITROS launch file!')])

    ld.add_action(SetLaunchConfiguration('simulation_name', simulation_name))
    ld.add_action(SetLaunchConfiguration('simulation_run_dir', simulation_run_dir))

    ld.add_action(SetLaunchConfiguration('batch_run_id', batch_run_id))
    ld.add_action(SetLaunchConfiguration('simulation_run_id', simulation_run_id))

    batch = citros.batch.get_batch(batch_run_id, simulation_name) 
    
    if not batch:
        citros.log.error(f"unknown batch id [{batch_run_id}]")
        return

    # default timeout to 10 minutes.
    timeout = str(600)

    # override with simulation value
    timeout_from_client = batch['timeout']            
    if (float(timeout_from_client) > 1):
        timeout = str(timeout_from_client)
    ld.add_action(SetLaunchConfiguration('timeout', timeout))  

    citros.log.info(f"initializing simulation, batch_id: {batch_run_id}, run_id: {simulation_run_id}, timeout: {timeout}")

    ################################
    # Arguments        
    ################################
    ld.add_action(DeclareLaunchArgument(
        "log_level",
        default_value=["info"],
        description="Logging level",
    ))

    ld.add_action(DeclareLaunchArgument(
        "simulation_name",
        description="simulation name",
    ))

    #
    ld.add_action(DeclareLaunchArgument(
        "simulation_run_dir",
        description="simulation metadata directory",
    ))

    ld.add_action(DeclareLaunchArgument(
        'batch_run_id',
        description=(
            "Batch Run id"
        ),      
    ))

    ld.add_action(DeclareLaunchArgument(
        'simulation_run_id',
        description=(
            "Simulation run id, as part of [sequence]/[simulation.repeats]"
        ),
    ))

    ld.add_action(DeclareLaunchArgument(
        'timeout',
        description=(
            "The timeout for the simulation [sec]"
        ),   
        default_value=str(60*60*24*7),   
    ))

    ################################
    # RECORDING BAG Proccess 
    ################################ 

    # the simulation run directory is created ad-hoc before the call to generate_launch_description.
    bag_folder = citros.BAG_DIR
    bag_cmd = ['ros2', 'bag', 'record', '-a', '-o', bag_folder]
    
    mcap = citros.STORAGE_TYPE == 'MCAP'
    if mcap:
        bag_cmd.append('-s')
        bag_cmd.append('mcap')

    record_proccess = ExecuteProcess(
        cmd=bag_cmd,
        name="citros_bag_recorder",
        output='screen', 
        log_cmd=True
    )
    ld.add_action(record_proccess)

    # ################################
    # # STD LOG on ros events. 
    # ################################   
    # # Setup a custom event handler for all stdout/stderr from processes.
    # # Later, this will be a configurable, but always present, extension to the LaunchService.
    # def on_output(event: Event) -> None:
    #     for line in event.text.decode().splitlines():
    #         # log files will be written to ROS_LOGS_DIR rather than CLI_LOGS _DIR
    #         citros.log.info(f"[ROS][{cast(process.ProcessIO, event).process_name}]{line}")

    # ld.add_action(RegisterEventHandler(
    #     OnProcessIO(                
    #             on_stdout=on_output,
    #             on_stderr=on_output,
    #         )
    #     )
    # )

    ################################
    # User launch file
    ################################           

    def launch_setup(context, *args, **kwargs):
        citros.log.debug("launch_setup")

        simulation_name = LaunchConfiguration("simulation_name").perform(context)
        simulation_run_dir = LaunchConfiguration("simulation_run_dir").perform(context)

        batch_run_id = LaunchConfiguration("batch_run_id").perform(context)
        simulation_run_id = LaunchConfiguration("simulation_run_id").perform(context)

        # config
        config = citros.params.init_params(simulation_name, simulation_run_dir, int(simulation_run_id))
        # send event with the config to CiTROS
        citros.events.starting(batch_run_id=batch_run_id, sid=simulation_run_id, tag="CONFIG", message="updated config", metadata=config)

        # launch
        launch_name = citros.get_simulation_info(simulation_name)['launch']['file']
        launch_package = citros.get_simulation_info(simulation_name)['launch']['package']

        client_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                os.path.join(get_package_share_directory(launch_package), 'launch'), 
                f"/{launch_name}"
            ]),
            launch_arguments={}.items(),
        )

        citros.log.info(f"Starting clients launch package:{launch_package} launch:{launch_name}")
        citros.events.running(batch_run_id=batch_run_id, sid=simulation_run_id, tag="LAUNCH", message="Starting clients launch", metadata=None)

        return [
            client_launch
        ]

    ld.add_action(OpaqueFunction(function=launch_setup))

    ################################
    # Timeout Events
    ################################  
    def handle_timeout(context, *args, **kwargs):   
        citros.log.debug("handle_timeout")        
        batch_run_id = LaunchConfiguration("batch_run_id").perform(context)  
        simulation_run_id = LaunchConfiguration("simulation_run_id").perform(context)       
        timeout = LaunchConfiguration("timeout").perform(context)
        citros.events.terminating(batch_run_id, simulation_run_id, tag="TIMEOUT", message=f"Reached timeout of: { timeout } sec", metadata=None)            

    ld.add_action(
        TimerAction(
            period=LaunchConfiguration("timeout"),
            actions=[LogInfo(msg="---------TIMEOUT---------"), 
                    OpaqueFunction(function=handle_timeout),
                    EmitEvent(event=Shutdown(reason='TIMEOUT'))],
        )
    )

    ################################
    # Exit
    ################################  
    def handle_shutdown(context, *args, **kwargs):   
        citros.log.debug("handle_shutdown")
        batch_run_id = LaunchConfiguration("batch_run_id").perform(context)  
        simulation_run_id = LaunchConfiguration("simulation_run_id").perform(context)            
        reason = LocalSubstitution('event.reason').perform(context)
        citros.events.terminating(batch_run_id, simulation_run_id, tag="SHUTDOWN", message=reason, metadata=None)    

    ld.add_action(RegisterEventHandler(
        OnShutdown(
            on_shutdown=[
                OpaqueFunction(function=handle_shutdown),
                LogInfo(msg=['Launch was asked to shutdown: ', LocalSubstitution('event.reason')]
            )]
        )
    ))

    ld.add_action(RegisterEventHandler(OnProcessExit(
        target_action=record_proccess,
        on_exit=[
            LogInfo(msg=(f'The simulation has finished.')),
            EmitEvent(event=Shutdown(
                        reason='Finished'))
        ]
    )))

    return ld
