from .citros_db import CitrosDB
from .citros_dict import CitrosDict


class _Stat:
    """
    Class for collecting technical statistics about connections from the CitrosDB class.

    Methods `get_stat()` and `print_stat()` return and display, correspondingly, information
    about how many connections and queries were done by all CitrosDB objects existing in the current session.
    The information is recorded only for those CitrosDB that were created with parameter debug = True:

    - `n_gql_connections` - number of graphql connections
    - `n_gql_queries` - number of graphql queries
    - `gql_calls` - the statistics of how many queries to gql database were done by each method.
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
        gql = {
            "n_gql_connections": CitrosDB.n_gql_connections,
            "n_gql_queries": CitrosDB.n_gql_queries,
        }
        pg = {
            "n_pg_connections": CitrosDB.n_pg_connections,
            "n_pg_queries": CitrosDB.n_pg_queries,
        }
        if format == "CitrosDict":
            gql["gql_calls"] = CitrosDict(CitrosDB.gql_calls)
            pg["pg_calls"] = CitrosDict(CitrosDB.pg_calls)
            stat = {**gql, **pg}
            stat = CitrosDict(stat)
        else:
            gql["gql_calls"] = CitrosDB.gql_calls
            pg["pg_calls"] = CitrosDB.pg_calls
            stat = {**gql, **pg}
        return stat

    def print_stat(self):
        """
        Print information about connections.
        """
        self.get_stat(format="CitrosDict").print()
