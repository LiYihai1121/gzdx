"""Entry-point CLI using argparse."""

from __future__ import annotations

import argparse
import sys

from gzdx import __version__
from gzdx.logger import setup_logging


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="gzdx", description="gzdx project CLI")
    parser.add_argument("--version", action="version", version=f"gzdx {__version__}")
    parser.add_argument("--debug", action="store_true", help="enable debug output")
    sub = parser.add_subparsers(dest="command", required=False)

    # hello subcommand
    hello = sub.add_parser("hello", help="say hello")
    hello.add_argument("name", nargs="?", default="world", help="who to greet")

    # info subcommand
    info = sub.add_parser("info", help="show project info")
    return parser


def app(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv or sys.argv[1:])

    level = "DEBUG" if args.debug else "INFO"
    setup_logging(level)

    if args.command == "hello":
        print(f"Hello, {args.name}!")
    elif args.command == "info":
        import platform
        print(f"gzdx {__version__}")
        print(f"Python {platform.python_version()}")
    else:
        parser.print_help()


if __name__ == "__main__":
    app()
