"""Tests for the copier template."""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture
def template_dir(request: pytest.FixtureRequest) -> Path:
    return request.config.rootpath
