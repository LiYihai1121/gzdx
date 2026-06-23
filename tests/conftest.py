from __future__ import annotations

import pytest

from gzdx.config import Settings
from gzdx.models import Item


@pytest.fixture
def settings() -> Settings:
    return Settings.load()


@pytest.fixture
def sample_item() -> Item:
    return Item(id="001", name="test-item", value=3.14)
