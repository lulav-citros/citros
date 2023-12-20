import os
from pathlib import Path
from decouple import config as _conf


class config:
    CITROS_HOME_DIR: str = Path.home() / ".citros"
    """
    ~/.citros
    """

    ROOT_DIR: str = _conf("ROOT_DIR", None)
    """
    the directory where `.citros` is located.
    """

    RECORDINGS_DIR: str = _conf("RECORDINGS_DIR", None)
    """
    the directory where `citros run` records all data to
    """

    VERBOSE: bool = _conf("VERBOSE", default=False, cast=bool)
    """
    system wide vorbose variable
    """

    STATS_INTERVAL: int = _conf("STATS_INTERVAL", default=1, cast=int)
    """
    update interval for System Stats Recorder
    """

    CITROS_ENVIRONMENT: str = _conf("CITROS_ENVIRONMENT", "LOCAL")
    """
    where we are running, can be [LOCAL, CLOUD, GITHUB]
    """

    STORAGE_TYPE = _conf("STORAGE_TYPE", "MCAP")
    """the storage type that will be used to record the ros bag into. default is MCAP. 
    options: [SQLITE3, MCAP]
    """

    ROS_DOMAIN_ID: int = _conf("ROS_DOMAIN_ID", 42, cast=int)
    """
    the domain id for ros to use. 
    """

    OPEN_TELEMETRY_URL = _conf("OPEN_TELEMETRY_URL", "localhost:3417")
    """
    the url for opentelemetry
    """

    TRACE_CONTEXT = _conf("TRACE_CONTEXT", None)
    """
    if the trace was started on the cluster by a different entity (e.g. the worker),
    its context is given by an environment variable.
    """

    # DATABASE
    ORGANIZATION_NAME = _conf("ORGANIZATION_NAME", "citros")

    DB_CONTAINER_NAME = _conf("DB_CONTAINER_NAME", "citros_db")
    CITROS_DATA_HOST = _conf("CITROS_DATA_HOST", "localhost")
    CITROS_DATA_PORT = _conf("CITROS_DATA_PORT", 5454, cast=int)
    POSTGRES_DATABASE = _conf("POSTGRES_DATABASE", "citros")
    POSTGRES_USERNAME = _conf("POSTGRES_USERNAME", "citros")
    POSTGRES_PASSWORD = _conf("POSTGRES_PASSWORD", "password")
