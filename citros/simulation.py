import os
import json
import sys
import uuid
import shutil
from pathlib import Path
from citros.stats import SystemStatsRecorder
from rich import print, inspect, print_json
from rich.rule import Rule
from rich.panel import Panel
from rich.padding import Padding
from rich.logging import RichHandler
from rich.console import Console
from rich.markdown import Markdown
from rich_argparse import RichHelpFormatter
from datetime import datetime

from .logger import get_logger, shutdown_log

from .utils import suppress_ros_lan_traffic, validate_dir
from .parameter_setup import ParameterSetup
from .citros_obj import (
    CitrosObj,
    CitrosException,
    CitrosNotFoundException,
    FileNotFoundException,
    NoValidException,
)
from .events import EventsOTLP


class Simulation(CitrosObj):
    """Object representing .citros/simulations/name.json file."""

    ##################
    ##### public #####
    ##################
    def _get_simulation_run_log(self, simulation_rec_dir):
        return get_logger(
            __name__,
            log_level=os.environ.get("LOGLEVEL", "DEBUG" if self.debug else "INFO"),
            log_file=str(simulation_rec_dir / "citros.log"),
            verbose=self.verbose,
        )

    def copy_ros_log(self, destination: str):
        from .utils import get_last_created_file, copy_files, rename_file

        ros_logs_dir_path = get_last_created_file(
            Path("~/.ros/log/").expanduser(), dirs=True
        )
        if get_last_created_file is None:
            self.log.warning(f"Failed to find the ros logs directory.")
            return

        log_file_path = Path(ros_logs_dir_path, "launch.log")
        copy_files([log_file_path], destination, self.log)
        new_file_path = Path(destination, log_file_path.name)
        rename_file(new_file_path, "ros.log")

    def run(self, simulation_rec_dir, trace_context=None, ros_domain_id=None):
        """Run simulation."""
        # create .citros/data if not exists
        simulation_rec_dir.mkdir(parents=True, exist_ok=True)

        self.log = self._get_simulation_run_log(simulation_rec_dir)

        self.log.debug(f"{'   '*self.level}{self.__class__.__name__}.run()")
        events = EventsOTLP(self, trace_context)

        # running inside ROS workspace context.
        from launch import LaunchService
        from citros.ros import generate_launch_description

        self.log.info(f"running simulation [{self.name}]")
        # print(f"running simulation [{self.name}]")

        if self.verbose:
            self.log.info(f'simulation run dir = "{simulation_rec_dir}]"')
        else:
            self.log.debug(f'simulation run dir = "{simulation_rec_dir}]"')

        if ros_domain_id:
            suppress_ros_lan_traffic(ros_domain_id)

        launch_description = generate_launch_description(
            self, simulation_rec_dir, events
        )

        if launch_description is None:
            msg = f"ERROR. Failed to create launch_description."
            self.log.error(msg)
            return

        launch_service = LaunchService(debug=False)  # self.debug)
        launch_service.include_launch_description(launch_description)

        systemStatsRecorder = SystemStatsRecorder(f"{simulation_rec_dir}/stats.csv")
        systemStatsRecorder.start()

        ret = launch_service.run()

        systemStatsRecorder.stop()

        print(
            f"[{'blue' if ret == 0 else 'red'}] - - Finished simulation with return code [{ret}].",
        )

        self.copy_ros_log(simulation_rec_dir)

        # TODO!
        # self.save_run_data()

        if ret != 0:
            events.error(
                # batch_id,
                # run_id,
                message=f"Finished simulation. Return code = [{ret}].",
            )
            events.on_shutdown()
            # sys.exit(ret)
        else:
            events.done(
                # batch_id,
                # run_id,
                message=f"Finished simulation. Return code = [{ret}].",
            )
        return ret

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
        self.log.debug(f"{'   '*self.level}{self.__class__.__name__}._validate()")

        """Validate simulation.json file."""
        Path(self.root).mkdir(parents=True, exist_ok=True)

        # validate json schema is correct
        success = validate_dir(
            self.root_citros / "simulations", "schema_simulation.json", self.log
        )

        if not success:
            self.log.debug(f"{'   '*self.level}{self.__class__.__name__}: False")
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
            self.log.debug(f"{'   '*self.level}{self.__class__.__name__}: return False")
            return False

        self.log.debug(f"{'   '*self.level}{self.__class__.__name__}: return True")
        return True

    # overriding
    def _load(self):
        self.log.debug(f"{'   '*self.level}{self.__class__.__name__}._load()")

        try:
            # loads self.path()
            super()._load()
        except FileNotFoundError as ex:
            self.log.error(f"simulation file {self.file} does not exist.")
            raise FileNotFoundException(f"simulation file {self.file} does not exist.")

    # overriding
    def _new(self):
        self.log.debug(f"{'   '*self.level}{self.__class__.__name__}._new()")
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
