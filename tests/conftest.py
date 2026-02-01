"""Tests for the copier template."""

from __future__ import annotations

from pathlib import Path
from typing import Any

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


@pytest.fixture(scope='session')
def mock_answers_required_without_defaults() -> dict[str, Any]:
    """Answers to question required with no default.

    For answers that you want to force a user to supply, as
    you cannot provide a sensible default ahead of time
    e.g. Name, but that do not matter for the tests
    """
    mock_file = Path(__file__).parent / 'mock_answers_required_without_defaults.yaml'
    with mock_file.open() as f:
        return yaml.safe_load(f)
