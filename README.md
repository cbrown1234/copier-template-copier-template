# copier-template-copier-template

A [Copier](https://copier.readthedocs.io/) meta-template — a template that scaffolds new Copier templates with modern Python project tooling preconfigured.

## Features

- **Best Practices:** template in subdirectory, [multiple (composable) template compatibility](https://copier.readthedocs.io/en/stable/configuring/#applying-multiple-templates-to-the-same-subproject)
- **Test harness included** pytest setup with examples and helpers, ready to test your template, and it's usage
- **Modern Batteries included** uv, semantic release, Renovate, and [go-task](https://taskfile.dev/) automation all preconfigured
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
copier copy git@gitlab.com:browniantech/copier-template-copier-template.git /path/to/new-template
# HTTPS
copier copy https://gitlab.com/browniantech/copier-template-copier-template.git /path/to/new-template
```

### Update an existing project

```bash
cd /path/to/your/project
copier update --answers-file .copier-answers.copier-template.yml
```

## Demo

[![demo](https://asciinema.org/a/b55vKtHm1GVDkRzL.svg)](https://asciinema.org/a/b55vKtHm1GVDkRzL)

## Development

Prerequisites: [uv](https://docs.astral.sh/uv/) and [Task](https://taskfile.dev/).

Run `task --list` to see available commands. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full development guide.

### Self-hosted

This repo uses itself. See `.copier-answers.copier-template.yml` for the answers used.

### Pre-commit composition

This template does not generate a `.pre-commit-config.yaml`. Pre-commit configuration is expected to be handled by a separate template that composes with this one.
