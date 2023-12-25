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


# citros data list
def parser_data_list(parent_subparser, epilog=None):
    description_path = "data/list.md"
    help = "data list section"

    parser = parent_subparser.add_parser(
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
    parser.add_argument("-dir", default=".", help="The working dir of the project")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=data_list)

    return parser


# citros data service status
def parser_data_service_status(parent_subparser, epilog=None):
    description_path = "data/service/status.md"
    help = "data service status section"

    parser = parent_subparser.add_parser(
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
        formatter_class=RichHelpFormatter,
    )

    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=data_service_status)

    subparser = parser.add_subparsers(dest="type")

    return parser


# citros data service
def parser_data_service(parent_subparser, epilog=None):
    description_path = "data/service.md"
    help = "data service section"

    parser = parent_subparser.add_parser(
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
        formatter_class=RichHelpFormatter,
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
    parser.set_defaults(func=data_service)

    subparser = parser.add_subparsers(dest="type")

    parser_data_service_status(subparser)

    return parser


# citros data db create
def parser_data_db_create(parent_subparser, epilog=None):
    description_path = "data/db/create.md"
    help = "data db create section"

    parser = parent_subparser.add_parser(
        "create",
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
    parser.set_defaults(func=data_db_create)

    # subparser = parser.add_subparsers(dest="type")

    return parser


# citros data db status
def parser_data_db_status(parent_subparser, epilog=None):
    description_path = "data/db/status.md"
    help = "data db status section"

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
        formatter_class=RichHelpFormatter,
    )

    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=data_db_status)

    # subparser = parser.add_subparsers(dest="type")

    return parser


# citros data db stop
def parser_data_db_stop(parent_subparser, epilog=None):
    description_path = "data/db/stop.md"
    help = "data db stop section"

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
        formatter_class=RichHelpFormatter,
    )

    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=data_db_stop)

    # subparser = parser.add_subparsers(dest="type")

    return parser


# citros data db logs
def parser_data_db_logs(parent_subparser, epilog=None):
    description_path = "data/db/logs.md"
    help = "data db logs section"

    parser = parent_subparser.add_parser(
        "logs",
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
    parser.set_defaults(func=data_db_logs)

    # subparser = parser.add_subparsers(dest="type")

    return parser


# citros data db clean
def parser_data_db_clean(parent_subparser, epilog=None):
    description_path = "data/db/clean.md"
    help = "data db clean section"

    parser = parent_subparser.add_parser(
        "clean",
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
    parser.set_defaults(func=data_db_clean)

    # subparser = parser.add_subparsers(dest="type")

    return parser


# citros data db
def parser_data_db(parent_subparser, epilog=None):
    description_path = "data/db.md"
    help = "data db section"

    parser = parent_subparser.add_parser(
        "db",
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
    parser.set_defaults(func=data_db)

    subparser = parser.add_subparsers(dest="type")

    parser_data_db_create(subparser)
    parser_data_db_status(subparser)
    parser_data_db_stop(subparser)
    parser_data_db_logs(subparser)
    parser_data_db_clean(subparser)

    return parser


# citros data
def parser_data(main_sub, epilog=None):
    description_path = "data.md"
    help = "data section"

    parser = main_sub.add_parser(
        "data",
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
    parser.add_argument("-dir", default=".", help="The working dir of the project")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=data)

    subsubparser = parser.add_subparsers(dest="type")
    parser_data_list(subsubparser, epilog)
    parser_data_service(subsubparser, epilog)
    parser_data_db(subsubparser, epilog)

    return parser
