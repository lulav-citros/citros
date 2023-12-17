# Quick Start

## Run Locally

In essence, the CITROS CLI is a collection of numerous commands, but to quickly get started with running a simulation once using the default parameter values, only two straightforward commands are required:

    $ citros init
    User is not logged in. Initializing Citros locally.
    Initialized Citros repository.
    $ citros run -n "some_batch_name" -m "some_message"

The first command, `citros init`, sets up a new `.citros` repository. If you are logged in, it will clone the `.citros` directory from a remote repository.

The second command, `citros run`, executes a simulation of the provided name a designated number of times. If you don't specify a simulation name (not to be confused with a batch name, which is mandatory by default), an interactive menu will appear, letting you select from the available simulations. If the "completions" value, representing the number of times the simulation should run, isn't specified, a single instance of the simulation will be executed.

## Run Remotely (on the cloud)

In order to run your simulation on the cloud, two (possibly three) additional steps are required:

1. First of all, you would need to login to CITROS by running `citros login`. 
2. After logging in, and before running `citros init`, **if you haven't done so already**, you would need to setup your ssh keys in order communicate with the CITROS server. One way to do this is through the [CITROS](https://citros.io) web GUI (which provides detailed instructions), but this may also be done through the CLI by running `citros setup-ssh`. see details [here](../commands/cli_commands.md#command-setup-ssh).

3. Once ssh is setup, you may run `citros init`. This will pull an existing CITROS repository from the CITROS server, or create a new one.

4. Now, you will need to build a docker image of your simulation and upload it CITROS, by running `citros docker-build-push`.

5. Finally, you may run your simulation on the cloud by simply adding `-r` to the `citros run` command. The image you uploaded in the previous step will be run the number of times you specified.

To sum up, assuming you have already setup your ssh keys, the following example will run a simulation 10 times on the CITROS cloud:

    $ citros login
    $ citros init
    $ citros docker-build-push
    $ citros run -n "some_batch_name" -m "some message" -r -c 10

**Note:** for clarity, the CITROS output was not given in the above example. See individual commands.