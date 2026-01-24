"""Tests for the copier template."""

from __future__ import annotations

import subprocess
from pathlib import Path


from tests.helpers import git_save


def test_dev_setup(sub_project: Path) -> None:
    subprocess.run(
        'pre-commit sample-config > .pre-commit-config.yaml',
        cwd=sub_project,
        shell=True,
        check=True,
    )
    git_save(sub_project)
    subprocess.run('task dev-setup', cwd=sub_project, shell=True, check=True)


def test_docker_mounts(sub_project: Path) -> None:
    subprocess.run('task example:docker-mount', cwd=sub_project, shell=True, check=True)


def test_sub_project_tests(sub_project: Path) -> None:
    subprocess.run(
        'task dev-setup:venv && task test',
        cwd=sub_project,
        shell=True,
        check=True,
    )
