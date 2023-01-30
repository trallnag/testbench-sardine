# Pre-Commit

Used for maintaining Git hooks. As it is written in Python, for
example [`pipx`](https://github.com/pypa/pipx) can be used to install it.

- <https://pre-commit.com/>
- <https://github.com/pre-commit/pre-commit>

Whenever this repository is initially cloned, execute:

```
pre-commit install --install-hooks
pre-commit install --install-hooks --hook-type commit-msg
```

Pre-commit should now run on every commit. It is also used in GitHub Actions.

Configured via [`../.pre-commit-config.yaml`](../.pre-commit-config.yaml).

## Cheat Sheet

Run against all files.

```shell
pre-commit run -a
```

Run specific hook against all files.

```shell
pre-commit run <hook> -a
```

Update hooks.

```
pre-commit autoupdate
```
