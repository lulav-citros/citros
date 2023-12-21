# cli
CITROS cli

# Commands

- citros [init](#initialization)
- citros [doctor](#doctor)
- citros [run](#run)
- citros [batch](#batch)
- citros [data](#data-access)
- citros [report](#reports)
- citros [observability](#observability)

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




## Batch
all batch operations
```python
#get the data for a batch run
citros batch get <id>

#lists all batches + status
citros batch list

# delete a batch run
citros batch delete <id> | <simulation>/<name>
```

## Data access
This DB will be used wo store the indexed bags for the 

    
```bash
# starts server to listen for data access requests.
citros data access
    [-p] #port
    [-v] #verbose
    [-D] #dockerized

# prints the available data (db status) size, mem, how many batches loaded, etc...
citros data status

# create a new DB instance 
# creates all permissions and tables needed for CITROS
citros data create
    [-n] #name of the DB
    [-p] #port of the DB
    [-u] #user of the DB
    [-P] #password of the DB
    [-v] #verbose
    [-D] #dockerized

# clean the DB from data that wasend used for more then -d days -h hours -m minutes
citros data clean
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

# generate a report from report_name as specified unser .citros/reports/report_name.json
citros report generator report_name
``` 

## Observability
start a node that will measue system / ros metrics and publish all to a topic

```bash
citros observability
    [-c] #channel
    [-t] #topic
    [-v] #verbose
```

