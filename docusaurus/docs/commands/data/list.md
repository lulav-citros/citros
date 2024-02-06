show table of all batch runs in local `.citros/data` folder 

```
citros data list
```

```
┌────────────────────────────┬──────────┬──────────┬───────────────────────────────────┬──────────┬─────────────┬──────────────────────────────────┐
│ Simulation                 │ Run name │ Versions │ message                           │   status │ completions │ path                             │
├────────────────────────────┼──────────┼──────────┼───────────────────────────────────┼──────────┼─────────────┼──────────────────────────────────┤
│ simulation_cannon_analytic │          │          │ This is a default batch message   │ UNLOADED │      1      │ .citros/data/simulation_cannon_a │
│                            │          │          │ from citros                       │          │             │ nalytic/citros/20240130183552/   │
│                            │          │          │ This is a default batch message   │ UNLOADED │      1      │ .citros/data/simulation_cannon_a │
│                            │          │          │ from citros                       │          │             │ nalytic/citros/20240130183527/   │
│                            │          │          │ This is a default batch message   │ UNLOADED │      5      │ .citros/data/simulation_cannon_a │
│                            │          │          │ from citros                       │          │             │ nalytic/citros/20240124094612/   │
│                            │          │          │ This is a default batch message   │ UNLOADED │      3      │ .citros/data/simulation_cannon_a │
│                            │          │          │ from citros                       │          │             │ nalytic/citros/20240124093700/   │
...

```