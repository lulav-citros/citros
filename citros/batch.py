import os
import json
import logging
from pathlib import Path
from datetime import datetime
from rich import print, inspect, print_json
from rich.logging import RichHandler

from citros.utils import get_user_git_info

from .simulation import Simulation


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
class Batch:
    def __init__(
        self,
        root,  # the base recordings dir
        simulation,  # if type(simulation) str then it is the name of the simulation if type(simulation) Simulation then it is the simulation object
        name: str = "citros",
        mesaage: str = "CITROS is AWESOME!!!",
        index: int = -1,  # default to take the last version of a runs
        log=None,
    ):
        if root is None:
            raise Exception("Error: root dir is None, batch needs is to operate")
        if simulation is None:
            raise Exception("Error: simulation is None, batch needs is to operate")
        if type(simulation) is not str and not Simulation:
            raise Exception("Error: simulation is not a string or Simulation object")

        if log is None:
            logging.basicConfig(
                level=os.environ.get("LOGLEVEL", "INFO"),
                format="%(message)s",
                datefmt="[%X]",
                handlers=[RichHandler(rich_tracebacks=True)],
            )
            self.log = logging.getLogger(__name__)
        else:
            self.log = log

        self.root = root
        self.simulation = simulation
        self.name = name
        self.message = mesaage
        self.index = index

        simulation_name = simulation if type(simulation) is str else simulation.name
        now = datetime.today().strftime("%Y%m%d%H%M%S")

        self.batch_dir = Path(root) / simulation_name / name / now

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

    # verify that the batch folder is ok:
    # - all json is correct.
    # - all files is intact.
    # - if files is signed check all signings (sha)
    def _validate(self):
        return True, None

    def _new(self):
        
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
            "data_last_access": "",
            "data_status": "UNLOADED",  # LOADED, UNLOADED, LOADING, ERROR
            "created_at": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
        }

        self._save()

    def _save(self):
        self.data["updated_at"]: datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.path(), "w") as file:
            json.dump(self.data, file, indent=4, sort_keys=True)

    def _load(self):
        if not self.batch_dir.exists():
            raise NoBatchFoundException(f'No batch fount at "{self.batch_dir}"')

        batch_info = self.path()

        # TODO: use self.index to load the last batch run

        try:
            with open(batch_info, "r") as file:
                batch_run = json.load(file)

                self.data.update(batch_run)
        except FileNotFoundError as e:
            self.log.error(f"no file for {batch_info}")
        except Exception as e:
            self.log.exception(e, self.data)

        # TODO[critical]: add all simulations to the batch {... simulations: [sim1, ...]}

    ###################
    ##### public ######
    ###################
    def path(self):
        """return the full path to the current main file.

        default to ".citros/project.json"

        Returns:
            str: the full path to the current main file.
        """
        return self.batch_dir / "info.json"

    def run(
        self,        
        completions: int = 1,
        ros_domain_id: int = None,
        trace_context: str = None,
    ):
        print("batch.run")

        self["completions"] = completions
        self["status"] = "RUNNING"

        ret = self.simulation.run(self.batch_dir / "0", trace_context=trace_context, ros_domain_id=ros_domain_id)

        return ret
