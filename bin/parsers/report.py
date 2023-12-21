import sys
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


# citros report
def parser_report_generate(subparser, epilog=None):
    description_path = "report/generate.md"
    help = "citros report generate section"
    parser = subparser.add_parser(
        "generate",
        description=Panel(
            Markdown(
                open(
                    importlib_resources.files(f"data.doc").joinpath(description_path),
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
        "-e", "--execute", action="store_true", help="Execute notebooks"
    )
    parser.add_argument(
        "-r", "--render", action="store_true", help="Render notebooks to PDF"
    )
    parser.add_argument("-s", "--sign", action="store_true", help="Sign PDFs")
    parser.add_argument(
        "-key",
        "--key-path",
        help="Path to private key file for signing",
        required="-s" in sys.argv,
    )
    parser.add_argument("-notebooks", nargs="+", help="Paths to Jupyter notebooks")
    parser.add_argument(
        "-style", "--style-path", help="Path to CSS style file", default=None
    )
    parser.add_argument("-output", "--output-folder", help="Path to output folder")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=report_generate)

    return parser


# citros report list
def parser_report_validate(subparser, epilog=None):
    description_path = "report/validate.md"
    help = "citros report validate section"
    parser = subparser.add_parser(
        "validate",
        description=Panel(
            Markdown(
                open(
                    importlib_resources.files(f"data.doc").joinpath(description_path),
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
        "-c", "--check", action="store_true", help="Verify PDF signatures"
    )
    # parser.add_argument("paths", nargs='*', help="Path to the public key file for verification, followed by paths to PDF files to be verified")
    parser.add_argument(
        "-key",
        "--public-key-path",
        help="Path to public key file for verification",
        required=True,
    )
    parser.add_argument(
        "-pdfs", nargs="+", help="Paths to PDF files to be verified", required=True
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="set logging level to debug"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="use verbose console prints"
    )
    parser.set_defaults(func=report_validate)
    return parser


# citros report
def parser_report(subparser, epilog=None):
    description_path = "report.md"
    help = "report section"
    parser = subparser.add_parser(
        "report",
        description=Panel(
            Markdown(
                open(
                    importlib_resources.files(f"data.doc").joinpath(description_path),
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
    parser.add_argument("-n", "--name", default=None, help="name of report")
    parser.add_argument("-m", "--match", default=None, help="match report pattern")

    parser.set_defaults(func=report)

    subparser = parser.add_subparsers(dest="type")
    # report run/list
    parser_report_generate(subparser, epilog=epilog)
    parser_report_validate(subparser, epilog=epilog)

    return parser
