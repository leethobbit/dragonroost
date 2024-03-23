

<div align="center">

# Dragonroost is under heavy development and is very feature-light right now. You can currently add/edit/delete animals (and their associated species, status, and location) and add basic person entries.

[![Build status](https://github.com/leethobbit/dragonroost/workflows/build/badge.svg?branch=master&event=push)](https://github.com/leethobbit/dragonroost/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/dragonroost.svg)](https://pypi.org/project/dragonroost/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/leethobbit/dragonroost/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/leethobbit/dragonroost/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/leethobbit/dragonroost/releases)
[![License](https://img.shields.io/github/license/leethobbit/dragonroost)](https://github.com/leethobbit/dragonroost/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

Dragonroost is an animal shelter/rescue management app, written in Python using the Django web framework.

</div>

## Roadmap

This app is in the early stages of development.  For a general idea of what I'm trying to do, please check out the [roadmap](ROADMAP.md).

## Very first steps

### Initialize your code

1. Initialize `git` inside your repo:

```bash
cd dragonroost && git init
```

2. If you don't have `Poetry` installed run:

```bash
task poetry-download
```

3. Initialize poetry and install `pre-commit` hooks:

```bash
task install
task pre-commit-install
```

4. Run the codestyle:

```bash
task codestyle
```

### Set up bots

- Set up [Dependabot](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates) to ensure you have the latest dependencies.
- Set up [Stale bot](https://github.com/apps/stale) for automatic issue closing.

### Poetry

Want to know more about Poetry? Check [its documentation](https://python-poetry.org/docs/).

<details>
<summary>Details about Poetry</summary>
<p>

Poetry's [commands](https://python-poetry.org/docs/cli/#commands) are very intuitive and easy to learn, like:

- `poetry add numpy@latest`
- `poetry run pytest`
- `poetry publish --build`

etc
</p>
</details>

### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.
- Make a commit to `GitHub`.
- Create a `GitHub release`.
- And... publish 🙂 `poetry publish --build`

Articles:

- [Open Source Guides](https://opensource.guide/).
- [A handy guide to financial support for open source](https://github.com/nayafia/lemonade-stand)
- [GitHub Actions Documentation](https://help.github.com/en/actions).
- Maybe you would like to add [gitmoji](https://gitmoji.carloscuesta.me/) to commit names. This is really funny. 😄

## 🚀 Features

### Development features

- Supports for `Python 3.9` and higher.
- [`Poetry`](https://python-poetry.org/) as the dependencies manager. See configuration in [`pyproject.toml`](https://github.com/leethobbit/dragonroost/blob/master/pyproject.toml) and [`setup.cfg`](https://github.com/leethobbit/dragonroost/blob/master/setup.cfg).
- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort) and [`pyupgrade`](https://github.com/asottile/pyupgrade).
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with code-formatting.
- Type checks with [`mypy`](https://mypy.readthedocs.io); docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint); security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit)
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).
- Ready-to-use [`.editorconfig`](https://github.com/leethobbit/dragonroost/blob/master/.editorconfig), [`.dockerignore`](https://github.com/leethobbit/dragonroost/blob/master/.dockerignore), and [`.gitignore`](https://github.com/leethobbit/dragonroost/blob/master/.gitignore). You don't have to worry about those things.

### Deployment features

- `GitHub` integration: issue and pr templates.
- `Github Actions` with predefined [build workflow](https://github.com/leethobbit/dragonroost/blob/master/.github/workflows/build.yml) as the default CI/CD.
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc with [`Taskfile`](https://github.com/leethobbit/dragonroost/blob/master/taskfile#L89). More details in [taskfile-usage](#taskfile-usage).
- [Dockerfile](https://github.com/leethobbit/dragonroost/blob/master/docker/Dockerfile) for your package.
- Always up-to-date dependencies with [`@dependabot`](https://dependabot.com/). You will only [enable it](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates).
- Automatic drafts of new releases with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). You may see the list of labels in [`release-drafter.yml`](https://github.com/leethobbit/dragonroost/blob/master/.github/release-drafter.yml). Works perfectly with [Semantic Versions](https://semver.org/) specification.

### Open source community features

- Ready-to-use [Pull Requests templates](https://github.com/leethobbit/dragonroost/blob/master/.github/PULL_REQUEST_TEMPLATE.md) and several [Issue templates](https://github.com/leethobbit/dragonroost/tree/master/.github/ISSUE_TEMPLATE).
- Files such as: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.
- [`Stale bot`](https://github.com/apps/stale) that closes abandoned issues after a period of inactivity. (You will only [need to setup free plan](https://github.com/marketplace/stale)). Configuration is [here](https://github.com/leethobbit/dragonroost/blob/master/.github/.stale.yml).
- [Semantic Versions](https://semver.org/) specification with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).

## Installation

```bash
pip install -U dragonroost
```

or install with `Poetry`

```bash
poetry add dragonroost
```



### Taskfile usage

[`taskfile`](https://github.com/leethobbit/dragonroost/blob/master/taskfile) contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
task poetry-download
```

To uninstall

```bash
task poetry-remove
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
task install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
task pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort` and `black`.

```bash
task codestyle

# or use synonym
task formatting
```

Codestyle checks only, without rewriting files:

```bash
task check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black` and `darglint` library

Update all dev libraries to the latest version using one comand

```bash
task update-dev-deps
```

<details>
<summary>4. Code security</summary>
<p>

```bash
task check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
task check-safety
```

</p>
</details>

</p>
</details>

<details>
<summary>5. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
task mypy
```

</p>
</details>

<details>
<summary>6. Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
task test
```

</p>
</details>

<details>
<summary>7. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
task lint
```

the same as:

```bash
task test && task check-codestyle && task mypy && task check-safety
```

</p>
</details>

<details>
<summary>8. Docker</summary>
<p>

```bash
task docker-build
```

which is equivalent to:

```bash
task docker-build VERSION=latest
```

Remove docker image with

```bash
task docker-remove
```

More information [about docker](https://github.com/leethobbit/dragonroost/tree/master/docker).

</p>
</details>

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/leethobbit/dragonroost/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/leethobbit/dragonroost/blob/master/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## 🛡 License

[![License](https://img.shields.io/github/license/leethobbit/dragonroost)](https://github.com/leethobbit/dragonroost/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/leethobbit/dragonroost/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{dragonroost,
  author = {Dan King},
  title = {Dragonroost is an animal shelter/rescue management app, written in Python using the Django web framework.},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/leethobbit/dragonroost}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
