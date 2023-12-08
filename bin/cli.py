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

from .parsers import parser_simulation, parser_parameter, parser_data, parser_report


install()

# PANNEL = ""
PANNEL = Panel.fit(
    f"""[green]████████████████████████████████████████████████████████████
██      ███        ██        ██       ████      ████      ██
█  ████  █████  ████████  █████  ████  ██  ████  ██  ███████
█  ███████████  ████████  █████       ███  ████  ███      ██
█  ████  █████  ████████  █████  ███  ███  ████  ████████  █
██      ███        █████  █████  ████  ███      ████      ██
████████████████████████████████████████████████████████████""",
    subtitle=f"[{citros_version}]",
)
EPILOG = Markdown("Read more at [citros](https://citros.io)")


def parser_init(main_sub):
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
        epilog=EPILOG,
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


def parser_doctor(main_sub):
    parser = main_sub.add_parser(
        "doctor",
        description=Panel(
            Markdown(
                open(
                    importlib_resources.files(f"data.doc").joinpath("doctor.md"), "r"
                ).read()
            ),
            subtitle=f"[{citros_version}]",
            title="description",
        ),
        epilog=EPILOG,
        help="doctor section",
        formatter_class=RichHelpFormatter,
    )
    parser.add_argument("-dir", default=".", help="The working dir of the project")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=doctor)


def parser_run(main_sub):
    parser = main_sub.add_parser(
        "run",
        description=Panel(
            Markdown(
                open(
                    importlib_resources.files(f"data.doc").joinpath("run.md"), "r"
                ).read()
            ),
        ),
        epilog=EPILOG,
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
    parser.add_argument("-i", "--run_id", nargs="?", default="", help="run id")
    parser.add_argument(
        "-c",
        "--completions",
        nargs="?",
        default=1,
        help="number of times to run the simulation",
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=run)


def main():
    # main parser -----------------------------------------
    parser = argparse.ArgumentParser(
        description=PANNEL,
        epilog=EPILOG,
        formatter_class=RichHelpFormatter,
        # add_help=False
    )
    parser.add_argument("-V", "--version", action="version", version=citros_version)

    subparsers = parser.add_subparsers(
        title="commands", help="citros commands", dest="type", required=True
    )

    parser_init(subparsers)
    parser_doctor(subparsers)
    parser_run(subparsers)
    parser_simulation(subparsers)
    parser_parameter(subparsers)
    parser_data(subparsers)

    parser_report(subparsers)

    args, argv = parser.parse_known_args()

    args.func(args, argv)


if __name__ == "__main__":
    main()
