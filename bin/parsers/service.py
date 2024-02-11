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


def parser_data_start(parent_subparser, epilog=None):
    description_path = "service/start.md"
    help = "service start"

    parser = parent_subparser.add_parser(
        "start",
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

    parser.add_argument("-dir", default=".", help="The working dir of the project")
    parser.add_argument("-H", "--host", default="0.0.0.0", help="host")
    parser.add_argument("-p", "--port", default="8000", help="post to listen to")
    parser.add_argument("-t", "--time", action="store_true", help="print request times")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=service_start)

    return parser


def parser_data_stop(parent_subparser, epilog=None):
    description_path = "service/stop.md"
    help = "service stop"

    parser = parent_subparser.add_parser(
        "stop",
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
        "-dir", "--dir", default=".", help="The working dir of the project"
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=service_stop)

    return parser


def parser_data_status(parent_subparser, epilog=None):
    description_path = "service/status.md"
    help = "service status"

    parser = parent_subparser.add_parser(
        "status",
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
        "-dir", "--dir", default=".", help="The working dir of the project"
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=service_status)

    return parser


# citros data
def parser_service(main_sub, epilog=None):
    description_path = "service.md"
    help = "service section"

    parser = main_sub.add_parser(
        "service",
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
    parser.add_argument("-dir", default=".", help="The working dir of the project")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=service)

    subsubparser = parser.add_subparsers(dest="type")
    parser_data_start(subsubparser, epilog)
    parser_data_stop(subsubparser, epilog)
    parser_data_status(subsubparser, epilog)

    return parser
