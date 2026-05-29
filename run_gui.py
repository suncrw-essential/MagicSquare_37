"""Launch the Magic Square GUI from the project root without editable install."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_SRC = _ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from magic_square.boundary.screen.app import main

if __name__ == "__main__":
    raise SystemExit(main())
