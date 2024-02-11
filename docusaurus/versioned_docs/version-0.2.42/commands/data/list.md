show table of all batch runs in local `.citros/data` folder 

```
citros data list
```

```
                                   Simulation Runs in: .citros/data                                   
┌────────────────────────────┬──────────┬──────────┬────────────┬──────────┬────────────┬────────────┐
│ Simulation                 │ Run name │ Versions │ message    │   status │ completio… │ path       │
├────────────────────────────┼──────────┼──────────┼────────────┼──────────┼────────────┼────────────┤
│ simulation_cannon_analytic │          │          │ This is a  │ UNLOADED │     1      │ .citros/da │
│                            │          │          │ default    │          │            │ ta/simulat │
│                            │          │          │ batch      │          │            │ ion_cannon │
│                            │          │          │ message    │          │            │ _analytic/ │
│                            │          │          │ from       │          │            │ citros/202 │
│                            │          │          │ citros     │          │            │ 4013018355 │
│                            │          │          │            │          │            │ 2/         │
│                            │          │          │ This is a  │ UNLOADED │     1      │ .citros/da │
│                            │          │          │ default    │          │            │ ta/simulat │
│                            │          │          │ batch      │          │            │ ion_cannon │
│                            │          │          │ message    │          │            │ _analytic/ │
│                            │          │          │ from       │          │            │ citros/202 │
│                            │          │          │ citros     │          │            │ 4013018352 │
│                            │          │          │            │          │            │ 7/         │
│                            │          │          │ This is a  │ UNLOADED │     5      │ .citros/da │
│                            │          │          │ default    │          │            │ ta/simulat │
│                            │          │          │ batch      │          │            │ ion_cannon │
│                            │          │          │ message    │          │            │ _analytic/ │
│                            │          │          │ from       │          │            │ citros/202 │
│                            │          │          │ citros     │          │            │ 4012409461 │
│                            │          │          │            │          │            │ 2/         │
│                            │          │          │ This is a  │ UNLOADED │     3      │ .citros/da │
│                            │          │          │ default    │          │            │ ta/simulat │
│                            │          │          │ batch      │          │            │ ion_cannon │
│                            │          │          │ message    │          │            │ _analytic/ │
│                            │          │          │ from       │          │            │ citros/202 │
│                            │          │          │ citros     │          │            │ 4012409370 │
│                            │          │          │            │          │            │ 0/         │
│                            │          │          │ This is a  │ UNLOADED │     3      │ .citros/da │
│                            │          │          │ default    │          │            │ ta/simulat │
│                            │          │          │ batch      │          │            │ ion_cannon │
│                            │          │          │ message    │          │            │ _analytic/ │
│                            │          │          │ from       │          │            │ citros/202 │
│                            │          │          │ citros     │          │            │ 4012409214 │
│                            │          │          │            │          │            │ 2/         │
...

```
## Table columns
- `Simulation`: is the simulation name as shown under `.citros/simulations`
- `Run name`: is the given name for the batch
- `Version`: is the version of the batch run (if you run with same batch name new version created)
- `Message`: the given message for this batch
- `Status`: one of [`LOADED`, `UNLOADED`, `UNKNOWN`] values
- `Completions`: the number of requested simulation completions runs for this batch
- `Path`: the location of the batch