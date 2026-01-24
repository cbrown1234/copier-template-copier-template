"""Tests for the copier template."""

from __future__ import annotations

from pathlib import Path

from copier import run_copy
import pytest

from tests.helpers import git_save


# TODO: parameterise with copier variables?
@pytest.fixture
def sub_project(template_dir: Path, tmp_path_factory: pytest.TempPathFactory) -> Path:
    sub_project = tmp_path_factory.mktemp('sub_project')
    run_copy(
        str(template_dir),
        sub_project,
        vcs_ref='HEAD',
        defaults=True,
        unsafe=True,
    )
    git_save(sub_project)
    return sub_project
