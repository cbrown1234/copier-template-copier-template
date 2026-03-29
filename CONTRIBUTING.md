# Contributing to copier-template-copier-template

## Dev setup

Prerequisites: [uv](https://docs.astral.sh/uv/) and [Task](https://taskfile.dev/).

```bash
task dev-setup
```

Run `task --list` to see all available commands.

### Optional dependencies

- [asciinema](https://docs.asciinema.org/manual/cli/quick-start/) for demo video with copiable text

## Running tests

There are two test suites:

- **`tests/`** — tests the template itself: verifies that `copier copy` and `copier update` produce the expected output.
- **`tests/sub_project/`** — tests a project generated *from* your template: verifies that the generated template works end-to-end.

Run both with:

```bash
task test
```

## Making changes

Template files live under `meta_template/`. After making changes, run `task test` to verify everything works.

To pull in upstream improvements from the meta-template:

```bash
copier update --answers-file .copier-answers.copier-template.yml
```
