"""Tests for vcs_platform feature."""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.mark.parametrize(
    'sub_project,expect_gitlab',
    [
        ({'vcs_platform': 'gitlab'}, True),
    ],
    indirect=['sub_project'],
)
def test_vcs_platform_gitlab_files(sub_project: Path, expect_gitlab: bool) -> None:
    """Test that GitLab files are included based on vcs_platform."""
    assert (sub_project / '.gitlab-ci.yml').exists() == expect_gitlab
    assert (sub_project / '.gitlab').is_dir() == expect_gitlab
