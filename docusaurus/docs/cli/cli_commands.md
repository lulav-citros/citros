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


## Command `doctor`

```sh
$ citros doctor [dir <folder_name>] [-d | --debug] [-v | --verbose]
[-s, --simulation_name] [-b, --batch_id][-n, --batch_name] 
[-m, --batch_message] [-i, --run_id] [-c, --completions]
[-r, --remote] [-k, --key] [-l, --lan_traffic] [--branch] [--commit]
```

<details>
  <summary>Description</summary>

Description goes here

#### Prerequisites:

#### Options
Option|Description
|--|--|


</details>


<details>
  <summary>Examples</summary>

</details>




----------------------------------------------------------------------------------------------------------------




## Command `simulation`

## Command `parameters`

## Command `launch`

## Command `batch`

## Command `data`

## Command `reports`

## Command `observability`

## Command `example`

```sh
$ citros run [dir <folder_name>] [-d | --debug] [-v | --verbose]
[-s, --simulation_name] [-b, --batch_id][-n, --batch_name] 
[-m, --batch_message] [-i, --run_id] [-c, --completions]
[-r, --remote] [-k, --key] [-l, --lan_traffic] [--branch] [--commit]
```

<details>
  <summary>Description</summary>

Description goes here

#### Prerequisites:
Ensure that the project has been built and sourced, for example:
    
    $ colcon build
    $ source install/local_setup.bash

#### Options
Option|Description
|--|--|
|`-dir` <folder_name> | Specifies the project's working directory. Defaults to `.`|
|`-d`, `--debug` | Sets the logging level to debug.|
|`-v`, `--verbose` | Enables verbose console output.|

</details>


<details>
  <summary>Examples</summary>

</details>