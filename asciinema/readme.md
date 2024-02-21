https://docs.asciinema.org/getting-started/

## asciinema Installation
cargo:
https://doc.rust-lang.org/cargo/getting-started/installation.html

```bash
# install cargo
curl https://sh.rustup.rs -sSf | sh

# install asciinema
cargo install --git https://github.com/asciinema/asciinema
# install agg (asciinema gif generator)
cargo install --git https://github.com/asciinema/agg
```



```bash
asciinema rec init.cast --overwrite 

$ citros 
# navigate to init

asciinema play init.cast

agg init.cast init.gif --cols 80 --rows 20
```


```bash
asciinema rec run.cast --overwrite 

$ citros 
# navigate to run

asciinema play run.cast

agg run.cast run.gif --cols 80 --rows 32
```
