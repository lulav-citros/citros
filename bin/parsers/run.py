import argparse
import importlib_resources
from bin.cli_impl import *
from rich_argparse import RichHelpFormatter
from rich import print, inspect, print_json
from rich.rule import Rule
from rich.panel import Panel
from rich.padding import Padding
from rich.logging import RichHandler
from rich.console import Console
from rich.markdown import Markdown
from rich_argparse import RichHelpFormatter
from rich.traceback import install

install()
from bin import __version__ as citros_version


def parser_run(main_sub, epilog=None):
    parser = main_sub.add_parser(
        "run",
        description=Panel(
            Markdown(
                open(
                    importlib_resources.files(f"data.doc.cli").joinpath("run.md"), "r"
                ).read()
            ),
        ),
        epilog=epilog,
        help="run section",
        formatter_class=RichHelpFormatter,
    )
    parser.add_argument("-dir", default=".", help="The working dir of the project")
    parser.add_argument(
        "-n", "--batch_name", nargs="?", default=None, help="a name for the run"
    )
    parser.add_argument(
        "-m", "--batch_message", nargs="?", default=None, help="a message for the run"
    )
    parser.add_argument(
        "-l",
        "--lan_traffic",
        action="store_true",
        help="receive LAN ROS traffic in your simulation.",
    )
    parser.add_argument(
        "-s", "--simulation_name", nargs="?", default=None, help="Simulation name"
    )

    parser.add_argument(
        "--version",
        nargs="?",
        default=None,
        help="the batch run version. .citros/data/{sim_name}/{batch_name}/{ **batch_version** }/{sid}",
    )

    parser.add_argument(
        "-c",
        "--completions",
        nargs="?",
        default=1,
        help="number of times to run the simulation",
    )
    parser.add_argument(
        "-i",
        "--index",
        nargs="?",
        default=-1,
        help="the pard of the batch. if -1 will run all the batch",
    )

    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=run)
