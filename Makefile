PYTHON = python3
PROJECT_DIR = app
DEVELOPMENT_DIR = _development
SETTINGS_FILE = pyproject.toml

SUBDIRS := '_development'

.PHONY: format lint secure type-check test enable-pre-commit-hooks dev-build dev-install dev-run dev-setup help

help:
	@echo "Available commands:"
	@echo "  make format  - Format the code with black and isort"
	@echo "  make lint    - Lint the code with flake8"
	@echo "  make secure    - Check security issues via bandit"
	@echo "  make type-check    - Check type issues via mypy"
	@echo "  make test    - Run the unit tests"
	@echo "  make enable-pre-commit-hooks    - Enable pre commit hook"
	@echo "  make dev-build  - Make docker up for development server"
	@echo "  make dev-install  - Install development stage dependencies"
	@echo "  make dev-run  - Run development server"
	@echo "  make dev-setup  - Make ready development server"
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

enable-pre-commit-hooks:
	${PYTHON} -m pre_commit install

dev-build:
	cd ${DEVELOPMENT_DIR} && docker compose -f docker-compose.dev.yml up --build -d

dev-install:
	cd ${DEVELOPMENT_DIR} && pip install -r requirements_dev.txt

dev-run:
	cd ${PROJECT_DIR} && ${PYTHON} manage.py runserver

dev-down:
	cd ${DEVELOPMENT_DIR} && docker compose down -v

dev-setup: dev-install dev-build dev-run