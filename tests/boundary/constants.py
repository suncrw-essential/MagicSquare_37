"""AC-FR-01-01 test constants shared by boundary tests."""

from __future__ import annotations

from typing import Any

AC_FR_01_01_CODE = "INVALID_SIZE"
AC_FR_01_01_MESSAGE = "Grid must be 4x4."

THREE_BY_FOUR_GRID: list[list[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

FOUR_EMPTY_ROW_LISTS: list[list[int]] = [[]] * 4

AC_FR_01_01_PARAM_GRIDS: list[Any] = [
    None,
    [],
    FOUR_EMPTY_ROW_LISTS,
    THREE_BY_FOUR_GRID,
]

FORBIDDEN_AC_FR_01_02_05_GRIDS: list[Any] = [
    [[1, 2, 3, 0], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
    [[1, 2, 3, 17], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
    [[1, 1, 3, 0], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]],
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
]

AC_FR_01_03_CODE = "ERR_EMPTY_COUNT"
AC_FR_01_03_MESSAGE = "Grid must contain exactly 2 empty cells (0)."

THREE_EMPTY_CELLS_GRID: list[list[int]] = [
    [0, 3, 2, 13],
    [5, 0, 11, 8],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]

AC_FR_01_03_PARAM_GRIDS: list[Any] = [
    [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ],
    THREE_EMPTY_CELLS_GRID,
]
