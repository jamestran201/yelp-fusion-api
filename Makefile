.PHONY: install check lint mypy

install:
	poetry install
	poetry run pre-commit install --hook-type pre-push

check: lint mypy

lint:
	poetry run black .
	poetry run isort .
	poetry run flake8

mypy:
	poetry run mypy --install-types yelpfusion
