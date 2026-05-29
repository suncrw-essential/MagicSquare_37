"""FR-03 missing number discovery — Entity tests."""

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
from magic_square.entity.missing_number_finder import find_not_exist_nums


class TestMissingNumberFinder:
    """D-MIS-01, FR-03, AC-08/09 — sorted missing pair."""

    def test_find_not_exist_nums_g1_sorted(self) -> None:
        """G1 must yield missing numbers (7, 10) in ascending order."""
        # Given
        grid = G1_TWO_BLANK_GRID
        # When
        first, second = find_not_exist_nums(grid)
        # Then
        assert first == 7
        assert second == 10
        assert first < second
