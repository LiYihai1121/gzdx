.PHONY: install lint test clean run

install:
	python -m venv .venv
	.venv\Scripts\activate && pip install -e ".[dev]"

lint:
	ruff check src tests
	mypy src

test:
	pytest --tb=short -q

clean:
	rm -rf build dist *.egg-info .pytest_cache .mypy_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +

run:
	python -m src.main
