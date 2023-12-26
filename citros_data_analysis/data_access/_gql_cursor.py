from ._gql_base import _GqlBase
from .citros_dict import CitrosDict
from datetime import datetime, timezone, timedelta
import os
from typing import Union, Optional, Any
import re
import json
from urllib.parse import quote

class _GqlCursor(_GqlBase):
    '''
    Communication with graph ql database
    '''

    def __init__(self, repo = None, simulation = None, debug = False):
        super().__init__()
        self._gql_debug = debug
        if repo is None:
            repo = os.getenv("CITROS_REPO")
            if repo is None:
                try:
                    path = str(self._find_citros_in_ancestors()/'project.json')
                    with open(path) as f:
                       repo = json.load(f)['name']
                except:
                    repo = None
        self._set_repo(repo, exact_match = True)

        if simulation is None:
            self._simulation = os.getenv("CITROS_SIMULATION")
        else:
            self._set_simulation(simulation)


    def _get_current_user_info(self):
        '''
        Query current user id and organization by token.

        Returns
        -------
        str
            user id
        '''
        query = """query MyQuery {
                      currentUser{
                        id
                        organization {
                          slug
                        }
                      }
                    }
                """
        res = self._gql_execute(query)
        if res is not None and len(res['currentUser']) != 0:
            user_id = res['currentUser'].get('id')
            if res['currentUser'].get('organization'):
                user_organization = res['currentUser']['organization'].get('slug')
            else:
                user_organization = None
        else:
            user_id = None
            user_organization = None
        return user_id, user_organization
        
    # def _get_current_database(self):
        
    #     '''
    #     Query users's database name.

    #     Returns
    #     -------
    #     str
    #         database name
    #     '''
    #     query = """query MyQuery {
    #                   currentUser {
    #                     organization {
    #                       name
    #                     }
    #                   }
    #                 }
    #             """
    #     res = self._gql_execute(query)
    #     if res is not None and len(res['currentUser']) != 0:
    #         try:
    #             return res['currentUser']['organization']['name']
    #         except:
    #             return None

    def _get_user_by_email(self, search_email):
        '''
        Get user id.

        Parameters
        ----------
        search_email : str
            Return user id that corresponds to the provided email or None if search was not succeed.

        Returns
        -------
        str
            user id
        '''
        declaration = '($search_email: Emailtype!)'
        usersList_arg = '(condition: {email: $search_email})'
        variable_values= {'search_email': search_email}
        query = """query MyQuery""" + declaration + """ {
                        usersList""" + usersList_arg +""" {
                          id
                        }
                    }
                """
        res = self._gql_execute(query, variable_values = variable_values)
        if res is not None and len(res['usersList']) != 0:
            return res['usersList'][0]['id']
        else:
            return None

    def _search_user(self, search = None, search_by = None, order_by = None, show_all = True):
        '''
        Retrieve users' information, including their first and last names, emails and a list of repositories created by these users.

        By default, shows information about all users of the organization.

        Parameters
        ----------
        search : str, optional
           - Provide email to display information about the exact user.
           - To search by the name, provide user's name and set `search_by` = 'name'
           - To search by the last name, provide user's last name and set `search_by` = 'last_name'

        search : str, optional
           - By default, if the `search` is provided, performs search by email.
           - To search by the name, set `search_by` = 'name'.
           - To search by the last name, set `search_by` = 'last_name'.

        order_by : str or list or dict
            To obtain the output in ascending order, provide one or more of the following options as either a single str or a as a list:
           - 'name'
           - 'last_name' 
           - 'email'<br />           
            To specify whether to use descending or ascending order, create a dictionary where the keys correspond to the options mentioned above, 
            and the values are either 'asc' for ascending or 'desc' for descending. For instance: {'name': 'asc', 'last_name': 'desc'}"

        show_all : bool, default True
            If `True`, shows all users without filtering according to set repositories and batches.
        '''
        order_by_all = {'name': 'FIRST_NAME', 'last_name': 'LAST_NAME', 'email': 'EMAIL'}
        declaration_list = []
        variable_values = {}

        #by default search by email
        if search is not None:
            if search_by is None:
                search_by = 'email'

        #main search
        if search_by == 'email':
            if not isinstance(search, str):
                print("search_user(): `search` must be a str to search by 'email'")
                return CitrosDict({})
            declaration_list.append('$search_email: Emailtype!')
            usersList_arg_dict = {'condition': {'email': '$search_email'}}
            variable_values['search_email'] = search
            mode = 'email'
        elif search_by == 'name':
            if not isinstance(search, str):
                print("search_user(): `search` must be a str to search by 'name'")
                return CitrosDict({})
            declaration_list.append('$search_name: String!')
            usersList_arg_dict = {'condition': {'firstName': '$search_name'}}
            variable_values['search_name'] = search
            mode = 'name'
        elif search_by == 'last_name':
            if not isinstance(search, str):
                print("search_user(): `search` must be a str to search by 'last_name'")
                return CitrosDict({})
            declaration_list.append('$search_last_name: String!')
            usersList_arg_dict = {'condition': {'lastName': '$search_last_name'}}
            variable_values['search_last_name'] = search
            mode = 'last_name'
        else:
            usersList_arg_dict = {}

        #order of the output, by now there is no 'orderBy' keyword in usersList_arg_dict
        if order_by is not None:
            order_by_arg = self._gql_order_dict(order_by, order_by_all)
            if order_by_arg != '':
                usersList_arg_dict['orderBy'] = order_by_arg        

        #if batch() is set: show user who created the batch, also need to know if this user created the repo too
        if (not show_all) and (self._batch_id is not None):
            declaration_list.append('$batch_id: UUID!')
            batchRunsList_arg = """
                            batchRunsList(condition: {id: $batch_id}) {
                              repo {
                                id
                                name
                              }
                            }
                    """
            variable_values['batch_id'] = self._batch_id
            reposList_arg = """
                            reposList {
                              id
                              name
                            }
                    """
            
        #elif repo() is set, show who created it and who created batches inside this repo
        elif (not show_all) and (self._repo_id is not None):
            declaration_list.append('$repo_id: UUID!')
            reposList_arg = """
                            reposList(condition: {id: $repo_id}) {
                              name
                            }
                    """
            variable_values['repo_id'] = self._repo_id
            batchRunsList_arg = """
                            batchRunsList(condition: {repoId: $repo_id}) {
                                repo {
                                  name
                                }
                            }
                    """

        #neither batch nor repo is set or show_all = True
        #show user and all repos which he created or in which he created batches
        else:
            batchRunsList_arg = """
                            batchRunsList {
                              repo {
                                name
                              }
                            }
                    """
            reposList_arg = """
                            reposList {
                              name
                            }
                    """

        if len(variable_values) == 0:
            variable_values = None
        if len(declaration_list) !=0 :
            declaration = '('+','.join(declaration_list)+')'
        else:
            declaration = ""
        if len(usersList_arg_dict) != 0:
            usersList_arg = '('+str(usersList_arg_dict).replace("'", '')[1:-1]+')'
        else:
            usersList_arg = ''
        
        query = """
                query MyQuery"""+declaration+""" {
                        usersList"""+usersList_arg+""" {
                        firstName
                        lastName
                        email
                        """+reposList_arg+"""
                        """+batchRunsList_arg+"""
                        }
                    }
                """
                    
        res = self._gql_execute(query, variable_values = variable_values)
        if res is None:
            return CitrosDict({})
        
        result = {}
        
        #if _batch_id is set, we would like to display only user, who created this batch and also check if he created the repo of this batch too
        if (not show_all) and (self._batch_id is not None):
            for item in res["usersList"]:
                if len(item['batchRunsList']) > 0:
                    repo_list_batch_cr = [item['batchRunsList'][0]['repo']['name']]
                    repo_list_cr = []
                    if len(item['reposList']) > 0:
                        for repo_item in item['reposList']:
                            if repo_item['id'] == self._repo_id:
                                repo_list_cr.append(repo_item['name'])
                                break
                    repo_list_cr.sort()
                    repo_list_batch_cr.sort()
                    inf_dict = CitrosDict({'name': item['firstName'], 'last_name': item['lastName'], 
                                        'create_repo': repo_list_cr, 'create_batch_in_repo': repo_list_batch_cr})
                    result[item['email']] = inf_dict
                    break
        
        #if _repo_id is set, we would like to display only users who created this repo or who created batches in this repo
        elif (not show_all) and (self._repo_id is not None):
            for item in res["usersList"]:
                repo_list_cr = []
                repo_list_batch_cr = []
                if len(item['reposList']) > 0:
                    repo_list_cr = [item['reposList'][0]['name']]

                if len(item['batchRunsList']) > 0:
                    for batch_item in item['batchRunsList']:
                        repo_list_batch_cr.append(batch_item['repo']['name'])
                    repo_list_batch_cr = list(set(repo_list_batch_cr))
                if len(repo_list_cr) > 0 or len(repo_list_batch_cr) > 0:
                    repo_list_cr.sort()
                    repo_list_batch_cr.sort()
                    inf_dict = CitrosDict({'name': item['firstName'], 'last_name': item['lastName'], 
                                        'create_repo': repo_list_cr, 'create_batch_in_repo': repo_list_batch_cr})
                    result[item['email']] = inf_dict
    
        # show all users even if they did not created repositories or batches
        # in create_repo - repositories that the user created and 
        # in create_batch_in_repo - repositories where user created batches
        else:
            for item in res["usersList"]:
                repo_list_cr = []
                repo_list_batch_cr = []
                if len(item['reposList']) > 0:
                    for repo_item in item['reposList']:
                        repo_list_cr.append(repo_item['name'])
                if len(item['batchRunsList']) > 0:
                    for batch_item in item['batchRunsList']:
                        repo_list_batch_cr.append(batch_item['repo']['name'])
                    repo_list_batch_cr = list(set(repo_list_batch_cr))
                repo_list_cr.sort()
                repo_list_batch_cr.sort()
                inf_dict = CitrosDict({'name': item['firstName'], 'last_name': item['lastName'], 
                                    'create_repo': repo_list_cr, 'create_batch_in_repo': repo_list_batch_cr})
                result[item['email']] = inf_dict

        result = CitrosDict(result)
        return result   

    def _is_uuid(self, string):
        '''
        Check if the string matches a pattern for a uuid format.

        Parameters
        ----------
        string: str
            String to check whether it matchs the uuid pattern.
        '''
        pattern = re.compile("^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$")
        return bool(pattern.match(string))
    
    def _resolve_search(self, search, exact_match = False):
        '''
        Prepare graph ql commands depending on the main format of the search. 
        '''
        variable_values = {}
        batchRunsList_arg = {}
        if search is None:
            mode = 'all'
            declaration = ''
            # batchRunsList_arg = ''
            batchRunsList_arg = {}
        elif isinstance(search, int):
            mode = 'number'
            declaration = "$offset: Int!"
            order = 'DESC' if search < 0 else 'ASC'
            # batchRunsList_arg = 'first: 1, orderBy: CREATED_AT_'+order+', offset: $offset'
            batchRunsList_arg = {'first': '1', 'orderBy': 'CREATED_AT_'+order, 'offset': '$offset'}
            variable_values["offset"] = abs(search)-1 if search < 0 else search
        elif isinstance(search, str):
            if self._is_uuid(search):
                declaration = "$search_id: UUID!"
                # batchRunsList_arg = 'condition: {id: $search_id}'
                batchRunsList_arg = {'condition': {'id': '$search_id'}}
                variable_values["search_id"] = search
                mode = 'id'
            else:
                #if the argument is a name or a part of the name, find the corresponding batch id
                declaration = "$search_name: String!"
                if exact_match:
                    # batchRunsList_arg = 'condition: {name: $search_name}'
                    batchRunsList_arg = {'condition': {'name': '$search_name'}}
                else:    
                    # batchRunsList_arg = 'filter: {name: {includes: $search_name}}'
                    batchRunsList_arg = {'filter': {'name': {'includes': '$search_name'}}}
                variable_values['search_name'] = search
                mode = 'name'
        else:
            mode = 'unknown'
            declaration = None
            batchRunsList_arg = None
            variable_values = None

        return declaration, batchRunsList_arg, variable_values, mode

    def _check_batch_format(self, search):
        '''
        Check if the provided variable matches the format suitable for performing the batch search.

        Parameters
        ----------
        search : str or int
            Must be part of the batch name or the exact batch id or int value 
            (0 - the first that was created, -1 - the last created) or None.
        '''
        if search is not None:
            if isinstance(search, (int, str)):
                return True
            else:
                if search is None:
                    return True
                else:
                    return False

    def _is_batch_exist(self, search):
        '''
        Check in graph ql table if the batch exists.

        Parameters
        ----------
        search : str or int
            Must be part of the batch name or the exact batch id or int value 
            (0 - the first that was created, -1 - the last created) or None.
        
        Returns
        -------
        result : bool
            False if the result of the search is blank. Otherwise, True.
        note : 
            Number of id records that match the search. It may be > 1 for search by name: 
            either the name was not unique or it was multiple partition matching.
        '''
        if self._check_batch_format(search):
            declaration, batchRunsList_arg, variable_values, mode = self._resolve_search(search, exact_match = False)
        else:
            return False
        # if mode == 'unknown':
        if declaration != '':
            declaration = '('+declaration+')'
        batchRunsList_arg = '('+str(batchRunsList_arg).replace("'", '')[1:-1]+')'
        query = """
                query MyQuery"""+declaration+""" {
                  batchRunsList"""+batchRunsList_arg+""" {
                    id
                  }
                }
                """
        res = self._gql_execute(query, variable_values = variable_values)
        if res is not None:
            if len(res['batchRunsList']) == 0:
                return False
            else:
                return True
        else:
            return False

    def _get_batch_list(self, search = None, exact_match = False, user_id = None):
        '''
        Make a query to graph ql and return the list of batch ids.
        '''
        if not self._check_batch_format(search):
            print("could not understand the format of the queried batch. "
                  "Set batch either as int value (0 - the batch that was created first, -1 - the last created batch) "
                "or as str to search by batch's name or id")
            return None, None
        declaration_list = []
        # batchRunsList_list = []

        declaration_search, batchRunsList_dict, variable_values, mode = self._resolve_search(search, exact_match = exact_match)
        if mode == 'unknown':
            print("could not understand the format of the queried batch. "
                  "Set batch either as int value (0 - the batch that was created first, -1 - the last created batch) "
                "or as str to search by batch's name or id")
            return None, None
        if mode != 'all':
            declaration_list.append(declaration_search)
            # batchRunsList_list.append(batchRunsList_arg_search)
        
        if self._repo_id is not None:
            declaration_list.append('$repo_id: UUID!')
            # batchRunsList_list.append('condition: {repoId: $repo_id}')
            self._update_dict(batchRunsList_dict, {'condition': {'repoId': '$repo_id'}})
            variable_values['repo_id'] = self._repo_id

        if self._simulation is not None:
            declaration_list.append('$simulation: String!')
            self._update_dict(batchRunsList_dict, {'condition': {'simulation': '$simulation'}})
            variable_values['simulation'] = self._simulation

        if user_id is not None:
            declaration_list.append('$user_id: UUID!')
            # batchRunsList_list.append('condition: {userId: $user_id}')
            self._update_dict(batchRunsList_dict, {'condition': {'userId': '$user_id'}})
            variable_values['user_id'] = user_id

        if len(declaration_list) != 0:
            declaration = '('+','.join(declaration_list)+')'
        else:
            declaration = ''
        if len(batchRunsList_dict) != 0:
            batchRunsList_arg = '(' + str(batchRunsList_dict).replace("'", '')[1:-1] +')'
            # batchRunsList_arg = '('+','.join(batchRunsList_list)+')'
        else:
            batchRunsList_arg = ''

        query = """
                query MyQuery"""+declaration+""" {
                   batchRunsList"""+batchRunsList_arg+""" {
                     id
                     name
                   }
                }
                """
        res = self._gql_execute(query, variable_values = variable_values)
        if res is not None:
            return res['batchRunsList'], mode
        else:
            return None, None
    
    def _set_batch(self, search, exact_match = False, user_id = None):
        '''
        Set the batch
        '''
        if hasattr(self, '_test_mode'):
            self._batch_id = search
            self._batch_name = None
            return
        
        if (search is None) or search == 'None':
            self._batch_id = None
            self._batch_name = None
            return

        #check the format
        if not self._check_batch_format(search):
            print("could not understand the format of the queried batch. "
                  "Set batch either as int value (0 - the batch that was created first, -1 - the last created batch) "
                "or as str to search by batch's name or id")
            self._batch_id = None
            self._batch_name = None
            return
        
        #get the batch id and names that match `search`
        res, mode = self._get_batch_list(search = search, exact_match = exact_match, user_id = user_id)
        if res is None:
            self._batch_id = None
            self._batch_name = None
            return

        #check if the match is unique
        if len(res) == 0:
            #no matches
            if_repo = ('in the repository "' + self._repo_name + '" ') if self._repo_name is not None else ''
            if_simulation = (' created in simulation "' + self._simulation + '"') if self._simulation is not None else ''
            if mode == 'number':
                print(f'batch is not set: '+if_repo+f'there is no batch under the number {search}'+if_simulation+f',\ntry `search_batch()` method')
            elif mode == 'id':
                print(f'batch is not set: '+if_repo+f'there is no batch with id = "{search}"'+if_simulation+f',\ntry `search_batch()` method')
            elif mode == 'name':
                if exact_match:
                    print(f'batch is not set: '+if_repo+f'there is no batch with name = "{search}"'+if_simulation+f',\ntry `search_batch()` method')
                else:
                    print(f'batch is not set: '+if_repo+f'there is no batch with "{search}" in name'+if_simulation+f',\ntry `search_batch()` method')
            elif mode == 'all':
                (f'there is no batches '+if_repo+f'in the database')
            self._batch_id = None
            self._batch_name = None
            return
        elif len(res) > 1:
            #match is ambiguous
            if mode == 'name':
                res_list = []
                for item in res:
                    res_list.append(item['name'])
                if not exact_match:
                    print(f'batch is not set: there is more than one batch with "{search}" in the name,\nprovide one of the following options to `batch()` method with `exact_match` = True:')
                    print(res_list)
                    print("or try `search_batch()` method'")
                else:
                    print(f'batch is not set: there is more than one batch with "{search}" in the name')
                    print("try `search_batch()` method or specify repository by `repo()` or simulation by `simulation()`'")
            elif mode == 'all':
                print('the number of batches in database is more then one, please specify or try `search_batch()` method')
            self._batch_id = None
            self._batch_name = None
            return
        elif len(res) == 1:
            #batch is unique
            self._batch_id = res[0]['id']
            self._batch_name = res[0]['name']
    
    def _set_repo(self, search = None, exact_match = False):
        '''
        Set the repo_id and repo_name
        '''
        if (search is None) or (search == 'None'):
            self._repo_name = None
            self._repo_id = None
            return
        if not isinstance(search, (str, int)):
            print("repository must be defined either as str (name or part of the name or repository id)"+\
                  "or int value (0 - the repository that was created first, -1 - the last created repo)")
            return CitrosDict({})
        
        declaration, reposList_arg, variable_values, mode = self._resolve_search(search, exact_match = exact_match)
        declaration = '(' + declaration + ')'
        reposList_arg = '(' + str(reposList_arg).replace("'", '')[1:-1] + ')'

        query = """query MyQuery"""+declaration+""" {
                  reposList"""+reposList_arg+""" {
                    id
                    name
                  }
                }
                """
        res = self._gql_execute(query, variable_values = variable_values)['reposList']
        if res is None:
            self._repo_id = None
            self._repo_name = None
            return
        
        #check if the match is unique
        if len(res) == 0:
            #no matches
            if mode == 'number':
                print(f'repository is not set: there is no repository under the number {search}, try `repo_info()` method')
            elif mode == 'id':
                print(f'repository is not set: there is no repository with id = "{search}", try `repo_info()` method')
            elif mode == 'name':
                if exact_match:
                    print(f'repository is not set: there is no repository with name = "{search}", try `repo_info()` method')
                else:
                    print(f'repository is not set: there is no repository with "{search}" in name, try `repo_info()` method')
            elif mode == 'all':
                ('there is no repos in the database')
            return None
        elif len(res) > 1:
            #match is ambiguous
            if mode == 'name':
                res_list = []
                for item in res:
                    res_list.append(item['name'])
                if not exact_match:
                    print(f'repository is not set: there is more than one repositories with "{search}" in the name,\nprovide one of the following options to `repo()` method with `exact_match` = True:')
                    print(res_list)
                    print("or try `repo_info()` method'")
                else:
                    print(f'repository is not set: there is more than one repository with "{search}" in the name:')
                    print(res_list)
                    print("try `repo_info()` method'")
            elif mode == 'all':
                print('the number of repos in database is more then one, please specify or try `repo_info()` method')
            return None
        elif len(res) == 1:
            #repo is unique
            self._repo_id = res[0]['id']
            self._repo_name = res[0]['name']

    def _set_simulation(self, simulation):
        '''
        Set simulation name.

        Parameters
        ----------
        simulation : str
            Name of the simulation.
        '''
        if simulation is None:
            self._simulation = None
        elif isinstance(simulation, str):
            self._simulation = simulation
        else:
            self._simulation = None
            print("simulation is not set, 'simulation' must be a str")

    def _parse_date(self, date_str):
        '''
        Parse date time and return the result as dictionary.

        Parameters
        ----------
        date_str : str
            Date time in the format 'dd-mm-yyyy hh:mm:ss +HH:MM', 
            where +HH:MM or -HH:MM is a timezone. 
        
        Returns
        -------
        str
            Dictionary with collected date-time information. Try to find patterns 'dd-mm-yyyy', 
            'hh:mm:ss' and '+HH:MM' separately.
        '''
        pattern_date = '^(?P<day>\d{1,2})(?!\d)(?!:)(-(?P<month>\d{1,2})(?!\d)(-(?P<year>\d{2,4})(?!\d))?)?'
        pattern_time = '(?<!-)(?<!:)(?<!\d)(?<!\+)(?P<hour>\d{1,2})(?!\d)(?!-)(:(?P<minute>\d{1,2})(?!\d)(:(?P<second>\d{1,2})(?!\d))?)?'
        pattern_timezone = '(?P<tz_sign>[+,-])(?P<tz_h>\d{1,2}):(?P<tz_m>\d{1,2})?(?!\d)'
        current_datetime = datetime.now().astimezone(tz=timezone.utc)
        date_default = {
            'year': current_datetime.year,
            'month': current_datetime.month,
            'day': current_datetime.day,
            'hour': 0,
            'minute': 0,
            'second': 0,
            'tz_sign': '+', 
            'tz_h': 0, 
            'tz_m': 0
        }
        
        date = {}
        if len(date_str) == 1 or len(date_str) == 2:
            try:
                date['day'] = int(date_str)
                print(date['day'])
            except:
                pass
        else:
            for match in re.finditer(pattern_date, date_str):
                date['year'] = int(match['year']) if match['year'] is not None else date_default['year']
                date['month'] = int(match['month']) if match['month'] is not None else date_default['month']
                date['day'] = int(match['day']) if match['day'] is not None else date_default['day']
            if 'year' in date.keys():
                if date['year'] < 2000:
                    date['year'] = int(date['year'] + 2000)
            for match in re.finditer(pattern_time, date_str):
                date['hour'] = int(match['hour']) if match['hour'] is not None else date_default['hour']
                date['minute'] = int(match['minute']) if match['minute'] is not None else date_default['minute']
                date['second'] = int(match['second']) if match['second'] is not None else date_default['second']
            for match in re.finditer(pattern_timezone, date_str):
                date['tz_sign'] = match['tz_sign'] if match['tz_sign'] is not None else date_default['tz_sign']
                date['tz_h'] = int(match['tz_h']) if match['tz_h'] is not None else date_default['tz_h']
                date['tz_m'] = int(match['tz_m']) if match['tz_m'] is not None else date_default['tz_m']
        date = {**date_default, **date}
        return date
    
    def _search_repo(self, search: Optional[Union[int, str]] = None, search_by: str = None, order_by: str = None,
                  exact_match: bool = False, user_id: Optional[str] = None) -> CitrosDict:
        '''
        Return information about repositories.
        '''
        if not isinstance(search, (str, int)) and search is not None:
            print("search_repo(): set `search` as str to search by repo's name or id or " + \
                      "as int value (0 - the repository that was created first, -1 - the last created repo)")
            return CitrosDict({})
        
        order_by_all = {'name': 'NAME', 'id': 'ID', 'description': 'DESCRIPTION', 'git': 'GIT', 
                        'created_at': 'CREATED_AT', 'updated_at': 'UPDATED_AT'}

        declaration_list = []
        # reposList_list = []
        variable_values = {}

        if search_by is None:
            declaration_search, reposList_dict, variable_values_search, mode = self._resolve_search(search, exact_match = exact_match)
            if mode == 'unknown':
                print("search_repo(): set `search` as str to search by repository's name or id or " + \
                      "as int value (0 - the repository that was created first, -1 - the most recently created repo)")
                return CitrosDict({})            
            if mode != 'all':
                declaration_list.append(declaration_search)
                # reposList_list.append(reposList_arg_search)
            variable_values = {**variable_values, **variable_values_search}
        elif search_by == 'name':
            if not isinstance(search, str):
                print("`search` must be a str to search by 'name'")
                return CitrosDict({})
            else:
                declaration_list.append('$search_name: String!')
                if exact_match:
                    # reposList_list.append('condition: {name: $search_name}')
                    reposList_dict = {'condition': {'name': '$search_name'}}
                else:
                    # reposList_list.append('filter: {name: {includes: $search_name}}')
                    reposList_dict = {'filter': {'name': {'includes': '$search_name'}}}
                variable_values['search_name'] = search
                mode = 'name'
        elif search_by in ['repo_id', 'id']:
            if not isinstance(search, str):
                print("`search` must be a str to search by 'id'")
                return CitrosDict({})
            elif not self._is_uuid(search):
                print("`search` must have uuid format to search by 'id'")
                return CitrosDict({})
            else:
                declaration_list.append('$search_id: UUID!')
                # reposList_list.append('condition: {id: $search_id}')
                reposList_dict = {'condition': {'id': '$search_id'}}
                variable_values['search_id'] = search
                mode = 'id'
        elif search_by in ['created_after', 'created_before', 'updated_after', 'updated_before']:
            if not isinstance(search, str):
                print("`search` must be a str to search by date fields")
                return CitrosDict({})
            search_date = self._parse_date(search)
            offset = timezone(int(search_date['tz_sign']+'1')*timedelta(hours=search_date['tz_h'], minutes=search_date['tz_m']))
            search_date_str = datetime(year = search_date['year'], month = search_date['month'], day = search_date['day'], 
                     hour = search_date['hour'], minute = search_date['minute'], second = search_date['second'], tzinfo=offset).isoformat()

            field = search_by.split('_')[0]+'At'
            comparison_sign = {'after': 'greater', 'before': 'less'}
            comparison = comparison_sign[search_by.split('_')[1]]+'Than'

            declaration_list.append("$search_date: Datetime!")
            # reposList_list.append("filter: {"+field+": {"+comparison+": $search_date}}")
            reposList_dict = {'filter': {field: {comparison: '$search_date'}}}
            variable_values['search_date'] = search_date_str
            mode = search_by
        elif search_by == 'description':
            if not isinstance(search, str):
                print("`search` must be a str to search by 'description'")
                return CitrosDict({})
            else:
                declaration_list.append('$search_description: String!')
                if exact_match:
                    # reposList_list.append('condition: {description: $search_description}')
                    reposList_dict = {'condition': {'description': '$search_description'}}
                else:
                    # reposList_list.append('filter: {description: {includes: $search_description}}')
                    reposList_dict = {'filter': {'description': {'includes': '$search_description'}}}
                variable_values['search_description'] = search
                mode = 'description'
        elif search_by == 'git':
            if not isinstance(search, str):
                print("`search` must be a str to search by 'git'")
                return CitrosDict({})
            else:
                declaration_list.append('$search_git: String!')
                if exact_match:
                    # reposList_list.append('condition: {git: $search_git}')
                    reposList_dict = {'condition': {'git': '$search_git'}}
                else:
                    # reposList_list.append('filter: {git: {includes: $search_git}}')
                    reposList_dict = {'filter': {'git': {'includes': '$search_git'}}}
                variable_values['search_git'] = search
                mode = 'git'
        else:
            reposList_dict = {}

        if user_id is not None:
            declaration_list.append('$user_id: UUID!')
            # reposList_list.append('condition: {userId: $user_id}')
            self._update_dict(reposList_dict, {'condition': {'userId': '$user_id'}})
            variable_values['user_id'] = user_id

        if not isinstance(search, int) and order_by is not None:
            order_by_arg = self._gql_order_dict(order_by, order_by_all)
            if order_by_arg != '':
                reposList_dict['orderBy'] = order_by_arg

        if len(variable_values) == 0:
            variable_values = None

        if len(declaration_list) != 0:
            declaration = '(' + ','.join(declaration_list) + ')'
        else:
            declaration = ''

        if len(reposList_dict) != 0:
            # reposList_arg = '(' + ','.join(reposList_list) + ')'
            reposList_arg = '(' + str(reposList_dict).replace("'", '')[1:-1] + ')'
        else:
            reposList_arg = ''

        query = """query MyQuery"""+declaration+""" {
                  reposList"""+reposList_arg+""" {
                    id
                    name
                    createdAt
                    updatedAt
                    description
                    git
                  }
                }
                """
        res = self._gql_execute(query, variable_values = variable_values)
        if res is None:
            CitrosDict({})
        result = {}
        for item in res['reposList']:
            inf_dict = CitrosDict({'id': item['id'], 'description': item['description'], 'created_at': item['createdAt'],
                                    'updated_at': item['updatedAt'], 'git': item['git']})
            if item['name'] in result.keys():
                if isinstance(result[item['name']], dict):
                    result[item['name']] = [result[item['name']]]
                result[item['name']].append(inf_dict)
            else:
                result[item['name']] = inf_dict
        result = CitrosDict(result)
        return result
    
    def _gql_order_dict(self, order_by, order_by_all):
        '''
        Parameters
        ----------
        order_by : dict or list or str
            dict with ordering rules
        order_by_all : dict
            dict with allowed keys for ordering and corresponding fields in the database.

        Returns
        -------
        str
            str for order_by statement
        '''
        result = ''
        if order_by is not None:
            order_by_list = []
            if isinstance(order_by, dict):
                for k, v in order_by.items():
                    if not isinstance(v, str):
                        print(f"could not resolve order by '{k}': '{v}', order should be string, either 'asc' or 'desc'")
                    else:
                        v = v.upper()
                        if k in order_by_all.keys():
                            if v in ['ASC', 'DESC']:
                                order_by_list.append(order_by_all[k]+'_'+v)
                            else:
                                print(f"could not resolve order by '{k}': '{v}', order should be either 'asc' or 'desc'")
                        else:
                            print(f"could not set order by '{k}', choose from {list(order_by_all.keys())}")
                if len(order_by_list) != 0:
                    result = '['+','.join(order_by_list)+']'
            elif isinstance(order_by, (str, list)):
                if isinstance(order_by, str):
                    order_by = [order_by]
                for k in order_by:
                    if k in order_by_all.keys():
                        order_by_list.append(order_by_all[k]+'_ASC')
                    else:
                        print(f"could not set order by '{k}', choose from {list(order_by_all.keys())}")
                if len(order_by_list) != 0:
                    #there is no 'orderBy' key word in batchRunsList_dict
                    result = '['+','.join(order_by_list)+']'
            else:
                print(f"the output is not ordered, `order_by` must be a dict, not {type(order_by).__name__}")
        return result

    def _update_dict(self, b, a):
        '''
        Recursively update the dictionary.
        '''
        if isinstance(a, dict):
            for k, v in a.items():
                if isinstance(b, dict) and k in b.keys():
                    self._update_dict(b[k], v)
                else:
                    b[k] = v
    
    def _search_batch(self, search: Optional[Union[str, int, float]] = None, search_by: str = None, sid_status: str = None, 
                   order_by: Optional[Union[str, list, dict]] = None, exact_match: bool = False, user_id: Optional[str] = None) -> CitrosDict:
        '''
        Return information about batches.
        '''
        sid_status_all = ['DONE', 'SCHEDULE', 'ERROR', 'CREATING', 'INIT', 'STARTING', 'RUNNING', 'TERMINATING', 'STOPPING']
        batch_status_all = ['DONE', 'SCHEDULE', 'RUNNING', 'TERMINATING', 'ERROR']
        data_status_all = ['LOADED', 'LOADING', 'UNLOADED', 'ERROR', 'UNKNOWN']
        order_by_all = {'name': 'NAME', 'id': 'ID', 'simulation': 'SIMULATION', 'status': 'STATUS', 'data_status': 'DATA_STATUS', 
                        'data_last_access': 'DATA_LAST_ACCESS', 'tag': 'TAG', 'message': 'MESSAGE', 'created_at': 'CREATED_AT', 
                        'updated_at': 'UPDATED_AT', 'parallelism': 'PARALLELISM', 'completions': 'COMPLETIONS', 
                        'cpu': 'CPU', 'gpu': 'GPU', 'memory': 'MEMORY'}

        declaration_list = []
        # batchRunsList_dict = {}
        variable_values = {}

        #main search
        if search_by is None:
            declaration_search, batchRunsList_dict, variable_values_search, mode = self._resolve_search(search, exact_match = exact_match)
            if mode == 'unknown':
                print("search_batch(): set `search` as int value (0 - the batch that was created first, -1 - the last created batch) "+ \
                        "or as str to search by batch's name or id")
                return CitrosDict({})
            # if (self._batch_id is not None) and self._batch_id != search:
            #     return CitrosDict({})
            if mode != 'all':
                declaration_list.append(declaration_search)
                # self._update_dict(batchRunsList_dict, batchRunsList_search)
                # batchRunsList_list.append(batchRunsList_search)
            variable_values = {**variable_values, **variable_values_search}
        elif search_by == 'name':
            if not isinstance(search, str):
                print("`search` must be a str to search by 'name'")
                return CitrosDict({})
            else:
                declaration_list.append('$search_name: String!')
                if exact_match:
                    # batchRunsList_list.append('condition: {name: $search_name}')
                    batchRunsList_dict = {'condition': {'name': '$search_name'}}
                else:
                    # batchRunsList_list.append('filter: {name: {includes: $search_name}}')
                    batchRunsList_dict = {'filter': {'name': {'includes': '$search_name'}}}
                variable_values['search_name'] = search
                mode = 'name'
        elif search_by in ['id', 'id']:
            if not isinstance(search, str):
                print("`search` must be a str to search by 'id'")
                return CitrosDict({})
            elif not self._is_uuid(search):
                print("`search` must have uuid format to search by 'id'")
                return CitrosDict({})
            # elif (self._batch_id is not None) and self._batch_id != search:
            #     return CitrosDict({})
            else:
                declaration_list.append('$search_id: UUID!')
                # batchRunsList_list.append('condition: {id: $search_id}')
                batchRunsList_dict = {'condition': {'id': '$search_id'}}
                variable_values['search_id'] = search
                mode = 'id'
        elif search_by == 'simulation':
            if not isinstance(search, str):
                print("`search` must be a str to search by 'simulation'")
                return CitrosDict({})
            else:
                declaration_list.append('$search_project: String!')
                if exact_match:
                    if (self._simulation is not None) and (self._simulation!=search):
                        return CitrosDict({})
                    else:
                        batchRunsList_dict = {'condition': {'simulation': '$search_project'}}
                else:
                    batchRunsList_dict = {'filter': {'simulation': {'includes': '$search_project'}}}
                variable_values['search_project'] = search
                mode = 'simulation'
        elif search_by in ['created_after', 'created_before', 'updated_after', 'updated_before', 'data_last_access_before', 'data_last_access_after']:
            if not isinstance(search, str):
                print("`search` must be a str to search by date fields")
                return CitrosDict({})
            search_date = self._parse_date(search)
            offset = timezone(int(search_date['tz_sign']+'1')*timedelta(hours=search_date['tz_h'], minutes=search_date['tz_m']))
            search_date_str = datetime(year = search_date['year'], month = search_date['month'], day = search_date['day'], 
                     hour = search_date['hour'], minute = search_date['minute'], second = search_date['second'], tzinfo=offset).isoformat()

            if search_by in ['created_after', 'created_before', 'updated_after', 'updated_before']:
                field = search_by.split('_')[0]+'At'
            elif search_by in ['data_last_access_before', 'data_last_access_after']:
                field = 'dataLastAccess'
            comparison_sign = {'after': 'greater', 'before': 'less'}
            comparison = comparison_sign[search_by.split('_')[-1]]+'Than'

            declaration_list.append("$search_date: Datetime!")
            # batchRunsList_list.append("filter: {"+field+": {"+comparison+": $search_date}}")
            batchRunsList_dict = {'filter': {field: {comparison: '$search_date'}}}
            variable_values['search_date'] = search_date_str
            mode = search_by
        elif search_by == 'status':
            if not isinstance(search, str):
                print("`search` must be a str to search by 'status'")
                return CitrosDict({})
            else:
                batch_status = search.upper()
                if not batch_status in batch_status_all:
                    print(f'search_batch(): batch status = "{search}" does not exist. Choose from: {batch_status_all}')
                    return CitrosDict({})
                declaration_list.append("$search_status: BatchStatusType!")
                # batchRunsList_list.append("condition: {status: $search_status}")
                batchRunsList_dict = {'condition': {'status': '$search_status'}}
                variable_values['search_status'] = batch_status
                mode = 'status'
        elif search_by == 'data_status':
            if not isinstance(search, str):
                print("`search` must be a str to search by 'data_status'")
                return CitrosDict({})
            else:
                data_status = search.upper()
                if not data_status in data_status_all:
                    print(f'search_batch(): data status = "{search}" does not exist. Choose from: {data_status_all}')
                    return CitrosDict({})
                declaration_list.append("$search_data_status: String!")
                batchRunsList_dict = {'condition': {'dataStatus': '$search_data_status'}}
                variable_values['search_data_status'] = data_status
                mode = 'data_status'
        elif search_by == 'tag':
            if not isinstance(search, str):
                print("`search` must be a str to search by 'tag'")
                return CitrosDict({})
            else:
                declaration_list.append('$search_tag: String!')
                if exact_match:
                    # batchRunsList_list.append('condition: {tag: $search_tag}')
                    batchRunsList_dict = {'condition': {'tag': '$search_tag'}}
                else:
                    # batchRunsList_list.append('filter: {tag: {includes: $search_tag}}')
                    batchRunsList_dict = {'filter': {'tag': {'includes': '$search_tag'}}}
                variable_values['search_tag'] = search
                mode = 'tag'
        elif search_by == 'message':
            if not isinstance(search, str):
                print("`search` must be a str to search by 'message'")
                return CitrosDict({})
            else:
                declaration_list.append('$search_message: String!')
                if exact_match:
                    # batchRunsList_list.append('condition: {message: $search_message}')
                    batchRunsList_dict = {'condition': {'message': '$search_message'}}
                else:
                    # batchRunsList_list.append('filter: {message: {includes: $search_message}}')
                    batchRunsList_dict = {'filter': {'message': {'includes': '$search_message'}}}
                variable_values['search_message'] = search
                mode = 'message'
        elif search_by == 'parallelism':
            if not isinstance(search, int):
                try:
                    search = int(search)
                except:
                    print("`search` must be an int to search by 'parallelism'")
                    return CitrosDict({})
            declaration_list.append('$search_parallelism: Int!')
            # batchRunsList_list.append('filter: {parallelism: {equalTo: $search_parallelism}}')
            batchRunsList_dict = {'filter': {'parallelism': {'equalTo': '$search_parallelism'}}}
            variable_values['search_parallelism'] = search
            mode = 'parallelism'
        elif search_by == 'completions':
            if not isinstance(search, int):
                try:
                    search = int(search)
                except:
                    print("`search` must be an int to search by 'completions'")
                    return CitrosDict({})
            declaration_list.append('$search_completions: Int!')
            # batchRunsList_list.append('filter: {completions: {equalTo: $search_completions}}')
            batchRunsList_dict = {'filter': {'completions': {'equalTo': '$search_completions'}}}
            variable_values['search_completions'] = search
            mode = 'completions'
        elif search_by == 'cpu':
            if not isinstance(search, float):
                try:
                    search = float(search)
                except:
                    print("`search` must be a float to search by 'cpu'")
                    return CitrosDict({})
            declaration_list.append('$search_cpu: Float!')
            # batchRunsList_list.append('filter: {cpu: {equalTo: $search_cpu}}')
            batchRunsList_dict = {'filter': {'cpu': {'equalTo': '$search_cpu'}}}
            variable_values['search_cpu'] = search
            mode = 'cpu'
        elif search_by == 'gpu':
            if not isinstance(search, float):
                try:
                    search = float(search)
                except:
                    print("`search` must be a float to search by 'gpu'")
                    return CitrosDict({})
            declaration_list.append('$search_gpu: Float!')
            # batchRunsList_list.append('filter: {gpu: {equalTo: $search_gpu}}')
            batchRunsList_dict = {'filter': {'gpu': {'equalTo': '$search_gpu'}}}
            variable_values['search_gpu'] = search
            mode = 'gpu'
        elif search_by == 'memory':
            if not isinstance(search, int):
                try:
                    search = int(search)
                except:
                    print("`search` must be a str or an int to search by 'memory'")
                    return CitrosDict({})
            declaration_list.append('$search_memory: BigInt!')
            # batchRunsList_list.append('filter: {memory: {equalTo: $search_memory}}')
            batchRunsList_dict = {'filter': {'memory': {'equalTo': '$search_memory'}}}
            variable_values['search_memory'] = search
            mode = 'memory'
        else:
            batchRunsList_dict = {}

        # we must use _update_dict() on batchRunsList_dict, as soon as there may be already be some 'condition' conditions
        if self._repo_id is not None:
            declaration_list.append('$repo_id: UUID!')
            self._update_dict(batchRunsList_dict, {'condition': {'repoId': '$repo_id'}})
            variable_values['repo_id'] = self._repo_id

        if self._simulation is not None:
            #we have already checked that in case search_by = 'simulation' search != self._simulation
            if exact_match and self._simulation==search:
                #the condition is already written
                pass
            else:
                declaration_list.append('$simulation: String!')
                self._update_dict(batchRunsList_dict, {'condition': {'simulation': '$simulation'}})
                variable_values['simulation'] = self._simulation

        if user_id is not None:
            declaration_list.append('$user_id: UUID!')
            self._update_dict(batchRunsList_dict, {'condition': {'userId': '$user_id'}})
            variable_values['user_id'] = user_id

        #condition on simulationRunsList, let simulationRunsList_arg be straightaway a string
        if sid_status is not None:
            sid_status_alt = sid_status.upper()
            if not sid_status_alt in sid_status_all:
                print(f'search_batch(): `sid_status` = "{sid_status}" does not exist. Choose from: {sid_status_all}')
                return CitrosDict({})
            declaration_list.append("$status_name: SimulationStatusType!")
            simulationRunsList_arg = "(condition: {status: $status_name})"
            variable_values["status_name"] = sid_status_alt
        else:
            simulationRunsList_arg = ""
        
        if len(variable_values) == 0:
            variable_values = None
        if len(declaration_list) !=0 :
            declaration = '('+','.join(declaration_list)+')'
        else:
            declaration = ""

        #'orderBy' in batchRunsList_dict may be only if `search` is int, and if `search` is int, returns one batch and we do not apply
        #ordering, so 'orderBy' is always unique in batchRunsList_dict
        if not isinstance(search, int) and order_by is not None:
            order_by_arg = self._gql_order_dict(order_by, order_by_all)
            #there is no 'orderBy' key word in batchRunsList_dict
            if order_by_arg != '':
                batchRunsList_dict['orderBy'] = order_by_arg
        
        if self._batch_id is not None:
            if variable_values.get('search_id'):
                if variable_values['search_id'] != self._batch_id:
                    #looking for the batch id that is different from the set self._batch_id
                    return CitrosDict({})
            else:
                declaration_list.append('$search_id: UUID!')
                batchRunsList_arg = {'condition': {'id': '$search_id'}}
                variable_values["search_id"] = search

        if len(batchRunsList_dict) != 0:
            # batchRunsList_arg = '('+','.join(batchRunsList_list)+')'
            batchRunsList_arg = '('+str(batchRunsList_dict).replace("'", '')[1:-1]+')'
        else:
            batchRunsList_arg = ''

        query = """query MyQuery"""+declaration+""" {
                  batchRunsList"""+batchRunsList_arg+""" {
                    id
                    name
                    createdAt
                    updatedAt
                    status
                    tag 
                    simulation
                    message
                    parallelism
                    completions
                    cpu
                    gpu
                    memory
                    dataStatus
                    dataLastAccess
                    simulationRunsList"""+simulationRunsList_arg+""" {
                      sid
                      status
                    }
                    repo {
                      name
                    }
                    
                  }
                }
                """
        res = self._gql_execute(query, variable_values = variable_values)
        if res is None:
            return CitrosDict({})

        result = {}
        for item in res['batchRunsList']:
            sids_list = []
            for s in item['simulationRunsList']:
                sids_list.append(int(s['sid']))
            # if len(sids_list) != 0:
            if sid_status is not None and len(sids_list) == 0:
                pass
            else:
                sids_list.sort()
                # result[item['id']]=sids_list
                link = f"https://citros.io/{quote(item['repo']['name'], safe='')}/data/runs/{quote(item['simulation'], safe='')}/{quote(item['name'], safe='')}"
                inf_dict = CitrosDict({'id': item['id'], 'sid': sids_list, 'created_at': item['createdAt'],
                                       'updated_at': item['updatedAt'], 'status': item['status'], 'data_status': item['dataStatus'], 
                                       'data_last_access': item['dataLastAccess'], 'tag': item['tag'],
                                       'simulation': item['simulation'], 'message': item['message'], 'parallelism': item['parallelism'],
                                       'completions': item['completions'], 'cpu': item['cpu'], 'gpu': item['gpu'], 
                                       'memory': item['memory'], 'repo': item['repo']['name'], 'link': link})
                if item['name'] in result.keys():
                    if isinstance(result[item['name']], dict):
                        result[item['name']] = [result[item['name']]]
                    result[item['name']].append(inf_dict)
                else:
                    result[item['name']] = inf_dict
        result = CitrosDict(result)
        return result

    def _get_batch_names(self, batch_ids):
        '''
        Return ids and names of the batches
        '''
        grql_query = """
        query MyQuery($batch_ids: [UUID!]) {
                    batchRunsList(
                        filter: {id: {in: $batch_ids}}
                    ) {
                        id
                        name
                    }
                    }
        """
        variable_values = {'batch_ids': batch_ids}
        return self._gql_execute(grql_query, variable_values = variable_values)
    
    def _get_batch_status(self, batch_id):
        '''
        Return the status of the batch.
        '''
        grql_query = """
        query MyQuery($batch_id: UUID!) {
          batchRunsList(condition: {id: $batch_id}) {
            dataStatus
            id
          }
        }
        """
        variable_values = {'batch_id': batch_id}
        res = self._gql_execute(grql_query, variable_values = variable_values)
        if len(res['batchRunsList']) != 0:
            return res['batchRunsList'][0]['dataStatus']
        else:
            return None

    def _set_data_access_time(self, batch_id):
        '''
        '''
        grql_query = """
        mutation dataAccessRequest($batchRun: UUID!) {
          setDataAccessTime(input: {batchRun: $batchRun}) {
            clientMutationId
          }
        }
        """
        variable_values = {'batchRun': batch_id}
        self._gql_execute(grql_query, variable_values = variable_values)

    def _set_batch_status(self, batch_id, status):
        '''
        '''
        grql_query = """
        mutation setStatus($batchRun: UUID!, $status: String!) {
          updateBatchRun(input: {id: $batchRun, patch: {dataStatus: $status}}) {
            clientMutationId
            batchRun {
              id
            }
          }
        }
        """
        variable_values = {'batchRun': batch_id, 'status': status}
        self._gql_execute(grql_query, variable_values = variable_values)
        
