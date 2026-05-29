"""Domain resolver protocol."""

from __future__ import annotations

from typing import Protocol


class DomainResolver(Protocol):
    """Domain puzzle resolution entry point."""

    def resolve(self, grid: object) -> object:
        """Resolve a valid 4x4 grid into a placement result."""
        ...
