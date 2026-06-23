.PHONY: install lint typecheck test coverage clean run ci

install:
	python -m venv .venv && .venv\Scripts\activate && pip install -e ".[dev]"
	.venv\Scripts\pre-commit install 2>nul || true

lint:
	ruff format --check .
	ruff check gzdx tests

typecheck:
	mypy gzdx

test:
	pytest --tb=short -q

coverage:
	pytest --tb=short --cov=gzdx --cov-report=term-missing -q

clean:
	@if exist build rmdir /s /q build
	@if exist dist rmdir /s /q dist
	@if exist *.egg-info rmdir /s /q *.egg-info
	@if exist .pytest_cache rmdir /s /q .pytest_cache
	@if exist .mypy_cache rmdir /s /q .mypy_cache
	@if exist htmlcov rmdir /s /q htmlcov
	@if exist .coverage del /q .coverage 2>nul
	@for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"

run:
	python -m gzdx

ci: lint typecheck coverage
