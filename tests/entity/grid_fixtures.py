"""Shared entity test grids (G0, G1, DT-002)."""

from __future__ import annotations

G0_COMPLETE_GRID: list[list[int]] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

G1_TWO_BLANK_GRID: list[list[int]] = [
    [16, 3, 2, 13],
    [5, 0, 11, 8],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]

DT_002_GRID: list[list[int]] = [
    [0, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 0],
]

G1_EXPECTED_SOLUTION = [2, 2, 10, 3, 3, 7]
DT_002_EXPECTED_SOLUTION = [1, 1, 16, 4, 4, 1]
