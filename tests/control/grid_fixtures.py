"""Control-layer test grids (D-SOL / SC-CTL RED)."""

from __future__ import annotations

G1_TWO_BLANK_GRID: list[list[int]] = [
    [16, 3, 2, 13],
    [5, 0, 11, 8],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]

G1_EXPECTED_SOLUTION: list[int] = [2, 2, 10, 3, 3, 7]

REVERSE_SUCCESS_GRID: list[list[int]] = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 0, 12],
    [4, 14, 15, 0],
]

REVERSE_EXPECTED_SOLUTION: list[int] = [3, 3, 6, 4, 4, 1]

NO_SOLUTION_GRID: list[list[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 0],
    [12, 13, 14, 0],
]
