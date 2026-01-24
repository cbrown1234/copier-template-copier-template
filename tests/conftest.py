"""Tests for the copier template."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml


@pytest.fixture
def template_dir(request) -> Path:
    return request.config.rootpath


@pytest.fixture
def copier_config(template_dir: Path) -> dict:
    with open(template_dir / 'copier.yml') as copier_config:
        return yaml.safe_load(copier_config)
