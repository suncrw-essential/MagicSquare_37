#!/usr/bin/env python
"""Generate or refresh tests/golden_master_expected.txt from solver output."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
GOLDEN_MASTER_DIR = PROJECT_ROOT / "tests" / "golden_master"
if str(GOLDEN_MASTER_DIR) not in sys.path:
    sys.path.insert(0, str(GOLDEN_MASTER_DIR))

from approve import DEFAULT_EXPECTED_PATH, write_expected_file


def main() -> int:
    """Write the GM-1 golden master baseline from current solver output."""
    content = write_expected_file(DEFAULT_EXPECTED_PATH)
    print(f"Wrote {DEFAULT_EXPECTED_PATH} ({len(content)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
