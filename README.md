# Development setup

- Running the `git clone` to clone the repository.
- Preparing the `pipenv` environment.
- Running the `pipenv install -e .`.
- Running the `pipenv run pytest -vv` to run unit tests.
- Running the `pipenv run pytest --cov-report html` to run unit tests and generate coverage report with the HTML format. The report will be generated in the `htmlcov` directory.

# Publishing package steps

- Running the `poetry check` command.
- Running the `poetry build --username <username> --password <password>` command.

# Refrences

- https://hackersandslackers.com/python-poetry-package-manager
- https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04
- https://www.freecodecamp.org/news/how-to-build-and-publish-python-packages-with-poetry
- https://stackoverflow.com/questions/68882603/using-python-poetry-to-publish-to-test-pypi-org
