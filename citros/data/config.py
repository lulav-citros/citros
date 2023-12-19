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

    # ORGANIZATION_NAME = _conf("ORGANIZATION_NAME", "home_organization")
    # POSTGRES_USERNAME = _conf("POSTGRES_USERNAME", "citros_anonymous")
    # POSTGRES_PASSWORD = _conf("POSTGRES_PASSWORD", "")
    # POSTGRES_HOST = _conf("POSTGRES_HOST", "")
    # POSTGRES_PORT = _conf("POSTGRES_PORT", "")
    # POSTGRES_DATABASE = _conf("POSTGRES_DATABASE", "")