import os
import time
import psycopg2
import importlib_resources

from jinja2 import Template
from pathlib import Path
from .logger import get_logger, shutdown_log


class CitrosDB:
    def __init__(
        self,
        db_user="citros",
        db_password="password",
        db_host="localhost",
        db_port="5454",
        db_name="citros",
        organization_name="citros",
        log=None,
        verbose=False,
        debug=False,
    ) -> None:
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.organization_name = organization_name
        self.verbose = verbose
        self.debug = debug
        self._init_log(Path.cwd())

    ###################
    ##### private #####
    ###################
    def _init_log(self, root=None, log=None):
        self.log = log
        if self.log is None:
            log_dir = root / "logs"

            if not log_dir.exists():
                Path.home().joinpath(".citros/logs").mkdir(parents=True, exist_ok=True)
                log_dir = Path.home().joinpath(".citros/logs")

            self.log = get_logger(
                __name__,
                log_level=os.environ.get("LOGLEVEL", "DEBUG" if self.debug else "INFO"),
                log_file=str(log_dir / "citros.log"),
                verbose=self.verbose,
            )

    def init_db(self):
        """
        Initialize the database by creating the organization's database and executing SQL scripts.

        Args:
            organization_name (str): The name of the organization.
            db_user (str): The username for the database connection.
            db_password (str): The password for the database connection.
            db_host (str): The host address of the database server.
            db_port (int): The port number of the database server.
            db_name (str): The name of the database.

        Raises:
            Exception: If failed to render the SQL template.

        Returns:
            None
        """

        connection = self.connect()
        cursor = connection.cursor()
        connection.autocommit = True

        # Define variables for rendering the template
        context = {
            "ORGANIZATION_NAME": self.organization_name,
            "USER_NAME": self.db_user,
            "USER_PASSWORD": self.db_password,
        }
        # Render the template with the provided context
        with open(
            importlib_resources.files(f"data.sql").joinpath(
                "templates/create_db.sql.j2"
            ),
            "r",
        ) as file_:
            template = Template(file_.read())
            rendered_sql = template.render(context)

        if rendered_sql is None:
            raise Exception("Failed to render sql template")
        # cursor.execute(f'CREATE DATABASE "{organization_name}";')
        try:
            print(rendered_sql)
            cursor.execute(rendered_sql)
        except psycopg2.DatabaseError as e:
            print(f"Database already exist ... log: {e}")

        connection.close()

    def connect(self):
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
                    user=self.db_user,
                    password=self.db_password,
                    host=self.db_host,
                    port=self.db_port,
                    database=self.db_name,
                )
                self.log.info("Successfully connected to Postgres Database")

                return connection

            except psycopg2.OperationalError as e:
                if "too many clients" in str(e).lower():
                    time.sleep(sleep_durations[retries])
                    retries = retries + 1 if retries < 9 else 9
                    self.log.warning(e)
                else:
                    self.log.error(e)
                    break

    def create_table(self, connection, schema_name, table_name):
        from jinja2 import Environment, FileSystemLoader

        self.log.debug(f"creating table: {schema_name}.{table_name}")

        cursor = connection.cursor()

        context = {
            "ORGANIZATION_NAME": self.organization_name,
            "SCHEMA_NAME": schema_name,
            "TABLE_NAME": table_name,
        }

        with open(
            importlib_resources.files(f"data.sql").joinpath(
                "templates/create_table.sql.j2"
            ),
            "r",
        ) as file_:
            template = Template(file_.read())
            # Render the template with the provided context
            rendered_sql = template.render(context)

        # TODO: query check if table exists. if not, create it.
        try:
            cursor.execute(rendered_sql)
        except Exception as ex:
            print(ex)
            return

    def drop_table(self, connection, schema_name, table_name):
        from jinja2 import Environment, FileSystemLoader

        self.log.debug(f"dropping table: {schema_name}.{table_name}")

        cursor = connection.cursor()

        context = {
            "SCHEMA_NAME": schema_name,
            "TABLE_NAME": table_name,
        }

        with open(
            importlib_resources.files(f"data.sql").joinpath(
                "templates/drop_table.sql.j2"
            ),
            "r",
        ) as file_:
            template = Template(file_.read())
            # Render the template with the provided context
            rendered_sql = template.render(context)

        # TODO: query check if table exists. if not, create it.
        try:
            cursor.execute(rendered_sql)
            connection.commit()
            print(rendered_sql)
        except Exception as ex:
            print(ex)
