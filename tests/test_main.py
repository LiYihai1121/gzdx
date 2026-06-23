from __future__ import annotations

from gzdx import __version__


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_imports() -> None:
    from gzdx.config import Settings
    from gzdx.logger import setup_logging
    from gzdx.models import Item
    from gzdx.utils.helpers import chunks, clamp, round_to

    assert Settings
    assert setup_logging
    assert Item
    assert chunks
    assert clamp
    assert round_to
