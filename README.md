# Starter Template for Python projects

Use this cookiecutter template 🍪 to start every new Python project.

## Getting Started

Nothing can be easier:

```
git clone https://github.com/imankulov/cookiecutter-python-project.git
cookiecutter cookiecutter-python-project/
```

For Windows, you might need to run `python -m cookiecutter` as the command might not work even though it's correctly configured on the PATH.


## What's inside

The template covers your back with the following elements:

- README.md with a pre-defined structure.
- CHANGELOG.md file with an initial message.
- Stub project template.
- Test directory with a sample test file.
- GitHub workflow configuration to run pytest automatically.
- Pre-configured mypy, Flake8, isort.
- A set of pre-commit hooks.
- pyproject.toml for Poetry.

## Django flavour

There is a branch [django](https://github.com/imankulov/cookiecutter-python-project/tree/django) that contains an opinionated setup for starting up a new Django project. The setup includes:

- Dependencies: django, django-environ, psycopg2-binary, sentry-sdk
- Dev dependencies: pytest-django
- Sample environment file: env.example
- A boilerplate project template. The settings.py file reads environment from the .env file.

If you want to start a new Django project, switch to a Django branch before starting the cookiecutter.

```
git clone https://github.com/imankulov/cookiecutter-python-project.git
git checkout django
cookiecutter cookiecutter-python-project/
```

## How to use it

Before creating a project:

- Install [Poetry](https://python-poetry.org/docs/#installation)
- Choose a project name. Likely, in the format `foo-bar` and create a GitHub
  repository for it. The root package of your project will have a default
  name `foo_bar`. Make sure that you made the repository private if you plan to create
  a private (non-open-source) project.
- Choose the license. For public projects use MIT, for private projects use
  "Proprietary".

After creating a project:

- Initialize git repo with `git init`
- Initialize your pre-commit hooks inside the repo with `pre-commit install`. For
  more details follow https://pre-commit.com/
- Initialize virtual environment and install all dependencies with `poetry install`
- Add all files to the repo, review staged changes and commit them.
- Deploy changes to GitHub.
- For Windows, you might need to change your personal access token to GitHub, see information [here](https://github.com/gitextensions/gitextensions/issues/4916#issuecomment-557509451)

Other hints:

- Use [How to Write Good Documentation](https://www.sohamkamani.com/blog/how-to-write-good-documentation/)
  to fill in our README with the content.
- Use [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) guideline for your
  changelog entries.

## Tests with GitHub actions

A file `.github/workflows/tests.yml` is responsible for running tests on GitHub and
upload coverage results to codecov.io.

To make it work with codecov.

- Go to https://app.codecov.io/ and find a repository upload token for your project.
- Go to your repository settings on GitHub, and define the actions secret
  `CODECOV_TOKEN`: Settings → Secrets → New repository secret).

If you don't configure the token, the action quietly skips the upload step.

## How to configure VSCode

At the moment, VSCode doesn't automatically detect Poetry environments. You can set it
manually though. For a newly created project, create a `.vscode/settings.json`

```
poetry install
mkdir -p .vscode
cat <<EOF > .vscode/settings.json
{
  "python.pythonPath": "$(poetry env info -p)/bin/python"
}
EOF
```

Ref: https://github.com/microsoft/vscode-python/issues/8372

## Using .env with VSCode

If you use VSCode and the [vscode-dotenv](https://github.com/mikestead/vscode-dotenv)
extension, add the following lines to your `.vscode/settings.json` file:

```json
"files.associations": {
  "env.example": "dotenv",
  "env.github-actions": "dotenv"
}
```

## How to contribute

Well, just create an issue or a pull request.
