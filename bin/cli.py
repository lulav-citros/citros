import argparse
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

# PANNEL = ""
PANNEL = Panel.fit(
f'''[green]████████████████████████████████████████████████████████████
██      ███        ██        ██       ████      ████      ██
█  ████  █████  ████████  █████  ████  ██  ████  ██  ███████
█  ███████████  ████████  █████       ███  ████  ███      ██
█  ████  █████  ████████  █████  ███  ███  ████  ████████  █
██      ███        █████  █████  ████  ███      ████      ██
████████████████████████████████████████████████████████████''',  
    subtitle=f"[{citros_version}]"
)
EPILOG =  Markdown('Read more at [citros](https://citros.io)')

def parser_init(main_sub):
    parser = main_sub.add_parser(
        "init", 
        description=Panel(Markdown(open('bin/doc/init.md', 'r').read()), subtitle=f"[{citros_version}]"),
        epilog=EPILOG,
        help="init section",
        formatter_class=RichHelpFormatter,
    )
    parser.add_argument("-dir", default=".", help="The working dir of the project")
    parser.add_argument("-d", "--debug", action='store_true', help="set logging level to debug")
    parser.add_argument("-v", "--verbose", action='store_true', help="use verbose console prints")
    parser.set_defaults(func=init)

def parser_doctor(main_sub):
    parser = main_sub.add_parser(
        "doctor", 
        description=Panel(Markdown(open('bin/doc/doctor.md', 'r').read()), subtitle=f"[{citros_version}]", title="description"),
        epilog=EPILOG,
        help="doctor section",
        formatter_class=RichHelpFormatter,
    )
    parser.add_argument("-dir", default=".", help="The working dir of the project")
    parser.add_argument("-d", "--debug", action='store_true', help="set logging level to debug")
    parser.add_argument("-v", "--verbose", action='store_true', help="use verbose console prints")
    parser.set_defaults(func=doctor)

def parser_run(main_sub):
    parser = main_sub.add_parser(
        "run", 
        description=Panel(Markdown(open('bin/doc/run.md', 'r').read())),
        epilog=EPILOG,
        help="run section",
        formatter_class=RichHelpFormatter,
    )
    parser.add_argument("-dir", default=".", help="The working dir of the project")
    parser.add_argument("-d", "--debug", action='store_true', help="set logging level to debug")
    parser.add_argument("-v", "--verbose", action='store_true', help="use verbose console prints")
    parser.set_defaults(func=run)

def parser_batch(main_sub):
    parser = main_sub.add_parser(
        "batch", 
        description=Panel(Markdown(open('bin/doc/batch.md', 'r').read()), subtitle=f"[{citros_version}]"),
        epilog=EPILOG,
        help="batch section",
        formatter_class=RichHelpFormatter,
    )
    data_subparser = parser.add_subparsers(dest='type')
    
    data_access_parser = data_subparser.add_parser(
        'list',
        description=Panel(Markdown(open('bin/doc/batch/list.md', 'r').read()), subtitle=f"[{citros_version}]"),
        epilog=EPILOG,
        help="citros batch list section",
        formatter_class=RichHelpFormatter
    )    
    data_access_parser.add_argument("-d", "--debug", action='store_true', help="set logging level to debug")
    data_access_parser.add_argument("-v", "--verbose", action='store_true', help="use verbose console prints")
    data_access_parser.set_defaults(func=batch_list)
    
    data_create_subparser = data_subparser.add_parser(
        'get',
        description=Panel(Markdown(open('bin/doc/batch/get.md', 'r').read()), subtitle=f"[{citros_version}]"),
        epilog=EPILOG,
        help="citros batch get section",
        formatter_class=RichHelpFormatter
    )    
    data_create_subparser.add_argument("-d", "--debug", action='store_true', help="set logging level to debug")
    data_create_subparser.add_argument("-v", "--verbose", action='store_true', help="use verbose console prints")
    data_create_subparser.set_defaults(func=batch_get)
    
    data_status_subparser = data_subparser.add_parser(
        'delete',
        description=Panel(Markdown(open('bin/doc/batch/delete.md', 'r').read()), subtitle=f"[{citros_version}]"),
        epilog=EPILOG,
        help="citros batch delete section",
        formatter_class=RichHelpFormatter
    )    
    data_status_subparser.add_argument("-d", "--debug", action='store_true', help="set logging level to debug")
    data_status_subparser.add_argument("-v", "--verbose", action='store_true', help="use verbose console prints")
    data_status_subparser.set_defaults(func=batch_delete)
        
def parser_data(main_sub):
    parser = main_sub.add_parser(
        "data", 
        description=Panel(Markdown(open('bin/doc/data.md', 'r').read()), subtitle=f"[{citros_version}]", title="description"),
        epilog=EPILOG,
        help="data section",
        formatter_class=RichHelpFormatter,
    )
    data_subparser = parser.add_subparsers(dest='type')
    
    data_access_parser = data_subparser.add_parser(
        'access',
        description=Panel(Markdown(open('bin/doc/data/access.md', 'r').read()), subtitle=f"[{citros_version}]", title="description"),
        epilog=EPILOG,
        help="citros data access section",
        formatter_class=RichHelpFormatter
    )
    data_access_parser.add_argument("-dir", default=".", help="The working dir of the project")
    data_access_parser.add_argument("-H", "--host", default="0.0.0.0", help="host")
    data_access_parser.add_argument("-p", "--port", default="8000", help="post to listen to")
    data_access_parser.add_argument("-t", "--time", action='store_true', help="print request times")
    data_access_parser.add_argument("-d", "--debug", action='store_true', help="set logging level to debug")
    data_access_parser.add_argument("-v", "--verbose", action='store_true', help="use verbose console prints")
    data_access_parser.set_defaults(func=data_access)
    
    data_create_subparser = data_subparser.add_parser(
        'create',
        description=Panel(Markdown(open('bin/doc/data/create.md', 'r').read()), subtitle=f"[{citros_version}]", title="description"),
        epilog=EPILOG,
        help="citros data create section",
        formatter_class=RichHelpFormatter
    )    
    data_create_subparser.add_argument("-d", "--debug", action='store_true', help="set logging level to debug")
    data_create_subparser.add_argument("-v", "--verbose", action='store_true', help="use verbose console prints")
    data_create_subparser.set_defaults(func=data_create)
    
    data_status_subparser = data_subparser.add_parser(
        'status',
        description=Panel(Markdown(open('bin/doc/data/status.md', 'r').read()), subtitle=f"[{citros_version}]", title="description"),
        epilog=EPILOG,
        help="citros data status section",
        formatter_class=RichHelpFormatter
    )    
    data_status_subparser.add_argument("-d", "--debug", action='store_true', help="set logging level to debug")
    data_status_subparser.add_argument("-v", "--verbose", action='store_true', help="use verbose console prints")
    data_status_subparser.set_defaults(func=data_status)
    
    data_clean_subparser = data_subparser.add_parser(
        'clean',
        description=Panel(Markdown(open('bin/doc/data/clean.md', 'r').read()), subtitle=f"[{citros_version}]", title="description"),
        epilog=EPILOG,
        help="citros data clean section",
        formatter_class=RichHelpFormatter
    ) 
    data_clean_subparser.add_argument("-d", "--debug", action='store_true', help="set logging level to debug")
    data_clean_subparser.add_argument("-v", "--verbose", action='store_true', help="use verbose console prints")
    data_clean_subparser.set_defaults(func=data_clean)
    
def parser_report(main_sub):
    parser = main_sub.add_parser(
        "report", 
        description=Panel(Markdown(open('bin/doc/report.md', 'r').read()), subtitle=f"[{citros_version}]", title="description"),
        epilog=EPILOG,
        help="report section",
        formatter_class=RichHelpFormatter,
    )
    subparser = parser.add_subparsers(dest='type')
    
    generate_parser = subparser.add_parser(
        'generate',
        description=Panel(Markdown(open('bin/doc/report/generate.md', 'r').read()), subtitle=f"[{citros_version}]", title="description"),
        epilog=EPILOG,
        help="citros report generate section",
        formatter_class=RichHelpFormatter
    )
    generate_parser.add_argument("-dir", default=".", help="The working dir of the project")
    generate_parser.add_argument("-d", "--debug", action='store_true', help="set logging level to debug")
    generate_parser.add_argument("-v", "--verbose", action='store_true', help="use verbose console prints")
    generate_parser.set_defaults(func=report_generate)
    
    validate_parser = subparser.add_parser(
        'validate',
        description=Panel(Markdown(open('bin/doc/report/validate.md', 'r').read()), subtitle=f"[{citros_version}]", title="description"),
        epilog=EPILOG,
        help="citros report validate section",
        formatter_class=RichHelpFormatter
    )
    validate_parser.add_argument("-dir", default=".", help="The working dir of the project")
    validate_parser.add_argument("-d", "--debug", action='store_true', help="set logging level to debug")
    validate_parser.add_argument("-v", "--verbose", action='store_true', help="use verbose console prints")
    validate_parser.set_defaults(func=report_validate)
     
def main():
    # main parser -----------------------------------------
    parser = argparse.ArgumentParser(
        description=PANNEL,
        epilog=EPILOG,
        formatter_class=RichHelpFormatter,
        # add_help=False
    )
    parser.add_argument('-V', "--version",
                        action="version",
                        version=citros_version)
    
    subparsers = parser.add_subparsers(title="commands", 
                                       help="citros commands", 
                                       dest='type', 
                                       required=True)
    
    parser_init(subparsers)
    parser_doctor(subparsers)
    parser_run(subparsers)
    parser_batch(subparsers)
    parser_data(subparsers)
    parser_report(subparsers)

    args, argv = parser.parse_known_args()
    
    args.func(args, argv)

if __name__ == '__main__':
    main()