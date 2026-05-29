"""Main window for the Magic Square PyQt application."""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from magic_square.boundary.errors import FailureResult
from magic_square.boundary.invalid_size import INVALID_SIZE_CODE
from magic_square.boundary.screen.grid_panel import GridInputPanel
from magic_square.boundary.screen.sample_grid import DT_002_SAMPLE_GRID
from magic_square.boundary.screen_boundary import ScreenBoundary
from magic_square.entity.puzzle_resolver import PuzzleDomainResolver


class MagicSquareMainWindow(QMainWindow):
    """Primary UI: 4x4 grid input, solve action, contract result display."""

    def __init__(self, boundary: ScreenBoundary | None = None) -> None:
        super().__init__()
        self._boundary = boundary or ScreenBoundary(resolver=PuzzleDomainResolver())
        self._grid_panel = GridInputPanel(self)
        self._result_label = QLabel("Enter a 4×4 grid and press Solve.")
        self._code_label = QLabel("")
        self._build_ui()

    def _build_ui(self) -> None:
        """Compose layout, controls, and signal wiring."""
        self.setWindowTitle("Magic Square 4×4")
        self.setMinimumSize(480, 520)

        central = QWidget(self)
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(16)

        title = QLabel("Magic Square Solver")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)

        hint = QLabel(
            "Values: 0 = empty cell, 1–16 = filled. "
            "Exactly two empty cells are required for a valid puzzle."
        )
        hint.setWordWrap(True)
        hint.setStyleSheet("color: #555;")
        layout.addWidget(hint)

        layout.addWidget(self._grid_panel)

        button_row = QHBoxLayout()
        solve_btn = QPushButton("Solve")
        solve_btn.setDefault(True)
        solve_btn.clicked.connect(self._on_solve)
        button_row.addWidget(solve_btn)

        sample_btn = QPushButton("Load Sample")
        sample_btn.clicked.connect(self._on_load_sample)
        button_row.addWidget(sample_btn)

        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self._on_clear)
        button_row.addWidget(clear_btn)

        button_row.addStretch()
        layout.addLayout(button_row)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(separator)

        result_title = QLabel("Result")
        result_title.setStyleSheet("font-weight: bold;")
        layout.addWidget(result_title)

        self._code_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        layout.addWidget(self._code_label)

        self._result_label.setWordWrap(True)
        self._result_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        layout.addWidget(self._result_label)
        layout.addStretch()

    def _on_solve(self) -> None:
        """Collect grid input and delegate to ScreenBoundary.solve()."""
        grid = self._grid_panel.get_grid()
        result = self._boundary.solve(grid)
        self._show_result(result)

    def _on_load_sample(self) -> None:
        """Load the DT-002 reference grid from design documentation."""
        self._grid_panel.set_grid(DT_002_SAMPLE_GRID)
        self._code_label.setText("")
        self._result_label.setText("Sample grid loaded. Press Solve to run validation.")

    def _on_clear(self) -> None:
        """Reset the grid and result panel."""
        self._grid_panel.clear_grid()
        self._code_label.setText("")
        self._result_label.setText("Grid cleared.")

    def _show_result(self, result: FailureResult | list[int]) -> None:
        """Render a Boundary contract result in the result panel."""
        if isinstance(result, list):
            self._code_label.setText("Status: SUCCESS")
            self._result_label.setStyleSheet("color: #1b5e20;")
            row1, col1, num1, row2, col2, num2 = result
            self._result_label.setText(
                f"Placement: ({row1},{col1})={num1}, ({row2},{col2})={num2}\n"
                f"int[6]: {result}"
            )
            return

        self._code_label.setText(f"Code: {result.code}")

        if result.code == INVALID_SIZE_CODE:
            self._result_label.setStyleSheet("color: #b00020;")
            self._result_label.setText(result.message)
            return

        self._result_label.setStyleSheet("color: #b00020;")
        self._result_label.setText(result.message)
