"""Boundary failure result types."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class FailureResult(BaseModel):
    """Standard failure response for Boundary contract violations."""

    model_config = ConfigDict(frozen=True)

    code: str
    message: str
