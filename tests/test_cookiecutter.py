from pathlib import Path
import subprocess as subp

import pytest

template_root = Path(__file__).parents[1].as_posix()


@pytest.fixture(scope="module")
def bake_result(cookies_session):
    """Reusable project fixture."""
    # Set the module scope because creating a new project takes a while.
    return cookies_session.bake(
        extra_context={"project_name": "Test Project"}, template=template_root
    )


def test_bake_creates_project(bake_result):
    assert bake_result.exit_code == 0
    assert bake_result.exception is None
    assert bake_result.project_path.name == "test-project"
    assert bake_result.project_path.is_dir()
    assert (bake_result.project_path / "test_project").is_dir()


def test_bake_initializes_git(bake_result):
    assert (bake_result.project_path / ".git").is_dir()


def test_bake_install_pre_commit_hooks(bake_result):
    assert (bake_result.project_path / ".git/hooks/pre-commit").is_file()


def test_bake_commits_all_changes(bake_result):
    ret = subp.run(["git", "diff", "--quiet"], cwd=bake_result.project_path)
    assert ret.returncode == 0
