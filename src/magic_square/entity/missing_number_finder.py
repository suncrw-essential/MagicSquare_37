"""FR-03 missing number discovery."""

from __future__ import annotations

from magic_square.entity.constants import EMPTY_CELL, MAX_CELL_VALUE, MIN_CELL_VALUE


def find_not_exist_nums(grid: list[list[int]]) -> tuple[int, int]:
    """Return the two missing values from 1..16 in ascending order.

    Args:
        grid: A puzzle grid with exactly fourteen distinct occupied values.

    Returns:
        ``(a, b)`` where ``a < b`` and both are absent from the grid.
    """
    occupied = {value for row in grid for value in row if value != EMPTY_CELL}
    missing = [
        value
        for value in range(MIN_CELL_VALUE, MAX_CELL_VALUE + 1)
        if value not in occupied
    ]
    return missing[0], missing[1]
