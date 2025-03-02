
PYTHON = python3

PROJECT_DIR = app

SETTINGS_FILE = pyproject.toml

PHONY = help format lint check all

help:
	@echo "Available commands:"
	@echo "  make format  - Format the code with black and isort"
	@echo "  make lint    - Lint the code with autoflake and flake8"
	@echo "  make check   - Check the code quality with autoflake and flake8"
	@echo "  make all     - Run all tasks: format, lint, check"
	@echo "  make_help    - Show this help message"

format:
	${PYTHON} -m black ${PROJECT_DIR} --config ${SETTINGS_FILE}
	${PYTHON} -m isort ${PROJECT_DIR} --settings-file ${SETTINGS_FILE}

lint:
	${PYTHON} -m autoflake --recursive --in-place ${PROJECT_DIR}
	${PYTHON} -m flake8 ${PROJECT_DIR} --config ${SETTINGS_FILE}

check:
	${PYTHON} -m autoflake --check --recursive ${PROJECT_DIR}
	${PYTHON} -m flake8 ${PROJECT_DIR} --config ${SETTINGS_FILE}

all:
	${MAKE} make format
	${MAKE} make lint
	${MAKE} make check

