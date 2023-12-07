import yaml
import json
import os
import numpy
from pathlib import Path
import importlib.util
import inspect


class citros_params():
    def __init__(self, citros):
        self.citros = citros
        self.log = citros.log
        self.CONFIG_FOLDER = None
   

    def save_config(self, config):  
        # callback running inside ROS workspace context.   
        from ament_index_python.packages import get_package_share_directory
                
        for package_name, citros_config in config['packages'].items():
            self.log.debug(f"Saving config for [{package_name}]")

            # TODO: add other method to get the package path
            path_to_package = None
            try:
                # get the path to the package install directory - the project must be sourced for it to work 
                path_to_package = get_package_share_directory(package_name)            
            except Exception as e:
                self.log.exception(e)
                continue                

            if not path_to_package:
                continue
                
            path = Path(path_to_package, "config")    
            
            # check if folder exists
            if not path.exists():
                self.log.debug(f"No config directory {path} exits for pack:{package_name}. passing.") 
                continue
                                                
            path = Path(path, "params.yaml")
            
            # check if file exists
            if not Path(path).exists():
                self.log.debug(f"No config file {path} exits for package: {package_name}. passing.") 
                continue
            
            with open(path, "r") as stream:
                try:    
                    default_config = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    self.log.exception(exc)
            
            # citros_config will overwrite default_config if the same key appears in both. 
            merged_config = {**default_config, **citros_config}
            self.log.debug(json.dumps(merged_config, indent=4))
            
            # override default values
            with open(path, 'w') as file:
                yaml.dump(merged_config, file)  

            # sanity check
            if self.CONFIG_FOLDER is None:
                raise ValueError(f"citros_params.save_config: CONFIG_FOLDER is None.")

            # save for metadata
            Path(self.CONFIG_FOLDER).mkdir(exist_ok=True)
            with open(Path(self.CONFIG_FOLDER, f"{package_name}.yaml"), 'w') as file:                                     
                yaml.dump(merged_config, file)         
    

    def init_params(self, simulation_name : str, sim_run_dir : str, run_id : int):
        """
        Fetches parameters from CITROS, saves them to files, and returns the config.
        """          
        self.CONFIG_FOLDER = os.path.join(sim_run_dir, 'config')

        if not simulation_name.endswith('.json'):
            simulation_name = simulation_name + '.json'

        with open(Path(self.citros.SIMS_DIR, simulation_name), 'r') as file:
            sim_data = json.load(file)

        param_setup = sim_data['parameter_setup']

        with open(Path(self.citros.PARAMS_DIR, param_setup), 'r') as file:
            param_setup_data = json.load(file)

        citros_context = {"run_id": run_id}

        processed_data = self.evaluate_dictionary(param_setup_data, citros_context)

        self.log.debug("Saving parameters to files. ")        
        self.save_config(processed_data)
        self.log.debug("Done saving config files.")      

        return processed_data
    

    def evaluate_dictionary(self, dictionary, citros_context=None):
        """
        example usage
        dictionary = {
            "c": {
                "function": "/path/to/user_defined_function.py:user_function",
                "args": ["a", "b"]
            },
            "b": {
                "function": "numpy.add",
                "args": ["a", 3]
            },
            "a": 5
        }

        result = evaluate_dictionary(dictionary)
        print(result)  # Output: {"c": ..., "b": 8, "a": 5}
        """

        def load_function(function_path, function_name):
            self.log.debug(f"function_path = {function_path}, function_name = {function_name}")

            if not function_path.startswith('numpy'):
                spec = importlib.util.spec_from_file_location("user_module", function_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                function = getattr(module, function_name)
            else:
                function = eval(function_path)
            return function

        def recursive_key_search(d, key):
            """
            Recursively search for a key within nested dictionaries.
            
            :param d: The dictionary to search.
            :param key: The key to search for. Can be multi-level e.g. "outer.inner".
            :return: The value corresponding to the given key or None if not found.
            """
            # If the key exists at this level of dictionary, return it
            if key in d:
                return d[key]
            
            # If key does not contain a ".", search for it recursively within
            # all nested dictionaries
            if "." not in key:
                for k, v in d.items():
                    if isinstance(v, dict):
                        item = recursive_key_search(v, key)
                        if item is not None:
                            return item
                        
            # If key contains a ".", split it and navigate the nested 
            # dictionaries accordingly.
            else:
                first, remainder = key.split(".", 1)
                if first in d and isinstance(d[first], dict):
                    return recursive_key_search(d[first], remainder)
                return None

        def collect_all_keys(dct):
            """
            Collect all keys from a nested dictionary.
            
            :param dct: The dictionary to extract keys from.
            :return: A set containing all keys in the dictionary, including nested keys.
            """
            keys = set(dct.keys())
            for value in dct.values():
                if isinstance(value, dict):
                    keys |= collect_all_keys(value)
            return keys
        
        def is_valid_reference_key(key):
            """
            Check if a given reference key is valid within a dictionary structure.
            
            :param key: The reference key to check. Can be multi-level e.g. "outer.inner".
            :return: True if valid, False otherwise.
            """
            parts = key.split('.')
            current_dict = dictionary
            for part in parts:
                if part not in current_dict:
                    return False
                current_dict = current_dict[part]
            return True

        all_keys = collect_all_keys(dictionary)
        visited_keys = set()  # For circular dependency checks

        def evaluate_value(value):
            """
            Recursively evaluate a value. If the value corresponds to a function, 
            it loads and executes the function. If the value is a dictionary or a list, 
            it recursively evaluates its contents. If the value is a string that references
            another key, it fetches the value for that key.
            
            :param value: The value to evaluate.
            :return: The evaluated result.
            """

            # the value is a dictionary representing a function to be executed
            if isinstance(value, dict) and "function" in value:
                function_detail = value["function"].split(":")
                if function_detail[0].startswith("numpy."):
                    function_path = function_detail[0]
                    function_name = None
                else:
                    # at this point function_path is only the file name.
                    function_path, function_name = function_detail
                    function_path = str(self.citros.PARAMS_FUNCTIONS_DIR / function_path)

                function = load_function(function_path, function_name)

                # Check if function has a parameter named `citros_context` and add it if so
                if function_name is not None and 'citros_context' in inspect.signature(function).parameters:
                    value["args"].append(citros_context)

                args = [evaluate_value(arg) for arg in value["args"]]
                result = function(*args)

                # convert numpy scalars to native scalars, if needed.
                if isinstance(result, (numpy.generic)):
                    return result.item()
                return result
            
            # regular dictionary
            elif isinstance(value, dict):
                return {k: evaluate_value(v) for k, v in value.items()}

            # list
            elif isinstance(value, list):
                return [evaluate_value(v) for v in value]

            # the value is a string representing a reference to another key
            elif isinstance(value, str) and (value in all_keys or is_valid_reference_key(value)):
                if value in visited_keys:
                    raise ValueError(f"Circular dependency detected with key: {value}")
                visited_keys.add(value)
                result = evaluate_value(recursive_key_search(dictionary, value))
                visited_keys.remove(value)
                return result

            # any other type
            else:
                return value

        # the actual work - recursively evaluate the values in the given dictionary. 
        return evaluate_value(dictionary)