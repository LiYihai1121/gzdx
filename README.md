# gzdx

projects learning

## Getting Started

`ash
# Create virtual environment & install
make install
# Activate
.venv\Scripts\activate
`

`ash
# Run CLI
gzdx hello
gzdx hello gzdx
gzdx info
gzdx --help

# Or via module
python -m gzdx hello
`

`ash
# Run tests
make test
# With coverage
make coverage
`

`ash
# Lint & type check
make lint
make typecheck

# Full CI
make ci
`

## Commands

| Command | Description |
|---------|-------------|
| make install | Create venv + install package + pre-commit hook |
| make run | Run CLI via python -m gzdx |
| make test | Run pytest |
| make coverage | Test with coverage report |
| make lint | ruff check + format check |
| make typecheck | mypy type checking |
| make clean | Remove build/cache artefacts |
| make ci | All checks (lint + typecheck + coverage) |

## Project Structure

`
├── gzdx/              # Main package
│   ├── cli/           #  CLI entry-point (argparse)
│   ├── models/        #  Domain data models
│   ├── utils/         #  Utility helpers
│   ├── config.py      #  Environment-based settings
│   ├── logger.py      #  Logging setup
│   └── __main__.py    #  python -m gzdx
├── tests/             # pytest suite
│   ├── conftest.py    #  Shared fixtures
│   ├── test_cli.py
│   ├── test_config.py
│   ├── test_helpers.py
│   └── test_main.py
├── docs/              # Documentation
├── .github/workflows/ # GitHub Actions CI
├── .pre-commit-config.yaml
├── Makefile
├── pyproject.toml
├── LICENSE            # Apache 2.0
└── README.md
`

## License

Apache 2.0 -- see [LICENSE](LICENSE).
