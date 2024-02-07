Interact with recorded batch data.

The first steps is to choose a batch run, then descide what you want to do with it. 

You can view `info`, `load`/`unload` batch to/from DB, `delete` the batch run

```
citros data tree
? Select Simulation: simulation_cannon_analytic
? Select Batch: first
? Select Version: 20240124083131
? Select Action: 
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│❯ Info                                                                                              │
│  Load                                                                                              │
│  Unload                                                                                            │
│  Delete                                                                                            │
│  ---------------                                                                                   │
│  EXIT                                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
## Commands details
- `Info`: will print the info about the chosen batch run. 
- `Load`: will try to load the chosen batch to DB
- `Unload`: will try to unload the chosen batch from DB
- `Delete`: will delete the chosen batch from `.citros/data` folder