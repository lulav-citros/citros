
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
    print(Panel.fit(f"""[green]CITROS[/green] started data-access service at [green]http://{args.host}:{args.port}.
API: open [green]http://{args.host}:{args.port}/redoc[/green] for documantation"""))    
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
	with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug, on_init=True) as citros:
		
		if citros.check_project(True):
			citros.print(f"The directory {Path(args.dir).resolve()} has already been initialized.", color='yellow')

			citros_remote = citros.get_citros_remote()
			if citros_remote:
				citros.print(f"working remotely with [{citros_remote}].")
				return

			if not citros.isAuthenticated():
				citros.print("No remotes found and user is not logged in. Working offline.")
			else:
				citros.print(f"You are logged in but have yet to add a remote repo.{linesep}" + \
							 f"To add a remote repo, call the following citros commands:")
				citros.print(f"citros setup-ssh{linesep}citros add-remote", color='cyan')
				citros.print(f"It is also recommended that you then run")
				citros.print(f"citros status", color='cyan')
				citros.print(f"and resolve any conflicts you may have with the remote.")
			
			return

		if not citros.isAuthenticated():
			citros.print("User is not logged in. Initialzing Citros locally.")

			# init repo and work offline
			repo = git.Repo.init(path=citros_path)

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
				citros.print(f"internal_sync on init failed.", color='red')

		else:
			citros.print("Checking internet connection...")
			if not citros.utils.is_connected():
				citros.print(f"No internet connection. Check your connection and try again.", color='red')
				return

			citros.print("Checking ssh...")
			if not citros.utils.check_ssh_key_uploaded(try_all_keys=True):
				citros.print(f"ssh keys have not been uploaded to citros.", color='red')
				citros.print(f"Did you forget to run citros setup-ssh?", color='cyan')
				return
            
			citros.print("Updating Citros...")
			citros_remote = citros.upsert_repo_to_citros()

			if not citros_remote:
				citros.print(f"Failed to get citros remote url.", color='red')
				return
			else:
				citros.print("Waiting for repo to be ready...")
				
				# it may take a few seconds for the repo to be available on the remote.
				if not citros.wait_till_repo_ready():
					citros.print("Unfortunately something went wrong with the remote repo. " + \
								 "Please try again in a few moments.", color='yellow')
					return

				# if a new repo was created on the remote, an empty repo will be cloned.
				repo = citros.clone_repo(citros_path, citros_remote)

				citros.print(f"Citros repo successfully cloned from remote.", color='magenta')
				
				citros.set_divergent_branches_reconcile_config(repo)

				citros.checkout_user_branch_if_different()

				citros.set_default_citros_branch()

				first_commit = citros.is_repo_empty(repo)

				citros.update_git_exclude(citros.USER_PROJ_DIR, ".citros*")

				citros.update_git_exclude(citros.CITROS_REPO_DIR, ".runs/")

				citros.save_user_commit_hash()

				citros.copy_user_templates()

				
     
				success = citros.internal_sync(True)

				if success:
					citros.print(f"Citros successfully synched with local project.")

					if first_commit:
						if citros.try_commit("first commit"):
							citros.git_push()
							citros.print(f"All changes committed and pushed to citros.", color='magenta')
					else:
						citros.print(f"You may review your changes via `citros status` " + \
									 f"and commit them via `citros commit`.", color='magenta')
				else:
					citros.print(f"Failed to sync citros with local project." + \
				  				 f"See log file under {citros.CLI_LOGS_DIR} for details.", color='red')

		citros.print(f"Intialized Citros repository.", color='green')
