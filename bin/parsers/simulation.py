import argparse
import importlib_resources
from bin.cli_impl import *
from rich import print, inspect, print_json
from rich.rule import Rule
from rich.panel import Panel
from rich.padding import Padding
from rich.logging import RichHandler
from rich.console import Console
from rich.markdown import Markdown
from rich.traceback import install
from bin import __version__ as citros_version
from .formatter import RichHelpFormatterCitros

install()


# citros simulation run
def parser_simulation_run(subparser, epilog=None):
    description_path = "simulation/run.md"
    help = "citros data create section"
    parser = subparser.add_parser(
        "run",
        description=Panel(
            Markdown(
                open(
                    importlib_resources.files(f"data.doc.cli").joinpath(
                        description_path
                    ),
                    "r",
                ).read()
            ),
            subtitle=f"[{citros_version}]",
            title="description",
        ),
        epilog=epilog,
        help=help,
        formatter_class=RichHelpFormatterCitros,
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=simulation_run)

    return parser


# citros simulation list
def parser_simulation_list(subparser, epilog=None):
    description_path = "simulation/list.md"
    help = "citros data status section"
    parser = subparser.add_parser(
        "list",
        description=Panel(
            Markdown(
                open(
                    importlib_resources.files(f"data.doc.cli").joinpath(
                        description_path
                    ),
                    "r",
                ).read()
            ),
            subtitle=f"[{citros_version}]",
            title="description",
        ),
        epilog=epilog,
        help=help,
        formatter_class=RichHelpFormatterCitros,
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=simulation_list)
    return parser


# citros simulation
def parser_simulation(subparser, epilog=None):
    description_path = "simulation.md"
    help = "simulation section"
    parser = subparser.add_parser(
        "simulation",
        description=Panel(
            Markdown(
                open(
                    importlib_resources.files(f"data.doc.cli").joinpath(
                        description_path
                    ),
                    "r",
                ).read()
            ),
            subtitle=f"[{citros_version}]",
            title="description",
        ),
        epilog=epilog,
        help=help,
        formatter_class=RichHelpFormatterCitros,
        aliases=["sim"],
    )
    parser.add_argument("-n", "--name", default=None, help="name of simulation")
    parser.add_argument("-m", "--match", default=None, help="match simulation pattern")

    subparser = parser.add_subparsers(dest="type")
    # simulation run/list
    parser_simulation_run(subparser, epilog=epilog)
    parser_simulation_list(subparser, epilog=epilog)

    return parser
