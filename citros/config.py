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

    SUPPRESS_ROS_LAN_TRAFFIC: bool = _conf("SUPPRESS_ROS_LAN_TRAFFIC", False, cast=bool)
    """
    avoid seeing ros traffic from other simulations on the same LAN.
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
