# CLI Commands

## Command `init`
```sh
$ citros init [-dir <folder_name>] [-d | --debug] 
[-v | --verbose] [-project_name <proj_name>]
```

<details>
  <summary>Description</summary>

The `init` command is used to initialize a CITROS repository. Depending on the user's login status, this behavior varies. For logged-out users, the project initializes locally. However, logged-in users will have the `.citros` directory cloned from the CITROS remote repository. If it's a new project, an empty project will be cloned.

The initialization process involves creating a `.citros` directory within your ROS project directory and generating several files and folders therein. These files are set up to allow you to run a simulation of your project with default configurations and settings. You can tailor your CITROS repository to your specific needs by manually modifying these files (see the Project Configuration section for more details).

**Note:** the initialization process will also make sure that within your CITROS repo, you are working on a branch whose name is the same as the current branch in your ROS project. It will do so by checking it out (and possibly creating such a branch if it does not already exist).

#### Options
Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|
|`-project_name` <proj_name> | Optional name for the project. Defaults to the last folder in the path of *dir*|

</details>

<details>
  <summary>Examples</summary>

Example 1 - Initializing while logged out:

    $ citros init
    User is not logged in. Initializing Citros locally.
    Initialized Citros repository.

Example 2 - Initializing while logged in:
    
    $ citros init
    Checking internet connection...
    Checking ssh...
    Updating Citros...
    Waiting for repo to be ready...
    Citros repo successfully cloned from remote.
    Citros successfully synched with local project.
    You may review your changes via `citros status` and commit them via `citros commit`.
    Initialized Citros repository.

Note: The init command can only be executed with effect once per project. If you attempt to initialize an existing CITROS repository, you will be notified that the action is redundant, and no changes will be made. 
Example:

    $ citros init
    The directory /workspaces/cannon has already been initialized.
    No remotes found and user is not logged in. Working offline.

To re-initialize an existing CITROS repository, you must first delete the existing .citros directory for your project.
</details>

## Command `setup-ssh`

```sh
$ citros setup-ssh [-d | --debug] [-v | --verbose]
```

<details>

<summary>Description</summary>

The `setup-ssh` command sets up SSH keys for secure communication with the remote CITROS repository.

Setting up your ssh keys can be done in several different ways. You can do it manually by yourself, following the instructions on the [citros.io](https://citros.io) website, or you can use the `setup-ssh` command to automate this process.

When using `setup-ssh`, you may run it directly on your computer, in which case you will only ever need to run it once. This, of course, means you'll need to install the citros-cli directly on you computer, rather than inside a dev-container. 

If you'd rather avoid this, you can also run `setup-ssh` inside a dev container, but the price in that case, is that you'll have to run it once for each dev-container you use (and again if you rebuild the dev-container). Also, since you are prompted to give a unique title for the ssh key that will be generated, you will have to do so every time you run `setup-ssh`. 

In any case, you may view (and possibly delete) your keys in your profile settings on the [citros.io](https://citros.io) website. 

**Note:** this command *may* append some bash commands to the end of any of the following user profile files, if they exist in the user's home directory: `~/.bashrc` , `~/.bash_profile`, `~/.zprofile`. 

#### Prerequisites
User must be logged in (using `citros login`).

#### Options
Option|Description
|--|--|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|

</details>

<details>
  <summary>Examples</summary>

    $ citros setup-ssh
      
</details>

## Command `status`

```sh
$ citros status [-dir <folder_name>] 
[-d | --debug] [-v | --verbose]
```
<details>
  <summary>Description</summary>

  The `status` command first syncs any changes in your ROS project with your CITROS repository and than retrieves the current state of your CITROS repository. Essentially, it acts as a wrapper for the `git status` command specifically for your CITROS repository.
  
  This command provides a quick and concise overview of the changes made to your project, giving you insights into tracked, modified, and staged files.
  
  #### Options
Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|
</details>

<details>
  <summary>Examples</summary>

  In the example below, we employ the `status` command to gain insight into the condition of our CITROS repository. This becomes particularly beneficial when there's a divergence between your local and remote branches—like when the remote branch received updates you haven't pulled yet, while you've committed local changes still awaiting a push to the remote.:

    $ citros status
    On branch main
    Your branch and 'origin/main' have diverged,
    and have 1 and 4 different commits each, respectively.

    nothing to commit, working tree clean
    $ citros pull
    $ citros status
    On branch main
    Your branch is ahead of 'origin/main' by 2 commits.

    nothing to commit, working tree clean
    $ citros push
    $ citros status
    On branch main
    Your branch is up to date with 'origin/main'.

    nothing to commit, working tree clean
</details>

## Command `add-remote`

```sh
$ citros add-remote [-dir <folder_name>] 
[-d | --debug] [-v | --verbose]
```
<details>
  <summary>Description</summary>

  The `add-remote` command associates a remote CITROS repository, named `origin`, with your local repository. This remote repository is hosted on the CITROS servers.
  
  #### Prerequisites
  `citros setup-ssh` has already been run.

**Important:** If you execute `citros init` while logged in, the `add-remote` command will automatically run in the background, making a direct call unnecessary. However, if you initially ran `citros init` while logged out and later decide to work with the online CITROS system (e.g., running commands like `citros push`), you will need to manually run the `add-remote` command.

Furthermore, to ensure secure communication with the server, the `setup-ssh` command should be executed before running add-remote.

#### Options
Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|

</details>

<details>
  <summary>Examples</summary>

    $ citros add-remote

</details>


## Command `commit`
```sh
$ citros commit [-dir <folder_name>] 
[-d | --debug] [-v | --verbose] [-m | message]
```

<details>
  <summary>Description</summary>

  The `commit` command captures all modifications to your local CITROS repository in a snapshot, essentially serving as a wrapper for the `git commit` command, but tailored to your CITROS repository.
  By executing this command, you essentially save the current state of your project, allowing you to keep track of your progress, revert changes, and even collaborate more effectively. This forms an integral part of managing and controlling the version history of your CITROS repository.

  #### Options

Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|
|`-m`, `--message` | Commit message|
</details>

<details>
  <summary>Examples</summary>

    $ citros commit -m "added an awesome feature"
</details>

## Command `pull`

```sh
$ citros pull [-dir <folder_name>] 
[-d | --debug] [-v | --verbose]
```
<details>

<summary>Description</summary>

The `pull` command fetches from and integrates with another CITROS repository or a local branch. Essentially, it acts as a wrapper for the `git pull` command within the context of your CITROS repo.

**Note:** if there conflicts between your local copy and the remote copy that cannot be resolved automatically, than a manual merge will have to take place. Not to worry - CITROS makes this process user-friendly - see [Merge](#command-merge) for details.

#### Options
Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|

</details>


<details>
  <summary>Examples</summary>

    $ citros pull
</details>



## Command `push`
  
```sh
$ citros push [-dir <folder_name>] 
[-d | --debug] [-v | --verbose]
```

<details>
  <summary>Description</summary>

  The `push` command transfers all committed changes in your local CITROS repository to the remote repository. Essentially, it acts as a wrapper for the `git push` command within the context of your CITROS repo.
  
  By employing the `push` command, you are synchronizing your local project modifications with the remote repository. This is crucial not only for backing up your work on the server but also for enabling seamless collaboration with other team members using the CITROS platform.

  #### Options

Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|
</details>

<details>
  <summary>Examples</summary>

    $ citros push
    35461c6..d60a662

    Successfully pushed to branch `main`.
    $ citros push
    [up to date]

    Successfully pushed to branch `main`.

In the example above you can see that when there is a local commit to be pushed to the remote, `citros push` will push it and specify its commit hash. When running this command while already synched with the remote, you will be notified accordingly. 

</details>


## Command `diff`

```sh
$ citros diff [-dir <folder_name>] 
[-d | --debug] [-v | --verbose]
```    
<details>
  <summary>Description</summary>

  The `diff` command presents you with a detailed description of all differences between the latest commit and your working directory. New lines will be colored in green, and deleted lines will be colored in red.
  
  #### Options
Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|
</details>

<details>
  <summary>Examples</summary>

    $ citros diff
    diff --git a/simulations/simulation_cannon_analytic.json b/simulations/simulation_cannon_analytic.json
    index e7c823f..178c95b 100644
    --- a/simulations/simulation_cannon_analytic.json
    +++ b/simulations/simulation_cannon_analytic.json
    @@ -5,7 +5,7 @@
            "file": "cannon_analytic.launch.py",
            "package": "scheduler"
        },
    -    "timeout": 60,
    +    "timeout": 42,
        "GPU": 0,
        "CPU": 2,
        "MEM": "265MB",

</details>


## Command `checkout`

```sh
$ citros checkout [-dir <folder_name>] 
[-d | --debug] [-v | --verbose] [-b, --branch]
```    

<details>
  <summary>Description</summary>

  The `checkout` command lets you check out a different branch than the one your are currently on. It essentially wraps the `git checkout` command. If you have any uncommitted changes in your CITROS working directory, you will be asked if you want to commit those changes. If you decline, the checkout will not take place, since CITROS doesn't allow checking out while the working directory is dirty.
  
  If the branch you're attempting to check out exists (locally or on the remote), it will be checked out. If it doesn't exist yet, you will be asked if you would like to create it. If you decline, the checkout will not take place.
  
  #### Options
Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|
|`-b`, `--branch` | The name of the branch to be checked out.|
</details>

<details>
  <summary>Examples</summary>

In the following example we checkout the branch `master` (not before confirming we want to commit the changes in our working directory), and then checkout the branch `main`. 

    $ citros checkout -b master
    Cannot checkout: there are uncommitted changes in your repo.
    Would you like to commit them? (y/n) y
    Checking out local branch master
    $ citros checkout -b main
    Checking out local branch main

</details>


## Command `merge`
   
```sh
$ citros merge [-dir <folder_name>] 
[-d | --debug] [-v | --verbose]
```    

<details>
  <summary>Description</summary>

  The `merge` command enables you to integrate another branch into your current one. You'll be shown a list of accessible branches to select from. When both your branch and the target branch have modifications to the same file, the outcome varies based on the nature of these changes. Non-conflicting changes will be seamlessly merged. 
  
  However, if conflicts arise, the merge operation halts, requiring you to address these discrepancies manually, using a diff/merge tool. 
  
  #### Options
Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|
</details>

<details>
  <summary>Examples</summary>


In the following example we attempt to merge the branch `master` into the current branch:

    $ citros merge
    ? Please choose the branch you wish to merge into the current branch: master
    Merge failed due to conflicting changes between the current branch and `master`.
    Files with conflicts:
    - notebooks/test.ipynb
    Please resolve the conflicts manually.
    ...

If you are not running inside a dev-container, an instance of VS-Code will be automatically opened (pending your approval) for you to use a merge tool. After all conflicts have been resolved, save the files, close VS-Code and answer `y` to indicate that all conflicts have indeed been resolved. At this point CITROS will commit the merge on your behalf.

If you are running inside a dev-container, you'll have to run a few git commands by yourself, but not to worry - CITROS will provide you with step-by-step instructions:


    $ citros merge
    ? Please choose the branch you wish to merge into the current branch: test_branch
    Merge failed due to conflicting changes between the current branch and `test_branch`.
    Files with conflicts:
    - parameter_setups/functions/my_func.py
    Please resolve the conflicts manually.
    Since you are running inside a dev-container, you'll have to:
    1. Open a terminal, e.g.
    ctrl-alt-t
    2. Navigate to the .citros directory under your project, e.g.
    cd path/to/your/project/.citros
    3. Run the following two commands to set VS code as the git merge tool for your .citros repo:
    git config merge.tool code
    git config mergetool.code.cmd "code --wait $MERGED"
    (if you already have a merge tool set for git, you may skip this step).
    4. Open your mergetool (i.e. VS code) to resolve the conflict:
    git mergetool

    After all conflicts have been resolved, save the files, close the merge tool, answer y in the terminal and close it.
    Press y to commit the merge or n to abort the merge.
    Note: if you press y and there are still unresolved conflicts, the merge will still be aborted.
    All conflicts resolved (y/n): y
    Conflicts resolved. Committing the merge...


**Note:** For files that CITROS manages, like `project.json`, conflicts will be auto-resolved in favor of the current branch's version.

</details>


## Command `discard`

```sh
$ citros discard [-dir <folder_name>] 
[-d | --debug] [-v | --verbose] [-files] [--ALL]
```    

<details>
  <summary>Description</summary>

The `discard` command allows to you discard any uncommitted changes in your CITROS working directory. Simply specify the file paths of the files you would like to discard. Notice you have to specify the file paths relative to the `.citros` directory. 

If you'd like discard **all** changes in your working directory, effectively checking out the HEAD commit, instead of specifying individual file paths, you may use the --ALL flag.

**Notice**: the effects of this command cannot be undone.

#### Options
Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|
|`files` | List of files to revert.|
|`--ALL` | Revert all files.|

</details>

<details>
  <summary>Examples</summary>

```bash
$ citros status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
        modified:   project.json

$ citros discard project.json
$ citros status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

or, using the --ALL flag:
```bash
$ citros discard --ALL
Warning: all of the following changes will be discarded:
Modified files:
   - project.json
Discard all changes? (yes/no): yes
All changes in the working directory have been reverted to the last commit.
```

</details>


## Command `login`

```sh
$ citros login 
[-d | --debug] [-v | --verbose] 
[-username] [-password] [--local]
```    
<details>
  <summary>Description</summary>

The `login` command allows you to authenticate your session with CITROS. To use this command, you must already have a registered account with [CITROS](https://citros.io), including a valid username (email) and password.

By logging in, you unlock additional features such as cloud-based simulations, data analysis tools, automated report generation, and collaboration with other CITROS users. Use this command to seamlessly integrate your local workspace with the CITROS platform and fully utilize its capabilities.

#### Options
Option|Description
|--|--|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|
|`-username` | The user's username (email).|
|`-password` | The user's password|
|`--local` | Save auth token locally (inside .citros).|

After entering the command, if either the username or password was not given, you will be prompted for your email (the username) and password.
</details>


<details>
  <summary>Examples</summary>

    $ citros login
    $ email: example@lulav.space
    $ Password: 
    User logged in.

</details>

## Command `logout`

```sh
$ citros logout 
[-d | --debug] [-v | --verbose] 
```   

<details>
  <summary>Description</summary>

  The `logout` command terminates your active session with CITROS.

#### Options
Option|Description
|--|--|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|

</details>

<details>
  <summary>Examples</summary>
</details>


## Command `list`

```sh
$ citros list 
[-d | --debug] [-v | --verbose] 
```

<details>
  <summary>Description</summary>

  The `list` command displays all available simulation names. These names are derived from the filenames in the `simulations` folder within your CITROS repository. Each of these files corresponds to an available launch file in your ROS project. For instance, if your ROS project contains a launch file named `foo.launch.py`, a corresponding simulation file named `simulation_foo.json` will be generated in your simulations folder.

#### Options
Option|Description
|--|--|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|

</details>

<details>
  <summary>Examples</summary>

    $ citros list
    1. simulation_cannon_analytic
    2. simulation_cannon_numeric
</details>


## Command `run`

```sh
$ citros run [dir <folder_name>] [-d | --debug] [-v | --verbose]
[-s, --simulation_name] [-b, --batch_id][-n, --batch_name] 
[-m, --batch_message] [-i, --run_id] [-c, --completions]
[-r, --remote] [-k, --key] [-l, --lan_traffic] [--branch] [--commit]
```

<details>
  <summary>Description</summary>

  The `run` command launches a simulation either locally on your machine, or remotely on the CITROS cluster.

#### Prerequisites:
Ensure that the project has been built and sourced, for example:
    
    $ colcon build
    $ source install/local_setup.bash

If you'd like to run your simulation remotely, you would also need to make sure:
1. You're logged in (via `citros login`).
2. You've built and pushed a docker image of your project (using `citros docker-build-push`).
3. Your `.citros` directory is synched with the remote repository (using `citros commit` and `citros push`). 

#### Options
Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|
|`-s`, `--simulation_name` | Identifies the simulation you want to run. This is the name of the JSON file (excluding the `json` suffix) in the `simulations` folder. If you don't provide a simulation name, an interactive menu will display allowing you to select from the available simulations.|
|`-b`, `--batch_id` | Batch ID. Intended for CITROS internal use only - DO NOT USE.|
|`-n`, `--batch_name` | Assigns a descriptive name for this simulation run, e.g. according to its settings and/or parameter setup. You can disable this option requirement via `settings.json`. If disabled, and no name is given, the default name will be the date and time.|
|`-m`, `--batch_message` | Provides a descriptive message for this simulation run, e.g. according to its settings and/or parameter setup. This can also be disabled via `settings.json`.|
|`-i`, `--run_id` | Simulation run ID. Intended for CITROS internal use only - DO NOT USE.|
|`-c`, `--completions` | Sets the number of completions (simulation runs). Defaults to 1 if not specified.|
|`-r`, `--remote` | Executes the simulation remotely on the cluster. See prerequisites above for details.|
|`-k`, `--key` | Authentication key. Intended for CITROS internal use only - DO NOT USE.|
|`-l`, `--lan_traffic` | A flag which causes the simulation to receive LAN ROS traffic.|
|`--branch` | The git branch name CITROS should use when running you simulation remotely. Defaults to active branch. For remote run only, will be ignored otherwise.|
|`--commit` | The git commit hash CITROS should use when running you simulation remotely. defaults to latest commit. For remote run only, will be ignored otherwise.|


If no simulation name was provided, an interactive session will begin, and you will be prompted to select a simulation from the list of available simulations (via up, down and enter keys). 
</details>


<details>
  <summary>Examples</summary>

    $ citros run
    ? Please choose the simulation you wish to run 
    ❯ simulation_cannon_analytic
      simulation_cannon_numeric

**Note:** the `-n` and `-m` flags are mandatory by default. If you would like them to be optional, you can set the `force_batch_name` and `force_message` flags in `settings.json` to `"False"`. In that case, batch names will default to the date and time the simulation was run. 

</details>


## Command `docker-build`

```sh
$ citros docker-build [-dir <folder_name>] 
[-d | --debug] [-v | --verbose] [-n | --image_name]
[-t, --tag]
```

<details>
  <summary>Description</summary>

The `docker-build` command is used to construct a Docker image of your ROS project. This image encapsulates your project's environment, facilitating the portability and reproducibility of your simulations across different systems.

#### Prerequisites
1. If you are working inside a dev-container, make sure that the `docker-in-docker` feature is enabled in your project's `devcontainer.json`, i.e.:

```sh
    "features": {
		"ghcr.io/devcontainers/features/docker-in-docker:2": {
			"version": "latest",
			"moby": true
		}
	}
  ```

2. You must have an appropriate Dockerfile under the main directory of your project. An Explanation on how to write the Dockerfile such that it could be used with CITROS, may be found [here](https://citros.io/doc/docs_tutorials/dockerfile_overview/).

#### Options
Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|
|`-n`, `--image_name` | The requested image name (e.g. the project name). Defaults to the last folder in the path of dir |
|`-t`, `--tag` | the requested tag name for the image. Defaults to `latest`|
</details>

<details>
  <summary>Examples</summary>

    $ citros docker-build
    Building Docker image...
    => building with "default" instance using docker driver
    => ...
    Done.
</details>


## Command `docker-build-push`

```sh
$ citros docker-build-push [-dir <folder_name>] 
[-d | --debug] [-v | --verbose] [-n | --image_name]
```

<details>
  <summary>Description</summary>

The `docker-build-push` command is used to construct a Docker image of your ROS project and upload it to the CITROS registry. This image encapsulates your project's environment, facilitating the portability and reproducibility of your simulations across different systems. 

Two tagged images will be built and pushed: `latest` and the ROS project's latest commit hash, so that it is archived in the docker registry.

#### Prerequisites
1. If you are working inside a dev-container, make sure that the `docker-in-docker` feature is enabled in your project's `devcontainer.json`, i.e.:

```sh
    "features": {
		"ghcr.io/devcontainers/features/docker-in-docker:2": {
			"version": "latest",
			"moby": true
		}
	}
```

2. You must have an appropriate Dockerfile under the main directory of your project. An Explanation on how to write the Dockerfile such that it could be used with CITROS, may be found [here](https://citros.io/doc/docs_tutorials/dockerfile_overview/).

#### Options
Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|
|`-n`, `--image_name` | The requested image name (e.g. the project name). Defaults to the last folder in the path of dir |
</details>

<details>
  <summary>Examples</summary>

    $ citros docker-build-push
    Building Docker image...
    => building with "default" instance using docker driver
    => ...
    Done.
    Pushing Docker image...
    The push refers to repository [us-central1-docker.pkg.dev/citros/lulav/cannon]
    ea97705925b1: Pushed 
    0d42db2cff87: Preparing 
    3752398ae296: Layer already exists 
    ...
    latest: digest: sha256:b5d109f83c1dbbaf97d918e721889988210d9bc1a91f3ecde884fbc394bcca1c size: 5136
    The push refers to repository [us-central1-docker.pkg.dev/citros/lulav/cannon]
    ea97705925b1: Layer already exists 
    5deba67bdae6: Layer already exists 
    ... 
    7f858865b89b41f493d1197c3329c0214996a625: digest: sha256:b5d109f83c1dbbaf97d918e721889988210d9bc1a91f3ecde884fbc394bcca1c size: 5136
    Done.
</details>
