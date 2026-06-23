"""Generic helper utilities."""

from __future__ import annotations

import math
from collections.abc import Iterable


def chunks[T](seq: Iterable[T], size: int) -> Iterable[list[T]]:
    """Yield successive *size*-sized chunks from *seq*."""
    buf: list[T] = []
    for item in seq:
        buf.append(item)
        if len(buf) == size:
            yield buf
            buf = []
    if buf:
        yield buf


def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp *value* to [*lo*, *hi*]."""
    return max(lo, min(hi, value))


def round_to(value: float, decimals: int = 2) -> float:
    """Round to *decimals* places, avoiding float surprises."""
    return float(f"{value:.{decimals}f}")
