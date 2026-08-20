.PHONY: test lint test-coverage

test:
	uv run pytest

lint:
	uv run ruff check .

test-coverage:
	uv run pytest --cov=gendiff --cov-report=term-missing