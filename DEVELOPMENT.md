### Pre-commit

Tool written in Python used for maintaining Git hooks.

- <https://pre-commit.com/>

Whenever this repository is initially cloned, execute:

```shell
pre-commit install --install-hooks
pre-commit install --install-hooks --hook-type commit-msg
```

Pre-commit should now run on every commit.

Read [`docs/devel/pre-commit.md`](docs/devel/pre-commit.md) for more.
