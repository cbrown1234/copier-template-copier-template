"""Tests for the copier template."""

from __future__ import annotations

from pathlib import Path

from copier import run_copy
import pytest

from tests.helpers import git_save


@pytest.fixture
def sub_sub_project(
    sub_project: Path, tmp_path_factory: pytest.TempPathFactory
) -> Path:
    sub_sub_project = tmp_path_factory.mktemp('sub_sub')
    run_copy(
        str(sub_project),
        sub_sub_project,
        vcs_ref='HEAD',
        defaults=True,
        unsafe=True,
    )
    git_save(sub_sub_project)
    return sub_sub_project


def test_sub_project_copy_default(sub_sub_project: Path) -> None:
    assert (sub_sub_project / '.copier-answers.your-template-name.yml').exists()
