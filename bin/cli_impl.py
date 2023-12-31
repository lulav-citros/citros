import os
import glob
import json
import importlib_resources

from bin import __version__ as citros_version
from time import sleep
from citros import Citros
from pathlib import Path
from rich import box, print, inspect, print_json, pretty
from rich.table import Table
from rich.console import Console
from rich.rule import Rule
from rich.panel import Panel
from rich.padding import Padding
from rich.logging import RichHandler
from rich.console import Console
from rich.markdown import Markdown
from rich_argparse import RichHelpFormatter


pretty.install()

from InquirerPy import prompt, inquirer
from rich.prompt import Prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from prompt_toolkit.validation import Validator, ValidationError

from citros import (
    Batch,
    CitrosNotFoundException,
    str_to_bool,
    suppress_ros_lan_traffic,
    Report,
    NoNotebookFoundException,
    NoConnectionToCITROSDBException,
)
from .config import config

# import sys
# import path
# directory = path.Path(__file__).abspath()
# sys.path.append(directory.parent.parent)


class NumberValidator(Validator):
    """
    small helper class for validating user input during an interactive session.
    """

    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message="Please enter a number", cursor_position=len(document.text)
            )


def citros(args, argv):
    print(
        Panel(
            Markdown(
                open(
                    importlib_resources.files(f"data.doc.cli").joinpath("citros.md"),
                    "r",
                ).read()
            ),
            subtitle=f"[{citros_version}]",
        )
    )
    # action
    action = inquirer.select(
        message="Select Action:",
        choices=[
            Choice("data", name="Data: for data managment "),
            Choice("report", name="Report: generation and management"),
            Choice("run", name="Run: new simulation"),
            # Separator(),
        ],
        default="",
        border=True,
    ).execute()

    if action == "data":
        data(args, argv)
    elif action == "report":
        report(args, argv)
    elif action == "run":
        run(args, argv)
    else:
        print("[red]Error: unknown action")


############################# CLI implementation ##############################
def init(args, argv):
    """
    :param args.dir:
    :param args.debug:
    :param args.verbose:
    """
    print(f'initializing CITROS at "{Path(args.dir).resolve()}". ')
    citros = Citros(new=True, root=args.dir, verbose=args.verbose, debug=args.debug)
    if args.debug:
        print("[green]done initializing CITROS")


def run(args, argv):
    """
    :param args.simulation_name:
    :param args.index:
    :param args.completions:

    :param args.batch_name:
    :param args.batch_message:

    :param args.lan_traffic:

    :param args.debug:
    :param args.verbose:
    """

    try:
        citros = Citros(root=args.dir, verbose=args.verbose, debug=args.debug)
    except CitrosNotFoundException:
        print(
            f"[red]Error:[/red] {Path(args.dir).expanduser().resolve()} has not been initialized with citros."
        )
        print(Panel.fit(Padding("You may run [green]citros init ", 1), title="help"))
        return

    if args.debug:
        print("[green]done initializing CITROS")

    if not hasattr(args, "batch_name"):
        batch_name = Prompt.ask("Please name this batch run", default="citros")
    else:
        batch_name = args.batch_name

    # print(batch_name)

    if not hasattr(args, "batch_message"):
        batch_message = Prompt.ask(
            "Enter a message for this batch run",
            default="This is a default batch message from citros",
        )
    else:
        batch_message = args.batch_message

    if not hasattr(args, "completions"):
        completions = Prompt.ask(
            "How many times you want the simulation to run?",
            default="1",
        )
    else:
        completions = args.completions

    if not batch_name and str_to_bool(citros.settings["force_batch_name"]):
        print("[red]Please supply a batch name with flag -n <name>.")
        print(
            Panel.fit(
                Padding('You may run [green]"citros run -n <name>" ', 1), title="help"
            )
        )
        return False

    if not batch_message and str_to_bool(citros.settings["force_message"]):
        print("[red]Please supply a batch message with flag -m <message>.")
        print(
            Panel.fit(
                Padding('You may run [green]"citros run -m <message>"', 1), title="help"
            )
        )
        return False

    simulation_name = getattr(args, "simulation_name", None)
    simulation = choose_simulation(
        citros,
        simulation_name,
    )
    root_rec_dir = f"{args.dir}/.citros/data"
    if config.RECORDINGS_DIR:
        root_rec_dir = config.RECORDINGS_DIR

    batch = Batch(
        root_rec_dir,
        simulation,
        name=batch_name,
        message=batch_message,
        version=getattr(args, "version", None),
        verbose=args.verbose,
        debug=args.debug,
    )
    try:
        batch.run(
            completions,
            getattr(args, "index", -1),
            ros_domain_id=config.ROS_DOMAIN_ID,
            trace_context=config.TRACE_CONTEXT,
        )
    except ModuleNotFoundError:
        print("[red]Error:[/red] ROS2 is not installed or not in your PATH.")
        print(
            Panel(
                Padding(
                    """Please install ROS2 on the system and source it:
[green]source /opt/ros/{ros2 distribution}/setup.bash[/green]

Please build your ROS2 workspace and source it by:
[green]colcon build
source install/local_setup.bash""",
                    1,
                ),
                title="help",
            )
        )
        return
    # when running multiple runs, load to DB after all runs is done.
    # if index != -1 then we run only a part of the batch, so we don't want to load to DB yet.
    if getattr(args, "index", -1) == -1:
        try:
            print("Upoading data po DB...")
            batch.unload()
            batch.upload()
        except NoConnectionToCITROSDBException:
            print("[red]CITROS DB is not running.")
            print(
                Panel.fit(
                    Padding("[green]citros data db create", 1),
                    title="help",
                )
            )

    print(f"[green]CITROS run completed successfully. ")
    print(
        f"[green]You may run [blue]'citros data service'[/blue] to get access to your data using CITROS API."
    )


# helper function
def choose_simulation(citros: Citros, simulation_name=None):
    """
    Choose a simulation from the available simulations in the Citros object.

    Args:
        citros (Citros): The Citros object containing the simulations.
        simulation_name (str, optional): The name of the simulation to choose. Defaults to None.

    Returns:
        Simulation: The chosen simulation object.

    Raises:
        KeyError: If the specified simulation name is not found in the available simulations.
    """

    simulations_dict = {}
    for s in citros.simulations:
        simulations_dict[s.name] = s

    if simulation_name:
        return simulations_dict[simulation_name]
    sim_names = simulations_dict.keys()

    # sanity check - should never happen because internal_sync will fail if there
    #                isn't at least one simulation file.
    if not sim_names:
        print(
            f"[red]There are currently no simulations in your {citros.SIMS_DIR} folder. \
                	 Please create at least one simulation for your project."
        )
        return

    # interactive
    answers = prompt(
        [
            {
                "type": "list",
                "name": "sim_names",
                "message": "Please choose the simulation you wish to run:",
                "choices": sim_names,
            }
        ]
    )

    sim_name = answers.get("sim_names")
    return simulations_dict[sim_name]


def doctor(args, argv):
    # TODO[critical]: implement doctor
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


############################# Simulation implementation ##############################
def simulation_list(args, argv):
    # TODO[critical]: implement
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def simulation_run(args, argv):
    # TODO[critical]: implement
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


####################### parameter setup implementation ##############################
def parameter_setup_new(args, argv):
    # TODO[critical]: implement
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def parameter_setup_list(args, argv):
    # TODO[critical]: implement
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def parameter_setup(args, argv):
    # TODO[critical]: implement
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


############################# DATA implementation ##############################
def data(args, argv):
    # -s simulation
    # -n name
    # -i version index
    # print batch info.

    try:
        citros = Citros(root=args.dir, verbose=args.verbose, debug=args.debug)
    except CitrosNotFoundException:
        print(
            f"[red]Error:[/red] {Path(args.dir).expanduser().resolve()} has not been initialized with citros."
        )
        print(Panel.fit(Padding("You may run [green]citros init ", 1), title="help"))
        return

    simulations = [sim.name for sim in citros.simulations]

    if simulations == []:
        print(f"There are currently no simulations in {citros.root_citros} folder.")
        print("Go wild and run as many simulation as you can with CITROS. ")
        print(
            Panel.fit(
                Padding('[green]citros run -n <name>" -m <message', 1),
                title="help",
            )
        )
        return
    chosen_simulation = inquirer.select(
        message="Select Simulation:",
        choices=[
            Choice("list", name="List: list all runs"),
            Separator(),
        ]
        + simulations,
        default="",
        border=True,
    ).execute()

    if chosen_simulation == "list":
        data_list(args, argv)
        return

    # batch

    batches = citros.get_batches(simulation=chosen_simulation)
    batches = [batch["name"] for batch in batches]
    if batches == []:
        print("[yellow]There are no batches for this simulation yet.")
        print(
            Panel.fit(
                Padding(
                    'You may run [green]"citros run"[/green] to create a new DB',
                    1,
                )
            )
        )
        return

    chosen_batch = inquirer.fuzzy(
        message="Select Batch:", choices=batches, default="", border=True
    ).execute()

    batches = citros.get_batches(simulation=chosen_simulation, batch=chosen_batch)
    assert len(batches) <= 1

    # version
    versions = batches[0]["versions"]
    version = inquirer.fuzzy(
        message="Select Version:", choices=versions, default="", border=True
    ).execute()

    # action
    action = inquirer.select(
        message="Select Action:",
        choices=[
            Choice("info", name="Info"),
            Choice("load", name="Load"),
            Choice("unload", name="Unload"),
            Choice("delete", name="Delete")
            # Separator(),
        ],
        default="",
        border=True,
    ).execute()

    # commands
    if action == "info":
        # print(
        #     f"chosen_simulation={chosen_simulation}, chosen_batch={chosen_batch}, version={version}"
        # )
        batch = citros.get_batch(
            simulation=chosen_simulation, name=chosen_batch, version=version
        )

        console = Console()
        console.rule(
            f".citros/data/{chosen_simulation}/{chosen_batch}/{version}/info.json"
        )
        console.print_json(data=batch.data)

    elif action == "load":
        print(
            f"Uploading data to DB... { chosen_simulation} / {chosen_batch} / {version}"
        )
        batch = citros.get_batch(
            simulation=chosen_simulation, name=chosen_batch, version=version
        )

        try:
            batch.unload()
            batch.upload()
        except NoConnectionToCITROSDBException:
            print("[red]CITROS DB is not running.")
            print(
                Panel.fit(
                    Padding(
                        'You may run [green]"citros data db create"[/green]  to create a new DB',
                        1,
                    )
                )
            )
            return

        console = Console()
        console.rule(f"{chosen_simulation} / {chosen_batch} / {version}")
        console.print_json(data=batch.data)

    elif action == "unload":
        print(
            f"Dropping data from DB... { chosen_simulation } / {chosen_batch} / {version}"
        )
        batch = citros.get_batch(
            simulation=chosen_simulation, name=chosen_batch, version=version
        )

        batch.unload()

    elif action == "delete":
        print(f"deleting data from { chosen_simulation } / {chosen_batch} / {version}")
        citros.delete_batch(
            simulation=chosen_simulation, name=chosen_batch, version=version
        )


def data_list(args, argv):
    # inspect(args)
    try:
        citros = Citros(root=args.dir, verbose=args.verbose, debug=args.debug)
        flat_batches = citros.get_batches_flat()
    except CitrosNotFoundException:
        print(
            f"[red]Error:[/red] {Path(args.dir).expanduser().resolve()} has not been initialized with citros."
        )
        print(Panel.fit(Padding("You may run [green]citros init ", 1), title="help"))

        return

    table = Table(
        title=f"Simulation Runs in: [blue]{citros.root_citros / 'data'}", box=box.SQUARE
    )
    # table.add_column(
    #     "date",
    #     style="green",
    #     no_wrap=True,
    # )
    # table.add_column(
    #     "date",
    #     style="green",
    #     no_wrap=True,
    # )
    table.add_column("Simulation", style="cyan", no_wrap=True)
    table.add_column("Run name", style="magenta", justify="left")
    table.add_column("Versions", justify="left", style="green")
    table.add_column("message", style="magenta", justify="left")
    table.add_column("status", justify="right", style="green")
    table.add_column("completions", style="magenta", justify="center")
    table.add_column(
        "path", style="cyan", justify="left", no_wrap=False, overflow="fold"
    )

    for flat_batch in flat_batches:
        if flat_batch["status"] == "LOADED":
            status_clore = "green"
        elif flat_batch["status"] == "UNLOADED":
            status_clore = "yellow"
        else:
            status_clore = "red"

        table.add_row(
            flat_batch["simulation"],
            flat_batch["name"],
            flat_batch["version"],
            flat_batch["message"],
            f"[{status_clore}]{flat_batch['status']}",
            flat_batch["completions"],
            # flat_batch["path"],
            str(flat_batch["path"]).removeprefix(os.getcwd()).removeprefix("/"),
        )

    console = Console()
    console.print(table)


def data_service(args, argv):
    """
    :param args.dir
    :param args.debug:
    :param args.verbose:
    :param args.project_name:
    """
    from citros import data_access_service, NoDataFoundException

    root = Path(args.dir).expanduser().resolve() / ".citros/data"
    print(
        Panel.fit(
            f"""started at [green]http://{args.host}:{args.port}[/green].
API: open [green]http://{args.host}:{args.port}/redoc[/green] for documantation
Listening on: [green]{str(root)}""",
            title="[green]CITROS service",
        )
    )
    try:
        # TODO[important]: make async
        data_access_service(
            str(root),
            time=args.time,
            host=args.host,
            port=int(args.port),
            debug=args.debug,
            verbose=args.verbose,
        )
    except NoDataFoundException:
        print(
            f'[red] "{Path(args.dir).expanduser().resolve()}" has not been initialized. cant run "citros data service" on non initialized directory.'
        )
        return


def data_service_status(args, argv):
    # TODO[important]: implement  after making this sevice async. return status of service.
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


# Hot Reload
def data_load(args, argv):
    pass


# Hot Reload
def data_unload(args, argv):
    pass


def data_db(args, argv):
    # TODO[important]: implement
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def _init_db(verbose, debug):
    """
    initializing the DB
    """
    from citros import CitrosDB

    citrosDB = CitrosDB(
        config.POSTGRES_USERNAME,
        config.POSTGRES_PASSWORD,
        config.CITROS_DATA_HOST,
        config.CITROS_DATA_PORT,
        config.POSTGRES_DATABASE,
        verbose=verbose,
        debug=debug,
    )

    citrosDB.init_db()


def data_db_create(args, argv):
    import docker

    # inspect(config)
    try:
        client = docker.from_env()
    except Exception as e:
        print(
            "[red]Docker is not running. Please start docker and try again. exiting..."
        )
        if args.verbose:
            raise e
        return

    try:
        container = client.containers.get(config.DB_CONTAINER_NAME)
        container.start()
        # inspect(container)
        print(f"[green]CITROS DB is created")
        return
    except docker.errors.NotFound:
        container = None

    container = client.containers.run(
        "postgres",
        name=config.DB_CONTAINER_NAME,
        environment=[
            f"POSTGRES_USER={config.POSTGRES_USERNAME}",
            f"POSTGRES_PASSWORD={config.POSTGRES_PASSWORD}",
            f"POSTGRES_DB={config.POSTGRES_DATABASE}",
        ],
        detach=True,
        ports={"5432/tcp": config.CITROS_DATA_PORT},
    )
    # TODO: check container status...
    sleep(3)
    print(f"[green]CITROS Initializing DB...")
    _init_db(args.verbose, args.debug)
    print(
        f"[green]CITROS DB is running at: {config.CITROS_DATA_HOST}:{config.CITROS_DATA_PORT}"
    )


def data_db_init(args, argv):
    print(f"[green]CITROS Initializing DB...")
    _init_db(args.verbose, args.debug)
    print(
        f"[green]CITROS DB is running at: {config.CITROS_DATA_HOST}:{config.CITROS_DATA_PORT}"
    )


def data_db_status(args, argv):
    import docker

    try:
        client = docker.from_env()
    except Exception as e:
        print(
            "[red]Docker is not running. Please start docker and try again. exiting..."
        )
        if args.verbose:
            raise e
        return

    container = client.containers.get(config.DB_CONTAINER_NAME)
    # print(container)
    if container:
        print(
            f"[green]CITROS DB is running at: {container.attrs['NetworkSettings']['IPAddress']}:{container.attrs['NetworkSettings']['Ports']['5432/tcp'][0]['HostPort']}"
        )
    else:
        print(
            f"[red]CITROS DB is not running. Please run 'citros data db create' to create a new DB."
        )

    # console = Console()
    # with console.screen(hide_cursor=False) as screen:
    #     for line in container.stats(stream=True):
    #         stat = line.strip()
    #         stat = json.loads(stat)
    #         stat = json.dumps(stat, indent=4)
    #         # console.print(stat)
    #         screen.update(Panel(str(stat)))
    #         # inspect(stat)
    #         # sleep(5)
    #         #TODO: create status panel.


def data_db_stop(args, argv):
    import docker

    try:
        client = docker.from_env()
    except Exception as e:
        print(
            "[red]Docker is not running. Please start docker and try again. exiting..."
        )
        if args.verbose:
            raise e
        return

    try:
        container = client.containers.get(config.DB_CONTAINER_NAME)
        container.stop()
        print(f"[green]CITROS DB is stopped.")
    except docker.errors.NotFound:
        print(f"[green]CITROS DB is not running.")


def data_db_logs(args, argv):
    import docker

    try:
        client = docker.from_env()
    except Exception as e:
        print(
            "[red]Docker is not running. Please start docker and try again. exiting..."
        )
        if args.verbose:
            raise e
        return

    try:
        container = client.containers.get(config.DB_CONTAINER_NAME)
        console = Console()
        console.rule(
            f" Logs from CITROS database container: {config.DB_CONTAINER_NAME}"
        )
        for line in container.logs(stream=True, follow=False):
            print(line.decode("utf8").strip())
            # console.line(line.decode("utf8").strip())
            # console.log(line.decode("utf8").strip())

        console.rule()
    except docker.errors.NotFound:
        print(
            f"[red]CITROS DB is not running. Please run 'citros data db create' to create a new DB."
        )
        print(
            Panel.fit(
                Padding('You may run [green]"citros data db create" ', 1), title="help"
            )
        )


def data_db_clean(args, argv):
    import docker

    try:
        client = docker.from_env()
    except Exception as e:
        print(
            "[red]Docker is not running. Please start docker and try again. exiting..."
        )
        if args.verbose:
            raise e
        return

    container = client.containers.get(config.DB_CONTAINER_NAME)
    try:
        container.remove()
    except docker.errors.APIError as e:
        if e.status_code == 409:
            print("[red]CITROS DB is running. Please stop it before cleaning.")
            print(
                Panel.fit(
                    Padding('You may run [green]"citros data db stop" ', 1),
                    title="help",
                )
            )
        else:
            raise e


############################# REPORT implementation ##############################
def report(args, argv):
    print(
        Panel(
            Markdown(
                open(
                    importlib_resources.files(f"data.doc.cli").joinpath("report.md"),
                    "r",
                ).read()
            ),
            title="citros report",
            subtitle=f"[{citros_version}]",
        )
    )
    # action
    action = inquirer.select(
        message="Select Action:",
        choices=[
            Choice("list", name="List: reports list "),
            Choice("generate", name="Generate: new report"),
            Choice("validate", name="Validate: report integrity"),
            # Separator(),
        ],
        default="",
        border=True,
    ).execute()

    if action == "list":
        report_list(args, argv)
    elif action == "generate":
        report_generate(args, argv)
    elif action == "validate":
        report_validate(args, argv)
    else:
        print("[red]Error: unknown action")


def report_list(args, argv):
    try:
        citros = Citros(root=args.dir, verbose=args.verbose, debug=args.debug)
        flat_repo = citros.get_reports_flat()
    except CitrosNotFoundException:
        print(
            f"[red]Error:[/red] {Path(args.dir).expanduser().resolve()} has not been initialized with citros."
        )
        print(Panel.fit(Padding("You may run [green]citros init ", 1), title="help"))
        return

    table = Table(
        title=f"Reports from: [blue]{citros.root_citros / 'reports'}", box=box.SQUARE
    )
    table.add_column("date", style="cyan", no_wrap=False)
    # table.add_column("started_at", style="cyan", no_wrap=True)
    # table.add_column("finished_at", style="cyan", no_wrap=True)
    table.add_column("name", style="magenta", justify="left")
    table.add_column("Versions", justify="left", style="green")
    table.add_column("message", style="magenta", justify="left")
    table.add_column("progress", justify="right", style="green")
    table.add_column("status", style="magenta", justify="left")
    table.add_column(
        "path", style="cyan", justify="left", no_wrap=False, overflow="fold"
    )
    _name = None
    for flat in flat_repo:
        table.add_row(
            flat["started_at"],
            # flat["finished_at"],
            None if flat["name"] == _name else flat["name"],
            flat["version"],
            flat["message"],
            str(flat["progress"]),
            flat["status"],
            str(flat["path"]).removeprefix(os.getcwd()).removeprefix("/"),
            # f"[link={flat['path']}]path[/link]",
        )
        _name = flat["name"]

    console = Console()
    console.print(table)


def report_generate(args, argv):
    """
    Handle the 'generate' command for Citros report.

    :param args.execute: Flag to indicate execution of notebooks.
    :param args.render: Flag to indicate rendering of notebooks to PDF.
    :param args.sign: Flag to indicate signing of PDFs.
    :param args.key_path: Path to the private key file for signing PDFs.
    :param args.notebooks: List of paths to Jupyter notebooks.
    :param args.style_path: Path to the CSS style file, if any.

    :param args.dir
    :param args.name
    :param args.message
    :param args.output: Path to the output folder for generated files.
    """
    # inspect(args)
    try:
        citros = Citros(root=args.dir, verbose=args.verbose, debug=args.debug)
    except CitrosNotFoundException:
        print(
            f"[red]Error:[/red] {Path(args.dir).expanduser().resolve()} has not been initialized with citros."
        )
        print(Panel.fit(Padding("You may run [green]citros init ", 1), title="help"))
        return
    simulation_name = getattr(args, "simulation", None)
    simulation = choose_simulation(
        citros,
        simulation_name,
    )

    batch = citros.get_batch(
        simulation,
        getattr(args, "batch", None),
        getattr(args, "version", None),
    )
    # inspect(batch)
    report = Report(
        name=args.name,
        message=args.message,
        citros=citros,
        output=args.output,
        batch=batch,
        notebooks=args.nb,
        sign=args.sign,
        log=citros.log,
        debug=args.debug,
        verbose=args.verbose,
    )

    # Execute notebooks
    print("[green]Executing notebook...")
    folder = report.run()

    print(f'[green]Report generation completed at [blue]"{folder}"')


def report_validate(args, argv):
    """
    Handle the 'validate' command for Citros report.

    :param args.check: Flag to indicate verification of PDF signatures.
    :param args.public_key_path: Path to the public key file for verification.
    :param args.pdfs: List of paths to PDF files to be verified.
    """

    # Extract arguments
    check_flag = args.check
    public_key_path = args.public_key_path
    pdf_paths = args.pdfs

    # Validate arguments
    if not check_flag:
        print("Error: Check flag is not set.")
        return

    if not public_key_path:
        print("Error: Missing public key for verification.")
        return

    if not pdf_paths:
        print("Error: No PDF paths provided for verification.")
        return

    # Verify PDF signatures
    for pdf_path in pdf_paths:
        if Report.validate(pdf_path, public_key_path):
            print(f"The contents of {pdf_path} are intact.")
        else:
            print(f"Warning: The contents of {pdf_path} may have been altered.")

    print("PDF verification completed.")
