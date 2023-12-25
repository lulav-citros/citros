import json
import yaml
import numpy
import shutil
import inspect
import importlib.util
import importlib_resources

from pathlib import Path

from .citros_obj import CitrosObj
from .utils import get_data_file_path, validate_dir
from citros.parsers import ParserRos2


class ParameterSetup(CitrosObj):
    """Object representing .citros/simulation.json file."""

    ##################
    ##### public #####
    ##################

    # overriding
    def path(self):
        return self.root_citros / "parameter_setups" / f"{self.file}"

    def render(self, destination, context={}):
        """
        Fetches parameters from CITROS, saves them to files, and returns the config.

        destination: the simulation recording folder.
        """
        self.log.debug(f"{self.__class__.__name__}._validate()")
        rendered_parameters = self._evaluate(context)

        self.log.debug("Saving parameters to files. ")
        self._save_rendered(rendered_parameters, destination)
        self.log.debug("Done saving config files.")

        return rendered_parameters

    ###################
    ##### private #####
    ###################

    # overriding
    def _validate(self):
        """Validate parameter_setup.json file."""
        self.log.debug(f"{'   '*self.level}{self.__class__.__name__}._validate()")

        success = validate_dir(
            self.root_citros / "parameter_setups", "schema_param_setup.json", self.log
        )

        return success

    # overriding
    def _new(self):
        self.log.debug(f"{'   '*self.level}{self.__class__.__name__}._new()")
        path = self.path()

        # avoid overwrite
        if path.exists():
            self._load()
            # return

        Path(self.root_citros / "parameter_setups").mkdir(parents=True, exist_ok=True)

        self.parser_ros2 = ParserRos2(self.log)
        # get default parameter setup and write it to file.
        default_parameter_setup = self.parser_ros2.generate_default_params_setup(
            self.citros
        )
        # self.data = default_parameter_setup | self.data
        self.data.update(default_parameter_setup)
        self._save()

        # copy functions
        destination = self.root_citros / "parameter_setups" / "functions"
        destination.mkdir(parents=True, exist_ok=True)

        if not (destination / "my_func.py").exists():  # avoid overwriting
            importlib_resources.files(f"data.sample_code").joinpath("my_func.py")

            with importlib_resources.files(f"data.sample_code").joinpath(
                "my_func.py"
            ) as md_file_path:
                shutil.copy2(md_file_path, destination / f"my_func.py")

            with importlib_resources.files(f"data.doc.folder").joinpath(
                "parameter_setups/functions/README.md"
            ) as md_file_path:
                shutil.copy2(md_file_path, destination / f"README.md")

        # TODO: when addeing a parameter to a package/node, add/append it to the parameter setups that use it.

    def _evaluate(self, context=None):
        """
        evalues self
        self.data = {
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

        print(result)  # Output: {"c": ..., "b": 8, "a": 5}
        """
        self.log.debug(f"{self.__class__.__name__}._evaluate(context={context})")

        def load_function(function_path, function_name):
            self.log.debug(
                f"function_path = {function_path}, function_name = {function_name}"
            )

            if not function_path.startswith("numpy"):
                self.log.debug("Loading user defined function.")
                spec = importlib.util.spec_from_file_location(
                    "user_module", function_path
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                function = getattr(module, function_name)
            else:
                self.log.debug("Loading numpy function.")
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
            parts = key.split(".")
            current_dict = self.data
            for part in parts:
                if part not in current_dict:
                    return False
                current_dict = current_dict[part]
            return True

        all_keys = collect_all_keys(self.data)
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
                    function_path = str(
                        self.citros.root_citros
                        / "parameter_setups"
                        / "functions"
                        / function_path
                    )

                function = load_function(function_path, function_name)
                # Check if function has a parameter named `context` and add it if so
                if value.get("args") is None:
                    value["args"] = []

                try:
                    if (
                        function_name is not None
                        and "context" in inspect.signature(function).parameters
                    ):
                        value["args"].append(context)
                except Exception as e:
                    self.log.exception(e)

                args = [evaluate_value(arg) for arg in value["args"]]

                result = function(*args)
                self.log.debug(
                    f"function = {function}, args = {args}, result = {result}"
                )

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
            elif isinstance(value, str) and (
                value in all_keys or is_valid_reference_key(value)
            ):
                if value in visited_keys:
                    raise ValueError(f"Circular dependency detected with key: {value}")
                visited_keys.add(value)
                result = evaluate_value(recursive_key_search(self.data, value))
                visited_keys.remove(value)
                return result

            # any other type
            else:
                return value

        # the actual work - recursively evaluate the values in the given dictionary.
        return evaluate_value(self.data)

    def _save_rendered(self, config, destination):
        # callback running inside ROS workspace context.
        from ament_index_python.packages import get_package_share_directory

        for package_name, citros_config in config["packages"].items():
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
                self.log.debug(
                    f"No config directory {path} exits for pack:{package_name}. passing."
                )
                continue

            path = Path(path, "params.yaml")

            # check if file exists
            if not Path(path).exists():
                self.log.debug(
                    f"No config file {path} exits for package: {package_name}. passing."
                )
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
            with open(path, "w") as file:
                yaml.dump(merged_config, file)

            # sanity check
            if destination is None:
                raise ValueError(f"citros_params.save_config: {destination} is None.")

            # save for metadata
            Path(destination, "config").mkdir(exist_ok=True)
            with open(Path(destination, "config", f"{package_name}.yaml"), "w") as file:
                yaml.dump(merged_config, file)
