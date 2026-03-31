# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

A Copier **meta-template**: a template that generates other Copier templates. Running `copier copy` against this repo scaffolds a new, fully-configured Copier template project. The repo is self-hosted — it was generated from its own earlier version (see `.copier-answers.copier-template.yml`).

## Commands

All task automation uses [go-task](https://taskfile.dev/):

```sh
task dev-setup        # Install pre-commit hooks and uv dependencies
task test             # Run the full test suite
task cog              # Regenerate cogapp-managed files (e.g. .gitignore)
task release          # Dry-run semantic release
task release:actual   # Perform actual release
```

Run a single test file or test case with pytest directly:

```sh
uv run pytest tests/test_copy.py -k test_name_here
```

Linting and formatting run automatically via pre-commit. To run manually:

```sh
uv run pre-commit run --all-files
```

## Architecture

### Directory layout

```
copier.yml              # Template questions and configuration for this meta-template
meta_template/          # The actual template source — becomes the generated project
  copier.yml.tmpl
  pyproject.toml.tmpl
  Taskfile.yaml.tmpl
  tests/                # Test suite shipped inside every generated template
  ...
tests/                  # Tests for the meta-template itself (not the generated output)
taskfile/               # Modular Taskfile includes
```

### Dual test suites

- `tests/` — validates that this meta-template works: runs `copier copy` and `copier update` and checks the results.
- `meta_template/tests/` — tests that are **shipped inside every generated template** to verify that the generated template itself works. These run within the context of a generated project, not this repo.

### Template delimiters

Copier's default Jinja delimiters conflict with most template file content, so this project uses custom delimiters defined in `copier.yml`:

| Role | Delimiter |
|---|---|
| Variable | `<< variable >>` |
| Block | `<% if ... %>` / `<% endif %>` |
| Comment | `<# ... #>` |

Generated projects can optionally use square-bracket delimiters (`[[ variable ]]`) instead, controlled by the `template_style` question.

Template source files use the `.tmpl` extension.

### Template questions (`copier.yml`)

The meta-template asks seven key questions when generating a new template project:

1. `vcs_platform` — GitLab or GitHub (controls which CI config is generated)
2. `output_template_name` — name for the generated template
3. `template_style` — Jinja (`<< >>`) or Square Brackets (`[[ ]]`) delimiters
4. `include_pydantic_validation` — add `copier-pydantic` for answer validation
5. `include_template_extensions` — add `copier-template-extensions` for local Jinja extensions
6. `license_type` — MIT, Apache 2.0, Unlicense, or None
7. `copyright_name` / `copyright_year` — license holder details

### Toolchain

| Tool | Purpose |
|---|---|
| **uv** | Python package management and venv |
| **pytest + plumbum** | Testing (shell commands as Python calls) |
| **Ruff** | Linting and formatting (`ruff.toml`) |
| **python-semantic-release** | Automated versioning and changelog |
| **cogapp** | Code generation for dynamic file sections (`.gitignore`) |
| **Renovate** | Automated dependency updates |
| **pre-commit** | Hook runner for all linting/validation |
