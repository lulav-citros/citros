import traceback
import os
import time
import json
import yaml
import psycopg2
import logging
from glob import glob
from decouple import config
from jinja2 import Environment, FileSystemLoader

from rosbag import BagReaderCustomMessages
from logger import get_logger, shutdown_log
from pathlib import Path


class Uploader:
    """
    The Uploader class is responsible for uploading data to CITROS db.


    assuming structure:
        .citros/data/{simulation name}/{batch name}/{simulation run id}/bag/{bag file}

    Attributes:
    -----------
    root : str
        The root directory where the data is located. (default to .citros/data)
    simulation : str
        The simulation name.
    batch : str
        The batch name.
    version : str
        The version of the uploader.

    log : Optional
        The log object for logging messages.
    verbose : bool
        Flag indicating whether to enable verbose mode.
    debug : bool
        Flag indicating whether to enable debug mode.

    """

    def __init__(
        self,
        root: str,
        simulation: str,
        batch: str,
        version: str,
        log=None,
        verbose=False,
        debug=False,
    ) -> None:
        self.verbose = verbose
        self.debug = debug
        self._init_log(log)

    ###################
    ##### private #####
    ###################
    def _init_log(
        self,
        log=None,
    ):
        self.log = log
        if self.log is None:
            log_dir = self.root_citros / "logs"
            if self.new:
                log_dir.mkdir(parents=True, exist_ok=True)
            else:
                if not log_dir.exists():
                    Path.home().joinpath(".citros/logs").mkdir(
                        parents=True, exist_ok=True
                    )
                    log_dir = Path.home().joinpath(".citros/logs")

            self.log = get_logger(
                __name__,
                log_level=os.environ.get("LOGLEVEL", "DEBUG" if self.debug else "INFO"),
                log_file=str(log_dir / "citros.log"),
                verbose=self.verbose,
            )

    @staticmethod
    def _get_citros_bags(path: str) -> list:
        """
        Search for `.citros.mcap` and `.citros.db3` bag files in a specified directory.

        This method walks through the directory structure rooted at `path` to locate
        files ending with `.citros.mcap` or `.citros.db3`. It returns a list containing
        the full paths to these files.

        Parameters:
        -----------
        path : str
            The root directory where the search will begin.

        Returns:
        --------
        list
            A list of full file paths to the bag files. An exception is raised if no
            bag files are found.

        Raises:
        -------
        Exception
            If no `.citros.mcap` or `.citros.db3` bag files are found.

        Examples:
        ---------
        >>> _get_citros_bags('/path/to/root')
        ['/path/to/root/folder1/bag1.citros.mcap', '/path/to/root/folder2/bag2.citros.db3']

        """
        bags = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".citros.mcap"):
                    Uploader._logger.debug(f"Found MCAP bag: {file}")
                elif file.endswith(".citros.db3"):
                    Uploader._logger.debug(f"Found SQLITE3 bag: {file}")
                else:
                    continue
                bags.append(os.path.join(root, file))
        if len(bags) < 1:
            raise Exception(
                f"Didn't find SQLITE3 or MCAP bag in the [{path}] folder ..."
            )

        return bags

    @staticmethod
    def _create_table_if_not_exists(
        cursor, batch_run_id: str, organization_name: str
    ) -> None:
        """
        Create a new table in a PostgreSQL database if it doesn't exist.

        This method utilizes a Jinja2 SQL template (`create_table.sql.j2`) to generate
        the SQL query required to create the table. The SQL query is then executed to
        create the table if it doesn't already exist.

        Parameters:
        -----------
        cursor : psycopg2.cursor
            The psycopg2 cursor object associated with the database connection.

        batch_run_id : str
            The ID used to identify a specific batch run, used as part of the table name.

        organization_name : str
            The name of the organization, used in the SQL template for table creation.

        Returns:
        --------
        None

        Raises:
        -------
        psycopg2.Error
            If any error occurs while executing the SQL query.

        Examples:
        ---------
        >>> _create_table_if_not_exists(cursor, 'batch_001', 'my_organization')
        # (No output; table is created in database)

        """
        env = Environment(loader=FileSystemLoader("/app/sql/"))
        template = env.get_template("create_table.sql.j2")
        # Define variables for rendering the template
        context = {"ORGANIZATION_NAME": organization_name, "BATCH_RUN_ID": batch_run_id}
        # Render the template with the provided context
        rendered_sql = template.render(context)
        cursor.execute(rendered_sql)

    @staticmethod
    def _get_custom_message(directory_path: str) -> list:
        """
        Search for and return the paths of folders containing custom message types.

        This method searches through the directory specified by `directory_path` to
        find any folders that contain custom message types. These folders are assumed
        to contain a 'msg/' subdirectory.

        Parameters:
        -----------
        directory_path : str
            The directory path where the method will search for custom message types.

        Returns:
        --------
        list
            A list of strings, each being the path of a folder containing custom message types.

        Raises:
        -------
        Exception
            If any error occurs while accessing the file system.

        Examples:
        ---------
        >>> _get_custom_message('/path/to/directory')
        # ['/path/to/directory/custom_msgs1/msg/', '/path/to/directory/custom_msgs2/msg/']

        """
        try:
            packages = [
                folder
                for folder in os.listdir(directory_path)
                if os.path.isdir(os.path.join(directory_path, folder))
            ]
            msgs = [directory_path + package + "/msg/" for package in packages]
            if len(msgs) > 0:
                Uploader._logger.debug(f"Found custom message in {msgs}")
        except Exception:
            msgs = []
        return msgs

    @staticmethod
    def _get_parameters(directory_path: str) -> list:
        """
        Search for and return the paths of parameter files in the given directory.

        This method scans the directory specified by `directory_path` to find parameter files.
        It looks for files ending with ".json", ".yaml", or ".yml".

        Parameters:
        -----------
        directory_path : str
            The directory path where the method will search for parameter files.

        Returns:
        --------
        list
            A list of strings, each being the path of a parameter file.

        Logs:
        -----
        Debug log if no parameters are found in the specified directory.

        Examples:
        ---------
        >>> _get_parameters('/path/to/directory')
        # ['/path/to/directory/params1.json', '/path/to/directory/params2.yaml']

        """
        parameters = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".json"):
                    Uploader._logger.debug(f"Found json parameters file: {file}")
                elif file.endswith(".yaml") or file.endswith(".yml"):
                    Uploader._logger.debug(f"Found yaml parameters file: {file}")
                else:
                    continue
                parameters.append(os.path.join(root, file))
        if len(parameters) < 1:
            Uploader._logger.debug(
                f"Didn't find parameters in the [{directory_path}] folder ..."
            )

        return parameters

    @staticmethod
    def _read_parameters_file(file_path: str) -> dict:
        """
        Read the content of a parameter file and return it as a JSON-formatted dictionary.

        This method reads a parameter file specified by `file_path`, converts its content to
        a Python dictionary, and then returns the dictionary as a JSON-formatted string.
        It can read both JSON and YAML formatted parameter files.

        Parameters:
        -----------
        file_path : str
            The path to the parameter file to be read. The file should have either a .json, .yaml, or .yml extension.

        Returns:
        --------
        dict
            A dictionary containing the parameters read from the file, serialized to JSON format.

        Raises:
        -------
        Exception if the file cannot be read or parsed.

        Examples:
        ---------
        >>> _read_parameters_file('/path/to/params.json')
        # '{"key": "value"}'

        >>> _read_parameters_file('/path/to/params.yaml')
        # '{"key": "value"}'

        """
        _, ext = os.path.splitext(file_path)
        with open(file_path, "r") as f:
            if ext == ".json":
                return json.dumps(json.load(f))
            elif ext == ".yaml" or ext == ".yml":
                return json.dumps(yaml.safe_load(f))

    @classmethod
    def connect_to_pg(cls, pg_setup):
        """
        Establish a connection to a PostgreSQL database and return a connection object and cursor.

        This method tries to establish a connection to the PostgreSQL database using the
        setup parameters provided in `pg_setup`. If the connection is successful, it returns
        the connection object and a cursor to interact with the database. In case of an
        OperationalError like "too many clients", it retries connecting.

        Parameters:
        -----------
        pg_setup : dict
            A dictionary containing PostgreSQL setup parameters, including:
                - username: Database username
                - password: Database password
                - host: Database host address
                - port: Database port number
                - db_name: Database name

        Returns:
        --------
        connection : psycopg2.extensions.connection or None
            The connection object for the database, or None if the connection fails.

        cursor : psycopg2.extensions.cursor or None
            A new cursor object using the connection, or None if the connection fails.

        Raises:
        -------
        psycopg2.OperationalError:
            An error from the psycopg2 driver when unable to connect to the database.

        Examples:
        ---------
        >>> connect_to_pg({'username': 'user', 'password': 'pass', 'host': 'localhost', 'port': '5432', 'db_name': 'db'})
        # (psycopg2.extensions.connection, psycopg2.extensions.cursor)

        """
        connection = None
        retries = 0
        sleep_durations = [2**x for x in range(10)]
        while not connection:
            try:
                connection = psycopg2.connect(
                    user=pg_setup["username"],
                    password=pg_setup["password"],
                    host=pg_setup["host"],
                    port=pg_setup["port"],
                    database=pg_setup["db_name"],
                )
                cls._logger.info("Successfully connected to Postgres Database")
                cursor = connection.cursor()
                return connection, cursor

            except psycopg2.OperationalError as e:
                if "too many clients" in str(e).lower():
                    time.sleep(sleep_durations[retries])
                    retries = retries + 1 if retries < 9 else 9
                    cls._logger.warning(e)
                else:
                    cls._logger.error(e)
                    break

    @classmethod
    def initialize(cls) -> dict:
        """
        Initialize the setup parameters for connecting to a PostgreSQL database.

        This method retrieves several environment variables using the `config` function from the `decouple` package.
        It then validates that the required variables are set, and if not, logs an error and exits the program.
        Finally, it returns a dictionary containing all the setup parameters necessary for a PostgreSQL connection.

        Returns:
        --------
        pg_setup : dict
            A dictionary containing PostgreSQL setup parameters, including:
                - environment: The environment where the program is running ("CLUSTER" by default)
                - simulation_id: The simulation ID (from JOB_COMPLETION_INDEX environment variable)
                - batch_run_id: The batch run ID (from BATCH_RUN_ID environment variable)
                - host: Database host address
                - port: Database port number
                - db_name: Database name
                - username: Database username
                - password: Database password
                - organization_name: Organization name

        Raises:
        ------
        SystemExit:
            Exits the program if essential environment variables like CITROS_DATA_USERNAME, CITROS_DATA_PASSWORD, or ORGANIZATION_NAME are not set.

        Examples:
        ---------
        >>> initialize()
        # {'environment': 'CLUSTER', 'simulation_id': '', 'batch_run_id': '', ...}
        """
        # TODO: TRACE = config("TRACE_ID")

        environment = config("ENVIRONMENT", "CLUSTER")
        simulation_id = config("JOB_COMPLETION_INDEX", "")
        batch_run_id = config("BATCH_RUN_ID", "")

        host = config("POSTGRES_HOST", "shared-playground-postgresql.ns-citros-shared")
        port = config("POSTGRES_PORT", "5432")
        db_name = config("POSTGRES_DATABASE", "postgres")
        username = config("POSTGRES_USERNAME", "citros_anonymous")
        password = config("POSTGRES_PASSWORD", "citros_anonymous")
        organization_name = config("ORGANIZATION_NAME", "")

        if username == "citros_anonymous" or password == "citros_anonymous":
            cls._logger.error("CITROS_DATA_USERNAME/CITROS_DATA_PASSWORD not set")
            raise Exception("CITROS_DATA_USERNAME/CITROS_DATA_PASSWORD not set")

        if organization_name == "" or organization_name is None:
            cls._logger.error("ORGANIZATION_NAME not set")
            raise Exception("ORGANIZATION_NAME not set")

        pg_setup = {
            "environment": environment,
            "simulation_id": simulation_id,
            "batch_run_id": batch_run_id,
            "host": host,
            "port": port,
            "db_name": db_name,
            "username": username,
            "password": password,
            "organization_name": organization_name,
        }

        cls._logger.info("DB Setup:")
        cls._logger.info(f"\tEnvironment = {pg_setup['environment']}")
        cls._logger.info(f"\tUsername = {pg_setup['username']}")
        cls._logger.info(f"\tOrganization Name = {pg_setup['organization_name']}")

        return pg_setup

    @classmethod
    def upload_bag_to_pg(
        cls,
        cursor,
        connection,
        batch_run_id: str,
        simulation_id: int,
        bag: str,
        msgs: list,
    ):
        """
        Upload a bag file to a PostgreSQL database.

        This method reads messages from a bag file using the `BagReaderCustomMessages` class and uploads them to
        a PostgreSQL database table. The method handles both successful and unsuccessful uploads, logging
        appropriate messages in both cases.

        Parameters:
        ----------
        cursor : psycopg2.cursor
            The cursor object for interacting with the PostgreSQL database.

        connection : psycopg2.connection
            The connection object for the PostgreSQL database.

        batch_run_id : str
            The ID of the batch run to which this bag file belongs.

        simulation_id : str
            The ID of the simulation run to which this bag file belongs.

        bag : str
            The path to the bag file that needs to be uploaded.

        msgs : list
            List of paths to custom message directories (if any).

        Returns:
        -------
        tuple
            A tuple containing:
            - A boolean indicating whether the upload was successful.
            - A status message string.
            - None if successful, or an error message string if unsuccessful.

        Raises:
        ------
        Exception, psycopg2.Error:
            Any exceptions raised during database interactions are caught and logged.

        Examples:
        --------
        >>> upload_bag_to_pg(cursor, connection, 'batch_001', 'sim_001', '/path/to/bag', ['/path/to/custom/msg'])
        # (True, 'Success, uploaded [/path/to/bag] to Postgres. [size: 100 MB]', None)
        """
        try:
            start_time = time.time()
            cls._logger.info(f"Uploading {bag} to PG")
            bagReader = BagReaderCustomMessages(custom_message_path=msgs)
            total_size = 0
            for buffer in bagReader.read_messages(bag, simulation_id):
                size = buffer.seek(0, os.SEEK_END)
                size = buffer.tell()
                total_size = total_size + size
                buffer.seek(0)
                cls._logger.debug(
                    f" \tInserting buffer size: {((size / 1024 ) / 1024):.2f} MB"
                )
                if size == 0:
                    continue
                cursor.execute(f"SET search_path TO data_bucket")
                try:
                    cursor.copy_from(
                        buffer,
                        batch_run_id,
                        sep=chr(0x1E),
                        null="",
                        columns=["sid", "rid", "time", "topic", "type", "data"],
                    )
                except (Exception, psycopg2.Error) as error:
                    buffer.seek(0)
                    cls._logger.error(f"buffer = {buffer.getvalue()}")
                    cls._logger.error(
                        f" Failed to insert record into table, aborting upload to DB.",
                        error,
                    )
                    cls._logger.exception(error)
                    return False, "Got exception from pgdb", str(error)

                connection.commit()
            cls._logger.info(
                f"Done uploading {bag}, took {(time.time() - start_time):.3f} [sec]"
            )
            return (
                True,
                f"Success, uploaded [{bag}] to Postgres. [size: {(total_size / 1024)/1024} MB]",
                None,
            )
        except (Exception, psycopg2.Error) as error:
            cls._logger.exception(
                f" Failed to insert record into table, aborting upload to DB.", error
            )
            cls._logger.exception(traceback.format_exc())
            return False, "Got exception from pgdb", str(error)
        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                cls._logger.debug(f"PostgreSQL connection is closed")
                logging.shutdown()

    @classmethod
    def upload_parameters_to_pg(
        cls,
        cursor,
        connection,
        batch_run_id: str,
        simulation_run_id: int,
        parameter_file: str,
    ):
        """
        Upload simulation parameters to a PostgreSQL database table.

        This function takes a dictionary of parameters and uploads them to a specified table in a PostgreSQL database.
        If the upload is successful, the method will commit the changes and return a success message.

        Parameters:
        ----------
        cursor : psycopg2.cursor
            The cursor object for interacting with the PostgreSQL database.

        connection : psycopg2.connection
            The connection object for the PostgreSQL database.

        params_dict : dict
            A dictionary containing key-value pairs of parameters to upload. Keys are parameter names as strings,
            and values are the corresponding parameter values.

        table_name : str, optional
            The name of the database table where parameters should be uploaded. Default is 'parameters'.

        Returns:
        -------
        tuple
            A tuple containing:
            - A boolean indicating whether the upload was successful.
            - A status message string.
            - None if successful, or an error message string if unsuccessful.

        Raises:
        ------
        psycopg2.Error:
            Any exceptions raised during database interactions are caught and logged.

        Examples:
        --------
        >>> params = {'param1': 1, 'param2': 2}
        >>> upload_parameters_to_pg(cursor, connection, params)
        # (True, 'Parameters uploaded successfully to table [parameters].', None)
        """
        try:
            cls._logger.debug(f"Uploading parameter file: {parameter_file}")
            parameter_dict = cls._read_parameters_file(parameter_file)
            cls._logger.debug(f"Parameter:\n[{json.dumps(parameter_dict, indent=2)}]")
            record_to_insert = {
                "sid": simulation_run_id,
                "rid": 0,
                "time": 0,
                "topic": "/config",
                "type": parameter_file,
                "data": parameter_dict,
            }

            postgres_insert_query = f""" 
                insert into data_bucket."{batch_run_id}"
                (sid, rid, time, topic, type, data)
                values (%(sid)s, %(rid)s, %(time)s, %(topic)s, %(type)s, %(data)s);
            """

            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()

        except Exception as e:
            cls._logger.error(e)

        finally:
            if connection:
                cursor.close()
                connection.close()
                cls._logger.debug(f"PostgreSQL connection is closed")
                logging.shutdown()

    @classmethod
    def sync_element(cls, *args) -> None:
        """
        Synchronize a specified element (either parameters or bag data) to the PostgreSQL database.

        This method takes in various arguments to specify what kind of data to sync (parameters or bag),
        and then delegates the actual upload task to the appropriate helper methods
        (`upload_parameters_to_pg` or `upload_bag_to_pg`).

        Parameters:
        ----------
        *args : tuple
            Arguments unpacked in the method. The first argument should be `batch_run_id`, the second
            `simulation_id`, the third `pg_setup`, and the fourth `element_type` which specifies the type of element
            to sync ("parameter" or "bag"). Additional arguments depend on the element_type.

        Returns:
        -------
        None

        Raises:
        ------
        Exception
            Any exceptions raised during the process are caught, logged, and the PostgreSQL connection is reset.

        Examples:
        --------
        >>> sync_element(batch_run_id='batch123', simulation_id=0, pg_setup=pg_setup_dict, element_type='parameter', parameter_file='params.json')
        # Uploads parameter data to the Postgres database.

        >>> sync_element(batch_run_id='batch123', simulation_id=0, pg_setup=pg_setup_dict, element_type='bag', bag_file='data.bag', msgs=custom_msgs)
        # Uploads bag data to the Postgres database.

        """
        batch_run_id = args[0]
        simulation_id = args[1]
        pg_setup = args[2]
        element_type = args[3]

        cls.start_time = time.time()

        connection, cursor = cls.connect_to_pg(pg_setup)

        try:
            cls._create_table_if_not_exists(
                cursor, batch_run_id, pg_setup["organization_name"]
            )
        except Exception as ex:
            print(ex)
            # https://stackoverflow.com/questions/10399727/psqlexception-current-transaction-is-aborted-commands-ignored-until-end-of-tra
            connection, cursor = cls.connect_to_pg(pg_setup)

        if element_type == "parameter":
            cls.upload_parameters_to_pg(
                cursor, connection, batch_run_id, simulation_id, args[4]
            )
        elif element_type == "bag":
            cls.upload_bag_to_pg(
                cursor, connection, batch_run_id, simulation_id, args[4], args[5]
            )

    @classmethod
    def sync(cls) -> None:
        """
        Perform a full synchronization of bags and parameters to a PostgreSQL database.

        This method initializes database settings and iterates through all the simulation runs
        within the batch. For each simulation run, it fetches Citros bags and parameters and uploads
        them to the PostgreSQL database using helper methods.

        Steps:
        1. Initialize database settings with `initialize()`.
        2. Traverse through each simulation folder and identify batches and simulations.
        3. For each simulation run, identify the bags and parameters.
        4. Synchronize each element using `sync_element`.

        Returns:
        -------
        None

        Raises:
        ------
        Exception
            Exceptions are handled in helper methods and logged appropriately.

        Examples:
        --------
        >>> Uploader.sync()
        # Syncs all Citros bags and parameters for all batches and simulation runs to the Postgres database.
        """
        pg_setup = cls.initialize()

        runs = "/var/lib/citros/runs"

        cls._logger.debug(f"runs: [{runs}]")
        for simulation_name in glob(f"{runs}/*"):
            cls._logger.debug(f"simulation_name folder: [{simulation_name}]")

            for batch_name in glob(f"{simulation_name}/*"):
                cls._logger.debug(f"\tbatch_name folder: [{batch_name}]")

                with open(f"{batch_name}/info.json") as f:
                    batch_info = json.load(f)

                for sid_path in glob(f"{batch_name}/*"):
                    if sid_path.split(".")[-1] == "json":
                        continue
                    cls._logger.debug(f"\t\tsid: [{sid_path}]")

                    with open(f"{sid_path}/info.json") as f:
                        simulation_run_info = json.load(f)

                    batch_id = batch_info["id"]
                    sid = simulation_run_info["id"]

                    # expect multiple bags inside a folder only if the bag is splitted into multiple bags
                    bags = cls._get_citros_bags(f"{sid_path}/bag/")
                    msgs = cls._get_custom_message(f"{sid_path}/msgs/")
                    parameters = cls._get_parameters(f"{sid_path}/config/")

                    for parameter in parameters:
                        cls.sync_element(
                            batch_id, sid, pg_setup, "parameter", parameter
                        )

                    for bag in bags:
                        cls.sync_element(batch_id, sid, pg_setup, "bag", bag, msgs)


def main():
    Uploader.sync()


if __name__ == "__main__":
    main()
