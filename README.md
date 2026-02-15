# copier-template-copier-template

A [Copier](https://copier.readthedocs.io/) meta-template — a template that scaffolds new Copier templates with modern Python project tooling preconfigured.

## Features

- **Test harness included** pytest setup with examples and helpers, ready to test your template, and it's usage
- **Modern Batteries included** semantic release, Renovate, Ruff, and [go-task](https://taskfile.dev/) automation all preconfigured
- **CI/CD out of the box** Supports GitLab CI or GitHub Actions, with matrix testing across Python versions
- **Optional Copier extensions**
    - [Pydantic validation](https://pypi.org/project/copier-pydantic/)
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
copier copy <template-url> /path/to/new/project
```

### Update an existing project

```bash
cd /path/to/your/project
copier update
```

## Development

### Prerequisites

- [uv](https://docs.astral.sh/uv/)
- [Task](https://taskfile.dev/)

[Task](https://taskfile.dev/) is the project task runner. Run `task --list` to see available commands, including dev setup, testing, and releases.

### Self-hosted

This repo uses itself. See `.copier-answers.copier-template.yml` for the answers used.
