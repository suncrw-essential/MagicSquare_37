"""GM-2 Golden Master regression tests for Magic Square Solver."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
GOLDEN_MASTER_DIR = Path(__file__).resolve().parent
if str(GOLDEN_MASTER_DIR) not in sys.path:
    sys.path.insert(0, str(GOLDEN_MASTER_DIR))

from approve import DEFAULT_EXPECTED_PATH, approve_scenario
from contract import assert_error_contract, assert_success_contract
from magic_square.boundary.errors import FailureResult
from magic_square.boundary.screen_boundary import ScreenBoundary
from magic_square.entity.puzzle_resolver import PuzzleDomainResolver
from scenarios import SCENARIO_BY_TEST_ID, GoldenMasterScenario

pytestmark = pytest.mark.golden_master


@pytest.fixture(scope="module")
def boundary() -> ScreenBoundary:
    """Production ScreenBoundary wired to the real domain resolver."""
    return ScreenBoundary(resolver=PuzzleDomainResolver())


@pytest.fixture(scope="module")
def expected_path() -> Path:
    """Committed golden master baseline path."""
    return DEFAULT_EXPECTED_PATH


def _run_golden_master_case(
    scenario: GoldenMasterScenario,
    boundary: ScreenBoundary,
    expected_path: Path,
) -> None:
    """Execute approve comparison plus output-contract assertions."""
    approve_scenario(scenario, expected_path=expected_path, boundary=boundary, auto_create=False)
    result = boundary.solve(scenario.grid)
    if scenario.kind == "success":
        assert isinstance(result, list)
        assert scenario.placement is not None
        assert_success_contract(scenario.grid, result, placement=scenario.placement)
        return
    assert scenario.error_code is not None
    assert isinstance(result, FailureResult)
    assert_error_contract(result, scenario.error_code)


class TestGoldenMasterMagicSquare:
    """GM-2 — per-scenario golden master regression with contract checks."""

    def test_gm_tc_01_normal_success(
        self,
        boundary: ScreenBoundary,
        expected_path: Path,
    ) -> None:
        """GM-TC-01: small-first placement succeeds and matches baseline."""
        _run_golden_master_case(SCENARIO_BY_TEST_ID["GM-TC-01"], boundary, expected_path)

    def test_gm_tc_02_reverse_success(
        self,
        boundary: ScreenBoundary,
        expected_path: Path,
    ) -> None:
        """GM-TC-02: reverse fallback succeeds and matches baseline."""
        _run_golden_master_case(SCENARIO_BY_TEST_ID["GM-TC-02"], boundary, expected_path)

    def test_gm_tc_03_invalid_blank_count(
        self,
        boundary: ScreenBoundary,
        expected_path: Path,
    ) -> None:
        """GM-TC-03: invalid blank count returns ERR_EMPTY_COUNT."""
        _run_golden_master_case(SCENARIO_BY_TEST_ID["GM-TC-03"], boundary, expected_path)

    def test_gm_tc_04_duplicate_number(
        self,
        boundary: ScreenBoundary,
        expected_path: Path,
    ) -> None:
        """GM-TC-04: duplicate non-zero values return ERR_DUPLICATE."""
        _run_golden_master_case(SCENARIO_BY_TEST_ID["GM-TC-04"], boundary, expected_path)

    def test_gm_tc_05_no_valid_magic_square(
        self,
        boundary: ScreenBoundary,
        expected_path: Path,
    ) -> None:
        """GM-TC-05: unsolvable grid returns ERR_NO_SOLUTION."""
        _run_golden_master_case(SCENARIO_BY_TEST_ID["GM-TC-05"], boundary, expected_path)
