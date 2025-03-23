PYTHON = python3
PROJECT_DIR = app
SETTINGS_FILE = pyproject.toml

.PHONY: help format lint

help:
	@echo "Available commands:"
	@echo "  make format  - Format the code with black and isort"
	@echo "  make lint    - Lint the code with flake8"
	@echo "  make test    - Run the unit tests"
	@echo "  make help    - Show this help message"

format:
	$(PYTHON) -m isort $(PROJECT_DIR) --settings $(SETTINGS_FILE)
	$(PYTHON) -m autoflake $(PROJECT_DIR) --config $(SETTINGS_FILE)
	$(PYTHON) -m black $(PROJECT_DIR) --config $(SETTINGS_FILE)
	$(PYTHON) -m autopep8 $(PROJECT_DIR) --global-config $(SETTINGS_FILE)

lint:
	$(PYTHON) -m flake8 --config $(SETTINGS_FILE) $(PROJECT_DIR)
	$(PYTHON) -m black $(PROJECT_DIR) --check --diff --config $(SETTINGS_FILE)
	$(PYTHON) -m isort $(PROJECT_DIR) --check --diff --settings $(SETTINGS_FILE)

secure:
	$(PYTHON) -m bandit -r $(PROJECT_DIR) --config ${SETTINGS_FILE}

type-check:
	$(PYTHON) -m mypy $(PROJECT_DIR) --config ${SETTINGS_FILE}

test:
	cd ${PROJECT_DIR} && ${PYTHON} manage.py test

install:
	pip install -r requirements.txt