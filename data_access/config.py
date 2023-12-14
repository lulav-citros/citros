import os
from decouple import config as _conf


class config:
    # CITROS_DIR: str = _conf("CITROS_DIR", None)
    # """
    # the directory where `.citros` is located.
    # """

    ROOT_DIR: str = _conf(
        "ROOT_DIR", default=os.path.join(os.getcwd(), ".citros/data"), cast=str
    )
    """
    the directory where `citros run` records all data to
    """
