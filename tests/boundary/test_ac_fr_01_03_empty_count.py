"""AC-FR-01-03 empty cell count — Boundary tests."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

_BOUNDARY_TEST_DIR = Path(__file__).resolve().parent
if str(_BOUNDARY_TEST_DIR) not in sys.path:
    sys.path.insert(0, str(_BOUNDARY_TEST_DIR))

from constants import (
    AC_FR_01_03_CODE,
    AC_FR_01_03_MESSAGE,
    AC_FR_01_03_PARAM_GRIDS,
    THREE_EMPTY_CELLS_GRID,
)
from magic_square.boundary.errors import FailureResult
from magic_square.boundary.screen_boundary import ScreenBoundary
from magic_square.entity.resolver import DomainResolver

COMPLETE_GRID_NO_EMPTIES: list[list[int]] = AC_FR_01_03_PARAM_GRIDS[0]
PRD_SECTION_8_3_MESSAGE = AC_FR_01_03_MESSAGE


class TestAcFr0103EmptyCountFailure:
    """AC-FR-01-03, PRD §8.1 ERR_EMPTY_COUNT — wrong empty-cell count."""

    def test_complete_grid_returns_err_empty_count_code(
        self, boundary: ScreenBoundary
    ) -> None:
        """G0 complete grid (0 empties) must yield ERR_EMPTY_COUNT."""
        grid = COMPLETE_GRID_NO_EMPTIES
        result = boundary.solve(grid)
        assert isinstance(result, FailureResult)
        assert result.code == AC_FR_01_03_CODE

    def test_three_empty_cells_returns_err_empty_count_code(
        self, boundary: ScreenBoundary
    ) -> None:
        """Grid with three zeros must yield ERR_EMPTY_COUNT."""
        grid = THREE_EMPTY_CELLS_GRID
        result = boundary.solve(grid)
        assert result.code == AC_FR_01_03_CODE

    def test_complete_grid_returns_prd_message(
        self, boundary: ScreenBoundary
    ) -> None:
        """G0 must yield PRD §8.1 empty-count message."""
        grid = COMPLETE_GRID_NO_EMPTIES
        result = boundary.solve(grid)
        assert result.message == AC_FR_01_03_MESSAGE

    def test_three_empty_cells_returns_prd_message(
        self, boundary: ScreenBoundary
    ) -> None:
        """Three-zero grid must yield PRD §8.1 empty-count message."""
        grid = THREE_EMPTY_CELLS_GRID
        result = boundary.solve(grid)
        assert result.message == AC_FR_01_03_MESSAGE


class TestAcFr0103DomainIsolation:
    """AC-FR-01-03 — resolve() must not be invoked on empty-count failure."""

    def test_complete_grid_resolve_zero_calls_spy(
        self, boundary: ScreenBoundary, mock_resolver: DomainResolver
    ) -> None:
        """G0 must not call resolve()."""
        boundary.solve(COMPLETE_GRID_NO_EMPTIES)
        assert mock_resolver.resolve.call_count == 0

    def test_three_empty_cells_resolve_zero_calls_spy(
        self, boundary: ScreenBoundary, mock_resolver: DomainResolver
    ) -> None:
        """Three-zero grid must not call resolve()."""
        boundary.solve(THREE_EMPTY_CELLS_GRID)
        assert mock_resolver.resolve.call_count == 0


class TestAcFr0103MessageIdentity:
    """AC-FR-01-03 — message byte-for-byte identity."""

    def test_complete_grid_message_exact_prd_section_8_1(
        self, boundary: ScreenBoundary
    ) -> None:
        """G0 message must match PRD §8.1 exactly."""
        result = boundary.solve(COMPLETE_GRID_NO_EMPTIES)
        assert isinstance(result, FailureResult)
        assert result.message == PRD_SECTION_8_3_MESSAGE


@pytest.mark.parametrize("grid", AC_FR_01_03_PARAM_GRIDS)
class TestAcFr0103ParametrizedContract:
    """AC-FR-01-03 — parametrized empty-count contract checks."""

    def test_param_grid_returns_err_empty_count_code(
        self, boundary: ScreenBoundary, grid: Any
    ) -> None:
        """Each in-scope grid must return ERR_EMPTY_COUNT."""
        result = boundary.solve(grid)
        assert result.code == AC_FR_01_03_CODE

    def test_param_grid_resolve_zero_calls(
        self, boundary: ScreenBoundary, mock_resolver: DomainResolver, grid: Any
    ) -> None:
        """Each in-scope grid must not invoke resolve()."""
        boundary.solve(grid)
        assert mock_resolver.resolve.call_count == 0
