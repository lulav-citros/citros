## `citros run`

```sh
$ citros run [dir <folder_name>] 
             [-d | --debug] 
             [-v | --verbose]
             [-s, --simulation_name] 
             [-b, --batch_id]
             [-n, --batch_name] 
             [-m, --batch_message] 
             [-i, --run_id] 
             [-c, --completions]
             [-r, --remote] 
             [-k, --key] 
             [-l, --lan_traffic] 
             [--branch] 
             [--commit]
```

### Description
The `run` command launches a simulation either locally on your machine, or remotely on the CITROS cluster.

#### Prerequisites:
Ensure that the project has been built and sourced, for example:
    
    $ colcon build
    $ source install/local_setup.bash

If you'd like to run your simulation remotely, you would also need to make sure:
1. You're logged in (via `citros login`).
2. You've built and pushed a docker image of your project (using `citros docker-build-push`).
3. Your `.citros` directory is synched with the remote repository (using `citros commit` and `citros push`). 


If no simulation name was provided, an interactive session will begin, and you will be prompted to select a simulation from the list of available simulations (via up, down and enter keys). 


#### Examples
```bash
$ citros run
? Please choose the simulation you wish to run 
❯ simulation_cannon_analytic
    simulation_cannon_numeric
```