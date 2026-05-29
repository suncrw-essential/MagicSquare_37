"""FR-04 magic square validation."""

from __future__ import annotations

from magic_square.entity.constants import (
    EMPTY_CELL,
    GRID_SIZE,
    MAGIC_CONSTANT,
    MAX_CELL_VALUE,
    MIN_CELL_VALUE,
)


def is_magic_square(grid: list[list[int]]) -> bool:
    """Return whether ``grid`` is a complete valid 4x4 magic square.

    Args:
        grid: Candidate completed grid (no empty cells).

    Returns:
        True when all rows, columns, diagonals sum to ``MAGIC_CONSTANT``
        and values are exactly 1..16 each once.
    """
    if any(EMPTY_CELL in row for row in grid):
        return False

    values = [cell for row in grid for cell in row]
    if sorted(values) != list(range(MIN_CELL_VALUE, MAX_CELL_VALUE + 1)):
        return False

    for row in grid:
        if sum(row) != MAGIC_CONSTANT:
            return False

    for col_idx in range(GRID_SIZE):
        if sum(grid[row_idx][col_idx] for row_idx in range(GRID_SIZE)) != MAGIC_CONSTANT:
            return False

    if sum(grid[index][index] for index in range(GRID_SIZE)) != MAGIC_CONSTANT:
        return False

    if (
        sum(grid[index][GRID_SIZE - 1 - index] for index in range(GRID_SIZE))
        != MAGIC_CONSTANT
    ):
        return False

    return True
