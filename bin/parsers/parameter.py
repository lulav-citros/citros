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
from bin import __version__ as citros_version

install()


# citros parameter setup new
def parser_parameter_setup_new(subparser, epilog=None):
    description_path = "parameter/setup/new.md"
    help = "citros parameter new section"

    parameter_setup_subparser = subparser.add_parser(
        "new",
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
        formatter_class=RichHelpFormatter,
    )
    parameter_setup_subparser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parameter_setup_subparser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parameter_setup_subparser.set_defaults(func=parameter_setup_new)
    return parameter_setup_subparser


# citros parameter setup list
def parser_parameter_setup_list(subparser, epilog=None):
    description_path = "parameter/setup/list.md"
    help = "citros parameter setup list section"

    parameter_setup_subparser = subparser.add_parser(
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
        formatter_class=RichHelpFormatter,
    )
    parameter_setup_subparser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parameter_setup_subparser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parameter_setup_subparser.set_defaults(func=parameter_setup_list)
    return parameter_setup_subparser


# citros parameter setup
def parser_parameter_setup(subparser, epilog=None):
    description_path = "parameter/setup.md"
    help = "citros data create section"

    parser = subparser.add_parser(
        "setup",
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
        formatter_class=RichHelpFormatter,
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=parameter_setup)

    subsubparser = parser.add_subparsers(dest="type")

    parser_parameter_setup_new(subsubparser)
    parser_parameter_setup_list(subsubparser)

    return parser


# citros parameter
def parser_parameter(subparser, epilog=None):
    description_path = "parameter.md"
    help = "simulation section"

    parser = subparser.add_parser(
        "parameter",
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
        formatter_class=RichHelpFormatter,
        aliases=["param"],
    )
    parser.add_argument("-n", "--name", default=None, help="name of parameter")
    parser.add_argument("--package", default=None, help="ilter package")
    parser.add_argument("--node", default=None, help="filter node")
    parser.add_argument("-m", "--match", default=None, help="match parameter pattern")

    subparser = parser.add_subparsers(dest="type")

    # simulation run/list
    parser_parameter_setup(subparser, epilog=epilog)

    return parser
