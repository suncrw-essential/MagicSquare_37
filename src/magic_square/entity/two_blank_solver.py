"""FR-05 two-blank solver."""

from __future__ import annotations

import copy

from magic_square.entity.blank_finder import find_blank_coords
from magic_square.entity.exceptions import NoValidPlacementError
from magic_square.entity.magic_square_validator import is_magic_square
from magic_square.entity.missing_number_finder import find_not_exist_nums


def solve_two_blanks(grid: list[list[int]]) -> list[int]:
    """Solve a two-blank puzzle using small-first then reverse placement.

    Args:
        grid: Valid puzzle grid with exactly two empty cells.

    Returns:
        ``[r1, c1, n1, r2, c2, n2]`` for the first successful attempt.

    Raises:
        NoValidPlacementError: When neither placement attempt is valid.
    """
    (row1, col1), (row2, col2) = find_blank_coords(grid)
    small, large = find_not_exist_nums(grid)

    attempt_one = copy.deepcopy(grid)
    attempt_one[row1 - 1][col1 - 1] = small
    attempt_one[row2 - 1][col2 - 1] = large
    if is_magic_square(attempt_one):
        return [row1, col1, small, row2, col2, large]

    attempt_two = copy.deepcopy(grid)
    attempt_two[row1 - 1][col1 - 1] = large
    attempt_two[row2 - 1][col2 - 1] = small
    if is_magic_square(attempt_two):
        return [row1, col1, large, row2, col2, small]

    raise NoValidPlacementError(
        "No valid magic square placement exists for the given grid."
    )
