## `citros report generate`

### Description

A citros report is a collection of `data from a batch of simulations` and a `set of notebooks` that renders into a `signed pdf` report that can be shared. 


### Example:
```bash
$ citros report generate -nb citros_template/notebooks/test1.ipynb --dir . --simulation simulation_cannon_numeric --batch citros --version 20231230092549 --name citros --message "This is a default report message from citros"
```

</details>