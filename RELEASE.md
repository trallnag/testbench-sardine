# Release

This document describes the release process and is targeted at maintainers.

## Preparation

Pick a name for the new release. It must follow
[Semantic Versioning](https://semver.org). For example `1.2.0` or `5.10.7`. In
the following the name is referenced with `$VERSION`.

```shell
VERSION=1.0.1
```

Make sure that the "Unreleased" section in the [changelog](CHANGELOG.md) is
up-to-date. Feel free to adjust entries for example by adding additional
examples or highlighting breaking changes.

Move the content of the "Unreleased" section that will be included in the new
release to a new section with an appropiate title for the release. Should the
"Unreleased" section now be empty, add "Nothing." to it.

Open [`src/testbench_sardine/__init__.py`](src/testbench_sardine/__init__.py)
and set the `__version__` variable to `$VERSION`. You can also use the following
command to do this.

```shell
sed -i "/^__version__/c\__version__ = \"$VERSION\"" src/*/__init__.py
```

Bump the version using Poetry next.

```shell
poetry version $VERSION
```

Continue with the next section.

## Trigger

Stage and commit the changes. Remember to sign the commit.

```shell
git add CHANGELOG.md src/*/__init__.py pyproject.toml
git commit -S -m "chore: Prepare release v$VERSION"
```

Ensure that the commit is signed.

```
git log --show-signature -1
```

Tag the commit with an annotated and signed tag.

```
git tag -s v$VERSION -m ""
```

Ensure that the tag is signed.

```
git show v$VERSION
```

Push changes on the master branch.

```
git push origin master
```

Check workflow runs in GitHub Actions and ensure everything is fine.

Now push the tag itself.

```
git push origin v$VERSION
```

This triggers the release workflow which will build a package, publish it to
PyPI, and draft a GitHub release.

## Wrap Up

Ensure that the new set has been published to PyPI
[here](https://pypi.org/project/testbench-sardine).

Go to the release page of this project on GitHub
[here](https://github.com/trallnag/testbench-sardine/releases) and review
the automatically created release draft.

Add release notes by extracting them from the [changelog](CHANGELOG.md).

Publish the release draft.
