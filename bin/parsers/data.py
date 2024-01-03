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
    parser.add_argument(
        "-dir", "--dir", default=".", help="The working dir of the project"
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=data_list)

    return parser


def parser_data_tree(parent_subparser, epilog=None):
    description_path = "data/tree.md"
    help = "data tree section"

    parser = parent_subparser.add_parser(
        "tree",
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
        "-dir", "--dir", default=".", help="The working dir of the project"
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=data_tree)

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


# citros data db init
def parser_data_db_init(parent_subparser, epilog=None):
    description_path = "data/db/init.md"
    help = "data db init section"

    parser = parent_subparser.add_parser(
        "init",
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
    parser.set_defaults(func=data_db_init)

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
def parser_data_db_remove(parent_subparser, epilog=None):
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
    parser.set_defaults(func=data_db_remove)

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
    parser_data_db_init(subparser)
    parser_data_db_status(subparser)
    parser_data_db_stop(subparser)
    parser_data_db_logs(subparser)
    parser_data_db_remove(subparser)

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
    parser_data_tree(subsubparser, epilog)
    parser_data_db(subsubparser, epilog)

    return parser
