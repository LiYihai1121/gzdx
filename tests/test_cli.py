from __future__ import annotations

from gzdx.cli.main import app, build_parser


def test_parser_build() -> None:
    parser = build_parser()
    assert parser.prog == "gzdx"


def test_hello(capsys) -> None:
    app(["hello", "gzdx"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, gzdx!"


def test_hello_default(capsys) -> None:
    app(["hello"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, world!"


def test_info(capsys) -> None:
    app(["info"])
    captured = capsys.readouterr()
    assert "gzdx" in captured.out
    assert "Python" in captured.out
