import os
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
# from report import process_settings, execute_notebooks, render_notebooks_to_pdf, sign_pdf_with_key, verify_pdf_signature

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
    """
    Handle the 'generate' command for Citros report.

    :param args.execute: Flag to indicate execution of notebooks.
    :param args.render: Flag to indicate rendering of notebooks to PDF.
    :param args.sign: Flag to indicate signing of PDFs.
    :param args.key_path: Path to the private key file for signing PDFs.
    :param args.notebooks: List of paths to Jupyter notebooks.
    :param args.style_path: Path to the CSS style file, if any.
    :param args.settings_path: Path to the settings JSON file.
    :param args.output_folder: Path to the output folder for generated files.
    """

    # Extract arguments
    execute_flag = args.execute
    render_flag = args.render
    sign_flag = args.sign
    notebook_paths = args.notebooks
    key_path = args.key_path
    style_path = args.style_path
    settings_path = args.settings_path
    output_folder = args.output_folder

    # Validate arguments
    if not notebook_paths or not output_folder:
        print("Error: Missing notebook paths or output folder.")
        return

    if sign_flag and not key_path:
        print("Error: Missing key for signing.")
        return

    if not settings_path:
        print("Error: Missing settings file.")
        return

    # Process settings
    settings_data = _report.process_settings(settings_path)

    # Execute notebooks
    if execute_flag:
        _report.execute_notebooks(notebook_paths, output_folder)

    # Render notebooks to PDF
    if render_flag:
        _report.render_notebooks_to_pdf(notebook_paths, output_folder, style_path)

    # Sign PDFs
    if sign_flag:
        if not render_flag:
            print("Error: Signing requires notebooks to be rendered to PDF first.")
            return
        pdf_paths = [os.path.join(output_folder, os.path.basename(notebook_path).replace('.ipynb', '.pdf')) for notebook_path in notebook_paths]
        for pdf_path in pdf_paths:
            _report.sign_pdf_with_key(pdf_path, key_path, output_folder)

    print("Report generation completed.")

def report_validate(args, argv):
    """
    Handle the 'validate' command for Citros report.

    :param args.check: Flag to indicate verification of PDF signatures.
    :param args.public_key_path: Path to the public key file for verification.
    :param args.pdfs: List of paths to PDF files to be verified.
    :param args.settings_path: Path to the settings JSON file.
    """

    # Extract arguments
    check_flag = args.check
    public_key_path = args.public_key_path
    pdf_paths = args.pdfs
    settings_path = args.settings_path

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

    if not settings_path:
        print("Error: Missing settings file.")
        return

    # Verify PDF signatures
    for pdf_path in pdf_paths:
        if _report.verify_pdf_signature(pdf_path, public_key_path):
            print(f"The contents of {pdf_path} are intact.")
        else:
            print(f"Warning: The contents of {pdf_path} may have been altered.")

    print("PDF verification completed.")

