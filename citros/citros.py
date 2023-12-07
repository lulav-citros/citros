import traceback
import jwt
import json
import traceback
import sys
import os
import git
import time
import shutil
import jsonschema
import subprocess
#import threading
import re
from python_on_whales import docker, exceptions
from datetime import datetime
from pathlib import Path
from decouple import config
from os import linesep
from contextlib import contextmanager

## graphQL
from gql import Client, gql
from gql.transport.exceptions import TransportQueryError
from gql.transport.requests import RequestsHTTPTransport

import requests 

from .citros_events import citros_events
from .citros_utils import citros_utils
from .citros_batch import citros_batch
from .parsers import parser_ros2
from .citros_params import citros_params
from .logger import get_logger, shutdown
import citros_meta


class Citros:
    """
    The Citros class implements the frontend of the Citros CLI.
    It must be instantiated within a `with` block in order to prevent 
    resource leaks and unexpected behavior.
    """

    def __init__(self, user_proj_dir=".", verbose=False, debug=False, on_init=False):    
        """
        Initialize Citros instance.

        Args:
        user_proj_dir:  optional user project directory, defaults to current 
                        working directory.
        verbose:        optionally turn on verbose console output.
        debug:          If True, sets log level to debug and turns on debug
                        output for the ROS simulation. Else, log level will 
                        be info, and debug output for the ROS simulation will 
                        not be given. Defaults to False.
        """
        self.VERBOSE = verbose
        self.STATS_INTERVAL = 1       # seconds
        self.STORAGE_TYPE = 'SQLITE3' # default to sqlite3
        self.SUPPRESS_ROS_LAN_TRAFFIC = True

        self.USER_TEMPLATE_DIR = Path("INVALID_PATH")

        # on the cluster, the .citros dir is a volume, 
        # and its path is given by an environment variable.
        # Also, there is no `USER_PROJ_DIR` since the user's 
        # image does not include the source, only the install 
        # and build directories.
        if 'CITROS_DIR' in os.environ:
            self.CITROS_REPO_DIR = Path(os.environ["CITROS_DIR"])
            self.USER_PROJ_DIR = Path("INVALID_PATH")
            self.is_initialized = True
        else:
            if on_init:
                self.USER_PROJ_DIR = Path(user_proj_dir).expanduser().resolve()
                self.CITROS_REPO_DIR = Path(self.USER_PROJ_DIR, ".citros")
                self.USER_TEMPLATE_DIR = Path(self.USER_PROJ_DIR, "citros_template")
                assert self.USER_PROJ_DIR.name != ".citros", "cannot create .citros inside .citros"
            else:
                self.CITROS_REPO_DIR = self.find_citros_in_ancestors(user_proj_dir)
                self.is_initialized = self.CITROS_REPO_DIR is not None and \
                                      (Path(self.CITROS_REPO_DIR, ".git")).exists()
                if self.is_initialized:
                    self.USER_PROJ_DIR = self.CITROS_REPO_DIR.parent
                else:
                    # for commands that don't need initialization, e.g. login,
                    # it's ok that these paths remain uninitialized.
                    self.CITROS_REPO_DIR = Path("UNINITIALIZED")
                    self.USER_PROJ_DIR = Path("UNINITIALIZED")

        self.CITROS_HOME_DIR = Path.home() / ".citros"

        self.alternate_auth_paths = [self.CITROS_HOME_DIR / "auth", 
                                     Path("/var/lib/citros/auth")]

        self.PROJECT_FILE = Path(self.CITROS_REPO_DIR, "project.json")
        self.SETTINGS_FILE = Path(self.CITROS_REPO_DIR, "settings.json")
        self.REPO_ID_FILE = Path(self.CITROS_REPO_DIR, "citros_repo_id")

        # subdirs
        self.SIMS_DIR = Path(self.CITROS_REPO_DIR, "simulations")
        self.PARAMS_DIR = Path(self.CITROS_REPO_DIR, "parameter_setups")
        self.PARAMS_FUNCTIONS_DIR = Path(self.PARAMS_DIR, "functions")
        self.NOTEBOOKS_DIR = Path(self.CITROS_REPO_DIR, "notebooks")
        self.WORKFLOWS_DIR = Path(self.CITROS_REPO_DIR, "workflows")
        self.RUNS_DIR = Path(self.CITROS_REPO_DIR, "runs")
        self.FOXGLOVE_DIR = Path(self.CITROS_REPO_DIR, "foxglove")
        self.REPORTS_DIR = Path(self.CITROS_REPO_DIR, "reports")

        self.CLI_LOGS_DIR = Path(self.CITROS_HOME_DIR, "logs")

        self.md_files_and_destinations = [ \
            ('README_functions.md', self.PARAMS_FUNCTIONS_DIR),
            ('README_notebooks.md', self.NOTEBOOKS_DIR),
            ('README_parameter_setups.md', self.PARAMS_DIR),
            ('README_simulations.md', self.SIMS_DIR),
            ('README_workflows.md', self.WORKFLOWS_DIR),
            ('README_foxglove.md', self.FOXGLOVE_DIR),
            ('README_reports.md', self.REPORTS_DIR)]

        # A list of files that will always be taken from the current branch 
        # during merges, thereby avoiding merge conflicts. Add more as needed.
        self._files_to_keep_ours = ['project.json', 'user_commit'] 

        self.is_local_init = False

        self._user = None
        # do not access directly, only via get/set token.
        self._jwt_token = None
        
        # GQL
        self._gql_client = None
        self._token_changed = False
        
        # for logger. do not set directly, only via set_logger
        self._batch_id = None
        self._run_id = None

        # set via create_sim_run_dir, do not set directly
        self.SIM_RUN_DIR = None
        self.BAG_DIR = None
        self.MSGS_DIR = None

        # set via set_batch_name_and_message, do not set directly
        self._batch_name = ""
        self._batch_message = ""

        self._sim_name = None

        self.CITROS_ENVIRONMENT = config("CITROS_ENVIRONMENT", "LOCAL")
        self.DOCKER_REGISTRY = config("DOCKER_REGISTRY", "us-central1-docker.pkg.dev/citros")
        
        # internal communication is via http
        url_prefix = "http" if self.CITROS_ENVIRONMENT == "CLUSTER" else "https"

        self.CITROS_DOMAIN = config("CITROS_DOMAIN", "citros.io")
        self.CITROS_URL = f"{url_prefix}://{self.CITROS_DOMAIN}"
        self.CITROS_GIT_USER = config("CITROS_GIT_USER", "git")
        self.CITROS_GIT_DOMAIN = config("CITROS_GIT_DOMAIN", self.CITROS_DOMAIN)
        self.CITROS_GIT_URL = f"{self.CITROS_GIT_USER}@{self.CITROS_GIT_DOMAIN}"
        
        self.print(f"--- using CITROS_URL = {self.CITROS_URL}", only_verbose=True)
        self.print(f"--- using CITROS_GIT_URL = {self.CITROS_GIT_URL}", only_verbose=True)
        
        self.CITROS_ENTRYPOINT = f"{self.CITROS_URL}/api/graphql"
        self.CITROS_LOGS = f"{self.CITROS_URL}/api/logs"        
        self.CITROS_GTOKEN = f"{self.CITROS_URL}/api/gtoken" 
        self.CITROS_HEALTH_CHECK = f"{self.CITROS_URL}/api/check" 
        
        self.OPEN_TELEMETRY_URL = config("OPEN_TELEMETRY_URL", "localhost:3417")

        self.CITROS_NETWORK_CHECK_URL = config("CITROS_NETWORK_CHECK_URL", "http://www.google.com")

        self.log = None

        self.log_level = 'debug' if debug else 'info'
        self.set_logger(self.CLI_LOGS_DIR)
        
        self._init_components()

        self.repo_id = None
        if self.REPO_ID_FILE.exists():
            with open(self.REPO_ID_FILE, 'r') as file:
                self.repo_id = file.read()


    

    def _init_components(self):
        self.events = citros_events(self)        
        self.parser_ros2 = parser_ros2(self)       
        self.params = citros_params(self)
        self.utils = citros_utils(self)
        self.batch = citros_batch(self)


    def print(self, message, only_debug=False, only_verbose=False, color='default'):
        if (only_debug and self.log_level != 'debug') or \
           (only_verbose and not self.VERBOSE):
            return
        
        default = Citros.COLORS['default']
        color = Citros.COLORS[color]
        if color is None:
            color = default
        
        print(f"{color}{message}{default}")


    def set_batch_name_and_message(self, batch_name, batch_message):
        with open(self.SETTINGS_FILE, 'r') as file:
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
        elif Path(self.RUNS_DIR, self._sim_name, self._batch_name).exists():
            while Path(self.RUNS_DIR, self._sim_name, f"{self._batch_name}_{str(batch_name_idx)}").exists():
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
        self.print(f"An exception was raised. See log file under {self.CLI_LOGS_DIR} for details" + \
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

        self.utils.stop_collecting_stats()

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
            with open(Path(self.SIMS_DIR, simulation_name), 'r') as f:
                data = json.load(f)
        except FileNotFoundError as ex:
            self.log.error(f"simulation file {simulation_name} does not exist.")
            raise ex

        return data

    def get_package_name(self, launch_name : str):
        with open(self.PROJECT_FILE, 'r') as f:
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
        path = self.SIMS_DIR
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
        
        if not Path(self.PARAMS_DIR, param_setup).exists():
            self.print(f"Could not find parameter setup file {param_setup} referenced in {sim_file}.", color='red')
            return False
        
        all_launch_names = [launch[1] for launch in self._get_launches_info(self.PROJECT_FILE)]
        if launch_file not in all_launch_names:
            self.print(f"Could not find launch file named {launch_file} referenced in {sim_file}.", color='red')
            return False
        
        return True
                
    
    def _validate_citros_files(self, create_default_if_empty : bool):
        """
        Assumption: project.json exists.
        """
        success = self._validate_dir(self.PARAMS_DIR, 'schema_param_setup.json', None)
        
        success = success and \
                  self._validate_dir(self.SIMS_DIR, 
                                    'schema_simulation.json', 
                                    'default_simulation.json',
                                    create_default_if_empty)

        success = success and \
                  self._validate_dir(self.WORKFLOWS_DIR, 
                                    'schema_flow.json', 
                                    'default_flow.json',
                                    create_default_if_empty)
        
        success = success and \
                  self._validate_file(self.SETTINGS_FILE, 
                                     'schema_settings.json',
                                     'default_settings.json',
                                     True)
        return success


    def _create_folders(self):
        if not self.CITROS_REPO_DIR.is_dir():
            self.CITROS_REPO_DIR.mkdir(parents=True)

        if not self.SIMS_DIR.is_dir():
            self.SIMS_DIR.mkdir(parents=True)

        if not self.PARAMS_DIR.is_dir():
            self.PARAMS_DIR.mkdir(parents=True)

        if not self.PARAMS_FUNCTIONS_DIR.is_dir():
            self.PARAMS_FUNCTIONS_DIR.mkdir(parents=True)

        if not self.NOTEBOOKS_DIR.is_dir():
            self.NOTEBOOKS_DIR.mkdir(parents=True)

        if not self.WORKFLOWS_DIR.is_dir():
            self.WORKFLOWS_DIR.mkdir(parents=True)

        if not self.RUNS_DIR.is_dir():
            self.RUNS_DIR.mkdir(parents=True)

        if not self.FOXGLOVE_DIR.is_dir():
            self.FOXGLOVE_DIR.mkdir(parents=True)

        if not self.REPORTS_DIR.is_dir():
            self.REPORTS_DIR.mkdir(parents=True)


    def _get_project_name(self):
        proj_file_path = self.PROJECT_FILE
        if proj_file_path.exists():
            with open(proj_file_path, "r") as proj_file:
                proj_file_data = json.load(proj_file)
                return proj_file_data.get("name", "")
        
        # return user's project directory name by default
        return self.USER_PROJ_DIR.name


    def _create_simulations(self):
        """
        create a default simulation.json for every launch file in the project.
        """
        if self.PROJECT_FILE.exists():
            launch_infos = self._get_launches_info(self.PROJECT_FILE)
            if not launch_infos:
                self.log.warning("No launch files found in user's project.")
                self.print("No launch files found. If you have launch files in your project, "  + \
                           "make sure they are of the form *.launch.py", color='yellow')
                return

            for package_name, launch_file in launch_infos:
                launch_name = launch_file.split('.')[0]

                sim_file_path = Path(self.SIMS_DIR, f"simulation_{launch_name}.json")

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
        if not Path(self.CITROS_REPO_DIR, '.gitignore').exists():
            with open(Path(self.CITROS_REPO_DIR, '.gitignore'), 'w') as file:
                ignores = linesep.join(['runs/', 'auth', '__pycache__/']) # add more as needed.
                file.write(ignores)


    def get_ignore_list(self):
        if Path(self.CITROS_REPO_DIR, '.citrosignore').exists():
            with open(Path(self.CITROS_REPO_DIR, '.citrosignore'), 'r') as file:
                lines = [line.strip() for line in file if '#' not in line]
                self.log.debug(f".citrosignore contenrs: {lines}")
                return lines
        else:
            self.log.debug(f"Could not find .citrosignore in {self.CITROS_REPO_DIR}")
            return []
    

    def _copy_examples_and_markdown(self):
        destination = self.PARAMS_FUNCTIONS_DIR
        if not Path(destination, "my_func.py").exists(): # avoid overwriting
            with self.utils.get_data_file_path('sample_code', "my_func.py") as source_file_path:
                shutil.copy2(source_file_path, destination)

        destination = self.CITROS_REPO_DIR
        if not Path(destination, ".citrosignore").exists(): # avoid overwriting
            with self.utils.get_data_file_path('misc', ".citrosignore") as source_file_path:
                shutil.copy2(source_file_path, destination)

        for file_destination_pair in self.md_files_and_destinations:
            with self.utils.get_data_file_path('markdown', file_destination_pair[0]) as md_file_path:
                destination = file_destination_pair[1]
                shutil.copy2(md_file_path, f"{destination}/README.md")


    def copy_user_templates(self):
        if self.USER_TEMPLATE_DIR.exists():
            self.utils.copy_subdir_files(self.USER_TEMPLATE_DIR, self.CITROS_REPO_DIR)


    def save_user_commit_hash(self):
        user_commit, _ = self.get_git_info(self.USER_PROJ_DIR)

        with open(Path(self.CITROS_REPO_DIR, 'user_commit'), 'w') as file:
            file.write(user_commit)


    def create_gitkeep_in_empty_dirs(self, ignored = []):
        for root, dirs, files in os.walk(str(self.CITROS_REPO_DIR)):
            if not dirs and not files and not root in ignored:
                gitkeep_file = Path(root, '.gitkeep')
                open(gitkeep_file, 'a').close()


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

        success = success and self.parser_ros2.check_user_defined_functions(self.PARAMS_DIR)

        at_least_one_sim = False

        for file in self.SIMS_DIR.iterdir():
            if str(file).endswith('.json'):
                at_least_one_sim = True
                success = success and self._check_sim_file_contents(file)

        if not at_least_one_sim:
            self.log.error(f"No simulation file found in {self.SIMS_DIR}")
            self.print("You must supply at least one simulation file.", color='red')
            success = False

        self.create_gitkeep_in_empty_dirs([str(self.RUNS_DIR)])

        self.save_user_commit_hash()

        return success


    def check_project(self, on_init=False):
        if self.CITROS_REPO_DIR.exists():
            self.internal_sync(on_init)
            return True
        else:
            return False


    def sync_project(self, name):
        project_data = self.parser_ros2.parse(str(self.USER_PROJ_DIR), name)
        with open(self.PROJECT_FILE, 'w') as file:
            json.dump(project_data, file, sort_keys=True, indent=4)
        
        self.parser_ros2.generate_default_params_setup(self.PROJECT_FILE, 
                                                       Path(self.PARAMS_DIR,
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
        runs_dir = self.RUNS_DIR if self.CITROS_ENVIRONMENT != "CLUSTER" else \
                   Path("/var/lib/citros/runs")

        run_dir = Path(runs_dir, self._sim_name, self._batch_name, str(run_id))
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
        
        msg_paths = self.parser_ros2.get_msg_files(self.USER_PROJ_DIR)
        for msg_path in msg_paths:
            # assuming msg files are under package_name/msg/
            package_name = Path(msg_path).parent.parent.name
            target_dir = Path(self.MSGS_DIR, package_name, 'msg')
            self.utils.copy_files([msg_path], str(target_dir), True)


    def get_bag_name(self):
        if self.STORAGE_TYPE == 'SQLITE3':
            return 'bag_0.db3'
        elif self.STORAGE_TYPE == 'MCAP':
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
        log_file_path = Path(self.CLI_LOGS_DIR, "citros.log")
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

        if self.SUPPRESS_ROS_LAN_TRAFFIC:
            self.utils.suppress_ros_lan_traffic()

        launch_description = generate_launch_description(self)

        if launch_description is None:
            msg = f"Couldn\'t run run_id:[{run_id}]. Failed to create launch_description."
            self.log.error(msg)
            return
        
        launch_service = LaunchService(debug=(self.log_level == 'debug'))
        launch_service.include_launch_description(launch_description)

        self.utils.start_collecting_stats(self.STATS_INTERVAL, Path(self.SIM_RUN_DIR, 'metrics.csv'))
        
        ret = launch_service.run()

        self.utils.stop_collecting_stats()

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


    def run_simulation_by_k8s(self, batch_id, run_id):
        """
        Used by the the Kubernetes cluster to run a single simulation run.
        Kubernetes runs this function as a `job`, a given number of times.
        The environment variable JOB_COMPLETION_INDEX will hold the index 
        of the current run (run_id). The command Kubernetes runs is:
        citros run <batch_id> JOB_COMPLETION_INDEX 
        This is how looping over all the batch runs is implemented on the cluster.
        
        Assumption: user is logged in, so we can query the db to get the 
                    simulation name given the batch_id.
        """
        if run_id == "JOB_COMPLETION_INDEX":
            run_id = config("JOB_COMPLETION_INDEX", "bad-value-from-k8s")
            self.log.info(f"got JOB_COMPLETION_INDEX={run_id} from k8s.")
        else:
            raise Exception("run_simulation_by_k8s: Expected run_id to be JOB_COMPLETION_INDEX")

        if run_id == "bad-value-from-k8s":
            raise Exception("run_simulation_by_k8s: bad value from k8s")
        
        # raise if not logged in
        batch = self.batch.get_batch(batch_id)

        # raise on error
        self.events.otlp_context = batch["metadata"]
        self._sim_name = str(batch["simulation"])
        self.STORAGE_TYPE = str(batch["storageType"])

        self.check_batch_name()
        
        self.log.info(f"running a single simulation run from batch [{batch_id}]")
        self.single_simulation_run(batch_id, run_id)


    def run_simulation(self, sim_name, completions, remote, commit_hash, branch_name):   
        completions = int(completions)

        cpu = self.get_simulation_info(sim_name)['CPU']
        gpu = self.get_simulation_info(sim_name)['GPU']
        mem = self.get_simulation_info(sim_name)['MEM']
        timeout = self.get_simulation_info(sim_name)['timeout']
        
        self.STORAGE_TYPE = self.get_simulation_info(sim_name)['storage_type']
        
        user_commit, user_branch = self.get_git_info(self.USER_PROJ_DIR)
        citros_commit, citros_branch = self.get_git_info(self.CITROS_REPO_DIR)

        latest_tag = ""

        if remote:
            if not self.repo_id: # sanity check
                raise Exception("run_simulation: repo id is None")
            
            if commit_hash:
                user_commit = commit_hash
            if branch_name:
                user_branch = branch_name

            latest_tag = user_commit

            if not self.check_docker_image_uploaded(user_commit):
                self.print(f"No docker image has been uploaded for user commit {user_commit}.", color='yellow')
                latest_tag = self.get_latest_docker_image_tag(user_branch)
                
                if latest_tag is None:
                    raise Exception("Failed getting latest image tag. Have you uploaded at least one docker image?")
                    
                self.print(f"image with tag {latest_tag} will be run instead", color='yellow')
                self.print(f"To run an image with your latest commit, run `citros docker-build-push` first.", color='yellow')

        self._sim_name = sim_name
        self.check_batch_name()

        batch_id = self.batch.generate_batch_id()

        # start the open-telemetry trace.
        self.events.creating(batch_id)

        where = "locally" if not remote else \
                f"on Citros cluster. See {self.CITROS_URL}/{self._get_project_name()}/batch/{batch_id}"

        msg = f"created new batch_id: {batch_id}. Running {where}."
        self.log.info(msg)
        self.print(msg, color='blue')

        # create a new batch for this simulation. 
        # if remote is True, than the query to the db will trigger the Kubernetes 
        # worker to start the simulation on the cluster.
        if remote:
            batch_id = self.batch.create_batch(batch_id, self.repo_id, sim_name, gpu, cpu, mem, 
                                               self.STORAGE_TYPE, completions, user_commit, user_branch, 
                                               citros_commit, citros_branch, latest_tag, timeout, name=self._batch_name, 
                                               message=self._batch_message, parallelism=completions, 
                                               metadata=self.events.otlp_context)
            return
        
        self.run_batch(batch_id, completions, self._batch_message)


    def check_docker_image_uploaded(self, user_commit):  
        proj_name = self._get_project_name()
        images_url = f"https://citros.io/api/artifactory/{proj_name}/{user_commit}"
             
        resp_data = self.request_image_tags(images_url)

        if resp_data is None: 
            return False
        
        try:
            err = resp_data.get('error', None)
            if err != None:
                if err == 'NOT_FOUND':
                    return False
                else:
                    self.log.error(f"request_image_tags returned: {resp_data}")
                    return False
            
            for name_version_pair in resp_data['relatedTags']:
                img_name = name_version_pair['name']
                if user_commit in img_name:
                    return True

            return False
        
        except Exception as ex:
            self.handle_exceptions(ex)
            return False
        

    def get_latest_docker_image_tag(self, branch_name):  
        proj_name = self._get_project_name()
        images_url = f"https://citros.io/api/artifactory/{proj_name}/branch.{branch_name}"
             
        resp_data = self.request_image_tags(images_url)

        if resp_data is None: 
            return None
        
        try:
            for img in resp_data:
                for name_version_pair in img['relatedTags']:
                    img_name = str(name_version_pair['name'])
                    tag = img_name.split('/')[-1]
                    if tag != "latest" and not 'branch.' in tag:
                        return tag

            self.log.error(f"Could not find latest hash in branch {branch_name}")
            return None
        
        except Exception as ex:
            self.handle_exceptions(ex)
            return None
        

    def request_image_tags(self, images_url):
        if not self.isAuthenticated():
            self.print("User is not logged in. Please log in first.", color='yellow')
            return None

        try:
            resp = requests.post(images_url, headers={
                "Authorization": f"Bearer {self._get_token()}"
            })
            resp.raise_for_status()     
            resp_data = resp.json()
        except requests.HTTPError as ex:
            self.log.error(f"HTTP error occurred: {images_url}")
            self.handle_exceptions(ex)
            return None
        except requests.RequestException as ex:
            self.log.error(f"A network error occurred: {images_url}")
            self.handle_exceptions(ex)
            return None
        except json.JSONDecodeError as ex:
            self.log.error(f"Failed to decode JSON response: {images_url}")
            self.handle_exceptions(ex)
            return None
        
        return resp_data