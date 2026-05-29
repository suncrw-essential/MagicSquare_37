"""FR-02 blank coordinate discovery."""

from __future__ import annotations

from magic_square.entity.constants import EMPTY_CELL


def find_blank_coords(
    grid: list[list[int]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Locate the first and second empty cells in row-major order (1-index).

    Args:
        grid: A GRID_SIZE x GRID_SIZE puzzle grid with exactly two empty cells.

    Returns:
        ``((r1, c1), (r2, c2))`` using 1-based coordinates.
    """
    blanks: list[tuple[int, int]] = []
    for row_idx, row in enumerate(grid):
        for col_idx, value in enumerate(row):
            if value == EMPTY_CELL:
                blanks.append((row_idx + 1, col_idx + 1))
    return blanks[0], blanks[1]
