import json
import glob
import shutil
import importlib_resources

from os import linesep
from pathlib import Path

from citros.parsers import ParserRos2
from citros.utils import validate_dir, validate_file

# from .ros import Ros
from .settings import Settings
from .simulation import Simulation
from .parameter_setup import ParameterSetup
from .citros_obj import (
    CitrosObj,
    CitrosException,
    FileNotFoundException,
    CitrosNotFoundException,
    NoValidException,
)

from rich.traceback import install
from rich.logging import RichHandler
from rich import print, inspect, print_json
from rich.panel import Panel
from rich.padding import Padding
import shutil

install()

from .batch import Batch


class Citros(CitrosObj):
    """Object representing .citros/simulations/{name}.json file."""

    # def __enter__(self):
    #     """
    #     Returns the Citros instance. This allows the class to be used in a `with` statement.
    #     """
    #     return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     """
    #     Makes sure the stats collecting thread is stopped and handles exceptions.

    #     Args:
    #     exc_type: The type of exception.
    #     exc_val: The exception instance.
    #     exc_tb: A traceback object encapsulating the call stack at the point
    #             where the exception originally occurred.
    #     """
    #     self.events.on_shutdown()

    #     self.systemStatsRecorder.stop()

    #     if exc_type is not None:
    #         self._handle_exceptions(exc_val, exit=True)

    def __init__(
        self,
        name="project",
        root=None,
        new=False,
        log=None,
        citros=None,
        verbose=False,
        debug=False,
        level=0,
    ):
        ###################
        ##### .citros #####
        ###################
        # init settings
        self.settings = None

        # init parameter_setups
        self.parameter_setups = []

        # init simulations
        self.simulations = []

        #################
        ##### utils #####
        #################
        self._ros = None

        super().__init__(name, root, new, log, citros, verbose, debug, level)

    def __str__(self):
        # print_json(data=self.data)
        return json.dumps(self.data, indent=4)

    ###################
    ##### private #####
    ###################
    # overriding
    def _validate(self):
        """Validate the json file."""

        # TODO: check that the project.json file is valid

        return True

    # overriding
    def _load(self):
        self.log.debug(f"{'   '*self.level}{self.__class__.__name__}.load()")

        self.copy_default_citros_files()

        # loads the main file (project.json)
        try:
            self.log.debug(f"loading .citros/project.json")
            super()._load()
        except FileNotFoundError as ex:
            self.log.error(f"simulation file {self.file} does not exist.")
            raise FileNotFoundException(f"simulation file {self.file} does not exist.")

        # loads the settings.json file
        self.log.debug(f"loading .citros/settings.json")
        self.settings = Settings(
            "settings",
            root=self.root,
            log=self.log,
            citros=self,
            new=self.new,
            debug=self.debug,
            verbose=self.verbose,
            level=self.level + 1,
        )

        # loads the parameter_setups
        for file in glob.glob(f"{self.root_citros}/parameter_setups/*.json"):
            file = file.split("/")[-1]
            self.log.debug(f"loading parameter_setup: {file}")
            self.parameter_setups.append(
                ParameterSetup(
                    file,
                    root=self.root,
                    new=self.new,
                    log=self.log,
                    citros=self,
                    debug=self.debug,
                    verbose=self.verbose,
                    level=self.level + 1,
                )
            )

        # loads the simulations
        for file in glob.glob(f"{self.root_citros}/simulations/*.json"):
            file = file.split("/")[-1]
            # self.simulations.append(Simulation(self.root, file, self.log, citros=self))
            self.log.debug(f"loading simulation: {file}")
            self.simulations.append(
                Simulation(
                    file,
                    root=self.root,
                    new=self.new,
                    log=self.log,
                    citros=self,
                    debug=self.debug,
                    verbose=self.verbose,
                    level=self.level + 1,
                )
            )

        # utils
        # self.ros = Ros(self.root, "ros.json", self.log)

    # overriding
    def _new(self):
        self.log.debug(f"{'   '*self.level}{self.__class__.__name__}._new()")

        # create the .citros folder
        Path(self.root_citros).mkdir(parents=True, exist_ok=True)
        # copy data files.
        self.copy_default_citros_files()

        # settings
        self.log.debug(f"creating .citros/settings.json")
        self.settings = Settings(
            "settings",
            root=self.root,
            log=self.log,
            citros=self,
            new=self.new,
            verbose=self.verbose,
            debug=self.debug,
            level=self.level + 1,
        )

        self._parser_ros2 = ParserRos2(self.log, self.get_citros_ignore_list())
        # get data from ros2
        project_data = self._parser_ros2.parse(str(self.root))
        with open(self.path(), "w") as file:
            json.dump(project_data, file, sort_keys=True, indent=4)

        self.data = project_data
        self._save()

        # parameter setups
        self.log.debug(f"creating .citros/parameter_setups/default_param_setup.json")
        self.parameter_setups = ParameterSetup(
            "default_param_setup",
            root=self.root,
            log=self.log,
            citros=self,
            new=self.new,
            verbose=self.verbose,
            debug=self.debug,
            level=self.level + 1,
        )

        # create simulation per launch file as default
        self.log.debug(f"creating .citros/simulations/*")
        self._create_simulations()

    #################
    ##### utils #####
    #################
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

    def _create_simulations(self):
        launch_infos = self._get_launches()
        if not launch_infos:
            self.log.warning("No launch files found in user's project.")
            print(
                Panel.fit(
                    Padding(
                        "[yellow]No launch files found. [white]If you have launch files in your project, make sure they are of the form [green]*.launch.py ",
                        1,
                    ),
                    title="help",
                )
            )

            return

        # inspect(launch_infos)
        for launch in launch_infos:
            package_name = launch["package"]
            launch_file = launch["name"]

            # print("vova", self.root, f"simulation_{launch_file.split('.')[0]}.json")
            self.simulations.append(
                Simulation(
                    f"simulation_{launch_file.split('.')[0]}",
                    root=self.root,
                    new=self.new,
                    log=self.log,
                    citros=self,
                    package_name=package_name,
                    launch_file=launch_file,
                    verbose=self.verbose,
                    debug=self.debug,
                    level=self.level + 1,
                )
            )

    def get_citros_ignore_list(self):
        if Path(self.root_citros, ".citrosignore").exists():
            with open(Path(self.root_citros, ".citrosignore"), "r") as file:
                lines = [line.strip() for line in file if "#" not in line]
                self.log.debug(f".citrosignore contenrs: {lines}")
                return lines
        else:
            self.log.debug(f"Could not find .citrosignore in {self.root_citros}")
            return []

    def copy_default_citros_files(self):
        self.log.debug(
            f"{'   '*self.level}{self.__class__.__name__}.copy_default_citros_files()"
        )

        source_folder = importlib_resources.files("data.defaults.citros")

        self.log.debug(f"copying {source_folder} to {self.root_citros}")

        shutil.copytree(source_folder, self.root_citros, dirs_exist_ok=True)

        self.log.debug(f"Done.")

    ###################
    ##### public ######
    ###################
    def delete_batch(self, simulation: str, name: str, version: str):
        import shutil

        shutil.rmtree(self.root_citros / "data" / simulation / name / version)

    def get_batch(self, simulation: str, name: str, version=-1):
        batch = Batch(
            self.root_citros / "data",
            simulation,
            name=name,
            version=version if type(version) is str else None,
            index=version if type(version) is int else None,
            debug=self.debug,
            verbose=self.verbose,
        )

        return batch

    def unload_batch(self, simulation, batch):
        versions = glob.glob(f"{simulation}/{batch}/*")
        for ver in versions:
            batch = self.get_batch(simulation, batch, ver)
            batch.unload()

    def get_batches(self, simulation=None, batch=None, filter: str = None):
        batches = []
        if simulation:
            simulations = sorted(
                glob.glob(f"{str(self.root_citros / 'data' / simulation)}")
            )
        else:
            simulations = sorted(glob.glob(f"{str(self.root_citros / 'data')}/*/"))

        for sim in simulations:
            if batch:
                batch_names = sorted(glob.glob(f"{sim}/{batch}/"))
            else:
                batch_names = sorted(glob.glob(f"{sim}/*/"))

            print(f"batch_names={batch_names}")

            for batch_name in batch_names:
                versions = sorted(glob.glob(f"{batch_name}/*/"), reverse=True)

                batches.append(
                    {
                        "simulation": sim.removesuffix("/").split("/")[-1],
                        "name": batch_name.removesuffix("/").split("/")[-1],
                        "versions": [
                            v.removesuffix("/").split("/")[-1] for v in versions
                        ],
                    }
                )

        return batches

    def get_batches_flat(self):
        batches = []
        simulations = sorted(glob.glob(f"{str(self.root_citros / 'data')}/*/"))
        for sim in simulations:
            if not Path(sim).is_dir():
                continue
            names = sorted(glob.glob(f"{sim}/*/"))
            _simulation = sim.removesuffix("/").split("/")[-1]
            for name in names:
                if not Path(name).is_dir():
                    continue
                versions = sorted(glob.glob(f"{name}/*/"), reverse=True)
                # print(versions)
                _name = name.removesuffix("/").split("/")[-1]
                try:
                    batch_hr_statu = json.loads((Path(name) / "hr.json").read_text())
                except:
                    batch_hr_statu = {"status": "UNLOADED"}

                for version in versions:
                    batch = json.loads((Path(version) / "info.json").read_text())
                    status = "UNLOADED"
                    if (
                        batch_hr_statu.get("version", None)
                        == version.removesuffix("/").split("/")[-1]
                    ):
                        status = batch_hr_statu.get("status")

                    batches.append(
                        {
                            "created_at": batch["created_at"],
                            "simulation": _simulation,
                            "name": _name,
                            "version": version.removesuffix("/").split("/")[-1],
                            "message": batch["message"],
                            f"status": status,
                            "completions": str(batch["completions"]),
                            "path": version,
                        }
                    )

                    # for printing.
                    _simulation = None
                    _name = None

        return batches
