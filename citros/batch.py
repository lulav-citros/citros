import os
import glob
import json
import logging
from pathlib import Path
from datetime import datetime
from rich import print, inspect, print_json
from rich.logging import RichHandler

from citros.utils import get_user_git_info

from .simulation import Simulation
from .logger import get_logger, shutdown_log

from .batch_uploader import BatchUploader


class NoBatchFoundException(Exception):
    def __init__(self, message="No batch found."):
        super().__init__(message)


# * create new batch for running simulations
# to be able to run simulation Batch needs to have a simulation
# Batch(simulation : Simulation)


# * create new batch for reading data from previous runs
# To be able to interact with recorded batches
# Batch(path: Path, index: int) # path data/simulation/batch,
# index = -1 will get the latest batch run from this dir
# index = n will get the n's batch run
class Batch(BatchUploader):
    def __exit__(self):
        self.log.debug(
            f"{self.__class__.__name__}.__exit__()",
        )
        shutdown_log()

    def __init__(
        self,
        root,  # the base recordings dir
        simulation,  # if type(simulation) str then it is the name of the simulation if type(simulation) Simulation then it is the simulation object
        name: str = "citros",
        message: str = "CITROS is AWESOME!!!",
        index: int = -1,  # default to take the last version of a runs
        version=None,
        log=None,
        debug=False,
        verbose=False,
    ):
        self.debug = debug
        self.verbose = verbose

        if root is None:
            raise Exception("Error: root dir is None, batch needs is to operate")
        if simulation is None:
            raise Exception("Error: simulation is None, batch needs is to operate")
        if type(simulation) is not str and not Simulation:
            raise Exception("Error: simulation is not a string or Simulation object")

        self.root = root
        self.simulation = simulation
        self.name = name
        self.message = message
        self.version = version
        self.index = index

        self.simulation_name = (
            simulation if type(simulation) is str else simulation.name
        )

        self.batch_dir = Path(root) / self.simulation_name / name

        # get version
        if not version:  # no version specified
            if type(simulation) is Simulation:  # create new batch
                self.version = datetime.today().strftime("%Y%m%d%H%M%S")
            else:
                versions = sorted(glob.glob(f"{str(self.batch_dir)}/*/"))
                # get version from index
                version_path = versions[self.index]
                if version_path.endswith("/"):
                    version_path = version_path[:-1]

                self.version = version_path.split("/")[-1]

        # print(f"{self.simulation_name} / {name} / {self.version}")
        self.batch_dir = Path(root) / self.simulation_name / name / self.version

        self._init_log(log)

        self.log.debug(f"{self.__class__.__name__}.init()")
        self.log.debug(f"self.batch_dir:{str(self.batch_dir)}")

        self.data = {}

        # when simulation is a string then we are creating loading a batch from a path
        if type(simulation) is str:
            self._load()
        # when simulation is a Simulation then we are creating new batch and starting a simulations
        else:
            self._new()

        self._validate()

    def __str__(self):
        # print_json(data=self.data)
        return json.dumps(self.data, indent=4)

    def __getitem__(self, key):
        """get element from object

        Args:
            key (str): the element key

        Returns:
            str: the element value
        """
        return self.data[key]

    def get(self, key, default=None):
        """get element from object

        Args:
            key (str): the element key

        Returns:
            str: the element value
        """
        return self.data.get(key, default)

    def __setitem__(self, key, newvalue):
        self.data[key] = newvalue
        self._save()

    ###################
    ##### private #####
    ###################
    def _init_log(self, log=None):
        self.log = log
        if self.log is None:
            if type(self.simulation) is Simulation:  # creating new
                self.batch_dir.mkdir(parents=True, exist_ok=True)
                log_dir = self.batch_dir
            else:
                Path.home().joinpath(".citros/logs").mkdir(parents=True, exist_ok=True)
                log_dir = Path.home().joinpath(".citros/logs")

            self.log = get_logger(
                __name__,
                log_level=os.environ.get("LOGLEVEL", "DEBUG" if self.debug else "INFO"),
                log_file=str(log_dir / "citros.log"),
                verbose=self.verbose,
            )

    # verify that the batch folder is ok:
    # - all json is correct.
    # - all files is intact.
    # - if files is signed check all signings (sha)
    def _validate(self):
        # TODO[enhancement]: add validations
        return True, None

    def _new(self):
        self.log.debug(
            f"{self.__class__.__name__}._new()",
        )
        self.batch_dir.mkdir(parents=True, exist_ok=True)

        commit, branch = get_user_git_info(self.simulation.root)

        # inspect(self.simulation)
        self.data = {
            "simulation": self.simulation.name,
            "name": self.name,
            "message": self.message,
            "gpu": self.simulation["GPU"],
            "cpu": self.simulation["CPU"],
            "memory": self.simulation["MEM"],
            "timeout": self.simulation["timeout"],
            "commit": commit,
            "branch": branch,
            "storage_type": self.simulation["storage_type"],  # SQLITE, MCAP
            # will be filled at runtime
            "completions": "",
            "status": "",
            "metadata": "",
            "created_at": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
        }

        self._save()

    def _save(self):
        self.log.debug(
            f"{self.__class__.__name__}._save()",
        )
        self.data["updated_at"]: datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.path(), "w") as file:
            json.dump(self.data, file, indent=4, sort_keys=True)

    def _load(self):
        self.log.debug(
            f"{self.__class__.__name__}._load()",
        )
        if not self.batch_dir.exists():
            raise NoBatchFoundException(f'No batch fount at "{self.batch_dir}"')

        batch_info = self.path()

        self.log.debug(f"loading version: {batch_info}")

        try:
            with open(Path(batch_info), "r") as file:
                batch_run = json.load(file)

                self.data.update(batch_run)
        except FileNotFoundError as e:
            self.log.error(f"no file for {batch_info}")
        except Exception as e:
            self.log.exception(e, self.data)

    ###################
    ##### public ######
    ###################
    def path(self):
        """return the full path to the current main file.

        default to ".citros/project.json"

        Returns:
            str: the full path to the current main file.
        """
        # versions = sorted(glob.glob(f"{str(self.batch_dir)}/*"))
        # batch_version = versions[self.index]

        return self.batch_dir / "info.json"

    def simulation_run(
        self,
        sid: int,
        ros_domain_id: int = None,
        trace_context: str = None,
    ):
        self.log.debug(f"{self.__class__.__name__}.simulation_run()")
        self["status"] = "RUNNING"
        sim_dir = self.batch_dir / str(sid)
        # create log that will write to the simulation dir.
        ret = self.simulation.run(
            sim_dir, sid=sid, trace_context=trace_context, ros_domain_id=ros_domain_id
        )

        self.log.debug(f"{self.__class__.__name__}.run(): ret {ret}")
        return ret

    def run(
        self,
        completions: int = 1,
        sid: int = -1,  # the run id to complete. -1 -> run all
        ros_domain_id: int = None,
        trace_context: str = None,
    ):
        self.log.debug(f"{self.__class__.__name__}.run()")
        self["completions"] = completions

        if sid != -1:
            self.simulation_run(sid, ros_domain_id, trace_context)
            return
        for i in range(int(completions)):
            self.log.debug(f"run {i}")
            self.simulation_run(i, ros_domain_id, trace_context)
