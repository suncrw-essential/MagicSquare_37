"""Screen boundary — external solve entry point (RED stub)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from magic_square.boundary.duplicate import (
    ERR_DUPLICATE_CODE,
    ERR_DUPLICATE_MESSAGE,
)
from magic_square.boundary.empty_count import (
    ERR_EMPTY_COUNT_CODE,
    ERR_EMPTY_COUNT_MESSAGE,
)
from magic_square.boundary.errors import FailureResult
from magic_square.boundary.invalid_size import (
    GRID_SIZE,
    INVALID_SIZE_CODE,
    INVALID_SIZE_MESSAGE,
)
from magic_square.boundary.no_solution import NO_SOLUTION_CODE, NO_SOLUTION_MESSAGE
from magic_square.entity.constants import EMPTY_CELL, REQUIRED_EMPTY_COUNT
from magic_square.entity.exceptions import NoValidPlacementError

if TYPE_CHECKING:
    from magic_square.entity.resolver import DomainResolver


class ScreenBoundary:
    """Boundary facade for puzzle solve requests."""

    def __init__(self, resolver: DomainResolver) -> None:
        self._resolver = resolver

    def solve(self, grid: object) -> FailureResult | list[int]:
        """Validate input and delegate to domain resolver when valid."""
        if grid is None or grid == [] or grid == [[]] * GRID_SIZE:
            return FailureResult(
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
            )
        if isinstance(grid, list) and len(grid) != GRID_SIZE:
            return FailureResult(
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
            )
        if isinstance(grid, list):
            empty_count = sum(
                cell == EMPTY_CELL for row in grid for cell in row
            )
            if empty_count != REQUIRED_EMPTY_COUNT:
                return FailureResult(
                    code=ERR_EMPTY_COUNT_CODE,
                    message=ERR_EMPTY_COUNT_MESSAGE,
                )
            nonzero = [cell for row in grid for cell in row if cell != EMPTY_CELL]
            if len(nonzero) != len(set(nonzero)):
                return FailureResult(
                    code=ERR_DUPLICATE_CODE,
                    message=ERR_DUPLICATE_MESSAGE,
                )
        try:
            result = self._resolver.resolve(grid)
        except NoValidPlacementError:
            return FailureResult(
                code=NO_SOLUTION_CODE,
                message=NO_SOLUTION_MESSAGE,
            )
        if isinstance(result, list) and len(result) == 6:
            return result
        return FailureResult(code="STUB", message="not implemented")
