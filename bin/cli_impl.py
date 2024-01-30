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


keybindings = {
    "skip": [{"key": "c-c"}, {"key": "escape"}],
}


def exit_citros_cli():
    print("[green]Bye👋")
    exit(0)


def citros(args, argv):
    # action
    action = inquirer.select(
        raise_keyboard_interrupt=False,
        mandatory=False,
        keybindings=keybindings,
        message="Select Action:",
        choices=[
            Choice("init", name="🍋 Init: initialize .citros in current directory"),
            Choice("run", name="🔥 Run: new simulation"),
            Choice("data", name="📊 Data: for data management "),
            Choice("report", name="📝 Report: generation and management"),
            Choice("service", name="🔖 Service: CITROS API service functions"),
            Separator(),
            Choice("exit", name="EXIT"),
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
    elif action == "init":
        init(args, argv)
    elif action == "service":
        service(args, argv)
    elif action == "exit":
        exit_citros_cli()
    elif action is None:
        exit_citros_cli()
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
    # inspect(args)
    is_interactive = False
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

    if not hasattr(args, "batch_name") or args.batch_name is None:
        is_interactive = True
        batch_name = Prompt.ask("Please name this batch run", default="citros")
    else:
        batch_name = args.batch_name

    if not hasattr(args, "batch_message") or args.batch_message is None:
        batch_message = Prompt.ask(
            "Enter a message for this batch run",
            default="This is a default batch message from citros",
        )
    else:
        batch_message = args.batch_message

    if is_interactive or not hasattr(args, "completions"):
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

    batch_version = getattr(args, "version", None)
    batch_index = getattr(args, "index", -1)

    console = Console()
    console.rule(f"command")
    print(
        f'[white]citros run --dir {args.dir} --batch_name {batch_name} --batch_message "{batch_message}" --simulation_name {simulation_name} {"--version " + batch_version if batch_version is not None else ""} --completions {completions} --index {batch_index}'
    )
    console.rule(f"")

    batch = Batch(
        root_rec_dir,
        simulation,
        name=batch_name,
        message=batch_message,
        version=batch_version,
        verbose=args.verbose,
        debug=args.debug,
    )
    try:
        batch.run(
            completions,
            batch_index,
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
        except Exception as e:
            citros.logger.debug(e)
            if args.verbose == True:
                print(e)

            print(f"[red]Error:[/red] Failed to upload data to DB {type(e).__name__}.")

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


############################# Simulation implementation ##############################
# TODO[critical]: implement
def simulation_list(args, argv):
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


# TODO[critical]: implement
def simulation_run(args, argv):
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


####################### parameter setup implementation ##############################
# TODO[critical]: implement
def parameter_setup_new(args, argv):
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


# TODO[critical]: implement
def parameter_setup_list(args, argv):
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


# TODO[critical]: implement
def parameter_setup(args, argv):
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


############################# DATA implementation ##############################
def data(args, argv):
    action = inquirer.select(
        raise_keyboard_interrupt=False,
        mandatory=False,
        keybindings=keybindings,
        message="Select Action:",
        choices=[
            Choice("tree", name="🌲 Tree: tree view of data"),
            Choice("list", name="*️⃣  List: reports list"),
            Choice("db", name="📂 DB: section"),
            Choice("service", name="🗳  Service: section"),
            Separator(),
            Choice("exit", name="EXIT"),
        ],
        default="",
        border=True,
    ).execute()

    if action is None:
        exit_citros_cli()

    if action == "tree":
        data_tree(args, argv)
    elif action == "list":
        data_list(args, argv)
    elif action == "db":
        data_db(args, argv)
    elif action == "service":
        service(args, argv)
    elif action == "exit":
        exit_citros_cli()
    else:
        print("[red]Error: unknown action")
    return


def data_tree(args, argv):
    """
    choose a batch run then choose an action to perform on the batch run.

    Args:
        args: The command-line arguments passed to the function.
        argv: The list of command-line arguments.

    Returns:
        None
    """

    try:
        citros = Citros(root=args.dir, verbose=args.verbose, debug=args.debug)
    except CitrosNotFoundException:
        print(
            f"[red]Error:[/red] {Path(args.dir).expanduser().resolve()} has not been initialized with citros."
        )
        print(Panel.fit(Padding("You may run [green]citros init ", 1), title="help"))
        return

    chosen_simulation, chosen_batch, version = choose_batch(
        citros.root_citros,
        simulation_name=getattr(args, "simulation", None),
        batch_name=getattr(args, "batch", None),
        version=getattr(args, "version", None),
    )

    setattr(args, "simulation", chosen_simulation)
    setattr(args, "batch", chosen_batch)
    setattr(args, "version", version)

    # action
    action = inquirer.select(
        raise_keyboard_interrupt=False,
        mandatory=False,
        keybindings=keybindings,
        message="Select Action:",
        choices=[
            Choice("info", name="Info"),
            Choice("load", name="Load"),
            Choice("unload", name="Unload"),
            Choice("delete", name="Delete"),
            Separator(),
            Choice("exit", name="EXIT"),
        ],
        default="",
        border=True,
    ).execute()

    if action is None:
        exit_citros_cli()

    if action == "info":
        data_info(args, argv)
    elif action == "load":
        data_load(args, argv)
    elif action == "unload":
        data_unload(args, argv)
    elif action == "delete":
        data_delete(args, argv)
    elif action == "exit":
        exit_citros_cli()
    else:
        print("[red]Error: unknown action")


def data_list(args, argv):
    """
    List simulation runs and their details.

    Returns:
        None
    """

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
            str(flat_batch["path"]).removeprefix(os.getcwd()).removeprefix("/"),
        )

    console = Console()
    console.print(table)


def data_info(args, argv):
    """
    Handle the 'info' command for Citros data.

    :param args.simulation: simulation name
    :param args.batch: batch name
    :param args.version: batch_version

    :param args.debug: Flag to indicate debug mode.
    :param args.verbose: Flag to indicate verbose console prints.
    """
    try:
        citros = Citros(root=args.dir, verbose=args.verbose, debug=args.debug)
    except CitrosNotFoundException:
        print(
            f"[red]Error:[/red] {Path(args.dir).expanduser().resolve()} has not been initialized with citros."
        )
        print(Panel.fit(Padding("You may run [green]citros init ", 1), title="help"))
        return

    chosen_simulation, chosen_batch, version = choose_batch(
        citros.root_citros,
        simulation_name=getattr(args, "simulation", None),
        batch_name=getattr(args, "batch", None),
        version=getattr(args, "version", None),
    )

    batch = citros.get_batch(
        simulation=chosen_simulation, name=chosen_batch, version=version
    )

    console = Console()
    console.rule(f".citros/data/{chosen_simulation}/{chosen_batch}/{version}/info.json")
    console.print_json(data=batch.data)
    console.rule(f"")


def data_load(args, argv):
    """
    Handle the 'load' command for Citros data. loads tha batch to citros postgres DB instance.

    :param args.simulation: simulation name
    :param args.batch: batch name
    :param args.version: batch_version

    :param args.debug: Flag to indicate debug mode.
    :param args.verbose: Flag to indicate verbose console prints.
    """
    try:
        citros = Citros(root=args.dir, verbose=args.verbose, debug=args.debug)
    except CitrosNotFoundException:
        print(
            f"[red]Error:[/red] {Path(args.dir).expanduser().resolve()} has not been initialized with citros."
        )
        print(Panel.fit(Padding("You may run [green]citros init ", 1), title="help"))
        return

    chosen_simulation, chosen_batch, version = choose_batch(
        citros.root_citros,
        simulation_name=getattr(args, "simulation", None),
        batch_name=getattr(args, "batch", None),
        version=getattr(args, "version", None),
    )
    print(f"Uploading data to DB... { chosen_simulation} / {chosen_batch} / {version}")
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


def data_unload(args, argv):
    """
    Handle the 'unload' command for Citros data. unloads tha batch to citros postgres DB instance.

    :param args.simulation: simulation name
    :param args.batch: batch name
    :param args.version: batch_version

    :param args.debug: Flag to indicate debug mode.
    :param args.verbose: Flag to indicate verbose console prints.
    """
    try:
        citros = Citros(root=args.dir, verbose=args.verbose, debug=args.debug)
    except CitrosNotFoundException:
        print(
            f"[red]Error:[/red] {Path(args.dir).expanduser().resolve()} has not been initialized with citros."
        )
        print(Panel.fit(Padding("You may run [green]citros init ", 1), title="help"))
        return

    chosen_simulation, chosen_batch, version = choose_batch(
        citros.root_citros,
        simulation_name=getattr(args, "simulation", None),
        batch_name=getattr(args, "batch", None),
        version=getattr(args, "version", None),
    )
    print(
        f"Dropping data from DB... { chosen_simulation } / {chosen_batch} / {version}"
    )
    batch = citros.get_batch(
        simulation=chosen_simulation, name=chosen_batch, version=version
    )

    batch.unload()


def data_delete(args, argv):
    """
    Handle the 'delete' command for Citros data. delete batch from filesystem and DB.

    :param args.simulation: simulation name
    :param args.batch: batch name
    :param args.version: batch_version

    :param args.debug: Flag to indicate debug mode.
    :param args.verbose: Flag to indicate verbose console prints.
    """
    try:
        citros = Citros(root=args.dir, verbose=args.verbose, debug=args.debug)
    except CitrosNotFoundException:
        print(
            f"[red]Error:[/red] {Path(args.dir).expanduser().resolve()} has not been initialized with citros."
        )
        print(Panel.fit(Padding("You may run [green]citros init ", 1), title="help"))
        return

    chosen_simulation, chosen_batch, version = choose_batch(
        citros.root_citros,
        simulation_name=getattr(args, "simulation", None),
        batch_name=getattr(args, "batch", None),
        version=getattr(args, "version", None),
    )
    print(f"deleting data from { chosen_simulation } / {chosen_batch} / {version}")
    citros.delete_batch(
        simulation=chosen_simulation, name=chosen_batch, version=version
    )


def data_db(args, argv):
    action = inquirer.select(
        raise_keyboard_interrupt=False,
        mandatory=False,
        keybindings=keybindings,
        message="Select Action:",
        choices=[
            Choice(
                "create", name="▶ Create: create citros db instance and initializes it."
            ),
            Choice("remove", name="🗑  Remove: remove the db instance."),
            Choice("init", name="✏  Init: initialize the db instance"),
            Choice("logs", name="📝 Logs: show logs of DB instance"),
            Choice("status", name="❓ Status: Show weather the serivce is up or not"),
            Choice("stop", name="⏹  Stop: stops the citros db instance if running."),
            Separator(),
            Choice("exit", name="EXIT"),
        ],
        default="",
        border=True,
    ).execute()

    if action is None:
        exit_citros_cli()

    if action == "create":
        data_db_create(args, argv)
    elif action == "remove":
        data_db_remove(args, argv)
    elif action == "init":
        data_db_init(args, argv)
    elif action == "logs":
        data_db_logs(args, argv)
    elif action == "status":
        data_db_status(args, argv)
    elif action == "stop":
        data_db_stop(args, argv)
    elif action == "exit":
        exit_citros_cli()
    else:
        print("[red]Error: unknown action")


def _init_db(verbose, debug):
    """
    initializing the DB
    """
    from citros import CitrosDB_old

    citrosDB = CitrosDB_old(
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
    # TODO: check container status instead of sleep.
    sleep(3)
    data_db_init(args, argv)
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

    try:
        container = client.containers.get(config.DB_CONTAINER_NAME)
    except docker.errors.NotFound:
        print(
            f"Docker container {config.DB_CONTAINER_NAME} not found!, probably not running or not it this env."
        )
        print(f"[red]Please run 'citros data db create' to create a new DB.")

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


def data_db_remove(args, argv):
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
            print("[red]CITROS DB is running. Please stop it before clearing.")
            print(
                Panel.fit(
                    Padding('You may run [green]"citros data db stop" ', 1),
                    title="help",
                )
            )
        else:
            raise e


############################# Service implementation ##############################
def service(args, argv):
    action = inquirer.select(
        raise_keyboard_interrupt=False,
        mandatory=False,
        keybindings=keybindings,
        message="Select Action:",
        choices=[
            Choice("start", name="▶  Start: starts CITROS API serivce."),
            Choice("stop", name="⏹  Stop: Stops the CITROS API service."),
            Choice("status", name="❓ Status: Show CITROS API status."),
            Separator(),
            Choice("exit", name="EXIT"),
        ],
        default="",
        border=True,
    ).execute()

    if action is None:
        exit_citros_cli()

    if action == "start":
        service_start(args, argv)
    elif action == "stop":
        service_stop(args, argv)
    elif action == "status":
        service_status(args, argv)
    elif action == "exit":
        exit_citros_cli()
    else:
        print("[red]Error: unknown action")


def service_start(args, argv):
    """
    :param args.dir
    :param args.debug:
    :param args.verbose:
    :param args.project_name:
    """
    from citros import data_access_service, NoDataFoundException

    host = getattr(args, "host", "0.0.0.0")
    port = getattr(args, "port", "8000")
    time = getattr(args, "time", False)

    root = Path(args.dir).expanduser().resolve() / ".citros/data"
    print(
        Panel.fit(
            f"""started at [green]http://{host}:{port}[/green].
API: open [green]http://{host}:{port}/redoc[/green] for documantation
Listening on: [green]{str(root)}""",
            title="[green]CITROS service",
        )
    )
    try:
        # TODO[important]: make async
        data_access_service(
            str(root),
            time=time,
            host=host,
            port=int(port),
            debug=args.debug,
            verbose=args.verbose,
        )
    except NoDataFoundException:
        print(
            f'[red] "{Path(args.dir).expanduser().resolve()}" has not been initialized. cant run "citros data service" on non initialized directory.'
        )
        return


# TODO[important]: implement
def service_stop(args, argv):
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


# TODO[important]: implement  after making this sevice async. return status of service.
def service_status(args, argv):
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


############################# Reports implementation ##############################


def report(args, argv):
    # inspect(args)
    # print(
    #     Panel(
    #         Markdown(
    #             open(
    #                 importlib_resources.files(f"data.doc.cli").joinpath("report.md"),
    #                 "r",
    #             ).read()
    #         ),
    #         title="citros report",
    #         subtitle=f"[{citros_version}]",
    #     )
    # )
    # action
    action = inquirer.select(
        raise_keyboard_interrupt=False,
        mandatory=False,
        keybindings=keybindings,
        message="Select Action:",
        choices=[
            Choice("list", name="*️⃣  List: reports list "),
            Choice("generate", name="⚡ Generate: new report"),
            Choice("validate", name="❓ Validate: report integrity"),
            Separator(),
            Choice("exit", name="EXIT"),
        ],
        default="",
        border=True,
    ).execute()

    if action is None:
        exit_citros_cli()

    if action == "list":
        report_list(args, argv)
    elif action == "generate":
        report_generate(args, argv)
    elif action == "validate":
        report_validate(args, argv)
    elif action == "exit":
        exit_citros_cli()
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

    simulation, batch_name, version = choose_batch(
        citros.root_citros,
        simulation_name=getattr(args, "simulation", None),
        batch_name=getattr(args, "batch", None),
        version=getattr(args, "version", None),
    )

    if not hasattr(args, "name") or args.name is None:
        report_name = Prompt.ask("Please name this report", default="citros")
    else:
        report_name = args.name

    if not hasattr(args, "message") or args.message is None:
        report_message = Prompt.ask(
            "Enter a message for this report",
            default="This is a default report message from citros",
        )
    else:
        report_message = args.message

    if not hasattr(args, "output"):
        output = None
    else:
        output = args.output

    if not hasattr(args, "notebooks"):
        notebook_list = []
        for notebook in glob.glob(f"{os.getcwd()}/**/*.ipynb", recursive=True):
            notebook_list.append(notebook.removeprefix(os.getcwd()).removeprefix("/"))

        notebooks = inquirer.select(
            raise_keyboard_interrupt=False,
            mandatory=False,
            keybindings=keybindings,
            message="Select notebook:",
            choices=notebook_list,
            border=True,
            multiselect=True,
            instruction="Use [space] to select notebooks, [enter] to confirm selection.",
            mandatory_message="Please select at least one notebook",
        ).execute()

        # print(f"chosen_notebooks: {notebooks}")

    else:
        notebooks = args.notebooks

    if not hasattr(args, "sign"):
        sign = False  # TODO: change to True and sign!
    else:
        sign = args.sign

    batch = citros.get_batch(
        simulation,
        batch_name,
        version,
    )
    # inspect(batch)
    # print(
    #     f"report_name={report_name}, report_message={report_message}, output={output}, sign={sign}"
    # )
    report = Report(
        name=report_name,
        message=report_message,
        citros=citros,
        output=output,
        batch=batch,
        notebooks=notebooks,
        sign=sign,
        log=citros.log,
        debug=args.debug,
        verbose=args.verbose,
    )

    # if args.debug:
    console = Console()
    console.rule(f"command")
    print(
        f'[white]citros report generate {"--output " + str(output) if output is not None else ""} {" ".join(["-nb " + str(nb) for nb in notebooks])} --dir {args.dir} --simulation {simulation} --batch {batch_name} --version {version} --name {report_name} --message "{report_message}" {"--sign" if sign else ""} '
    )
    console.rule(f"")

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


## Utils


def choose_batch(
    root_citros: Path, simulation_name=None, batch_name=None, version=None
):
    data_root = root_citros / "data"

    chosen_simulation = simulation_name
    if chosen_simulation is None:
        simulations = []
        for simulation_path in glob.glob(f"{data_root}/[!_]*/"):
            if simulation_path.endswith("/"):
                simulation_path = simulation_path[:-1]
            simulation = simulation_path.split("/")[-1]
            simulations.append(simulation)
        # print(f"simulations: {simulations}")
        if simulations == []:
            print("[yellow]Warning: No simulations found. Please create a simulation.")
            exit_citros_cli()
        chosen_simulation = inquirer.select(
            raise_keyboard_interrupt=False,
            mandatory=False,
            keybindings=keybindings,
            message="Select Simulation:",
            choices=simulations,
            default="",
            border=True,
        ).execute()
    # print(f"chosen_simulation: {chosen_simulation}")
    if chosen_simulation is None:
        exit_citros_cli()

    chosen_batch = batch_name
    if chosen_batch is None:
        batch_list = []
        for batch_path in glob.glob(f"{data_root}/{chosen_simulation}/[!_]*/"):
            if batch_path.endswith("/"):
                batch_path = batch_path[:-1]
            batch_name = batch_path.split("/")[-1]
            batch_list.append(batch_name)

        chosen_batch = inquirer.select(
            raise_keyboard_interrupt=False,
            mandatory=False,
            keybindings=keybindings,
            message="Select Batch:",
            choices=batch_list,
            default="",
            border=True,
        ).execute()

    # print(f"chosen_batch: {chosen_batch}")

    if chosen_batch is None:
        exit_citros_cli()

    chosen_version = version
    if chosen_version is None:
        version_list = []
        for version_path in glob.glob(
            f"{data_root}/{chosen_simulation}/{chosen_batch}/[!_]*/"
        ):
            if version_path.endswith("/"):
                version_path = version_path[:-1]
            version = version_path.split("/")[-1]
            version_list.append(version)
        if version_list == []:
            print("[yellow]Warning: No versions found for this batch.")
            exit_citros_cli()
        chosen_version = inquirer.select(
            raise_keyboard_interrupt=False,
            mandatory=False,
            keybindings=keybindings,
            message="Select Version:",
            choices=sorted(version_list, reverse=True),
            default="",
            border=True,
        ).execute()

    if chosen_version is None:
        exit_citros_cli()

    return chosen_simulation, chosen_batch, chosen_version
