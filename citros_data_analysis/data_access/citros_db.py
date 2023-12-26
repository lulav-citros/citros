from __future__ import annotations
import pandas as pd
import matplotlib.pyplot as plt
import os
from prettytable import PrettyTable, ALL
from typing import Union, Optional, Any
import matplotlib.figure
from ._gql_cursor import _GqlCursor
from ._pg_cursor import _PgCursor
from ._plotter import _Plotter
from .citros_dict import CitrosDict
# from .references import Ref
import warnings
import time

class CitrosDB(_PgCursor, _GqlCursor):
    '''
    CitrosDB object allows to get general information about the batch and make queries.

    Parameters
    ----------
    repo : str or int, optional
        Repository name or id.
        If name is provided, searches for the exact match.
        If an integer value is provided, it determines the selection based on the order of repository creation (-1 for the last created, 0 for the first).
        Default is ENV variable "CITROS_REPO". When operating from a local environment and ENV variable is not set, `repo` is set to the 'name' field from the '.citros/project.json' file.
    simulation : str, optional
        Name of the simulation. Default is ENV variable "CITROS_SIMULATION" if it is set or None if the variable is not defined.
    batch : str or int, optional
        Batch name or id.
        If name is provided, searches for the exact match.
        If an integer value is provided, it determines the selection based on the order of batch creation (-1 for the last created, 0 for the first).
        Default is ENV variable "bid" if it is set or None if the variable is not defined.
    sid : int, optional
        Simulation run id.
        Default is ENV variable "CITROS_SIMULATION_RUN_ID" if it is set or None if the variable is not defined.
    host : str
        Database host address.
        Default is ENV variable "PG_HOST" if it is set or None if the variable is not defined.
    port : str, optional
        Default is ENV variable "PG_PORT" if it is set or None if the variable is not defined.
    database : str, optional
        Database name.
        Default is ENV variable "PG_DATABASE". When operating from a local environment and ENV variable is not set, defined by CITROS CLI authentication.
    schema : str, optional
        Default is ENV variable "PG_SCHEMA" if it is set or None if the variable is not defined.
    user : str, optional
        User name.
        Default is ENV variable "PG_USER". When operating from a local environment and ENV variable is not set, defined by CITROS CLI authentication.
    password : str, optional
        Password.
        Default is ENV variable "PG_PASSWORD". When operating from a local environment and ENV variable is not set, defined by CITROS CLI authentication.
    debug : bool, default False
        If `False`, program will try to handle errors and only print error messages without code breaking.
        If `True`, this will cause the code to abort if an error occurs.
    async_query : bool, default False
        If `False` and the batch is not yet downloaded into the database, checks the status of the batch and tries to query it during the `async_timeout` time.
    async_timeout : int, default 180
        Time of waiting for the batch to be downloaded into the database.
        Used only if `async_query` is set `False`. During this time checks the status of the batch and tries to query it.  
    '''

    def __init__(self, repo = None, simulation = None, batch = None, sid = None, host = None, port = None, database = None, schema = None, 
                   user = None, password = None, debug = False, async_query = False, async_timeout = 180):
        
        _PgCursor.__init__(self, host = host, port = port, user = user, password = password, database = database, 
                schema = schema, batch = batch, sid = sid, debug = debug, async_query = async_query, async_timeout = async_timeout)
        _GqlCursor.__init__(self, repo = repo, simulation = simulation, debug = debug)
        
        if self._user is None or self._database is None:
            try:
                user_id, user_organization = self._get_current_user_info()
            except:
                user_id = None
                user_organization = None

            if self._user is None:
                if user_id is None:
                    if self._debug:
                        raise NameError('`user` is not defined')
                    else:
                        print('`user` is not defined')
                else:
                    self._user = user_id

            if self._database is None:
                if user_organization is None:
                    if self._debug:
                        raise NameError('`database` is not defined')
                    else:
                        print('`database` is not defined')
                else:
                    self._database = user_organization
        
        if self._password is None:
            if self._user is not None:
                self._password = self._user
            else:
                if self._debug:
                    raise NameError('`password` is not provided')
                else:
                    print('`password` is not provided')

        self._set_batch(self._batch_id, exact_match = True)
        

    def _copy(self):
        '''
        Make a copy of the CitrosDB object.

        Returns
        -------
        CitrosDB
        '''
        ci = CitrosDB(repo = 'None',
                      database  = self._database,
                      batch = 'None',
                      sid = self._sid,
                      host = self._host,
                      port = self._port,
                      schema = self._schema,
                      user = self._user, 
                      password = self._password,
                      debug = self._debug,
                      async_query=self.async_query,
                      async_timeout=self.async_timeout)
        
        if self._sid is None:
            if hasattr(self, '_sid_val'):
                ci._sid_val = self._sid_val.copy()
        if hasattr(self, 'error_flag'):
            ci._error_flag = self._error_flag
        if hasattr(self, '_rid_val'):
            ci._rid_val = self._rid_val.copy()
        if hasattr(self, '_time_val'):
            ci._time_val = self._time_val.copy()
        if hasattr(self, '_filter_by'):
            ci._filter_by = self._filter_by
        if hasattr(self, '_order_by'):
            ci._order_by = self._order_by

        if hasattr(self, 'batch_status'):
            ci.batch_status = self.batch_status
        
        ci._simulation = self._simulation
        ci._repo_id = self._repo_id
        ci._repo_name = self._repo_name
        ci._batch_id = self._batch_id
        if hasattr(self, '_batch_name'):
            ci._batch_name = self._batch_name
        if hasattr(self, '_test_mode'):
            ci._test_mode = self._test_mode

        if isinstance(self._topic, list):
            ci._topic = self._topic.copy()
        elif isinstance(self._topic, str):
            ci._topic = [self._topic]
        else:
            ci._topic = None
        
        if hasattr(self, '_method'):
            ci._method = self._method
        if hasattr(self, '_n_avg'):
            ci._n_avg = self._n_avg
        if hasattr(self, '_n_skip'):
            ci._n_skip = self._n_skip
        return ci
    
    def _async_wait(self):
        '''
        Check batch status according to max wait time set by `async_timeout`,
        return True if the batch is available, otherwise False.

        Returns
        -------
        bool
            If the batch is available.
        '''
        if (self.batch_status is None) or (self.batch_status == 'ERROR'):
            return False
        if self.async_timeout < 10:
            waite_schema = [self.async_timeout]
        else:
            waite_schema = [10]
            next_t = sum(waite_schema)
            while (sum(waite_schema)+next_t) < self.async_timeout:
                waite_schema.append(next_t)
                next_t = sum(waite_schema)
            if sum(waite_schema) < self.async_timeout:
                waite_schema.append(self.async_timeout - sum(waite_schema))
        for t in waite_schema:
            time.sleep(t)
            if self._is_batch_available():
                return True
        print('Time set by async_timeout is over')
        return False

    def _is_batch_available(self):
        '''
        Check if the batch is set and in the database.
        '''
        if hasattr(self, '_test_mode'):
            return True
        
        # check if the batch is set.
        if not self._is_batch_set():
            self.batch_status = None
            return False
        else:
            # query for the batch status
            self.batch_status = self._get_batch_status(self._batch_id)

            if self.batch_status is None:
                # could not find the batch
                print(f"there is no batch with the id: '{self._batch_id}'")
                return False
            else:
                # write that user try to get batch
                self._set_data_access_time(self._batch_id)

                if self.batch_status == 'LOADED':
                    # table is not downloaded, will try to download and catch and handle error if it occurs
                    return True
                    # if async_query and table is not downloaded, will try to download and catch and handle error if it occurs
                    # if self.async_query:
                    #     return True
                    # else:
                    #     # check if this table in postgres schema
                    #     if self._is_batch_in_database(self._batch_id):
                    #         # table is really downloaded, everything is ok
                    #         return True
                    #     else:
                    #         # table is not in postgres schema, set status UNLOADED
                    #         print(f"the batch '{self._batch_name if self._batch_name is not None else 'id'}': '{self._batch_id}' exists, but not loaded into the database. We are checking")
                    #         self._set_batch_status(self._batch_id, 'UNLOADED')
                    #         self.batch_status = 'UNLOADED'
                    #         return False
                    
                elif self.batch_status == 'LOADING':
                    #batch is loading now
                    async_string =' Please wait a few minutes and try again' if self.async_query else '\nPlease keep waiting...'
                    print(f"The batch '{self._batch_name if self._batch_name is not None else 'id'}': '{self._batch_id}' is loading.{async_string}")
                        #   f"{' Please wait a few minutes and try again' if self.async_query else ''}")
                    return False
                
                elif self.batch_status == 'UNLOADED':
                    #batch is not loaded
                    async_string = '\nPlease wait a few minutes and try again' if self.async_query else '\nPlease keep waiting...'
                    print(f"The batch '{self._batch_name if self._batch_name is not None else 'id'}': '{self._batch_id}' exists"
                          f", but not loaded into the database.{async_string}")
                        #   f"\n{'Please wait a few minutes and try again' if self.async_query else ''}")
                    return False

                elif self.batch_status == 'ERROR':
                    print(f"The batch '{self._batch_name if self._batch_name is not None else 'id'}': '{self._batch_id}' can not be loaded"
                          ", batch status is 'ERROR'")
                    return False
                
                elif self.batch_status == 'UNKNOWN':
                    # check if this table is in postgres schema
                    if self._is_batch_in_database(self._batch_id):
                        self._set_batch_status(self._batch_id, 'LOADED')
                        self.batch_status = 'LOADED'
                        return True
                    else:
                        self._set_batch_status(self._batch_id, 'UNLOADED')
                        self.batch_status = 'UNLOADED'
                        async_string = '\nPlease wait a few minutes and try again' if self.async_query else '\nPlease keep waiting...'
                        print(f"The batch '{self._batch_name if self._batch_name is not None else 'id'}': '{self._batch_id}' exists, but not loaded into the database.{async_string}")
                            #   f"\n{'Please wait a few minutes and try again' if self.async_query else ''}")
                        return False
                else:
                    print(f"batch '{self._batch_name if self._batch_name is not None else 'id'}': '{self._batch_id}' has unsupported status: '{self.batch_status}'")

    def _handle_pg_error(self, error_name):
        '''
        Returns True if error was 'UndefinedTable'.
        It is the case when batch_status erroneously is 'LOADED', but batch is not downloaded into postgres.  
        In that case status is set as 'UNLOADED'
        '''
        if hasattr(self, '_test_mode'):
            print(f"The batch '{self._batch_name if self._batch_name is not None else 'id'}': '{self._batch_id}' exists, but not loaded into the database. We are checking.")
            return
        if error_name == 'UndefinedTable':
            if self.batch_status == 'LOADED':
                async_string = '\nPlease wait a few minutes and try again' if self.async_query else '\nPlease keep waiting...'
                # expected error when batch_status erroneously is 'LOADED', but batch is not downloaded into postgres
                print(f"The batch '{self._batch_name if self._batch_name is not None else 'id'}': '{self._batch_id}' exists, but not loaded into the database. We are checking.{async_string}")
                    #   f"\n{'Please wait a few minutes and try again' if self.async_query else ''}")
                # change status
                self._set_batch_status(self._batch_id, 'UNLOADED')
                self.batch_status = 'UNLOADED'
                # return True for async_query = False
                return True

    def repo(self, repo: Union[int, str] = None, inplace: bool = False, exact_match: bool = False) -> Optional[CitrosDB]:
        '''
        Set repository to the CitrosDB object.

        Parameters
        ----------
        repo : int or str
            - To set the repository with the exact id, provide the repository id as str.
            - To set a repository using its name, provide the name as a string. If the provided string matches multiple repository names, check the whole list by `search_repo()` method.
            - To query the first created / second created / etc repository, set `repo` = 0, `repo` = 1, etc.
            - To query the the last created / the second-to-last created / etc repository, set `repo` = -1, `repo` = -2, etc.
        inplace : bool, default False
            If True, set repository id to the current CitrosDB object, otherwise returns new CitrosDB object with
            set repository id.
        exact_match : bool, default False
            If True, search for the repository with exact match in name field.
            If False, searches for the occurrence of the provided string within the name field.

        Returns
        -------
        out : CitrosDB
            CitrosDB with set repository id or None, if `inplace` = True.

        See Also
        --------
        CitrosDB.search_repo

        Examples
        --------
        Display information about all batches of the repository 'projects':

        >>> citros = da.CitrosDB()
        >>> citros.repo('projects').search_batch().print()
        {
         'dynamics': {
           'id': '00000000-dddd-1111-2222-333333333333',
           'sid': [1, 3, 2],
           'created_at': '2023-06-21T15:03:07.308498+00:00',
           ...
           'repo': 'projects',
           'link': https://citros.io/...
         }
        }

        By default, the `repo` method searches for occurrences of the provided string in repository names rather than exact matches. 
        For instance, if there are multiple repositories with the word 'projects' in their names, such as 'projects' and 'projects_1', 
        the `repo` method will indicate this and not set the repository. To search for an exact repository name, 
        set the `exact_match` parameter to True.

        >>> citros.repo('projects', exact_name = True)

        Show information about all batches of the last created repository:

        >>> citros = da.CitrosDB()
        >>> citros.repo(-1).search_batch().print()
        {
         'kinematics': {
           'id': '00000000-aaaa-1111-2222-333333333333',
           'sid': [1, 2, 3, 4, 5],
           'created_at': '2023-06-14T11:44:31.728585+00:00',
           ...
           'repo': 'citros_project',
           'link': https://citros.io/...
         },
         'kinematics_2': {
           'id': '00000000-bbbb-1111-2222-333333333333',
           'sid': [0, 1, 2, 3],
           'created_at': '2023-06-21T13:51:47.29987+00:00',
           ...
           'repo': 'citros_project',
           'link': https://citros.io/...
         }
        }

        Show information about all batches of the repository with id 'rrrrrrrr-1111-2222-3333-444444444444':

        >>> citros = da.CitrosDB()
        >>> citros.repo('rrrrrrrr-1111-2222-3333-444444444444').search_batch().print()
        {
         'kinematics': {
           'id': '00000000-aaaa-1111-2222-333333333333',
           'sid': [1, 2, 3, 4, 5],
           'created_at': '2023-06-14T11:44:31.728585+00:00',
           ...
           'repo': 'citros_project',
           'link': https://citros.io/...
         },
         'kinematics_2': {
           'id': '00000000-bbbb-1111-2222-333333333333',
           'sid': [0, 1, 2, 3],
           'created_at': '2023-06-21T13:51:47.29987+00:00',
           ...
           'repo': 'citros_project',
           'link': https://citros.io/...
         }
        }

        Assign the 'projects' repository to the existing CitrosDB object and show details for all its batches:

        >>> citros = da.CitrosDB()
        >>> citros.repo('projects', inplace = True)
        >>> citros.search_batch().print()
        {
         'dynamics': {
           'id': '00000000-dddd-1111-2222-333333333333',
           'sid': [1, 3, 2],
           'created_at': '2023-06-21T15:03:07.308498+00:00',
           ...
           'repo': 'projects',
           'link': https://citros.io/...
         }
        }
        '''
        if inplace:
            _GqlCursor._set_repo(self, repo, exact_match = exact_match)
            return None
        else:
            ci = self._copy()
            _GqlCursor._set_repo(ci, repo, exact_match = exact_match)
            return ci
        
    def search_repo(self, search: Optional[Union[int, str]] = None, search_by: Optional[str] = None, order_by: Optional[str] = None,
                  exact_match: bool = False, user: str = 'all') -> CitrosDict:
        '''
        Return information about repositories.

        The output is a dictionary, that contains repository names as dictionary keys 
        and repository ids, list of corresponding simulation ids and date of creation as dictionary values.

        Parameters
        ----------
        search : int or str
            - To search for the  repository with the exact id, provide the repository id as str.
            - To search by  repository name or by words that partially match the  repository name, provide the corresponding word as str.
            - To query the first created / second created / etc  repository, set `search` = 0, `search` = 1, etc.
            - To query the the last created / the second-to-last created / etc  repository, set `search` = -1, `search` = -2, etc.
            
            To use another field for search, set the appropriate `search_by` parameter

        search_by : str
            By default, the search is conducted based on name, repository id or ordinal number according to the creation time.
            To perform a search using an another field, set the `search_by` parameter to one of the following 
            and provide the appropriate format to `search` field:
            Provide `search` as a `str` for the following fields:
            - 'description'
            - 'git'

            Provide `search` as `str` that may contains date, time and timezone information, like: 'dd-mm-yyyy hh:mm:ss +hh:mm',
            or only date and time without timezone: 'dd-mm-yyyy hh:mm:ss', or only date: 'dd-mm-yyyy' / 'dd-mm' / 'dd'
            or only time: 'hh:mm:ss' / 'hh:mm' with or without timezone. 
            Any missing date information is automatically set to today's date, and any missing time information is set to 0.
            - 'created_after'
            - 'created_before'
            - 'updated_after'
            - 'updated_before'

        order_by : str or list or dict
            To obtain the output in ascending order, provide one or more of the following options as either a single value as str or a as a list:
            - 'name'
            - 'id' 
            - 'description'
            - 'created_at'
            - 'updated_at'
            - 'git'

            To specify whether to use descending or ascending order, create a dictionary where the keys correspond to the options mentioned above, 
            and the values are either 'asc' for ascending or 'desc' for descending. For instance: {'name': 'asc', 'created_at': 'desc'}"

        exact_match : bool, default False
            If True and `search` is str, looks for an exact match in the field defined by the 'search_by' parameter.
            If `search_by` is not defined, search is performed by name.
            If set to False, searches for the occurrences of the provided string within the field defined by the 'search_by' parameter.

        user : str, default 'all'
            Set `user` as 'me' to filter and display only the repositories that belong to you.
            To get the repositories that were created by another user, provide the email.

        Returns
        -------
        out : citros_data_analysis.data_access.citros_dict.CitrosDict
            Information about the repositories.
        
        Examples
        --------
        Display the information about all repositories:

        >>> citros.search_repo().print()
        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         },
         'projects': {
           'id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
           'description': 'statistics',
           'created_at': '2023-05-18T12:55:41.144263+00:00',
           'updated_at': '2023-08-18T11:25:31.356987+00:00',
           'git': '...'
         },
         'citros': {
           'id': 'rrrrrrrr-1111-2222-3333-444444666666',
           'description': 'project repository',
           'created_at': '2023-05-16T13:52:44.523112+00:00',
           'updated_at': '2023-05-26T15:25:17.321432+00:00',
           'git': '...'
         }
        }

        Print information about all repositories that have word 'citros' in their name, order them in descending order by time of creation:

        >>> citros.search_repo('citros', order_by = {'created_at': 'desc'}).print()
        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         },
         'citros': {
           'id': 'rrrrrrrr-1111-2222-3333-444444666666',
           'description': 'project repository',
           'created_at': '2023-05-16T13:52:44.523112+00:00',
           'updated_at': '2023-05-26T15:25:17.321432+00:00',
           'git': '...'
         }
        }

        By default, the `search_repo` method searches for occurrences of the provided string in repository names rather than exact matches. 
        To select information for only 'citros' repository, set the `exact_match` parameter to True:

        >>> citros.search_repo('citros', exact_match = True).print()
        {
         'citros': {
           'id': 'rrrrrrrr-1111-2222-3333-444444666666',
           'description': 'project repository',
           'created_at': '2023-05-22T13:52:44.523112+00:00',
           'updated_at': '2023-05-26T15:25:17.321432+00:00',
           'git': '...'
         }
        }
        
        Display the repository that was created the last:

        >>> citros.search_repo(-1).print()
        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         }
        }

        Display the repository with the repository id = 'rrrrrrrr-1111-2222-aaaa-555555555555':

        >>> citros.search_repo('rrrrrrrr-1111-2222-aaaa-555555555555').print()
        {
        'projects': {
           'id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
           'description': 'statistics',
           'created_at': '2023-05-18T12:55:41.144263+00:00',
           'updated_at': '2023-08-18T11:25:31.356987+00:00',
           'git': '...'
         }
        }

        Show the repository with word 'citros' in the 'description' field:

        >>> citros.search_repo('citros', search_by = 'description').print()
        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         }
        }

        Display repositories that were updated earlier then 12:30 18 August 2023, timezone +0:00:

        >>> citros.search_repo('18-08-2023 12:30:00 +0:00', search_by = 'updated_before').print()

        {
        'projects': {
           'id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
           'description': 'statistics',
           'created_at': '2023-05-18T12:55:41.144263+00:00',
           'updated_at': '2023-08-18T11:25:31.356987+00:00',
           'git': '...'
         }
        }

        Show repositories that were created after 19 May:

        >>> citros.search_repo('19-05', search_by = 'created_after').print()
        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         }
        }

        Display repositories that were last updated before 8:00 AM today:

        >>> citros.search_repo('8:00', search_by = 'updated_before').print()

        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         },
         'projects': {
           'id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
           'description': 'statistics',
           'created_at': '2023-05-18T12:55:41.144263+00:00',
           'updated_at': '2023-08-18T11:25:31.356987+00:00',
           'git': '...'
         },
         'citros': {
           'id': 'rrrrrrrr-1111-2222-3333-444444666666',
           'description': 'project repository',
           'created_at': '2023-05-16T13:52:44.523112+00:00',
           'updated_at': '2023-05-26T15:25:17.321432+00:00',
           'git': '...'
         }
        }

        By default, all repositories are displayed, regardless of their creator. 
        To show only the repositories that belong to you, set `user` = 'me':

        >>> citros.search_repo(user = 'me').print()

        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         }
        }

        To display repositories, that were created by another user, provide the email:

        >>> citros.search_repo(user = 'user@mail.com').print()

        {
        'citros': {
           'id': 'rrrrrrrr-1111-2222-3333-444444666666',
           'description': 'project repository',
           'created_at': '2023-05-16T13:52:44.523112+00:00',
           'updated_at': '2023-05-26T15:25:17.321432+00:00',
           'git': '...'
         }
        }
        
        Get list of the all existing repositories names as a list:

        >>> repos_names = list(citros.search_repo().keys())
        >>> print(repo_names)
        ['projects', 'citros_project', 'citros']
        '''
        if user in ['all', None]:
            user_id = None
        elif not isinstance(user, str):
            print(f"search_repo(): `user` must be str ")
            return CitrosDict({})
        elif user == 'me':
            user_id = self._user
        else:
            user_id = self._get_user_by_email(user)
            if user_id is None:
                print(f'search_repo(): no user with email "{user}", try search_user() or get_users() methods')
                return CitrosDict({})
        
        return _GqlCursor._search_repo(self, search= search, search_by = search_by, order_by = order_by,
                  exact_match = exact_match, user_id = user_id)

    def repo_info(self, search: Optional[Union[int, str]] = None, search_by: Optional[str] = None, order_by: Optional[str] = None,
                  exact_match: bool = False, user: str = 'all') -> CitrosDict:
        '''
        Return information about repositories.

        .. deprecated:: 0.8.0
            Use `CitrosDB.search_repo` instead.

        The output is a dictionary, that contains repository names as dictionary keys 
        and repository ids, list of corresponding simulation ids and date of creation as dictionary values.

        Parameters
        ----------
        search : int or str
            - To search for the  repository with the exact id, provide the repository id as str.
            - To search by  repository name or by words that partially match the  repository name, provide the corresponding word as str.
            - To query the first created / second created / etc  repository, set `search` = 0, `search` = 1, etc.
            - To query the the last created / the second-to-last created / etc  repository, set `search` = -1, `search` = -2, etc.
            
            To use another field for search, set the appropriate `search_by` parameter

        search_by : str
            By default, the search is conducted based on name, repository id or ordinal number according to the creation time.
            To perform a search using an another field, set the `search_by` parameter to one of the following 
            and provide the appropriate format to `search` field:
            Provide `search` as a `str` for the following fields:
            - 'description'
            - 'git'

            Provide `search` as `str` that may contains date, time and timezone information, like: 'dd-mm-yyyy hh:mm:ss +hh:mm',
            or only date and time without timezone: 'dd-mm-yyyy hh:mm:ss', or only date: 'dd-mm-yyyy' / 'dd-mm' / 'dd'
            or only time: 'hh:mm:ss' / 'hh:mm' with or without timezone. 
            Any missing date information is automatically set to today's date, and any missing time information is set to 0.
            - 'created_after'
            - 'created_before'
            - 'updated_after'
            - 'updated_before'

        order_by : str or list or dict
            To obtain the output in ascending order, provide one or more of the following options as either a single value as str or a as a list:
            - 'name'
            - 'id' 
            - 'description'
            - 'created_at'
            - 'updated_at'
            - 'git'

            To specify whether to use descending or ascending order, create a dictionary where the keys correspond to the options mentioned above, 
            and the values are either 'asc' for ascending or 'desc' for descending. For instance: {'name': 'asc', 'created_at': 'desc'}"

        exact_match : bool, default False
            If True and `search` is str, looks for an exact match in the field defined by the 'search_by' parameter.
            If `search_by` is not defined, search is performed by name.
            If set to False, searches for the occurrences of the provided string within the field defined by the 'search_by' parameter.

        user : str, default 'all'
            Set `user` as 'me' to filter and display only the repositories that belong to you.
            To get the repositories that were created by another user, provide the email.

        Returns
        -------
        out : citros_data_analysis.data_access.citros_dict.CitrosDict
            Information about the repositories.

        See Also
        --------
        CitrosDB.search_repo

        Examples
        --------
        Display the information about all repositories:

        >>> citros.repo_info().print()
        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         },
         'projects': {
           'id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
           'description': 'statistics',
           'created_at': '2023-05-18T12:55:41.144263+00:00',
           'updated_at': '2023-08-18T11:25:31.356987+00:00',
           'git': '...'
         },
         'citros': {
           'id': 'rrrrrrrr-1111-2222-3333-444444666666',
           'description': 'project repository',
           'created_at': '2023-05-16T13:52:44.523112+00:00',
           'updated_at': '2023-05-26T15:25:17.321432+00:00',
           'git': '...'
         }
        }

        Print information about all repositories that have word 'citros' in their name, order them in descending order by time of creation:

        >>> citros.repo_info('citros', order_by = {'created_at': 'desc'}).print()
        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         },
         'citros': {
           'id': 'rrrrrrrr-1111-2222-3333-444444666666',
           'description': 'project repository',
           'created_at': '2023-05-16T13:52:44.523112+00:00',
           'updated_at': '2023-05-26T15:25:17.321432+00:00',
           'git': '...'
         }
        }

        By default, the `repo_info` method searches for occurrences of the provided string in repository names rather than exact matches. 
        To select information for only 'citros' repository, set the `exact_match` parameter to True:

        >>> citros.repo_info('citros', exact_match = True).print()
        {
         'citros': {
           'id': 'rrrrrrrr-1111-2222-3333-444444666666',
           'description': 'project repository',
           'created_at': '2023-05-22T13:52:44.523112+00:00',
           'updated_at': '2023-05-26T15:25:17.321432+00:00',
           'git': '...'
         }
        }
        
        Display the repository that was created the last:

        >>> citros.repo_info(-1).print()
        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         }
        }

        Display the repository with the repository id = 'rrrrrrrr-1111-2222-aaaa-555555555555':

        >>> citros.repo_info('rrrrrrrr-1111-2222-aaaa-555555555555').print()
        {
        'projects': {
           'id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
           'description': 'statistics',
           'created_at': '2023-05-18T12:55:41.144263+00:00',
           'updated_at': '2023-08-18T11:25:31.356987+00:00',
           'git': '...'
         }
        }

        Show the repository with word 'citros' in the 'description' field:

        >>> citros.repo_info('citros', search_by = 'description').print()
        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         }
        }

        Display repositories that were updated earlier then 12:30 18 August 2023, timezone +0:00:

        >>> citros.repo_info('18-08-2023 12:30:00 +0:00', search_by = 'updated_before').print()

        {
        'projects': {
           'id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
           'description': 'statistics',
           'created_at': '2023-05-18T12:55:41.144263+00:00',
           'updated_at': '2023-08-18T11:25:31.356987+00:00',
           'git': '...'
         }
        }

        Show repositories that were created after 19 May:

        >>> citros.repo_info('19-05', search_by = 'created_after').print()
        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         }
        }

        Display repositories that were last updated before 8:00 AM today:

        >>> citros.repo_info('8:00', search_by = 'updated_before').print()

        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         },
         'projects': {
           'id': 'rrrrrrrr-1111-2222-aaaa-555555555555',
           'description': 'statistics',
           'created_at': '2023-05-18T12:55:41.144263+00:00',
           'updated_at': '2023-08-18T11:25:31.356987+00:00',
           'git': '...'
         },
         'citros': {
           'id': 'rrrrrrrr-1111-2222-3333-444444666666',
           'description': 'project repository',
           'created_at': '2023-05-16T13:52:44.523112+00:00',
           'updated_at': '2023-05-26T15:25:17.321432+00:00',
           'git': '...'
         }
        }

        By default, all repositories are displayed, regardless of their creator. 
        To show only the repositories that belong to you, set `user` = 'me':

        >>> citros.repo_info(user = 'me').print()

        {
         'citros_project': {
           'id': 'rrrrrrrr-1111-2222-3333-444444444444',
           'description': 'citros runs',
           'created_at': '2023-05-20T09:57:44.632361+00:00',
           'updated_at': '2023-08-20T07:45:11.136632+00:00',
           'git': '...'
         }
        }

        To display repositories, that were created by another user, provide the email:

        >>> citros.repo_info(user = 'user@mail.com').print()

        {
        'citros': {
           'id': 'rrrrrrrr-1111-2222-3333-444444666666',
           'description': 'project repository',
           'created_at': '2023-05-16T13:52:44.523112+00:00',
           'updated_at': '2023-05-26T15:25:17.321432+00:00',
           'git': '...'
         }
        }
        
        Get list of the all existing repositories names as a list:

        >>> repos_names = list(citros.repo_info().keys())
        >>> print(repo_names)
        ['projects', 'citros_project', 'citros']
        '''
        warnings.warn(
            "The CitrosDB.repo_info method has been deprecated "
            "and will be removed in a future version.\n"
            "Use CitrosDB.search_repo instead.",
            FutureWarning,
            stacklevel = 2
        )

        if user in ['all', None]:
            user_id = None
        elif not isinstance(user, str):
            print(f"repo_info(): `user` must be str ")
            return CitrosDict({})
        elif user == 'me':
            user_id = self._user
        else:
            user_id = self._get_user_by_email(user)
            if user_id is None:
                print(f'repo_info(): no user with email "{user}", try search_user() or get_users() methods')
                return CitrosDict({})
        
        return _GqlCursor._search_repo(self, search= search, search_by = search_by, order_by = order_by,
                  exact_match = exact_match, user_id = user_id)
    
    def get_repo(self):
        '''
        Get information about the current repository if the repository is set.

        Returns
        -------
        repo : citros_data_analysis.data_access.citros_dict.CitrosDict
            Information about the current repository. If the repository is not set, return None.

        Examples
        --------
        Get information about the current repository:

        >>> citros = da.CitrosDB(repo = 'citros_project')
        >>> df = citros.get_repo()
        {
         'name': 'citros_project',
         'id': 'rrrrrrrr-1111-2222-3333-444444444444',
         'description': 'citros runs',
         'created_at': '2023-05-20T09:57:44.632361+00:00',
         'updated_at': '2023-08-20T07:45:11.136632+00:00',
         'git': '...'
        }
        '''
        if self._repo_id is not None:
            search_res = self.search_repo(self._repo_id)
            if len(search_res) == 1:
                res = {}
                for k, v in search_res.items():
                    res['name'] = k
                    res = CitrosDict({**res, **v})
                return res
            else:
                return None
        else:
            return None

    def get_repo_name(self):
        '''
        Get the name of the current repository if the repository is set.

        Returns
        -------
        name : str
            Name of the current repository. If the repository is not set, return None.

        Examples
        --------
        Get the name of the last created repository:

        >>> citros = da.CitrosDB()
        >>> df = citros.repo(-1).get_repo_name()
        'citros_project'
        '''
        return self._repo_name

    def get_repo_id(self):
        '''
        Get the id of the current repository if the repository is set.

        Returns
        -------
        id : str
            id of the current repository. If the repository is not set, return None.

        Examples
        --------
        Get id of the repository 'citros_project':

        >>> citros = da.CitrosDB()
        >>> df = citros.repo('citros_project').get_repo_id()
        'rrrrrrrr-1111-2222-3333-444444444444'
        '''
        return self._repo_id
    
    def simulation(self, simulation: str = None, inplace: bool = False):
        '''
        Set batch to the CitrosDB object.

        Parameters
        ----------
        simulation : str
            Name of the simulation.
        inplace : bool, default False
            If True, set simulation name to the current CitrosDB object, otherwise returns new CitrosDB 
            object with set simulation.

        Returns
        -------
        out : CitrosDB
            CitrosDB with set simulation or None, if `inplace` = True.

        Examples
        --------
        Show information about the batch 'test' that was created in 'simulation_cannon_analytic' simulation:

        >>> citros = da.CitrosDB()
        >>> citros.simulation('simulation_cannon_analytic').search_batch('test').print()
        {
          'test': {
            'id': '01318463-e2ce-4642-89db-0132f9ab49c2',
            'sid': [0],
            'created_at': '2023-05-16T20:20:13.932897+00:00',
            'updated_at': '2023-07-16T20:21:30.648711+00:00',
            'status': 'DONE',
            'tag': 'latest',
            'simulation': 'simulation_cannon_analytic',
         ...
        }
        '''
        if inplace:
            self._set_simulation(simulation)
            return None
        else:
            ci = self._copy()
            ci._set_simulation(simulation)
            return ci
    
    def get_simulation(self):
        '''
        Get information about the current simulation if the simulation is set.

        Returns
        -------
        simulation : citros_data_analysis.data_access.citros_dict.CitrosDict
            Dict with the simulation name.

        Examples
        --------
        Get the name of the simulation that was set during initialization of CitrosDB object:

        >>> citros = da.CitrosDB(simulation = 'simulation_cannon_analytic')
        >>> citros.get_simulation()
        {'name': 'simulation_cannon_analytic'}
        '''
        return CitrosDict({'name': self._simulation})
        
    def get_simulation_name(self):
        '''
        Get the simulation name if the simulation is set.

        Returns
        -------
        name : str
            Name of the simulation. If the simulation is not set, return None.

        Examples
        --------
        Get the name of the simulation that was set during initialization of CitrosDB object:

        >>> citros = da.CitrosDB(simulation = 'simulation_cannon_analytic')
        >>> citros.get_simulation_name()
        'simulation_cannon_analytic'
        '''
        return self._simulation

    def batch(self, batch: Optional[Union[int, str]] = None, inplace: bool = False, exact_match: bool = False,
              user: str = 'all') -> Optional[CitrosDB]:
        '''
        Set batch to the CitrosDB object.

        Parameters
        ----------
        batch : int or str
            - To set the batch with the exact id, provide the batch id as str.
            - To set a batch using its name, provide the name as a string. 
            By default, searches for the occurrence of the provided string within the name field.
            If the provided string matches multiple batch names, the batch will not be set.
            This way you can set `exact_match` = `True` if you would like to set the exact name of the batch,
            specify repository and/or simulation by `repo()` and `simulation()` methods,
            or provide batch id instead of name (look for id by `search_batch()` method).
            - To query the first created / second created / etc batch, set `batch` = 0, `batch` = 1, etc.
            - To query the the last created / the second-to-last created / etc batch, set `batch` = -1, `batch` = -2, etc.
        inplace : bool, default False
            If True, set batch id to the current CitrosDB object, otherwise returns new CitrosDB object with
            set batch id.
        exact_match : bool, default False
            If `True`, search for the batch with exact match in name field. 
            If `False`, searches for the occurrence of the provided string within the name field.
        user : str, default 'all'
            Set `user` = 'me' to search only among batches that were created by you. 
            To display batches that were created by another user, provide the user's email.

        Returns
        -------
        out : CitrosDB
            CitrosDB with set batch id or None, if `inplace` = True.

        See Also
        --------
        CitrosDB.repo, CitrosDB.simulation, CitrosDB.search_batch

        Examples
        --------
        Get data for topic 'A' from the batch '00000000-1111-2222-3333-444444aaaaaa':

        >>> citros = da.CitrosDB()
        >>> df = citros.batch('00000000-1111-2222-3333-444444aaaaaa').topic('A').data()

        Get data for topic 'B' from the batch last created batch:

        >>> citros = da.CitrosDB()
        >>> df = citros.batch(-1).topic('B').data()

        Get data for topic 'C' from the batch named 'dynamics':

        >>> citros = da.CitrosDB()
        >>> df = citros.batch('dynamics').topic('C').data()

        If there are several batches with word 'dynamics' in their name, for example 'dynamics' and 'aerodynamics', 
        the batch will not be set, since the `batch` method searches for the occurrences of the provided string within repository names.
        To force it to look for the exact match, set `exact_match` = True:

        >>> citros.batch('dynamics', exact_match = True)

        Set batch id '00000000-1111-2222-3333-444444444444' to the already existing `CitrosDB()` object and query data from topic 'A':

        >>> citros = da.CitrosDB()
        >>> citros.batch('00000000-1111-2222-3333-444444444444', inplace = True)
        >>> df = citros.topic('A').data()
        '''
        if user in ['all', None]:
            user_id = None
        elif not isinstance(user, str):
            print(f"batch(): `user` must be str, no filter by user is applied")
            user_id = None
        elif user == 'me':
            user_id = self._user
        else:
            user_id = self._get_user_by_email(user)
            if user_id is None:
                print(f'batch(): no user with email "{user}", try search_user() or get_users() methods; no filter by user is applied')
                user_id = None
            
        if inplace:
            self._set_batch(batch, exact_match = exact_match, user_id = user_id)
            return None
        else:
            ci = self._copy()
            ci._set_batch(batch, exact_match = exact_match, user_id = user_id)
            return ci
        
    def search_batch(self, search: Optional[Union[str, int, float]] = None, search_by: Optional[str] = None, sid_status: Optional[str] = None, 
                   order_by: Optional[Union[str, list, dict]] = {'created_at': 'desc'}, exact_match: bool = False, user: str = 'all') -> CitrosDict:
        '''
        Return information about batches.

        The output is a dictionary, where the keys are the batch names and the corresponding values provide general information about each batch.

        Parameters
        ----------
        search : str, int or float
            - To search for the batch with the exact id, provide the batch id as str.
            - To search by batch name or by words that occurred in the batch name, provide the corresponding word as str. For the exact match set `exact_match` = True.
            - To query the first created / second created / etc batch, set `search` = 0, `search` = 1, etc.
            - To query the the last created / the second-to-last created / etc batch, set `search` = -1, `search` = -2, etc.
            
            To use another field for search, set the appropriate `search_by` parameter

        search_by : str
            By default, the search is conducted based on name, batch id or ordinal number according to the creation time.
            To perform a search using an another field, set the `search_by` parameter to one of the following
            and provide the appropriate format to `search` field:
            
            Provide `search` as a str for the following fields (looking for the occurrence of `search`, for the exact match set `exact_match` = True):
            - 'simulation'
            - 'tag'
            - 'message'

            - 'status': search by the batch status: set `search_by` = 'status' and 
            `search` = `'DONE'`, `'SCHEDULE'`, `'RUNNING'`, `'TERMINATING'` or `'ERROR'`

            - 'data_status': search by the data status: set `search_by` = 'status' and 
            `search` = `'LOADED'`, `'LOADING'`, `'UNLOADED'`, `'ERROR'`, `'UNKNOWN'`

            Provide `search` as `str` that may contains date, time and timezone information, like: 'dd-mm-yyyy hh:mm:ss +hh:mm', 
            or only date and time without timezone: 'dd-mm-yyyy hh:mm:ss', or only date: 'dd-mm-yyyy' / 'dd-mm' / 'dd'
            or only time: 'hh:mm:ss' / 'hh:mm' with or without timezone. 
            Any missing date information is automatically set to today's date, and any missing time information is set to 0:
            - 'created_after'
            - 'created_before'
            - 'updated_after'
            - 'updated_before'
            - 'data_last_access_after'
            - 'data_last_access_after'

            Provide `search` as an int for:
            - 'parallelism'
            - 'completions'
            - 'memory'

            Provide `search` as float for:
            - 'cpu'
            - 'gpu'
        
        sid_status : str, optional
            Select batches with the exact status of the simulation run: `'DONE'`, `'SCHEDULE'`, `'ERROR'`, `'CREATING'`, `'INIT'`, `'STARTING'`, `'RUNNING'`, `'TERMINATING'` or `'STOPPING'`.
            If the status is not specified, returns batches with sids with all statuses.

        order_by : str or list or dict, default {'created_at': 'desc'}
            By default the output is ordered by the time of creation, with the most recent batch on top.
            To obtain the output in ascending order, provide one or more of the following options as either a single str or a as a list:
            - 'name'
            - 'id' 
            - 'simulation'
            - 'status'
            - 'data_status'
            - 'data_last_access'
            - 'tag' 
            - 'message'
            - 'created_at'
            - 'updated_at'
            - 'parallelism'
            - 'completions'
            - 'cpu'
            - 'gpu'
            - 'memory'           
            
            To specify whether to use descending or ascending order, create a dictionary where the keys correspond to the options mentioned above, 
            and the values are either 'asc' for ascending or 'desc' for descending. For instance: {'name': 'asc', 'created_at': 'desc'}"

        exact_match : bool, default False
            If True and `search` is a `str`, looks for an exact match in the field defined by the 'search_by' parameter.
            If `search_by` is not defined, search is performed by name.
            If set to False, searches for the occurrences of the provided string within the field defined by the 'search_by' parameter.

        user : str, default 'all'
            Set `user` = 'me' to filter and display only the batches that belong to you. 
            To display batches that were created by another user, provide the user's email.

        Returns
        -------
        out : citros_data_analysis.data_access.citros_dict.CitrosDict
            Information about the batches.
        
        Examples
        --------
        Display the information about all batches:

        >>> citros.search_batch().print()
        {
         'kinematics': {
           'id': '00000000-aaaa-1111-2222-333333333333',
           'sid': [1, 2, 3, 4, 5],
           'created_at': '2023-06-14T11:44:31.728585+00:00',
           'updated_at': '2023-06-14T11:44:31.728585+00:00',
           'status': 'DONE',
           'data_status': 'LOADED',
           'data_last_access': '2023-06-15T13:24:0.368282+00:00',
           'tag': 'latest',
           'simulation': 'simulation_parameters',
           'message': 'launch_params',
           'parallelism': 1,
           'completions': 1,
           'cpu': 2,
           'gpu': 0,
           'memory': '265',
           'repo': 'citros_project',
           'link': https://citros.io/...
         },
         'kinematics_2': {
           'id': '00000000-bbbb-1111-2222-333333333333',
           'sid': [0, 1, 2, 3],
           'created_at': '2023-06-21T13:51:47.29987+00:00',
           'updated_at': '2023-06-21T13:51:47.29987+00:00',
           ...
         },
         'velocity': {
           'id': '00000000-cccc-1111-2222-333333333333',
           'sid': [0, 2],
           'created_at': '2023-06-18T20:57:27.830134+00:00',
           'updated_at': '2023-06-18T20:57:27.830134+00:00',
           ...
         },
         'dynamics': {
           'id': '00000000-dddd-1111-2222-333333333333',
           'sid': [1, 3, 2],
           'created_at': '2023-06-21T15:03:07.308498+00:00',
           'updated_at': '2023-06-21T15:03:07.308498+00:00',
           ...
         }
        }

        Print information about all kinematics batches, order them in descending order by time of creation:

        >>> citros.search_batch('kinematics', order_by = {'created_at': 'desc'}).print()
        {
         'kinematics_2': {
           'id': '00000000-bbbb-1111-2222-333333333333',
           'sid': [0, 1, 2, 3],
           'created_at': '2023-06-21T13:51:47.29987+00:00',
           ...
         },
         'kinematics': {
           'id': '00000000-aaaa-1111-2222-333333333333',
           'sid': [1, 2, 3, 4, 5],
           'created_at': '2023-06-14T11:44:31.728585+00:00',
           ...
         }
        }

        If the information about only batch named exactly 'kinematics' is needed, `exact_match` = True:

        >>> citros.search_batch('kinematics', exact_match = True).print()
        {
         'kinematics': {
           'id': '00000000-aaaa-1111-2222-333333333333',
           'sid': [1, 2, 3, 4, 5],
           'created_at': '2023-06-14T11:44:31.728585+00:00',
           ...
         }
        }

        Display the batch that was created the last:

        >>> citros.search_batch(-1).print()
        {
         'dynamics': {
           'id': '00000000-dddd-1111-2222-333333333333',
           'sid': [1, 3, 2],
           'created_at': '2023-06-21T15:03:07.308498+00:00'
           ...
         }
        }

        Display the batch with the batch id = '00000000-cccc-1111-2222-333333333333':

        >>> citros.search_batch('00000000-cccc-1111-2222-333333333333').print()
        {
         'velocity': {
           'id': '00000000-cccc-1111-2222-333333333333',
           'sid': [0, 2],
           'created_at': '2023-06-18T20:57:27.830134+00:00'
           ...
         }
        }

        Show the batch with word 'test' in the 'tag' field:

        >>> citros.search_batch('test', search_by = 'tag').print()
        {
         'velocity': {
           'id': '00000000-cccc-1111-2222-333333333333',
           'sid': [0, 2],
           'created_at': '2023-06-18T20:57:27.830134+00:00',
           'updated_at': '2023-06-18T20:57:27.830134+00:00',
           'status': 'DONE',
           'data_status': 'LOADED',
           ...
         }
        }

        Display batches that were created before 15:00 21 June 2023, timezone +0:00:

        >>> citros.search_batch('21-06-2023 15:00:00 +0:00', search_by = 'created_after').print()
        {
         'dynamics': {
           'id': '00000000-dddd-1111-2222-333333333333',
           'sid': [1, 3, 2],
           'created_at': '2023-06-21T15:03:07.308498+00:00',
           'updated_at': '2023-06-21T15:03:07.308498+00:00',
           ...
         }
        }
        
        Show batches that were created earlier then 15 June:

        >>> citros.search_batch('15-06', search_by = 'created_before').print()
        {
         'kinematics': {
           'id': '00000000-aaaa-1111-2222-333333333333',
           'sid': [1, 2, 3, 4, 5],
           'created_at': '2023-06-14T11:44:31.728585+00:00',
           ...
         }
        }

        Show batches that were last updated before 9:00 PM today:

        >>> citros.search_batch('21:00', search_by = 'updated_before').print()
        {
         'kinematics': {
           'id': '00000000-aaaa-1111-2222-333333333333',
           'sid': [1, 2, 3, 4, 5],
           'created_at': '2023-06-14T11:44:31.728585+00:00',
           'updated_at': '2023-06-14T11:44:31.728585+00:00',
           ...
         },
         'kinematics_2': {
           'id': '00000000-bbbb-1111-2222-333333333333',
           'sid': [0, 1, 2, 3],
           'created_at': '2023-06-21T13:51:47.29987+00:00',
           'updated_at': '2023-06-21T13:51:47.29987+00:00',
           ...
         },
         'velocity': {
           'id': '00000000-cccc-1111-2222-333333333333',
           'sid': [0, 2],
           'created_at': '2023-06-18T20:57:27.830134+00:00',
           'updated_at': '2023-06-18T20:57:27.830134+00:00',
           ...
         },
         'dynamics': {
           'id': '00000000-dddd-1111-2222-333333333333',
           'sid': [1, 3, 2],
           'created_at': '2023-06-21T15:03:07.308498+00:00',
           'updated_at': '2023-06-21T15:03:07.308498+00:00',
           ...
         }
        }

        By default, all batches are displayed, regardless of their creator. 
        To view only the batches that belong to you, set `user` = 'me':

        >>> citros.search_batch(user = 'me').print()

        {
        'velocity': {
           'id': '00000000-cccc-1111-2222-333333333333',
           'sid': [0, 2],
           'created_at': '2023-06-18T20:57:27.830134+00:00',
           'updated_at': '2023-06-18T20:57:27.830134+00:00',
           ...
         }
        }

        To display batches, that were created by another user, provide the email:

        >>> citros.search_batch(user = 'user@mail.com').print()

        {
        'dynamics': {
           'id': '00000000-dddd-1111-2222-333333333333',
           'sid': [1, 3, 2],
           'created_at': '2023-06-21T15:03:07.308498+00:00',
           'updated_at': '2023-06-21T15:03:07.308498+00:00',
           ...
         }
        }

        Get list of the all existing batches names as a list:

        >>> batches_names = list(citros.search_batch().keys())
        >>> print(batches_names)
        ['kinematics', 'kinematics_2', 'velocity', 'dynamics']
        '''
        if user in ['all', None]:
            user_id = None
        elif not isinstance(user, str):
            print(f"search_batch(): `user` must be str ")
            return CitrosDict({})
        elif user == 'me':
            user_id = self._user
        else:
            user_id = self._get_user_by_email(user)
            if user_id is None:
                print(f'search_batch(): no user with email "{user}", try search_user() or get_users() methods')
                return CitrosDict({})

        return _GqlCursor._search_batch(self, search = search, search_by = search_by, sid_status = sid_status, 
                   order_by = order_by, exact_match = exact_match, user_id = user_id)

    def batch_info(self, search: Optional[Union[str, int, float]] = None, search_by: Optional[str] = None, sid_status: Optional[str] = None, 
                   order_by: Optional[Union[str, list, dict]] = None, exact_match: bool = False, user: str = 'all') -> CitrosDict:
        '''
        Return information about batches.

        .. deprecated:: 0.8.0
            Use `CitrosDB.search_batch` instead.

        The output is a dictionary, where the keys are the batch names and the corresponding values provide general information about each batch.

        Parameters
        ----------
        search : str, int or float
            - To search for the batch with the exact id, provide the batch id as str.
            - To search by batch name or by words that occurred in the batch name, provide the corresponding word as str. For the exact match set `exact_match` = True.
            - To query the first created / second created / etc batch, set `search` = 0, `search` = 1, etc.
            - To query the the last created / the second-to-last created / etc batch, set `search` = -1, `search` = -2, etc.
            
            To use another field for search, set the appropriate `search_by` parameter

        search_by : str
            By default, the search is conducted based on name, batch id or ordinal number according to the creation time.
            To perform a search using an another field, set the `search_by` parameter to one of the following
            and provide the appropriate format to `search` field:
            
            Provide `search` as a str for the following fields (looking for the occurrence of `search`, for the exact match set `exact_match` = True):
            - 'simulation'
            - 'tag'
            - 'message'

            - 'status': search by the batch status: set `search_by` = 'status' and 
            `search` = 'DONE', 'SCHEDULE', 'RUNNING', 'TERMINATING' or 'ERROR'
            
            - 'data_status': search by the data status: set `search_by` = 'status' and 
            `search` = `'LOADED'`, `'LOADING'`, `'UNLOADED'`, `'ERROR'`, `'UNKNOWN'`

            Provide `search` as `str` that may contains date, time and timezone information, like: 'dd-mm-yyyy hh:mm:ss +hh:mm', 
            or only date and time without timezone: 'dd-mm-yyyy hh:mm:ss', or only date: 'dd-mm-yyyy' / 'dd-mm' / 'dd'
            or only time: 'hh:mm:ss' / 'hh:mm' with or without timezone. 
            Any missing date information is automatically set to today's date, and any missing time information is set to 0:
            - 'created_after'
            - 'created_before'
            - 'updated_after'
            - 'updated_before'
            - 'data_last_access_after'
            - 'data_last_access_after'

            Provide `search` as an int for:
            - 'parallelism'
            - 'completions'
            - 'memory'

            Provide `search` as float for:
            - 'cpu'
            - 'gpu'
        
        sid_status : str, optional
            Select batches with the exact status of the simulation run: 'DONE', 'SCHEDULE', 'ERROR', 'CREATING', 'INIT', 'STARTING', 'RUNNING', 'TERMINATING' or 'STOPPING'.
            If the status is not specified, returns batches with sids with all statuses.

        order_by : str or list or dict
            To obtain the output in ascending order, provide one or more of the following options as either a single str or a as a list:
            - 'name'
            - 'id' 
            - 'simulation'
            - 'status'
            - 'tag' 
            - 'message'
            - 'created_at'
            - 'updated_at'
            - 'parallelism'
            - 'completions'
            - 'cpu'
            - 'gpu'
            - 'memory'           
            
            To specify whether to use descending or ascending order, create a dictionary where the keys correspond to the options mentioned above, 
            and the values are either 'asc' for ascending or 'desc' for descending. For instance: {'name': 'asc', 'created_at': 'desc'}"

        exact_match : bool, default False
            If True and `search` is a `str`, looks for an exact match in the field defined by the 'search_by' parameter.
            If `search_by` is not defined, search is performed by name.
            If set to False, searches for the occurrences of the provided string within the field defined by the 'search_by' parameter.

        user : str, default 'all'
            Set `user` = 'me' to filter and display only the batches that belong to you. 
            To display batches that were created by another user, provide the user's email.

        Returns
        -------
        out : citros_data_analysis.data_access.citros_dict.CitrosDict
            Information about the batches.

        See Also
        --------
        CitrosDB.search_batch

        Examples
        --------
        Display the information about all batches:

        >>> citros.batch_info().print()
        {
         'kinematics': {
           'id': '00000000-aaaa-1111-2222-333333333333',
           'sid': [1, 2, 3, 4, 5],
           'created_at': '2023-06-14T11:44:31.728585+00:00',
           'updated_at': '2023-06-14T11:44:31.728585+00:00',
           'status': 'DONE',
           'data_status': 'LOADED',
           'data_last_access': '2023-06-15T13:24:0.368282+00:00',
           'tag': 'latest',
           'simulation': 'simulation_parameters',
           'message': 'launch_params',
           'parallelism': 1,
           'completions': 1,
           'cpu': 2,
           'gpu': 0,
           'memory': '265',
           'repo': 'citros_project',
           'link': https://citros.io/...
         },
         'kinematics_2': {
           'id': '00000000-bbbb-1111-2222-333333333333',
           'sid': [0, 1, 2, 3],
           'created_at': '2023-06-21T13:51:47.29987+00:00',
           'updated_at': '2023-06-21T13:51:47.29987+00:00',
           ...
         },
         'velocity': {
           'id': '00000000-cccc-1111-2222-333333333333',
           'sid': [0, 2],
           'created_at': '2023-06-18T20:57:27.830134+00:00',
           'updated_at': '2023-06-18T20:57:27.830134+00:00',
           ...
         },
         'dynamics': {
           'id': '00000000-dddd-1111-2222-333333333333',
           'sid': [1, 3, 2],
           'created_at': '2023-06-21T15:03:07.308498+00:00',
           'updated_at': '2023-06-21T15:03:07.308498+00:00',
           ...
         }
        }

        Print information about all kinematics batches, order them in descending order by time of creation:

        >>> citros.batch_info('kinematics', order_by = {'created_at': 'desc'}).print()
        {
         'kinematics_2': {
           'id': '00000000-bbbb-1111-2222-333333333333',
           'sid': [0, 1, 2, 3],
           'created_at': '2023-06-21T13:51:47.29987+00:00',
           ...
         },
         'kinematics': {
           'id': '00000000-aaaa-1111-2222-333333333333',
           'sid': [1, 2, 3, 4, 5],
           'created_at': '2023-06-14T11:44:31.728585+00:00',
           ...
         }
        }

        If the information about only batch named exactly 'kinematics' is needed, `exact_match` = True:

        >>> citros.batch_info('kinematics', exact_match = True).print()
        {
         'kinematics': {
           'id': '00000000-aaaa-1111-2222-333333333333',
           'sid': [1, 2, 3, 4, 5],
           'created_at': '2023-06-14T11:44:31.728585+00:00',
           ...
         }
        }

        Display the batch that was created the last:

        >>> citros.batch_info(-1).print()
        {
         'dynamics': {
           'id': '00000000-dddd-1111-2222-333333333333',
           'sid': [1, 3, 2],
           'created_at': '2023-06-21T15:03:07.308498+00:00'
           ...
         }
        }

        Display the batch with the batch id = '00000000-cccc-1111-2222-333333333333':

        >>> citros.batch_info('00000000-cccc-1111-2222-333333333333').print()
        {
         'velocity': {
           'id': '00000000-cccc-1111-2222-333333333333',
           'sid': [0, 2],
           'created_at': '2023-06-18T20:57:27.830134+00:00'
           ...
         }
        }

        Show the batch with word 'test' in the 'tag' field:

        >>> citros.batch_info('test', search_by = 'tag').print()
        {
         'velocity': {
           'id': '00000000-cccc-1111-2222-333333333333',
           'sid': [0, 2],
           'created_at': '2023-06-18T20:57:27.830134+00:00',
           'updated_at': '2023-06-18T20:57:27.830134+00:00',
           'status': 'DONE',
           'data_status': 'LOADED',
           ...
         }
        }

        Display batches that were created before 15:00 21 June 2023, timezone +0:00:

        >>> citros.batch_info('21-06-2023 15:00:00 +0:00', search_by = 'created_after').print()
        {
         'dynamics': {
           'id': '00000000-dddd-1111-2222-333333333333',
           'sid': [1, 3, 2],
           'created_at': '2023-06-21T15:03:07.308498+00:00',
           'updated_at': '2023-06-21T15:03:07.308498+00:00',
           ...
         }
        }
        
        Show batches that were created earlier then 15 June:

        >>> citros.batch_info('15-06', search_by = 'created_before').print()
        {
         'kinematics': {
           'id': '00000000-aaaa-1111-2222-333333333333',
           'sid': [1, 2, 3, 4, 5],
           'created_at': '2023-06-14T11:44:31.728585+00:00',
           ...
         }
        }

        Show batches that were last updated before 9:00 PM today:

        >>> citros.batch_info('21:00', search_by = 'updated_before').print()
        {
         'kinematics': {
           'id': '00000000-aaaa-1111-2222-333333333333',
           'sid': [1, 2, 3, 4, 5],
           'created_at': '2023-06-14T11:44:31.728585+00:00',
           'updated_at': '2023-06-14T11:44:31.728585+00:00',
           ...
         },
         'kinematics_2': {
           'id': '00000000-bbbb-1111-2222-333333333333',
           'sid': [0, 1, 2, 3],
           'created_at': '2023-06-21T13:51:47.29987+00:00',
           'updated_at': '2023-06-21T13:51:47.29987+00:00',
           ...
         },
         'velocity': {
           'id': '00000000-cccc-1111-2222-333333333333',
           'sid': [0, 2],
           'created_at': '2023-06-18T20:57:27.830134+00:00',
           'updated_at': '2023-06-18T20:57:27.830134+00:00',
           ...
         },
         'dynamics': {
           'id': '00000000-dddd-1111-2222-333333333333',
           'sid': [1, 3, 2],
           'created_at': '2023-06-21T15:03:07.308498+00:00',
           'updated_at': '2023-06-21T15:03:07.308498+00:00',
           ...
         }
        }

        By default, all batches are displayed, regardless of their creator. 
        To view only the batches that belong to you, set `user` = 'me':

        >>> citros.batch_info(user = 'me').print()

        {
        'velocity': {
           'id': '00000000-cccc-1111-2222-333333333333',
           'sid': [0, 2],
           'created_at': '2023-06-18T20:57:27.830134+00:00',
           'updated_at': '2023-06-18T20:57:27.830134+00:00',
           ...
         }
        }

        To display batches, that were created by another user, provide the email:

        >>> citros.batch_info(user = 'user@mail.com').print()

        {
        'dynamics': {
           'id': '00000000-dddd-1111-2222-333333333333',
           'sid': [1, 3, 2],
           'created_at': '2023-06-21T15:03:07.308498+00:00',
           'updated_at': '2023-06-21T15:03:07.308498+00:00',
           ...
         }
        }

        Get list of the all existing batches names as a list:

        >>> batches_names = list(citros.batch_info().keys())
        >>> print(batches_names)
        ['kinematics', 'kinematics_2', 'velocity', 'dynamics']
        '''
        warnings.warn(
            "The CitrosDB.batch_info method has been deprecated "
            "and will be removed in a future version.\n"
            "Use CitrosDB.search_batch instead.",
            FutureWarning,
            stacklevel = 2
        )

        if user in ['all', None]:
            user_id = None
        elif not isinstance(user, str):
            print(f"batch_info(): `user` must be str ")
            return CitrosDict({})
        elif user == 'me':
            user_id = self._user
        else:
            user_id = self._get_user_by_email(user)
            if user_id is None:
                print(f'batch_info(): no user with email "{user}", try search_user() or get_users() methods')
                return CitrosDict({})

        return _GqlCursor._search_batch(self, search = search, search_by = search_by, sid_status = sid_status, 
                   order_by = order_by, exact_match = exact_match, user_id = user_id)
    
    def get_batch(self):
        '''
        Get information about the current batch if the batch is set.

        Returns
        -------
        batch : citros_data_analysis.data_access.citros_dict.CitrosDict
            Information about the current batch. If the batch is not set, return None.

        Examples
        --------
        Get information about the current batch:

        >>> citros = da.CitrosDB(batch = 'kinematics')
        >>> citros.get_batch()
        {
         'name': 'kinematics',
         'id': '00000000-aaaa-1111-2222-333333333333',
         'sid': [1, 2, 3, 4, 5],
         'created_at': '2023-06-14T11:44:31.728585+00:00',
         'updated_at': '2023-06-14T11:44:31.728585+00:00',
         'status': 'DONE',
         'data_status': 'LOADED',
         'data_last_access': '2023-06-15T13:24:0.368282+00:00',
         'tag': 'latest',
         'simulation': 'simulation_parameters',
         'message': 'launch_params',
         'parallelism': 1,
         'completions': 1,
         'cpu': 2,
         'gpu': 0,
         'memory': '265',
         'repo': 'citros_project',
         'link': https://citros.io/...
        }
        '''
        if self._batch_id is not None:
            search_res = self.search_batch(self._batch_id)
            if len(search_res) == 1:
                res = {}
                for k, v in search_res.items():
                    res['name'] = k
                    res = CitrosDict({**res, **v})
                return res
            else:
                return None
        else:
            return None

    def get_batch_name(self):
        '''
        Get the name of the current batch if the batch is set.

        Returns
        -------
        name : str
            Name of the current batch. If the batch is not set, return None.

        Examples
        --------
        Get name of the most recently created batch:

        >>> citros = da.CitrosDB()
        >>> citros.batch(-1).get_batch_name()
        'dynamics'
        '''
        return self._batch_name

    def get_batch_id(self):
        '''
        Get the id of the current batch if the batch is set.

        Returns
        -------
        id : str
            id of the current batch. If the batch is not set, return None.

        Examples
        --------
        Get id of the batch 'dynamics':

        >>> citros = da.CitrosDB()
        >>> citros.batch('dynamics').get_batch_id()
        '00000000-dddd-1111-2222-333333333333'
        '''
        return self._batch_id
    
    def get_batch_size(self):
        '''
        Print sizes of the all batches in the current schema that are downloaded in the database.

        .. deprecated:: 0.8.0
            Use `CitrosDB.search_batch` or `CitrosDB.info` methods instead.

        Print table with batch ids, batch size and total batch size with indexes.

        See Also
        --------
        CitrosDB.search_batch

        Examples
        --------
        Print the table with information about batch sizes:

        >>> citros = da.CitrosDB()
        >>> citros.get_batch_size()
        +-----------+--------------------------------------+-------------+------------+
        | batch     | batch id                             | size        | total size |
        +-----------+--------------------------------------+-------------+------------+
        | stars     | 00000000-1111-2222-3333-444444444444 | 32 kB       | 64 kB      |
        | galaxies  | 00000000-aaaa-2222-3333-444444444444 | 8192 bytes  | 16 kB      |
        +-----------+--------------------------------------+-------------+------------+
        '''
        warnings.warn(
            "The CitrosDB.get_batch_size method has been deprecated "
            "and will be removed in a future version.\n"
            "Use CitrosDB.search_batch or CitrosDB.info instead.",
            FutureWarning,
            stacklevel = 2
        )

        table_to_display = self._get_batch_size(mode = 'all', names = True)
        table = PrettyTable(field_names=['batch', 'batch id', 'size', 'total size'], align='l')
        if table_to_display is not None:
            table.add_rows(table_to_display)
        print(table)

    def get_current_batch_size(self):
        '''
        Print size of the current batch, if it is set.

        .. deprecated:: 0.8.0
            Use `CitrosDB.get_batch` or `CitrosDB.info` methods instead.

        Print table with batch name, batch size and total batch size with indexes.

        See Also
        --------
        CitrosDB.get_batch, CitrosDB.info

        Examples
        --------
        Print the table with information about batch sizes:

        >>> citros = da.CitrosDB(batch = 'galaxies')
        >>> citros.get_current_batch_size()
        +-----------+--------------------------------------+-------------+------------+
        | batch     | batch id                             | size        | total size |
        +-----------+--------------------------------------+-------------+------------+
        | galaxies  | 00000000-1111-2222-3333-444444444444 | 8192 bytes  | 16 kB      |
        +-----------+--------------------------------------+-------------+------------+
        '''
        warnings.warn(
            "The CitrosDB.get_current_batch_size method has been deprecated "
            "and will be removed in a future version.\n"
            "Use CitrosDB.get_batch or CitrosDB.info instead.",
            FutureWarning,
            stacklevel = 2
        )
        
        if not self._is_batch_available():
            return None
        table_to_display = self._get_batch_size(mode = 'current', names = True)
        table = PrettyTable(field_names=['batch', 'batch id', 'size', 'total size'], align='l')
        if table_to_display is not None:
            table.add_rows(table_to_display)
        print(table)

    def _get_batch_size(self, mode = 'all', names = False):
        '''
        Return sizes of the all tables in the current schema.

        Returns
        -------
        list of tuples
            Each tuple contains name of the table, table size and total size with indexes.
        '''
        table_size, error_name = _PgCursor._get_batch_size(self, mode = mode)
        if (self.async_query) and (error_name is not None):
            self._handle_pg_error(error_name)
            return None
        if table_size is None:
            return None
        if names:
            batch_ids = [table_size[i][0] for i in range(len(table_size))]
            if hasattr(self, '_test_mode'):
                batch_names = ['-' for i in range(len(table_size))]
            else:
                res = self._get_batch_names(batch_ids)
                if res is None:
                    return None
                names_dict = {row['id']:row['name'] for row in res['batchRunsList']}
                keys = names_dict.keys()
                batch_names = []
                for row in table_size:
                    if row[0] in keys:
                        batch_names.append(names_dict[row[0]])
                    else:
                        batch_names.append('-')
            table_to_display = [[batch_names[i]] + list(table_size[i]) for i in range(len(table_size))]
            return table_to_display
        else:
            return table_size
    
    def get_users(self, show_all = True):
        '''
        Display a table that presents key users information, including their first names, last names, and email addresses.

        By default displays all users. 
        
        If `show_all` = `False` and if the repository is set (using the `repo()` method 
        or during initialization of CitrosDB object), displays information only about users who have been 
        involved in work with this repository (user who created the repository and users who have created batches within it).

        If `show_all` = `False` and if the batch is set (using the `batch()` method or during initialization of CitrosDB object), 
        shows information about the user who created that specific batch.

        Parameters
        ----------
        show_all : bool, default True
            If `True`, shows all users without filtering according to set repositories and batches.

        See Also
        --------
        CitrosDB.batch, CitrosDB.repo, CitrosDB.user_info

        Examples
        --------
        Display information about users:

        >>> citros.get_users()
        +--------+------------+-----------------------------+
        | name   | last name  | email                       |
        +--------+------------+-----------------------------+
        | alex   | blanc      | alex@mail.com               |
        | david  | gilbert    | david@mail.com              |
        | mary   | stevenson  | mary@mail.com               |
        +--------+------------+-----------------------------+
        '''
        users_dict = _GqlCursor._search_user(self, order_by = 'email', show_all = show_all)

        if users_dict is not None and len(users_dict) > 0:
            table_users = [[v['name'], v['last_name'], k] for k, v in users_dict.items()]
        else:
            table_users = None
        table = PrettyTable(field_names=['name', 'last name', 'email'], align='l')
        if table_users is not None:
            table.add_rows(table_users)
        print(table)

    def search_user(self, search: Optional[str] = None, search_by: Optional[str] = None, 
                  order_by: Optional[Union[str, list, dict]] = None, show_all = True):
        '''
        Retrieve information about users, including their first names, last names, emails and the lists of repositories 
        they have created, along with the repositories in which these users have created batches.

        By default return all users. 
        
        If `show_all` = `False` and if the repository is set (using the `repo()` method 
        or during initialization of CitrosDB object), displays information only about users who have been 
        involved in work with this repository (user who created the repository and users who have created batches within it).

        If `show_all` = `False` and if the batch is set (using the `batch()` method or during initialization of CitrosDB object), 
        shows information about the user who created that specific batch.

        Parameters
        ----------
        search : str, optional
            - By default, it displays information about all users within the organization.
            - Provide email to display information about the exact user.
            - To search user by their name, provide user's name and set `search_by` = 'name'
            - To search by the last name, provide user's last name and set `search_by` = 'last_name'

        search_by : str, optional
            - By default, if the `search` is provided, performs search by email.
            - To search by the name, set `search_by` = 'name'.
            - To search by the last name, set `search_by` = 'last_name'.

        order_by : str or list or dict
            To obtain the output in ascending order, provide one or more of the following options as either a single str or a as a list:
            - 'name'
            - 'last_name' 
            - 'email'           
            
            To specify whether to use descending or ascending order, create a dictionary where the keys correspond to the options mentioned above, 
            and the values are either 'asc' for ascending or 'desc' for descending. For instance: {'name': 'asc', 'last_name': 'desc'}"

        show_all : bool, default True
            If `True`, shows all users without filtering according to set repositories and batches.

        Returns
        -------
        out : citros_data_analysis.data_access.citros_dict.CitrosDict
            Information about the users.

        See Also
        --------
        CitrosDB.repo, CitrosDB.batch, CitrosDB.get_users

        Examples
        --------
        Display all users of your organization, order the output by names:

        >>> citros.search_user('order_by' = 'name').print()
        {
         {
         'david@mail.com': {
           'name': 'david',
           'last_name': 'gilbert',
           'create_repo': ['robot_master', 'automaton_lab'],
           'create_batch_in_repo': ['robot_master']
         },
         'mary@mail.com': {
           'name': 'mary',
           'last_name': 'stevenson',
           'create_repo': ['mech_craft'],
           'create_batch_in_repo': ['mech_craft', 'robot_master']
         },
         ...
        }

        Display information about the user with email 'mary@mail.com':
        
        >>> citros.search_user('mary@mail.com').print()
        {
         'mary@mail.com': {
           'name': 'mary',
           'last_name': 'stevenson',
           'create_repo': ['mech_craft'],
           'create_batch_in_repo': ['mech_craft', 'robot_master']
         }
        }

        Search for the user David:
        
        >>> citros.search_user('david', search_by = 'name').print()
        {
         'david@mail.com': {
           'name': 'david',
           'last_name': 'gilbert',
           'create_repo': ['robot_master', 'automaton_lab'],
           'create_batch_in_repo': ['robot_master']
         }
        }

        Show user, who created repository 'mech_craft' or created batches in this repository:

        >>> citros.repo('mech_craft').search_user().print()
        {
         'mary@mail.com': {
           'name': 'mary',
           'last_name': 'stevenson',
           'create_repo': ['mech_craft'],
           'create_batch_in_repo': ['mech_craft', 'robot_master']
         }
        }

        If there is a batch 'velocity' in 'robot_master' repository, to show who create it execute the following:

        >>> citros.batch('velocity').search_user().print()
        {
         'david@mail.com': {
           'name': 'david',
           'last_name': 'gilbert',
           'create_repo': ['robot_master'],
           'create_batch_in_repo': ['robot_master']
         }
        }
        '''
        return _GqlCursor._search_user(self, search = search, search_by = search_by, order_by = order_by, show_all = show_all)
    
    def user_info(self, search: Optional[str] = None, search_by: Optional[str] = None, 
                  order_by: Optional[Union[str, list, dict]] = None):
        '''
        Retrieve information about users, including their first names, last names, emails and the lists of repositories 
        they have created, along with the repositories in which these users have created batches.
        
        .. deprecated:: 0.8.0
            Use `CitrosDB.search_user` method instead.

        If the repository is set using the `repo()` method, it displays information about both the user who created that repository 
        and users who have created batches within it. 
        If the batch is set using the `batch()` method, it shows information about the user who created that specific batch.

        Parameters
        ----------
        search : str, optional
            - By default, it displays information about all users within the organization.
            - Provide email to display information about the exact user.
            - To search user by their name, provide user's name and set `search_by` = 'name'
            - To search by the last name, provide user's last name and set `search_by` = 'last_name'

        search_by : str, optional
            - By default, if the `search` is provided, performs search by email.
            - To search by the name, set `search_by` = 'name'.
            - To search by the last name, set `search_by` = 'last_name'.

        order_by : str or list or dict
            To obtain the output in ascending order, provide one or more of the following options as either a single str or a as a list:
            - 'name'
            - 'last_name' 
            - 'email'           
            
            To specify whether to use descending or ascending order, create a dictionary where the keys correspond to the options mentioned above, 
            and the values are either 'asc' for ascending or 'desc' for descending. For instance: {'name': 'asc', 'last_name': 'desc'}"

        Returns
        -------
        out : citros_data_analysis.data_access.citros_dict.CitrosDict
            Information about the users.

        See Also
        --------
        CitrosDB.search_user, CitrosDB.repo, CitrosDB.batch

        Examples
        --------
        Display all users of your organization, order the output by names:

        >>> citros.user_info('order_by' = 'name').print()
        {
         {
         'david@mail.com': {
           'name': 'david',
           'last_name': 'gilbert',
           'create_repo': ['robot_master', 'automaton_lab'],
           'create_batch_in_repo': ['robot_master']
         },
         'mary@mail.com': {
           'name': 'mary',
           'last_name': 'stevenson',
           'create_repo': ['mech_craft'],
           'create_batch_in_repo': ['mech_craft', 'robot_master']
         },
         ...
        }

        Display information about the user with email 'mary@mail.com':
        
        >>> citros.user_info('mary@mail.com').print()
        {
         'mary@mail.com': {
           'name': 'mary',
           'last_name': 'stevenson',
           'create_repo': ['mech_craft'],
           'create_batch_in_repo': ['mech_craft', 'robot_master']
         }
        }

        Search for the user David:
        
        >>> citros.user_info('david', search_by = 'name').print()
        {
         'david@mail.com': {
           'name': 'david',
           'last_name': 'gilbert',
           'create_repo': ['robot_master', 'automaton_lab'],
           'create_batch_in_repo': ['robot_master']
         }
        }

        Show user, who created repository 'mech_craft' or created batches in this repository:

        >>> citros.repo('mech_craft').user_info().print()
        {
         'mary@mail.com': {
           'name': 'mary',
           'last_name': 'stevenson',
           'create_repo': ['mech_craft'],
           'create_batch_in_repo': ['mech_craft', 'robot_master']
         }
        }

        If there is a batch 'velocity' in 'robot_master' repository, to show who create it execute the following:

        >>> citros.batch('velocity').user_info().print()
        {
         'david@mail.com': {
           'name': 'david',
           'last_name': 'gilbert',
           'create_repo': ['robot_master'],
           'create_batch_in_repo': ['robot_master']
         }
        }
        '''
        warnings.warn(
            "The CitrosDB.user_info method has been deprecated "
            "and will be removed in a future version.\n"
            "Use CitrosDB.search_user instead.",
            FutureWarning,
            stacklevel = 2
        )
        return _GqlCursor._search_user(self, search = search, search_by = search_by, order_by = order_by)
    
    def topic(self, topic_name: Optional[Union[str, list]] = None) -> CitrosDB:
        '''
        Select topic.

        Parameters
        ----------
        topic_name : str or list of str
            Name of the topic.

        Returns
        -------
        out : CitrosDB
            CitrosDB with set 'topic' parameter.

        Examples
        --------
        Get data for topic name 'A' from batch 'dynamics':

        >>> citros = da.CitrosDB()
        >>> df = citros.batch('dynamics').topic('A').data()

        Get maximum value of the 'sid' among topics 'A' and 'B':

        >>> citros = da.CitrosDB()
        >>> citros.batch('dynamics').topic(['A', 'B']).get_max_value('sid')
        3
        '''
        ci = self._copy()
        _PgCursor.topic(ci, topic_name = topic_name)
        return ci
        
    def sid(self, value: Optional[Union[int, list]] = None, start: int = 0, end: int = None, count: int = None) -> CitrosDB:
        '''
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

        Returns
        -------
        out : CitrosDB
            CitrosDB with set 'sid' parameter.

        Examples
        --------
        Get data from batch 'robotics' for topic 'A' where sid values are 1 or 2:

        >>> citros = da.CitrosDB()
        >>> df = citros.batch('robotics').topic('A').sid([1,2]).data()

        Get data from batch 'robotics' for for topic 'A' where sid is in the range of 3 <= sid <= 8 :
        
        >>> citros = da.CitrosDB()
        >>> df = citros.batch('robotics').topic('A').sid(start = 3, end = 8).data()

        or the same with `count`:
        
        >>> df = citros.batch('robotics').topic('A').sid(start = 3, count = 6).data()

        For sid >= 7:
        
        >>> df = citros.batch('robotics').topic('A').sid(start = 7).data()
        '''
        ci = self._copy()
        _PgCursor.sid(ci, value = value, start = start, end = end, count = count)
        return ci
        
    def rid(self, value: Optional[Union[int, list]] = None, start: int = 0, end: int = None, count: int = None) -> CitrosDB:
        '''
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

        Returns
        -------
        out : CitrosDB
            CitrosDB with set 'rid' parameter.

        Examples
        --------
        Get data from batch 'aero' for topic 'A' where rid values are 10 or 20:

        >>> citros = da.CitrosDB()
        >>> df = citros.batch('aero').topic('A').rid([10, 20]).data()

        Get data from batch 'aero' for topic 'A' where rid is in the range of 0 <= rid <= 9 :
        
        >>> citros = da.CitrosDB()
        >>> df = citros.batch('aero').topic('A').rid(start = 0, end = 9).data()

        or the same with `count`:
        
        >>> df = citros.batch('aero').topic('A').rid(start = 0, count = 10).data()

        For rid >= 5:
        
        >>> df = citros.batch('aero').topic('A').rid(start = 5).data()
        '''
        ci = self._copy()
        _PgCursor.rid(ci, value = value, start = start, end = end, count = count)
        return ci

    def time(self, start: int = 0, end: int = None, duration: int = None) -> CitrosDB:
        '''
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

        Returns
        -------
        out : CitrosDB
            CitrosDB with set 'time' parameter.

        Examples
        --------
        Get data from batch 'kinematics' for topic 'A' where time is in the range 10ns <= time <= 20ns:
        
        >>> citros = da.CitrosDB()
        >>> df = citros.batch('kinematics').topic('A').time(start = 10, end = 20).data()

        To set time range 'first 10ns starting from 10th nanosecond', that means 10ns <= time < 20ns:
        
        >>> df = citros.batch('kinematics').topic('A').time(start = 10, duration = 10).data()

        For time >= 20:
        
        >>> df = citros.batch('kinematics').topic('A').time(start = 20).data()
        '''
        ci = self._copy()
        _PgCursor.time(ci, start = start, end = end, duration = duration)
        return ci
    
    def info(self) -> CitrosDict:
        '''
        Return information about the batch, based on the configurations set by topic(), rid(), sid() and time() methods.

        The output is a dictionary, that contains:
        ```python
        'size': size of the selected data,
        'sid_count': number of sids,
        'sid_list': list of the sids,
        'topic_count': number of topics,
        'topic_list': list of topics,
        'message_count': number of messages
        ```
        If specific sid is set, also appends dictionary 'sids', with the following structure:
        ```python
        'sids': {
          <sid, int>: {
            'topics': {
              <topic_name, str>: {
                'message_count': number of messages,
                'start_time': time when simulation started,
                'end_time': time when simulation ended,
                'duration': duration of the simulation process,
                'frequency': frequency of the simulation process (in Hz)}}}}
        ```
        If topic is specified, appends dictionary 'topics':
        ```python
        'topics': {
          <topic_name, str>: {
            'type': type,
            'data_structure': structure of the data,
            'message_count': number of messages}}
        ```
        If the topic has multiple types with the same data structure, they are presented in 
        'type' as a list. If the types have different data structures, they are grouped by 
        their data structure types and numbered as "type_group_0", "type_group_1", and so on:
        ```python
        'topics': {
          <topic_name, str>: {
            "type_group_0": {
              'type': type,
              'data_structure': structure of the data,
              'message_count': number of messages},
            "type_group_1": {
              'type': type,
              'data_structure': structure of the data,
              'message_count': number of messages}}}
        ```

        Returns
        -------
        out : citros_data_analysis.data_access.citros_dict.CitrosDict
            Information about the batch.

        Examples
        --------
        Display information about batch 'dynamics':

        >>> citros = da.CitrosDB()
        >>> citros.batch('dynamics').info().print()
        {
         'size': '27 kB',
         'sid_count': 3,
         'sid_list': [1, 2, 3],
         'topic_count': 4,
         'topic_list': ['A', 'B', 'C', 'D'],
         'message_count': 100
        }

        Display information about topic 'C' of the batch 'dynamics':

        >>> citros.batch('dynamics').topic('C').info().print()
        {
         'size': '6576 bytes',
         'sid_count': 3,
         'sid_list': [1, 2, 3],
         'topic_count': 1,
         'topic_list': ['C'],
         'message_count': 24,
         'topics': {
           'C': {
             'type': 'c',
             'data_structure': {
               'data': {
                 'x': {
                   'x_1': 'int', 
                   'x_2': 'float',
                   'x_3': 'float'
                 },
                 'note': 'list',
                 'time': 'float',
                 'height': 'float'
               }
             },
             'message_count': 24
           }
         }
        }

        Display information about simulation run 1 and 2 of the batch 'dynamics':

        >>> citros.batch('dynamics').sid([1,2]).info().print()
        {
         'size': '20 kB',
         'sid_count': 2,
         'sid_list': [1, 2],
         'topic_count': 4,
         'topic_list': ['A', 'B', 'C', 'D'],
         'message_count': 76,
         'sids': {
           1: {
             'topics': {
               'A': {
                  'message_count': 4,
                  'start_time': 2000000000,
                  'end_time': 17000000000,
                  'duration': 15000000000,
                  'frequency': 0.267
               },
               'B': {
                  'message_count': 9,
        ...
                  'duration': 150000000,
                  'frequency': 60.0
               }
             }
           }
         }
        }

        Display information about simulation run 1 and 2 of the topic 'C' of the batch 'dynamics':

        >>> citros.batch('dynamics').topic('C').sid(2).info().print()
        {
         'size': '2192 bytes',
         'sid_count': 1,
         'sid_list': [2],
         'topic_count': 1,
         'topic_list': ['C'],
         'message_count': 8,
         'sids': {
           2: {
             'topics': {
               'C': {
                 'message_count': 8,
                 'start_time': 7000000170,
                 'end_time': 19000000800,
                 'duration': 12000000630,
                 'frequency': 0.667
               }
             }
           }
         },
         'topics': {
           'C': {
             'type': 'c',
             'data_structure': {
               'data': {
                 'x': {
                   'x_1': 'int', 
                   'x_2': 'float',
                   'x_3': 'float'
                 },
                 'note': 'list',
                 'time': 'float',
                 'height': 'float'
                 }
               },
             'message_count': 8
           }
         }
        }
        '''
        for _ in range(2):
            waiting_event = False
            if not self._is_batch_available():
                # if the status 'UNLOADED', 'LOADING', 'ERROR', None
                if not self.async_query:
                    waiting_result = self._async_wait()
                    waiting_event = True
                    if not waiting_result:
                        return CitrosDict({})
                else:
                    return CitrosDict({})
            result, error_name = _PgCursor._pg_info(self)
            if error_name is not None:
                handle_res = self._handle_pg_error(error_name)
                if (not self.async_query) and handle_res:
                    # try again because batch_status erroneously was 'LOADED' but batch was not downloaded into postgres
                    if waiting_event:
                        # but do not if we have already waited for batch - probably data was not simulated
                        print("Please check if the the simulation run was successful or try to query later")
                        break
                else:
                    break
            else:
                break
        return result
    
    def get_data_structure(self, topic: str = None):
        '''
        Display table with topic names, types and corresponding them data structures of the json-data columns for the specific batch.

        Batch must be set during initialization of CitrosDB object or by `batch()` method.

        Parameters
        ----------
        topic : list or list of str, optional
            List of the topics to show data structure for.
            Have higher priority, than those defined by `topic()` and `set_filter()` methods 
            and will override them.
            If not specified, shows data structure for all topics.

        See Also
        --------
        CitrosDB.batch

        Examples
        --------
        Print structure of the json-data column for topics 'A' and 'C' of the batch 'kinematics':

        >>> citros = da.CitrosDB()
        >>> citros.batch('kinematics').topic(['A', 'C']).get_data_structure()
        
        or
        
        >>> citros.batch('kinematics').get_data_structure(['A', 'C'])
        +-------+------+-----------------+
        | topic | type | data            |
        +-------+------+-----------------+
        |     A |    a | {               |
        |       |      |   x: {          |
        |       |      |     x_1: float, |
        |       |      |     x_2: float, |
        |       |      |     x_3: float  |
        |       |      |   },            |
        |       |      |   note: list,   |
        |       |      |   time: float,  |
        |       |      |   height: float |
        |       |      | }               |
        +-------+------+-----------------+
        |     C |    c | {               |
        |       |      |   x: {          |
        |       |      |     x_1: float, |
        |       |      |     x_2: float, |
        |       |      |     x_3: float  |
        |       |      |   },            |
        |       |      |   note: list,   |
        |       |      |   time: float,  |
        |       |      |   height: float |
        |       |      | }               |
        +-------+------+-----------------+
        '''
        for _ in range(2):
            waiting_event = False
            if not self._is_batch_available():
                # if the status 'UNLOADED', 'LOADING', 'ERROR', None
                if not self.async_query:
                    waiting_result = self._async_wait()
                    waiting_event = True
                    if not waiting_result:
                        return None
                else:
                    return None
            error_name = _PgCursor._pg_get_data_structure(self, topic = topic)
            if error_name is not None:
                handle_res = self._handle_pg_error(error_name)
                if (not self.async_query) and handle_res:
                    # try again because batch_status erroneously was 'LOADED' but batch was not downloaded into postgres
                    if waiting_event:
                        # but do not if we have already waited for batch - probably data was not simulated
                        print("Please check if the the simulation run was successful or try to query later")
                        break
                else:
                    break
            else:
                break
    
    def set_filter(self, filter_by: dict = None) -> CitrosDB:
        '''
        Set constraints on query.

        Allows to set constraints on json-data columns before querying.

        Parameters
        ----------
        filter_by : dict
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}, where:
            - key_n - must match labels of the columns,
            - value_n  - in the case of equality: list of exact values,
                       in the case of inequality: dict with ">", ">=", "<" or "<=".
            Conditions, passed here, have higher priority over those defined by `topic()`, `rid()`, `sid()` and `time()` and will override them.
            If one of the sampling method is used (`skip()`, `avg()` or `move_avg()`), constraints on additional columns (rid, sid, time) are applied 
            BEFORE sampling while constraints on columns from json-data are applied AFTER sampling.

        Returns
        -------
        out : CitrosDB
            CitrosDB with set constraints.

        See Also
        --------
        CitrosDB.topic : set topic name to query
        CitrosDB.sid : set sid values to query
        CitrosDB.rid : set rid values to query
        CitrosDB.time : set time constraints
        CitrosDB.set_order : set order of the output

        Examples
        --------
        If the structure of the data column is the following:
        
        ```python
        {x: {x_1: 11}, note: [13, 34]}
        {x: {x_1: 22}, note: [11, 35]}
        {x: {x_1: 12}, note: [12, 36]}
        ...
        ```
        to get data of the batch 'testing' for topic 'A' where values of json-data column 10 < data.x.x_1 <= 20:
        
        >>> citros = da.CitrosDB()
        >>> citros.batch('testing').topic('A').set_filter({'data.x.x_1': {'>': 10, '<=': 20}}).data()
             sid  rid  time topic type  data.x.x_1     data.note
        0      0    0  4862     A    a          11      [13, 34]
        1      0    2  7879     A    a          12      [12, 36]
        ...

        get data where the value on the first position in the json-array 'note' equals 11 or 12:
        
        >>> citros.batch('testing').topic('A').set_filter({'data.note[0]': [11, 12]}).data()
             sid  rid  time topic type  data.x.x_1     data.note
        0      0    1  4862     A    a          22      [11, 35]
        1      0    2  7879     A    a          12      [12, 36]
        ...
        '''
        ci = self._copy()
        _PgCursor.set_filter(ci, filter_by = filter_by)
        return ci

    def set_order(self, order_by: Optional[Union[str, list, dict]] = None) -> CitrosDB:
        '''
        Apply sorting to the result of the data querying.

        Sort the result of the query in ascending or descending order.

        Parameters
        ----------
        order_by : str, list of str or dict, optional
            If `order_by` is a single string or a list of strings, it represents the column label(s) by which the result is sorted in ascending order.
            For more control, use a dictionary with column labels as keys and values ('asc' for ascending, 'desc' for descending) to define the sorting order.

        Examples
        --------
        Get data from the batch 'aerodynamics' for topic 'A' and sort the result by sid in ascending order and by rid in descending order.

        >>> citros = da.CitrosDB()
        >>> df = citros.batch('aerodynamics').topic('A').set_order({'sid': 'asc', 'rid': 'desc'}).data()

        Sort the result by sid and rid in ascending order:

        >>> citros = da.CitrosDB()
        >>> df = citros.batch('aerodynamics').topic('A').set_order(['sid', 'rid']).data()
        '''
        ci = self._copy()
        _PgCursor.set_order(ci, order_by = order_by)
        return ci
    
    def skip(self, s: int = None):
        '''
        Select each `s`-th message.

        `skip` is aimed to reduce the number of rows in the query output.
        This method should be called before querying methods `data()` or `data_dict()`.
        Messages with different sids are selected separately.
        If any constraints on 'sid', 'rid', 'time', 'topic' and 'type' columns are set, they are applied before sampling, while constraints on data from json column are applied after sampling.

        Parameters
        ----------
        s : int, optional
            Control number of the messages to skip, only every `s`-th message will be selected.

        Returns
        -------
        out : CitrosDB
            CitrosDB with parameters set for sampling method 'skip'.

        See Also
        --------
        CitrosDB.avg, CitrosDB.move_avg, CitrosDB.data, CitrosDB.data_dict

        Examples
        --------
        Get every 3th message of the topic 'A':
        
        >>> citros = da.CitrosDB()
        >>> df = citros.topic('A').skip(3).data()
        the 1th, the 4th, the 7th ... messages will be selected
        '''
        ci = self._copy()
        _PgCursor.skip(ci, n_skip = s)
        return ci
    
    def avg(self, n: int = None) -> CitrosDB:
        '''
        Set the directive to group and average every set of `n` consecutive messages in the database before querying.

        `avg()` is aimed to reduce number of rows before querying.
        This method should be called before querying methods `data()` or `data_dict()`.
        Messages with different sids are processed separately. 
        While averaging, the value in the 'rid' column is determined by taking the minimum 'rid' value from the rows being averaged.
        If any constraints on 'sid', 'rid', 'time', 'topic' and 'type' columns are set, they are applied before sampling, while constraints on data from json column are applied after sampling.

        Parameters
        ----------
        n : int
            Number of messages to average.

        Returns
        -------
        out : CitrosDB
            CitrosDB with parameters set for sampling method 'avg'.

        See Also
        --------
        CitrosDB.skip, CitrosDB.move_avg, CitrosDB.data, CitrosDB.data_dict

        Examples
        --------
        Average each 3 messages of the topic 'A' and then query the result:
        
        >>> citros = da.CitrosDB()
        >>> df = citros.topic('A').avg(3).data()
        '''
        ci = self._copy()
        _PgCursor.avg(ci, n_avg = n)
        return ci
    
    def move_avg(self, n: int = None, s: int = 1):
        '''
        Set the directive to compute moving average with the window size equals `n` and then during querying select each `s`-th message of the result.

        `move_avg()` is aimed to smooth data and reduce number of rows in the query output.
        This method should be called before querying methods `data()` or `data_dict()`.
        Messages with different sids are processed separately.
        While averaging, the value in the 'rid' column is determined by taking the minimum 'rid' value from the rows being averaged.
        If any constraints on 'sid', 'rid', 'time', 'topic' and 'type' columns are set, they are applied before sampling, while constraints on data from json column are applied after sampling.

        Parameters
        ----------
        n : int, optional
            Number of messages to average.
        s : int, default 1
            Control number of the messages to skip, only every `s`-th message will be selected.

        Returns
        -------
        out : CitrosDB
            CitrosDB with parameters set for sampling method 'move_avg'.

        Examples
        --------
        For data in topic 'A' calculate moving average with the window equals 5 
        and select every second row of the result:
        
        >>> citros = da.CitrosDB()
        >>> df = citros.topic('A').move_avg(5,2).data()
        '''
        ci = self._copy()
        _PgCursor.move_avg(ci, n_avg = n, n_skip = s)
        return ci

    def data(self, data_names: list = None, additional_columns: list = None) -> pd.DataFrame:
        '''
        Return pandas.DataFrame with data.

        Query data according to the constraints set by `batch()`, `topic()`, `rid()`, `sid()` and `time()` methods
        and one of the aggregative methods `skip()`, `avg()` or `move_avg()`.
        The order of the output can be set by `set_order()` method, be default the output is ordered by 'sid' and 'rid' columns.

        Parameters
        ----------
        data_names : list, optional
            Labels of the columns from json data column.
        additional_columns : list, optional
            Columns to download outside the json data column: `sid`, `rid`, `time`, `topic`, `type`.
            `sid` column is always queried.
            If not specified then all additional columns are queried.

        Returns
        -------
        out : pandas.DataFrame
            Table with selected data.

        See Also
        --------
        CitrosDB.batch, CitrosDB.topic, CitrosDB.rid, CitrosDB.sid, CitrosDB.time, CitrosDB.skip, CitrosDB.avg, CitrosDB.move_avg, CitrosDB.set_order,
        CitrosDB.data_dict

        Examples
        --------
        If the structure of the data column in the batch 'dynamics' in the topic 'A' is the following:
        
        ```python
        {x: {x_1: 1}, note: ['a', 'b']}
        {x: {x_1: 2}, note: ['c', 'd']}
        ...
        ```
        to get the column with the values of json-object 'x_1'
        and the column with the values from the first position in the json-array 'note':

        >>> citros = da.CitrosDB()
        >>> df = citros.batch('dynamics').topic('A').data(["data.x.x_1", "data.note[0]"])
        >>> df
             sid  rid  time topic type  data.x.x_1  data.note[0]
        0      0    0  4862     A    a           1             a
        1      0    1  7749     A    a           2             c
        ...

        Get the whole 'data' column with json-objects divided into separate columns:
        
        >>> df = citros.batch('dynamics').topic('A').data()
        >>> df
             sid  rid  time topic type  data.x.x_1  data.note
        0      0    0  4862     A    a           1     [a, b]
        1      0    1  7749     A    a           2     [c, d]
        ...

        Get the whole 'data' column as a json-object:
        
        >>> df = citros.batch('dynamics').topic('A').data(["data"])
        >>> df
             sid  rid  time topic type                             data
        0      0    0  4862     A    a  {x: {x_1: 1}, note: ['a', 'b']}
        1      0    1  7749     A    a  {x: {x_1: 2}, note: ['c', 'd']}
        ...

        Besides the json data column, there are some additional columns: simulation run id (sid), rid, time, topic, and type. 
        By default, all of them are queried. To select only particular ones, use `additional_columns` parameter 
        (note that the 'sid' column is always queried):

        >>> dfs = citros.batch('dynamics').topic('A').set_order({'rid': 'asc'}).avg(2)\\
                        .data(['data.x.x_1', 'data.x.x_2'], additional_columns = ['rid', 'topic'])
        >>> dfs[2]
             sid  rid  topic  data.x.x_1  data.x.x_2
        0      2    0      A         1.5           8
        1      2    2      A           5          10
        ...
        '''
        for _ in range(2):
            waiting_event = False
            if not self._is_batch_available():
                # if the status 'UNLOADED', 'LOADING', 'ERROR', None
                if not self.async_query:
                    waiting_result = self._async_wait()
                    waiting_event = True
                    if not waiting_result:
                        return None
                else:
                    return None
            result, error_name = _PgCursor._data(self, data_names = data_names, additional_columns = additional_columns)
            if error_name is not None:
                handle_res = self._handle_pg_error(error_name)
                if (not self.async_query) and handle_res:
                    # try again because batch_status erroneously was 'LOADED' but batch was not downloaded into postgres
                    if waiting_event:
                        # but do not if we have already waited for batch - probably data was not simulated
                        print("Please check if the the simulation run was successful or try to query later")
                        break
                else:
                    break
            else:
                break
        return result
    
    def data_dict(self, data_names: list = None, additional_columns: list = None) -> pd.DataFrame:
        '''
        Return a dict where a dict key is a simulation run id (sid), and a dict value is a pandas.DataFrame related to that sid.

        Parameters
        ----------
        data_names : list, optional
            Labels of the columns from json data column.
        additional_columns : list, optional
            Columns to download outside the json data column: `sid`, `rid`, `time`, `topic`, `type`.
            `sid` column is always queried.
            If not specified then all additional columns are queried.

        Returns
        -------
        out : dict of pandas.DataFrames
            dict with tables, key is a value of sid.

        See Also
        --------
        CitrosDB.data

        Examples
        --------
        Let's suppose that the structure of the data column in the batch 'dynamics' for simulation run sid = 2 in the topic 'A' is the following:
        
        ```python
        {x: {x_1: 1, x_2: 3}
        {x: {x_1: 2, x_2: 13}
        {x: {x_1: 4, x_2: 15}
        {x: {x_1: 6, x_2: 5}
        ...
        ```

        Download averaged data for each sid separately, return output in ascending order by 'rid':

        >>> citros = da.CitrosDB()
        >>> dfs = citros.batch('dynamics').topic('A').set_order({'rid': 'asc'}).avg(2)\\
                        .data_dict(['data.x.x_1', 'data.x.x_2'])

        Print sid values:

        >>> print(f'sid values are: {list(dfs.keys())}')
        sid values are: [1, 2, 3, 4]

        Get table corresponding to the sid = 2:

        >>> dfs[2]
             sid  rid  time topic type  data.x.x_1  data.x.x_2
        0      2    0  6305     A    a         1.5           8
        1      2    2  7780     A    a           5          10
        ...

        Besides the json data column, there are some additional columns: simulation run id (sid), rid, time, topic, and type. 
        By default, all of them are queried. To select only particular ones, use `additional_columns` parameter 
        (note that the 'sid' column is always queried):

        >>> dfs = citros.batch('dynamics').topic('A').set_order({'rid': 'asc'}).avg(2)\\
                        .data_dict(['data.x.x_1', 'data.x.x_2'], additional_columns = ['rid', 'topic'])
        >>> dfs[2]
             sid  rid  topic  data.x.x_1  data.x.x_2
        0      2    0      A         1.5           8
        1      2    2      A           5          10
        ...
        '''
        for _ in range(2):
            waiting_event = False
            if not self._is_batch_available():
                # if the status 'UNLOADED', 'LOADING', 'ERROR', None
                if not self.async_query:
                    waiting_result = self._async_wait()
                    waiting_event = True
                    if not waiting_result:
                        return {}
                else:
                    return {}
            result_table, error_name = _PgCursor._data(self, data_names = data_names, additional_columns = additional_columns)
            if error_name is not None:
                handle_res = self._handle_pg_error(error_name)
                if (not self.async_query) and handle_res:
                    # try again because batch_status erroneously was 'LOADED' but batch was not downloaded into postgres
                    if waiting_event:
                        # but do not if we have already waited for batch - probably data was not simulated
                        print("Please check if the the simulation run was successful or try to query later")
                        break
                else:
                    break
            else:
                break
        
        if result_table is not None:
            sid_list = list(set(result_table['sid']))
            tables = {}
            for s in sid_list:
                flag = result_table['sid'] == s
                tables[s] = result_table[flag].reset_index(drop = True)
            return tables
        else:
            return {}

    def get_sid_tables(self, data_query: list = None, topic: Optional[Union[str, list]] = None, additional_columns: list = None, 
                       filter_by: dict = None, order_by: Optional[Union[str, list, dict]] = None, 
                       method: str = None, n: int = 1, s: int = 1):
        '''
        Return a dict where each key represents a specific sid value, and its corresponding value is a pandas.DataFrame related to that sid.

        .. deprecated:: 0.9.0
            Use `CitrosDB.data_dict` instead.

        Parameters
        ----------
        data_query : list, optional
            Labels of the data to download from the json-format column "data".
            If blank list, then all columns are are downloaded.
        topic : str or list of str
            Name of the topic.
            Have higher priority than defined by `topic()`.
            May be overridden by `filter_by` argument.
        additional_columns : list, optional
            Columns to download outside the json "data".
            If blank list, then all columns are are downloaded.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}, where:
            - key_n - must match labels of the columns,
            - value_n - in the case of equality: list of exact values
                        in the case of inequality: dict with ">", ">=", "<" or "<=".
            Conditions, passed here, have higher priority over those defined by `topic()`, `rid()`, `sid()`, `time()` and `set_filter()` and will override them.
        order_by : str or list of str or dict, optional
            If `order_by` is a single string or a list of strings, it represents the column label(s) by which the result is sorted in ascending order.
            For more control, use a dictionary with column labels as keys and values ('asc' for ascending, 'desc' for descending) to define the sorting order.
            Conditions, passed here, have higher priority over those defined by `set_order()` and will override them.
        method : {'', 'avg', 'move_avg', 'skip'}, optional
            Method of sampling:
            'avg' - average - average `n` rows;
            'move_avg' - moving average - average `n` rows and return every `s`-th row;
            'skip' - select every `s`-th row;
            '' - no sampling.
            If not specified, no sampling is applied.
        n : int, default 1
            Used only if `method` is 'move_avg' or 'avg'.
            Number of rows for averaging.
        s : int, default 1
            Used only if `method` is 'move_avg' or 'skip'.
            Number of rows to skip in a result output. 
            For example, if s = 2, only every second row will be returned.

        Returns
        -------
        out : dict of pandas.DataFrames
            dict with tables, key is a value of sid.

        Examples
        --------
        Download averaged data for each sid separately, setting ascending order by 'rid':

        >>> citros = da.CitrosDB()
        >>> dfs = citros.topic('A').set_order({'rid': 'asc'}).avg(2)\\
                        .get_sid_tables(data_query=['data.x.x_1'])

        Print sid values:

        >>> print(f'sid values are: {list(dfs.keys())}')
        sid values are: [1, 2, 3, 4]

        Get table corresponding to the sid = 2 and assign it to 'df':

        >>> df = dfs[2]

        The same, but setting constraints by parameters: 

        >>> dfs = citros.get_sid_tables(data_query = ['data.x.x_1'],
        ...                             topic = 'A', 
        ...                             additional_columns = [], 
        ...                             filter_by = {}, 
        ...                             order_by = {'rid': 'asc'}, 
        ...                             method = 'avg', 
        ...                             n = 2)
        >>> print(f'sid values are: {list(dfs.keys())}')
        sid values are: [1, 2, 3, 4]
        '''
        warnings.warn(
            "The CitrosDB.get_sid_tables method has been deprecated "
            "and will be removed in a future version.\n"
            "Use CitrosDB.data_dict instead.",
            FutureWarning,
            stacklevel = 2
        )
        if not self._is_batch_available():
            return None
        result, error_name = _PgCursor._get_sid_tables(self, data_query, topic, additional_columns, filter_by, order_by, method, n, s)
        if (self.async_query) and (error_name is not None):
            self._handle_pg_error(error_name)
        return result
    
    def get_min_value(self, column_name: str, filter_by: dict = None, return_index: bool = False):
        '''
        Return minimum value of the column `column_name`.

        Parameters
        ----------
        column_name : str
            Label of the column.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}, where:
            - key_n - must match labels of the columns,
            - value_n  - in the case of equality: list of exact values,
                       in the case of inequality: dict with ">", ">=", "<" or "<=".
            Conditions, passed here, have higher priority over those defined by `topic()`, `rid()`, `sid()`, `time()` and `set_filter()` and will override them.
        return_index : bool, default False
            If True, the pair of sid and rid corresponding to the obtained minimum value is also returned.
            If there are several cases when the maximum or minimum value is reached, the lists of corresponding sids and rids are returned.

        Returns
        -------
        value : int, float, str or None
            Minimum value of the column `column_name`.
        sid : int or list
            Corresponding to the minimum value's sid. Returns only if `return_index` is set to True.
        rid : int or list
            Corresponding to the minimum value's rid. Returns only if `return_index` is set to True.

        Examples
        --------
        Get min value of the column 'data.x.x_2' where topics are 'A' or 'B', 10 <= 'time' <= 5000 and data.x.x_1 > 10:

        >>> citros = da.CitrosDB()
        >>> result = citros.topic(['A', 'B'])\\
        ...                .set_filter({'data.x.x_1': {'>=': 10}})\\
        ...                .time(start = 10, end = 5000)\\
        ...                .get_min_value('data.x.x_2')
        >>> print(result)
        -4.0

        Get also the sid and rid of the minimum value:

        >>> result, sid_min, rid_min = citros.topic(['A', 'B'])\\
        ...                            .set_filter({'data.x.x_1': {'>=': 10}})\\
        ...                            .time(start = 10, end = 5000)\\
        ...                            .get_min_value('data.x.x_2', return_index = True)
        >>> print(f"min = {result} at sid = {sid_min}, rid = {rid_min}")
        min = -4.0 at sid = 4, rid = 44

        The same as in the first example, but passing all constraints by `filter_by` parameter:

        >>> result = citros.get_min_value('data.x.x_2',
        ...                               filter_by = {'topic': ['A', 'B'], 
        ...                                            'time': {'>=': 10, '<=': 5000}, 
        ...                                            'data.x.x_1' : {'>':10}})
        >>> print(result)
        -4.0
        '''
        for _ in range(2):
            waiting_event = False
            if not self._is_batch_available():
                # if the status 'UNLOADED', 'LOADING', 'ERROR', None
                if not self.async_query:
                    waiting_result = self._async_wait()
                    waiting_event = True
                    if not waiting_result:
                        return None, None, None if return_index else None
                else:
                    return None, None, None if return_index else None

            result, error_name = _PgCursor.get_min_max_value(self, column_name = column_name, filter_by = filter_by, 
                                           return_index = return_index, mode = 'MIN')
            if error_name is not None:
                handle_res = self._handle_pg_error(error_name)
                if (not self.async_query) and handle_res:
                    # try again because batch_status erroneously was 'LOADED' but batch was not downloaded into postgres
                    if waiting_event:
                        # but do not if we have already waited for batch - probably data was not simulated
                        print("Please check if the the simulation run was successful or try to query later")
                        break
                else:
                    break
            else:
                break
        return result
    
    def get_max_value(self, column_name: str, filter_by: dict = None, return_index: bool = False):
        '''
        Return maximum value of the column `column_name`.

        Parameters
        ----------
        column_name : str
            Label of the column.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}, where:
            - key_n - must match labels of the columns,
            - value_n  - in the case of equality: list of exact values,
                       in the case of inequality: dict with ">", ">=", "<" or "<=".
            Conditions, passed here, have higher priority over those defined by `topic()`, `rid()`, `sid()`, `time()` and `set_filter()` and will override them.
        return_index : bool, default False
            If True, the pair of sid and rid corresponding to the obtained maximum value is also returned.

        Returns
        -------
        value : int, float, str or None
            Maximum value of the column `column_name`.
        sid : int or list
            Corresponding to the maximum value's sid. Returns only if `return_index` is set to True.
        rid : int or list
            Corresponding to the maximum value's rid. Returns only if `return_index` is set to True

        Examples
        --------
        Get max value of the column 'data.x.x_2' where topics are 'A' or 'B', 10 <= 'time' <= 5000 and data.x.x_1 > 10:
        
        >>> citros = da.CitrosDB()
        >>> result = citros.topic(['A', 'B'])\\
        ...                .set_filter({'data.x.x_1': {'>=': 10}})\\
        ...                .time(start = 10, end = 5000)\\
        ...                .get_max_value('data.x.x_2')
        >>> print(result)
        76.0

        Get also the sid and rid of the maximum value:

        >>> result, sid_max, rid_max = citros.topic(['A', 'B'])\\
        ...                            .set_filter({'data.x.x_1': {'>=': 10}})\\
        ...                            .time(start = 10, end = 5000)\\
        ...                            .get_max_value('data.x.x_2', return_index = True)
        >>> print(f"max = {result} at sid = {sid_max}, rid = {rid_max}")
        max = 76.0 at sid = 4, rid = 47

        The same as in the first example, but passing all constraints by `filter_by` parameter:

        >>> result = citros.get_max_value('data.x.x_2',
        ...                               filter_by = {'topic': ['A', 'B'], 
        ...                                            'time': {'>=': 10, '<=': 5000}, 
        ...                                            'data.x.x_1' : {'>':10}})
        >>> print(result)
        76.0
        '''
        for _ in range(2):
            waiting_event = False
            if not self._is_batch_available():
                # if the status 'UNLOADED', 'LOADING', 'ERROR', None
                if not self.async_query:
                    waiting_result = self._async_wait()
                    waiting_event = True
                    if not waiting_result:
                        return None, None, None if return_index else None
                else:
                    return None, None, None if return_index else None
            result, error_name = _PgCursor.get_min_max_value(self, column_name = column_name, filter_by = filter_by, 
                                           return_index = return_index, mode = 'MAX')
            if error_name is not None:
                handle_res = self._handle_pg_error(error_name)
                if (not self.async_query) and handle_res:
                    # try again because batch_status erroneously was 'LOADED' but batch was not downloaded into postgres
                    if waiting_event:
                        # but do not if we have already waited for batch - probably data was not simulated
                        print("Please check if the the simulation run was successful or try to query later")
                        break
                else:
                    break
            else:
                break
        return result

    def get_counts(self, column_name: str = None, group_by: Optional[Union[str, list]] = None, filter_by: dict = None, 
                   nan_exclude: bool = False) -> list:
        '''
        Return number of the rows in the column `column_name`.

        Parameters
        ----------
        column_name : str
            Label of the column.
        group_by : list, optional
            Labels of the columns to group by. If blank, do not group.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}, where:
            - key_n - must match labels of the columns,
            - value_n  - in the case of equality: list of exact values,
                       in the case of inequality: dict with ">", ">=", "<" or "<=".
            Conditions, passed here, have higher priority over those defined by `topic()`, `rid()`, `sid()`, `time()` and `set_filter()` and will override them.
        nan_exclude : bool, default False
            If True, nan values are excluded from the count.

        Returns
        -------
        out : list of tuples or None
            Number of rows in `column_name`.

        Examples
        --------
        Calculate the total number of rows:

        >>> citros = da.CitrosDB()
        >>> citros.get_counts()
        [(300,)]

        Calculate the total number of rows in the topic 'A':

        >>> citros = da.CitrosDB()
        >>> citros.topic('A').get_counts()
        [(100,)]

        If the structure of the data column is the following:

        ```python
        {x: {x_1: 52}, note: ['b', 'e']}
        {x: {x_1: 11}, note: ['a', 'c']}
        {x: {x_1: 92}, note: ['b', 'd']}
        ...
        ```
        to find the number of values from the first position of the json-array 'note' for topics 'A' or 'B',
        where 10 <= 'time' <= 5000 and data.x.x_1 > 10:

        >>> citros = da.CitrosDB()
        >>> citros.topic(['A', 'B'])\\
        ...       .set_filter({'data.x.x_1': {'>': 10}})\\
        ...       .time(start = 10, end = 5000)\\
        ...       .get_counts('data.note[0]')
        [(30,)]

        To perform under the same conditions, but to get values grouped by topics:

        >>> citros.topic(['A', 'B'])\\
        ...       .set_filter({'data.x.x_1': {'>': 10}})\\
        ...       .time(start = 10, end = 5000)\\
        ...       .get_counts('data.note[0]', group_by = ['topic'])
        [('A', 17), ('B', 13)]

        The same, but passing all constraints by `filter_by` parameter:
        
        >>> citros.get_counts('data.note[0]',
        ...                    group_by = ['topic'],
        ...                    filter_by = {'topic': ['A', 'B'], 
        ...                                 'time': {'>=': 10, '<=': 5000}, 
        ...                                 'data.x.x_1' : {'>':10}})
        [('A', 17), ('B', 13)]
        '''
        for _ in range(2):
            waiting_event = False
            if not self._is_batch_available():
                # if the status 'UNLOADED', 'LOADING', 'ERROR', None
                if not self.async_query:
                    waiting_result = self._async_wait()
                    waiting_event = True
                    if not waiting_result:
                        return None
                else:
                    return None
            result, error_name = _PgCursor._get_counts(self, column_name = column_name, group_by = group_by, filter_by= filter_by, 
                                                       nan_exclude = nan_exclude)
            if error_name is not None:
                handle_res = self._handle_pg_error(error_name)
                if (not self.async_query) and handle_res:
                    # try again because batch_status erroneously was 'LOADED' but batch was not downloaded into postgres
                    if waiting_event:
                        # but do not if we have already waited for batch - probably data was not simulated
                        print("Please check if the the simulation run was successful or try to query later")
                        break
                else:
                    break
            else:
                break
        return result

    def get_unique_counts(self, column_name: str = None, group_by: list = None, filter_by: dict = None, 
                          nan_exclude: bool = False) -> list:
        '''
        Return number of the unique values in the column `column_name`.

        Parameters
        ----------
        column_name : str
            Column to count its unique values.
        group_by : list, optional
            Labels of the columns to group by. If blank, do not group.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}, where:
            - key_n - must match labels of the columns,
            - value_n  - in the case of equality: list of exact values,
                       in the case of inequality: dict with ">", ">=", "<" or "<=".
            Conditions, passed here, have higher priority over those defined by `topic()`, `rid()`, `sid()`, `time()` and `set_filter()` and will override them.
        nan_exclude : bool, default False
            If True, nan values are excluded from the count.

        Returns
        -------
        out : list of tuples or None
            Counts of the unique values in `column_name`.

        Examples
        --------
        If the structure of the data column is the following:

        ```python
        {x: {x_1: 52}, note: ['b', 'e']}
        {x: {x_1: 11}, note: ['a', 'c']}
        {x: {x_1: 92}, note: ['b', 'd']}
        ...
        ```
        to get the number of unique values from the first position of the json-array 'note' for topics 'A' or 'B',
        where 10 <= 'time' <= 5000 and data.x.x_1 > 10:

        >>> citros = da.CitrosDB()
        >>> citros.topic(['A', 'B'])\\
        ...       .set_filter({'data.x.x_1': {'>': 10}})\\
        ...       .time(start = 10, end = 5000)\\
        ...       .get_unique_counts('data.note[0]')
        [(2,)]

        To perform under the same conditions, but to get values grouped by topics:

        >>> citros.topic(['A', 'B'])\\
        ...       .set_filter({'data.x.x_1': {'>': 10}})\\
        ...       .time(start = 10, end = 5000)\\
        ...       .get_unique_counts('data.note[0]', group_by = ['topic'])
        [('A', 2), ('B', 2)]
        
        The same, but passing all constraints by `filter_by` parameter:

        >>> citros.get_unique_counts('data.note[0]',
        ...                           group_by = ['topic'],
        ...                           filter_by = {'topic': ['A', 'B'], 
        ...                                        'time': {'>=': 10, '<=': 5000}, 
        ...                                        'data.x.x_1' : {'>':10}})
        [('A', 2), ('B', 2)]
        '''
        for _ in range(2):
            waiting_event = False
            if not self._is_batch_available():
                # if the status 'UNLOADED', 'LOADING', 'ERROR', None
                if not self.async_query:
                    waiting_result = self._async_wait()
                    waiting_event = True
                    if not waiting_result:
                        return None
                else:
                    return None
            result, error_name = _PgCursor._get_unique_counts(self, column_name = column_name, group_by = group_by, filter_by = filter_by, 
                          nan_exclude = nan_exclude)
            if error_name is not None:
                handle_res = self._handle_pg_error(error_name)
                if (not self.async_query) and handle_res:
                    # try again because batch_status erroneously was 'LOADED' but batch was not downloaded into postgres
                    if waiting_event:
                        # but do not if we have already waited for batch - probably data was not simulated
                        print("Please check if the the simulation run was successful or try to query later")
                        break
                else:
                    break
            else:
                break
        return result

    def get_unique_values(self, column_names: Optional[Union[str, list]], filter_by: dict = None) -> list:
        '''
        Return unique values of the columns `column_names`.

        Parameters
        ----------
        column_names : str or list of str
            Columns for which the unique combinations of the values will be found.
        filter_by : dict, optional
            Constraints to apply on columns: {key_1: value_1, key_2: value_2, ...}, where:
            - key_n - must match labels of the columns,
            - value_n  - in the case of equality: list of exact values,
                       in the case of inequality: dict with ">", ">=", "<" or "<=".
            Conditions, passed here, have higher priority over those defined by `topic()`, `rid()`, `sid()`, `time()` and `set_filter()` and will override them.

        Returns
        -------
        out : list or list of tuples
            Each tuple contains unique combinations of the values for `column_names`.

        Examples
        --------
        Get unique values of type for topics 'A' or 'B', where 10 <= 'time' <= 5000 and data.x.x_1 > 10:
        
        >>> citros = da.CitrosDB()
        >>> result = citros.topic(['A', 'B'])\\
        ...                .set_filter({'data.x.x_1': {'>': 10}})\\
        ...                .time(start = 10, end = 5000)\\
        ...                .get_unique_values(['type'])
        >>> print(result)
        ['a', 'b']

        The same, but passing all constraints by `filter_by` parameter:
        
        >>> result = citros.get_unique_values(['type'], filter_by = {'topic': ['A', 'B'], 
        ...                                       'time': {'>=': 10, '<=': 5000}, 
        ...                                       'data.x.x_1': {'>':10}})
        >>> print(result)
        ['a', 'b']
        '''
        for _ in range(2):
            waiting_event = False
            if not self._is_batch_available():
                # if the status 'UNLOADED', 'LOADING', 'ERROR', None
                if not self.async_query:
                    waiting_result = self._async_wait()
                    waiting_event = True
                    if not waiting_result:
                        return None
                else:
                    return None
            result, error_name = _PgCursor._get_unique_values(self, column_names = column_names, filter_by = filter_by)
            if error_name is not None:
                handle_res = self._handle_pg_error(error_name)
                if (not self.async_query) and handle_res:
                    # try again because batch_status erroneously was 'LOADED' but batch was not downloaded into postgres
                    if waiting_event:
                        # but do not if we have already waited for batch - probably data was not simulated
                        print("Please check if the the simulation run was successful or try to query later")
                        break
                else:
                    break
            else:
                break
        return result
    
    def time_plot(self, ax: plt.Axes, *args, topic_name: Optional[str] = None, var_name: Optional[str] = None, 
                  time_step: Optional[float] = 1.0, sids: list = None, y_label: Optional[str] = None, title_text: Optional[str] = None, 
                  legend: bool = True, remove_nan: bool = True, inf_vals: Optional[float] = 1e308, **kwargs):
        '''
        Query data and make plot `var_name` vs. `Time` for each of the sids, where `Time` = `time_step` * rid.

        Both `CitrosDB.time_plot()` and `CitrosDB.xy_plot()` methods are aimed to quickly make plots.
        They allow you to query data and plot it at once, without need to first save data as a separate DataFrame.
        The constraints on data may be set by `batch()`, `topic()`, `rid()`, `sid()` and `time()` methods
        and one of the aggregative methods `skip()`, `avg()` or `move_avg()`.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Figure axis to plot on.
        *args : Any
            Additional arguments to style lines, set color, etc, 
            see **[matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)**.
        topic_name : str
            Input topic name. If specified, will override value that was set by `topic()` method.
        var_name : str
            Name of the variable to plot along y-axis.
        time_step : float or int, default 1.0
            Time step, `Time` = `time_step` * rid.
        sids : list
            List of the sids. If specified, will override values that were set by `sid()` method.
            If not specified, data for all sids is used.
        y_label : str
            Label to set to y-axis. Default `var_name`.
        title_text : str
            Title of the figure. Default '`var_y_name` vs. Time'.
        legend : bool, default True
            If True, show the legend with sids.
        remove_nan : bool, default True
            If True, NaN values will be removed before plotting.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.

        Other Parameters
        ----------------
        kwargs : dict, optional
            Other keyword arguments, see **[matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)**.

        See Also
        --------
        CitrosDB.xy_plot,
        CitrosDB.batch, CitrosDB.topic, CitrosDB.rid, CitrosDB.sid, CitrosDB.time, CitrosDB.skip, CitrosDB.avg, CitrosDB.move_avg, CitrosDB.set_order

        Examples
        --------
        Import matplotlib and create figure to plot on:

        >>> import matplotlib.pyplot as plt
        >>> fig, ax = plt.subplots()

        For batch 'dynamics' for topic 'A' plot `data.x.x_1` vs. `Time` for all existing sids, `Time` = 0.5 * rid

        >>> citros = da.CitrosDB()
        >>> citros.batch('dynamics').topic('A').time_plot(ax, var_name = 'data.x.x_1', time_step = 0.5)

        ![time_plot_1](../../img_documentation/time_plot_1.png "time_plot_1")

        Create a new figure and plot only part of the data, where 'data.x.x_1' <= 0; plot by dashed line:

        >>> fig, ax = plt.subplots()
        >>> citros.batch('dynamics').topic('A').set_filter({'data.x.x_1':{'<=': 0}})\\
                  .time_plot(ax, '--', var_name = 'data.x.x_1', time_step = 0.5)

        ![time_plot_2](../../img_documentation/time_plot_2.png "time_plot_2")
        '''
        for _ in range(2):
            waiting_event = False
            if not self._is_batch_available():
                # if the status 'UNLOADED', 'LOADING', 'ERROR', None
                if not self.async_query:
                    waiting_result = self._async_wait()
                    waiting_event = True
                    if not waiting_result:
                        return None
                else:
                    return None
            var_df, sids, error_name = _PgCursor.data_for_time_plot(self, topic_name, var_name, time_step, sids, remove_nan, inf_vals)
            if error_name is not None:
                handle_res = self._handle_pg_error(error_name)
                if (not self.async_query) and handle_res:
                    # try again because batch_status erroneously was 'LOADED' but batch was not downloaded into postgres
                    if waiting_event:
                        # but do not if we have already waited for batch - probably data was not simulated
                        print("Please check if the the simulation run was successful or try to query later")
                        break
                else:
                    break
            else:
                break

        if var_df is None:
            return
    
        plotter = _Plotter()
        plotter.time_plot(var_df, ax, var_name, sids, y_label, title_text, legend, *args, **kwargs)

    def xy_plot(self, ax: plt.Axes, *args, topic_name: Optional[str] = None, var_x_name: Optional[str] = None, 
                var_y_name: Optional[str] = None, sids: Optional[Union[int, list]] = None, x_label: Optional[str] = None, 
                y_label: Optional[str] = None, title_text: Optional[str] = None, legend: bool = True, remove_nan: bool = True, 
                inf_vals: Optional[float] = 1e308, **kwargs):
        '''
        Query data and make plot `var_y_name` vs. `var_x_name` for each of the sids.

        Both `CitrosDB.time_plot()` and `CitrosDB.xy_plot()` methods are aimed to quickly make plots.
        They allow you to query data and plot it at once, without need to first save data as a separate DataFrame.
        The constraints on data may be set by `batch()`, `topic()`, `rid()`, `sid()` and `time()` methods
        and one of the aggregative methods `skip()`, `avg()` or `move_avg()`.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Figure axis to plot on.
        *args : Any
            Additional arguments to style lines, set color, etc, 
            see **[matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)**.
        topic_name : str
            Input topic name. If specified, will override value that was set by `topic()` method.
        var_x_name : str
            Name of the variable to plot along x-axis.
        var_y_name : str
            Name of the variable to plot along y-axis.
        sids : int or list of int, optional
            List of the sids. If specified, will override values that were set by `sid()` method.
            If not specified, data for all sids is used.
        x_label : str, optional
            Label to set to x-axis. Default `var_x_name`.
        y_label : str, optional
            Label to set to y-axis. Default `var_y_name`.
        title_text : str, optional
            Title of the figure. Default '`var_y_name` vs. `var_x_name`'.
        legend : bool, default True
            If True, show the legend with sids.
        remove_nan : bool, default True
            If True, NaN values will be removed before plotting.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.

        Other Parameters
        ----------------
        kwargs : dict, optional
            Other keyword arguments, see **[matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)**.

        See Also
        --------
        CitrosDB.time_plot,
        CitrosDB.batch, CitrosDB.topic, CitrosDB.rid, CitrosDB.sid, CitrosDB.time, CitrosDB.skip, CitrosDB.avg, CitrosDB.move_avg, CitrosDB.set_order

        Examples
        --------
        >>> import matplotlib.pyplot as plt
        >>> fig, ax = plt.subplots()

        For batch 'dynamics' for topic 'A' plot 'data.x.x_1' vs. 'data.time' for all existing sids:

        >>> citros = da.CitrosDB()
        >>> citros.batch('dynamics').topic('A').xy_plot(ax, var_x_name = 'data.x.x_1', var_y_name = 'data.time')

        ![xy_plot_1](../../img_documentation/xy_plot_1.png "xy_plot_1")

        Create new figure and plot only part of the data, where 'data.x.x_1' <= 0, sid = 1 and 2; plot by dashed lines:

        >>> fig, ax = plt.subplots()
        >>> citros.batch('dynamics').topic('A').set_filter({'data.x.x_1':{'<=': 0}}).sid([1,2])\\
                  .xy_plot(ax, '--', var_x_name = 'data.x.x_1', var_y_name = 'data.time')

        ![xy_plot_2](../../img_documentation/xy_plot_2.png "xy_plot_1")
        '''
        for _ in range(2):
            waiting_event = False
            if not self._is_batch_available():
                # if the status 'UNLOADED', 'LOADING', 'ERROR', None
                if not self.async_query:
                    waiting_result = self._async_wait()
                    waiting_event = True
                    if not waiting_result:
                        return None
                else:
                    return None
            xy_df, sids, error_name = _PgCursor.data_for_xy_plot(self, topic_name, var_x_name, var_y_name, sids, remove_nan, inf_vals)
            if error_name is not None:
                handle_res = self._handle_pg_error(error_name)
                if (not self.async_query) and handle_res:
                    # try again because batch_status erroneously was 'LOADED' but batch was not downloaded into postgres
                    if waiting_event:
                        # but do not if we have already waited for batch - probably data was not simulated
                        print("Please check if the the simulation run was successful or try to query later")
                        break
                else:
                    break
            else:
                break
        
        if xy_df is None:
            return
        
        plotter = _Plotter()
        plotter.xy_plot(xy_df, ax,  var_x_name, var_y_name, sids, x_label, y_label, title_text, legend, *args, **kwargs)
    
    def plot_graph(self, df: pd.DataFrame, x_label: str, y_label: str, *args, ax: Optional[plt.Axes] = None, legend: bool = True, 
                   title: Optional[str] = None, set_x_label: Optional[str] = None, set_y_label: Optional[str] = None, 
                   remove_nan: bool = True, inf_vals: Optional[float] = 1e308, **kwargs):
        '''
        Plot graph '`y_label` vs. `x_label`' for each sid, where `x_label` and `y_label`
        are the labels of columns of the pandas.DataFrame `df`.

        Parameters
        ----------
        df : pandas.DataFrame
            Data table.
        x_label : str
            Label of the column to plot along x-axis.
        y_label : str
            Label of the column to plot along y-axis.
        *args : Any
            Additional arguments to style lines, set color, etc, 
            see **[matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)**.
        ax : matplotlib.axes.Axes
            Figure axis to plot on. If not specified, the new pair of fig, ax will be created.
        legend : bool, default True
            If True, show the legend with sids.
        title : str
            Set title of the plot.
        set_x_label : str, default None
            Label to set to the x-axis. If None, label is set according to `x_label`.
        set_y_label : str, default None
            Label to set to the y-axis. If None, label is set according to `y_label`.
        remove_nan : bool, default True
            If True, NaN values will be removed before plotting.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.

        Returns
        -------
        fig : matplotlib.figure.Figure
            Created figure if `ax` is not passed.
        ax : matplotlib.axes.Axes
            Created axis if `ax` is not passed.

        Other Parameters
        ----------------
        kwargs : dict, optional
            Other keyword arguments, see **[matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)**.

        See Also
        --------
        CitrosDB.plot_3dgraph, CitrosDB.multiple_y_plot, CitrosDB.multiplot, CitrosDB.plot_sigma_ellipse

        Examples
        --------
        Import matplotlib and create figure to plot on:

        >>> import matplotlib.pyplot as plt
        >>> fig, ax = plt.subplots()

        Download from batch 'kinematics' for topic 'A' from json-data column 'data.x.x_1' and 'data.x.x_2' columns:

        >>> citros = da.CitrosDB()
        >>> df = citros.batch('kinematics').topic('A').data(['data.x.x_1', 'data.x.x_2'])

        Plot `data.x.x_1` vs. `data.x.x_2`:

        >>> citros.plot_graph(df, 'data.x.x_1', 'data.x.x_2', ax = ax, title = 'Example plot')

        ![plot_graph_1](../../img_documentation/plot_graph_1.png "plot_graph_1")
        
        If `ax` parameter is not passed, `plot_graph()` generates a pair of (matplotlib.figure.Figure, matplotlib.axes.Axes) objects and
        returns them. Let's plot the previous image without passing `ax` argument, and also let's plot with a dotted line:

        >>> fig, ax = citros.plot_graph(df, 'data.x.x_1', 'data.x.x_2', '.', title = 'Example plot')
        >>> fig.show()

        ![plot_graph_2](../../img_documentation/plot_graph_2.png "plot_graph_2")
        '''
        plotter = _Plotter()
        return plotter.plot_graph(df, x_label, y_label, ax, legend, title , set_x_label, set_y_label, 
                                  remove_nan, inf_vals,  *args, **kwargs)

    def plot_3dgraph(self, df: pd.DataFrame, x_label: str, y_label: str, z_label: str, *args, ax: Optional[plt.Axes] = None, 
                     scale: bool = True, legend: bool = True, title: Optional[str] = None, 
                     set_x_label: Optional[str] = None, set_y_label: Optional[str] = None, set_z_label: Optional[str] = None, 
                     remove_nan: bool = True, inf_vals: Optional[float] = 1e308, **kwargs):
        '''
        Plot 3D graph '`z_label` vs. `x_label` and `y_label`' for each sid, where `x_label`, `y_label` and `z_label`
        are the labels of columns of the pandas.DataFrame `df`.

        Parameters
        ----------
        df : pandas.DataFrame
            Data table.
        x_label : str
            Label of the column to plot along x-axis.
        y_label : str
            Label of the column to plot along y-axis.
        *args : Any
            Additional arguments to style lines, set color, etc, 
            see **[matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)**.
        ax : matplotlib.axes.Axes
            Figure axis to plot on. If not specified, the new pair of fig, ax will be created.
        scale : bool, default True
            Specify whether the axis range should be the same for all axes.
        legend : bool, default True
            If True, show the legend with sids.
        title : str
            Set title of the plot.
        set_x_label : str, default None
            Label to set to the x-axis. If None, label is set according to `x_label`.
        set_y_label : str, default None
            Label to set to the y-axis. If None, label is set according to `y_label`.
        set_z_label : str, default None
            Label to set to the z-axis. If None, label is set according to `z_label`.
        remove_nan : bool, default True
            If True, NaN values will be removed before plotting.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.

        Returns
        -------
        fig : matplotlib.figure.Figure
            Created figure if `ax` is not passed.
        ax : matplotlib.axes.Axes
            Created axis if `ax` is not passed.

        Other Parameters
        ----------------
        kwargs : dict, optional
            Other keyword arguments, see **[matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)**.
        
        See Also
        --------
        CitrosDB.plot_graph, CitrosDB.multiple_y_plot, CitrosDB.multiplot, CitrosDB.plot_sigma_ellipse

        Examples
        --------
        Import matplotlib and mplot3d for 3D plots and create figure to plot on:

        >>> import matplotlib.pyplot as plt
        >>> from mpl_toolkits import mplot3d
        >>> fig = plt.figure(figsize=(6, 6))
        >>> ax = fig.add_subplot(111, projection = '3d')

        For topic 'A' from batch 'testing' from json-data column download 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' columns:

        >>> citros = da.CitrosDB()
        >>> df = citros.batch('testing').topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3'])

        Make 3D plot with dashed lines; `scale` = True aligns all axes to have the same range:

        >>> citros.plot_3dgraph(df, 'data.x.x_1', 'data.x.x_2', 'data.x.x_3', '--', ax = ax, scale = True)

        ![plot_3dgraph_1](../../img_documentation/plot_3dgraph_1.png "plot_3dgraph_1")
        '''
        plotter = _Plotter()
        return plotter.plot_3dgraph(df, x_label, y_label, z_label, ax, scale, legend, title, 
                                    set_x_label, set_y_label, set_z_label, remove_nan, inf_vals, *args, **kwargs)
        
    def multiple_y_plot(self, df: pd.DataFrame, x_label: str, y_labels: str, *args, fig: Optional[matplotlib.figure.Figure] = None, 
                        legend: bool = True, title: Optional[str] = None, set_x_label: Optional[str] = None, 
                        set_y_label: Optional[str] = None, remove_nan: bool = True, inf_vals: Optional[float] = 1e308, **kwargs):
        '''
        Plot a series of vertically arranged graphs 'y vs. `x_label`', with the y-axis labels 
        specified in the `y_labels` parameter.

        Different colors correspond to different sids.

        Parameters
        ----------
        df : pandas.DataFrame
            Data table.
        x_label : str
            Label of the column to plot along x-axis.
        y_labels : list of str
            Labels of the columns to plot along y-axis.
        *args : Any
            Additional arguments to style lines, set color, etc, 
            see **[matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)**.
        fig : matplotlib.figure.Figure, optional
            If None, a new Figure will be created.
        legend : bool, default True
            If True, show the legend with sids.
        title : str
            Set title of the plot.
        set_x_label : str, default None
            Label to set to the x-axis. If None, label is set according to `x_label`.
        set_y_label : list of str, default None
            Labels to set to the y-axis. If None, label is set according to `y_labels`.
        remove_nan : bool, default True
            If True, NaN values will be removed before plotting.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.

        Returns
        -------
        fig : matplotlib.figure.Figure
            Created figure if `fig` is not passed.
        ax : numpy.ndarray of matplotlib.axes.Axes
            Created axis if `fig` is not passed.

        Other Parameters
        ----------------
        kwargs : dict, optional
            Other keyword arguments, see **[matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)**.

        See Also
        --------
        CitrosDB.plot_graph, CitrosDB.plot_3dgraph, CitrosDB.multiplot, CitrosDB.plot_sigma_ellipse

        Examples
        --------
        For topic 'A' from batch 'testing' from json-data column download 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' and 'data.time' columns:

        >>> citros = da.CitrosDB()
        >>> df = citros.batch('testing').topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3', 'data.time'])

        Plot three subplots with a common x axis: 'data.x.x_1' vs. 'data.time', 'data.x.x_2' vs. 'data.time' and 'data.x.x_3' vs. 'data.time':

        >>> fig, ax = citros.multiple_y_plot(df, 'data.time', ['data.x.x_1', 'data.x.x_2', 'data.x.x_3'])

        ![multiple_y_plot_1](../../img_documentation/multiple_y_plot_1.png "multiple_y_plot_1")

        If `ax` parameter is not passed, `multiple_y_plot()` generates a pair of (matplotlib.figure.Figure, matplotlib.axes.Axes) objects and
        returns them. Let's make a scatter plot in this manner:

        >>> fig, ax = citros.multiple_y_plot(df, 'data.time', ['data.x.x_1', 'data.x.x_2', 'data.x.x_3'], '.')

        ![multiple_y_plot_2](../../img_documentation/multiple_y_plot_2.png "multiple_y_plot_2")
        '''
        plotter = _Plotter()
        return plotter.multiple_y_plot(df, x_label, y_labels,  fig, legend, title, set_x_label, set_y_label, remove_nan, inf_vals, *args, **kwargs)
        
    
    def multiplot(self, df: pd.DataFrame, labels: list, *args, scale: bool = True, fig: Optional[matplotlib.figure.Figure] = None, 
                  legend: bool = True, title: Optional[str] = None, set_x_label: Optional[str] = None, set_y_label: Optional[str] = None, 
                  remove_nan: bool = True, inf_vals: Optional[float] = 1e308, label_all_xaxis: bool = False, 
                  label_all_yaxis: bool = False, num: int = 5, **kwargs):
        '''
        Plot a matrix of N x N graphs, each displaying either the histogram with values distribution (for graphs on the diogonal) or
        the relationship between variables listed in `labels`, with N being the length of `labels` list.

        For non-diagonal graphs, colors are assigned to points according to sids.

        Parameters
        ----------
        df : pandas.DataFrame
            Data table.
        labels : list of str
            Labels of the columns to plot.
        *args : Any
            Additional arguments to style lines, set color, etc, 
            see **[matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)**.
        scale : bool, default True
            Specify whether the axis range should be the same for x and y axes.
        fig : matplotlib.figure.Figure, optional
            If None, a new Figure will be created.
        legend : bool, default True
            If True, show the legend with sids.
        title : str
            Set title of the plot.
        set_x_label : list of str
            Labels to set to the x-axis. If None, label is set according to `labels`.
        set_y_label : list of str
            Labels to set to the y-axis. If None, label is set according to `labels`.
        remove_nan : bool, default True
            If True, NaN values will be removed before plotting.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.
        label_all_xaxis : bool, default False
            If True, x labels are set to the x-axes of the all graphs, otherwise only to the graphs in the bottom row.
        label_all_yaxis : bool, default False
            If True, y labels are set to the y-axes of the all graphs, otherwise only to the graphs in the first column.
        num : int, default 5
            Number of bins in the histogram on the diagonal.
            
        Returns
        -------
        fig : matplotlib.figure.Figure
            Created figure if `fig` is not passed.
        ax : numpy.ndarray of matplotlib.axes.Axes
            Created axis if `fig` is not passed.

        Other Parameters
        ----------------
        kwargs : dict, optional
            Other keyword arguments, see **[matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)**.

        See Also
        --------
        CitrosDB.plot_graph, CitrosDB.plot_3dgraph, CitrosDB.multiple_y_plot, CitrosDB.plot_sigma_ellipse

        Examples
        --------
        For topic 'A' from the batch 'testing_robotics' from json-data column download 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3':

        >>> citros = da.CitrosDB()
        >>> df = citros.batch('testing_robotics').topic('A').data(['data.x.x_1', 'data.x.x_2', 'data.x.x_3'])

        Plot nine graphs: histograms for three graphs on the diagonal, that represent 
        distribution of the 'data.x.x_1', 'data.x.x_2' and 'data.x.x_3' values, and six graphs that show 
        correlation between them; plot by dots and scale x and y axes ranges to one interval for each graph:

        >>> fig, ax = citros.multiplot(df, ['data.x.x_1', 'data.x.x_2', 'data.x.x_3'], '.' , scale = True)
        >>> fig.show()

        ![multiplot](../../img_documentation/multiplot.png "multiplot")
        '''
        plotter = _Plotter()
        return plotter.multiplot(df, labels, scale, fig, legend, title, set_x_label, set_y_label, remove_nan, inf_vals, label_all_xaxis, 
                  label_all_yaxis, num, *args, **kwargs)
        
    def plot_sigma_ellipse(self, df: pd.DataFrame, x_label: str, y_label: str, ax: plt.Axes = None, n_std: int = 3, 
                           plot_origin: bool = True, bounding_error: bool = False, inf_vals: Optional[float] = 1e308, 
                           legend: bool = True, title: Optional[str] = None, set_x_label: Optional[str] = None, 
                           set_y_label: Optional[str] = None, scale: bool = False, return_ellipse_param: bool = False):
        '''
        Plot sigma ellipses for the set of data.

        Parameters
        ----------
        df : pandas.DataFrame
            Data table.
        x_label : str
            Label of the column to plot along x-axis.
        y_labels : list of str
            Labels of the columns to plot along y-axis.
        ax : matplotlib.axes.Axes
            Figure axis to plot on. If not specified, the new pair of fig, ax will be created and returned.
        n_std : int or list of ints
            Radius of ellipses in sigmas.
        plot_origin: bool, default True
            If True, depicts origin (0, 0) with black cross.
        bounding_error : bool, default False
            If True, plots bounding error circle for each of the ellipses.
        inf_vals : None or float, default 1e308
            If specified, all values that exceed the provided value in absolute terms will be removed before plotting.
            If this functionality is not required, set inf_vals = None.
        legend : bool, default True
            If True, show the legend.
        title : str, optional
            Set title. If None, title is set as '`x_label` vs. `y_label`'.
        set_x_label : str, optional
            Set label of the x-axis. If None, label is set according to `x_label`.
        set_y_label : str, optional
            Set label of the y-axis. If None, label is set according to `y_label`.
        scale : bool, default False
            Specify whether the axis range should be the same for x and y axes.
        return_ellipse_param : bool, default False
            If True, returns ellipse parameters.

        Returns
        -------
        fig : matplotlib.figure.Figure
            Created figure if `ax` is not passed.
        ax : numpy.ndarray of matplotlib.axes.Axes
            Created axis if `ax` is not passed.
        ellipse_param : dict or list of dict
            Ellipse parameters if `return_ellipse_param` set True.
            Parameters of the ellipse:
            - x : float - x coordinate of the center.
            - y : float - y coordinate of the center.
            - width : float - total ellipse width (diameter along the longer axis).
            - height : float - total ellipse height (diameter along the shorter axis).
            - alpha : float - angle of rotation, in degrees, anti-clockwise from the shorter axis.

            If bounding_error set True:
            - bounding_error : float - radius of the error circle.

        See Also
        --------
        CitrosDB.plot_graph, CitrosDB.plot_3dgraph, CitrosDB.multiple_y_plot, CitrosDB.multiplot

        Examples
        --------
        Let's assume that in topic 'A', the batch named 'aerostatic' includes the columns 'data.x.x_1' and 'data.x.x_2'.
        We would like to analyze the spread of these values from their mean.
        First, we'll query the data and compute new columns 'X1' and 'X2', which will represent the deviations of 'data.x.x_1' and 'data.x.x_2' from their respective mean values:

        >>> citros = da.CitrosDB()
        >>> df = citros.batch('aerostatic').topic('A').data(['data.x.x_1', 'data.x.x_2'])
        >>> df['X1'] = df['data.x.x_1'] - df['data.x.x_1'].mean()
        >>> df['X2'] = df['data.x.x_2'] - df['data.x.x_2'].mean()

        Let's plot 'X1' vs. 'X2', 3-$\sigma$ ellipse, origin point that has coordinates (0, 0) 
        and set the same range for x and y axis:

        >>> fig, ax = citros.plot_sigma_ellipse(df, x_label = 'X1', y_label = 'X2',
        ...                                      n_std = 3, plot_origin=True, scale = True)

        ![plot_sigma_ellipse_1](../../img_documentation/plot_sigma_ellipse_1.png "plot_sigma_ellipse_1")

        If we set `return_ellipse_param` = `True`, the parameters of the error ellipse will be returned:
        >>> fig, ax, param = citros.plot_sigma_ellipse(df, x_label = 'X1', y_label = 'X2', n_std = 3, 
        ...                                            plot_origin=True, scale = True, return_ellipse_param = True)
        >>> print(param)
        {'x': 0,
         'y': 0,
         'width': 2.1688175559868204,
         'height': 0.6108213775972502,
         'alpha': -132.38622331887413}

        Plot the same but for 1-, 2- and 3-$\sigma$ ellipses, add bounding error circle (that indicates the maximum distance
        between the ellipse points and the origin), set custom labels and title to the plot:

        >>> fig, ax = citros.plot_sigma_ellipse(df, x_label = 'X1', y_label = 'X2', 
        ...                                     n_std = [1,2,3], plot_origin=True, bounding_error=True, 
        ...                                     set_x_label='x, [m]', set_y_label = 'y, [m]', 
        ...                                     title = 'Coordinates')

        ![plot_sigma_ellipse_2](../../img_documentation/plot_sigma_ellipse_2.png "plot_sigma_ellipse_2")
        '''
        plotter = _Plotter()
        return plotter.plot_sigma_ellipse(df, x_label, y_label, ax, n_std, plot_origin, bounding_error, inf_vals, 
                           legend, title, set_x_label, set_y_label, scale, return_ellipse_param)