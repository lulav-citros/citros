# cli
CITROS cli

# projest main directories:
- `.citros` - contain all the citros information
- `/runs` - contain all the generated data 

# Commands

- citros [init](#initialization)
- citros [doctor](#doctor)
- citros [run](#run)
- citros [simulation](#simulation)
- citros [parameters](#parameters)
- citros [launch](#launch)
- citros [batch](#batch)
- citros [data](#data-access)
- citros [report](#reports)
- citros [observability](#observability)
- usefull [usefull](#usefull)

---
## initialization
analyze the ROS2 project and initialize the .citros folder with all the files needed to operate citros

```bash
citros init 
    [-d | --destination] <repository folder>

```

## doctor
checks for problems in .citros folder and suggests fixes

```bash
citros doctor
    [-d | --destination] <repository folder>
```

## Run
starts a simulation locally or on remote

```bash
citros run
    [-gh | --github] #iniate an action that will runs the simulation on github as a workflow. 

    [-c] #completions

    [-o] #destination folder defaults to .citros/runs

    [-D] #dockerized - we will run dockerzed version of the simulation (can run parallel simulations on the same machine)

    [-p] #parallelism ? do we need it or can we know how many cpu available and devide it by the requested number of cpus per cpu 8 (available cpu) / 2 (requested cpu) = 4 (number of parallel runs)

    [-r] #remote run

    [-s] #simulation name

    [-t] #time limit

    [-v] #verbose

    [-w] #workflow
```

## Simulation
all simulation operations
```bash
citros simulation
    [-n] simulaiton name 
# prompt simulation list to choose from
# after shoosing simulation prompt another question 
# run/info/delete

citros simulation run
    [-n] simulaiton name 
# prompt another question 
# run/info/delete

citros simulation list 
    [-m] match pattern
# list all simulations list
```

## Parameters
all parameters operations
```bash
# ROS2 parameter
citros parameter
    [-n] name
    [-p] package 
    [-n] node 
    [-m] match pattern
# List the parameters for each package/node in the project

#.citros 
citros parameter setup     
    [-n] name
# get parameter setup details
# if nothing specified prompt a list of all the parameter setups to choose from

citros parameter setup new     
    [-n] name
    [-m] match pattern
    [-c] #copy from [parameter setup name]
# create new parameter setup

citros parameter setup list    
    [-m] match pattern
# List all the parameter setups and match pattern
```

## Launch
all lauch operations
```bash

citros launch 
    [-n] name
    [-m] match pattern
# list all the launch files
```

## Data access
This DB will be used wo store the indexed bags for the 

```bash
citros data
    [-d | --dir] # data directory (.cittros/runs)
# return a snapshot of the /runs folder
# how many runs, and a detail about each run/simulation

citros data list 
    [-d | --dir] # data directory
    [-s] simulation


##################
### Hot reload ###
##################
# starts server to listen for data access requests.
citros data service
    [-d | --dir] # data directory
    [-p] #port
    [-v] #verbose
    [-D] #dockerized

# prints the available data (db status) size, mem, how many batches loaded, etc...
citros data service status
    [-d | --dir] # data directory


# DB related
# create a new PGDB instance 
# creates all permissions and tables needed for CITROS
citros data db create
    [-d | --dir] # data directory
    [-n] #name of the DB
    [-p] #port of the DB
    [-u] #user of the DB
    [-P] #password of the DB
    [-v] #verbose
    [-D] #dockerized

# prints the available data (db status) size, mem, how many batches loaded, etc...
citros data db status
    [-d | --dir] # data directory

# clean the DB from data that wasend used for more then -d days -h hours -m minutes
citros data db clean
    [-d] #days
    [-h] #hours
    [-m] #minutes
    [-v] #verbose
    [-D] #dockerized
```
<details>
<summary>REST API details</summary>
  
The user can check the availability of the data in a rest api that will be created by the service.

### check the availability of the data
GET http://{domain}:{port}/{batch run name}
```json
{
    "status": "unloaded",
    "last access": "2020-01-01 00:00:00",
    ...
}
```
### request access for batch run
POST http://{domain}:{port}/{batch run name}
```json
{
    "status": "loading",
    "last access": "2020-01-01 00:00:00",
    ...
}
```
</details>



## Reports
A report is a signed set of generated notebooks with batch run data.
this report can be shared trough CITROR or sent as a file.
```bash
# generate a signed report from a list of notebooks and use the data from the batch run specified.
citros report generate notebook.ipynb simulation/batch_run_name
    [-n] report_name *IF NOT PROVIDED A PROMPT WILL FOLLOW

# generate a report from report_name as specified unser .citros/reports/report_name.json
citros report generate 
    [-n] report_name *IF NOT PROVIDED A PROMPT WILL FOLLOW
``` 

## Observability
start a node that will measue system / ros metrics and publish all to a topic

```bash
citros observability
    [-c] #channel
    [-t] #topic
    [-v] #verbose
```



# usefull
```bash
# build
docker build -t citros .

# run 
citros data access
# or all commands can run inside docker
# run citros cli inside docker
docker run -it -p 8000:8000 citros data access
```






---
---
---
---
---
---
---
---
---

# CLI Overview

Welcome to CITROS CLI. [CITROS](https://citros.io/) serves as an innovative platform for executing ROS project simulations, automating integration, and conducting in-depth performance analysis.

The CITROS CLI offers ROS 2 developers a seamless interface to launch multiple ROS simulations for a specific project with just a single command. Beyond setting static parameter values, it empowers users with the flexibility to utilize function objects. This means you can craft dynamic simulation environments where each execution produces unique parameter values, whether they're sourced from standard numpy functions or tailored via user-defined computations. Moreover, these operations can be executed offline without relying on any external dependencies.

CITROS takes its capabilities a notch higher when the user logs in. Once logged in, users can tap into the full potential of CITROS, ranging from running parallel simulations in the cloud to utilizing advanced data analysis tools for performance examination. Additionally, automatic report generation is a standout feature, aiding in effortless documentation of your work. Beyond these technical perks, logging in also paves the way for collaborative work, allowing you to engage and exchange ideas with team members.

For additional information, please refer to the CITROS documentation. This will provide you with comprehensive insights and detailed instructions for effective usage of CITROS in general and CITROS CLI in particular, and their full suite of features.

We are dedicated to enriching your ROS project simulation experience, and this package is our contribution to that cause.

## Table of Contents
1. [Quick Start](doc/overview/cli_quickstart.md)
2. [Installation](doc/overview/cli_install.md)
4. [CLI Commands](doc/commands/cli_commands.md)
5. [Citros Repository directory and file Structure](doc/structure/citros_structure.md) 
6. [Citros Repository Configuration](doc/configuration/config_params.md)
7. [User Templates](doc/user_templates.md)

