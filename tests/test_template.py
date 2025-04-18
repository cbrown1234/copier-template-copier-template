"""Tests for the copier template."""

from __future__ import annotations

from pathlib import Path

from copier import run_copy, run_update
import pytest
from pytest_virtualenv import VirtualEnv

from helpers import git_save, is_git_repo_dirty

TEMPLATE_DIR = Path(__file__).parent.parent.absolute()
ANSWER_FILE_DEFAULT = '.copier-answers.copier-template.yml'


def test_copy_default(tmp_path: Path) -> None:
    run_copy(
        str(TEMPLATE_DIR),
        tmp_path,
        vcs_ref='HEAD',
        defaults=True,
        unsafe=True,
    )
    assert (tmp_path / ANSWER_FILE_DEFAULT).exists()


@pytest.mark.skipif(is_git_repo_dirty(), reason='Fail on dirty repo')
def test_update_default(tmp_path: Path) -> None:
    run_copy(
        str(TEMPLATE_DIR),
        tmp_path,
        defaults=True,
        unsafe=True,
    )
    git_save(tmp_path)
    run_update(
        tmp_path,
        vcs_ref='HEAD',
        defaults=True,
        overwrite=True,  # The default when run via CLI
        answers_file=ANSWER_FILE_DEFAULT,
        unsafe=True,
    )
    assert (tmp_path / ANSWER_FILE_DEFAULT).exists()


def test_dev_setup(tmp_path: Path, virtualenv: VirtualEnv) -> None:
    run_copy(
        str(TEMPLATE_DIR),
        tmp_path,
        vcs_ref='HEAD',
        defaults=True,
        unsafe=True,
    )
    git_save(tmp_path)
    virtualenv.run('pre-commit sample-config > .pre-commit-config.yaml', cd=tmp_path)
    git_save(tmp_path)
    virtualenv.run('task dev-setup', cd=tmp_path)


def test_docker_mounts(tmp_path: Path, virtualenv: VirtualEnv) -> None:
    run_copy(
        str(TEMPLATE_DIR),
        tmp_path,
        vcs_ref='HEAD',
        defaults=True,
        unsafe=True,
    )
    virtualenv.run('task example:docker-mount', cd=tmp_path)
