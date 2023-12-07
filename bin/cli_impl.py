
import path
import sys
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








def init_citros(args, argv):
	"""
	:param args.dir
	:param args.debug:
	:param args.verbose:
	:param args.project_name:
	"""   
	with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug, on_init=True) as citros:
		citros_path = citros.CITROS_REPO_DIR

		if not is_git_repo(citros.USER_PROJ_DIR):
			citros.print(f"The project directory `{citros.USER_PROJ_DIR}` is not a valid git repo.{linesep}" + \
						 f"If you are running inside a devcontainer, make sure the directory " + \
						 f"is not a git submodule.", color='red')
			return

		if citros.check_project(True):
			citros.print(f"The directory {Path(args.dir).resolve()} has already been initialized.", color='yellow')

			# check .git was not corrupted or deleted
			if not is_git_repo(citros_path):
				citros.print(f"The Citros directory {citros_path} is not a valid git repository.", color='red')
				return

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

				# write the repo id to file
				with open(citros.REPO_ID_FILE, 'w') as file:
					file.write(citros.repo_id)
     
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


# def setup_ssh(args, argv):
# 	with Citros(verbose=args.verbose, debug=args.debug) as citros:
# 		if not citros.utils.is_connected():
# 			citros.print(f"No internet connection. Check your connection and try again.", color='red')
# 			return

# 		if not citros.isAuthenticated():
# 			citros.print(f"Cannot setup ssh while not logged in. Login and try again.", color='red')
# 			return

# 	title = input("Please provide a descriptive title for the new ssh key (e.g. 'Personal laptop'): ")
	
# 	if not citros.utils.is_valid_file_name(title):
# 		citros.print(f"Invalid title. Please try again.", color='red')
# 		return
	
# 	citros.setup_ssh(title)


# def status(args, argv):
# 	with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug) as citros: 
# 		if not citros.is_initialized:
# 			citros.print(f"Cannot check status. {args.dir} has not been initialized.", color='red')
# 			return
		
# 		if not citros.verify_citros_branch():
# 			citros.print(f"Check out the correct branch and try again.", color='red')
# 			return

# 		citros.internal_sync()

# 		citros.print_git_output(git.Repo(citros.CITROS_REPO_DIR).git.status())


# def add_remote(args, argv):
# 	with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug) as citros: 
# 		if not citros.is_initialized:
# 			citros.print(f"Cannot add remote. {args.dir} has not been initialized.", color='red')
# 			return

# 		citros_remote = citros.upsert_repo_to_citros()
# 		if citros_remote:
# 			citros.add_remote(citros.CITROS_REPO_DIR, 'origin', citros_remote)
# 			citros.print(f"Successfully added remote [{citros_remote}].", color='magenta')

# 			# since this couldn't be done during an offline init, we do it now
# 			citros.set_default_citros_branch()
# 		else:
# 			citros.print(f"Failed to get citros remote url.", color='red')


# def commit(args, argv):
#     with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug) as citros: 
#         if not citros.is_initialized:
#             citros.print(f"Cannot commit. {args.dir} has not been initialized.", color='red')
#             return
		
#         if not citros.verify_citros_branch():
#             citros.print(f"Check out the correct branch and try again.", color='red')
#             return

#         citros.try_commit(args.message)
        

# def push(args, argv):
#     with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug) as citros:
#         if not citros.is_initialized:
#             citros.print(f"Cannot push. {args.dir} has not been initialized.", color='red')
#             return
		
#         if not citros.utils.is_connected():
#             citros.print(f"No internet connection. Check your connection and try again.", color='red')
#             return

#         if not citros.verify_citros_branch():
#             citros.print(f"Check out the correct branch and try again.", color='red')
#             return

#         citros.git_push()


# def pull(args, argv):
#     with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug) as citros:
#         if not citros.is_initialized:
#             citros.print(f"Cannot pull. {args.dir} has not been initialized.", color='red')
#             return
		
#         if not citros.utils.is_connected():
#             citros.print(f"No internet connection. Check your connection and try again.", color='red')
#             return
		
#         if not citros.verify_citros_branch():
#             citros.print(f"Check out the correct branch and try again.", color='red')
#             return

#         citros.git_pull()


# def diff(args, argv):
# 	with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug) as citros:
# 		if not citros.is_initialized:
# 			citros.print(f"Cannot diff. {args.dir} has not been initialized.", color='red')
# 			return
		
# 		if not citros.verify_citros_branch():
# 			citros.print(f"Check out the correct branch and try again.", color='red')
# 			return

# 		citros.git_diff()


# def checkout(args, argv):
# 	with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug) as citros:
# 		if not citros.is_initialized:
# 			citros.print(f"Cannot checkout. {args.dir} has not been initialized.", color='red')
# 			return
		
# 		if args.branch:
# 			citros.checkout_branch(args.branch)
# 		else:
# 			citros.print("Please provide a branch name to checkout:", color='red')
# 			citros.print("citros checkout -b <branch name>", color='cyan')


# def merge(args, argv):
# 	with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug) as citros:
# 		if not citros.is_initialized:
# 			citros.print(f"Cannot merge. {args.dir} has not been initialized.", color='red')
# 			return
		
# 		local_branches = citros.get_local_branch_names(include_current=False)

# 		if not local_branches:
# 			citros.print(f"Cannot merge: no other branches exist in your repository.", color='red')
# 			return
		
# 		branch_names_q = generate_question("list", "local_branches", 
#             "Please choose the branch you wish to merge into the current branch:", local_branches )

# 		answers = prompt([branch_names_q])  # use default style
# 		branch_name = answers.get("local_branches")

# 		citros.merge_branch(branch_name)


# def discard(args, argv):
# 	with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug) as citros:
# 		if not citros.is_initialized:
# 			citros.print(f"Cannot discard. {args.dir} has not been initialized.", color='red')
# 			return
		
# 		citros.discard_changes(args.files, args.ALL)
		

# def login(args, argv): 
#     with Citros(verbose=args.verbose, debug=args.debug) as citros:       
#         username, password = args.username, args.password

#         if args.local:
#             citros.is_local_init = True

#         if not citros.isAuthenticated() and (args.username is None or args.password is None):
#             username = input("email: ")
#             password = getpass()     
#         resp = citros.login(username, password)
#         if resp:
#             citros.print("User logged in.", color='green')
#         else:
#             citros.print("Failed to log in. Please try again.", color='red')

    
# def logout(args, argv):
#     with Citros(verbose=args.verbose, debug=args.debug) as citros: 
#         citros.logout() 
#         citros.print("User logged out.")


# def list_project(args, argv):
#     with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug) as citros:
#         if not citros.is_initialized:
#             citros.print(f"Cannot list. {args.dir} has not been initialized.", color='red')
#             return

#         simulations = citros.get_simulations()
#         i = 1
#         for s in simulations:
#             citros.print(f"{str(i)}. {s}")
#             i = i + 1


# def run(args, argv):
# 	"""
# 	:param args.dir
# 	:param args.simulation_name:
# 	:param args.batch_id:
# 	:param args.run_id:
# 	:param args.remote:
# 	:param args.completions:
# 	:param args.debug:
# 	:param args.batch_name:
# 	:param args.batch_message:
# 	:param args.verbose:
#     :param args.key:
#     :param args.lan_traffic:
#     :param args.branch
#     :param args.commit
# 	"""   
# 	sim_name, batch_id, run_id = args.simulation_name, args.batch_id, args.run_id
# 	remote, completions = args.remote, args.completions
	
# 	with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug) as citros:
# 		if not citros.is_initialized:
# 			citros.print(f"Cannot run. {args.dir} has not been initialized.", color='red')
# 			return
		
# 		if args.key:
# 			citros.set_auth_key(args.key, args.dir)
		
# 		if not citros.verify_citros_branch(batch_id):
# 			citros.print(f"Check out the correct branch and try again.", color='red')
# 			return
                
# 		if not citros.check_ros_build(citros.USER_PROJ_DIR):
# 			citros.print(f"Cannot run. `install` directory was not found.", color='red')
# 			citros.print(f"Run `colcon build` first.", color='cyan')
# 			return

# 		loggedin = citros.isAuthenticated()

# 		if remote and not loggedin:
# 			citros.print(f"Cannot run remotely - please log in first.", color='red')
# 			return

# 		success = citros.internal_sync(False)

# 		if not success:
# 			citros.print(f"internal_sync before run failed. Cannot run.{linesep}" + \
# 						 f"Fix the errors in your project configuration files and try again.", color='red')
# 			return

# 		success = citros.set_batch_name_and_message(args.batch_name, args.batch_message)

# 		if not success:
# 			citros.print(f"Please try again with all required command parameters.", color='yellow')
# 			return
		
# 		citros.SUPPRESS_ROS_LAN_TRAFFIC = not args.lan_traffic

# 		if batch_id:
# 			if not citros.CITROS_ENVIRONMENT == 'CLUSTER':
# 				raise ValueError("cannot run batch on non CLUSTER environment.")
# 			citros.run_simulation_by_k8s(batch_id, run_id)
# 		elif sim_name:
# 			citros.run_simulation(sim_name, completions, remote, args.commit, args.branch)
# 		else:
# 			# simulation is chosen by the user 
# 			run_interactively(citros, completions, remote, args.commit, args.branch)


# def run_interactively(citros : Citros, completions, remote, commit_hash, branch_name):
#     sim_names = citros.get_simulations()
    
#     # sanity check - should never happen because internal_sync will fail if there 
#     #                isn't at least one simulation file.
#     if not sim_names:
#         citros.print(f"There are currently no simulations in your {citros.SIMS_DIR} folder. \
#                 	 Please create at least one simulation for your project.", color='red')
#         return
    
#     sim_names_q = generate_question("list", "sim_names", 
#                                     "Please choose the simulation you wish to run:", sim_names )
#     #completions_q = generate_question("input", "completions", "Please enter number of completions:",
#     #                                  NumberValidator, lambda val: int(val))
#     answers = prompt([sim_names_q])  # use default style
#     sim_name = answers.get("sim_names")

#     citros.run_simulation(sim_name, completions, remote, commit_hash, branch_name)


# def docker_build(args, argv):
#     with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug) as citros:
#         if not citros.is_initialized:
#             citros.print(f"{args.dir} has not been initialized.",color='red')
#             return
		
#         if not citros.verify_citros_branch():
#             citros.print(f"Check out the correct branch and try again.", color='red')
#             return
        
#         citros.build_docker_image([f"{args.image_name}:{args.tag}"])


# def docker_build_push(args, argv):
#     with Citros(user_proj_dir=args.dir, verbose=args.verbose, debug=args.debug) as citros:
#         if not citros.is_initialized:
#             citros.print(f"{args.dir} has not been initialized.",color='red')
#             return

#         if not citros.utils.is_connected():
#             citros.print(f"No internet connection. Check your connection and try again.", color='red')
#             return

#         if not citros.verify_citros_branch():
#             citros.print(f"Check out the correct branch and try again.", color='red')
#             return

#         if not citros.isAuthenticated():
#             citros.print(f"Please log in to Citros first.", color='red')
#             return
        
#         if not citros.is_logged_in_to_docker():
#             citros.print("Logging in to docker...")
#             if not citros.docker_login():
#                 return
        
#         success = citros.build_and_push_docker_image(args.image_name)

#         if not success:
#             citros.print(f"Failed to build or push.", color='red')

