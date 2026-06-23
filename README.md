# gzdx

projects learning

## Quick Start (Conda)

`ash
# Create conda environment and install the project
make conda-setup

# Activate environment
conda activate gzdx

# Run CLI
python -m gzdx hello
python -m gzdx hello gzdx
python -m gzdx info
python -m gzdx --help
`

Alternatively, use the gzdx command after activation:

`ash
gzdx hello
`

## Development

`ash
# Run tests
make test
`

`ash
# Test with coverage
make coverage
`

`ash
# Lint & type check
make lint
make typecheck

# Full CI suite
make ci
`

## Commands

| Command | Description |
|---------|-------------|
| make conda-setup | Create gzdx conda environment from environment.yml |
| make install | Install/update project in the conda environment |
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
├── environment.yml    # Conda environment definition
├── .condarc           # Conda channel config
├── Makefile
├── pyproject.toml
├── LICENSE            # Apache 2.0
└── README.md
`

## License

Apache 2.0 -- see [LICENSE](LICENSE).
