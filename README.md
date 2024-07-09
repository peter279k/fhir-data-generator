# Development setup

- Running the `git clone` to clone the repository.
- Preparing for the `pipenv` environment.
- Running the `pipenv install` command to install packages.
- Running the `pipenv install -d` command to install development packages.
- Running the `pipenv run poetry install` command to install local package.
- Running the `pipenv run pytest -vv` to run unit tests.
- Running the `pipenv run pytest --cov --cov-report html` to run unit tests and generate coverage report with the HTML format. The report will be generated in the `htmlcov` directory.

# Publishing package steps

- Running the `poetry check` command to check whether everything is okay.
- Running the `poetry build` command to build archived Python package file.
- Running the `poetry config pypi-token.pypi <pypi token>` command to configure Pypi token.
- Running the `poetry publish` command to publish the Python package.

# Publish package to testPyi

- Running the `poetry config repositories.test-pypi https://test.pypi.org/legacy/` command to configure testPypi URL.
- Running the `poetry config pypi-token.test-pypi <test_pypi_token>` command to configure testPypi token.
- Running the `poetry publish -r test-pypi` command to publish the testPypi.

# Refrences

- https://hackersandslackers.com/python-poetry-package-manager
- https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04
- https://www.freecodecamp.org/news/how-to-build-and-publish-python-packages-with-poetry
- https://stackoverflow.com/questions/68882603/using-python-poetry-to-publish-to-test-pypi-org
