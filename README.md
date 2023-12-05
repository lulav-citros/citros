# cli
CITROS cli


## Commands

`citros init`

initialize the .citros folder with all the files needed to operate citros

### flags:

`-d` `--destination` repository folder 

--- 
`citros doctor`

checks for problems in .citros folder and suggests fixes

### flags:
`-d` `--destination` repository folder 

--- 
`citros run`

starts a simulation locally or on remote

### flags:
`-gh` `--github` iniate an action that will runs the simulation on github as a workflow. 

`-c` completions

`-o` destination folder defaults to .citros/runs

`-d` dockerized - we will run dockerzed version of the simulation (can run parallel simulations on the same machine)

`-p` parallelism ? do we need it or can we know how many cpu available and devide it by the requested number of cpus per cpu 8 (available cpu) / 2 (requested cpu) = 4 (number of parallel runs)

`-r` remote run

`-s` simulation name

`-t` time limit

`-v` verbose

`-w` workflow

--- 
`citros batch list`

lists all batches + status

--- 
`citros batch get <id>`

get the data for a batch

