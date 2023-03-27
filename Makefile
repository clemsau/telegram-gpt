.PHONY: run format lint type-check all

run:
	python main.py

format:
	black .
	isort .

lint:
	ruff .

type-check:
	mypy ./src

qa: format lint type-check
