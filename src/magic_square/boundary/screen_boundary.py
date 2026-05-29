"""Screen boundary — external solve entry point (RED stub)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from magic_square.boundary.errors import FailureResult
from magic_square.boundary.invalid_size import (
    INVALID_SIZE_CODE,
    INVALID_SIZE_MESSAGE,
)

if TYPE_CHECKING:
    from magic_square.entity.resolver import DomainResolver


class ScreenBoundary:
    """Boundary facade for puzzle solve requests.

    RED stub: intentionally wrong behavior until GREEN implementation.
    """

    def __init__(self, resolver: DomainResolver) -> None:
        self._resolver = resolver

    def solve(self, grid: object) -> FailureResult:
        """Validate input and delegate to domain resolver when valid."""
        if grid is None or grid == []:
            return FailureResult(
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
            )
        self._resolver.resolve(grid)
        return FailureResult(code="STUB", message="not implemented")
