"""Concrete domain resolver wiring FR-02~FR-05 solver."""

from __future__ import annotations

from magic_square.entity.two_blank_solver import solve_two_blanks


class PuzzleDomainResolver:
    """Domain resolver that delegates to the two-blank solver."""

    def resolve(self, grid: object) -> list[int]:
        """Resolve a validated grid into a six-int placement tuple.

        Args:
            grid: ``list[list[int]]`` puzzle input.

        Returns:
            Placement result ``[r1, c1, n1, r2, c2, n2]``.
        """
        if not isinstance(grid, list):
            msg = "grid must be a list"
            raise TypeError(msg)
        return solve_two_blanks(grid)
