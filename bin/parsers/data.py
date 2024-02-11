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


# citros data list
def parser_data_list(parent_subparser, epilog=None):
    description_path = "data/list.md"
    help = "Will list all recorded batches under .citros/data folder as a table"

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
    parser.set_defaults(func=data_list)

    return parser


def parser_data_tree(parent_subparser, epilog=None):
    description_path = "data/tree.md"
    help = "Will list all recorded batches under .citros/data folder in a tree view"

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
    parser.set_defaults(func=data_tree)

    subsubparser = parser.add_subparsers(dest="type")
    parser_data_tree_info(subsubparser, epilog)
    parser_data_tree_load(subsubparser, epilog)
    parser_data_tree_unload(subsubparser, epilog)
    parser_data_tree_delete(subsubparser, epilog)

    return parser


# citros data tree load
def parser_data_tree_info(parent_subparser, epilog=None):
    description_path = "data/tree/info.md"
    help = "will show batch info "

    parser = parent_subparser.add_parser(
        "info",
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
    parser.add_argument("-s", "--simulation", help="simulation name")
    parser.add_argument("-b", "--batch", default="citros", help="batch name")
    parser.add_argument("--version", help="batch version ")

    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=data_info)

    return parser


# citros data tree load
def parser_data_tree_load(parent_subparser, epilog=None):
    description_path = "data/tree/load.md"
    help = "will load the batch to db"

    parser = parent_subparser.add_parser(
        "load",
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
    parser.add_argument("-s", "--simulation", help="simulation name")
    parser.add_argument("-b", "--batch", default="citros", help="batch name")
    parser.add_argument("--version", help="batch version ")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=data_load)

    return parser


# citros data tree load
def parser_data_tree_unload(parent_subparser, epilog=None):
    description_path = "data/tree/unload.md"
    help = "will unload the batch from db"

    parser = parent_subparser.add_parser(
        "unload",
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
    parser.add_argument("-s", "--simulation", help="simulation name")
    parser.add_argument("-b", "--batch", default="citros", help="batch name")
    parser.add_argument("--version", help="batch version ")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=data_unload)

    return parser


# citros data tree load
def parser_data_tree_delete(parent_subparser, epilog=None):
    description_path = "data/tree/delete.md"
    help = "will delete the batch"

    parser = parent_subparser.add_parser(
        "delete",
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
    parser.add_argument("-s", "--simulation", help="simulation name")
    parser.add_argument("-b", "--batch", default="citros", help="batch name")
    parser.add_argument("--version", help="batch version ")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=data_delete)

    return parser


# citros data db create
def parser_data_db_create(parent_subparser, epilog=None):
    description_path = "data/db/create.md"
    help = "Create and init new DB docker instance"

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
        formatter_class=RichHelpFormatterCitros,
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
    help = "initialize DB for use with citros."

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
        formatter_class=RichHelpFormatterCitros,
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
    help = "Get DB status"

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
    help = "Stop the DB"

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
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=data_db_stop)

    # subparser = parser.add_subparsers(dest="type")

    return parser


# citros data db start
def parser_data_db_start(parent_subparser, epilog=None):
    description_path = "data/db/start.md"
    help = "Start the DB"

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

    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=data_db_start)

    # subparser = parser.add_subparsers(dest="type")

    return parser


# citros data db logs
def parser_data_db_logs(parent_subparser, epilog=None):
    description_path = "data/db/logs.md"
    help = "Get DB logs"

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
        formatter_class=RichHelpFormatterCitros,
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
    help = "Clean all data from DB"

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
        formatter_class=RichHelpFormatterCitros,
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


def parser_data_db_remove(parent_subparser, epilog=None):
    description_path = "data/db/remove.md"
    help = "Remove DB instance"

    parser = parent_subparser.add_parser(
        "remove",
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
        formatter_class=RichHelpFormatterCitros,
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
    parser_data_db_start(subparser)
    parser_data_db_logs(subparser)
    parser_data_db_remove(subparser)
    parser_data_db_clean(subparser)

    return parser


# citros data
def parser_data(main_sub, epilog=None):
    description_path = "data.md"
    help = "Data related functionality"

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
        formatter_class=RichHelpFormatterCitros,
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
