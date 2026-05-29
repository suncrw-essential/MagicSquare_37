"""Shared fixtures for Boundary Track A tests."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import create_autospec

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from magic_square.boundary.screen_boundary import ScreenBoundary
from magic_square.entity.resolver import DomainResolver


@pytest.fixture
def mock_resolver() -> DomainResolver:
    """Autospec domain resolver for spy/mock isolation tests."""
    return create_autospec(DomainResolver, instance=True)


@pytest.fixture
def boundary(mock_resolver: DomainResolver) -> ScreenBoundary:
    """ScreenBoundary wired with a mock domain resolver."""
    return ScreenBoundary(resolver=mock_resolver)
