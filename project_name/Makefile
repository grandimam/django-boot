.PHONY: install install-hooks runserver lint format

install:
	pip install -r requirements.txt


install-hooks:
	pre-commit install


runserver:
	python manage.py runserver


lint:
	flake8 .


format:
	black .
	isort .
