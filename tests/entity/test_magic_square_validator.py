"""FR-04 magic square validation — Entity tests."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

_ENTITY_TEST_DIR = Path(__file__).resolve().parent
if str(_ENTITY_TEST_DIR) not in sys.path:
    sys.path.insert(0, str(_ENTITY_TEST_DIR))

from grid_fixtures import G0_COMPLETE_GRID
from magic_square.entity.magic_square_validator import is_magic_square


class TestMagicSquareValidator:
    """D-VAL-01~06, FR-04, AC-10/11 — magic square predicate."""

    def test_is_magic_square_g0_true(self) -> None:
        """Complete G0 grid must validate as a magic square."""
        assert is_magic_square(G0_COMPLETE_GRID) is True

    def test_is_magic_square_row_mismatch_false(self) -> None:
        """Breaking one row sum must invalidate the grid."""
        grid = copy.deepcopy(G0_COMPLETE_GRID)
        grid[0][0] = 15
        grid[0][1] = 4
        assert is_magic_square(grid) is False

    def test_is_magic_square_col_mismatch_false(self) -> None:
        """Breaking one column sum must invalidate the grid."""
        grid = copy.deepcopy(G0_COMPLETE_GRID)
        grid[0][0] = 15
        grid[1][0] = 4
        assert is_magic_square(grid) is False

    def test_is_magic_square_diagonal_mismatch_false(self) -> None:
        """Breaking a diagonal sum must invalidate the grid."""
        grid = copy.deepcopy(G0_COMPLETE_GRID)
        grid[0][0] = 15
        grid[3][3] = 2
        assert is_magic_square(grid) is False

    def test_is_magic_square_duplicate_false(self) -> None:
        """Duplicate non-zero values must invalidate the grid."""
        grid = [
            [16, 3, 2, 13],
            [5, 10, 11, 8],
            [9, 6, 7, 12],
            [4, 15, 14, 16],
        ]
        assert is_magic_square(grid) is False

    def test_is_magic_square_with_zero_false(self) -> None:
        """Incomplete grids containing zero must not validate."""
        grid = copy.deepcopy(G0_COMPLETE_GRID)
        grid[0][0] = 0
        assert is_magic_square(grid) is False
