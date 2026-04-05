"""Tests for min_python_version feature."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

try:
    import tomllib  # stdlib in Python 3.11+
except ImportError:
    import tomli as tomllib  # type: ignore[no-redef]  # backport for Python 3.10

import pytest
import yaml


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
    with (sub_project / 'pyproject.toml').open('rb') as f:
        pyproject = tomllib.load(f)
    assert pyproject['project']['requires-python'] == f'>= {expected["version"]}'

    with (sub_project / 'ruff.toml').open('rb') as f:
        ruff_toml = tomllib.load(f)
    assert ruff_toml['target-version'] == expected['ruff_target']


@pytest.mark.parametrize(
    ('vcs_platform', 'ci_file', 'get_versions'),
    [
        (
            'github',
            '.github/workflows/test.yml',
            lambda c: c['jobs']['tests']['strategy']['matrix']['python-version'],
        ),
        (
            'gitlab',
            '.gitlab/ci/copier-template/.gitlab-ci.yml',
            lambda c: c['tests']['parallel']['matrix'][0]['PYTHON_VERSION'],
        ),
    ],
)
@pytest.mark.parametrize(
    ('min_python_version', 'expected_versions'),
    [
        ('3.10', ['3.10', '3.11', '3.12', '3.13', '3.14']),
        ('3.12', ['3.12', '3.13', '3.14']),
        ('3.14', ['3.14']),
    ],
)
def test_ci_matrix(
    sub_project_factory: Callable,
    vcs_platform: str,
    ci_file: str,
    get_versions: Callable,
    min_python_version: str,
    expected_versions: list[str],
) -> None:
    sub_project = sub_project_factory(
        {'vcs_platform': vcs_platform, 'min_python_version': min_python_version}
    )
    with (sub_project / ci_file).open() as f:
        ci_config = yaml.safe_load(f)

    assert get_versions(ci_config) == expected_versions
