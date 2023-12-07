import os
import sys
import json
import time
import shutil
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
from .citros_utils import citros_utils
from .citros_batch import citros_batch
from .citros_params import citros_params
from .citros_events import citros_events


class Citros:
    """
    The Citros class implements the frontend of the Citros CLI.
    It must be instantiated within a `with` block in order to prevent 
    resource leaks and unexpected behavior.
    """

    def __init__(self, root_dir=".", verbose=False, debug=False, on_init=False):    
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
        
        # the main dir that contains .citros folder
        self.root_dir: Path = None if self.config.ROOT_DIR is None else Path(self.config.ROOT_DIR) # USER_PROJ_DIR
        # path to .citros folder
        self.citros_dir: Path = None if self.root_dir is None else Path(self.root_dir, ".citros") # CITROS_REPO_DIR
        
        # if ROOT_DIR is provided we dont need to search for it. 
        if not self.root_dir:
            if on_init:
                # on initialization it is clear where .citros is going
                self.root_dir = Path(root_dir).expanduser().resolve()
                self.citros_dir = None if self.root_dir is None else Path(self.root_dir, ".citros")
                
                assert self.root_dir and self.root_dir.name != ".citros", "cannot create .citros inside .citros"
            else:
                # if not initializing then lets search for .citros in ancestors. 
                self.citros_dir = self.find_citros_in_ancestors(root_dir)
                if self.citros_dir is not None:
                    self.root_dir = self.citros_dir.parent            
                else:
                    # for commands that don't need initialization, e.g. login,
                    # it's ok that these paths remain uninitialized.
                    self.citros_dir = Path("UNINITIALIZED")
                    self.root_dir = Path("UNINITIALIZED")
        
        
        self.root_dir_routs = {
            "path": self.root_dir,
            "citros": {
                "path": self.citros_dir,
                "project": Path(self.citros_dir, "project.json"),
                "settings": Path(self.citros_dir, "settings.json"),
                "simulations": {
                    "path": Path(self.citros_dir, "simulations")
                },
                "parameters": {
                    "path": Path(self.citros_dir, "parameter_setups"),
                    "functions": {
                        "path": Path(self.citros_dir, "parameter_setups", "functions"),
                    }
                },
                "notebooks": {
                    "path": Path(self.citros_dir, "notebooks")
                },
                "reports": {
                    "path": Path(self.citros_dir, "reports")
                },
                "runs": {
                    "path": self.config.RECORDINGS_DIR if self.config.RECORDINGS_DIR is not None else Path(self.citros_dir, "runs")
                },
                "logs": {
                    "path": Path(self.config.CITROS_HOME_DIR, "logs")
                }
            }
        }

        # default files to copy
        self.md_files_and_destinations = [ \
            ('README_functions.md', self.root_dir_routs["citros"]["parameters"]["functions"]["path"]),
            ('README_notebooks.md', self.root_dir_routs["citros"]["notebooks"]["path"]),
            ('README_parameter_setups.md', self.root_dir_routs["citros"]["parameters"]["path"]),
            ('README_simulations.md', self.root_dir_routs["citros"]["simulations"]["path"]),            
            ('README_reports.md', self.root_dir_routs["citros"]["reports"]["path"])]

        # set via create_sim_run_dir, do not set directly
        self.SIM_RUN_DIR = None
        self.BAG_DIR = None
        self.MSGS_DIR = None

        # set via set_batch_name_and_message, do not set directly
        self._batch_name = ""
        self._batch_message = ""

        self._sim_name = None

        self.CITROS_ENVIRONMENT = config.CITROS_ENVIRONMENT

        self.log = None

        self.log_level = 'debug' if debug else 'info'
        
        self.set_logger(self.root_dir_routs["citros"]["logs"]["path"])
        
        self._init_components()

        self.systemStatsRecorder = SystemStatsRecorder(Path(self.SIM_RUN_DIR, 'metrics.csv'), self.config.STATS_INTERVAL)


    def _init_components(self):
        self.events = citros_events(self)        
        self.parser_ros2 = parser_ros2(self)       
        self.params = citros_params(self)
        self.utils = citros_utils(self)
        self.batch = citros_batch(self)


    def print(self, message, only_debug=False, only_verbose=False, color='default'):
        if (only_debug and self.log_level != 'debug') or \
           (only_verbose and not self.config.VERBOSE):
            return
        
        print(f"[{color}]{message}[/{color}]")


    def set_batch_name_and_message(self, batch_name, batch_message):
        with open(self.root_dir_routs["citros"]["settings"]["path"], 'r') as file:
            settings = json.load(file)

        if not batch_message and self.utils.str_to_bool(settings['force_message']):
            self.print("Please supply a batch message (-m <message>).", color='yellow')
            self.print("You may turn off mandating of batch message in settings.json")
            return False
        
        if not batch_name and self.utils.str_to_bool(settings['force_batch_name']):
            self.print("Please supply a batch name (-n <name>).", color='yellow')
            self.print("You may turn off mandating of batch name in settings.json")
            return False

        self._batch_name = batch_name
        self._batch_message = batch_message
        return True
    

    def check_batch_name(self):
        batch_name_idx = 1

        if not self._batch_name or not self.utils.is_valid_file_name(self._batch_name):
            self._batch_name = self.utils.get_foramtted_datetime()
            
        # avoid duplicate batch dir names
        elif Path(self.root_dir_routs["citros"]["runs"]["path"], self._sim_name, self._batch_name).exists():
            while Path(self.root_dir_routs["citros"]["runs"]["path"], self._sim_name, f"{self._batch_name}_{str(batch_name_idx)}").exists():
                batch_name_idx = batch_name_idx + 1
            self._batch_name = f"{self._batch_name}_{str(batch_name_idx)}"


    def set_logger(self, log_dir : Path, file_name='citros.log', batch_id=None, run_id=None):
        self._batch_id = batch_id
        self._run_id = run_id

        # log directory might not exist yet when calling from constructor
        if not Path(log_dir).exists():
            log_dir.mkdir(parents=True)

        on_cluster = self.CITROS_ENVIRONMENT == "CLUSTER"
        log_file = str(Path(log_dir, file_name))
        self.log = get_logger(f"{citros_meta.__title__}:{citros_meta.__version__}", 
                              self._batch_id, self._run_id, self.log_level, log_file, on_cluster)


    def handle_exceptions(self, e, exit=False):
        """
        Handles exceptions and logs them.

        Args:
        e: Exception to handle.
        """
        self.print(f'An exception was raised. See log file under {self.root_dir_routs["citros"]["logs"]["path"]} for details' + \
                   f" (or use the -d flag to log to the terminal).", color='red')
        stack_trace = traceback.format_exception(type(e), e, e.__traceback__)
        stack_trace_str = "".join(stack_trace)
        self.log.error(f"Exception details:{linesep}{stack_trace_str}")
        
        if exit:
            shutdown() # flush logger
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
            self.handle_exceptions(exc_val, exit=True)

        # commented out 10/8/2023 due to a hang on Gleb's computer.
        # self.check_latest_version()


    def find_citros_in_ancestors(self, proj_dir=""):
        current_dir = Path.cwd() if not proj_dir else Path(proj_dir).expanduser().resolve()

        # Ensure we don't go into an infinite loop at the root directory
        while current_dir != current_dir.parent:
            citros_dir = current_dir / ".citros"
            if citros_dir.exists():
                return citros_dir.expanduser().resolve()
            current_dir = current_dir.parent

        return None

    ####################### simulation attributes getters #####################

    def get_simulation_info(self, simulation_name : str):
        if not simulation_name.endswith('.json'):
            simulation_name = simulation_name + '.json'
            
        try:
            with open(Path(self.root_dir_routs["citros"]["simulations"]["path"], simulation_name), 'r') as f:
                data = json.load(f)
        except FileNotFoundError as ex:
            self.log.error(f"simulation file {simulation_name} does not exist.")
            raise ex

        return data


    def get_package_name(self, launch_name : str):
        with open(self.root_dir_routs["path"], 'r') as f:
            data = json.load(f)
            
        for package in data['packages']:
            for launch in package['launches']:
                if launch['name'] == launch_name:
                    package_path = package['path']
                    if Path(package_path, 'package.xml').exists():
                        return Path(package_path).name  
                    
        # If no matching launch or package is found
        return None

    ############################### .CITROS FOLDER DB #########################
    
    def get_simulations(self):
        path = self.root_dir_routs["citros"]["simulations"]["path"]
        sims = []
        if path.is_dir():
            if self._has_files(path):
                for file in path.iterdir():
                    if not str(file).endswith('.json'):
                        continue
                    sim = file.name.split('.')[0]
                    sims.append(sim)    
        return sims
    
    #################### initialization and validation ########################

    def _has_files(self, dir : Path):
        return any(p.is_file() for p in dir.iterdir()) 
    

    def _validate_json_file(self, json_filepath, schema_filepath, default_filepath):
        with open(json_filepath, 'r') as file:
            data = json.load(file)

        with open(schema_filepath, 'r') as file:
            schema = json.load(file)

        # not all validatable files have defaults (e.g. simulation setup).
        default = {}
        if default_filepath:
            with open(default_filepath, 'r') as file:
                default = json.load(file)

        try:
            # in order to support future changes in schemas (i.e. additional fields), 
            # we merge with the default, so any new fields will be added to the user's 
            # file and the validation will succeed.
            merged_dict = {**default, **data}
            jsonschema.validate(instance=merged_dict, schema=schema)
            self.print(f"{json_filepath} is valid.", only_verbose=True)
            
            if merged_dict != data:
                with open(json_filepath, 'w') as file:
                    file.write(json.dumps(merged_dict, indent=4))

            return True
        except jsonschema.exceptions.ValidationError as ve:
            self.log.error(f"{json_filepath} is not valid:{linesep}{ve}")
            return False


    def _copy_default_file(self, default_file_path, destination, override_existing=False):
        assert destination is not None
        if Path(destination).exists() and not override_existing:
            self.print(f"File {destination} already exists, avoiding override by default file.", only_verbose=True)
            return

        shutil.copy2(Path(default_file_path), destination)


    def _validate_file(self, file_path : Path, schema_file, default_file_name, copy_if_missing=False):
        default_filepath = None
        if default_file_name:
            with self.utils.get_data_file_path('defaults', default_file_name) as default_file:
                default_filepath = default_file
        
        if file_path.is_file():
            with self.utils.get_data_file_path('schemas', schema_file) as schema_path:
                return self._validate_json_file(str(file_path), schema_path, default_filepath)
        elif copy_if_missing:
            self._copy_default_file(default_filepath, file_path)
            return True
        else:
            return False


    def _validate_dir(self, path : Path, schema_file, default_file_name, copy_if_empty=False):
        default_filepath = None
        if default_file_name:
            with self.utils.get_data_file_path('defaults', default_file_name) as default_file:
                default_filepath = default_file

        if path.is_dir() and self._has_files(path):
            with self.utils.get_data_file_path('schemas', schema_file) as schema_path:
                for file in path.iterdir():
                    if str(file).endswith('json'):
                        if not self._validate_json_file(file, schema_path, default_filepath):
                            return False
                return True
        elif copy_if_empty:
            self._copy_default_file(default_filepath, Path(path, default_file_name))
            return True
        else:
            # empty folder is valid
            return True


    def _get_launches_info(self, proj_json: Path):
        with open(proj_json, 'r') as file:
            data = json.load(file)

        launch_info = []

        for package in data.get('packages', []):
            for launch in package.get('launches', []):
                if 'name' in launch:
                    launch_info.append((package.get('name', ''), launch['name']))
        
        return launch_info


    def _check_sim_file_contents(self, sim_file):
        with open(sim_file, 'r') as file:
            sim_data = json.load(file)

        param_setup = sim_data["parameter_setup"]
        launch_file = sim_data["launch"]["file"]
        
        if not Path(self.root_dir_routs["citros"]["parameters"]["path"], param_setup).exists():
            self.print(f"Could not find parameter setup file {param_setup} referenced in {sim_file}.", color='red')
            return False
        
        all_launch_names = [launch[1] for launch in self._get_launches_info(self.root_dir_routs["path"])]
        if launch_file not in all_launch_names:
            self.print(f"Could not find launch file named {launch_file} referenced in {sim_file}.", color='red')
            return False
        
        return True
                
    
    def _validate_citros_files(self, create_default_if_empty : bool):
        """
        Assumption: project.json exists.
        """
        success = self._validate_dir(self.root_dir_routs["citros"]["parameters"]["path"], 'schema_param_setup.json', None)
        
        success = success and \
                  self._validate_dir(self.root_dir_routs["citros"]["simulations"]["path"], 
                                    'schema_simulation.json', 
                                    'default_simulation.json',
                                    create_default_if_empty)

        success = success and \
                  self._validate_file(self.root_dir_routs["citros"]["settings"]["path"], 
                                     'schema_settings.json',
                                     'default_settings.json',
                                     True)
        return success


    def _create_folders(self):
        if not self.citros_dir.is_dir():
            self.citros_dir.mkdir(parents=True)

        if not self.root_dir_routs["citros"]["simulations"]["path"].is_dir():
            self.root_dir_routs["citros"]["simulations"]["path"].mkdir(parents=True)

        if not self.root_dir_routs["citros"]["parameters"]["path"].is_dir():
            self.root_dir_routs["citros"]["parameters"]["path"].mkdir(parents=True)

        if not self.root_dir_routs["citros"]["parameters"]["functions"]["path"].is_dir():
            self.root_dir_routs["citros"]["parameters"]["functions"]["path"].mkdir(parents=True)

        if not self.root_dir_routs["citros"]["notebooks"]["path"].is_dir():
            self.root_dir_routs["citros"]["notebooks"]["path"].mkdir(parents=True)

        if not self.root_dir_routs["citros"]["runs"]["path"].is_dir():
            self.root_dir_routs["citros"]["runs"]["path"].mkdir(parents=True)


        if not self.root_dir_routs["citros"]["reports"]["path"].is_dir():
            self.root_dir_routs["citros"]["reports"]["path"].mkdir(parents=True)


    def _get_project_name(self):
        proj_file_path = self.root_dir_routs["path"]
        if proj_file_path.exists():
            with open(proj_file_path, "r") as proj_file:
                proj_file_data = json.load(proj_file)
                return proj_file_data.get("name", "")
        
        # return user's project directory name by default
        return self.root_dir.name


    def _create_simulations(self):
        """
        create a default simulation.json for every launch file in the project.
        """
        if self.root_dir_routs["path"].exists():
            launch_infos = self._get_launches_info(self.root_dir_routs["path"])
            if not launch_infos:
                self.log.warning("No launch files found in user's project.")
                self.print("No launch files found. If you have launch files in your project, "  + \
                           "make sure they are of the form *.launch.py", color='yellow')
                return

            for package_name, launch_file in launch_infos:
                launch_name = launch_file.split('.')[0]

                sim_file_path = Path(self.root_dir_routs["citros"]["simulations"]["path"], f"simulation_{launch_name}.json")

                # avoid overwrite
                if sim_file_path.exists():
                    continue

                sim_file_path = str(sim_file_path)

                with self.utils.get_data_file_path('defaults', 'default_simulation.json') as default_file:
                    self._copy_default_file(default_file, sim_file_path)

                    with open(sim_file_path, 'r') as sim_file:
                        sim_json = json.load(sim_file)
                          
                    sim_json["launch"]["file"] = launch_file
                    sim_json["launch"]["package"] = package_name
                    
                    with open(sim_file_path, 'w') as sim_file:
                        json.dump(sim_json, sim_file, indent=4)


    def _create_gitignore(self):
        if not Path(self.citros_dir, '.gitignore').exists():
            with open(Path(self.citros_dir, '.gitignore'), 'w') as file:
                ignores = linesep.join(['runs/', 'auth', '__pycache__/']) # add more as needed.
                file.write(ignores)


    def get_ignore_list(self):
        if Path(self.citros_dir, '.citrosignore').exists():
            with open(Path(self.citros_dir, '.citrosignore'), 'r') as file:
                lines = [line.strip() for line in file if '#' not in line]
                self.log.debug(f".citrosignore contenrs: {lines}")
                return lines
        else:
            self.log.debug(f"Could not find .citrosignore in {self.citros_dir}")
            return []
    

    def _copy_examples_and_markdown(self):
        destination = self.root_dir_routs["citros"]["parameters"]["functions"]["path"]
        if not Path(destination, "my_func.py").exists(): # avoid overwriting
            with self.utils.get_data_file_path('sample_code', "my_func.py") as source_file_path:
                shutil.copy2(source_file_path, destination)

        destination = self.citros_dir
        if not Path(destination, ".citrosignore").exists(): # avoid overwriting
            with self.utils.get_data_file_path('misc', ".citrosignore") as source_file_path:
                shutil.copy2(source_file_path, destination)

        for file_destination_pair in self.md_files_and_destinations:
            with self.utils.get_data_file_path('markdown', file_destination_pair[0]) as md_file_path:
                destination = file_destination_pair[1]
                shutil.copy2(md_file_path, f"{destination}/README.md")


    def save_user_commit_hash(self):
        user_commit, _ = self.get_git_info(self.root_dir)

        with open(Path(self.citros_dir, 'user_commit'), 'w') as file:
            file.write(user_commit)


    def internal_sync(self, on_init=False):
        # no synching or validation is done on the cluster - there is no user code.
        if self.CITROS_ENVIRONMENT == 'CLUSTER':
            return True
        
        if on_init:
            self._create_gitignore()

        self._create_folders()

        self._copy_examples_and_markdown()
        
        self.sync_project(self._get_project_name())
            
        self._create_simulations()
        
        success = self._validate_citros_files(on_init)

        success = success and self.parser_ros2.check_user_defined_functions(self.root_dir_routs["citros"]["parameters"]["path"])

        at_least_one_sim = False

        for file in self.root_dir_routs["citros"]["simulations"]["path"].iterdir():
            if str(file).endswith('.json'):
                at_least_one_sim = True
                success = success and self._check_sim_file_contents(file)

        if not at_least_one_sim:
            self.log.error(f'No simulation file found in {self.root_dir_routs["citros"]["simulations"]["path"]}')
            self.print("You must supply at least one simulation file.", color='red')
            success = False

        self.save_user_commit_hash()

        return success


    def check_project(self, on_init=False):
        if self.citros_dir.exists():
            self.internal_sync(on_init)
            return True
        else:
            return False


    def sync_project(self, name):
        project_data = self.parser_ros2.parse(str(self.root_dir), name)
        with open(self.root_dir_routs["path"], 'w') as file:
            json.dump(project_data, file, sort_keys=True, indent=4)
        
        self.parser_ros2.generate_default_params_setup(self.root_dir_routs["path"], 
                                                       Path(self.root_dir_routs["citros"]["parameters"]["path"],
                                                            'default_param_setup.json'))

    def check_ros_build(self, project_path):
        package_paths = self.parser_ros2.get_project_package_paths(project_path)
        workspaces = set()
        for package_path in package_paths:
            src_dir = self.utils.find_ancestor_with_name(package_path, "src")
            if src_dir is None:
                msg = f"Unsupported project structure: package {package_path} is not under `src` folder."
                self.log.error(msg)
                self.print(msg, color='red')
                return False
            workspaces.add(Path(src_dir).parent)

        for ws in workspaces:
            if not any(p.is_dir() and p.name == "install" for p in ws.iterdir()):
                msg = f"Workspace {ws} has not been built."
                self.log.error(msg)
                self.print(msg, color='red')
                return False
            
        return True

    ############################## RUN ########################################
    
    def create_sim_run_dir(self, run_id):        
        run_dir = Path(self.root_dir_routs["citros"]["runs"], self._sim_name, self._batch_name, str(run_id))
        run_dir.mkdir(parents=True, exist_ok=False)
        self.SIM_RUN_DIR = str(run_dir)
        self.BAG_DIR = str(Path(self.SIM_RUN_DIR, 'bag'))
        self.MSGS_DIR = str(Path(self.SIM_RUN_DIR, 'msgs'))

        # in case the user needs access to SIM_RUN_DIR.
        os.environ['CITROS_SIM_RUN_DIR'] = self.SIM_RUN_DIR

        self.print(f"simulation run dir = [{self.SIM_RUN_DIR}]", only_verbose=True )

    def copy_msg_files(self):
        #sanity check
        if self.MSGS_DIR is None:
            self.log.error("MSG_DIRS has not been created.")
            return
        
        msg_paths = self.parser_ros2.get_msg_files(self.root_dir)
        for msg_path in msg_paths:
            # assuming msg files are under package_name/msg/
            package_name = Path(msg_path).parent.parent.name
            target_dir = Path(self.MSGS_DIR, package_name, 'msg')
            self.utils.copy_files([msg_path], str(target_dir), True)

    def get_bag_name(self):
        if self.config.STORAGE_TYPE == 'SQLITE3':
            return 'bag_0.db3'
        elif self.config.STORAGE_TYPE == 'MCAP':
            return 'bag_0.mcap'
        else:
            raise ValueError("Unknown storage type.")

    def save_run_info(self):
        bag_hash = self.utils.compute_sha256_hash(Path(self.BAG_DIR, self.get_bag_name()))
 
        batch = self.batch.get_batch(self._batch_id, self._sim_name)

        with open(Path(self.SIM_RUN_DIR).parent / 'info.json', 'w') as sim_file:
            json.dump(batch, sim_file, indent=4)

        batch['batchId'] = self._batch_id
        batch['bagHash'] = bag_hash
        batch['id'] = self._run_id

        with open(Path(self.SIM_RUN_DIR, 'info.json'), 'w') as sim_file:
            json.dump(batch, sim_file, indent=4)
        
    def is_inside_dev_container(self):
        return "REMOTE_CONTAINERS" in os.environ

    def save_system_vars(self):
        # Get all environment variables
        env_vars = dict(os.environ)
        
        pip_freeze_output = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
        
        if pip_freeze_output.returncode != 0:
            self.log.error('pip freeze failed: ' + pip_freeze_output.stderr)
            python_packages = []
        else:
            python_packages = pip_freeze_output.stdout.split(linesep)

        data = {'environment_variables' : env_vars,
                'python_packages' : python_packages
                }
        
        with open(Path(self.SIM_RUN_DIR, 'environment.json'), 'w') as f:
            json.dump(data, f, indent=4)

    def copy_ros_log(self):
        ros_logs_dir_path = self.utils.get_last_created_file(Path("~/.ros/log/").expanduser(), dirs=True)

        if ros_logs_dir_path is not None:
            log_file_path = Path(ros_logs_dir_path, 'launch.log')
            self.utils.copy_files([log_file_path], self.SIM_RUN_DIR)
            new_file_path = Path(self.SIM_RUN_DIR, log_file_path.name)
            self.utils.rename_file(new_file_path, "ros.log")
        else:
            self.log.warning(f"Failed to find the ros logs directory.")

    def copy_citros_log(self):
        log_file_path = Path(self.root_dir_routs["citros"]["logs"]["path"], "citros.log")
        self.utils.copy_files([log_file_path], self.SIM_RUN_DIR)

    def save_run_data(self):
        self.copy_msg_files()
        self.copy_citros_log()
        self.copy_ros_log()
        self.save_run_info()
        self.save_system_vars()


    def single_simulation_run(self, batch_id, run_id):   
        # running inside ROS workspace context.  
        from launch import LaunchService 
        from citros.launches import generate_launch_description  

        self.print(f" + + running simulation [{run_id}]", color='blue')  

        self.create_sim_run_dir(run_id)
        
        self.set_logger(self.SIM_RUN_DIR, 'citros_sim_launch.log', batch_id, run_id)

        if self.config.SUPPRESS_ROS_LAN_TRAFFIC:
            self.utils.suppress_ros_lan_traffic()

        launch_description = generate_launch_description(self)

        if launch_description is None:
            msg = f"Couldn\'t run run_id:[{run_id}]. Failed to create launch_description."
            self.log.error(msg)
            return
        
        launch_service = LaunchService(debug=(self.log_level == 'debug'))
        launch_service.include_launch_description(launch_description)
        
        self.systemStatsRecorder.start()
        
        ret = launch_service.run()
        
        self.systemStatsRecorder.stop()

        color = 'blue' if ret == 0 else 'red'
        self.print(f" - - Finished simulation run_id = [{run_id}] with return code [{ret}].", color=color) 

        self.save_run_data()
        
        if ret != 0:
            self.events.error(batch_id, run_id, message=f"Finished simulation. Return code = [{ret}].")
            self.events.on_shutdown()
            sys.exit(ret)
        else:
            self.events.done(batch_id, run_id, message=f"Finished simulation. Return code = [{ret}].")


    def run_batch(self, batch_id, completions, description=""):
        self.print(f" + running batch [{batch_id}], description: {description}, repeating simulations: [{completions}]", color='blue')

        for run_id in range(0, completions):
            try:
                self.single_simulation_run(batch_id, run_id)                   
                time.sleep(1)
            except Exception as e:
                self.print("------------------------")   
                self.print (e, color='red')
                traceback.print_exc()
                self.print("------------------------")
                continue

        self.print(f" - Finished [{batch_id}] batch.", color='blue')


    def run_simulation(self, sim_name, completions, remote, commit_hash, branch_name):   
        completions = int(completions)

        cpu = self.get_simulation_info(sim_name)['CPU']
        gpu = self.get_simulation_info(sim_name)['GPU']
        mem = self.get_simulation_info(sim_name)['MEM']
        timeout = self.get_simulation_info(sim_name)['timeout']
        
        storage_type = self.get_simulation_info(sim_name).get('storage_type', self.config.STORAGE_TYPE)
        
        user_commit, user_branch = self.get_git_info(self.root_dir)
        citros_commit, citros_branch = self.get_git_info(self.citros_dir)

        latest_tag = ""

        self._sim_name = sim_name
        self.check_batch_name()

        batch_id = self.batch.generate_batch_id()

        # start the open-telemetry trace.
        self.events.creating(batch_id)

        where = "locally" # if not remote else f"on Citros cluster. See {self.CITROS_URL}/{self._get_project_name()}/batch/{batch_id}"

        msg = f"created new batch_id: {batch_id}. Running {where}."
        self.log.info(msg)
        self.print(msg, color='blue')

        self.run_batch(batch_id, completions, self._batch_message)
