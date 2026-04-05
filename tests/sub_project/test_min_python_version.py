"""Tests for min_python_version feature."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

import pytest

GITHUB_CI = '.github/workflows/test.yml'
GITLAB_CI = '.gitlab/ci/copier-template/.gitlab-ci.yml'


@pytest.mark.parametrize(
    ('sub_project', 'expected'),
    [
        (
            {},
            {
                'version': '3.10',
                'ruff_target': 'py310',
            },
        ),
        (
            {'min_python_version': '3.12'},
            {
                'version': '3.12',
                'ruff_target': 'py312',
            },
        ),
        (
            {'min_python_version': '3.14'},
            {
                'version': '3.14',
                'ruff_target': 'py314',
            },
        ),
    ],
    indirect=['sub_project'],
)
def test_min_python_version(sub_project: Path, expected: dict) -> None:
    pyproject = (sub_project / 'pyproject.toml').read_text()
    assert f'requires-python = ">= {expected["version"]}"' in pyproject

    ruff_toml = (sub_project / 'ruff.toml').read_text()
    assert f'target-version = "{expected["ruff_target"]}"' in ruff_toml


@pytest.mark.parametrize(
    ('vcs_platform', 'ci_file', 'ci_key'),
    [
        ('github', GITHUB_CI, 'python-version'),
        ('gitlab', GITLAB_CI, 'PYTHON_VERSION'),
    ],
)
@pytest.mark.parametrize(
    ('min_python_version', 'ci_matrix'),
    [
        ('3.10', '["3.10", "3.11", "3.12", "3.13", "3.14"]'),
        ('3.12', '["3.12", "3.13", "3.14"]'),
        ('3.14', '["3.14"]'),
    ],
)
def test_ci_matrix(
    make_sub_project: Callable,
    vcs_platform: str,
    ci_file: str,
    ci_key: str,
    min_python_version: str,
    ci_matrix: str,
) -> None:
    sp = make_sub_project(
        {'vcs_platform': vcs_platform, 'min_python_version': min_python_version}
    )
    assert f'{ci_key}: {ci_matrix}' in (sp / Path(ci_file)).read_text()
