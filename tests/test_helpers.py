from __future__ import annotations

import pytest

from gzdx.utils.helpers import chunks, clamp, round_to


class TestChunks:
    def test_even(self) -> None:
        assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]

    def test_remainder(self) -> None:
        assert list(chunks([1, 2, 3], 2)) == [[1, 2], [3]]

    def test_empty(self) -> None:
        assert list(chunks([], 3)) == []


class TestClamp:
    def test_within(self) -> None:
        assert clamp(5, 0, 10) == 5

    def test_below(self) -> None:
        assert clamp(-5, 0, 10) == 0

    def test_above(self) -> None:
        assert clamp(15, 0, 10) == 10


class TestRoundTo:
    def test_basic(self) -> None:
        assert round_to(3.14159, 2) == 3.14

    def test_no_decimals(self) -> None:
        assert round_to(3.14159, 0) == 3.0

    def test_rounding_up(self) -> None:
        assert round_to(2.675, 2) == 2.68
