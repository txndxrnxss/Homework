PYTHON=python3
PIP=pip3

install:
    $(PIP) install -r requirements.txt

flake8:
    $(PYTHON) -m flake8 .

isort:
    $(PYTHON) -m isort .

black:
    $(PYTHON) -m black --check .

format:
    $(PYTHON) -m isort .
    $(PYTHON) -m black .

check: flake8 isort black  