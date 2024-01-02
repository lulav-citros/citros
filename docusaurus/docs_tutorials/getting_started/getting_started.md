---
sidebar_position: 1
sidebar_label: 'Getting Started'


# Install softwares
# install citros
# clone 
# open in container
# build + source

# ??install citros
# init citros
# run local
# run remote

# build + source
# commit
# push
# run


---

# Getting Started

## Prerequisites for Working With CITROS

### Softwares to Work with CITROS

Download and install the following to work with CITROS

- [Python3](https://www.python.org/downloads/)
- [git](https://git-scm.com/)
- [Docker](https://docs.docker.com/get-docker/) - To understand why CITROS uses Docker, read [CITROS usage in Dockerfile](../dockerfile_overview/dockerfile_overview.md).

### Working With CITROS on Web

- You need a working internet connection.
- Sign up to [CITROS](https://citros.io) and remember your login credentials.

## Installation

To install CITROS using pip, open terminal and write the following command:

    $ pip install citros 

You can verify that the installation succeeded by running 

```bash
$ citros -V
```
:::tip
If you ran the `pip install citros` command and you still getting 
```bash
 $ citros: command not found
```
Try running:
```bash
 $ source ~/.profile 
```
This should solve your problem and you should be able to run citros commands, otherwise [contact us](https://discord.com/).
:::
## Clone CITROS Garden Project

All the projects can be found [here](https://github.com/orgs/citros-garden/repositories)

To clone the repository:
 ```sh
 git clone git@github.com:citros-garden/repository_name.git
   ```

## Run Project in VScode

### Open Project in VScode Dev Container

1. Open the cloned repository in VScode:

 ```sh
 cd ~/project-name
 code .
 ```
2. Open and run Docker.
3. Open the project in VScode.
4. Press on the bottom left corner icon.

![Alt text](img/container_corner.png)

5. Choose **Reopen in Container**

![Alt text](img/container_open_container.png)

6. Open VScode terminal and make sure you are in the right location. <br />
 ```    
 ros@docker-desktop:/workspaces/[Project Name]$
 ```

7. [Build the project](#build-the-project)

### Build the project
 ```bash
 $ colcon build
 $ source install/local_setup.bash
 ```
## Initialization

### Log in to CITROS

First and foremost, we need to log in:
```bash
$ citros login
email: example@lulav.space
Password: 
User logged in.
```

### Set up SSH

This process only needs to be performed once per machine, and can be performed either using the CITROS website or using CITROS CLI
<Tabs>
<TabItem value="citros_cli" label="SSH Setup with CITROS CLI">

```bash
citros setup-ssh
```

for further details, see the [CLI Documentation](https://citros.io/doc/docs_cli)
</TabItem>

<TabItem value="citros_web" label="SSH Setup with CITROS Website">

2. [Navigate to SSH Keys Settings](https://citros.io/settings?tab=ssh_keys).

3. Click "New SSH Key" button

4. Enter SSH key name.

5. Paste the public key.

6. Click "Add" button to add the SSH Key to the account.

7. The new key will be added to the list item.

for further details, see the [Adding a New SSH Key Documentation](https://citros.io/doc/docs/authentication/ssh/ssh_add_new)

</TabItem>
</Tabs>

### Init CITROS

#### Before Running `citros init`

First and foremost, the `.citros` directory can only be **initialized once**. 
If the `.citros` directory exists in your local project and the project [**already exists on the remote server**](https://citros.io/cannon), you have to delete the `.citros` directory from your project before 
running `citros init` command.

To Check if the project already exists on the remote server:
1. go to [repositories](https://citros.io/repo)

2. Look for your project name either by scrolling through the list or using the search box.

3. If you didn't find your project you may skip the next step.

4. if you found the project, delete the `.citros` directory **from your local project**. 

5. you may continue to the [next step](#running-citros-init). 

#### Running `citros init`

```bash
$ citros init
Checking internet connection...
Checking ssh...
Updating Citros...
Waiting for repo to be ready...
Citros repo successfully cloned from remote.
Creating and checking out a new local branch `main` that will track the remote branch.
Default branch of remote 'origin' set to: main
Citros successfully synched with local project.
You may review your changes via `citros status` and commit them via `citros commit`.
Initialized Citros repository.
```
As you can see, a lot more is happening when you initialize your repository while being logged in. We will not delve into all the details behind the scenes, but as always, feel free to roam through the [CLI Documentation](https://citros.io/doc/docs_cli) for further details.

:::caution Warning

 If you try to run `init` while a `.citros` directory already exists in your project, you will get a response similar to this:
```bash
$ citros init
The directory /workspaces/cannon has already been initialized.
working remotely with [git@citros.io:lulav/cannon.git].
```

 1. If you want to reinitialize your CITROS repository, you'll have to first delete the current `.citros` directory.

2. If you initialized the CITROS repository offline, and it [**doesn't exist** on the remote server yet](https://citros.io/cannon) (i.e. it has not been initialized online by you or anyone else) - then rather than deleting the `.citros` directory, you can run:
 ```bash
 citros add-remote
 ```

 which will add the CITROS server as a remote for your CITROS repo on your behalf, and take care of a few other details that are handled when initializing while being logged in.
 
 At this point it is recommended you commit and push your changes to the remote by running:
 ```bash
 citros commit
 citros push
 ``` 
:::


<!-- 



### Environment Variables
   
   `citros_cli` uses several environment variables, some of which you may change according to your needs, although for the most part, the defaults are likely to be what you want. Generally speaking, most of these are only used by developers of the package, and should not be used.

| ENV | Description | used in |
| --- | --- | --- |
| `CITROS_DOMAIN` | The main domain, defaults to `citros.io` | all packages |
| `CITROS_DIR` | Used by the citros cluster, do not use. | citros |
| `CITROS_SIM_RUN_DIR` | The directory under `.citros/runs` in which all simulation data will be saved (see [runs](/docs_cli/structure/citros_structure#directory-runs)). This can be handy, if your code needs to know this location in order to access some of the files, e.g. parameter setups. | citros | -->

## Upload to CITROS Server
The working directory of your ROS project must be clean. So if you made any changes, simply commit your changes first.
```sh
 citros commit
 citros push
 ```
To run a simulation on the cloud - we need to build a docker image of our ROS project, tag it with the current commit hash for the project, and upload it to CITROS.
all this is accomplished by running a single command:

```bash
citros docker-build-push
``` 

## Simulation Running Options

#### The basic run command is

```sh
citros run -n 'batch_name' -m 'batch_message'
```
This command will run the simulation on your machine, and save all the results under `.citros/runs/[simulation_name]` folder. The content of the folder will contain

- recorded bags
- logs from the simulation and citros itself
- metadata about the run
- metrics and information about the system it was running
- and more.

#### To run more than one simulation add `-c number`

```sh
citros run -n 'batch_name' -m 'batch_message' -c 15
```
This will run 15 simulation and all will be saved as explained above.

#### To run the simulation on the cloud add `-r`

```sh
citros run -n 'batch_name' -m 'batch_message' -r
```

```sh
citros run -n 'batch_name' -m 'batch_message' -r 15
```

after you execute a remote (-r) run command, a link directly to the *runs* tab on the CITROS website will appear in the output
```bash
created new batch_id: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeeeee. Running on Citros cluster. See https://citros.io/cannon/batch/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeeeee.
```

For mor run commands parameters and options check [CLI Commands](/docs/cli/cli_commands).


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';