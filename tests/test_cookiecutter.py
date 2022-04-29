from pathlib import Path

template_root = Path(__file__).parents[1].as_posix()


def test_bake_project(cookies):
    result = cookies.bake(
        extra_context={"project_name": "Test Project"}, template=template_root
    )
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "test-project"
    assert result.project_path.is_dir()
    assert (result.project_path / "test_project").is_dir()
