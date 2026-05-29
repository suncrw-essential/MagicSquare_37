"""FR-05 success path — Boundary integration tests."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

_ENTITY_TEST_DIR = PROJECT_ROOT / "tests" / "entity"
if str(_ENTITY_TEST_DIR) not in sys.path:
    sys.path.insert(0, str(_ENTITY_TEST_DIR))

from grid_fixtures import (
    DT_002_EXPECTED_SOLUTION,
    DT_002_GRID,
    G1_EXPECTED_SOLUTION,
    G1_TWO_BLANK_GRID,
)
from magic_square.boundary.screen_boundary import ScreenBoundary
from magic_square.entity.puzzle_resolver import PuzzleDomainResolver


class TestBoundarySuccessPath:
    """U-OUT-01/02, FR-05 — valid grid returns int[6] via domain resolver."""

    def test_valid_g1_returns_six_int_success_array(self) -> None:
        """G1 must return a six-int placement tuple."""
        boundary = ScreenBoundary(resolver=PuzzleDomainResolver())
        result = boundary.solve(G1_TWO_BLANK_GRID)
        assert isinstance(result, list)
        assert len(result) == 6
        assert result == G1_EXPECTED_SOLUTION

    def test_valid_dt002_coordinates_one_indexed(self) -> None:
        """DT-002 must return 1-index coordinates and missing numbers."""
        boundary = ScreenBoundary(resolver=PuzzleDomainResolver())
        result = boundary.solve(DT_002_GRID)
        assert result == DT_002_EXPECTED_SOLUTION
        row1, col1, num1, row2, col2, num2 = result
        assert row1 == 1 and col1 == 1 and num1 == 16
        assert row2 == 4 and col2 == 4 and num2 == 1
