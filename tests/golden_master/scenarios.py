"""Golden Master scenario definitions (GM-1 / GM-2)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from constants import FORBIDDEN_AC_FR_01_02_05_GRIDS, THREE_EMPTY_CELLS_GRID

NORMAL_SUCCESS_GRID: list[list[int]] = [
    [16, 3, 2, 13],
    [5, 10, 11, 0],
    [9, 6, 7, 12],
    [4, 15, 0, 1],
]

REVERSE_SUCCESS_GRID: list[list[int]] = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 0, 12],
    [4, 14, 15, 0],
]

NO_SOLUTION_GRID: list[list[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 0],
    [12, 13, 14, 0],
]

DUPLICATE_GRID: list[list[int]] = FORBIDDEN_AC_FR_01_02_05_GRIDS[2]

ScenarioKind = Literal["success", "error"]
PlacementKind = Literal["small_first", "reverse"]


@dataclass(frozen=True)
class GoldenMasterScenario:
    """Single Golden Master input scenario."""

    test_id: str
    name: str
    grid: list[list[int]]
    kind: ScenarioKind
    placement: PlacementKind | None = None
    error_code: str | None = None


GOLDEN_MASTER_SCENARIOS: tuple[GoldenMasterScenario, ...] = (
    GoldenMasterScenario(
        "GM-TC-01",
        "normal_success",
        NORMAL_SUCCESS_GRID,
        "success",
        placement="small_first",
    ),
    GoldenMasterScenario(
        "GM-TC-02",
        "reverse_success",
        REVERSE_SUCCESS_GRID,
        "success",
        placement="reverse",
    ),
    GoldenMasterScenario(
        "GM-TC-03",
        "invalid_blank_count",
        THREE_EMPTY_CELLS_GRID,
        "error",
        error_code="ERR_EMPTY_COUNT",
    ),
    GoldenMasterScenario(
        "GM-TC-04",
        "duplicate_number",
        DUPLICATE_GRID,
        "error",
        error_code="ERR_DUPLICATE",
    ),
    GoldenMasterScenario(
        "GM-TC-05",
        "no_valid_solution",
        NO_SOLUTION_GRID,
        "error",
        error_code="ERR_NO_SOLUTION",
    ),
)

SCENARIO_BY_TEST_ID: dict[str, GoldenMasterScenario] = {
    scenario.test_id: scenario for scenario in GOLDEN_MASTER_SCENARIOS
}
