import subprocess as subp


DATABASE = "{{ cookiecutter.database }}"


def run():
    """Main entrypoint."""
    if DATABASE == "sqlite":
        # We don't need docker-compose.yml for sqlite
        run_command("rm", "-f", "docker-compose.yml")

    run_command("git", "init")
    run_command("git", "add", ".")
    run_command("pre-commit", "install")
    run_command("pre-commit", "autoupdate")
    run_command("git", "add", ".")  # make sure we stage .pre-commit configuration
    run_command("pre-commit", "run", "--all-files")
    run_command("git", "add", ".")  # absorb changes made by pre-commit
    run_command(
        "git",
        "commit",
        "-m",
        "Generate project from imankulov/cookiecutter-python-project",
    )


def run_command(*args):
    """Helper function to run a command."""
    print(f"Running: {' '.join(args)}")
    return subp.run(args)


run()
