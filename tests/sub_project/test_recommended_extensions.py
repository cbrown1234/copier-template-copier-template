"""Tests for the copier template."""

from __future__ import annotations

from pathlib import Path

import pytest


def test_default_no_extensions(sub_project: Path) -> None:
    assert not (sub_project / 'models.py').exists()
    assert not (sub_project / 'extensions').exists()

    readme = (sub_project / 'README.md').read_text()
    assert '--trust' not in readme

    copier_yml = (sub_project / 'copier.yml').read_text()
    assert '_jinja_extensions' not in copier_yml

    pyproject = (sub_project / 'pyproject.toml').read_text()
    assert 'copier-pydantic' not in pyproject
    assert 'copier-template-extensions' not in pyproject


@pytest.mark.parametrize(
    'sub_project',
    [{'include_pydantic_validation': True}],
    indirect=True,
)
def test_pydantic_validation_enabled(sub_project: Path) -> None:
    assert (sub_project / 'models.py').exists()

    readme = (sub_project / 'README.md').read_text()
    assert '--trust' in readme

    copier_yml = (sub_project / 'copier.yml').read_text()
    assert 'copier_pydantic.MultilineValidation' in copier_yml
    assert 'copier_pydantic.PydanticExtension' in copier_yml

    pyproject = (sub_project / 'pyproject.toml').read_text()
    assert 'copier-pydantic' in pyproject
    assert 'copier-template-extensions' not in pyproject


@pytest.mark.parametrize(
    'sub_project',
    [{'include_template_extensions': True}],
    indirect=True,
)
def test_template_extensions_enabled(sub_project: Path) -> None:
    assert (sub_project / 'extensions').is_dir()

    readme = (sub_project / 'README.md').read_text()
    assert '--trust' in readme

    copier_yml = (sub_project / 'copier.yml').read_text()
    assert 'copier_template_extensions.TemplateExtensionLoader' in copier_yml

    pyproject = (sub_project / 'pyproject.toml').read_text()
    assert 'copier-pydantic' not in pyproject
    assert 'copier-template-extensions' in pyproject


@pytest.mark.parametrize(
    'sub_project',
    [{'include_pydantic_validation': True, 'include_template_extensions': True}],
    indirect=True,
)
def test_both_extensions_enabled(sub_project: Path) -> None:
    assert (sub_project / 'models.py').exists()
    assert (sub_project / 'extensions').is_dir()

    readme = (sub_project / 'README.md').read_text()
    assert '--trust' in readme

    copier_yml = (sub_project / 'copier.yml').read_text()
    assert 'copier_pydantic.MultilineValidation' in copier_yml
    assert 'copier_pydantic.PydanticExtension' in copier_yml
    assert 'copier_template_extensions.TemplateExtensionLoader' in copier_yml

    pyproject = (sub_project / 'pyproject.toml').read_text()
    assert 'copier-pydantic' in pyproject
    assert 'copier-template-extensions' in pyproject
