import os
from gql import Client, gql
from gql.transport.exceptions import TransportQueryError
from gql.transport.requests import RequestsHTTPTransport
from pathlib import Path
import jwt
from datetime import datetime, timezone, timedelta
import inspect

class _GqlBase:
    '''
    Basis methods for communication with graph ql database
    '''
    _gql_client = None

    _jwt_token = None

    #the following parameters are collected for all objects created with debug = True parameter CitrosDB(debug = True):
    #number of connections to gql database
    n_gql_connections = 0
    #number of queries to gql database
    n_gql_queries = 0
    # dict with method names and corresponding number of queries
    gql_calls = {}

    def __init__(self):

        self.CITROS_ENVIRONMENT = os.getenv("CITROS_ENVIRONMENT", "LOCAL")
        url_prefix = "http" if self.CITROS_ENVIRONMENT == "CLUSTER" else "https"
        self.CITROS_DOMAIN = os.getenv("CITROS_DOMAIN", "citros.io")
        self.CITROS_URL = f"{url_prefix}://{self.CITROS_DOMAIN}"
        self.CITROS_ENTRYPOINT = f"{self.CITROS_URL}/api/graphql"

        self._jwt_token_env = "KERNEL_CITROS_ACCESS_KEY"

        self.CITROS_HOME_DIR = Path.home() / ".citros"

        self.alternate_auth_paths = [self.CITROS_HOME_DIR / "auth", 
                                    Path("/var/lib/citros/auth")]
        self._token_changed = False

        self._gql_debug = False
    
    def _find_citros_in_ancestors(self, proj_dir=""):
        current_dir = Path.cwd() if not proj_dir else Path(proj_dir).expanduser().resolve()

        # Ensure we don't go into an infinite loop at the root directory
        while current_dir != current_dir.parent:
            citros_dir = current_dir / ".citros"
            if citros_dir.exists():
                return citros_dir.expanduser().resolve()
            current_dir = current_dir.parent

        return None
    
    def _find_auth_key(self, proj_dir=""):
        # option 1: Start from current directory and traverse upwards
        citros_dir = self._find_citros_in_ancestors(proj_dir)
        if citros_dir is not None and Path(citros_dir, "auth").exists():
            return Path(citros_dir, "auth")

        # option 2: Look in alternate locations, e.g. the user's home folder.
        for auth_path in self.alternate_auth_paths:
            if auth_path.exists():
                return auth_path.expanduser().resolve()
        
        return None
    
    def _validate_token(self, token : str):
        """
        Validates the JWT token.

        Args:
        token: JWT token to validate.

        Returns:
        Boolean indicating if the token is valid.
        """
        try:
            dictionary = jwt.decode(token, options={"verify_signature": False}, audience="postgraphile")

            expiration_timestamp = dictionary.get('exp', None)
            if not expiration_timestamp:
                return False
            
            date = datetime.fromtimestamp(expiration_timestamp)
            current_timestamp = datetime.now().timestamp()

            if expiration_timestamp < current_timestamp:
                # self.print(f"your login token has expired on {date}", color='yellow', only_verbose=True)
                print(f"your login token has expired on {date}", color='yellow', only_verbose=True)
                return False

            return True
        
        except Exception as ex:
            self.handle_exceptions(ex)
            return False

    def handle_exceptions(self, e, exit=False):
        import traceback
        from os import linesep
        print(f"An exception was raised:")
        stack_trace = traceback.format_exception(type(e), e, e.__traceback__)
        stack_trace_str = "".join(stack_trace)
        print(f"Exception details:{linesep}{stack_trace_str}")

    def _get_transport(self):
        '''
        Obtain transport with authorization if user is authenticated.
        '''                      
        transport = RequestsHTTPTransport(
            url=self.CITROS_ENTRYPOINT,
            verify=True,
            retries=3            
        )
        if _GqlBase._jwt_token:
            transport.headers = {
                "Authorization": f"Bearer {_GqlBase._jwt_token}",
            }
        return transport

    def _get_gql_client(self):
        '''
        Obtain GraphQL client.
        '''
        _jwt_token = self._get_token_from_file()
        #client is set and token has not been changed -> return client
        if _GqlBase._gql_client and _GqlBase._jwt_token == _jwt_token:
            # print('return the same client')
            return _GqlBase._gql_client
        
        #client has not been set yet or client is set but token has been changed -> make new client
        _GqlBase._jwt_token = _jwt_token
        transport = self._get_transport()
        # print('new client')
        _GqlBase._gql_client = Client(transport=transport, fetch_schema_from_transport=False)
        if self._gql_debug:
            _GqlBase.n_gql_connections += 1
        return _GqlBase._gql_client

    def _gql_execute(self, query, variable_values=None):
        '''
        Execute a GraphQL query.

        Parameters
        ----------
        query : gql
            gql query
        variable_values : dict, default None
            variables for the gql query

        Returns
        -------
        dict: 
            Result of the executed query
        '''
        gql_query = gql(query)
        try:
            result = self._get_gql_client().execute(gql_query, variable_values=variable_values)
            if self._gql_debug:
                _GqlBase.n_gql_queries += 1
                self._calculate_gql_calls(inspect.stack()[1][3])
            return result
        except Exception as e:
            #try once again with new client
            try:
                _GqlBase._gql_client = None
                result = self._get_gql_client().execute(gql_query, variable_values=variable_values)
                if self._gql_debug:
                    _GqlBase.n_gql_queries += 1
                    self._calculate_gql_calls(inspect.stack()[1][3])
                return result
            except Exception as ex:
                self.handle_exceptions(ex)                      
        return None

    def _get_token_from_file(self):
        """
        Gets the JWT token from file
        """
        _jwt_token = os.getenv(self._jwt_token_env, None)
        if _jwt_token is None:
            try:
                auth_path = self._find_auth_key()
                if auth_path is None:
                    raise FileNotFoundError
                
                if auth_path not in self.alternate_auth_paths:
                    auth_paths = [auth_path] + self.alternate_auth_paths
                else:
                    idx = self.alternate_auth_paths.index(auth_path)
                    auth_paths = self.alternate_auth_paths[idx:]

                for path in auth_paths:
                    with open(path, mode='r') as file:            
                        _jwt_token = file.read()
                        # self._token_changed = True
                        if not self._validate_token(_jwt_token):
                            # self.log.info(f"JWT token stored at {path} is invalid, removing.")
                            print(f"JWT token stored at {path} is invalid")
                            # self._remove_token()
                        else:
                            break # valid token found
                        
            except FileNotFoundError as e:
                # Key file wasn't found. assuming the user is not logged in...
                _jwt_token = None
                return None
            except Exception as e:
                self.handle_exceptions(e)
                print(e)

        return _jwt_token
    
    def _calculate_gql_calls(self, method):
        if _GqlBase.gql_calls.get(method):
            _GqlBase.gql_calls[method] += 1
        else:
            _GqlBase.gql_calls[method] = 1