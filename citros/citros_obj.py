import os
import json
import logging
from pathlib import Path
from rich.logging import RichHandler
from rich import print, inspect, print_json
# import logger
from .logger import get_logger, shutdown_log


class CitrosException(Exception):
    def __init__(self, message="Simulation exception."):
        super().__init__(message)


class CitrosNotFoundException(CitrosException):
    def __init__(self, message="No batch found."):
        super().__init__(message)


class FileNotFoundException(CitrosException):
    def __init__(self, message="No batch found."):
        super().__init__(message)


class NoValidException(CitrosException):
    def __init__(self, message="No batch found."):
        super().__init__(message)


class CitrosObj:
    """Object representing .citros/*.json filew."""

    #####################
    ##### overrides #####
    #####################
    def __init__(
        self,
        name: str,
        root=None,
        new=False,
        log=None,
        citros=None,
        verbose=False,
        debug=False,
        level=0,
    ):
        """CITROS object is a folder and a set of json file that is located in the .citros folder

        Args:
            root (str): the root path to the `parent` of .citros folder
            name (str): the name of the pbject file
            new (bool, optional): will create new object if true. Defaults to False.
            log (logging, optional): log. Defaults to None.
            citros (CitrosObj, optional): the main citros object that represent "project.json" file. Defaults to None.

        Raises:
            CitrosException: _description_
        """
        self.verbose = verbose
        self.debug = debug
        self.level = level

        self.name = name
        if name.endswith(".json"):
            self.name = name[:-5]
        self.file = self.name + ".json"

        if root is None:
            raise CitrosException(f'root cant be "{root}"')
        if name is None:
            raise CitrosException(f'name cant be "{name}"')

        self.new = new

        # self.root = the path to the parent of .citros object.
        # self.root = Path.cwd() if root is None else Path(root).expanduser().resolve()
        # self.root = self._find_citros_in_ancestors(new=new)
        self.root = Path.cwd() if root is None else Path(root).expanduser().resolve()

        # path to .citros folder
        self.root_citros = self.root / ".citros"

        self._init_log(log)
        
        self.log.debug(
            f"{'   '*level}{self.__class__.__name__}.init(name={self.name}, new={new})",
        )
        
        # holds tha main citros object.
        self.citros = citros
        if citros is None:
            self.citros = self

        self.data = {}
        if self.new:
            if self.path().exists():
                self._load()
            else:
                self._new()
        else:
            self._load()

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
        self.save()

    ###################
    ##### private #####
    ###################
    def _init_log(self, log=None):
        self.log = log
        if self.log is None:
            log_dir = self.root_citros / "logs"
            if self.new:
                log_dir.mkdir(parents=True, exist_ok=True)
            else:
                if not log_dir.exists():
                    Path.home().joinpath(".citros/logs").mkdir(parents=True, exist_ok=True)
                    log_dir = Path.home().joinpath(".citros/logs")                    
            
            self.log = get_logger(
                __name__,
                log_level=os.environ.get("LOGLEVEL", "DEBUG" if self.debug else "INFO"),
                log_file=str(log_dir / "citros.log"),
                verbose=self.verbose
            )        
            
    def _validate(self) -> bool:
        """Validate .json file."""
        raise NoValidException()

    def _save(self):
        """Save .json file."""

        # print("_save self.path()", self.path())
        with open(self.path(), "w") as file:
            json.dump(self.data, file, indent=4, sort_keys=True)

    def _create(self):
        """_summary_
            this should be idempotent function:
                can be applied multiple times without changing the result
            if file exists -> check and append values if needded
            else -> create new file

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    def _load(self):
        if not Path(self.root_citros).exists():
            raise CitrosNotFoundException(f'"{self.root_citros}" does not exist.')

        if not Path(self.path()).exists():
            raise FileNotFoundException(f'"{self.path()}" does not exist.')

        """Load .json file."""
        with open(self.path(), "r") as file:
            self.data = json.load(file)

    def _new(self):
        """initialize citros object Create .json file."""
        raise NotImplementedError

    def _find_citros_in_ancestors(self, proj_dir=None, new=False):
        current_dir = (
            Path.cwd() if proj_dir is None else Path(proj_dir).expanduser().resolve()
        )

        return current_dir
        # print("current_dir", current_dir)
        # Ensure we don't go into an infinite loop at the root directory
        while current_dir != current_dir.parent:
            citros_dir = current_dir / ".citros"
            # print("citros_dir", citros_dir)
            if citros_dir.exists():
                return citros_dir.expanduser().resolve()
            current_dir = current_dir.parent

        return None

    ##################
    ##### public #####
    ##################
    def path(self):
        """return the full path to the current main file.

        default to ".citros/project.json"

        Returns:
            str: the full path to the current main file.
        """
        return self.root_citros / self.file
