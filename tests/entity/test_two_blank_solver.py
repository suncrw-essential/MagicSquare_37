"""FR-05 two-blank solver — Entity tests."""

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

from grid_fixtures import (
    DT_002_EXPECTED_SOLUTION,
    DT_002_GRID,
    G1_EXPECTED_SOLUTION,
    G1_TWO_BLANK_GRID,
)
from magic_square.entity.two_blank_solver import solve_two_blanks


class TestTwoBlankSolver:
    """D-SOL-01/04, FR-05, AC-12~16 — placement solver."""

    def test_solution_g1_step_a_success(self) -> None:
        """G1 small-first attempt must return the expected int[6]."""
        result = solve_two_blanks(G1_TWO_BLANK_GRID)
        assert result == G1_EXPECTED_SOLUTION

    def test_solution_dt002_success(self) -> None:
        """DT-002 reference grid must return [1,1,1,4,4,16]."""
        result = solve_two_blanks(DT_002_GRID)
        assert result == DT_002_EXPECTED_SOLUTION

    def test_solution_output_contract(self) -> None:
        """G1 output must have length 6 and 1-index coordinates in range."""
        result = solve_two_blanks(G1_TWO_BLANK_GRID)
        assert len(result) == 6
        row1, col1, num1, row2, col2, num2 = result
        assert 1 <= row1 <= 4
        assert 1 <= col1 <= 4
        assert 1 <= row2 <= 4
        assert 1 <= col2 <= 4
        assert {num1, num2} == {7, 10}
