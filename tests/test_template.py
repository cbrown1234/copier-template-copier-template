"""Tests for the copier template."""

from __future__ import annotations

from pathlib import Path

from copier import run_copy, run_update
from plumbum import local
from plumbum.cmd import task

from helpers import git, git_save

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


def test_dev_setup(tmp_path: Path) -> None:
    run_copy(
        str(TEMPLATE_DIR),
        tmp_path,
        vcs_ref='HEAD',
        defaults=True,
        unsafe=True,
    )
    with local.cwd(tmp_path):
        git('init')
        task('dev-setup')
    git_save(tmp_path)
