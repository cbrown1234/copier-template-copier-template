"""Tests for license file generation."""

from __future__ import annotations

from pathlib import Path

try:
    import tomllib  # stdlib in Python 3.11+
except ImportError:
    import tomli as tomllib  # type: ignore[no-redef]  # backport for Python 3.10

import pytest


def test_default_mit_license(sub_project: Path) -> None:
    license_file = sub_project / 'LICENSE'
    assert license_file.exists()

    license_text = license_file.read_text()
    assert 'MIT License' in license_text
    assert 'Mock Name' in license_text

    with (sub_project / 'pyproject.toml').open('rb') as f:
        pyproject = tomllib.load(f)
    assert pyproject['project']['license'] == 'MIT'
    assert pyproject['project']['license-files'] == ['LICENSE']


@pytest.mark.parametrize(
    'sub_project',
    [{'license_type': 'apache-2.0'}],
    indirect=True,
)
def test_apache_license(sub_project: Path) -> None:
    license_file = sub_project / 'LICENSE'
    assert license_file.exists()

    license_text = license_file.read_text()
    assert 'Apache License' in license_text
    assert 'Mock Name' in license_text

    with (sub_project / 'pyproject.toml').open('rb') as f:
        pyproject = tomllib.load(f)
    assert pyproject['project']['license'] == 'Apache-2.0'
    assert pyproject['project']['license-files'] == ['LICENSE']


@pytest.mark.parametrize(
    'sub_project',
    [{'license_type': 'unlicense'}],
    indirect=True,
)
def test_unlicense(sub_project: Path) -> None:
    license_file = sub_project / 'LICENSE'
    assert license_file.exists()

    license_text = license_file.read_text()
    assert 'public domain' in license_text
    # Unlicense doesn't have copyright holder name
    assert 'Mock Name' not in license_text

    with (sub_project / 'pyproject.toml').open('rb') as f:
        pyproject = tomllib.load(f)
    assert pyproject['project']['license'] == 'Unlicense'
    assert pyproject['project']['license-files'] == ['LICENSE']


@pytest.mark.parametrize(
    'sub_project',
    [{'license_type': 'none'}],
    indirect=True,
)
def test_no_license(sub_project: Path) -> None:
    license_file = sub_project / 'LICENSE'
    assert not license_file.exists()

    with (sub_project / 'pyproject.toml').open('rb') as f:
        pyproject = tomllib.load(f)
    assert 'license' not in pyproject['project']
    assert 'license-files' not in pyproject['project']
