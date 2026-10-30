"""Tests for the copier template using plumbum."""

from __future__ import annotations

from pathlib import Path

import pytest
from plumbum import local
from plumbum.cmd import task, uv

from tests.helpers import git_save


@pytest.mark.parametrize(
    ('sub_project', 'pre_commit_tool'),
    [
        ({'pre_commit_tool': 'prek'}, 'prek'),
        ({'pre_commit_tool': 'pre-commit'}, 'pre-commit'),
    ],
    indirect=['sub_project'],
)
def test_dev_setup(sub_project: Path, pre_commit_tool: str) -> None:
    with local.cwd(sub_project):
        (uv['run', pre_commit_tool, 'sample-config'] > '.pre-commit-config.yaml')()
        git_save(sub_project)
        task('dev-setup')


def test_docker_mounts(sub_project: Path) -> None:
    with local.cwd(sub_project):
        task('example:docker-mount')


def test_sub_project_tests(sub_project: Path) -> None:
    with local.cwd(sub_project):
        task('dev-setup:venv')
        task('test')


def test_sub_project_tests_dirty_repo(sub_project: Path) -> None:
    with local.cwd(sub_project):
        task('dev-setup:venv')
        (sub_project / 'dirty_file.txt').write_text('dirty')
        task('test')


def test_dev_setup_venv_ci(sub_project: Path) -> None:
    with local.cwd(sub_project):
        uv('lock')
        task('dev-setup:venv:ci')
