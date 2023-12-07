# Git Commit Guidelines

The official doc [git-commit-guidlines] or [commit-message-format]

```html
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

example: 

```bash 
git commit -m "docs(readme.md): change

changed the doc

pr: sha"
```

```python 
allowed types = [
    "build",
    "chore",
    "ci",
    "docs",
    "feat",
    "fix",
    "perf",
    "style",
    "refactor",
    "test",
]
minor types = ["feat"]
patch types = ["fix", "perf"]
```

# Versioning locally
we are working with [semantic-release] for versioning our package. 

```bash
$ python3 setup.py version 
```

this command will release a new version (major, minor or patch) if it found the right commit `<type>`
see how to do it [semantic-release]


# Install locally


```bash
$ python3 -m pip install -e .
```

[semantic-release]: https://python-semantic-release.readthedocs.io/

[commit-message-format]: https://python-semantic-release.readthedocs.io/en/latest/commit-parsing.html

[git-commit-guidlines]: https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits