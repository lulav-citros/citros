import os
import json
import logging
from pathlib import Path
from rich.logging import RichHandler

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
    def __init__(self, 
                 root, # the base recordings dir
                 simulation: Simulation, 
                 name : str ="citros",
                 mesaage: str ="CITROS is AWESOME!!!", 
                 index: int = -1, # default to take the last version of a runs
                 log=None):
        self.root = root
        if root is None or simulation is None:
            raise Exception("Error: root dir is None, batch needs is to operate")
        if simulation is None or simulation is None:
            raise Exception("Error: simulation is None, batch needs is to operate")
        
        now = datetime.today().strftime('%Y%m%d%H%M%S')
        
        self.batch_dir = Path(root) / simulation_name / batch_name
        self.batch_dir = os.path.join(root, simulation_name, batch_name)

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

        code, message = self._validate()
        if code == 404:
            raise NoBatchFoundException

        self.data = {
            "simulation": simulation_name,
            "name": batch_name,
            "message": "",
            "gpu": "",
            "cpu": "",
            "memory": "",
            "timeout": "",
            "commit": "",
            "branch": "",
            "storage_type": "MCAP",  # SQLITE, MCAP
            "completions": "",
            "parallelism": "",
            "status": "",
            "metadata": "",
            "data_last_access": "",
            "data_status": "UNLOADED",  # LOADED, UNLOADED, LOADING, ERROR
            "created_at": "",
            "updated_at": "",
        }

        self._load()

    def __str__(self):
        # print_json(data=self.data)
        return json.dumps(self.data, indent=4)

    ###################
    ##### private #####
    ###################
    
    # verify that the batch folder is ok:
    # - all json is correct.
    # - all files is intact.
    # - if files is signed check all signings (sha)
    def _validate(self):
        if os.path.exists(self.batch_dir) == False:
            return 404, "there is no folder for this batch."
        # TODO[critical]: add checks.
        return True, None

    def _new(self):
        
        pass
    
    
    def _load(self):
        batch_info = os.path.join(self.batch_dir, "info.json")

        try:
            with open(batch_info, "r") as file:
                batch_run = json.load(file)

                self.data.update(batch_run)
        except FileNotFoundError as e:
            self.log.error(f"no file for {batch_info}")
        except Exception as e:
            self.log.exception(e, self.data)

        # TODO[critical]: add all simulations to the batch {... simulations: [sim1, ...]}

    # start loading data to PG
    def load_data():
        pass

    ###################
    ##### public #####
    ###################
    def run(self, name, message, completions=1):
        #TODO: complete this
        self.simulation.run(
            name=name,
            message=message,
        )
        