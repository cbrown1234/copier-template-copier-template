"""Tests for the copier template using plumbum."""

from __future__ import annotations

from pathlib import Path

from plumbum import local
from plumbum.cmd import pre_commit, task

from tests.helpers import git_save


def test_dev_setup(sub_project: Path) -> None:
    with local.cwd(sub_project):
        (pre_commit['sample-config'] > '.pre-commit-config.yaml')()
        git_save(sub_project)
        task('dev-setup')


def test_docker_mounts(sub_project: Path) -> None:
    with local.cwd(sub_project):
        task('example:docker-mount')


def test_sub_project_tests(sub_project: Path) -> None:
    with local.cwd(sub_project):
        task('dev-setup:venv')
        task('test')
