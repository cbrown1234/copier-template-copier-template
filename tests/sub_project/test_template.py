"""Tests for the copier template."""

from __future__ import annotations

from pathlib import Path

import pytest
from copier import run_copy

from tests.helpers import git_save


@pytest.fixture
def sub_sub_project(
    sub_project: Path,
    tmp_path_factory: pytest.TempPathFactory,
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


class TestRecommendedExtensions:
    def test_default_no_extensions(self, sub_project: Path) -> None:
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
    def test_pydantic_validation_enabled(self, sub_project: Path) -> None:
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
    def test_template_extensions_enabled(self, sub_project: Path) -> None:
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
    def test_both_extensions_enabled(self, sub_project: Path) -> None:
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
