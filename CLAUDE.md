# CLAUDE.md

## What This Project Is

A Copier **meta-template**: a template (`meta_template/`) that generates other Copier templates. Running `copier copy` against this repo scaffolds a new, fully-configured Copier template project. The repo is self-hosted — changes to generic content (README, CI config, etc.) should go in `meta_template/` so downstream users receive them on `copier update`.

## Commands

Examples

```sh
task dev-setup   # Install pre-commit hooks and uv dependencies
task test        # Run the full test suite
task cog         # Regenerate cogapp-managed files (e.g. .gitignore)
task --list      # See all project commmands
```

Pass additional args to pytest via `--`:

```sh
task test -- -k test_name_here
task test -- tests/test_copy.py -v
```

## Architecture

### Dual test suites

- `tests/` — validates that this meta-template works (runs `copier copy`/`copier update`)
- `meta_template/tests/` — shipped inside every generated template; runs within a generated project, not this repo

### Template delimiters

Custom delimiters (defined in `copier.yml`) replace Copier's defaults to avoid conflicts with template file content:

| Role | Delimiter |
|---|---|
| Variable | `<< variable >>` |
| Block | `<% if ... %>` / `<% endif %>` |
| Comment | `<# ... #>` |

The `template_style` question lets generated projects use `[[ ]]` instead. Template source files use the `.tmpl` extension.
