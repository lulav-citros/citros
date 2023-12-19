import importlib_resources
from jinja2 import Template


class CitrosDB:
    def __init__(
        self, organization_name, db_user, db_password, db_host, db_port, db_name
    ) -> None:
        self.organization_name = organization_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name

    @staticmethod
    def init_db(organization_name, db_user, db_password, db_host, db_port, db_name):
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
        import psycopg2

        connection = None
        connection = psycopg2.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_name,
        )
        cursor = connection.cursor()
        connection.autocommit = True
        # sql_files = ["create-organization-db.sql.j2", "create-organization-role.sql.j2"]

        # Define variables for rendering the template
        context = {
            "ORGANIZATION_NAME": organization_name,
            "USER_NAME": db_user,
            "USER_PASSWORD": db_password,
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
