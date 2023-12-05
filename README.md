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

`-d` destination folder defaults to .citros/runs


--- 
`citros batch list`

lists all batches + status

--- 
`citros batch get <id>`

get the data for a batch

