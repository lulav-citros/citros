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


# citros simulation
def parser_launch(subparser, epilog=None):
    description_path = "launch.md"
    help = "launch section"

    parser = subparser.add_parser(
        "launch",
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
    parser.add_argument("-n", "--name", default=None, help="name of simulation")
    parser.add_argument("-m", "--match", default=None, help="match simulation pattern")

    subparser = parser.add_subparsers(dest="type")

    return parser
