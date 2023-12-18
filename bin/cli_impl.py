import path
import sys
from citros import Citros
from pathlib import Path
from rich import print, inspect, print_json
from rich.rule import Rule
from rich.panel import Panel
from rich.padding import Padding
from rich.logging import RichHandler
from rich.console import Console
from rich.markdown import Markdown
from rich_argparse import RichHelpFormatter
from citros.utils import str_to_bool, suppress_ros_lan_traffic
from citros.batch import Batch
from rich.table import Table
from rich.console import Console
from rich import pretty
from rich import box

import json

pretty.install()


import glob
from .config import config

from citros import CitrosNotFoundException

directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from data_access import data_access as _data_access

from InquirerPy import prompt, inquirer
from prompt_toolkit.validation import Validator, ValidationError


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
            f'[red] "{Path(args.dir).expanduser().resolve()}" has not been initialized. cant run "citros run" on non initialized directory.'
        )
        return

    if args.debug:
        print("[green]done initializing CITROS")

    batch_name = args.batch_name
    batch_message = args.batch_message

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

    simulation = choose_simulation(
        citros,
        args.simulation_name,
    )

    root_rec_dir = f"{args.dir}/.citros/data"
    if config.RECORDINGS_DIR:
        root_rec_dir = config.RECORDINGS_DIR

    batch = Batch(
        root_rec_dir,
        simulation,
        name=batch_name,
        mesaage=batch_message,
        version=args.version,
        verbose=args.verbose,
        debug=args.debug,
    )
    batch.run(
        10,
        args.index,
        ros_domain_id=config.ROS_DOMAIN_ID,
        trace_context=config.TRACE_CONTEXT,
    )


# helper function
def choose_simulation(citros: Citros, simulation_name):
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
    # TODO[critical]: implement data_status
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def simulation_run(args, argv):
    # TODO[critical]: implement data_status
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


####################### parameter setup implementation ##############################
def parameter_setup_new(args, argv):
    # TODO[critical]: implement data_status
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def parameter_setup_list(args, argv):
    # TODO[critical]: implement data_status
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def parameter_setup(args, argv):
    # TODO[critical]: implement data_status
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


############################# DATA implementation ##############################
def data(args, argv):
    # -s simulation
    # -n name
    # -i version index
    # print batch info.
    root = Path(args.dir).expanduser().resolve() / ".citros/data"

    # simulation
    simulations_glob = sorted(glob.glob(f"{str(root)}/*"))
    simulations = []
    for sim in simulations_glob:
        if Path(sim).is_dir():
            simulations.append(str(sim).split("/")[-1])

    if simulations == []:
        print(f"There are currently no simulations in {root} folder.")
        print("Go wild and run as many simulation as you can with CITROS. ")
        print(
            Panel.fit(
                Padding('[green]citros run -n <name>" -m <message', 1),
                title="help",
            )
        )
        return
    chosen_simulation = inquirer.fuzzy(
        message="Select Simulation:", choices=simulations, default="", border=True
    ).execute()

    # batch
    batch_glob = sorted(glob.glob(f"{str(root / chosen_simulation)}/*"))
    batches = []
    for batch in batch_glob:
        if Path(batch).is_dir():
            batches.append(str(batch).split("/")[-1])

    chosen_batch = inquirer.fuzzy(
        message="Select Batch:", choices=batches, default="", border=True
    ).execute()

    # version
    version_glob = sorted(glob.glob(f"{str(root / chosen_simulation/ chosen_batch)}/*"))
    versions = []
    for version in version_glob:
        if Path(version).is_dir():
            versions.append(str(version).split("/")[-1])

    version = inquirer.fuzzy(
        message="Select Version:", choices=versions, default="", border=True
    ).execute()

    root / chosen_simulation / chosen_batch / version

    batch = Batch(
        root,
        chosen_simulation,
        name=chosen_batch,
        debug=args.debug,
        verbose=args.verbose,
    )
    # inspect(batch)
    console = Console()
    console.rule(f"{chosen_simulation} / {chosen_batch} / {version}")
    console.print_json(data=batch.data)

    return


def data_list(args, argv):
    root = Path(args.dir).expanduser().resolve() / ".citros/data"

    table = Table(title=f"Simulation Runs in: [blue]{root}", box=box.SQUARE)
    table.add_column("Simulation", style="cyan", no_wrap=True)
    table.add_column("Run name", style="magenta", justify="center")
    table.add_column("Versions", justify="left", style="green")
    table.add_column("Data", justify="right", style="green")

    simulations = sorted(glob.glob(f"{str(root)}/*"))
    for sim in simulations:
        names = sorted(glob.glob(f"{sim}/*"))
        _simulation = sim.split("/")[-1]
        for name in names:
            versions = sorted(glob.glob(f"{name}/*"))
            _name = name.split("/")[-1]
            for version in versions:
                table.add_row(
                    _simulation,
                    _name,
                    version.split("/")[-1],
                    "TODO!",  # TODO: get summery data from run (size, date, etc.)
                )

                _simulation = None
                _name = None

    console = Console()
    console.print(table)


def data_service(args, argv):
    """
    :param args.dir
    :param args.debug:
    :param args.verbose:
    :param args.project_name:
    """

    root = Path(args.dir).expanduser().resolve() / ".citros/data"
    print(
        Panel.fit(
            f"""started at [green]http://{args.host}:{args.port}[/green].
API: open [green]http://{args.host}:{args.port}/redoc[/green] for documantation
Listening on: [green]{str(root)}""",
            title="[green]CITROS service",
        )
    )

    _data_access(
        str(root),
        time=args.time,
        host=args.host,
        port=int(args.port),
        debug=args.debug,
        verbose=args.verbose,
    )


def data_service_status(args, argv):
    # TODO[critical]: implement data_status
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def data_db_create(args, argv):
    # docker run
    # --name myPostgresDb
    # -p 5455:5432
    # -e POSTGRES_USER=postgresUser
    # -e POSTGRES_PASSWORD=postgresPW
    # -e POSTGRES_DB=postgresDB
    # -d
    # postgres
    import docker
    import subprocess

    subprocess.run(["docker", "run", "ubuntu", "echo hello world"])

    # try:
    #     client = docker.from_env()
    # except Exception as e:
    #     print(
    #         "[red]Docker is not running. Please start docker and try again. exiting..."
    #     )
    #     if args.verbose:
    #         raise e
    #     return
    # client.containers.run("ubuntu", "echo hello world")


def data_db_status(args, argv):
    # TODO[critical]: implement data_create
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def data_db_clean(args, argv):
    # TODO[critical]: implement data_clean
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


############################# REPORT implementation ##############################
def report_generate(args, argv):
    # TODO[critical]: implement report_generate
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def report_validate(args, argv):
    # TODO[critical]: implement report_validate
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")
