"""Useful methods for testing copier templates."""

from copier.types import StrOrPath
from plumbum import local
from plumbum.cmd import git as _git
from plumbum.machines import LocalCommand
from pytest_gitconfig.plugin import DEFAULT_GIT_USER_EMAIL, DEFAULT_GIT_USER_NAME

git: LocalCommand = _git.with_env(
    GIT_AUTHOR_NAME=DEFAULT_GIT_USER_NAME,
    GIT_AUTHOR_EMAIL=DEFAULT_GIT_USER_EMAIL,
    GIT_COMMITTER_NAME=DEFAULT_GIT_USER_NAME,
    GIT_COMMITTER_EMAIL=DEFAULT_GIT_USER_EMAIL,
)


# Adapted from the copier repo tests
def git_save(
    dst: StrOrPath,
    message: str = 'Test commit',
    tag: str | None = None,
    allow_empty: bool = False,
) -> None:
    """Save the current repo state in git.

    Args:
        dst: Path to the repo to save.
        message: Commit message.
        tag: Tag to create, optionally.
        allow_empty: Allow creating a commit with no changes

    """
    with local.cwd(dst):
        git('init')
        git('add', '.')
        git('commit', '-m', message, *(['--allow-empty'] if allow_empty else []))
        if tag:
            git('tag', tag)
