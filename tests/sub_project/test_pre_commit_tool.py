"""Tests for pre_commit_tool feature."""

from __future__ import annotations

import tomllib
from collections.abc import Callable
from pathlib import Path

import pytest
import yaml


@pytest.mark.parametrize(
    ('sub_project', 'expected_dep', 'unexpected_dep'),
    [
        ({'pre_commit_tool': 'prek'}, 'prek', 'pre-commit'),
        ({'pre_commit_tool': 'pre-commit'}, 'pre-commit', 'prek'),
    ],
    indirect=['sub_project'],
)
def test_pre_commit_tool_dependency(
    sub_project: Path, expected_dep: str, unexpected_dep: str
) -> None:
    with (sub_project / 'pyproject.toml').open('rb') as f:
        pyproject = tomllib.load(f)
    dev_deps = [dep.split('>=')[0] for dep in pyproject['dependency-groups']['dev']]
    assert expected_dep in dev_deps
    assert unexpected_dep not in dev_deps


@pytest.mark.parametrize(
    ('sub_project', 'expected_cmds'),
    [
        (
            {'pre_commit_tool': 'prek'},
            {
                'dev-setup': ['uv run prek install', 'uv run prek autoupdate'],
                'lint': ['uv run prek run --all-files'],
            },
        ),
        (
            {'pre_commit_tool': 'pre-commit'},
            {
                'dev-setup': [
                    'uv run pre-commit install',
                    'uv run pre-commit autoupdate',
                ],
                'lint': ['uv run pre-commit run --all-files'],
            },
        ),
    ],
    indirect=['sub_project'],
)
def test_pre_commit_tool_tasks(
    sub_project: Path, expected_cmds: dict[str, list[str]]
) -> None:
    for taskfile, cmds in expected_cmds.items():
        with (
            sub_project / 'taskfile' / 'copier-template' / taskfile / 'Taskfile.yaml'
        ).open() as f:
            tasks = yaml.safe_load(f)['tasks']
        all_cmds = [cmd for t in tasks.values() for cmd in t.get('cmds', [])]
        for cmd in cmds:
            assert cmd in all_cmds


@pytest.mark.parametrize(
    ('vcs_platform', 'ci_file', 'get_env'),
    [
        ('github', '.github/workflows/test.yml', lambda c: c['env']),
        (
            'gitlab',
            '.gitlab/ci/copier-template/.gitlab-ci.yml',
            lambda c: c['tests']['variables'],
        ),
    ],
)
@pytest.mark.parametrize(
    ('pre_commit_tool', 'home_var', 'unexpected_var'),
    [
        ('prek', 'PREK_HOME', 'PRE_COMMIT_HOME'),
        ('pre-commit', 'PRE_COMMIT_HOME', 'PREK_HOME'),
    ],
)
def test_pre_commit_tool_ci_cache(
    sub_project_factory: Callable,
    vcs_platform: str,
    ci_file: str,
    get_env: Callable,
    pre_commit_tool: str,
    home_var: str,
    unexpected_var: str,
) -> None:
    sub_project = sub_project_factory(
        {'vcs_platform': vcs_platform, 'pre_commit_tool': pre_commit_tool}
    )
    with (sub_project / ci_file).open() as f:
        env = get_env(yaml.safe_load(f))

    assert env[home_var].endswith(f'.cache/{pre_commit_tool}')
    assert unexpected_var not in env


@pytest.mark.parametrize(
    ('sub_project', 'expected'),
    [
        ({'pre_commit_tool': 'pre-commit'}, True),
        ({'pre_commit_tool': 'prek'}, False),
        ({}, False),
    ],
    indirect=['sub_project'],
)
def test_pre_commit_tool_answer_recorded_only_on_opt_in(
    sub_project: Path, expected: bool
) -> None:
    """Beta flag: unrecorded unless opted in, so a later rollout asks fresh."""
    answers = yaml.safe_load(
        (sub_project / '.copier-answers.copier-template.yml').read_text()
    )
    assert ('pre_commit_tool' in answers) == expected
