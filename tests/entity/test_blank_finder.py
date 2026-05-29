"""FR-02 blank coordinate discovery — Entity tests."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

_ENTITY_TEST_DIR = Path(__file__).resolve().parent
if str(_ENTITY_TEST_DIR) not in sys.path:
    sys.path.insert(0, str(_ENTITY_TEST_DIR))

from grid_fixtures import G1_TWO_BLANK_GRID
from magic_square.entity.blank_finder import find_blank_coords


class TestBlankFinder:
    """D-LOC-01, FR-02, AC-06/07 — row-major blank coordinates."""

    def test_find_blank_coords_g1_row_major(self) -> None:
        """G1 must yield (2,2) and (3,3) in row-major order."""
        # Given
        grid = G1_TWO_BLANK_GRID
        # When
        first, second = find_blank_coords(grid)
        # Then
        assert first == (2, 2)
        assert second == (3, 3)
