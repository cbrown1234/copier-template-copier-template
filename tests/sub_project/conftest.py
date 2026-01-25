"""Tests for the copier template."""

from __future__ import annotations

from pathlib import Path

from copier import run_copy
import pytest

from tests.helpers import git_save


@pytest.fixture
def sub_project(
    request, template_dir: Path, tmp_path_factory: pytest.TempPathFactory
) -> Path:
    """Create a sub-project by copying the template.

    Can be used directly for default values, or with indirect parametrization
    to pass custom copier data:

        @pytest.mark.parametrize(
            'sub_project,expected',
            [
                ({'some_option': 'value1'}, 'expected1'),
                ({'some_option': 'value2'}, 'expected2'),
            ],
            indirect=['sub_project'],
        )
        def test_example(sub_project: Path, expected: str) -> None:
            ...
    """
    data = getattr(request, 'param', None)
    project = tmp_path_factory.mktemp('sub_project')
    run_copy(
        str(template_dir),
        project,
        vcs_ref='HEAD',
        data=data,
        defaults=True,
        unsafe=True,
    )
    git_save(project)
    return project
