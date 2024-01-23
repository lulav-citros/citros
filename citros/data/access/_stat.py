from .citros_db import CitrosDB
from .citros_dict import CitrosDict

class Stat:
    """
    Class for collecting technical statistics about connections from the CitrosDB class.

    Methods `get_stat()` and `print_stat()` return and display, correspondingly, information
    about how many connections and queries were done by all CitrosDB objects existing in the current session.
    The information is recorded only for those CitrosDB that were created with parameter debug_connect = True:

    - `n_pg_connection` - number of postgres connections
    - `n_pg_queries` - number of postgres queries
    - `pg_calls` - the statistics of how many queries to postgres database were done by each method.
    """

    def get_stat(self, format: str = "dict"):
        """
        Return information about connections.

        Parameters
        ----------
        format : {'dict','CitrosDict'}
            The returning format.

        Returns
        -------
        stat: dict or citros_data_analysis.data_access.citros_dict.CitrosDict
        """
        stat = {
            "n_pg_connections": CitrosDB.n_pg_connections,
            "n_pg_queries": CitrosDB.n_pg_queries,
        }
        if format == "CitrosDict":
            stat["pg_calls"] = CitrosDict(CitrosDB.pg_calls)
            stat = CitrosDict(stat)
        else:
            stat["pg_calls"] = CitrosDB.pg_calls
        return stat

    def print_stat(self):
        """
        Print information about connections.
        """
        self.get_stat(format="CitrosDict").print()
