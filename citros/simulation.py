import os
import json
import uuid
import shutil
from pathlib import Path
from rich import print, inspect, print_json
from rich.rule import Rule
from rich.panel import Panel
from rich.padding import Padding
from rich.logging import RichHandler
from rich.console import Console
from rich.markdown import Markdown
from rich_argparse import RichHelpFormatter
from datetime import datetime

from .utils import suppress_ros_lan_traffic, validate_dir
from .parameter_setup import ParameterSetup
from .citros_obj import CitrosObj, CitrosException, NoFoundException, NoValidException
from .events import EventsOTLP

from .config import config

class Simulation(CitrosObj):
    """Object representing .citros/simulations/name.json file."""

    ##################
    ##### public #####
    ##################
    def run(self, root, run_id=0):
        """Run simulation."""
        
        events = EventsOTLP(self)
        
        
        # running inside ROS workspace context.
        from launch import LaunchService
        from citros.ros import generate_launch_description

        print(f" + + running simulation [{run_id}]")

        now = datetime.today().strftime('%Y%m%d%H%M%S')
        # data/{sim}/{run name}/{date time}
        if config.RECORDINGS_DIR:
            simulation_rec_dir = Path(config.RECORDINGS_DIR) / self.name / name / now
        else:
            simulation_rec_dir = self.root_citros / 'data' / self.name / name / now
        
        if self.verbose:            
            print(f'simulation run dir = "{simulation_rec_dir}]"')
        
        # create .citros/data if not exists
        simulation_rec_dir.mkdir(parents=True, exist_ok=True)
        # TODO: create simulation_rec_dir / batch.json 
        
        
        # self.create_sim_run_dir(run_id)
        # self.set_logger(self.SIM_RUN_DIR, "citros_sim_launch.log", batch_id, run_id)

        if config.SUPPRESS_ROS_LAN_TRAFFIC:
            suppress_ros_lan_traffic()

        launch_description = generate_launch_description(self, name, message)

        if launch_description is None:
            msg = (
                f"Couldn't run run_id:[{run_id}]. Failed to create launch_description."
            )
            self.log.error(msg)
            return

        launch_service = LaunchService(debug=(self.log_level == "debug"))
        launch_service.include_launch_description(launch_description)

        self.systemStatsRecorder.start()

        ret = launch_service.run()

        self.systemStatsRecorder.stop()

        
        print(
            f"[{'blue' if ret == 0 else 'red'}] - - Finished simulation run_id = [{run_id}] with return code [{ret}].",

        )

        self.save_run_data()

        if ret != 0:
            self.events.error(
                batch_id, run_id, message=f"Finished simulation. Return code = [{ret}]."
            )
            self.events.on_shutdown()
            sys.exit(ret)
        else:
            self.events.done(
                batch_id, run_id, message=f"Finished simulation. Return code = [{ret}]."
            )

    # overriding
    def path(self):
        return self.root_citros / "simulations" / f"{self.file}"

    ###################
    ##### private #####
    ###################

    def __init__(
        self,
        name,
        root=None,
        new=False,
        log=None,
        citros=None,
        package_name=None,
        launch_file=None,
        verbose=False,
        debug=False,
        level=0,
    ):
        # used for new simulation
        self.package_name = package_name
        self.launch_file = launch_file
        super().__init__(name, root, new, log, citros, verbose, debug, level)

    # overriding
    def _validate(self):
        """Validate simulation.json file."""
        Path(self.root).mkdir(parents=True, exist_ok=True)

        # validate json schema is correct
        success = validate_dir(
            self.root_citros / "simulaitons", "schema_simulation.json", self.log
        )

        if not success:
            return False

        # validate parameter_setup file
        param_setup = self["parameter_setup"]

        parameter_setup = ParameterSetup(
            param_setup,
            root=self.root,
            new=self.new,
            log=self.log,
            citros=self.citros,
            verbose=self.verbose,
            debug=self.debug,
            level=self.level + 1,
        )

        # validate launch file
        launch_file = self["launch"]["file"]
        all_launch_names = [launch["name"] for launch in self._get_launches()]
        if launch_file not in all_launch_names:
            print(
                f'[red]Could not find launch file named {launch_file} referenced in "{self.path()}."',
            )
            return False

        return True

    # overriding
    def _load(self):
        # print(f"_load ({self.__class__.__name__}) ->  ", self.data)
        try:
            # loads self.path()
            super()._load()
        except FileNotFoundError as ex:
            self.log.error(f"simulation file {self.file} does not exist.")
            raise NoFoundException(f"simulation file {self.file} does not exist.")

    # overriding
    def _new(self):
        path = self.path()

        # avoid overwrite
        if path.exists():
            self._load()
            # return

        Path(self.root_citros / "simulations").mkdir(parents=True, exist_ok=True)

        # got from __init__
        if self.launch_file is None or self.package_name is None:
            raise ValueError(
                "package_name and launch_file must be provided when creating a new simulation"
            )

        default = {
            "id": str(uuid.uuid4()),
            "description": "Default simulation. Change the values according to your needs.",
            "parameter_setup": "default_param_setup.json",
            "launch": {"file": self.launch_file, "package": self.package_name},
            "timeout": 60,
            "GPU": 0,
            "CPU": 2,
            "MEM": 265,
            "storage_type": "MCAP",
        }
        self.data = default | self.data
        self._save()

    ###################
    ##### utils #####
    ###################

    def _get_launches(self):
        """returns a list of launch objects

        Args:
            proj_json (Path): path to project.json file

        Returns:
            [{
                package: str,
                name: str
            }]: array of launch info
        """

        launch_info = []

        for package in self.citros.get("packages", []):
            for launch in package.get("launches", []):
                if "name" in launch:
                    launch_info.append(
                        {"package": package.get("name", ""), "name": launch["name"]}
                    )

        return launch_info

    def _check_simualtion_run_name(self, name):
        batch_name_idx = 1

        if not name or not self.utils.is_valid_file_name(name):
            name = self.utils.get_foramtted_datetime()

        # avoid duplicate batch dir names
        elif Path(
            self._router()["citros"]["runs"]["path"],
            self._sim_name,
            name,
        ).exists():
            while Path(
                self._router()["citros"]["runs"]["path"],
                self._sim_name,
                f"{name}_{str(batch_name_idx)}",
            ).exists():
                batch_name_idx = batch_name_idx + 1
            name = f"{name}_{str(batch_name_idx)}"
        return name
