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


def parser_init(main_sub, epilog=None):
    parser = main_sub.add_parser(
        "init",
        description=Panel(
            Markdown(
                open(
                    importlib_resources.files(f"data.doc").joinpath("init.md"), "r"
                ).read()
            ),
            subtitle=f"[{citros_version}]",
        ),
        epilog=epilog,
        help="init section",
        formatter_class=RichHelpFormatter,
    )
    parser.add_argument("-dir", default=".", help="The working dir of the project")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=init)
