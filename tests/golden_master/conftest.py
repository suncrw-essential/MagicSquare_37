"""Shared pytest configuration for Golden Master tests."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
BOUNDARY_TEST_DIR = PROJECT_ROOT / "tests" / "boundary"
GOLDEN_MASTER_DIR = Path(__file__).resolve().parent

for path in (SRC_PATH, BOUNDARY_TEST_DIR, GOLDEN_MASTER_DIR):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))
