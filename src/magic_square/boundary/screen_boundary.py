"""Screen boundary — external solve entry point (RED stub)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from magic_square.boundary.errors import FailureResult

if TYPE_CHECKING:
    from magic_square.entity.resolver import DomainResolver


class ScreenBoundary:
    """Boundary facade for puzzle solve requests.

    RED stub: intentionally wrong behavior until GREEN implementation.
    """

    def __init__(self, resolver: DomainResolver) -> None:
        self._resolver = resolver

    def solve(self, grid: object) -> FailureResult:
        """Validate input and delegate to domain resolver when valid.

        RED: always invokes resolver and returns non-contract failure.
        """
        self._resolver.resolve(grid)
        return FailureResult(code="STUB", message="not implemented")
