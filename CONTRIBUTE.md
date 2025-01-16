# Contribute

You are very welcome to contribute to this repo or fork it for your own setup.

## Development Environment

- A Python IDE
- Poetry
  - https://python-poetry.org/docs/#installing-with-the-official-installer
- Open the project IDE and choose your Poetry installation as Python Interpreter.
- This loads the dependencies from the files within this project.

--> Now you can work with the code

- To install during development:
- `poetry install`
  - Then you can run for example: `poetry run anabolicarius init`


- To build (and install)
- `poetry build`
- `pip install .\dist\...` either the .whl or the .tar.gz
  - Then you can run the anabolicarius cli, e.g.: "init" ``anabolicarius init``