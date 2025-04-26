"""Tests for the copier template."""

from __future__ import annotations

from pathlib import Path

from copier import run_copy
import pytest
from pytest_virtualenv import VirtualEnv

from helpers import git_save

TEMPLATE_DIR = Path(__file__).parent.parent.absolute()
ANSWER_FILE_DEFAULT = '.copier-answers.copier-template.yml'


def test_sub_project_copy_default(
    tmp_path: Path, tmp_path_factory: pytest.TempPathFactory
) -> None:
    sub_project_dir = tmp_path
    run_copy(
        str(TEMPLATE_DIR),
        sub_project_dir,
        vcs_ref='HEAD',
        defaults=True,
        unsafe=True,
    )
    assert (sub_project_dir / ANSWER_FILE_DEFAULT).exists()
    sub_sub_project_dir = tmp_path_factory.mktemp('sub_sub')
    run_copy(
        str(sub_project_dir),
        sub_sub_project_dir,
        vcs_ref='HEAD',
        defaults=True,
        unsafe=True,
    )
    assert (sub_sub_project_dir / '.copier-answers.your-template-name.yml').exists()


def test_sub_project_tests(tmp_path: Path, virtualenv: VirtualEnv) -> None:
    sub_project_dir = tmp_path
    run_copy(
        str(TEMPLATE_DIR),
        sub_project_dir,
        vcs_ref='HEAD',
        defaults=True,
        unsafe=True,
    )
    git_save(sub_project_dir)
    virtualenv.run(
        'task dev-setup:virtualenv && task test',
        cd=sub_project_dir,
    )
