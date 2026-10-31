# copier-template-copier-template

[![Tests](https://github.com/cbrown1234/copier-template-copier-template/actions/workflows/test.yml/badge.svg)](https://github.com/cbrown1234/copier-template-copier-template/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A [Copier](https://copier.readthedocs.io/) meta-template — a template that scaffolds new Copier templates with modern Python project tooling preconfigured.

## Features

- **Best Practices:** template in subdirectory, [multiple (composable) template compatibility](https://copier.readthedocs.io/en/stable/configuring/#applying-multiple-templates-to-the-same-subproject)
- **Test harness included** pytest setup with examples and helpers, ready to test your template, and it's usage
- **Modern Batteries included** uv, [semantic release](https://python-semantic-release.readthedocs.io/), Renovate, and [go-task](https://taskfile.dev/) automation all preconfigured
- **CI/CD out of the box** Supports GitLab CI or GitHub Actions, with matrix testing across Python versions
- **Optional Copier extensions**
    - [Pydantic validation](https://pypi.org/project/copier-pydantic/) for answers
    - [local Jinja extensions](https://pypi.org/project/copier-template-extensions/)

## Install Copier

```bash
uv tool install copier
# or
pipx install copier
# or
brew install copier
```

## Usage

### Create a new project

```bash
# SSH
copier copy git@github.com:cbrown1234/copier-template-copier-template.git /path/to/new-template
# HTTPS
copier copy https://github.com/cbrown1234/copier-template-copier-template.git /path/to/new-template
```

For non-interactive usage (scripts, CI, AI agents), see `copier copy --help` for the `--defaults` and `--data` flags.

### Update an existing project

```bash
cd /path/to/your/project
copier update --answers-file .copier-answers.copier-template.yml
```

For non-interactive updates, use `--skip-answered` to reuse all existing answers without prompting.

## Demo

[![demo](https://asciinema.org/a/bFcXBgVNxzAaNAjO.svg)](https://asciinema.org/a/bFcXBgVNxzAaNAjO)

## Development

Prerequisites: [uv](https://docs.astral.sh/uv/) and [Task](https://taskfile.dev/).

Run `task --list` to see available commands. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full development guide.

### Self-hosted

This repo uses itself. See `.copier-answers.copier-template.yml` for the answers used.

### Pre-commit composition

This template does not generate a `.pre-commit-config.yaml`. Pre-commit configuration is expected to be handled by a separate template that composes with this one.

## Beta features

Beta features are hidden: Copier doesn't ask about them, and they're off unless you opt in. Opting in records the answer, so `copier update` keeps the feature. Projects that don't opt in are asked as normal once a feature graduates.

| Flag | Description |
|---|---|
| `include_actions_lockfile` | GitHub only. Verify the [GitHub Actions workflow lockfile](https://docs.github.com/en/actions/concepts/security/workflow-dependency-lockfiles) in CI, and configure Renovate to keep it up to date |
| `gitlab_non_root_tests` | GitLab only. Run the generated CI tests as a non-root user, so permission issues (e.g. root-owned files from docker bind mounts) show up in CI as they would locally |

### Usage

Opt in when creating a project:

```bash
copier copy -d include_actions_lockfile=true <template-url> /path/to/new-template
```

Or add it to an existing project:

```bash
copier update -d include_actions_lockfile=true --answers-file .copier-answers.copier-template.yml
```

Pass `-d <flag>=true` for each flag you want. To opt out, run `copier update` with `-d <flag>=false`.
