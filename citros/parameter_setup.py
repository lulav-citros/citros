import json
import shutil

from pathlib import Path

import importlib_resources
from citros.parsers import ParserRos2
from .citros_obj import CitrosObj
from .utils import get_data_file_path, validate_dir


class ParameterSetup(CitrosObj):
    """Object representing .citros/simulation.json file."""

    ##################
    ##### public #####
    ##################

    # overriding
    def path(self):
        return self.root_citros / "parameter_setups" / f"{self.file}"

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
        self.data = default_parameter_setup | self.data
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

            with importlib_resources.files(f"data.doc").joinpath(
                "parameter_setups/functions/README.md"
            ) as md_file_path:
                shutil.copy2(md_file_path, destination / f"README.md")

        # TODO: when addeing a parameter to a package/node, add/append it to the parameter setups that use it.
