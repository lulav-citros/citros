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

directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from data_access import data_access as _data_access

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
    from citros import Citros

    citros = Citros(verbose=args.verbose, debug=args.debug)

    is_project_exists = citros.check_citros_exists()

    success = citros.init()
    if success:
        if is_project_exists:
            print(
                f"[green]The directory {Path(args.dir).resolve()} has already been initialized."
            )
        else:
            print(f"[green]Intialized Citros repository.")
    else:
        print(f"[red]Could not initialize citros.")


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

    citros = Citros(verbose=args.verbose, debug=args.debug)

    is_project_exists = citros.check_citros_exists()
    if not is_project_exists:
        print(
            f"[red]The directory {Path(args.dir).resolve()} has not been initialized with CITROS."
        )
        print('  (use "citros init" to init the directory)')
        return

    success = citros.check_project()
    if not success:
        print(f"[red].citros is corappted :(")
        print(f"Fix the errors in your project configuration files and try again.")

    success = citros.check_batch_name_and_message(args.batch_name, args.batch_message)
    if not success:
        print(f"[yellow]Please try again with all required command parameters.")
        return

    if not args.lan_traffic:
        citros.utils.suppress_ros_lan_traffic()

    if args.simulation_name:
        citros.run_simulation(args.simulation_name, args.completions)
    else:
        # simulation is chosen by the user
        run_interactively(citros, args.completions)


def generate_question(type, name, message, choices=None, validator=None, filter=None):
    if type not in [
        "list",
        "raw_list",
        "expand",
        "confirm",
        "check_box",
        "input",
        "password",
        "editor",
    ]:
        print("question type not supported.")
        return {}

    if type == "list":
        if not choices:
            print("Nothing to choose from.")
            return {}
        return {"type": type, "name": name, "message": message, "choices": choices}
    elif type == "input":
        return {
            f"type": type,
            f"name": name,
            f"message": message,
            f"validate": validator,
            f"filter": filter,
        }
    else:
        raise NotImplementedError()


def run_interactively(citros: Citros, completions, commit_hash, branch_name):
    sim_names = citros.get_simulations()

    # sanity check - should never happen because internal_sync will fail if there
    #                isn't at least one simulation file.
    if not sim_names:
        print(
            f"[red]There are currently no simulations in your {citros.SIMS_DIR} folder. \
                	 Please create at least one simulation for your project."
        )
        return

    sim_names_q = generate_question(
        "list", "sim_names", "Please choose the simulation you wish to run:", sim_names
    )
    # completions_q = generate_question("input", "completions", "Please enter number of completions:",
    #                                  NumberValidator, lambda val: int(val))
    answers = prompt([sim_names_q])  # use default style
    sim_name = answers.get("sim_names")

    citros.run_simulation(sim_name, completions, commit_hash, branch_name)


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
            f"""[green]CITROS[/green] started data-access service at [green]http://{args.host}:{args.port}.
API: open [green]http://{args.host}:{args.port}/redoc[/green] for documantation"""
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
    # TODO[critical]: implement report_generate
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def report_validate(args, argv):
    # TODO[critical]: implement report_validate
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")
