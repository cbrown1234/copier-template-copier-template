"""Tests for the copier template."""

from __future__ import annotations

import subprocess
from pathlib import Path

from copier import run_copy
import pytest

from helpers import git_save

TEMPLATE_DIR = Path(__file__).parent.parent.absolute()
ANSWER_FILE_DEFAULT = '.copier-answers.copier-template.yml'


@pytest.fixture
def sub_project(tmp_path_factory: pytest.TempPathFactory) -> Path:
    sub_project = tmp_path_factory.mktemp('sub_project')
    run_copy(
        str(TEMPLATE_DIR),
        sub_project,
        vcs_ref='HEAD',
        defaults=True,
        unsafe=True,
    )
    git_save(sub_project)
    return sub_project


def test_sub_project_copy_default(
    sub_project: Path, tmp_path_factory: pytest.TempPathFactory
) -> None:
    assert (sub_project / ANSWER_FILE_DEFAULT).exists()
    sub_sub_project = tmp_path_factory.mktemp('sub_sub')
    run_copy(
        str(sub_project),
        sub_sub_project,
        vcs_ref='HEAD',
        defaults=True,
        unsafe=True,
    )
    assert (sub_sub_project / '.copier-answers.your-template-name.yml').exists()


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
