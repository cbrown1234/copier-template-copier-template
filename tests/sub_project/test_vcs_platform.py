"""Tests for vcs_platform feature."""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.mark.parametrize(
    ('sub_project', 'expect_gitlab', 'expect_github'),
    [
        ({'vcs_platform': 'gitlab'}, True, False),
        ({'vcs_platform': 'github'}, False, True),
    ],
    indirect=['sub_project'],
)
def test_vcs_platform_files(
    sub_project: Path, expect_gitlab: bool, expect_github: bool
) -> None:
    """Test that VCS platform files are included based on vcs_platform."""
    assert (sub_project / '.gitlab-ci.yml').exists() == expect_gitlab
    assert (sub_project / '.gitlab').is_dir() == expect_gitlab
    assert (
        sub_project / '.github' / 'workflows' / 'test.yml'
    ).exists() == expect_github
    assert (sub_project / '.github').is_dir() == expect_github
