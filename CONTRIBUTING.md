# Contributing

## Instructions for contributing code

1. Install `poetry` for package management.

Go to the [poetry](https://python-poetry.org/docs/) website and follow the
[instructions](https://python-poetry.org/docs/#installation) to install it to your machine.

2. Clone the project for local development.

```bash
git clone https://github.com/IgnisDa/Inscribe
cd Inscribe/
```

3. Install the project dependencies (virtual environment will be created automatically).

```bash
poetry install
```

4. Activate the virtual environment.

```bash
poetry shell
```

5. Create the database and start the website for local development.

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

6. Making commits to the repository.

To make it easier for you to make conventional commits, we use
[`commitizen`](https://github.com/commitizen/cz-cli) to manage our commits.

```bash
git add <file1> <file2> ...
git status
cz c
```

Follow the prompts to make a conventional commit.

## Issues

Issues are very valuable to this project.

- Ideas are a valuable source of contributions others can make
- Problems show where this project is lacking
- With a question you show where contributors can improve the user
  experience

Thank you for creating them.

## Pull Requests

Pull requests are a great way to get your ideas into this repository.

When deciding if I merge in a pull request I look at the following
things:

### Does it follow the contributor covenant

This repository has a [code of conduct](CODE_OF_CONDUCT.md), things that do not
respect it will be removed.

### Have the tests passed

The project is tested using `pytest` and `pytest-django`. To run the tests, run the
following commands in the project root. Before making a change to the repository, please
ensure that these tests all pass.

```bash
pytest --cov --cov-report=xml --cache-clear --cov-report term-missing --flake8
```

This will output the test results as well as show the coverage achieved for the test run.

### After contributing to this repository

After successfully getting your issue merged, please add your name to the list of
contributors in [contributors.md](contributors.md).
