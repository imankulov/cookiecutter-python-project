import subprocess as subp


def run():
    """Main entrypoint."""
    run_command("git", "init")
    run_command("git", "add", ".")
    run_command("pre-commit", "install")
    run_command("pre-commit", "autoupdate")
    run_command("git", "add", ".")  # make sure we stage .pre-commit configuration
    run_command("pre-commit", "run", "--all-files")
    run_command(
        "git", "commit", "-m", "Generate project from cookiecutter-python-project"
    )


def run_command(*args):
    """Helper function to run a command."""
    print(f"Running: {' '.join(args)}")
    return subp.run(args)


run()
