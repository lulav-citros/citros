import path
import sys
from pathlib import Path
from rich import print, inspect, print_json
from rich.rule import Rule
from rich.panel import Panel
from rich.padding import Padding
from rich.logging import RichHandler
from rich.console import Console
from rich.markdown import Markdown
from rich_argparse import RichHelpFormatter

directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from data_access import data_access as _data_access


############################# CLI implementation ##############################
def init(args, argv):
    # TODO[critical]: implement init
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def doctor(args, argv):
    # TODO[critical]: implement doctor
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def run(args, argv):
    # TODO[critical]: implement run
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


############################# BATCH implementation ##############################
def batch_list(args, argv):
    # TODO[critical]: implement batch_list
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def batch_get(args, argv):
    # TODO[critical]: implement batch_get
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def batch_delete(args, argv):
    # TODO[critical]: implement batch_delete
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


############################# DATA implementation ##############################
def data_access(args, argv):
    """
    :param args.dir
    :param args.debug:
    :param args.verbose:
    :param args.project_name:
    """

    # print(Panel(Markdown(open("bin/data.md", "r").read()), title="[green]CITROS", subtitle=f"[{citros_version}]"))
    print(
        Panel.fit(
            f"""[green]CITROS[/green] started data-access service at [green]http://{args.host}:{args.port}.
API: open [green]http://{args.host}:{args.port}/redoc[/green] for documantation"""
        )
    )
    _data_access(args, argv)


def data_status(args, argv):
    # TODO[critical]: implement data_status
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def data_create(args, argv):
    # TODO[critical]: implement data_create
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def data_clean(args, argv):
    # TODO[critical]: implement data_clean
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


############################# REPORT implementation ##############################
def report_generate(args, argv):
    # TODO[critical]: implement report_generate
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


def report_validate(args, argv):
    # TODO[critical]: implement report_validate
    print(f"[red] 'citros {args.func.__name__}' is Not implemented yet")


from citros import Citros


def init_citros(args, argv):
    """
    :param args.dir
    :param args.debug:
    :param args.verbose:
    :param args.project_name:
    """
    with Citros(
        user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug, on_init=True
    ) as citros:
        if citros.check_project(True):
            citros.print(
                f"The directory {Path(args.dir).resolve()} has already been initialized.",
                color="yellow",
            )
            return

        if not citros.isAuthenticated():
            citros.set_divergent_branches_reconcile_config(repo)

            citros.update_git_exclude(citros.USER_PROJ_DIR, ".citros*")

            citros.update_git_exclude(citros.CITROS_REPO_DIR, "runs/")

            citros.checkout_user_branch_if_different(check_remote=False)

            citros.save_user_commit_hash()

            citros.copy_user_templates()

            success = citros.internal_sync(True)

            if success:
                citros.try_commit("first commit")
            else:
                # sanity - should never happen.
                citros.print(f"internal_sync on init failed.", color="red")

        citros.print(f"Intialized Citros repository.", color="green")
