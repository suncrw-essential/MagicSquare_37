"""Placeholder domain resolver for Boundary wiring until domain GREEN."""

from __future__ import annotations


class StubDomainResolver:
    """No-op resolver used by the GUI and integration smoke paths."""

    def resolve(self, grid: object) -> object:
        """Accept a validated grid without performing domain logic."""
        return None
