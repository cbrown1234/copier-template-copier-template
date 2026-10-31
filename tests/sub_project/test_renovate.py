"""Tests for the generated Renovate setup."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

# The match string shared by Renovate's customManagers:githubActionsVersions and
# customManagers:gitlabPipelineVersions presets
RENOVATE_ANNOTATION_REGEX = (
    r'# renovate: datasource=(?P<datasource>[a-zA-Z0-9-._]+?) '
    r'depName=(?P<depName>[^\s]+?)'
    r'(?: (?:lookupName|packageName)=(?P<packageName>[^\s]+?))?'
    r'(?: versioning=(?P<versioning>[^\s]+?))?'
    r'(?: extractVersion=(?P<extractVersion>[^\s]+?))?'
    r'(?: registryUrl=(?P<registryUrl>[^\s]+?))?'
    r'\s+[A-Za-z0-9_]+?_VERSION\s*:\s*["\']?(?P<currentValue>.+?)["\']?\s'
)


@pytest.mark.parametrize(
    ('sub_project', 'preset', 'ci_glob'),
    [
        (
            {'vcs_platform': 'github'},
            'customManagers:githubActionsVersions',
            '.github/workflows/*.yml',
        ),
        (
            {'vcs_platform': 'gitlab'},
            'customManagers:gitlabPipelineVersions',
            '.gitlab/ci/**/.gitlab-ci.yml',
        ),
    ],
    indirect=['sub_project'],
)
def test_ci_tool_versions_renovate_managed(
    sub_project: Path, preset: str, ci_glob: str
) -> None:
    """CI tool versions are annotated for the platform's Renovate preset."""
    renovate = json.loads((sub_project / 'renovate.json').read_text())
    assert preset in renovate['extends']

    dep_names = {
        match['depName']
        for path in sub_project.glob(ci_glob)
        for match in re.finditer(RENOVATE_ANNOTATION_REGEX, path.read_text())
    }
    assert dep_names == {'astral-sh/uv', 'go-task/task'}


@pytest.mark.parametrize('sub_project', [{'vcs_platform': ''}], indirect=True)
def test_no_ci_preset_without_vcs_platform(sub_project: Path) -> None:
    renovate = json.loads((sub_project / 'renovate.json').read_text())
    assert renovate['extends'] == ['config:best-practices']
