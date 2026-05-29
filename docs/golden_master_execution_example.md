# GM-2 Golden Master — Execution Example

## Run command

```bash
pytest -m golden_master -v
```

## Passing output (2026-05-29)

```text
============================= test session starts =============================
platform win32 -- Python 3.13.13, pytest-8.4.2, pluggy-1.6.0
cachedir: .pytest_cache
rootdir: C:\dev\MagicSquare_37
configfile: pyproject.toml
collecting ... collected 67 items / 62 deselected / 5 selected

tests/golden_master/test_golden_master_magic_square.py::TestGoldenMasterMagicSquare::test_gm_tc_01_normal_success PASSED [ 20%]
tests/golden_master/test_golden_master_magic_square.py::TestGoldenMasterMagicSquare::test_gm_tc_02_reverse_success PASSED [ 40%]
tests/golden_master/test_golden_master_magic_square.py::TestGoldenMasterMagicSquare::test_gm_tc_03_invalid_blank_count PASSED [ 60%]
tests/golden_master/test_golden_master_magic_square.py::TestGoldenMasterMagicSquare::test_gm_tc_04_duplicate_number PASSED [ 80%]
tests/golden_master/test_golden_master_magic_square.py::TestGoldenMasterMagicSquare::test_gm_tc_05_no_valid_magic_square PASSED [100%]

====================== 5 passed, 62 deselected in 0.17s =======================
```

## Failure diff example

When solver output drifts from `tests/golden_master_expected.txt`, pytest fails with a
unified diff in this shape:

```text
E       Golden master mismatch for GM-TC-01 [normal_success]. Re-run scripts/generate_golden_master.py after reviewing the diff:
E       --- expected
E       +++ actual
E       @@ -4,4 +4,4 @@
E        9 6 7 12
E        4 15 0 1
E        Output:
E       -[2, 4, 8, 4, 3, 14]
E       +[2, 4, 8, 4, 3, 99]
```

## Refresh baseline

```bash
python scripts/generate_golden_master.py
git add tests/golden_master_expected.txt
```
