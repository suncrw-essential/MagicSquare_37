# Magic Square — Test Plan (AC-01: Row Count Validation)

| Field | Value |
|---|---|
| **Document ID** | TP-AC-01 |
| **Version** | 1.0 |
| **Date** | 2026-05-29 |
| **Author Role** | Senior QA Lead |
| **Primary AC** | AC-01 |
| **Primary FR** | FR-01 Input Verification (§10) |
| **Business Rule** | BR-01 — 입력은 정확히 4행이어야 한다 |
| **Sample Scenario** | `grid = None` → `{ code: "ERR_GRID_ROWS", message: "Grid must have exactly 4 rows." }` |
| **Related PRD** | `docs/PRD_MagicSquare.md`, `Report/02.MagicSquare_DualTrack_CleanArchitecture_Design.md` |
| **Stack** | Python 3.11+, pytest, pydantic, unittest.mock |

---

## 1. Purpose & Scope

본 계획서는 **FR-01 / AC-01(행 수 검증)** 을 중심으로, Boundary 계층의 입력 유효성 검사와 **Domain resolver 미호출** 정책을 pytest 단위 테스트로 고정한다.

### 1.1 In-Scope

| Layer | Component (planned) | Test focus |
|---|---|---|
| **Boundary** | `BoundaryValidator`, `ScreenBoundary.solve` | 행 수 ≠ 4 → `ERR_GRID_ROWS` + 고정 message |
| **Control** | `ApplicationService.solve_puzzle` (orchestrator) | 검증 실패 시 Domain 진입점 미위임 |
| **Entity** | *(mock only in this plan)* | AC-01 범위에서 직접 단위 테스트 없음 |

### 1.2 Out-of-Scope (명시적 제외)

| Item | Reason |
|---|---|
| `grid = 4×4` 정상 입력 | AC-01 범위 외 (FR-02~FR-05, 성공 경로) |
| AC-02~AC-05 상세 매트릭스 | 본 문서는 AC-01 **선행** 검증에 집중; 인접 케이스는 경계값 표에 **참조용**으로만 기재 |
| Integration / E2E | IT-01~IT-06은 후속 계획서 |
| UI 화면, DB, Web/API | PRD §9.2 Out-of-Scope |

---

## 2. Traceability

| Concept | Business Rule | FR | AC | Test Scenario | Component |
|---|---|---|---|---|---|
| 4행 입력 | BR-01 | FR-01 | AC-01 | TS-E-01, TD-03 | BoundaryValidator |
| Domain 미호출 | FR-01 Error Policy | FR-01 | AC-01 | GS-02, §15.1 Track A | ApplicationService |
| Dual-Track | §15 Dual-Track TDD | FR-01 | AC-01 | UT-002 (Design §2.3) | ScreenBoundary |

---

## 3. pytest 단위 테스트 범위 및 우선순위

### 3.1 Test Track 분류

| Track | ID prefix | Directory (planned) | Responsibility |
|---|---|---|---|
| **Track A — Boundary Contract** | `UT-A-` | `tests/boundary/` | IN 계약, 오류 code/message, Domain 미호출 |
| **Track B — Domain Logic** | `DT-B-` | `tests/entity/` | AC-01 범위 **외** (본 계획서 RED 1차 대상 아님) |

### 3.2 우선순위 (RED 순서)

Design §2.3 RED 순서 및 PRD §15.1 Track A 원칙을 따른다.

| Priority | Test ID | Target | Given | Then | Mock |
|---|---|---|---|---|---|
| **P0** | UT-A-01 | AC-01 canonical | `grid = None` | `ERR_GRID_ROWS` + message | Domain resolver **0회** |
| **P0** | UT-A-02 | AC-01 empty rows | `grid = []` | `ERR_GRID_ROWS` + message | Domain resolver **0회** |
| **P1** | UT-A-03 | AC-01 under-rows | `grid = 3×4` | `ERR_GRID_ROWS` + message | Domain resolver **0회** |
| **P1** | UT-A-04 | AC-01 over-rows | `grid = 5×5` | `ERR_GRID_ROWS` + message | Domain resolver **0회** |
| **P2** | UT-A-05 | AC-01 adjacent (참조) | `grid = [[]] * 4` | `ERR_GRID_COLS` *(AC-02)* | Domain resolver **0회** |
| **P2** | UT-A-06 | AC-01 adjacent (참조) | `grid = 4×3` | `ERR_GRID_COLS` *(AC-02)* | Domain resolver **0회** |
| **P3** | UT-A-07 | BoundaryValidator unit | 각 AC-01 입력 | validator 단독 반환값 | N/A (순수 validator) |
| **P3** | UT-A-08 | pydantic schema | `None` / non-list | ValidationError 또는 mapped error | N/A |

> **P0 → P1 → P2 → P3**: P0 RED 확정 후 GREEN. P2는 AC-01과 **동일한 선행 게이트**(Domain 미호출)를 공유하므로 Track A에 포함하되, 기대 code는 AC-02로 명시한다.

### 3.3 Planned Test Files

| File | Tests | Layer under test |
|---|---|---|
| `tests/boundary/test_ac01_grid_rows.py` | UT-A-01 ~ UT-A-04 | BoundaryValidator + ScreenBoundary |
| `tests/boundary/test_ac01_adjacent_size_errors.py` | UT-A-05 ~ UT-A-06 | BoundaryValidator (AC-02 참조) |
| `tests/boundary/test_ac01_domain_isolation.py` | UT-A-01 ~ UT-A-06 (parametrize) | Control orchestration + mock spy |
| `tests/boundary/test_input_schema_pydantic.py` | UT-A-08 | pydantic input model |

### 3.4 AAA Pattern (mandatory)

모든 테스트는 Arrange → Act → Assert 구조를 따른다.

```text
# Arrange   — grid 입력, mock Domain resolver 주입
# Act       — solve(grid) 또는 validate_grid(grid) 호출
# Assert    — code, message, mock.call_count == 0
```

---

## 4. 경계값 케이스 목록

### 4.1 AC-01 Primary Cases (`ERR_GRID_ROWS`)

| Case ID | Input (`grid`) | Row count | Expected `code` | Expected `message` | AC | Include |
|---|---|---:|---|---|---|
| **BV-01** | `None` | N/A (non-iterable) | `ERR_GRID_ROWS` | `Grid must have exactly 4 rows.` | AC-01 | ✅ |
| **BV-02** | `[]` | 0 | `ERR_GRID_ROWS` | `Grid must have exactly 4 rows.` | AC-01 | ✅ |
| **BV-03** | `3×4` (3 rows, each 4 cols) | 3 | `ERR_GRID_ROWS` | `Grid must have exactly 4 rows.` | AC-01 | ✅ |
| **BV-04** | `5×5` (5 rows, each 5 cols) | 5 | `ERR_GRID_ROWS` | `Grid must have exactly 4 rows.` | AC-01 | ✅ |

**3×4 example (BV-03):**

```python
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
```

**5×5 example (BV-04):**

```python
[[1]*5 for _ in range(5)]
```

### 4.2 Adjacent Size Cases (참조 — AC-01 범위 외 code, 동일 선행 게이트)

| Case ID | Input (`grid`) | Failure reason | Expected `code` | Expected AC | Domain call |
|---|---|---|---|---|---|
| **BV-05** | `[[]] * 4` | 4 rows, 0 cols per row | `ERR_GRID_COLS` | AC-02 | 0 |
| **BV-06** | `4×3` | 4 rows, 3 cols | `ERR_GRID_COLS` | AC-02 | 0 |
| **BV-07** | `4×4` valid structure | — | *(success path)* | — | **제외** |

**4×3 example (BV-06):**

```python
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
```

> AC-01 검증 순서: **행 수(BR-01) → 열 수(BR-02)**. BV-05/BV-06은 행 수 통과 후 열 수에서 실패하므로 `ERR_GRID_COLS`가 정답이다.

### 4.3 Explicit Exclusion

| Case ID | Input | Reason for exclusion |
|---|---|---|
| **BV-X-01** | `4×4` 정상 입력 (빈칸 2개 포함) | AC-01 범위 외; FR-02~FR-05 및 성공/후속 AC 테스트 대상 |

---

## 5. 예외 / 특이 케이스 목록

| Case ID | Category | Input / Condition | Expected behavior | Rationale |
|---|---|---|---|---|
| **EX-01** | Null input | `grid = None` | `ERR_GRID_ROWS`; **예외 전파 금지** | PRD §13: 비정의 예외 전파 정책 불허 |
| **EX-02** | Non-list type | `grid = "abcd"`, `grid = 16`, `grid = {}` | `ERR_GRID_ROWS` (또는 pydantic `ValidationError` → mapped `ERR_GRID_ROWS`) | 타입 계약 위반은 행 수 검증 이전/동시 처리 |
| **EX-03** | Nested non-list row | `grid = [1, 2, 3, 4]` (flat list) | `ERR_GRID_ROWS` 또는 schema error → mapped boundary error | `int[4][4]` 형식 위반 |
| **EX-04** | Row is `None` | `grid = [None, [], [], []]` | `ERR_GRID_COLS` *(AC-02)* 또는 schema error | 행 수는 4; 열 접근 불가 |
| **EX-05** | Aliased empty rows | `grid = [[]] * 4` | `ERR_GRID_COLS`; 동일 row 객체 참조여도 결정적 실패 | Python list alias 특성; BR-02 위반 |
| **EX-06** | Early exit | BV-01 ~ BV-04 | AC-02~AC-05 검사 **실행되지 않음** | FR-01: 실패 시 즉시 반환, Domain 미호출 |
| **EX-07** | Message immutability | Any AC-01 failure | message **바이트 단위** Design §2.2 표와 일치 | UX-02, PRD §13 |
| **EX-08** | Side-effect | Any AC-01 failure | 원본 `grid` 객체 **변경 없음** | BR-15 / NFR-04 (입력 무부작용) |

---

## 6. Domain Resolver 진입점 호출 횟수 검증 전략

### 6.1 Domain Entry Point Definition

| Symbol | Layer | Role |
|---|---|---|
| `TwoBlankSolver.solve` | Entity | Domain resolver (primary spy target) |
| `ApplicationService.solve_puzzle` | Control | Orchestrator — validator → (pass) → domain |

ECB 규칙: Boundary → Control → Entity. Boundary 테스트에서 Domain은 **mock**으로 대체한다.

### 6.2 Mock / Spy Pattern

**Primary approach:** `unittest.mock.create_autospec` + `patch` on Control layer dependency.

```python
from unittest.mock import create_autospec, patch

# Arrange
mock_solver = create_autospec(TwoBlankSolver, instance=True)
service = ApplicationService(solver=mock_solver)

# Act
result = service.solve_puzzle(grid=None)

# Assert — contract
assert result.code == "ERR_GRID_ROWS"
assert result.message == "Grid must have exactly 4 rows."

# Assert — isolation
mock_solver.solve.assert_not_called()
assert mock_solver.solve.call_count == 0
```

**Alternative (pytest-mock):**

```python
def test_ac01_none_does_not_invoke_domain(mocker, service):
    spy = mocker.spy(service._solver, "solve")
    service.solve_puzzle(grid=None)
    spy.assert_not_called()
```

### 6.3 Verification Matrix

| Test scope | Mock target | Injection point | Assertion |
|---|---|---|---|
| **Orchestration (recommended)** | `TwoBlankSolver.solve` | `ApplicationService` constructor | `call_count == 0` |
| **Boundary facade** | `ApplicationService.solve_puzzle` | `ScreenBoundary` | `call_count == 0` *(Boundary가 Control 우회 시 실패)* |
| **Pure validator** | N/A | `BoundaryValidator.validate` | Domain mock 불필요; 반환 타입만 검증 |

### 6.4 Anti-patterns (Forbidden)

| Pattern | Why forbidden |
|---|---|
| Domain mock 없이 `solve()` 통합 호출만 검증 | 실패 원인이 AC-01인지 Domain bug인지 분리 불가 |
| `assert not mock_solver.solve.called` 단독 사용 | message/code 미검증 → assertion dilution |
| Boundary → Entity 직접 import 테스트 | ECB §Forbidden: `boundary -> entity` |
| `skip` / `xfail` / weakened `call_count >= 0` | `.cursor/rules/magicsquare-forbidden.mdc` 위반 |

### 6.5 Parametrize Strategy

AC-01 + adjacent cases를 `@pytest.mark.parametrize`로 묶어 **동일 isolation assertion** 재사용:

| param id | grid | expected_code |
|---|---|---|
| `none` | `None` | `ERR_GRID_ROWS` |
| `empty_list` | `[]` | `ERR_GRID_ROWS` |
| `three_by_four` | `3×4 matrix` | `ERR_GRID_ROWS` |
| `five_by_five` | `5×5 matrix` | `ERR_GRID_ROWS` |
| `four_empty_rows` | `[[]]*4` | `ERR_GRID_COLS` |
| `four_by_three` | `4×3 matrix` | `ERR_GRID_COLS` |

각 param에 대해: **`mock_solver.solve.call_count == 0`** 필수.

---

## 7. pydantic 입력 스키마 전략

Boundary 계층에서 `grid: list[list[int]] | None` pydantic model을 사용할 경우:

| Stage | Responsibility | Failure mapping |
|---|---|---|
| **Schema parse** | 타입·nullable 거부 | `ValidationError` → Boundary 표준 `{code, message}` |
| **Semantic validate** | BR-01 row count | `ERR_GRID_ROWS` |
| **Semantic validate** | BR-02 col count | `ERR_GRID_COLS` |

UT-A-08: pydantic 실패가 **미처리 예외로 전파되지 않음**을 검증한다 (EX-01, EX-02).

---

## 8. 커버리지 목표

PRD §14 NFR-01 / NFR-02 및 Design §20 Engineering Principles 기준.

| Layer | Package path (planned) | Target | Measurement focus |
|---|---|---:|---|
| **Entity (Domain)** | `src/magic_square/entity/` | **≥ 95%** | BlankFinder, MissingNumberFinder, MagicSquareValidator, TwoBlankSolver |
| **Boundary** | `src/magic_square/boundary/` | **≥ 85%** | BoundaryValidator, ScreenBoundary, error mapping |
| **Control** | `src/magic_square/control/` | **≥ 85%** *(Boundary track에 포함)* | ApplicationService orchestration, early return paths |
| **Overall project** | `src/` | **≥ 80%** | `.cursor/rules/magicsquare-tdd-testing.mdc` minimum |

### 8.1 AC-01 Phase Coverage Expectations

| Phase | Expected coverage delta |
|---|---|
| P0 RED (UT-A-01, UT-A-02) | BoundaryValidator `validate` row-check branch ≥ 90% |
| P0 GREEN | `ScreenBoundary.solve` early-return path covered |
| P1 (orchestration tests) | ApplicationService validation-fail branch 100% |
| Full FR-01 complete | Boundary package ≥ 85% |

> AC-01 단독 구현만으로 Domain 95% 달성은 불가능하다. Domain coverage는 Track B (DT-B-*) RED 진행 시 누적 달성한다.

---

## 9. pytest-cov 측정 전략

### 9.1 Installation

```bash
pip install pytest pytest-cov pydantic
```

### 9.2 Standard measurement command

```bash
pytest --cov=src --cov-report=term-missing
```

### 9.3 AC-01 focused runs

```bash
# AC-01 boundary tests only
pytest tests/boundary/test_ac01_grid_rows.py tests/boundary/test_ac01_domain_isolation.py \
  --cov=src/magic_square/boundary \
  --cov=src/magic_square/control \
  --cov-report=term-missing \
  --cov-fail-under=85
```

```bash
# Domain package (Track B; full FR-01+ 이후)
pytest tests/entity/ \
  --cov=src/magic_square/entity \
  --cov-report=term-missing \
  --cov-fail-under=95
```

### 9.4 Recommended `.coveragerc` / `pyproject.toml` settings (planned)

| Setting | Value | Purpose |
|---|---|---|
| `source` | `src/magic_square` | 측정 루트 |
| `omit` | `tests/*`, `*/__init__.py` | 테스트·빈 init 제외 |
| `fail_under` | boundary run: 85, entity run: 95 | CI gate |
| `show_missing` | `true` | term-missing 리포트 |

### 9.5 CI gate sequence

1. `pytest tests/boundary/ --cov=src/magic_square/boundary --cov-fail-under=85`
2. `pytest tests/entity/ --cov=src/magic_square/entity --cov-fail-under=95`
3. `pytest --cov=src --cov-report=term-missing` (full report artifact)

### 9.6 Coverage interpretation rules

| Signal | Action |
|---|---|
| BoundaryValidator row-check line missing | UT-A-01 ~ UT-A-04 RED 추가 |
| ApplicationService `solve_puzzle` body partially covered | UT-A isolation tests 보강 |
| Entity covered in AC-01 phase | **Layer violation** — Boundary 테스트가 Domain 실행 중; mock 실패 |

---

## 10. Pass / Fail Criteria

| Criterion | Pass condition |
|---|---|
| **Contract** | BV-01 ~ BV-04 모두 `code == "ERR_GRID_ROWS"`, message 고정 문자열 일치 |
| **Isolation** | BV-01 ~ BV-06 모두 `TwoBlankSolver.solve.call_count == 0` |
| **Exclusion** | BV-X-01 (`4×4` 정상) 테스트 파일 **미포함** |
| **No weakening** | skip/xfail/assertion dilution 없음 |
| **Coverage** | Boundary ≥ 85% (AC-01 phase 후 validator+control early path) |
| **ECB** | Boundary 테스트가 Entity 직접 import하지 않음 |

---

## 11. Test Data Reference

| Data ID | Description | Maps to |
|---|---|---|
| TD-03 | invalid size matrix | BV-03, BV-04, TS-E-01 |
| *(new)* TD-03-NULL | `grid = None` | BV-01, UT-A-01 |
| *(new)* TD-03-EMPTY | `grid = []` | BV-02, UT-A-02 |

---

## 12. Appendix — Error Contract (fixed)

| code | message |
|---|---|
| `ERR_GRID_ROWS` | `Grid must have exactly 4 rows.` |
| `ERR_GRID_COLS` | `Each row must have exactly 4 columns.` |

Source: `docs/PRD_MagicSquare.md` §13, `Report/02` §2.2 Error schema.

---

## 13. Revision History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-05-29 | Initial AC-01 focused test plan |
