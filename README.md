# Table App & Api

There is an API for some nominal customer, which provide us with statistic information

## Installation

Use [pipenv](https://pypi.org/project/pipenv/) package manager to install all requirements from Pipfile.

```bash
pipenv update
```

Activate virtual environment:

```bash
pipenv shell
```

Also MySQL for database required. Set all options for database by settings.py file in DATABASE section.
settings.py location is config folder.
After all DATABASE settings done run the following command

```bash
python manage.py migrate
```

DEBAG = True
