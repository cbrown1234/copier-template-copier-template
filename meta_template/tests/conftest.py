"""Tests for the copier template."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml


@pytest.fixture
def template_dir(request: pytest.FixtureRequest) -> Path:
    return request.config.rootpath


@pytest.fixture
def copier_config(template_dir: Path) -> dict:
    copier_config_file = template_dir / 'copier.yml'
    with copier_config_file.open() as f:
        return yaml.safe_load(f)
