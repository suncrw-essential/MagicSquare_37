"""PyQt application entry point for Magic Square."""

from __future__ import annotations

import sys
from pathlib import Path


def _ensure_src_on_path() -> None:
    """Add ``src`` to ``sys.path`` when launched without installation."""
    src = Path(__file__).resolve().parents[3]
    src_str = str(src)
    if src_str not in sys.path:
        sys.path.insert(0, src_str)


def main() -> int:
    """Start the Magic Square PyQt GUI.

    Returns:
        Process exit code from ``QApplication.exec()``.
    """
    _ensure_src_on_path()

    from PyQt6.QtWidgets import QApplication

    from magic_square.boundary.screen.main_window import MagicSquareMainWindow

    app = QApplication(sys.argv)
    app.setApplicationName("Magic Square 4x4")
    window = MagicSquareMainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
