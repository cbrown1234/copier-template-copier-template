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

## Releases

Releases are automated via [python-semantic-release](https://python-semantic-release.readthedocs.io/). Preview what the next release would look like with:

```bash
task release
```

### CI setup

The release workflow uses the built-in `GITHUB_TOKEN`. If your default branch restricts pushes via [branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-a-branch-protection-rule/about-branch-protection-rules), use a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) stored as a repository secret named `GH_TOKEN` instead.

## Making changes

Template files live under `meta_template/`. After making changes, run `task test` to verify everything works.

To pull in upstream improvements from the meta-template:

```bash
copier update --answers-file .copier-answers.copier-template.yml
```
