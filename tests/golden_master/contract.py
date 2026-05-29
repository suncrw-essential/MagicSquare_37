"""Golden Master output contract assertions (GM-2)."""

from __future__ import annotations

import copy
from typing import Literal

from magic_square.boundary.errors import FailureResult
from magic_square.entity.blank_finder import find_blank_coords
from magic_square.entity.constants import GRID_SIZE
from magic_square.entity.magic_square_validator import is_magic_square
from magic_square.entity.missing_number_finder import find_not_exist_nums

PlacementKind = Literal["small_first", "reverse"]


def assert_int_six_tuple(result: list[int]) -> None:
    """OUT-01 — success path must return exactly six integers."""
    assert isinstance(result, list)
    assert len(result) == 6
    assert all(isinstance(value, int) for value in result)


def assert_one_index_coordinates(result: list[int]) -> None:
    """OUT-02/03 — rows and columns are 1-indexed within the grid."""
    row1, col1, _num1, row2, col2, _num2 = result
    for row, col in ((row1, col1), (row2, col2)):
        assert 1 <= row <= GRID_SIZE
        assert 1 <= col <= GRID_SIZE


def assert_row_major_blank_order(grid: list[list[int]], result: list[int]) -> None:
    """Blank coordinates in the result follow row-major discovery order."""
    (expected_r1, expected_c1), (expected_r2, expected_c2) = find_blank_coords(grid)
    row1, col1, _num1, row2, col2, _num2 = result
    assert (row1, col1) == (expected_r1, expected_c1)
    assert (row2, col2) == (expected_r2, expected_c2)


def assert_small_first_placement(grid: list[list[int]], result: list[int]) -> None:
    """FR-05 — small-first attempt succeeds before reverse fallback."""
    (row1, col1), (row2, col2) = find_blank_coords(grid)
    small, large = find_not_exist_nums(grid)
    attempt_one = copy.deepcopy(grid)
    attempt_one[row1 - 1][col1 - 1] = small
    attempt_one[row2 - 1][col2 - 1] = large
    assert is_magic_square(attempt_one)
    assert result == [row1, col1, small, row2, col2, large]


def assert_reverse_fallback_placement(grid: list[list[int]], result: list[int]) -> None:
    """FR-05 — reverse attempt succeeds only after small-first fails."""
    (row1, col1), (row2, col2) = find_blank_coords(grid)
    small, large = find_not_exist_nums(grid)
    attempt_one = copy.deepcopy(grid)
    attempt_one[row1 - 1][col1 - 1] = small
    attempt_one[row2 - 1][col2 - 1] = large
    attempt_two = copy.deepcopy(grid)
    attempt_two[row1 - 1][col1 - 1] = large
    attempt_two[row2 - 1][col2 - 1] = small
    assert not is_magic_square(attempt_one)
    assert is_magic_square(attempt_two)
    assert result == [row1, col1, large, row2, col2, small]


def assert_success_contract(
    grid: list[list[int]],
    result: list[int],
    *,
    placement: PlacementKind,
) -> None:
    """Validate int[6], 1-index, row-major, and placement-order rules."""
    assert_int_six_tuple(result)
    assert_one_index_coordinates(result)
    assert_row_major_blank_order(grid, result)
    if placement == "small_first":
        assert_small_first_placement(grid, result)
    else:
        assert_reverse_fallback_placement(grid, result)


def assert_error_contract(result: FailureResult, expected_code: str) -> None:
    """Boundary error DTO must expose the committed machine-readable code."""
    assert isinstance(result, FailureResult)
    assert result.code == expected_code
