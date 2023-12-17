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

from .parsers import (
    parser_run,
    parser_simulation,
    parser_parameter,
    parser_launch,
    parser_data,
    parser_report,
    parser_init,
    parser_doctor,
)

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

    parser_init(subparsers, EPILOG)
    parser_doctor(subparsers, EPILOG)
    parser_run(subparsers, EPILOG)
    parser_simulation(subparsers, EPILOG)
    parser_parameter(subparsers, EPILOG)
    parser_launch(subparsers, EPILOG)
    parser_data(subparsers, EPILOG)
    parser_report(subparsers, EPILOG)

    args, argv = parser.parse_known_args()

    args.func(args, argv)


if __name__ == "__main__":
    main()
