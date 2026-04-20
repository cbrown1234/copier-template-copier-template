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

The release job uses `CI_JOB_TOKEN` by default. Under **Settings → CI/CD → Job token permissions**:

- Enable [**Allow Git push requests to the repository**](https://docs.gitlab.com/ci/jobs/ci_job_token/) so semantic-release can push the version-bump commit and tag.
- Add this project to its own **Authorized groups and projects** allowlist and grant the following [fine-grained permissions](https://docs.gitlab.com/ci/jobs/fine_grained_permissions/):
    - `ADMIN_RELEASES` — create the GitLab release via the Releases API.
    - `READ_REPOSITORIES` — read repository metadata.

To override with a dedicated token, add a `GITLAB_TOKEN` CI/CD variable (masked, protected) with a [project access token](https://docs.gitlab.com/user/project/settings/project_access_tokens/) that has Maintainer role and `write_repository` + `api` scopes. When set, it takes precedence over `CI_JOB_TOKEN`.

## Making changes

Template files live under `meta_template/`. After making changes, run `task test` to verify everything works.

To pull in upstream improvements from the meta-template:

```bash
copier update --answers-file .copier-answers.copier-template.yml
```
