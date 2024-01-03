### CITROS 

citros is a suilt of tools for ros2 development and production. 
With this tool you can now easily run many monte carlo simulations scenarios by regenarating any of the parameters before running the simulation and then analyze the changes in the results using our built in tools.

to install citros
```bash
pip install citros --upgrade
```
go to your ros2 workspace and run citros init, this will create a `.citros` folder with all the required files.
```bash
citros init
```

start CITROS db for data indexing. you can load and unload batch runs to the db using the `citros data` command.
```bash
citros data db create
```

to run a simulation run the following command
```bash
citros run 
```
this will start a new batch run that will later can be used for analysis.

you can now access the data for analysis from any postgres client or use our tool for python data analysis. 
out python data analysis package will help you access the data and analyze it. we recoment using it from python notebook that later can be converted to a signed PDF report by running `citros report generate`. 

to analyze the results using citros
```bash
citros report generate 
```
