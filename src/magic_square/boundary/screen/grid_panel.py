"""4x4 grid input widgets for the Magic Square screen."""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QGridLayout,
    QLabel,
    QSizePolicy,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from magic_square.boundary.invalid_size import GRID_SIZE

EMPTY_CELL_VALUE = 0
MIN_OCCUPIED_VALUE = 1
MAX_OCCUPIED_VALUE = 16


class GridInputPanel(QWidget):
    """Editable GRID_SIZE x GRID_SIZE integer grid (0 = empty cell)."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._cells: list[list[QSpinBox]] = []
        self._build_ui()

    def _build_ui(self) -> None:
        """Lay out column headers and spin boxes."""
        outer = QVBoxLayout(self)
        grid = QGridLayout()
        grid.setHorizontalSpacing(8)
        grid.setVerticalSpacing(8)

        corner = QLabel("")
        corner.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(corner, 0, 0)

        for col in range(GRID_SIZE):
            header = QLabel(str(col + 1))
            header.setAlignment(Qt.AlignmentFlag.AlignCenter)
            header.setStyleSheet("font-weight: bold;")
            grid.addWidget(header, 0, col + 1)

        for row in range(GRID_SIZE):
            row_label = QLabel(str(row + 1))
            row_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            row_label.setStyleSheet("font-weight: bold;")
            grid.addWidget(row_label, row + 1, 0)

            row_cells: list[QSpinBox] = []
            for col in range(GRID_SIZE):
                spin = QSpinBox(self)
                spin.setRange(EMPTY_CELL_VALUE, MAX_OCCUPIED_VALUE)
                spin.setSpecialValueText("·")
                spin.setAlignment(Qt.AlignmentFlag.AlignCenter)
                spin.setSizePolicy(
                    QSizePolicy.Policy.Expanding,
                    QSizePolicy.Policy.Fixed,
                )
                spin.setMinimumWidth(52)
                grid.addWidget(spin, row + 1, col + 1)
                row_cells.append(spin)
            self._cells.append(row_cells)

        outer.addLayout(grid)

    def get_grid(self) -> list[list[int]]:
        """Return the current grid as nested lists."""
        return [[cell.value() for cell in row] for row in self._cells]

    def set_grid(self, grid: list[list[int]]) -> None:
        """Populate spin boxes from a GRID_SIZE x GRID_SIZE grid."""
        for row_idx in range(GRID_SIZE):
            for col_idx in range(GRID_SIZE):
                self._cells[row_idx][col_idx].setValue(grid[row_idx][col_idx])

    def clear_grid(self) -> None:
        """Reset every cell to empty (0)."""
        for row in self._cells:
            for cell in row:
                cell.setValue(EMPTY_CELL_VALUE)
