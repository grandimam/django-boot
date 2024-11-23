.PHONY: install-hooks format lint

install-hooks:
	pre-commit install

format:
	black .
	isort .

lint:
	flake8 .
	pre-commit run --all-files
