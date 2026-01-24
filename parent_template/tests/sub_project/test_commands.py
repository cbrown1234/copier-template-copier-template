"""Tests for a generated sub-project."""

from __future__ import annotations

import subprocess
from pathlib import Path


def test_sub_project_has_content(sub_project: Path) -> None:
    """Verify the generated project has files with content."""
    subprocess.run(
        'find . -type f | grep .',
        cwd=sub_project,
        shell=True,
        check=True,
    )
