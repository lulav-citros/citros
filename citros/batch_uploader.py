import os
import time
import json
import yaml
import logging
import psycopg2
import traceback
from glob import glob
from decouple import config
from jinja2 import Environment, FileSystemLoader
from rich import print, inspect, print_json

from .logger import get_logger, shutdown_log
from pathlib import Path


class BatchUploader:
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

    ###################
    ##### private #####
    ###################

    def _get_citros_bags(self, path: str) -> list:
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
                    self.log.debug(f"Found MCAP bag: {file}")
                elif file.endswith(".citros.db3"):
                    self.log.debug(f"Found SQLITE3 bag: {file}")
                else:
                    continue
                bags.append(os.path.join(root, file))
        if len(bags) < 1:
            raise Exception(
                f"Didn't find SQLITE3 or MCAP bag in the [{path}] folder ..."
            )

        return bags

    def _get_custom_message(self, directory_path: str) -> list:
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
                self.log.debug(f"Found custom message in {msgs}")
        except Exception:
            msgs = []
        return msgs

    def _get_parameters(self, directory_path: str) -> list:
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
                    self.log.debug(f"Found json parameters file: {file}")
                elif file.endswith(".yaml") or file.endswith(".yml"):
                    self.log.debug(f"Found yaml parameters file: {file}")
                else:
                    continue
                parameters.append(os.path.join(root, file))
        if len(parameters) < 1:
            self.log.debug(
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

    def upload_bag_to_pg(
        self,
        connection,
        schema_name: str,
        table_name: str,
        sid: int,
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

        schema_name : str

        table_name : str

        sid : str
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
        from .ros import BagReaderCustomMessages

        cursor = connection.cursor()
        try:
            start_time = time.time()
            self.log.info(f"Uploading {bag} to PG")
            bagReader = BagReaderCustomMessages(
                msgs,
                log=self.log,
                debug=self.debug,
                verbose=self.verbose,
            )
            total_size = 0
            for buffer in bagReader.read_messages(bag, sid):
                size = buffer.seek(0, os.SEEK_END)
                size = buffer.tell()
                total_size = total_size + size
                buffer.seek(0)
                self.log.debug(
                    f" \tInserting buffer size: {((size / 1024 ) / 1024):.2f} MB"
                )
                if size == 0:
                    continue
                cursor.execute(f"SET search_path TO {schema_name}")
                try:
                    cursor.copy_from(
                        buffer,
                        table_name,
                        sep=chr(0x1E),
                        null="",
                        columns=["sid", "rid", "time", "topic", "type", "data"],
                    )
                except (Exception, psycopg2.Error) as error:
                    buffer.seek(0)
                    self.log.error(f"buffer = {buffer.getvalue()}")
                    self.log.error(
                        f" Failed to insert record into table, aborting upload to DB.",
                        error,
                    )
                    self.log.exception(error)
                    return False, "Got exception from pgdb", str(error)

                connection.commit()
            self.log.debug(
                f"Done uploading {bag}, took {(time.time() - start_time):.3f} [sec]"
            )
            return (
                True,
                f"Success, uploaded [{bag}] to Postgres. [size: {(total_size / 1024)/1024} MB]",
                None,
            )
        except (Exception, psycopg2.Error) as error:
            self.log.exception(
                f" Failed to insert record into table, aborting upload to DB.", error
            )
            self.log.exception(traceback.format_exc())
            return False, "Got exception from pgdb", str(error)
        # finally:
        #     # closing database connection.
        #     if connection:
        #         cursor.close()
        #         connection.close()
        #         self.log.debug(f"PostgreSQL connection is closed")
        #         logging.shutdown()

    def upload_parameters_to_pg(
        self,
        connection,
        schema_name: str,
        table_name: str,
        sid: str,
        parameter_file: str,
    ):
        """
        Upload simulation parameters to a PostgreSQL database table.

        This function takes a dictionary of parameters and uploads them to a specified table in a PostgreSQL database.
        If the upload is successful, the method will commit the changes and return a success message.

        Parameters:
        ----------

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
            self.log.debug(f"Uploading parameter file: {parameter_file}")
            parameter_dict = self._read_parameters_file(parameter_file)
            self.log.debug(f"Parameter:\n[{json.dumps(parameter_dict, indent=2)}]")
            record_to_insert = {
                "sid": sid,
                "rid": 0,
                "time": 0,
                "topic": "/config",
                "type": parameter_file,
                "data": parameter_dict,
            }

            postgres_insert_query = f""" 
                insert into {schema_name}."{table_name}"
                (sid, rid, time, topic, type, data)
                values (%(sid)s, %(rid)s, %(time)s, %(topic)s, %(type)s, %(data)s);
            """

            cursor = connection.cursor()
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()

        except Exception as e:
            self.log.error(e)

        # finally:
        #     if connection:
        #         cursor.close()
        #         connection.close()
        #         self.log.debug(f"PostgreSQL connection is closed")
        #         logging.shutdown()

    def upload(self):
        self.log.debug(f"{self.__class__.__name__}.upload()")

        self["data_status"] = "LOADING"

        # inspect(self)
        # print(f"self.batch_dir: {self.batch_dir}")

        from .database import CitrosDB

        citrosDB = CitrosDB(
            log=self.log, debug=self.debug, verbose=self.verbose
        )  # TODO[critical]: fill with data

        schema_name = f"{self.simulation_name}"
        table_name = f"{self.name}-{self.version}"

        connection = citrosDB.connect()

        citrosDB.create_table(connection, schema_name, table_name)

        for sid_path in glob(f"{self.batch_dir}/*/"):
            sid = sid_path.removesuffix("/").split("/")[-1]

            # upload all parameters
            parameters = self._get_parameters(f"{self.batch_dir}/{sid}/config/")
            # print(parameters)
            for parameter in parameters:
                try:
                    cursor = connection.cursor()
                    self.upload_parameters_to_pg(
                        connection,
                        schema_name=schema_name,
                        table_name=table_name,
                        sid=sid,
                        parameter_file=parameter,
                    )
                except Exception as e:
                    self.log.error(e)
                    connection = citrosDB.connect()

            # uplaod bags
            bags = self._get_citros_bags(f"{self.batch_dir}/{sid}/bags/")
            # print(bags)
            msgs = self._get_custom_message(f"{self.batch_dir}/{sid}/msgs/")
            # print(msgs)

            for bag in bags:
                try:
                    status, message, error = self.upload_bag_to_pg(
                        connection,
                        schema_name=schema_name,
                        table_name=table_name,
                        sid=sid,
                        bag=bag,
                        msgs=msgs,
                    )
                    self.log.debug(
                        f"status: {status}, message: {message}, error: {error}"
                    )
                except Exception as e:
                    self.log.error(e)
                    connection = citrosDB.connect()

        self["data_status"] = "LOADED"
        cursor.close()
        connection.close()

    def unload(self):
        from .database import CitrosDB

        citrosDB = CitrosDB(
            log=self.log, debug=self.debug, verbose=self.verbose
        )  # TODO[critical]: fill with data

        schema_name = f"{self.simulation_name}"
        table_name = f"{self.name}-{self.version}"

        connection = citrosDB.connect()

        citrosDB.drop_table(connection, schema_name, table_name)

        self["data_status"] = "UNLOADED"
