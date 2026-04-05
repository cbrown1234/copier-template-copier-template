"""Tests for the copier template."""

from __future__ import annotations

from pathlib import Path

try:
    import tomllib  # stdlib in Python 3.11+
except ImportError:
    import tomli as tomllib  # type: ignore[no-redef]  # backport for Python 3.10

import pytest
import yaml


def test_default_no_extensions(sub_project: Path) -> None:
    assert not (sub_project / 'models.py').exists()
    assert not (sub_project / 'extensions').exists()

    readme = (sub_project / 'README.md').read_text()
    assert '--trust' not in readme

    with (sub_project / 'copier.yml').open() as f:
        copier_config = yaml.safe_load(f)
    assert '_jinja_extensions' not in copier_config

    with (sub_project / 'pyproject.toml').open('rb') as f:
        pyproject = tomllib.load(f)
    deps = pyproject['project']['dependencies']
    assert not any('copier-pydantic' in d for d in deps)
    assert not any('copier-template-extensions' in d for d in deps)


@pytest.mark.parametrize(
    'sub_project',
    [{'include_pydantic_validation': True}],
    indirect=True,
)
def test_pydantic_validation_enabled(sub_project: Path) -> None:
    assert (sub_project / 'models.py').exists()

    readme = (sub_project / 'README.md').read_text()
    assert '--trust' in readme

    with (sub_project / 'copier.yml').open() as f:
        copier_config = yaml.safe_load(f)
    assert 'copier_pydantic.MultilineValidation' in copier_config['_jinja_extensions']
    assert 'copier_pydantic.PydanticExtension' in copier_config['_jinja_extensions']

    with (sub_project / 'pyproject.toml').open('rb') as f:
        pyproject = tomllib.load(f)
    deps = pyproject['project']['dependencies']
    assert any('copier-pydantic' in d for d in deps)
    assert not any('copier-template-extensions' in d for d in deps)


@pytest.mark.parametrize(
    'sub_project',
    [{'include_template_extensions': True}],
    indirect=True,
)
def test_template_extensions_enabled(sub_project: Path) -> None:
    assert (sub_project / 'extensions').is_dir()

    readme = (sub_project / 'README.md').read_text()
    assert '--trust' in readme

    with (sub_project / 'copier.yml').open() as f:
        copier_config = yaml.safe_load(f)
    assert (
        'copier_template_extensions.TemplateExtensionLoader'
        in copier_config['_jinja_extensions']
    )

    with (sub_project / 'pyproject.toml').open('rb') as f:
        pyproject = tomllib.load(f)
    deps = pyproject['project']['dependencies']
    assert not any('copier-pydantic' in d for d in deps)
    assert any('copier-template-extensions' in d for d in deps)


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

    with (sub_project / 'copier.yml').open() as f:
        copier_config = yaml.safe_load(f)
    assert 'copier_pydantic.MultilineValidation' in copier_config['_jinja_extensions']
    assert 'copier_pydantic.PydanticExtension' in copier_config['_jinja_extensions']
    assert (
        'copier_template_extensions.TemplateExtensionLoader'
        in copier_config['_jinja_extensions']
    )

    with (sub_project / 'pyproject.toml').open('rb') as f:
        pyproject = tomllib.load(f)
    deps = pyproject['project']['dependencies']
    assert any('copier-pydantic' in d for d in deps)
    assert any('copier-template-extensions' in d for d in deps)
