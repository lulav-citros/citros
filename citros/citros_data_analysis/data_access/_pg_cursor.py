import os
import re
import json
import numpy as np
import pandas as pd
import inspect
import psycopg2

from citros.database import CitrosDB as CitrosDB_base

from typing import Union, Optional, Any
from psycopg2 import sql
from prettytable import PrettyTable, ALL

from .citros_dict import CitrosDict


class _PgCursor(CitrosDB_base):
    _connection_parameters = {
        "host": None,
        "user": None,
        "password": None,
        "database": None,
        "port": None,
    }
    pg_connection = None

    # the following parameters are collected for all objects created with debug = True parameter CitrosDB(debug = True):
    # number of connections to postgres database
    n_pg_connections = 0
    # number of queries to postgres database
    n_pg_queries = 0
    # dict with method names and corresponding number of queries
    pg_calls = {}

    def __init__(
        self,
        host=None,
        port=None,
        user=None,
        password=None,
        database=None,
        simulation = None,
        batch = None,
        debug = False
    ):
        init_args = {}
        if host is not None:
            init_args['db_host'] = host
        if port is not None:
            init_args['db_port'] = port
        if user is not None:
            init_args['db_user'] = user
        if password is not None:
            init_args['db_password'] = password
        if database is not None:
            init_args['db_name'] = database
        super().__init__(**init_args)

        if simulation is None:
            simulation = os.getenv("CITROS_SIMULATION")
        self._set_simulation(simulation)

        self._set_batch(batch)

        self._registr_dec2float()
        self.if_close_connection = True

        self._debug = debug
        self._all_additional_columns = ["sid", "rid", "time", "topic", "type"]
        self._order_by_allowed = ["asc", "ASC", "Asc", "desc", "DESC", "Desc"]

    def _set_simulation(self, simulation):
        """
        Set simulation name.

        Parameters
        ----------
        simulation : str
            Name of the simulation.
        """
        if simulation is None:
            self._simulation = None
        elif isinstance(simulation, str):
            self._simulation = simulation
        else:
            self._simulation = None
            print("simulation is not set, 'simulation' must be a str")

    def _set_batch(self, batch):
        """
        Set batch name.

        Parameters
        ----------
        batch : str
            Name of the batch.
        """
        if batch is None:
            self._batch_name = None
        elif isinstance(batch, str):
            self._batch_name = batch
        else:
            self._batch = None
            print("batch is not set, 'batch' must be a str")

    def _set_sid(self, value):
        """
        Set self._sid value.

        Parameters
        ----------
        value : int or list of ints or None
        """
        if value is not None:
            if isinstance(value, list):
                if len(value) != 0:
                    self._sid = []
                    for v in value:
                        try:
                            self._sid.append(int(v))
                        except:
                            print("sid must be int or list of ints")
                            self._sid = None
                            break
                else:
                    self._sid = None
            elif isinstance(value, int):
                self._sid = [value]
            else:
                try:
                    self._sid = [int(value)]
                except:
                    print("sid must be int or list of ints")
                    self._sid = None
        else:
            self._sid = None

    def _set_rid(self, value):
        """
        Set self._rid value.

        Parameters
        ----------
        value : int or list of ints or None
        """
        if value is not None:
            if isinstance(value, list):
                if len(value) != 0:
                    self._sid = []
                    for v in value:
                        try:
                            self._sid.append(int(v))
                        except:
                            print(
                                f"sid: provide int value for int or list of ints can not convert to int sid = {v};"
                            )
                            self._sid = None
                            break
                else:
                    self._sid = None
            elif isinstance(value, int):
                self._sid = [value]
            else:
                try:
                    self._sid = [int(value)]
                except:
                    print("sid must be int or list of ints")
                    self._sid = None
        else:
            self._sid = None

    def _make_connection_postgres(self):
        """
        Make connection to Postgres database to execute PostgreSQL commands.
        """
        _PgCursor.pg_connection = self.connect()
        if self._debug and _PgCursor.pg_connection is not None:
            _PgCursor.n_pg_connections += 1

    def _registr_dec2float(self):
        """
        Register returning types of the decimals as float.
        """
        DEC2FLOAT = psycopg2.extensions.new_type(
            psycopg2.extensions.DECIMAL.values,
            "DEC2FLOAT",
            lambda value, curs: float(value) if value is not None else np.nan,
        )
        psycopg2.extensions.register_type(DEC2FLOAT)

    def _change_connection_parameters(self):
        _PgCursor._connection_parameters["host"] = self.db_host
        _PgCursor._connection_parameters["user"] = self.db_user
        _PgCursor._connection_parameters["password"] = self.db_password
        _PgCursor._connection_parameters["database"] = self.db_name
        _PgCursor._connection_parameters["port"] = self.db_port

    def _if_connection_parameters_changed(self):
        new_connection = {
            "host": self.db_host,
            "user": self.db_user,
            "password": self.db_password,
            "database": self.db_name,
            "port": self.db_port,
        }
        return new_connection != _PgCursor._connection_parameters
    
    def _get_connection(self):
        """
        Return connection if it is set 
        """

    def _execute_query(self, query, param_execute=None, check_batch=True):
        """
        Execute Postgres query

        Parameters
        ----------
        query : str
            query to execute.
        param_execute : list
            Additional parameters to pass.
        check_batch : bool
            If True, check that batch is provided.

        Returns
        -------
        dict
            key 'res' contains list of tuples - result of the query execution, 'error' - error if it occurred or None
        """
        if param_execute == []:
            param_execute = None
        if check_batch:
            if self._batch_name is None:
                print("Error: please provide batch by citros.batch()")
                return {"res": None, "error": None}
        if _PgCursor.pg_connection is None:
            self._make_connection_postgres()
            self._change_connection_parameters()
        else:
            if self._if_connection_parameters_changed():
                try:
                    _PgCursor.pg_connection.close()
                except psycopg2.InterfaceError:
                    # connection is already closed
                    pass
                self._make_connection_postgres()
                self._change_connection_parameters()

        for j in range(2):
            try:
                with _PgCursor.pg_connection.cursor() as curs:
                    curs.execute(query, param_execute)
                    if self._debug:
                        _PgCursor.n_pg_queries += 1
                        self._calculate_pg_calls(inspect.stack()[1][3])
                    result = curs.fetchall()
                    return {"res": result, "error": None}

            except psycopg2.InterfaceError as e:
                if j == 0:
                    self._make_connection_postgres()
                else:
                    if self._debug:
                        raise e
                    else:
                        print("Error:", e)
                    return {"res": None, "error": type(e).__name__}
            except (
                psycopg2.errors.InFailedSqlTransaction,
                psycopg2.OperationalError,
            ) as e:
                if j == 0:
                    _PgCursor.pg_connection.close()
                    self._make_connection_postgres()
                else:
                    if self._debug:
                        raise e
                    else:
                        print("Error:", e)
                    return {"res": None, "error": type(e).__name__}
            except (
                psycopg2.errors.UndefinedColumn,
                psycopg2.errors.UndefinedFunction,
            ) as e:
                if self._debug:
                    raise e
                else:
                    print("Error:", e.args[0].split("\n")[0])
                return {"res": None, "error": type(e).__name__}
            except psycopg2.errors.UndefinedTable as e:
                return {"res": None, "error": type(e).__name__}
            except Exception as e:
                if self._debug:
                    raise e
                else:
                    print("Error:", e)
                return {"res": None, "error": type(e).__name__}

    def _calculate_pg_calls(self, method):
        """ """
        if _PgCursor.pg_calls.get(method):
            _PgCursor.pg_calls[method] += 1
        else:
            _PgCursor.pg_calls[method] = 1

    def _pg_info(self) -> CitrosDict:
        """
        Return information about the batch, based on the configurations set by topic(), rid(), sid() and time() methods.
        """
        if hasattr(self, "error_flag"):
            return CitrosDict({})

        filter_by = self._summarize_constraints()
        general_info, error_occurred, error_name = self._get_general_info(filter_by)
        result = general_info
        if error_name is None and not error_occurred:
            if self._sid is not None or hasattr(self, "_sid_val"):
                sid_info = self._get_sid_info(filter_by)
                result = CitrosDict({**result, "sids": sid_info})
            if self._topic is not None:
                topic_info = self._get_topic_info(filter_by)
                result = CitrosDict({**result, "topics": topic_info})
        return result

    def _get_general_info(self, filter_by):
        """
        Return general info.

        Returning dictionary contains:
        {
          'size': size of the selected data
          'sid_count': number of sids
          'sid_list': list of the sids
          'topic_count': number of topics
          'topic_list': list of topics
          'message_count': number of messages
        }

        Parameters
        ---------
        topic_name : list of str, optional
            Names of the topics. If not specified, returns for all topics.
        sid : list of ints, optional
            Simulation run ids. If not specified, returns for all sids.

        Returns
        -------
        CitrosDict
            Dictionary with general information.
        """
        (
            size,
            topic_list,
            sid_list,
            message_count,
            error_occurred,
            error_name,
        ) = self._general_info_query(filter_by=filter_by)
        sid_list.sort()
        sid_count = len(sid_list)
        topic_list.sort()
        topic_count = len(topic_list)
        result = CitrosDict(
            {
                "size": size,
                "sid_count": sid_count,
                "sid_list": sid_list,
                "topic_count": topic_count,
                "topic_list": topic_list,
                "message_count": message_count,
            }
        )
        return result, error_occurred, error_name

    def _get_sid_info(self, filter_by):
        """
        Return dictionary with information about each sid and each sid's topic.

        Dictionary has the following structure:
            int: {
                'topics': {
                    str: {
                        'message_count': number of messages
                        'start_time': time when simulation started
                        'end_time': time when simulation ended
                        'duration': duration of the simulation process
                        'frequency': frequency of the simulation process, 10**9 * 'message_count'/duration
                    }
                }
            }

        Parameters
        ----------
        sid : list
            Simulation run ids.
        topic_name : list of str, optional
            Names of the topics. If not specified, returns for all topics.

        Returns
        -------
        CitrosDict
            Dictionary with sid information.
        """
        df_time = self._sid_info_query(group_by=["sid", "topic"], filter_by=filter_by)
        if df_time is None:
            return []
        df_time = df_time.set_index(["sid", "topic"]).sort_index()
        sid_list = list(set(df_time.index.get_level_values("sid")))
        result = CitrosDict()
        for s in sid_list:
            result_sid = CitrosDict()
            topic_list = list(df_time.loc[s].index)
            result_topic_main = CitrosDict()
            for topic in topic_list:
                result_topic = CitrosDict()
                result_topic["message_count"] = int(
                    df_time.loc[(s, topic), "number of messages"]
                )
                result_topic["start_time"] = int(df_time.loc[(s, topic), "startTime"])
                result_topic["end_time"] = int(df_time.loc[(s, topic), "endTime"])
                result_topic["duration"] = int(df_time.loc[(s, topic), "duration"])
                try:
                    result_topic["frequency"] = round(
                        result_topic["message_count"]
                        * 10**9
                        / float(df_time.loc[(s, topic), "duration"]),
                        ndigits=3,
                    )
                except ZeroDivisionError:
                    result_topic["frequency"] = 0
                result_topic_main[topic] = result_topic
            result_sid["topics"] = result_topic_main
            result[s] = result_sid
        return result

    def _get_topic_info(self, filter_by):
        """
        Return dictionary with information about each topic and type in the batch.

        Dictionary has the following structure:
            str: {
                'type': type
                'data_structure': structure of the data
                'message_count': number of messages
            }

        Parameters
        ----------
        topic_names : list
            Names of the topics for which the information is collected.
            If not specified, information is collected for all topics.

        Returns
        -------
        CitrosDict
            Information about the selected topics.
        """
        message_count, structure = self._topic_info_query(
            filter_by=filter_by, out_format="dict"
        )
        F_message_count = pd.DataFrame(
            message_count, columns=["topic", "number"]
        ).set_index(["topic"])

        topic_dict = {}
        for item in structure:
            key = item[0]
            val = item[1:]
            if key in topic_dict:
                topic_dict[key].append(val)
            else:
                topic_dict[key] = [val]

        result = CitrosDict({})

        for topic_name, struct in topic_dict.items():
            result[topic_name] = CitrosDict({})
            if len(struct) > 0:
                d_ds = {0: struct[0][1]}
                d_t = {0: [struct[0][0]]}
                i = 0
            if len(struct) > 1:
                for row in struct[1:]:
                    added = False
                    for k, v in d_ds.items():
                        if row[1] == v:
                            d_t[k].append(row[0])
                            added = True
                    if not added:
                        i += 1
                        d_ds[i] = row[1]
                        d_t[i] = [row[0]]
            if i == 0:
                if len(d_t[0]) == 1:
                    type_output = d_t[0][0]
                else:
                    type_output = d_t[0]
                result[topic_name]["type"] = type_output
                result[topic_name]["data_structure"] = CitrosDict(
                    {"data": CitrosDict(d_ds[0])}
                )
            else:
                for j in range(i + 1):
                    if len(d_t[j]) == 1:
                        type_output = d_t[j][0]
                    else:
                        type_output = d_t[j]
                    result[topic_name]["type_group_" + str(j)] = CitrosDict(
                        {
                            "type": type_output,
                            "data_structure": CitrosDict({"data": CitrosDict(d_ds[j])}),
                        }
                    )
            result[topic_name]["message_count"] = int(
                F_message_count.loc[topic_name].iloc[0]
            )

        return result

    def topic(self, topic_name: Optional[Union[str, list]] = None):
        """
        Select topic.

        Parameters
        ----------
        topic_name : str or list of str
            Name of the topic.
        """
        if isinstance(topic_name, str):
            self._topic = [topic_name]
        elif isinstance(topic_name, list):
            for s in topic_name:
                if not isinstance(s, str):
                    print(
                        'topic(): "{s}" is not str; please provide `topic_name` as str or a list of str'
                    )
                    self._error_flag = True
                    return
            self._topic = topic_name.copy()
        elif isinstance(topic_name, np.ndarray):
            self._topic = list(topic_name)
        else:
            print("topic(): `topic_name` must be str or list of str")
            self._error_flag = True
        return

    def sid(
        self,
        value: Optional[Union[int, list]] = None,
        start: int = 0,
        end: int = None,
        count: int = None,
    ):
        """
        Set constraints on sid.

        Parameters
        ----------
        value : int or list of ints, optional
            Exact values of sid.
            If nothing is passed, then the default value of sid is used (ENV parameter "CITROS_SIMULATION_RUN_ID").
            If the default value does not exist, no limits for sid are applied.
        start : int, default 0
            The lower limit for sid values.
        end : int, optional
            The higher limit for sid, the end is included.
        count : int, optional
            Used only if the `end` is not set.
            Number of sid to return in the query, starting form the `start`.
        """
        if value is not None:
            if isinstance(value, (int, list)):
                self._set_sid(value)
            else:
                try:
                    self._sid = [int(value)]
                except:
                    print("sid(): sid `value` must be an int or a list of ints")
                    self._error_flag = True
                    return
        else:
            if start == 0 and end is None and count is None:
                return
            else:
                constr = {}
                if start > 0:
                    if not isinstance(start, int):
                        try:
                            start = int(start)
                        except:
                            print("sid(): sid `start` must be int")
                            self._error_flag = True
                            return
                    if start < 0:
                        print("sid(): sid `start` must be >= 0")
                        self._error_flag = True
                        return
                    constr[">="] = start
                if end is not None:
                    if not isinstance(end, int):
                        try:
                            end = int(end)
                        except:
                            print("sid(): sid `end` must be int")
                            self._error_flag = True
                            return
                    if end < 0:
                        print("sid(): sid `end` must be >= 0")
                        self._error_flag = True
                        return
                    if start > end:
                        print("sid(): sid `start` must be < `end`")
                        self._error_flag = True
                        return
                    constr["<="] = end
                else:
                    if count is not None:
                        if not isinstance(count, int):
                            try:
                                count = int(count)
                            except:
                                print("sid(): sid `count` must be int")
                                self._error_flag = True
                                return
                        if count < 0:
                            print("sid(): sid `count` must be >= 0")
                            self._error_flag = True
                            return
                        constr["<"] = start + count
                if len(constr) != 0:
                    self._sid = None
                    self._sid_val = {"sid": constr}

    def rid(
        self,
        value: Optional[Union[int, list]] = None,
        start: int = 0,
        end: int = None,
        count: int = None,
    ):
        """
        Set constraints on rid.

        Parameters
        ----------
        value : int or list of ints, optional
            Exact values of rid.
        start : int, default 0
            The lower limit for rid values.
        end : int, optional
            The higher limit for rid, the end is included.
        count : int, optional
            Used only if the `end` is not set.
            Number of rid to return in the query, starting form the `start`.
        """
        if value is not None:
            if isinstance(value, int):
                self._rid_val = {"rid": [value]}
            elif isinstance(value, list):
                if len(value) != 0:
                    good_rid = []
                    for v in value:
                        try:
                            good_rid.append(int(v))
                        except:
                            print(
                                "rid, provided by `value` argument, must be int or list of ints"
                            )
                            self._error_flag = True
                            break
                    self._rid_val = {"rid": good_rid}
            else:
                try:
                    self._rid_val = {"rid": [int(value)]}
                except:
                    print(
                        "rid, provided by `value` argument, must be int or list of ints"
                    )
                    return
        else:
            if start == 0 and end is None and count is None:
                return
            else:
                constr = {}
                if start != 0:
                    if not isinstance(start, int):
                        try:
                            start = int(start)
                        except:
                            print("rid(): rid `start` must be int")
                            self._error_flag = True
                            return
                    if start < 0:
                        print("rid(): rid `start` must be >= 0")
                        self._error_flag = True
                        return
                    constr[">="] = start
                if end is not None:
                    if not isinstance(end, int):
                        try:
                            end = int(end)
                        except:
                            print("rid(): rid `end` must be int")
                            self._error_flag = True
                            return
                    if end < 0:
                        print("rid(): rid `end` must be >= 0")
                        self._error_flag = True
                        return
                    if start > end:
                        print("rid(): rid `start` must be < `end`")
                        self._error_flag = True
                        return
                    constr["<="] = end
                else:
                    if count is not None:
                        if not isinstance(count, int):
                            try:
                                count = int(count)
                            except:
                                print("rid(): rid `count` must be int")
                                self._error_flag = True
                                return
                        if count < 0:
                            print("rid(): rid `count` must be >= 0")
                            self._error_flag = True
                            return
                        constr["<"] = start + count
                if len(constr) != 0:
                    self._rid_val = {"rid": constr}

    def time(self, start: int = 0, end: int = None, duration: int = None):
        """
        Set constraints on time.

        Parameters
        ----------
        start : int, default 0
            The lower limit for time values.
        end : int, optional
            The higher limit for time, the end is included.
        duration : int, optional
            Used only if the `end` is not set.
            Time interval to return in the query, starting form the `start`.
        """
        if start == 0 and end is None and duration is None:
            return
        else:
            constr = {}
            if start != 0:
                if not isinstance(start, int):
                    try:
                        start = int(start)
                    except:
                        print("time(): time `start` must be int")
                        self._error_flag = True
                        return
                if start < 0:
                    print("time(): time `start` must be >= 0")
                    self._error_flag = True
                    return
                constr[">="] = start

            if end is not None:
                if not isinstance(end, int):
                    try:
                        end = int(end)
                    except:
                        print("time(): time `end` must be int")
                        self._error_flag = True
                        return
                if end < 0:
                    print("time(): time `end` must be >= 0")
                    self._error_flag = True
                    return
                if start > end:
                    print("time(): time `start` must be < ``end``")
                    self._error_flag = True
                    return
                constr["<="] = end
            else:
                if duration is not None:
                    if not isinstance(duration, int):
                        try:
                            duration = int(duration)
                        except:
                            self._error_flag = True
                            return
                    if duration < 0:
                        print("time(): time `duration` must be >= 0")
                        self._error_flag = True
                        return
                    constr["<"] = start + duration
            if len(constr) != 0:
                self._time_val = {"time": constr}

    def set_filter(self, filter_by: dict = None):
        """
        Set constraints on query.

        Allows to set constraints on json-data columns.

        Parameters
        ----------
        filter_by : dict
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}.<br />
            key_n - must match labels of the columns, <br />
            value_n  - in the case of equality: list of exact values,<br />
                       in the case of inequality: dict with ">", ">=", "<" or "<=".<br />
            Conditions, passed here, have higher priority over those defined by `topic()`, `rid()`, `sid()` and `time()` and will override them.
            If sampling method is used, constraints on additional columns are applied BEFORE sampling while
            constraints on columns from json-data are applied AFTER sampling.
        """
        if filter_by is not None:
            if not isinstance(filter_by, dict):
                print("set_filter(): argument must be a dictionary")
                self._error_flag = True
                return
            if "topic" in filter_by.keys():
                if isinstance(filter_by["topic"], str):
                    filter_by["topic"] = [filter_by["topic"]]
            if "sid" in filter_by.keys():
                if isinstance(filter_by["sid"], int):
                    filter_by["sid"] = [filter_by["sid"]]
            if "rid" in filter_by.keys():
                if isinstance(filter_by["rid"], int):
                    filter_by["rid"] = [filter_by["rid"]]
            self._filter_by = filter_by.copy()

    def set_order(self, order_by: Optional[Union[str, list, dict]] = None):
        """
        Apply sorting to the result of the query.

        Sort the result of the query in ascending or descending order.

        Parameters
        ----------
        order_by : str, list of str or dict, optional
            If `order_by` is a single string or a list of strings, it represents the column label(s) by which the result is sorted in ascending order.
            For more control, use a dictionary with column labels as keys and values ('asc' for ascending, 'desc' for descending) to define the sorting order.
        """
        if order_by is not None:
            if not isinstance(order_by, (dict, list, str)):
                print(
                    "set_order(): argument must be a string, list of strings or a dictionary"
                )
                self._error_flag = True
                return
            else:
                result, error_flag = self._check_set_order(order_by)
                if error_flag is True:
                    self._error_flag = True
                    return
                else:
                    self._order_by = result

    def skip(self, n_skip: int = None):
        """
        Select each `n_skip`-th message.

        Messages with different sids are selected separately.

        Parameters
        ----------
        skip : int, optional
            Control number of the messages to skip.
        """
        if hasattr(self, "method"):
            print("only one sampling function may be applied")
            self._error_flag = True
            return
        if n_skip is None:
            return
        if not isinstance(n_skip, int):
            print("skip(): n_skip value must be int")
            self._error_flag = True
            return
        if n_skip <= 0:
            print("skip(): n_skip value must be > 0")
            self._error_flag = True
            return
        self._method = "skip"
        self._n_skip = n_skip
        self._n_avg = None

    def avg(self, n_avg: int = None):
        """
        Average `n_avg` number of messages.

        Messages with different sids are processed separately.
        The value in 'rid' column is set as a minimum value among the 'rid' values of the averaged rows.

        Parameters
        ----------
        n_avg : int
            Number of messages to average.
        """
        if hasattr(self, "method"):
            print("only one sampling function may be applied")
            self._error_flag = True
            return
        if n_avg is None:
            return
        if not isinstance(n_avg, int):
            print("avg(): n_avg value must be int")
            self._error_flag = True
            return
        if n_avg <= 0:
            print("avg(): n_avg value must be > 0")
            self._error_flag = True
            return
        self._method = "avg"
        self._n_avg = n_avg
        self._n_skip = None

    def move_avg(self, n_avg: int = None, n_skip: int = 1):
        """
        Compute moving average over `n_avg` massages and select each `n_skip`-th one.

        Messages with different sids are processed separately.
        The value in 'rid' column is set as a minimum value among the 'rid' values of the averaged rows.

        Parameters
        ----------
        n_avg : int, optional
            Number of messages to average.
        n_skip : int, default 1
            Number of the messages to skip.
            For example, if `skip` = 3, the 1th, the 4th, the 7th ... messages will be selected
        """
        if hasattr(self, "method"):
            print("only one sampling function may be applied")
            self._error_flag = True
            return
        if n_avg is None:
            return
        if not isinstance(n_avg, int):
            print("move_avg(): n_avg value must be int")
            self._error_flag = True
            return
        if n_avg <= 0:
            print("move_avg(): n_avg value must be > 0")
            self._error_flag = True
            return
        if not isinstance(n_skip, int):
            print("move_avg(): n_skip value must be int")
            self._error_flag = True
            return
        if n_skip <= 0:
            print("move_avg(): n_skip value must be > 0")
            self._error_flag = True
            return

        self._method = "move_avg"
        self._n_skip = n_skip
        self._n_avg = n_avg

    def _check_set_order(self, order_by):
        """
        Check and prepare `order_by` argument for set_order() method.

        Check if the `order_by` dictionary and its keys have the right types, changes dictionary values to lowercase and
        check if they are matches the words 'asc' and 'desc'.

        Parameters
        ----------
        order_by : dict, list of str or str
            Keys of the dictionary must match labels of the columns,
            values - define ascending ('asc') or descending ('desc') order.

        Returns
        -------
        result : dict
            `order_by` with checked types and changed to lowercase values.
        error_flag : bool
            True if `order_by` has problems with types or the values does not matches 'asc' or 'desc'.
        """
        result = {}
        error_flag = False
        if isinstance(order_by, dict):
            for k, v in order_by.items():
                if not isinstance(k, str):
                    print(
                        "set_order(): dictionary keyword (column label) must be a str"
                    )
                    error_flag = True
                    return result, error_flag
                if isinstance(v, str):
                    if v.lower() in ["asc", "desc"]:
                        result[k] = v.lower()
                    else:
                        error_flag = True
                        print(
                            'set_order(): dictionary value must be a str "asc" or "desc"'
                        )
                        return result, error_flag
                else:
                    print('set_order(): dictionary value must be a str "asc" or "desc"')
                    error_flag = True
                    return result, error_flag
        elif isinstance(order_by, str):
            result[order_by] = "asc"
        elif isinstance(order_by, list):
            for k in order_by:
                if not isinstance(k, str):
                    print("set_order(): list must contain str (column labels)")
                    error_flag = True
                    return result, error_flag
                else:
                    result[k] = "asc"
        return result, error_flag

    def _summarize_constraints(self):
        """
        Summarize all constraints, applied by `topic`, `sid`, `rid`, `time`, `filter_by` methods

        Returns
        -------
        dict
        """
        filter_by = {}
        if self._topic is not None:
            filter_by["topic"] = self._topic.copy()

        if self._sid is not None:
            filter_by["sid"] = self._sid
        else:
            if hasattr(self, "_sid_val"):
                filter_by = {**filter_by, **self._sid_val}
        if hasattr(self, "_rid_val"):
            filter_by = {**filter_by, **self._rid_val}
        if hasattr(self, "_time_val"):
            filter_by = {**filter_by, **self._time_val}

        # all constraints set by `set_filter()` override the previous setups
        if hasattr(self, "_filter_by"):
            filter_by = {**filter_by, **self._filter_by}

        return filter_by

    def _data(
        self, data_names: list = None, additional_columns: list = None
    ) -> pd.DataFrame:
        """
        Return table with data.

        Query data according to the constraints set by topic(), rid(), sid() and time() methods
        and one of the aggregative method skip(), avg() or move_avg().

        Parameters
        ----------
        data_names : list, optional
            Labels of the columns from json data column.
        additional_columns : list, optional
            Columns to download outside the json data column: `sid`, `rid`, `time`, `topic`, `type`.
            If not specified, then all additional columns are downloaded.

        Returns
        -------
        pandas.DataFrame
            Table with selected data.
        """
        if isinstance(additional_columns, str):
            additional_columns = [additional_columns]
        if additional_columns is None:
            additional_columns = []
        if len(additional_columns) != 0 and "sid" not in additional_columns:
            additional_columns.append("sid")

        if hasattr(self, "error_flag"):
            return None

        filter_by = self._summarize_constraints()

        if "topic" not in filter_by.keys():
            print("topic is not specified")
            return None
        elif len(filter_by["topic"]) > 1:
            print("too many topics to query data, please provide one topic")
            return None

        if isinstance(data_names, str):
            data_names = [data_names]

        if not hasattr(self, "_method"):
            self._method = ""
            self._n_avg = None
            self._n_skip = None

        if hasattr(self, "_order_by"):
            order_by = self._order_by
        else:
            # order_by = None
            order_by = {"sid": "asc", "rid": "asc"}

        df = self._get_data(
            data_names,
            additional_columns=additional_columns,
            filter_by=filter_by,
            order_by=order_by,
            method=self._method,
            n_avg=self._n_avg,
            n_skip=self._n_skip,
        )
        return df

    def _is_batch_in_database(self, tablename):
        """
        Check if the batch `tablename` is in the database.

        Parameters
        ----------
        tablename : batch name.

        Returns
        -------
        result : bool
            True if the batch is in the database, otherwise False.
        """
        query = sql.SQL("SELECT tablename from pg_tables where schemaname = %(schema)s")
        table_result = self._execute_query(
            query, {"schema": self._simulation}, check_batch=False
        )["res"]
        tables = [t[0] for t in table_result]
        if tablename not in tables:
            return False
        else:
            return True

    def _is_schema_exist(self):
        """
        Check if the schema exists.
        """
        query = sql.SQL(
            "SELECT DISTINCT schemaname from pg_tables where schemaname = %(schema)s"
        )
        schema_list = self._execute_query(
            query, {"schema": self._simulation}, check_batch=False
        )["res"]
        if len(schema_list) == 0:
            return False
        else:
            return True

    def _resolve_query_json(self, query_input, null_wrap=True):
        """
        Transform query for the json "data" column to SQL.

        Parameters
        ----------
        query_input : list
            Data to download.
            For example, if the value of "x" from json-format "data" is desired, data_query = ["data.x"].

        Returns
        -------
        result : str
            Part of the SQL query for json.
        col_label : list
            Names of the columns.
        json_labels : list
            Names of the variable in json.
        null_wrap : bool, default True
            If True, wraps x in nullif(x,'null') to change the null jsonb value, if there is any, to null sql value.
            Applies only to content of the json columns, not to ordinary columns.
        """
        result = []
        col_label = []
        json_labels = []

        for q_elem in query_input:
            q_row = q_elem.split(".")
            m = re.findall("\[(\d*)\]", q_row[0])
            if len(m) != 0:
                s_row = ["{}"]
                for mm in m:
                    try:
                        _ = int(mm)
                        s_row += [mm]
                    except:
                        pass
                n = re.search("([^\[]*)", q_row[0])
                col_label.append(sql.Identifier(n.group()))
            else:
                s_row = ["{}"]
                col_label.append(sql.Identifier(q_row[0]))
            if len(q_row) > 1:
                for q in q_row[1:]:
                    m = re.findall("\[(\d*)\]", q)
                    if len(m) != 0:
                        s_row += ["%s"]
                        for mm in m:
                            try:
                                _ = int(mm)
                                s_row += [mm]
                            except:
                                pass
                        n = re.search("([^\[]*)", q)
                        json_labels += [n.group()]
                    else:
                        s_row += ["%s"]
                        json_labels += [q]
            s_row_conct = " -> ".join(s_row)
            if null_wrap:
                if s_row_conct != "{}":
                    s_row_conct = "nullif(" + s_row_conct + ",'null')"
            result.append(s_row_conct)
        return ", ".join(result), col_label, json_labels

    def _resolve_filter_by(self, filter_by):
        """
        Transform constraints to SQL query form.

        Parameters
        ----------
        filter_by : dict
            Keys must match labels of the columns, values either list of exact values
            or signs "gt", "gte", "lt" & "lte" for ">", ">=", "<" & "<=".

        Returns
        -------
        query_filter: str
            SQL string.
        param_sql: list
            Parameters to put into sql.SQL().format().
        param_execute: list
            Parameters to put as second argument in self.cursor.execute().
        """
        param_sql = []
        param_execute = []
        filter_eq = {}
        filter_ineq = {}
        sign_dict = {
            "gt": ">",
            "lt": "<",
            "gte": ">=",
            "lte": "<=",
            "eq": "=",
            ">": ">",
            "<": "<",
            ">=": ">=",
            "<=": "<=",
            "=": "=",
        }
        numeric_types = ["int", "float"]

        if len(filter_by) != 0:
            query_filter = " WHERE "
            query_filter_eq = []
            query_filter_ineq = []
            eq_type = {}
            for k, v in filter_by.items():
                if isinstance(v, list):
                    filter_eq[k] = v
                    if isinstance(v[0], str):
                        eq_type[k] = "str"
                    else:
                        eq_type[k] = "num"
                elif isinstance(v, dict):
                    filter_ineq[k] = v
                else:
                    filter_eq[k] = [v]
                    if isinstance(v, str):
                        eq_type[k] = "str"
                    else:
                        eq_type[k] = "num"
            if len(filter_eq) != 0:
                for eq_col, eq_dict in filter_eq.items():
                    json_str, col_label, json_labels = self._resolve_query_json(
                        [eq_col]
                    )
                    if json_str != "{}":
                        # if json_str != "nullif({},'null')":
                        if eq_type[eq_col] == "str":
                            json_str = json_str[::-1].replace(">-", ">>-", 1)[::-1]
                        else:
                            json_str = "(" + json_str + ")::NUMERIC"
                    query_filter_eq.append(json_str + " = ANY(%s) ")
                    param_sql += col_label
                    param_execute += json_labels
                    param_execute.append(eq_dict)
            if len(filter_ineq) != 0:
                for ineq_col, ineq_dict in filter_ineq.items():
                    json_str, col_label, json_labels = self._resolve_query_json(
                        [ineq_col]
                    )
                    if (
                        json_str != "{}"
                        and type(list(ineq_dict.values())[0]).__name__ in numeric_types
                    ):
                        # if json_str != "nullif({},'null')" and type(list(ineq_dict.values())[0]).__name__ in numeric_types:
                        json_str = "(" + json_str + ")::NUMERIC "
                    for k, v in ineq_dict.items():
                        query_filter_ineq.append(json_str + sign_dict[k] + " %s ")
                        param_sql += col_label
                        param_execute += json_labels
                        param_execute.append(v)

            query_filter += "AND ".join(query_filter_eq + query_filter_ineq)
        else:
            query_filter = ""
        return query_filter, param_sql, param_execute

    def _resolve_order_by(self, order_by):
        """
        Transform order by clause to SQL query form.

        Parameters
        ----------
        order_by : dict
            Keys must match labels of the columns, values specify ascending ('asc') or descending ('desc') order.

        Returns
        -------
        query_order : str
            SQL string.
        param_sql_order : list
            Parameters to put into format of sql.SQL().format().
        param_execute_order : list
            Parameters to put as second argument in self.cursor.execute().
        """
        order_by_checked = {}
        param_sql_order = []
        param_execute_order = []
        query_order = ""
        if len(order_by) != 0:
            for k, v in order_by.items():
                if v in self._order_by_allowed:
                    order_by_checked[k] = v
            if len(order_by_checked) != 0:
                query_order_el = []
                for k, v in order_by_checked.items():
                    json_str, col_label, json_labels = self._resolve_query_json([k])
                    if json_str != "{}":
                        # if json_str != "nullif({},'null')":
                        query_order_el.append("(" + json_str + ")::NUMERIC " + v)
                    else:
                        query_order_el.append("{} " + v)
                    param_sql_order += col_label
                    param_execute_order += json_labels
                query_order = " ORDER BY " + ", ".join(query_order_el)
        return query_order, param_sql_order, param_execute_order

    def _get_batch_sizes(self):
        """
        Return sizes of the batches according to simulation() and batch() settings.

        Returns
        -------
        result : list of tuples
            Each tuple contains name of the table, table size and total size with indexes.
        """
        var = {}
        if self._simulation is None:
            schema_condition = "schemaname NOT IN ('pg_catalog', 'information_schema')"
        else:
            schema_condition = "schemaname = %(schema)s"
            var = {"schema": self._simulation}

        if self._batch_name is not None:
            tablename_condition = " AND tablename = %(tablename)s"
            var["tablename"] = self._batch_name
        else:
            tablename_condition = ""
        query = sql.SQL(
            "SELECT tablename, \
                        pg_size_pretty(pg_relation_size(schemaname||'.'||tablename)) as size, \
                        pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as total_size \
                        from pg_tables where "
            + schema_condition
            + tablename_condition
        )
        result = self._execute_query(query, var, check_batch=False)
        return result["res"]

    def _download_data_structure(self, filter_by=None, out_format="dict"):
        """
        Return structure of the "data".

        Parameters
        ----------
        filter_by : dict
            Constraints.
            Conditions, passed here, have higher priority, than defined by `topic()`, `rid()`, `sid()` and `time()`.
        format : str
            The output data structure format:
                'dict' - dict,
                'str' - string

        Returns
        -------
        result : list of tuples
            Each tuple contains topic and type names and structure of the corresponding data.
        """
        if filter_by is None:
            filter_by = {}

        param_execute = {}
        param_sql = [sql.Identifier(self._simulation, self._batch_name)]
        param_execute = []

        query_filter, param_sql_filter, param_execute_filter = self._resolve_filter_by(
            filter_by
        )
        param_sql += param_sql_filter
        param_execute += param_execute_filter

        query = sql.SQL(
            "SELECT DISTINCT ON (topic, type) topic, type, data FROM {}" + query_filter
        )

        query_result = self._execute_query(query.format(*param_sql), param_execute)
        q_result = query_result["res"]
        error_name = query_result["error"]

        if error_name is None and len(q_result) != 0:
            data_dict_list = list(map(lambda x: x[2], q_result))
            data_structure_list = []
            for data_dict in data_dict_list:
                type_dict = CitrosDict()
                CitrosDict()._get_type_dict(type_dict, data_dict)
                if out_format == "str":
                    type_json = json.dumps(type_dict, indent=2)
                    data_structure = type_json.replace('"', "")
                    data_structure_list.append(data_structure)
                else:
                    data_structure_list.append(type_dict)
            result = []
            for j in range(len(q_result)):
                result.append((q_result[j][0], q_result[j][1], data_structure_list[j]))
            return result
        else:
            return q_result

    def _topic_info_query(self, filter_by=None, out_format="dict"):
        """
        Return structure of the "data".

        Parameters
        ----------
        filter_by : dict
            Constraints.
            Conditions, passed here, have higher priority, than defined by `topic()`, `rid()`, `sid()` and `time()`.
        format : str
            The output data structure format:
                'dict' - dict,
                'str' - string

        Returns
        -------
        message_count : list of tuples
            Each tuple contains topic name and corresponding to this topic number of messages
        list of tuples
            Each tuple contains topic and type names and structure of the corresponding data.
        """
        if filter_by is None:
            filter_by = {}

        param_execute = {}
        param_sql = []
        param_execute = []

        query_filter, param_sql_filter, param_execute_filter = self._resolve_filter_by(
            filter_by
        )
        param_sql += param_sql_filter
        param_execute += param_execute_filter

        query = sql.SQL(
            """
        SELECT DISTINCT ON (topic, type) topic, type, data, topic_count
        FROM (
            SELECT topic, type, data, COUNT(*) OVER (PARTITION BY topic) as topic_count
            FROM {table_name}"""
            + query_filter
            + """) AS t;
        """
        )

        q_result = self._execute_query(
            query.format(*param_sql, table_name=sql.Identifier(self._simulation, self._batch_name)),
            param_execute,
            check_batch=False,
        )["res"]
        if q_result is not None and len(q_result) != 0:
            data_dict_list = list(map(lambda x: x[2], q_result))
            data_structure_list = []
            for data_dict in data_dict_list:
                type_dict = CitrosDict()
                CitrosDict()._get_type_dict(type_dict, data_dict)
                data_structure_list.append(type_dict)
            result = []
            message_count = {}
            for j in range(len(q_result)):
                result.append((q_result[j][0], q_result[j][1], data_structure_list[j]))
                message_count[q_result[j][0]] = q_result[j][3]
            message_count_result = [(k, v) for k, v in message_count.items()]
            return message_count_result, result
        else:
            return [], q_result

    def _pg_get_data_structure(self, topic: str = None):
        """
        Print structure of the json-data column for the specific topic(s).

        Parameters
        ----------
        topic : list or list of str, optional
            list of the topics to show data structure for.
            Have higher priority, than those defined by `topic()` and `set_filter()` methods
            and will override them.
            If not specified, shows data structure for all topics.
        """
        filter_by = self._summarize_constraints()

        if topic is not None:
            if isinstance(topic, list):
                filter_by["topic"] = topic
            elif isinstance(topic, str):
                filter_by["topic"] = [topic]
            else:
                print("`topic` must be a list of str")

        structure = self._download_data_structure(
            filter_by=filter_by, out_format="str"
        )

        if structure is None:
            return

        topic_dict = {}
        for item in structure:
            key = item[0]
            val = item[1:]
            if key in topic_dict:
                topic_dict[key].append(val)
            else:
                topic_dict[key] = [val]

        result_dict = {}
        for topic_name, item in topic_dict.items():
            result_dict[topic_name] = {}
            for tp, struct in item:
                if struct in result_dict[topic_name]:
                    result_dict[topic_name][struct].append(tp)
                else:
                    result_dict[topic_name][struct] = [tp]
        result_list = []
        for topic_name, val in result_dict.items():
            for struct, type_list in val.items():
                result_list.append([topic_name, "\n".join(type_list), struct])
        header = ["topic", "type", "data"]
        table = PrettyTable(field_names=header, align="r")
        table.align["data"] = "l"
        table.hrules = ALL
        table.add_rows(result_list)
        print(table)

    def _sid_info_query(self, group_by=None, filter_by=None):
        """
        Return information about the data for specified groups.

        Group data and return time of the start, end and duration, and number of message counts.

        Parameters
        ----------
        group_by : list, optional
            Labels of the columns to group by. If blank, do not group.
        filter_by : dict, optional
            Constraints.

        Returns
        -------
        df : pandas.DataFrame
            Contains columns specified in `group_by`, time of the start, end, duration, and number of messages.
        """
        if group_by is None:
            group_by = []
        query_str = "MIN(time) as minTime, MAX(time) as maxTime, (MAX(time) - MIN(time)) as \
                                    diffTime, COUNT(*) FROM {}"

        param_execute = []
        param_sql = []
        query_filter, param_sql_filtr, param_execute_filtr = self._resolve_filter_by(
            filter_by
        )
        # param_sql += param_sql_filtr
        param_execute += param_execute_filtr

        if len(group_by) != 0:
            query_str = "{}, " + query_str
            query_group_str = " GROUP BY {}"
            param_group_by_sql = sql.SQL(",").join(list(map(sql.Identifier, group_by)))
            param_sql = [
                param_group_by_sql,
                sql.Identifier(self._simulation, self._batch_name),
                *param_sql_filtr,
                param_group_by_sql,
            ]
        else:
            query_group_str = ""
            param_sql = [sql.Identifier(self._simulation, self._batch_name), *param_sql_filtr]

        query = sql.SQL("SELECT " + query_str + query_filter + query_group_str)
        # do not check if the batch exists and downloaded because it was done in _general_info
        result = self._execute_query(
            query.format(*param_sql), param_execute, check_batch=False
        )["res"]
        if result is not None:
            header = group_by + [
                "startTime",
                "endTime",
                "duration",
                "number of messages",
            ]
            df = pd.DataFrame(result, columns=header)
            return df
        else:
            return None

    def _get_keys_from_dict(self, d, keys, pre):
        """
        Recursive search for the full key name of the all dictionary levels.

        Parameters
        ----------
        d : dict
            The input dict.
        keys : list
            list to write the result into it.
        pre : list
            Prefix of the names.
        """
        for k, v in d.items():
            if isinstance(v, dict):
                self._get_keys_from_dict(v, keys, pre=pre + [k])
            else:
                keys.append(".".join(pre + [k]))

    def _get_unique_values(
        self, column_names: Optional[Union[str, list]], filter_by: dict = None
    ) -> list:
        """
        Return unique values of the columns `column_names`.

        Parameters
        ----------
        column_names : str or list of str
            Columns for which the unique combinations of the values will be found.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}.<br />
            key_n - must match labels of the columns, <br />
            value_n  - in the case of equality: list of exact values,<br />
                       in the case of inequality: dict with ">", ">=", "<" or "<=".<br />
            Conditions, passed here, have higher priority over those defined by `topic()`, `rid()`, `sid()`, `time()` and `set_filter()` and will override them.

        Returns
        -------
        list or list of tuples
            Each tuple contains unique combinations of the values for `column_names`.
        """
        filter_by_default = self._summarize_constraints()

        if filter_by is None:
            filter_by = filter_by_default
        else:
            filter_by = {**filter_by_default, **filter_by}

        if isinstance(column_names, str):
            column_names = [column_names]

        param_sql = []
        param_execute = []

        query_column, col_label, json_labels = self._resolve_query_json(column_names)
        param_sql += col_label
        param_execute += json_labels

        query_filter, param_sql_filtr, param_execute_filtr = self._resolve_filter_by(
            filter_by
        )
        param_sql += param_sql_filtr
        param_execute += param_execute_filtr
        query = sql.SQL(
            "SELECT DISTINCT " + query_column + " FROM {table}" + query_filter
        ).format(*param_sql, table=sql.Identifier(self._simulation, self._batch_name))
        query_result = self._execute_query(query, param_execute)
        data = query_result["res"]
        if data is not None:
            if len(column_names) == 1:
                result = [item[0] for item in data]
            else:
                result = data
            return result
        else:
            return []

    def _general_info_query(self, filter_by: dict = None) -> list:
        param_sql = []
        param_execute = []

        query_filter, param_sql_filtr, param_execute_filtr = self._resolve_filter_by(
            filter_by
        )
        param_sql += param_sql_filtr
        param_execute += param_execute_filtr

        query = sql.SQL(
            """
                        SELECT 
                          pg_size_pretty(SUM(pg_column_size(t.*))) AS total_size,
                          string_agg(DISTINCT t.topic::text, ', ') AS unique_topics,
                          string_agg(DISTINCT t.sid::text, ', ') AS unique_sids,
                          COUNT(t.*) AS n
                        FROM (
                            SELECT * FROM {table}"""
            + query_filter
            + """) AS t;"""
        ).format(*param_sql, table=sql.Identifier(self._simulation, self._batch_name))
        query_result = self._execute_query(query, param_execute)
        data = query_result["res"]
        error_name = query_result["error"]
        if data is not None:
            table_size = data[0][0]
            try:
                unique_topic = data[0][1].split(", ")
            except:
                unique_topic = []
            try:
                unique_sid = [int(x) for x in data[0][2].split(", ")]
            except:
                unique_sid = []
            try:
                n = int(data[0][3])
            except:
                n = 0
            return table_size, unique_topic, unique_sid, n, False, error_name
        else:
            return "", [], [], 0, True, error_name

    def _get_min_max_value(
        self,
        column_name: str,
        filter_by: dict = None,
        return_index: bool = False,
        mode="MAX",
    ):
        """
        Return maximum value of the column `column_name`.

        Parameters
        ----------
        column_name : str
            Label of the column.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}.<br />
            key_n - must match labels of the columns, <br />
            value_n  - in the case of equality: list of exact values,<br />
                       in the case of inequality: dict with ">", ">=", "<" or "<=".<br />
            Conditions, passed here, have higher priority over those defined by `topic()`, `rid()`, `sid()`, `time()` and `set_filter()` and will override them.
        return_index : bool, default False
            If True, the pair of sid and rid corresponding to the obtained minimum/maximum value is also returned.

        Returns
        -------
        value: int, float, str or None
            Minimum or maximum value of the column `column_name`.
        sid : int
            Corresponding to the minimum/maximum value's sid. Returns only if `return_index` is set to True.
        rid : int
            Corresponding to the minimum/maximum value's rid. Returns only if `return_index` is set to True.
        """
        filter_by_default = self._summarize_constraints()

        if filter_by is None:
            filter_by = filter_by_default
        else:
            filter_by = {**filter_by_default, **filter_by}

        if not isinstance(column_name, str):
            print("Error: `column_name` must be a str")
            return None
        if mode not in ["MIN", "MAX"]:
            print('mode is not supported, should be "MIN" or "MAX"')
            if return_index:
                return None, None, None
            else:
                return None

        all_additional_columns = self._all_additional_columns
        param_sql = []
        param_execute = []
        if column_name not in all_additional_columns:
            query_json, col_label, json_labels = self._resolve_query_json([column_name])
            query_row = "(" + query_json + ")::NUMERIC"
            param_sql += col_label
            param_execute += json_labels
        else:
            query_row = "{}"
            param_sql += [sql.Identifier(column_name)]

        query_filter, param_sql_filter, param_execute_filter = self._resolve_filter_by(
            filter_by
        )

        if return_index:
            param_sql = param_sql * 2 + param_sql_filter
            param_execute = param_execute * 2 + param_execute_filter
            query = sql.SQL(
                """
                            SELECT col_x, sid, rid
                            FROM (
                                SELECT """
                + query_row
                + """ as col_x, sid, rid, 
                                       """
                + mode
                + """("""
                + query_row
                + """) OVER () AS extremum_x
                                FROM {table_name}"""
                + query_filter
                + """) AS t
                            WHERE col_x = extremum_x;"""
            ).format(*param_sql, table_name=sql.Identifier(self._simulation, self._batch_name))

        else:
            param_sql += param_sql_filter
            param_execute += param_execute_filter
            query = sql.SQL(
                "SELECT "
                + mode
                + "("
                + query_row
                + ") FROM {table_name}"
                + query_filter
            ).format(*param_sql, table_name=sql.Identifier(self._simulation, self._batch_name))
        query_result = self._execute_query(query, param_execute)
        result = query_result["res"]

        if isinstance(result, list):
            if len(result) == 0:
                result = None
        if result is not None:
            if not return_index:
                return result[0][0]
            elif return_index and len(result) == 1:
                return result[0]
            else:
                sid_list = []
                rid_list = []
                for item in result:
                    sid_list.append(item[1])
                    rid_list.append(item[2])
                return result[0][0], sid_list, rid_list
        else:
            if return_index:
                return None, None, None
            else:
                return None

    def _get_counts(
        self,
        column_name: str = None,
        group_by: Optional[Union[str, list]] = None,
        filter_by: dict = None,
        nan_exclude: bool = False,
    ) -> list:
        """
        Return number of the rows in the column `column_name`.

        Parameters
        ----------
        column_name : str
            Label of the column.
        group_by : list, optional
            Labels of the columns to group by. If blank, do not group.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}.<br />
            key_n - must match labels of the columns, <br />
            value_n  - in the case of equality: list of exact values, <br />
                       in the case of inequality: dict with ">", ">=", "<" or "<=".<br />
            Conditions, passed here, have higher priority over those defined by `topic()`, `rid()`, `sid()`, `time()` and `set_filter()` and will override them.
        nan_exclude : bool, default False
            If True, nan values are excluded from the count.

        Returns
        -------
        list of tuples or None
            Number of rows in `column_name`.
        """
        if group_by is None:
            group_by = []
        elif isinstance(group_by, str):
            group_by = [group_by]

        filter_by_default = self._summarize_constraints()
        if filter_by is None:
            filter_by = filter_by_default
        else:
            filter_by = {**filter_by_default, **filter_by}

        if column_name is None or column_name == "" or column_name == "*":
            query_column = "*"
        elif not isinstance(column_name, str):
            print("Error: column_name must be a str")
            return None
        else:
            query_column = ""

        all_additional_columns = self._all_additional_columns
        param_sql = []
        param_execute = []
        if query_column != "*":
            if column_name not in all_additional_columns:
                query_column, col_label, json_labels = self._resolve_query_json(
                    [column_name], null_wrap=nan_exclude
                )
                param_sql += col_label
                param_execute += json_labels
            else:
                query_column = "{}"
                param_sql += [sql.Identifier(column_name)]

        # group by
        if len(group_by) != 0:
            query_group, group_label, json_group = self._resolve_query_json(group_by)

            param_sql = group_label + param_sql
            param_execute = json_group + param_execute

        # filter
        query_filter, param_sql_filter, param_execute_filter = self._resolve_filter_by(
            filter_by
        )
        param_sql += param_sql_filter
        param_execute += param_execute_filter

        if len(group_by) != 0:
            param_sql += group_label
            param_execute += json_group

        if len(group_by) == 0:
            query = sql.SQL(
                "SELECT COUNT(" + query_column + ") FROM {table_name}" + query_filter
            ).format(*param_sql, table_name=sql.Identifier(self._simulation, self._batch_name))
        else:
            query = sql.SQL(
                "SELECT "
                + query_group
                + ", COUNT("
                + query_column
                + ") FROM {table_name}"
                + query_filter
                + " GROUP BY "
                + query_group
            ).format(*param_sql, table_name=sql.Identifier(self._simulation, self._batch_name))
        query_result = self._execute_query(query, param_execute)

        return query_result["res"]

    def _get_unique_counts(
        self,
        column_name: str = None,
        group_by: list = None,
        filter_by: dict = None,
        nan_exclude: bool = False,
    ) -> list:
        """
        Return number of the unique values in the column `column_name`.

        Parameters
        ----------
        column_name : str
            Column to count its unique values.
        group_by : list, optional
            Labels of the columns to group by. If blank, do not group.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}.<br />
            key_n - must match labels of the columns, <br />
            value_n  - in the case of equality: list of exact values, <br />
                       in the case of inequality: dict with ">", ">=", "<" or "<=".<br />
            Conditions, passed here, have higher priority over those defined by `topic()`, `rid()`, `sid()`, `time()` and `set_filter()` and will override them.
        nan_exclude : bool, default False
            If True, nan values are excluded from the count.

        Returns
        -------
        list of tuples or None
            Counts of the unique values in `column_name`.
        """
        if group_by is None:
            group_by = []
        elif isinstance(group_by, str):
            group_by = [group_by]

        filter_by_default = self._summarize_constraints()
        if filter_by is None:
            filter_by = filter_by_default
        else:
            filter_by = {**filter_by_default, **filter_by}

        if column_name is None or column_name == "" or column_name == "*":
            query_column = "*"
        elif not isinstance(column_name, str):
            print("Error: `column_name` must be a str")
            return None
        else:
            query_column = ""

        all_additional_columns = self._all_additional_columns
        param_sql = []
        param_execute = []
        if query_column != "*":
            if column_name not in all_additional_columns:
                query_json, col_label, json_labels = self._resolve_query_json(
                    [column_name], null_wrap=nan_exclude
                )
                query_column = "(" + query_json + ")"
                param_sql += col_label
                param_execute += json_labels
            else:
                query_column = "{}"
                param_sql += [sql.Identifier(column_name)]

        # group by
        if len(group_by) != 0:
            query_group, group_label, json_group = self._resolve_query_json(group_by)

            if query_column != "*":
                param_sql = group_label + param_sql
                param_execute = json_group + param_execute

        # filter
        query_filter, param_sql_filter, param_execute_filter = self._resolve_filter_by(
            filter_by
        )
        param_sql += param_sql_filter
        param_execute += param_execute_filter

        if query_column == "*" and len(group_by) != 0:
            param_sql = group_label + param_sql + group_label
            param_execute = json_group + param_execute + json_group

        if len(group_by) == 0:
            if query_column == "*":
                query = sql.SQL(
                    "SELECT COUNT(*) FROM (SELECT DISTINCT * FROM {table_name}"
                    + query_filter
                    + ") as temp"
                ).format(*param_sql, table_name=sql.Identifier(self._simulation, self._batch_name))
            else:
                query = sql.SQL(
                    "SELECT COUNT(col_q) FROM (SELECT DISTINCT "
                    + query_column
                    + " as col_q FROM {table_name}"
                    + query_filter
                    + ") as temp"
                ).format(*param_sql, table_name=sql.Identifier(self._simulation, self._batch_name))
        else:
            query_group_as_col = []
            query_group_col = []
            for i, item in enumerate(query_group.split(", ")):
                query_group_as_col.append(item + " as col" + str(i))
                query_group_col.append("col" + str(i))
            query_group_as_col = ", ".join(query_group_as_col)
            query_group_col = ", ".join(query_group_col)
            if query_column == "*":
                query = sql.SQL(
                    "SELECT "
                    + query_group
                    + ", COUNT(*) FROM (SELECT DISTINCT * FROM {table_name}"
                    + query_filter
                    + ") as temp GROUP BY "
                    + query_group
                ).format(*param_sql, table_name=sql.Identifier(self._simulation, self._batch_name))
            else:
                query = sql.SQL(
                    "SELECT "
                    + query_group_col
                    + ", COUNT(col_q) FROM (SELECT DISTINCT "
                    + query_group_as_col
                    + ", "
                    + query_column
                    + " as col_q FROM {table_name}"
                    + query_filter
                    + ") as temp GROUP BY "
                    + query_group_col
                ).format(*param_sql, table_name=sql.Identifier(self._simulation, self._batch_name))
        query_result = self._execute_query(query, param_execute)
        return query_result["res"]

    def _get_data(
        self,
        data_query=None,
        additional_columns=None,
        filter_by=None,
        order_by=None,
        method="",
        n_avg=1,
        n_skip=1,
    ):
        """
        Return data from the database.

        Parameters
        ----------
        data_query : list, optional
            Labels of the data to download from the json-format column 'data'.
            For example, if the value of 'x' from json-format 'data' is desired, data_query = ['data.x'].
            If blank list, then all columns are are downloaded.
        additional_columns : list, optional
            Columns to download outside the json 'data'.
            If blank list, then columns ['sid', 'rid', 'time', 'topic', 'type'] are downloaded.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}.<br />
            key_n - must match labels of the columns,<br />
            value_n  - in the case of equality: list of exact values, <br />
                       in the case of inequality: dict with ">", ">=", "<" or "<=".<br />
            If sampling method is used, constraints on additional columns are applied BEFORE sampling while
            constraints on columns from json-data are applied AFTER sampling.
        order_by : dict, optional
            Keys must match labels of the columns, values specify ascending ('asc') or descending ('desc') order.
        method : {'', 'skip', 'avg', 'move_avg'}
            Method of sampling:
            'avg' - average - average `n_avg` rows;
            'move_avg' - moving average - average over `n_avg` rows and return every `n_skip`-th row;
            'skip' - skipping `n_skip` rows;
            '' - no sampling.
            If not specified, no sampling is applied
        n_avg : int, default 1
            Used only if `method` is 'move_avg' or 'avg'.
            Number of rows for averaging.
        n_skip : int, default 1
            Used only if `method` is 'move_avg' or 'skip'.
            Number of rows to skip in a result output.
            For example, if skip = 2, only every second row will be returned.

        Returns
        -------
        pandas.DataFrame
            Data from the database.
        """
        if data_query is None:
            data_query = ["data"]
            divide_by_columns = True
        else:
            divide_by_columns = False
        if additional_columns is None:
            additional_columns = []
        if filter_by is None:
            filter_by = {}
        if order_by is None:
            order_by = {}

        if not isinstance(additional_columns, list):
            print("Error: `additional_columns` must be a list")
            return None
        if not isinstance(data_query, list):
            print("Error: `data_query` must be a list")
            return None

        if method == "":
            df = self._get_data_all(
                data_query=data_query,
                additional_columns=additional_columns,
                filter_by=filter_by,
                order_by=order_by,
            )

        elif method == "skip":
            df = self._skip_rows(
                data_query=data_query,
                additional_columns=additional_columns,
                filter_by=filter_by,
                order_by=order_by,
                n_skip=n_skip,
            )

        elif method == "move_avg":
            df = self._moving_average(
                data_query=data_query,
                additional_columns=additional_columns,
                filter_by=filter_by,
                order_by=order_by,
                n_avg=n_avg,
                n_skip=n_skip,
            )

        elif method == "avg":
            df = self._average(
                data_query=data_query,
                additional_columns=additional_columns,
                filter_by=filter_by,
                order_by=order_by,
                n_avg=n_avg,
            )
        else:
            if self._debug:
                raise NameError('method "{}" does not exist'.format(method))
            else:
                print('method "{}" does not exist'.format(method))
                return None
        if df is not None:
            if divide_by_columns:
                df["data"] = df["data"].apply(
                    lambda x: json.dumps(x) if isinstance(x, dict) else x
                )

                normalized_data = pd.json_normalize(df["data"].apply(json.loads))
                normalized_data = normalized_data.add_prefix("data.")

                df = pd.concat([df.drop(columns="data"), normalized_data], axis=1)

            return df.fillna(np.nan)
        else:
            return None

    def _get_data_all(
        self, data_query=None, additional_columns=None, filter_by=None, order_by=None
    ):
        """
        Return data from database without sampling.

        Parameters
        ----------
        data_query : list, optional
            Labels of the data to download from the json-format column "data".
            If blank list, then all columns are are downloaded.
        additional_columns : list, optional
            Columns to download outside the json "data".
            If blank list, then all columns are are downloaded.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}.<br />
            key_n - must match labels of the columns, <br />
            value_n  - in the case of equality: list of exact values, <br />
                       in the case of inequality: dict with ">", ">=", "<" or "<=".
        order_by : dict, optional
            Keys must match labels of the columns, values specify ascending ('asc') or descending ('desc') order.

        Returns
        -------
        pandas.DataFrame
            Data from the database.
        """
        if data_query is None:
            data_query = []
        if additional_columns is None:
            additional_columns = []
        if filter_by is None:
            filter_by = {}
        if order_by is None:
            order_by = {}
        param_sql = []
        param_execute = []
        all_additional_columns = self._all_additional_columns
        if len(additional_columns) == 0:
            column_order = all_additional_columns

        else:
            column_order = (
                (["sid"] if "sid" in additional_columns else [])
                + (["rid"] if "rid" in additional_columns else [])
                + (["time"] if "time" in additional_columns else [])
                + (["topic"] if "topic" in additional_columns else [])
                + (["type"] if "type" in additional_columns else [])
            )
            column_order += [
                item for item in additional_columns if item not in column_order
            ]
        if len(column_order) != 0:
            query_addColumn = ["{}"]
            param_sql.append(sql.SQL(",").join(list(map(sql.Identifier, column_order))))
        else:
            query_addColumn = []

        query_json, col_label, json_labels = self._resolve_query_json(data_query)
        param_sql += col_label
        param_execute += json_labels

        query_filter, param_sql_filter, param_execute_filter = self._resolve_filter_by(
            filter_by
        )
        param_sql += param_sql_filter
        param_execute += param_execute_filter

        query_order, param_sql_order, param_execute_order = self._resolve_order_by(
            order_by
        )
        param_sql += param_sql_order
        param_execute += param_execute_order

        query = sql.SQL(
            "SELECT "
            + ", ".join(query_addColumn + [query_json])
            + " FROM {table}"
            + query_filter
            + query_order
        ).format(*param_sql, table=sql.Identifier(self._simulation, self._batch_name))

        query_result = self._execute_query(query, param_execute)
        data = query_result["res"]
        if data is not None:
            colnames = column_order + data_query
            df = pd.DataFrame(data, columns=colnames)
            return df
        else:
            return None

    def _skip_rows(
        self,
        data_query=None,
        additional_columns=None,
        filter_by=None,
        order_by=None,
        n_skip=1,
    ):
        """
        Pick every n-th row from the databes.

        Parameters
        ----------
        data_query : list, optional
            Labels of the data to download from the json-format column "data".
            If blank list, then all columns are are downloaded.
        additional_columns : list, optional
            Columns to download outside the json "data".
            If blank list, then all columns are are downloaded.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}.<br />
            key_n - must match labels of the columns, <br />
            value_n  - in the case of equality: list of exact values <br />
                       in the case of inequality: dict with ">", ">=", "<" or "<=".
        order_by : dict, optional
            Keys must match labels of the columns, values specify ascending ('asc') or descending ('desc') order.
        n_skip : int, default 1
            Number of rows to skip in a result output.
            For example, if skip = 2, only every second row will be returned.

        Returns
        -------
        pandas.DataFrame
            Data from the database.
        """
        if additional_columns is None:
            additional_columns = []
        if filter_by is None:
            filter_by = {}
        if order_by is None:
            order_by = {}
        if n_skip <= 0:
            print("`n_skip` must be > 0")
            return None
        if not isinstance(n_skip, int):
            try:
                n_skip = int(n_skip)
            except Exception:
                print("`n_skip` must be int")
                return None
        param_sql = []
        param_execute = []
        all_additional_columns = self._all_additional_columns

        if len(additional_columns) == 0:
            column_order = all_additional_columns
        else:
            column_order = (
                (["sid"] if "sid" in additional_columns else [])
                + (["rid"] if "rid" in additional_columns else [])
                + (["time"] if "time" in additional_columns else [])
                + (["topic"] if "topic" in additional_columns else [])
                + (["type"] if "type" in additional_columns else [])
            )

            column_order += [
                item for item in additional_columns if item not in column_order
            ]
        if len(column_order) != 0:
            query_addColumn = ["{}"]
            param_sql.append(sql.SQL(",").join(list(map(sql.Identifier, column_order))))
        else:
            query_addColumn = []

        query_json, col_label, json_labels = self._resolve_query_json(data_query)
        param_sql += col_label
        param_execute += json_labels

        filter_add_column = {}
        filter_data = {}
        for k, v in filter_by.items():
            if k in all_additional_columns or k in column_order:
                filter_add_column[k] = v
            else:
                filter_data[k] = v

        (
            query_filter_add_col,
            param_sql_filter_add_col,
            param_execute_filter_add_col,
        ) = self._resolve_filter_by(filter_add_column)
        param_sql += param_sql_filter_add_col
        param_execute += param_execute_filter_add_col

        (
            query_filter_data,
            param_sql_filter_data,
            param_execute_filter_data,
        ) = self._resolve_filter_by(filter_data)
        param_sql += param_sql_filter_data
        param_execute += param_execute_filter_data

        query_main = (
            "(SELECT *, row_number() OVER (PARTITION BY topic, sid ORDER BY rid) as index FROM {table} "
            + query_filter_add_col
            + ") as a "
        )

        if query_filter_data == "":
            query_skip = "WHERE (index - 1) %% %s = 0 "
        else:
            query_skip = " AND (index - 1) %% %s = 0 "
        param_execute += [n_skip]

        query_order, param_sql_order, param_execute_order = self._resolve_order_by(
            order_by
        )
        param_sql += param_sql_order
        param_execute += param_execute_order

        query = sql.SQL(
            "SELECT "
            + ",".join(query_addColumn + [query_json])
            + " FROM "
            + query_main
            + query_filter_data
            + query_skip
            + query_order
        ).format(*param_sql, table=sql.Identifier(self._simulation, self._batch_name))

        query_result = self._execute_query(query, param_execute)
        data = query_result["res"]
        if data is not None:
            colnames = column_order + data_query
            df = pd.DataFrame(data, columns=colnames)
            return df
        else:
            return None

    def _average(
        self,
        data_query=None,
        additional_columns=None,
        filter_by=None,
        order_by=None,
        n_avg=1,
    ):
        """
        Averaging data and return it from the database.

        Parameters
        ----------
        data_query : list
            Labels of the data to download from the json-format column "data".
            If blank list, then all columns are are downloaded.
        additional_columns : list
            Columns to download outside the json "data".
            If blank list, then all columns are are downloaded.
        filter_by : dict
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}.<br />
            key_n - must match labels of the columns, <br />
            value_n  - in the case of equality: list of exact values, <br />
                       in the case of inequality: dict with ">", ">=", "<" or "<=".
            Conditions, passed here, have higher priority, than defined by `topic()`, `rid()`, `sid()` and `time()`.
        order_by : dict
            Keys must match labels of the columns, values specify ascending ('asc') or descending ('desc') order.
        n_avg : int
            Number of rows for averaging.

        Returns
        -------
        pandas.DataFrame
            Data from the database.
        """
        if additional_columns is None:
            additional_columns = []
        if filter_by is None:
            filter_by = {}
        if order_by is None:
            order_by = {}
        if n_avg <= 0:
            print("`n_avg` must be > 0")
            return None
        if not isinstance(n_avg, int):
            try:
                n_avg = int(n_avg)
            except Exception:
                print("n_avg must be int")
                return None
        param_sql = []
        param_execute = []
        all_additional_columns = self._all_additional_columns

        if len(additional_columns) == 0:
            column_order = all_additional_columns
        else:
            column_order = (
                (["sid"] if "sid" in additional_columns else [])
                + (["rid"] if "rid" in additional_columns else [])
                + (["time"] if "time" in additional_columns else [])
                + (["topic"] if "topic" in additional_columns else [])
                + (["type"] if "type" in additional_columns else [])
            )
            column_order += [
                item for item in additional_columns if item not in column_order
            ]
        if len(column_order) != 0:
            query_addColumn = ["{}"]
        else:
            query_addColumn = []

        group_avg_query_list = ["topic", "sid"]
        group_avg_query = ", ".join(group_avg_query_list)

        additional_columns_main = column_order.copy()
        if len(order_by) != 0:
            for item in order_by.keys():
                if (
                    item not in additional_columns_main
                    and item in all_additional_columns
                ):
                    additional_columns_main.append(item)

        data_query_main = data_query.copy()

        for k, v in filter_by.items():
            if not (k in all_additional_columns or k in column_order):
                if k not in data_query:
                    data_query.append(k)

        for k, v in order_by.items():
            if not (k in all_additional_columns or k in column_order):
                if k not in data_query:
                    data_query.append(k)

        query_json_labels = {}
        for i, item in enumerate(data_query):
            query_json_labels[item] = "col" + str(i)

        filter_add_column = {}
        filter_data = {}
        for k, v in filter_by.items():
            if k in all_additional_columns or k in column_order:
                filter_add_column[k] = v
            else:
                filter_data[query_json_labels[k]] = v

        order_by_rev = {}
        if len(order_by) != 0:
            for k, v in order_by.items():
                if k in all_additional_columns or k in column_order:
                    order_by_rev[k] = v
                else:
                    order_by_rev[query_json_labels[k]] = v

        query_json, col_label, json_labels = self._resolve_query_json(data_query)

        additional_columns_avg = column_order.copy()
        if len(order_by) != 0:
            for item in order_by.keys():
                if (
                    item not in additional_columns_avg
                    and item in all_additional_columns
                ):
                    additional_columns_avg.append(item)

        query_addColumn_avg_list = []
        addColumn_avg_list = []
        if "sid" in additional_columns_avg:
            addColumn_avg_list.append(" sid ")
            additional_columns_avg.remove("sid")

        if "rid" in additional_columns_avg:
            addColumn_avg_list.append(" MIN(rid) as rid ")
            additional_columns_avg.remove("rid")

        if "time" in additional_columns_avg:
            addColumn_avg_list.append(" AVG(time) as time ")
            additional_columns_avg.remove("time")

        if "topic" in additional_columns_avg:
            addColumn_avg_list.append(" topic ")
            additional_columns_avg.remove("topic")

        if "type" in additional_columns_avg:
            addColumn_avg_list.append(" MIN(type) as type ")
            additional_columns_avg.remove("type")

        if len(additional_columns_avg) != 0:
            for item in additional_columns_avg:
                query_addColumn_avg_list.append(item)
            addColumn_avg_list.append("{}")

        for item in group_avg_query_list:
            if item not in additional_columns_main:
                additional_columns_main.append(item)

        query_json_main = []
        for q, item in zip(query_json.split(", "), data_query):
            query_json_main.append(q + " as " + query_json_labels[item])

        query_json_avg_list = []
        json_labels_list = []
        for item in data_query:
            query_json_avg_list.append(
                " AVG(("
                + query_json_labels[item]
                + ")::NUMERIC) as "
                + query_json_labels[item]
            )
        for item in data_query_main:
            json_labels_list.append(query_json_labels[item])

        (
            query_filter_data,
            param_sql_filter_data,
            param_execute_filter_data,
        ) = self._resolve_filter_by(filter_data)
        (
            query_filter_add_col,
            param_sql_filter_add_col,
            param_execute_filter_add_col,
        ) = self._resolve_filter_by(filter_add_column)
        query_order, param_sql_order, param_execute_order = self._resolve_order_by(
            order_by_rev
        )

        # query_avg
        if len(query_addColumn_avg_list) != 0:
            param_sql += [
                sql.SQL(",").join(list(map(sql.Identifier, query_addColumn_avg_list)))
            ]

        # main_query
        if len(additional_columns_main) != 0:
            param_sql += [
                sql.SQL(",").join(list(map(sql.Identifier, additional_columns_main)))
            ]
        param_sql += col_label
        param_execute += json_labels
        param_sql += param_sql_filter_add_col
        param_execute += param_execute_filter_add_col

        # query_group_avg
        param_execute += [n_avg]

        # query_filter_data
        if query_filter_data != "":
            param_sql += param_sql_filter_data
            param_execute += param_execute_filter_data

        # query_order
        param_sql += param_sql_order
        param_execute += param_execute_order

        query_avg = (
            "SELECT " + ", ".join(addColumn_avg_list + query_json_avg_list) + " FROM"
        )

        main_query = (
            "(SELECT "
            + ", ".join(
                query_addColumn
                + query_json_main
                + [
                    "row_number() OVER (PARTITION BY "
                    + group_avg_query
                    + " ORDER BY rid) as index"
                ]
            )
            + " FROM {table}"
            + query_filter_add_col
            + ") as A"
        )

        query_group_avg = " GROUP BY (index-1) / %s, " + group_avg_query

        if query_filter_data != "":
            query = sql.SQL(
                "SELECT "
                + ",".join(column_order + json_labels_list)
                + " FROM ("
                + query_avg
                + main_query
                + query_group_avg
                + ") as b "
                + query_filter_data
                + query_order
            ).format(*param_sql, table=sql.Identifier(self._simulation, self._batch_name))
        else:
            query = sql.SQL(
                query_avg + main_query + query_group_avg + query_order
            ).format(*param_sql, table=sql.Identifier(self._simulation, self._batch_name))
        query_result = self._execute_query(query, param_execute)
        data = query_result["res"]
        if data is not None:
            colnames = column_order + data_query_main
            df = pd.DataFrame(data, columns=colnames)
            return df
        else:
            return None

    def _moving_average(
        self,
        data_query=None,
        additional_columns=None,
        filter_by=None,
        order_by=None,
        n_avg=1,
        n_skip=1,
    ):
        """
        Calculate moving average and return every n-th row.

        Parameters
        ----------
        data_query : list, optional
            Labels of the data to download from the json-format column "data".
            If blank list, then all columns are are downloaded.
        additional_columns : list, optional
            Columns to download outside the json "data".
            If blank list, then all columns are are downloaded.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}.<br />
            key_n - must match labels of the columns, <br />
            value_n  - in the case of equality: list of exact values<br />
                       in the case of inequality: dict with ">", ">=", "<" or "<=".<br />
            Conditions, passed here, have higher priority, than defined by `topic()`, `rid()`, `sid()` and `time()`.
        order_by : dict, optional
            Keys must match labels of the columns, values specify ascending ('asc') or descending ('desc') order.
        n_avg : int, default 1
            Number of rows for averaging.
        n_skip : int, default 1
            Number of rows to skip in a result output.
            For example, if skip = 2, only every second row will be returned.

        Returns
        -------
        pandas.DataFrame
            Data from the database.
        """
        if additional_columns is None:
            additional_columns = []
        if filter_by is None:
            filter_by = {}
        if order_by is None:
            order_by = {}
        if n_skip <= 0:
            print("`n_skip` must be > 0")
            return None
        if not isinstance(n_skip, int):
            try:
                n_skip = int(n_skip)
            except Exception:
                print("n_skip must be int")
                return None
        if n_avg <= 0:
            print("`n_avg` must be > 0")
            return None
        if not isinstance(n_avg, int):
            try:
                n_avg = int(n_avg)
            except Exception:
                print("n_avg must be int")
                return None
        param_sql = []
        param_execute = []
        all_additional_columns = self._all_additional_columns

        partition_query_list = ["sid", "topic"]
        partition_query = ", ".join(partition_query_list)

        if len(additional_columns) == 0:
            column_order = all_additional_columns
        else:
            column_order = (
                (["sid"] if "sid" in additional_columns else [])
                + (["rid"] if "rid" in additional_columns else [])
                + (["time"] if "time" in additional_columns else [])
                + (["topic"] if "topic" in additional_columns else [])
                + (["type"] if "type" in additional_columns else [])
            )

            column_order += [
                item for item in additional_columns if item not in column_order
            ]

        additional_columns_main = column_order.copy()
        if len(order_by) != 0:
            for item in order_by.keys():
                if (
                    item not in additional_columns_main
                    and item in all_additional_columns
                ):
                    additional_columns_main.append(item)
        if "rid" not in additional_columns_main:
            additional_columns_main = ["rid"] + additional_columns_main

        data_query_main = data_query.copy()

        for k, v in filter_by.items():
            if not (k in all_additional_columns or k in column_order):
                if k not in data_query:
                    data_query.append(k)

        for k, v in order_by.items():
            if not (k in all_additional_columns or k in column_order):
                if k not in data_query:
                    data_query.append(k)

        query_json_labels = {}
        for i, item in enumerate(data_query):
            query_json_labels[item] = "col" + str(i)

        filter_add_column = {}
        filter_data = {}
        for k, v in filter_by.items():
            if k in all_additional_columns or k in column_order:
                filter_add_column[k] = v
            else:
                filter_data[query_json_labels[k]] = v

        order_by_rev = {}
        if len(order_by) != 0:
            for k, v in order_by.items():
                if k in all_additional_columns or k in column_order:
                    order_by_rev[k] = v
                else:
                    order_by_rev[query_json_labels[k]] = v

        query_json, col_label, json_labels = self._resolve_query_json(data_query)

        additional_columns_avg = column_order.copy()

        if len(order_by) != 0:
            for item in order_by.keys():
                if (
                    item not in additional_columns_avg
                    and item in all_additional_columns
                ):
                    additional_columns_avg.append(item)

        param_addColumn_avg = []
        query_addColumn_avg_list = []
        if "rid" in additional_columns_avg:
            query_addColumn_avg_list.append(" MIN(rid) OVER w as rid")
            additional_columns_avg.remove("rid")

        if "time" in additional_columns_avg:
            query_addColumn_avg_list.append(" AVG(time) OVER w AS time ")
            additional_columns_avg.remove("time")

        if len(additional_columns_avg) != 0:
            for item in additional_columns_avg:
                param_addColumn_avg.append(item)
            query_addColumn_avg_list.append("{}")

        for item in partition_query_list:
            if item not in additional_columns_main:
                additional_columns_main.append(item)

        addColumn_main_list = []
        for _ in additional_columns_main:
            addColumn_main_list.append("{}")

        json_main_list = []
        for q, item in zip(query_json.split(", "), data_query):
            json_main_list.append(q + " as " + query_json_labels[item])
        query_json_avg_list = []

        json_labels_list = []
        for item in data_query:
            query_json_avg_list.append(
                " AVG(("
                + query_json_labels[item]
                + ")::NUMERIC) OVER w as "
                + query_json_labels[item]
            )
        for item in data_query_main:
            json_labels_list.append(query_json_labels[item])

        (
            query_filter_data,
            param_sql_filter_data,
            param_execute_filter_data,
        ) = self._resolve_filter_by(filter_data)
        (
            query_filter_add_col,
            param_sql_filter_add_col,
            param_execute_filter_add_col,
        ) = self._resolve_filter_by(filter_add_column)
        query_order, param_sql_order, param_execute_order = self._resolve_order_by(
            order_by_rev
        )

        # query_avg
        if len(param_addColumn_avg) != 0:
            param_sql += [
                sql.SQL(",").join(list(map(sql.Identifier, param_addColumn_avg)))
            ]

        # main_query
        param_sql += list(map(sql.Identifier, additional_columns_main))
        param_sql += col_label
        param_execute += json_labels
        param_sql += param_sql_filter_add_col
        param_execute += param_execute_filter_add_col

        # query_window
        param_execute += [n_avg - 1]

        # query_filter_data
        param_sql += param_sql_filter_data
        param_execute += param_execute_filter_data

        # query_skip
        param_execute += [n_skip]

        # query_order
        param_sql += param_sql_order
        param_execute += param_execute_order

        query_avg = (
            "SELECT"
            + ", ".join(query_addColumn_avg_list + query_json_avg_list + ["index"])
            + " FROM "
        )

        main_query = (
            "(SELECT "
            + ",".join(
                addColumn_main_list
                + json_main_list
                + [
                    "row_number() OVER (PARTITION BY "
                    + partition_query
                    + " ORDER BY rid) as index"
                ]
            )
            + " FROM {table}"
            + query_filter_add_col
            + ") as A"
        )

        query_window = (
            "(PARTITION BY "
            + partition_query
            + " ORDER BY rid ROWS BETWEEN CURRENT ROW AND %s FOLLOWING )"
        )

        if query_filter_data == "":
            query_skip = " WHERE (index-1) %% %s = 0"
        else:
            query_skip = " AND (index-1) %% %s = 0"

        query = sql.SQL(
            "SELECT "
            + ",".join(column_order + json_labels_list)
            + " FROM ("
            + query_avg
            + main_query
            + " WINDOW w AS "
            + query_window
            + ") as b "
            + query_filter_data
            + query_skip
            + query_order
        ).format(*param_sql, table=sql.Identifier(self._simulation, self._batch_name))

        query_result = self._execute_query(query, param_execute)
        data = query_result["res"]
        if data is not None:
            colnames = column_order + data_query_main
            df = pd.DataFrame(data, columns=colnames)
            return df
        else:
            return None

    def data_for_time_plot(
        self, topic_name, var_name, time_step, sids, remove_nan, inf_vals
    ):
        """
        Query data for time plot.

        Parameters
        ----------
        topic_name : str
            Input topic name. If specified, will override value that was set by `topic()` method.
        var_name : str
            Name of the variable to plot along y-axis.
        time_step : float or int, default 1.0
            Time step, `Time` = `time_step` * rid.
        sids : list
            List of the sids. If specified, will override values that were set by `sid()` method.
            If not specified, data for all sids is queried.
        remove_nan : bool, default True
            If True, NaN values will be removed before plotting.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.

        Other Parameters
        ----------------
        **kwargs
            Other keyword arguments, see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)

        Returns
        -------
        df : pandas.DataFrame
            Data to plot.
        """
        if topic_name is None:
            if self._topic is not None:
                if len(self._topic) > 1:
                    print("please provide one topic instead of list of the topics")
                else:
                    topic_var = self._topic[0]
            else:
                print(
                    '"topic" is not specified, please provide it by topic() method or as an argument'
                )
                return None
        else:
            topic_var = topic_name

        if var_name is None:
            print(
                'please provide "var_name" - name of the variable to plot along y-axis'
            )
            return None

        if var_name not in ["sid", "rid", "time", "topic"]:
            data_columns = var_name
        else:
            data_columns = ["data"]

        # extract the variable dataframe from the topic struct, and sort it by sid (simulation-id) and rid (ros-id)
        df = (
            self.topic(topic_var)
            .sid(sids)
            .set_order({"sid": "asc", "rid": "asc"})
            ._data(data_columns)
        )
        if df is None:
            return None
        if len(df) == 0:
            print("there is no data matching the given criteria")
            return None
        if len(df[df[var_name].notna()]) == 0:
            print(f"there is no data for the column '{var_name}'")
            return None

        if remove_nan:
            flag = df[var_name].notna()
        else:
            flag = pd.Series(data=[True] * len(df))

        if inf_vals is not None:
            flag = flag & ((abs(df[var_name]) - inf_vals) < 0)

        if var_name == "sid":
            var_df = df[flag].set_index("sid", drop=False)
        else:
            var_df = df[flag].set_index("sid")
        var_df["Time"] = var_df["rid"] * time_step

        return var_df

    def data_for_xy_plot(
        self, topic_name, var_x_name, var_y_name, sids, remove_nan, inf_vals
    ):
        """
        Query data for xy plot.

        Parameters
        ----------
        topic_name : str
            Input topic name. If specified, will override value that was set by `topic()` method.
        var_x_name : str
            Name of the variable to plot along x-axis.
        var_y_name : str
            Name of the variable to plot along y-axis.
        sids : int or list of int, optional
            List of the sids. If specified, will override values that were set by `sid()` method.
            If not specified, data for all sids is queried.
        remove_nan : bool, default True
            If True, NaN values will be removed before plotting.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.

        Other Parameters
        ----------------
        **kwargs
            Other keyword arguments, see [matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)

        Returns
        -------
        df : pandas.DataFrame
            Data to plot.
        """
        if topic_name is None:
            if self._topic is not None:
                if len(self._topic) > 1:
                    print("please provide one topic instead of list of the topics")
                else:
                    topic_var = self._topic[0]
            else:
                print(
                    '"topic" is not specified, please provide it by topic() method or as an argument'
                )
                return None
        else:
            topic_var = topic_name

        if var_x_name is None:
            print(
                'please provide "var_x_name" - name of the variable to plot along x-axis'
            )
            return None
        if var_y_name is None:
            print(
                'please provide "var_y_name" - name of the variable to plot along y-axis'
            )
            return None

        data_columns = []

        if var_x_name not in ["sid", "rid", "time", "topic", var_y_name]:
            data_columns.append(var_x_name)
        if var_y_name not in ["sid", "rid", "time", "topic"]:
            data_columns.append(var_y_name)
        if len(data_columns) == 0:
            data_columns.append("data")

        # extract the variables dataframe from the topic struct, and sort it by sid (simulation-id) and rid (ros-id)
        df = (
            self.topic(topic_var)
            .sid(sids)
            .set_order({"sid": "asc", "rid": "asc"})
            ._data(data_columns)
        )
        if df is None:
            return None
        if len(df) == 0:
            print("there is no data matching the given criteria")
            return None
        if len(df[df[var_x_name].notna()]) == 0:
            print(f"there is no data for the column '{var_x_name}'")
            return None
        if len(df[df[var_y_name].notna()]) == 0:
            print(f"there is no data for the column '{var_y_name}'")
            return None

        if remove_nan:
            flag = df[var_x_name].notna() & df[var_y_name].notna()
        else:
            flag = pd.Series(data=[True] * len(df))

        if inf_vals is not None:
            flag = flag & (
                ((abs(df[var_x_name]) - inf_vals) < 0)
                & ((abs(df[var_y_name]) - inf_vals) < 0)
            )

        if var_x_name == "sid" or var_y_name == "sid":
            xy_df = df[flag].set_index("sid", drop=False)
        else:
            xy_df = df[flag].set_index("sid")

        if sids is None or sids == []:
            # sids = list(xy_df.columns.levels[1])
            sids = list(set(xy_df.index))
        else:
            if isinstance(sids, int):
                sids = [sids]
            # all_sids = list(xy_df.columns.levels[1])
            all_sids = list(set(xy_df.index))
            bad_sids = []
            for s in sids:
                if s not in all_sids:
                    bad_sids.append(s)
            if len(bad_sids) != 0:
                print("sids " + str(bad_sids) + " do not exist")
                sids = [s for s in sids if s not in bad_sids]
        return xy_df
