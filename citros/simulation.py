import os
import json
import sys
import uuid
import shutil
import importlib_resources

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

    def _copy_ros_log(self, destination: str):
        self.log.debug(f"{'   '*self.level}{self.__class__.__name__}._copy_ros_log()")
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

    @staticmethod
    def _guess_msgtype(path: Path) -> str:
        """
        Guess the message type based on the path.

        Args:
            path (Path): The file path to the message type.

        Returns:
            str: The guessed message type.
        """
        name = path.relative_to(path.parents[2]).with_suffix("")
        if "msg" not in name.parts:
            name = name.parent / "msg" / name.name
        return str(name)

    def _register_custom_message(self, msgpath: str):
        """
        Register custom message types from a given folder path.

        Args:
            message_folder_path (str): The folder path where custom messages are stored.
        """
        from rosbags.typesys import get_types_from_msg, register_types

        msgdef = msgpath.read_text(encoding="utf-8")
        add_types = get_types_from_msg(msgdef, self._guess_msgtype(msgpath))
        self.log.debug(f"{'   '*self.level}regisering {msgpath} ...")

        register_types(add_types)

    def _copy_msg_files(self, destination: str):
        self.log.debug(f"{'   '*self.level}{self.__class__.__name__}.copy_msg_files()")
        from .utils import copy_files
        from .parsers import ParserRos2

        msg_paths = ParserRos2(self.log).get_msg_files(self.root)
        for msg_path in msg_paths:
            # assuming msg files are under package_name/msg/
            package_name = Path(msg_path).parent.parent.name
            target_dir = Path(destination, package_name, "msg")
            copy_files([msg_path], str(target_dir), self.log, True)

            # register custom messages
            self._register_custom_message(str(msg_path))

    def _handle_msg_files(self, simulation_rec_dir):
        self._copy_msg_files(simulation_rec_dir)

    def _save_system_vars(self, destination: str):
        import subprocess
        from os import linesep

        self.log.debug(
            f"{'   '*self.level}{self.__class__.__name__}._save_system_vars()"
        )
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

        with open(Path(destination, "environment.json"), "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def _add_string_connection(writer, connection, msgtype):
        """
        Adds a new connection with a modified topic name by appending '/path' to the original topic.

        This method is specifically intended for handling string connections. After modifying the topic name,
        it uses the provided writer to add the new connection, keeping other connection parameters unchanged.

        Args:
            writer (Writer): An object responsible for writing data.
            connection (Connection): The original connection object.
            msgtype (str): The message type for the new connection.

        Returns:
            list: A list containing the writer and the newly created connection object.

        """
        from typing import TYPE_CHECKING, cast
        from rosbags.interfaces import ConnectionExtRosbag2, Connection

        ext = cast(ConnectionExtRosbag2, connection.ext)
        new_connection = writer.add_connection(
            topic=connection.topic + "/path",
            msgtype=msgtype,
            serialization_format=ext.serialization_format,
            offered_qos_profiles=ext.offered_qos_profiles,
        )
        return writer, new_connection

    @staticmethod
    def _create_string_topic(writer, file_name, connection):
        """
        Creates a new topic with a string message type, intended for writing a file path.

        This method attempts to create a new connection using the provided writer and an existing connection.
        The topic of the new connection is the original topic name with '/path' appended to it.
        It then creates a new String message populated with the given file name.

        Args:
            writer (Writer): The writer object responsible for writing data.
            file_name (str): The file name to be used in the new String message.
            connection (Connection): The original connection object.

        Returns:
            tuple: A tuple containing the writer, the new connection object, the new data (String message),
                and the message type for the new connection.

        Raises:
            Exception: Catches any exceptions thrown during the process. Handles specifically the case when
                    a connection with the new topic name already exists.
        """
        from rosbags.serde import deserialize_cdr, serialize_cdr
        from rosbags.rosbag2 import Reader, Writer
        from rosbags.interfaces import ConnectionExtRosbag2, Connection

        msgtype = String.__msgtype__
        try:
            # try to add string topic to the bag
            writer, new_connection = Simulation._add_string_connection(
                writer, connection, msgtype
            )
        except Exception as e:
            if "Connection can only be added once" in str(e):
                # the connection is already created, take it from the connection list
                new_connection = [
                    x
                    for x in writer.connections
                    if x.topic == connection.topic + "/path"
                ][0]
        new_data = String(file_name)
        return writer, new_connection, new_data, msgtype

    def _create_citros_bag(self, src: str, dst: str):
        """
        Create a new ROS bag file by reading from an existing bag and transforming its contents.

        This method reads messages from an existing ROS bag located at `src`, and writes to a new ROS bag at `dst`.
        It performs custom handling for messages of the type "sensor_msgs/msg/Image" by saving them as image files
        and then writing a new corresponding string message in the new bag.

        Args:
            src (str): The path to the source ROS bag file to be read.
            dst (str): The path to the destination ROS bag file to be created.

        Raises:
            Various exceptions could be raised during reading and writing of the bag files,
            which will be logged using the logger.

        Side Effects:
            - A new ROS bag is created at the location specified by `dst`.
            - Additional image data files and metadata might be created based on the source bag's content.
            - Logging information is produced to inform about the operations and potential errors.

        Note:
            - If an image topic is encountered, the image data is saved separately and a string message is added to the new bag.

        """
        self.log.debug(
            f"{'   '*self.level}{self.__class__.__name__}._create_citros_bag(src={src}, dst={dst})"
        )

        from typing import TYPE_CHECKING, cast
        from rosbags.serde import deserialize_cdr, serialize_cdr
        from rosbags.rosbag2 import Reader, Writer
        from rosbags.interfaces import ConnectionExtRosbag2, Connection

        if src.endswith("/"):
            src = src[:-1]

        # check id name of file contain .citros
        if ".citros" in src.split("/")[-1]:
            self.log.warning(f"CITROS bag already exist, skipping ...")
            return

        self.log.info(f"Creating a new CITROS bag: src = {src}\ndst = {dst}")

        try:
            with Reader(src) as reader, Writer(dst) as writer:
                # create connection map to the writer
                conn_map = {}
                for conn in reader.connections:
                    try:
                        ext = cast(ConnectionExtRosbag2, conn.ext)
                        conn_map[conn.id] = writer.add_connection(
                            topic=conn.topic,
                            msgtype=conn.msgtype,
                            serialization_format=ext.serialization_format,
                            offered_qos_profiles=ext.offered_qos_profiles,
                        )
                    except Exception as e:
                        self.log.error(e)
                        continue

                # reader.connections is a list, we need start from 0 and not from 1 (this is why is x-1)
                rconns = [reader.connections[x - 1] for x in conn_map]

                for connection, timestamp, data in reader.messages(connections=rconns):
                    if "sensor_msgs/msg/Image" in connection.msgtype:
                        # if this is a image topic export data and continue without saving in the new bag.
                        file_name = self._handle_image_message(dst, data, connection)
                        (
                            writer,
                            new_connection,
                            new_data,
                            msgtype,
                        ) = self._create_string_topic(writer, file_name, connection)
                        writer.write(
                            new_connection, timestamp, serialize_cdr(new_data, msgtype)
                        )
                        self.log.info(
                            f"Found image, saving image data under {file_name}"
                        )
                        continue
                    writer.write(conn_map[connection.id], timestamp, data)
                return
        except Exception as e:
            if "citros exists already" in str(e):
                self.log.warning("CITROS bag already exist ...")
                return

    def _get_bags(self, path: str) -> dict:
        """
        Retrieve the paths of bag files in the specified directory and its subdirectories.

        This method recursively traverses the directory structure from the specified path, looking for files with
        ".mcap" or ".db3" extensions. It logs the discovery of any such files.

        Args:
            path (str): The root directory where the search for bag files will commence.

        Returns:
            list: A dict of paths where ".mcap" or ".db3" files are found.

        Raises:
            Exception: If no ".mcap" or ".db3" files are found in the specified path and its subdirectories.

        Note:
            Logging is done to debug the discovery of ".mcap" and ".db3" files.
        """
        self.log.debug(f"{'   '*self.level}{self.__class__.__name__}._get_bags({path})")
        bags = {}
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".mcap"):
                    self.log.debug(f"Found MCAP bag: {file}")
                elif file.endswith(".db3"):
                    self.log.debug(f"Found SQLITE3 bag: {file}")
                else:
                    continue
                bags[root] = file

        if len(bags) < 1:
            raise Exception(
                f"Didn't find SQLITE3 or MCAP bag in the [{path}] folder ..."
            )

        return bags

    def _prepare_citros_bag(self, destination: str):
        # assuming bags already there (the simulations is done recording)
        bags = self._get_bags(f"{destination}/bags/")
        for bag_path, file_name_with_ext in bags.items():
            file_name = os.path.splitext(file_name_with_ext)[0]
            self._create_citros_bag(bag_path, bag_path + f"{file_name}.citros/")

    def run(self, simulation_rec_dir, sid=0, trace_context=None, ros_domain_id=None):
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

        # launch
        launch_description = generate_launch_description(
            self, simulation_rec_dir, sid, events
        )

        if launch_description is None:
            msg = f"ERROR. Failed to create launch_description."
            self.log.error(msg)
            return

        launch_service = LaunchService(debug=False)  # self.debug)
        launch_service.include_launch_description(launch_description)

        systemStatsRecorder = SystemStatsRecorder(f"{simulation_rec_dir}/stats.csv")
        systemStatsRecorder.start()

        # run simulation
        ret = launch_service.run()

        systemStatsRecorder.stop()

        print(
            f"[{'blue' if ret == 0 else 'red'}]Finished simulation with return code [{ret}].",
        )

        try:
            print(f"Copying ros logs...")
            self._copy_ros_log(simulation_rec_dir)
        except Exception as e:
            self.log.error(e)
        try:
            print(f"Copying and registering messages logs...")
            self._handle_msg_files(simulation_rec_dir)
        except Exception as e:
            self.log.error(e)
        try:
            print(f"Saving system vars...")
            self._save_system_vars(simulation_rec_dir)
        except Exception as e:
            self.log.error(e)
        try:
            print(f"Preparing citros bags...")
            self._prepare_citros_bag(simulation_rec_dir)
        except Exception as e:
            self.log.error(e)

        if ret != 0:
            events.error(
                message=f"Finished simulation. Return code = [{ret}].",
            )
            events.on_shutdown()
            # sys.exit(ret)
        else:
            events.done(
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
        self.parameter_setup = None
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

        self.parameter_setup = ParameterSetup(
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
        # self.data = default | self.data
        self.data.update(default)
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
