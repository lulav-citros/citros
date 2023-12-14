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

from .config import config

from citros import CitrosNotFoundException

directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from data_access import data_access as _data_access
from report import report as _report

from InquirerPy import prompt
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
    :param args.run_id:
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
        print(f'[red] "{Path(args.dir).expanduser().resolve()}" has not been initialized. cant run "citros run" on non initialized directory.')
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
        mesaage=batch_message
    )
    batch.run(
        10, 
        ros_domain_id=config.ROS_DOMAIN_ID,
        trace_context=config.TRACE_CONTEXT
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


############################# Simulation implementation ##############################
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
    # TODO[critical]: implement data_status
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def data_list(args, argv):
    # TODO[critical]: implement data_status
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def data_service(args, argv):
    """
    :param args.dir
    :param args.debug:
    :param args.verbose:
    :param args.project_name:
    """

    # print(Panel(Markdown(open("bin/data.md", "r").read()), title="[green]CITROS", subtitle=f"[{citros_version}]"))
    print(
        Panel.fit(
            f"""started at [green]http://{args.host}:{args.port}[/green].
API: open [green]http://{args.host}:{args.port}/redoc[/green] for documantation""",
            title="[green]CITROS service",
        )
    )
    _data_access(args, argv)


def data_service_status(args, argv):
    # TODO[critical]: implement data_status
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def data_db_create(args, argv):
    # TODO[critical]: implement data_status
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def data_db_status(args, argv):
    # TODO[critical]: implement data_create
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def data_db_clean(args, argv):
    # TODO[critical]: implement data_clean
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


############################# REPORT implementation ##############################

def report_generate(args, argv):
    print('ARGS:')
    print(args)
    
    report_args = []
    paths = args.paths
    current_index = 0

    if args.execute:
        report_args.append('-e')

    if args.render:
        report_args.append('-r')

    if args.sign:
        report_args.append('-s')
        key_path = paths[current_index]
        if not key_path:
            print("Error: Missing key for signing.")
            return
        report_args.append(key_path)
        current_index += 1

    notebook_paths = paths[current_index:-3] 
    style_path = None
    settings_path = None
    output_folder = None

    if args.render:
        style_path = paths[-3]
        current_index += 1

    settings_path = paths[-2]
    output_folder = paths[-1]

    report_args.extend(notebook_paths)
    if style_path:
        report_args.append(style_path)
    report_args.append(settings_path)
    report_args.append(output_folder)

    _report(report_args)

def report_validate(args, argv):
    check_flag = '-c' if args.check else ''
    paths = args.paths 

    if not paths:
        print("Error: No paths provided for validation.")
        sys.exit(1)

    key_path = paths[0]
    pdf_paths_to_check = paths[1:]

    if not key_path:
        print("Error: Missing key for validation.")
        sys.exit(1)

    if not pdf_paths_to_check:
        print("Error: No PDF paths provided for validation.")
        sys.exit(1)

    validate_args = [check_flag, key_path] + pdf_paths_to_check
    validate_args = [arg for arg in validate_args if arg]

    _report(validate_args)
