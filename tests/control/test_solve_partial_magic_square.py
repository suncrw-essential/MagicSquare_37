"""Control layer RED tests — D-SOL-01~04, SC-CTL-001 (Report/14 §6).

Expected RED failure until ``src/magic_square/control/`` exists (C3 GREEN).
Tier 1 Phase 0 excludes this directory: ``pytest tests/ --ignore=tests/control``.
"""

from __future__ import annotations

import sys
from pathlib import Path
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

_CONTROL_TEST_DIR = Path(__file__).resolve().parent
if str(_CONTROL_TEST_DIR) not in sys.path:
    sys.path.insert(0, str(_CONTROL_TEST_DIR))

from grid_fixtures import (
    G1_EXPECTED_SOLUTION,
    G1_TWO_BLANK_GRID,
    NO_SOLUTION_GRID,
    REVERSE_EXPECTED_SOLUTION,
    REVERSE_SUCCESS_GRID,
)
from magic_square.entity.constants import GRID_SIZE
from magic_square.entity.exceptions import NoValidPlacementError

pytestmark = pytest.mark.control_red


def _load_solve_partial_magic_square():
    """Import target under test (RED: module missing until C3)."""
    from magic_square.control.solve_partial_magic_square import (
        SolvePartialMagicSquare,
    )

    return SolvePartialMagicSquare


class TestSolvePartialMagicSquareDsol:
    """D-SOL-01~04 — Control orchestration (Report/09, Report/14)."""

    def test_d_sol_01_g1_step_a_success(self) -> None:
        """G1 small-first placement returns committed int[6]."""
        solver = _load_solve_partial_magic_square()
        result = solver.execute(G1_TWO_BLANK_GRID)
        assert result == G1_EXPECTED_SOLUTION

    def test_d_sol_02_g2_reverse_success(self) -> None:
        """G2 reverse fallback returns GM-TC-02 placement."""
        solver = _load_solve_partial_magic_square()
        result = solver.execute(REVERSE_SUCCESS_GRID)
        assert result == REVERSE_EXPECTED_SOLUTION

    def test_d_sol_03_no_valid_placement(self) -> None:
        """G3 unsolvable grid raises domain no-placement error."""
        solver = _load_solve_partial_magic_square()
        with pytest.raises(NoValidPlacementError):
            solver.execute(NO_SOLUTION_GRID)

    def test_d_sol_04_output_contract(self) -> None:
        """OUT-01/02 — length 6 and 1-index coordinates in range."""
        solver = _load_solve_partial_magic_square()
        result = solver.execute(G1_TWO_BLANK_GRID)
        assert len(result) == 6
        row1, col1, _n1, row2, col2, _n2 = result
        for row, col in ((row1, col1), (row2, col2)):
            assert 1 <= row <= GRID_SIZE
            assert 1 <= col <= GRID_SIZE


class TestSolvePartialMagicSquareFlow:
    """SC-CTL-001 — invalid input rejected at control boundary (Report/09 U-FLOW-02)."""

    def test_sc_ctl_001_null_matrix_rejected(self) -> None:
        """null matrix must not return success int[6] (C3: map to failure or raise)."""
        solver = _load_solve_partial_magic_square()
        with pytest.raises((TypeError, ValueError, AttributeError)):
            solver.execute(None)  # type: ignore[arg-type]
