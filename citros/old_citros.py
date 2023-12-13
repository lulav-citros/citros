import os
import sys
import git
import glob
import json
import time


import requests
import traceback
import traceback
import jsonschema
import subprocess
import citros_meta
from os import linesep
from pathlib import Path
from .config import config

from .stats import SystemStatsRecorder
from .parsers import parser_ros2
from .logger import get_logger, shutdown
from .utils import citros_utils
from .citros_batch import citros_batch
from .ros.params import citros_params
from .events import citros_events
from rich import print, print_json, inspect


class Citros:
    """
    The Citros class implements the frontend of the Citros CLI.
    It must be instantiated within a `with` block in order to prevent
    resource leaks and unexpected behavior.
    """

    def __init__(self, root_dir=None, verbose=False, debug=False):
        """
        Initialize Citros instance.

        Args:
        root_dir:       optional project directory, defaults to current
                        working directory.
        verbose:        optionally turn on verbose console output.
        debug:          If True, sets log level to debug and turns on debug
                        output for the ROS simulation. Else, log level will
                        be info, and debug output for the ROS simulation will
                        not be given. Defaults to False.
        """
        self.config = config

        # self.root_dir = ROOT_DIR -> search for .citros in `root_dir` ancestors -> root_dir
        self.root_dir: Path = (
            None if self.config.ROOT_DIR is None else Path(self.config.ROOT_DIR)
        )
        if self.root_dir is None:
            citros_dir = self._find_citros_in_ancestors(root_dir)
            # print("1", citros_dir)
            if citros_dir == self.config.CITROS_HOME_DIR:
                citros_dir = None

            if citros_dir is not None:
                self.root_dir = Path(citros_dir.parent)
            else:
                self.root_dir = Path(Path.cwd())

        if not self.root_dir:
            self.log.error("problem!!!")

        # logs
        self.log = None
        self.log_level = "debug" if debug else "info"
        self.set_logger(self._router()["citros"]["logs"]["path"])

        self._init_components()

        # self.data = {
        #     "simuations": [
        #         {
        #             "name": "simulation_1",
        #             "value": Smulation(path),
        #         }
        #     ]
        #     "parameters": [
        #         {
        #             "name": "parameter_1",
        #             "value": PS(path),
        #         }
        #     ]
        #     "settings": {}
        # }

    def _handle_exceptions(self, e, exit=False):
        """
        Handles exceptions and logs them.

        Args:
        e: Exception to handle.
        """
        self.print(
            f'An exception was raised. See log file under {self._router()["citros"]["logs"]["path"]} for details'
            + f" (or use the -d flag to log to the terminal).",
            color="red",
        )
        stack_trace = traceback.format_exception(type(e), e, e.__traceback__)
        stack_trace_str = "".join(stack_trace)
        self.log.error(f"Exception details:{linesep}{stack_trace_str}")

        if exit:
            shutdown()  # flush logger
            sys.exit(3)

    def __enter__(self):
        """
        Returns the Citros instance. This allows the class to be used in a `with` statement.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Makes sure the stats collecting thread is stopped and handles exceptions.

        Args:
        exc_type: The type of exception.
        exc_val: The exception instance.
        exc_tb: A traceback object encapsulating the call stack at the point
                where the exception originally occurred.
        """
        self.events.on_shutdown()

        self.systemStatsRecorder.stop()

        if exc_type is not None:
            self._handle_exceptions(exc_val, exit=True)

    def _router(self, root_dir=None):
        if root_dir is None:
            root_dir = self.root_dir

        citros_dir: Path = (
            None if self.root_dir is None else Path(self.root_dir, ".citros")
        )
        return {
            "path": root_dir,
            "citros": {
                "path": citros_dir,
                "project.json": Path(citros_dir, "project.json"),
                "settings.json": Path(citros_dir, "settings.json"),
                "simulations": {"path": Path(citros_dir, "simulations")},
                "parameters": {
                    "path": Path(citros_dir, "parameter_setups"),
                    "functions": {
                        "path": Path(citros_dir, "parameter_setups", "functions"),
                    },
                },
                "notebooks": {"path": Path(citros_dir, "notebooks")},
                "reports": {"path": Path(citros_dir, "reports")},
                "runs": {
                    "path": self.config.RECORDINGS_DIR
                    if self.config.RECORDINGS_DIR is not None
                    else Path(citros_dir, "runs"),
                },
                "logs": {"path": Path(self.config.CITROS_HOME_DIR, "logs")},
            },
        }

    def _init_components(self):
        self.events = citros_events(self)
        self.parser_ros2 = parser_ros2(self)
        self.params = citros_params(self)
        self.utils = citros_utils(self)
        self.batch = citros_batch(self)

    def print(self, message, only_debug=False, only_verbose=False, color="default"):
        if (only_debug and self.log_level != "debug") or (
            only_verbose and not self.config.VERBOSE
        ):
            return

        print(f"[{color}]{message}[/{color}]")

    #################### initialization and validation ########################

    def check_ros_build(self, project_path):
        package_paths = self.parser_ros2.get_project_package_paths(project_path)
        workspaces = set()
        for package_path in package_paths:
            src_dir = self.utils.find_ancestor_with_name(package_path, "src")
            if src_dir is None:
                msg = f"Unsupported project structure: package {package_path} is not under `src` folder."
                self.log.error(msg)
                self.print(msg, color="red")
                return False
            workspaces.add(Path(src_dir).parent)

        for ws in workspaces:
            if not any(p.is_dir() and p.name == "install" for p in ws.iterdir()):
                msg = f"Workspace {ws} has not been built."
                self.log.error(msg)
                self.print(msg, color="red")
                return False

        return True

    ############################## ROS Operations ############################

    def create_sim_run_dir(self, run_id):
        run_dir = Path(
            self._router()["citros"]["runs"],
            self._sim_name,
            self._batch_name,
            str(run_id),
        )
        run_dir.mkdir(parents=True, exist_ok=False)
        self.SIM_RUN_DIR = str(run_dir)
        self.BAG_DIR = str(Path(self.SIM_RUN_DIR, "bag"))
        self.MSGS_DIR = str(Path(self.SIM_RUN_DIR, "msgs"))

        # in case the user needs access to SIM_RUN_DIR.
        os.environ["CITROS_SIM_RUN_DIR"] = self.SIM_RUN_DIR

        self.print(f"simulation run dir = [{self.SIM_RUN_DIR}]", only_verbose=True)

    def copy_msg_files(self):
        # sanity check
        if self.MSGS_DIR is None:
            self.log.error("MSG_DIRS has not been created.")
            return

        msg_paths = self.parser_ros2.get_msg_files(self.root_dir)
        for msg_path in msg_paths:
            # assuming msg files are under package_name/msg/
            package_name = Path(msg_path).parent.parent.name
            target_dir = Path(self.MSGS_DIR, package_name, "msg")
            self.utils.copy_files([msg_path], str(target_dir), True)

    def get_bag_name(self):
        if self.config.STORAGE_TYPE == "SQLITE3":
            return "bag_0.db3"
        elif self.config.STORAGE_TYPE == "MCAP":
            return "bag_0.mcap"
        else:
            raise ValueError("Unknown storage type.")

    def save_run_info(self):
        bag_hash = self.utils.compute_sha256_hash(
            Path(self.BAG_DIR, self.get_bag_name())
        )

        batch = self.batch.get_batch(self._batch_id, self._sim_name)

        with open(Path(self.SIM_RUN_DIR).parent / "info.json", "w") as sim_file:
            json.dump(batch, sim_file, indent=4)

        batch["batchId"] = self._batch_id
        batch["bagHash"] = bag_hash
        batch["id"] = self._run_id

        with open(Path(self.SIM_RUN_DIR, "info.json"), "w") as sim_file:
            json.dump(batch, sim_file, indent=4)

    def is_inside_dev_container(self):
        return "REMOTE_CONTAINERS" in os.environ

    def save_system_vars(self):
        # Get all environment variables
        env_vars = dict(os.environ)

        pip_freeze_output = subprocess.run(
            ["pip", "freeze"], capture_output=True, text=True
        )

        if pip_freeze_output.returncode != 0:
            self.log.error("pip freeze failed: " + pip_freeze_output.stderr)
            python_packages = []
        else:
            python_packages = pip_freeze_output.stdout.split(linesep)

        data = {"environment_variables": env_vars, "python_packages": python_packages}

        with open(Path(self.SIM_RUN_DIR, "environment.json"), "w") as f:
            json.dump(data, f, indent=4)

    def copy_ros_log(self):
        ros_logs_dir_path = self.utils.get_last_created_file(
            Path("~/.ros/log/").expanduser(), dirs=True
        )

        if ros_logs_dir_path is not None:
            log_file_path = Path(ros_logs_dir_path, "launch.log")
            self.utils.copy_files([log_file_path], self.SIM_RUN_DIR)
            new_file_path = Path(self.SIM_RUN_DIR, log_file_path.name)
            self.utils.rename_file(new_file_path, "ros.log")
        else:
            self.log.warning(f"Failed to find the ros logs directory.")

    def copy_citros_log(self):
        log_file_path = Path(self._router()["citros"]["logs"]["path"], "citros.log")
        self.utils.copy_files([log_file_path], self.SIM_RUN_DIR)

    def save_run_data(self):
        self.copy_msg_files()
        self.copy_citros_log()
        self.copy_ros_log()
        self.save_run_info()
        self.save_system_vars()

    ############################## RUN ########################################
    def single_simulation_run(self, batch_id, run_id):
        # running inside ROS workspace context.
        from launch import LaunchService
        from citros.ros import generate_launch_description

        self.print(f" + + running simulation [{run_id}]", color="blue")

        self.create_sim_run_dir(run_id)

        self.set_logger(self.SIM_RUN_DIR, "citros_sim_launch.log", batch_id, run_id)

        if self.config.SUPPRESS_ROS_LAN_TRAFFIC:
            self.utils.suppress_ros_lan_traffic()

        launch_description = generate_launch_description(self)

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

        color = "blue" if ret == 0 else "red"
        self.print(
            f" - - Finished simulation run_id = [{run_id}] with return code [{ret}].",
            color=color,
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

    def run_batch(self, batch_id, completions, description=""):
        self.print(
            f" + running batch [{batch_id}], description: {description}, repeating simulations: [{completions}]",
            color="blue",
        )

        for run_id in range(0, completions):
            try:
                self.single_simulation_run(batch_id, run_id)
                time.sleep(1)
            except Exception as e:
                self.print("------------------------")
                self.print(e, color="red")
                traceback.print_exc()
                self.print("------------------------")
                continue

        self.print(f" - Finished [{batch_id}] batch.", color="blue")

    def run_simulation(
        self, sim_name, run_id=0, completions=1, commit=None, branch=None
    ):
        completions = int(completions)

        sim = self.get_simulation_info(sim_name)
        cpu = sim["CPU"]
        gpu = sim["GPU"]
        mem = sim["MEM"]
        timeout = sim["timeout"]
        storage_type = sim.get("storage_type", self.config.STORAGE_TYPE)
        commit, branch = self.get_user_git_info()

        sim_name = self.check_simualtion_run_name(sim_name)

        self.systemStatsRecorder = SystemStatsRecorder(
            Path(self.SIM_RUN_DIR, "metrics.csv")
        )

        batch_id = self.batch.generate_batch_id()

        # start the open-telemetry trace.
        self.events.creating(batch_id)

        where = "locally"  # if not remote else f"on Citros cluster. See {self.CITROS_URL}/{self._get_project_name()}/batch/{batch_id}"

        msg = f"created new batch_id: {batch_id}. Running {where}."
        self.log.info(msg)
        self.print(msg, color="blue")

        self.run_batch(batch_id, completions, self._batch_message)
