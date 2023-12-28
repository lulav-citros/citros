import os


def get_version():
    """
    Return version of the citros_data_analysis package.

    Examples
    --------
    >>> from citros_data_analysis import data_access as da
    >>> print(da.get_version())
    v0.1.1
    """
    rel_path = "../__init__.py"
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path)) as fp:
        for line in fp.read().splitlines():
            if line.startswith("__version__"):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        raise RuntimeError("Unable to find version string.")
