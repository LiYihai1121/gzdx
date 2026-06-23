"""Domain models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Item:
    """A generic data item."""
    id: str
    name: str
    value: float = 0.0


__all__ = ["Item"]
