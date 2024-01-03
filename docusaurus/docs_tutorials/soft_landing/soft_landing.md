---
sidebar_position: 10
sidebar_label: 'Soft Landing'
---

# Soft Landing Tutorial
## Overview

This is a ROS 2 simulation of soft landing of an object.  
In the ROS 2 system we have two nodes: the first represents the `dynamics` and the second one is the `controller`.
- **System dynamics** - The system's equation of motion is the kinematic equation of a free body fall.  
for more information see [Soft Landing](https://github.com/CITROS-garden/soft_landing)  

- **The controller** - The controller is based on this paper:
*S. Gutman, "Rendezvous and Soft Landing in Closed Form via LQ Optimization," 2019 27th Mediterranean Conference on Control and Automation (MED), Akko, Israel, 2019, pp. 536-540, doi: 10.1109/MED.2019.8798572.*

![jpg](img/soft_landing_control.jpg "soft landing")

With CITROS, you can easily run multiple simulations and compare the results to find the optimal solution. It's a powerful tool that saves time and effort, allowing you to focus on improving your designs and achieving your goals.  

![jpg](img/soft-landing-of-a-spacecraft-on-the-moon.png)

## Prerequisites

1. Please make sure you have all the [necessary softwares](../../docs/guides/getting_started#softwares-to-work-with-citros) to work with CITROS installed on your computer.
2. Install [Visual Studio code](https://code.visualstudio.com/download).
3. We strongly recommend that you work with [dockers](../../docs/guides/dockerfile_overview). However, if you wish to work without dockers, please refer to the [.devcontainer](https://github.com/citros-garden/soft_landing/tree/main/.devcontainer) directory in project's repo, the dependencies you need are in the `Dockerfile` and `install.sh` files.

## Table of Contents
1. [Installation](#installation)
2. [Workspace Overview](#workspace-overview)
3. [CITROS Initialization](#citros-initialization)
4. [Scenario](#scenario)
5. [Running the Scenario Using CITROS](#running-the-scenario-using-citros)
6. [Results](#results)

## Installation
   
1. Clone the repository:

 ```sh
 git clone git@github.com:citros-garden/soft_landing.git
   ```
2. Open the repository in the [VScode Dev Container](../../docs/guides/getting_started#open-project-in-vscode-dev-container).

## Workspace Overview
After all the prerequisites done, we can start configuring our project.  
This is a list of all the ROS 2 parameters that can be control by the user wish:



|     Parameter | Description | Package |
| -------- |    ------- |  ------- | 
| r_x0 , r_y0, r_z0 | initial position| dynamics |
| v_x0 ,v_y0,v_z0 | initial velocity |  dynamics |
| g_x , g_y , g_z | gravity vector | dynamics |
| dt | time interval | dynamics |
|  setpoint_r_x , setpoint_r_y , setpoint_r_z , |  ending position |controller |  
|  setpoint_v_x , setpoint_v_y , setpoint_v_z , |  ending velocity |controller |
|  g  | gravity parameter | controller |
| um |  acceleration limit | controller |
| e | stoping condition value | controller |
| dt | time interval | controller |

[citros_cli](/docs/cli/config_params) provides more information about how to change the parameters by the user.

The launch files:  
 `dynamics_controller.launch.py` launch the dynamics with the controller and `dynamics.launch.py` launch only the dynamics.  
 You can view the launch files [here](https://github.com/citros-garden/soft_landing/tree/main/src/dynamics/launch).

## CITROS Initialization

1. [Install CITROS](../../docs/guides/getting_started#installation).
2. Follow [these steps](../../docs/guides/getting_started#initialization) to Initialize CITROS.

Now you can see ```.CITROS``` directory in the explorer. 

## Scenario
Let's say we wish to land safely at some point on the moon's surface. To do that, we need a controller that can manage our velocity and guide us to the landing point while minimizing our speed.  
There are many controller ideas but we need to determine their effectiveness and limitations.  
Here we will try to find the limitations of the controller that based on the paper above by using CITROS.

The control guidance is a time-to-go dependent affine function. Time-to-go is obtained by solving a quartic polynomial equation for the initial conditions.  
So by giving the initial velocity value, we could check the validation of that controller.
Instead of giving some random values to the initial velocity of the simulation until we can find the limits, CITROS allows us to run multiple simulations parallel at a short time and also provide random values of the initial velocity.  
In this scenario,let's say that each initial velocity parameter (v_x0, v_y0, v_z0) will be distributed normally: N($\mu$, $\sigma$).  

By configuring the velocity parameters using $\mu$ and $\sigma$, we can identify the conditions under which the controller is most likely to fail.



## Running the Scenario Using CITROS

To configure the scenario described [above](#scenario), I created a `default_param_setup.json` file located in `.citros/parameter_setups` and a `function object` located in `.citros/parameter_setups/functions` to randomize the initial velocity with $\mu$ and $\sigma$ for each parameter.  
For the initial validation of the controller, I chose random values of $\mu$ and $\sigma$.

First ensure that the project has been [built and sourced](../../docs/guides/getting_started#build-the-project)

you're now ready to run a CITROS simulation, by using the run command:
```sh
citros run -n 'test' -m 'testytest'
? Please choose the simulation you wish to run:  
simulation_dynamics
❯ simulation_dynamics_controller
```

The `simulation_dynamics_controller` launches the `dynamics_controller.launch.py` file and `simulation_dynamics` launches the `dynamics.launch.py` file.  
To execute, select the launch file and press the `Enter` button.  
Wait for the output in the terminal.  

### Running on The Cloud

[Upload project to CITROS Server](../../docs/guides/getting_started#upload-to-citros-server)

Finally, we can run it in the cloud, simply add ```-r``` to the terminal command: 
```bash 
ros@docker-desktop:/workspaces/soft_landing$ citros run -n 'test' -m 'testytest' -r
? Please choose the simulation you wish to run:   
simulation_dynamics
❯ simulation_dynamics_controller
```

The simulation will now commence on the CITROS server, and the results will be uploaded automatically to the CITROS database.

For more run options check [cli commands documentation](/docs/cli/cli_commands#command-run). 

You can also **(run simulations/docs/cli/simulations/sim_step_by_step)** directly from [Runs tab](https://citros.io/soft_landing/batch) in your soft landing repository.

## Results

The results were:

![Alt text](img/image-7.png)

And by getting the miss distance and miss velocity we could show a figure of all the runs.  

![Alt text](img/image-8.png)  


![Alt text](img/image.png)

The full report with the data access and error analysis was generated using the data analysis package, can be found [here](https://CITROS.io/soft_landing/blob/main/notebooks/Soft_landing_analysis.ipynb).

After obtaining the results from CITROS and analyzing the data through visual graphs, we can confirm that the controller has met our demands. Most of the runs indicate that the miss distance and miss velocity are within our desired range.  

*In summary, for 100 simulations with different starting velocities*<br />
*we have 8 runs that miss the target (not within the radius 0.01[m] from the target).*<br />
*And we have 6 fail runs that land with a miss distance greater than 0.01[m] and miss velocity greater than 1[m/s]*

However, it's important to note that this is just the initial validation of the controller. We will need to conduct additional simulations to further validate our findings. Additionally, we can experiment with different values of $\mu$ and $\sigma$ for each parameter.   





