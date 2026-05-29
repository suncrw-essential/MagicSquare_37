"""Golden Master approve-pattern helpers (GM-1 / GM-2)."""

from __future__ import annotations

import difflib
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
BOUNDARY_TEST_DIR = PROJECT_ROOT / "tests" / "boundary"
GOLDEN_MASTER_TEST_DIR = Path(__file__).resolve().parent

for path in (SRC_PATH, BOUNDARY_TEST_DIR, GOLDEN_MASTER_TEST_DIR):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from magic_square.boundary.errors import FailureResult
from magic_square.boundary.screen_boundary import ScreenBoundary
from magic_square.entity.puzzle_resolver import PuzzleDomainResolver
from scenarios import GOLDEN_MASTER_SCENARIOS, GoldenMasterScenario

DEFAULT_EXPECTED_PATH = PROJECT_ROOT / "tests" / "golden_master_expected.txt"
SECTION_SEPARATOR = "________________________________________"


def format_grid(grid: list[list[int]]) -> str:
    """Format a 4x4 grid as space-separated rows."""
    return "\n".join(" ".join(str(cell) for cell in row) for row in grid)


def format_solve_result(result: FailureResult | list[int]) -> str:
    """Serialize a Boundary solve result for golden master comparison."""
    if isinstance(result, FailureResult):
        return f"Error:\n{result.code}"
    return f"Output:\n{result}"


def format_scenario_block(
    scenario: GoldenMasterScenario,
    result: FailureResult | list[int],
) -> str:
    """Render one golden master scenario section."""
    lines = [
        f"[{scenario.name}]",
        "Input:",
        format_grid(scenario.grid),
        format_solve_result(result),
        "",
        SECTION_SEPARATOR,
        "",
    ]
    return "\n".join(lines)


def scenario_block_text(
    scenario: GoldenMasterScenario,
    result: FailureResult | list[int],
) -> str:
    """Return the comparable scenario block without the trailing separator."""
    return format_scenario_block(scenario, result).split(SECTION_SEPARATOR, maxsplit=1)[
        0
    ].rstrip()


def extract_scenario_block(document: str, scenario_name: str) -> str | None:
    """Extract one scenario block from the committed golden master document."""
    marker = f"[{scenario_name}]"
    start = document.find(marker)
    if start == -1:
        return None
    rest = document[start + len(marker) :].lstrip("\n")
    separator_at = rest.find(SECTION_SEPARATOR)
    body = rest[:separator_at].rstrip() if separator_at != -1 else rest.rstrip()
    return f"{marker}\n{body}"


def format_unified_diff(expected: str, actual: str, *, label: str) -> str:
    """Render a unified diff for golden master failures."""
    return "\n".join(
        difflib.unified_diff(
            expected.splitlines(),
            actual.splitlines(),
            fromfile="expected",
            tofile="actual",
            lineterm="",
        )
    )


def build_expected_document(boundary: ScreenBoundary | None = None) -> str:
    """Capture current solver output for all golden master scenarios."""
    solver = boundary or ScreenBoundary(resolver=PuzzleDomainResolver())
    blocks = [
        format_scenario_block(scenario, solver.solve(scenario.grid))
        for scenario in GOLDEN_MASTER_SCENARIOS
    ]
    return "".join(blocks).rstrip() + "\n"


def write_expected_file(path: Path, boundary: ScreenBoundary | None = None) -> str:
    """Write the golden master baseline file and return its content."""
    content = build_expected_document(boundary=boundary)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return content


def approve_scenario(
    scenario: GoldenMasterScenario,
    expected_path: Path = DEFAULT_EXPECTED_PATH,
    boundary: ScreenBoundary | None = None,
    *,
    auto_create: bool = True,
) -> str:
    """Compare one scenario block using the approve pattern.

    When ``auto_create`` is True and the baseline file is missing, the full
    document is written from the current solver output.

    Args:
        scenario: Scenario under test.
        expected_path: Path to the committed golden master file.
        boundary: Optional ScreenBoundary override for tests.
        auto_create: Create or refresh the baseline when it is missing.

    Returns:
        The approved scenario block text.

    Raises:
        AssertionError: When actual output differs from the baseline.
    """
    solver = boundary or ScreenBoundary(resolver=PuzzleDomainResolver())
    result = solver.solve(scenario.grid)
    actual_block = scenario_block_text(scenario, result)

    if not expected_path.is_file():
        if not auto_create:
            msg = f"Golden master baseline not found: {expected_path}"
            raise AssertionError(msg)
        write_expected_file(expected_path, boundary=solver)
        return actual_block

    expected_document = expected_path.read_text(encoding="utf-8")
    expected_block = extract_scenario_block(expected_document, scenario.name)
    if expected_block is None:
        if not auto_create:
            msg = f"Scenario [{scenario.name}] missing from {expected_path}"
            raise AssertionError(msg)
        write_expected_file(expected_path, boundary=solver)
        return actual_block

    if actual_block == expected_block:
        return actual_block

    diff = format_unified_diff(expected_block, actual_block, label=scenario.test_id)
    msg = (
        f"Golden master mismatch for {scenario.test_id} [{scenario.name}]. "
        "Re-run scripts/generate_golden_master.py after reviewing the diff:\n"
        f"{diff}"
    )
    raise AssertionError(msg)


def approve(
    expected_path: Path = DEFAULT_EXPECTED_PATH,
    boundary: ScreenBoundary | None = None,
    *,
    auto_create: bool = True,
) -> str:
    """Compare the full golden master document against the solver output."""
    actual = build_expected_document(boundary=boundary)
    if not expected_path.is_file():
        if not auto_create:
            msg = f"Golden master baseline not found: {expected_path}"
            raise AssertionError(msg)
        write_expected_file(expected_path, boundary=boundary)
        return actual

    expected = expected_path.read_text(encoding="utf-8")
    if actual == expected:
        return expected

    diff = format_unified_diff(expected, actual, label="document")
    msg = (
        "Golden master document mismatch. Re-run scripts/generate_golden_master.py "
        "after reviewing the diff:\n"
        f"{diff}"
    )
    raise AssertionError(msg)
