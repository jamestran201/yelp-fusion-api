.PHONY: install

install:
	poetry install
	poetry run pre-commit install --hook-type pre-push
