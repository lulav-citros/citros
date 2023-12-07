import os
import json
import logging

from rich.logging import RichHandler

class NoBatchFoundException(Exception):
    def __init__(self, message="No batch found."):
        super().__init__(message)
    
class Batch:
    def __init__(self, root, simulation_name, batch_name, log=None):
        self.root = root
        if root is None or simulation_name is None or batch_name is None:
            raise Exception("root, simulation_name, batch_name cant be None.")
        self.batch_dir = os.path.join(root, simulation_name, batch_name)        
        
        if log is None:
            logging.basicConfig(
                level=os.environ.get("LOGLEVEL", "INFO"),
                format="%(message)s",
                datefmt="[%X]",
                handlers=[RichHandler(rich_tracebacks=True)]
            )
            self.log = logging.getLogger(__name__)
        else:
            self.log = log
                
        code, message = self._check_batch_run_folder_status()
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
            "storage_type": "MCAP", # SQLITE, MCAP
            
            "completions": "",
            "parallelism": "",
            
            "status": "",
            "metadata": "",
            
            "data_last_access": "",
            "data_status": "UNLOADED", # LOADED, UNLOADED, LOADING, ERROR
            
            "created_at": "",
            "updated_at": "",
        }
        
        self._extract_batch_run_from_folder()
    
    def __str__(self):
        # print_json(data=self.data)
        return json.dumps(self.data, indent=4)
    
    # verify that the batch folder is ok:
    # - all json is correct.
    # - all files is intact.
    # - if files is signed check all signings (sha)  
    def _check_batch_run_folder_status(self):
        if os.path.exists(self.batch_dir) == False:                        
            return 404, 'there is no folder for this batch.'
        # TODO[critical]: add checks. 
        return True, None
    
    def _extract_batch_run_from_folder(self):        
        batch_info = os.path.join(self.batch_dir, 'info.json')        
        
        try:
            with open(batch_info, 'r') as file:
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
