from __future__ import annotations

from gzdx.config import Settings


def test_settings_defaults() -> None:
    s = Settings.load()
    assert s.log_level == "INFO"
    assert isinstance(s.debug, bool)
    assert s.data_dir == "./data"


def test_settings_immutable() -> None:
    s = Settings.load()
    assert isinstance(s, Settings)


def test_settings_with_env(monkeypatch) -> None:
    monkeypatch.setenv("GZDX_DEBUG", "true")
    monkeypatch.setenv("GZDX_LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("GZDX_DATA_DIR", "/custom/data")
    s = Settings.load()
    assert s.debug is True
    assert s.log_level == "DEBUG"
    assert s.data_dir == "/custom/data"
