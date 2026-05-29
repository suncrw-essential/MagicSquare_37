"""AC-FR-01-01 invalid grid size — Boundary RED tests."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from magic_square.boundary.errors import FailureResult
from magic_square.boundary.screen_boundary import ScreenBoundary
from magic_square.entity.resolver import DomainResolver

_BOUNDARY_TEST_DIR = Path(__file__).resolve().parent
if str(_BOUNDARY_TEST_DIR) not in sys.path:
    sys.path.insert(0, str(_BOUNDARY_TEST_DIR))

from constants import (
    AC_FR_01_01_CODE,
    AC_FR_01_01_MESSAGE,
    AC_FR_01_01_PARAM_GRIDS,
    FORBIDDEN_AC_FR_01_02_05_GRIDS,
    FOUR_EMPTY_ROW_LISTS,
    THREE_BY_FOUR_GRID,
)

PRD_SECTION_8_1_MESSAGE = AC_FR_01_01_MESSAGE


class TestAcFr0101NormalFailureReturn:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — normal failure return."""

    def test_none_grid_returns_failure_invalid_size_code(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=None must yield INVALID_SIZE failure code."""
        # Given
        grid = None
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert isinstance(result, FailureResult)
        assert result.code == AC_FR_01_01_CODE

    def test_none_grid_returns_failure_prd_message(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=None must yield PRD §8.1 message."""
        # Given
        grid = None
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert result.message == AC_FR_01_01_MESSAGE

    def test_none_grid_returns_failure_not_success_tuple(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=None must not return a six-int success tuple."""
        # Given
        grid = None
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert not isinstance(result, (list, tuple))

    def test_none_grid_returns_failure_result_type(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=None must return the designated FailureResult structure."""
        # Given
        grid = None
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert type(result) is FailureResult

    def test_none_grid_returns_failure_without_unhandled_exception(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=None must complete via contract failure, not bare exception."""
        # Given
        grid = None
        # When / Then
        # AC-FR-01-01
        result = boundary.solve(grid)
        assert result.code == AC_FR_01_01_CODE
        assert result.message == AC_FR_01_01_MESSAGE


class TestAcFr0101BoundaryValues:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — boundary value grids."""

    def test_empty_list_grid_returns_failure_invalid_size_code(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=[] must yield INVALID_SIZE failure code."""
        # Given
        grid: list[list[int]] = []
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert result.code == AC_FR_01_01_CODE

    def test_four_empty_row_lists_grid_returns_failure_invalid_size_code(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=[[]]*4 must yield INVALID_SIZE failure code."""
        # Given
        grid = FOUR_EMPTY_ROW_LISTS
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert result.code == AC_FR_01_01_CODE

    def test_three_by_four_grid_returns_failure_invalid_size_code(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=3x4 must yield INVALID_SIZE failure code."""
        # Given
        grid = THREE_BY_FOUR_GRID
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert result.code == AC_FR_01_01_CODE

    def test_empty_list_grid_returns_failure_prd_message(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=[] must yield PRD §8.1 message."""
        # Given
        grid: list[list[int]] = []
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert result.message == AC_FR_01_01_MESSAGE

    def test_three_by_four_grid_returns_failure_result_type(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=3x4 must return FailureResult, not success payload."""
        # Given
        grid = THREE_BY_FOUR_GRID
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert isinstance(result, FailureResult)
        assert result.message == AC_FR_01_01_MESSAGE


class TestAcFr0101DomainIsolation:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — resolve() must not be invoked."""

    def test_none_grid_resolve_zero_calls_spy(
        self, boundary: ScreenBoundary, mock_resolver: DomainResolver
    ) -> None:
        """grid=None must not call resolve()."""
        # Given
        grid = None
        # When
        boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert mock_resolver.resolve.call_count == 0

    def test_empty_list_grid_resolve_zero_calls_spy(
        self, boundary: ScreenBoundary, mock_resolver: DomainResolver
    ) -> None:
        """grid=[] must not call resolve()."""
        # Given
        grid: list[list[int]] = []
        # When
        boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert mock_resolver.resolve.call_count == 0

    def test_four_empty_row_lists_resolve_zero_calls_spy(
        self, boundary: ScreenBoundary, mock_resolver: DomainResolver
    ) -> None:
        """grid=[[]]*4 must not call resolve()."""
        # Given
        grid = FOUR_EMPTY_ROW_LISTS
        # When
        boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert mock_resolver.resolve.call_count == 0

    def test_three_by_four_grid_resolve_zero_calls_spy(
        self, boundary: ScreenBoundary, mock_resolver: DomainResolver
    ) -> None:
        """grid=3x4 must not call resolve()."""
        # Given
        grid = THREE_BY_FOUR_GRID
        # When
        boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert mock_resolver.resolve.call_count == 0

    def test_none_grid_resolve_assert_not_called_mock(
        self, mock_resolver: DomainResolver
    ) -> None:
        """grid=None must keep resolve() uncalled (assert_not_called)."""
        # Given
        boundary = ScreenBoundary(resolver=mock_resolver)
        grid = None
        # When
        boundary.solve(grid)
        # Then
        # AC-FR-01-01
        mock_resolver.resolve.assert_not_called()


class TestAcFr0101MessageIdentity:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — message byte-for-byte identity."""

    def test_none_grid_message_exact_prd_section_8_1(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=None message must match PRD §8.1 exactly."""
        # Given
        grid = None
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert result.message == PRD_SECTION_8_1_MESSAGE
        assert result.message == "Grid must be 4x4."

    def test_empty_list_grid_message_exact_prd_section_8_1(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=[] message must match PRD §8.1 exactly."""
        # Given
        grid: list[list[int]] = []
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert result.message == PRD_SECTION_8_1_MESSAGE

    def test_three_by_four_grid_message_exact_prd_section_8_1(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=3x4 message must match PRD §8.1 exactly."""
        # Given
        grid = THREE_BY_FOUR_GRID
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert result.message == PRD_SECTION_8_1_MESSAGE

    def test_four_empty_row_lists_message_exact_prd_section_8_1(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=[[]]*4 message must match PRD §8.1 exactly."""
        # Given
        grid = FOUR_EMPTY_ROW_LISTS
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert result.message == PRD_SECTION_8_1_MESSAGE

    def test_none_grid_message_length_matches_prd_literal(
        self, boundary: ScreenBoundary
    ) -> None:
        """grid=None message length must equal PRD literal (no truncation)."""
        # Given
        grid = None
        expected = "Grid must be 4x4."
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert len(result.message) == len(expected)
        assert result.message == expected


class TestAcFr0101ScopeLimit:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — scope excludes AC-FR-01-02~05 / FR-02~05."""

    def test_scope_param_grids_exclude_valid_four_by_four(self) -> None:
        """AC-FR-01-01 parametrized inputs must not include valid 4x4 grids."""
        # Given
        valid_4x4 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
        # When / Then
        # AC-FR-01-01
        assert valid_4x4 not in AC_FR_01_01_PARAM_GRIDS

    def test_scope_param_grids_exclude_wrong_empty_count(self) -> None:
        """AC-FR-01-01 must not include AC-FR-01-03 empty-count cases."""
        # Given
        one_empty = FORBIDDEN_AC_FR_01_02_05_GRIDS[0]
        # When / Then
        # AC-FR-01-01
        assert one_empty not in AC_FR_01_01_PARAM_GRIDS

    def test_scope_param_grids_exclude_value_range_violation(self) -> None:
        """AC-FR-01-01 must not include AC-FR-01-04 value-range cases."""
        # Given
        out_of_range = FORBIDDEN_AC_FR_01_02_05_GRIDS[1]
        # When / Then
        # AC-FR-01-01
        assert out_of_range not in AC_FR_01_01_PARAM_GRIDS

    def test_scope_param_grids_exclude_duplicate_values(self) -> None:
        """AC-FR-01-01 must not include AC-FR-01-05 duplicate cases."""
        # Given
        duplicate = FORBIDDEN_AC_FR_01_02_05_GRIDS[2]
        # When / Then
        # AC-FR-01-01
        assert duplicate not in AC_FR_01_01_PARAM_GRIDS

    def test_scope_contract_code_is_only_invalid_size_constant(self) -> None:
        """AC-FR-01-01 RED scope uses INVALID_SIZE only (not ERR_EMPTY_COUNT)."""
        # Given
        forbidden_codes = {
            "ERR_EMPTY_COUNT",
            "ERR_VALUE_RANGE",
            "ERR_DUPLICATE",
            "ERR_GRID_COLS",
            "ERR_NO_SOLUTION",
        }
        # When / Then
        # AC-FR-01-01
        assert AC_FR_01_01_CODE == "INVALID_SIZE"
        assert AC_FR_01_01_CODE not in forbidden_codes


@pytest.mark.parametrize("grid", AC_FR_01_01_PARAM_GRIDS)
class TestAcFr0101ParametrizedContract:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — parametrized contract checks."""

    def test_param_grid_returns_failure_invalid_size_code(
        self, boundary: ScreenBoundary, grid: Any
    ) -> None:
        """Each in-scope invalid grid must return INVALID_SIZE."""
        # Given — grid from parametrize
        # When
        result = boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert result.code == AC_FR_01_01_CODE

    def test_param_grid_resolve_zero_calls(
        self, boundary: ScreenBoundary, mock_resolver: DomainResolver, grid: Any
    ) -> None:
        """Each in-scope invalid grid must not invoke resolve()."""
        # Given — grid from parametrize
        # When
        boundary.solve(grid)
        # Then
        # AC-FR-01-01
        assert mock_resolver.resolve.call_count == 0
