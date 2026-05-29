"""Domain-level exceptions."""

from __future__ import annotations


class NoValidPlacementError(Exception):
    """Raised when neither placement attempt produces a valid magic square."""
