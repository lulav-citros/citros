# Website1

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

### Installation

```
$ yarn
```

### Local Development

```
$ yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```
$ yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

Using SSH:

```
$ USE_SSH=true yarn deploy
```

Not using SSH:

```
$ GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.




# docker:
```bash
docker build --target development -t docs:dev .
docker run -p 3000:3000 docs:dev


docker build -t docusaurus:latest .
docker run --rm -p 3000:80 docusaurus:latest
```



```bash
# if building from linux machine
# docker build . docker-doc
docker build -t citros-doc . 
# *** when building from MAC M1 chip add FROM --platform=linux/amd64 ***
docker buildx build --platform linux/amd64 -t citros-doc .   


#run: 
docker run --rm -p 3000:80 citros-doc
# upload to google artifact registry

docker tag citros-doc registry.local:32000/citros/citros-docker/citros-doc
docker push registry.local:32000/citros/citros-docker/citros-doc

docker tag citros-doc us-central1-docker.pkg.dev/citros/citros-docker/citros-doc
docker push us-central1-docker.pkg.dev/citros/citros-docker/citros-doc

``` 