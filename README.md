# MagicSquare_37

4×4 마방진(Magic Square)을 다루는 학습·실습 프로젝트입니다.  
현재 단계는 **Dual-Track TDD · Clean Architecture** — 설계 완료 후 **Entity·Boundary·Golden Master 구현·테스트 진행 중** (AC-FR-01-01 GREEN 일부, FR-05 success path).

---

## 프로젝트 목적

| 구분 | 내용 |
|------|------|
| **표면 목표** | “4×4 마방진을 만드는 프로그램” |
| **실제 목표** | 4×4 격자(1~16 각 1회)가 **행·열·두 대각선의 합이 모두 같은지** 명시된 기준으로 **일관되게 판정**하고, 그 과정을 **반복·분해·실패 가시화**할 수 있는 환경을 정의하는 것 |
| **훈련 초점** | 제약 분해, 판정/생성 분리, 불변식 사고, 요구 정밀화, **TDD로 판정 계약을 구현 전에 고정** |

한 줄로 말하면, **“정답 격자 하나”보다 “무엇이 맞는지 말할 수 있는가”**를 먼저 정하는 프로젝트입니다.

---

## 도메인 요약

- **격자:** 4×4
- **값:** 1부터 16까지, 각각 정확히 한 번
- **조건:** 모든 행·열·주대각선·부대각선의 합이 동일 (이 경우 **34**)
- **주의:** “몇 줄만 합이 34”는 **부분 만족**이며, 전체 조건 만족과 구분해야 함

---

## 문제 정의 워크플로 (STEP 1 ~ 5)

| STEP | 주제 | 핵심 |
|------|------|------|
| **1** | Observation (관찰) | 무엇을 다루는 상황인지, 학습·설계 맥락, “만든다” 대신 **상황**으로 서술 |
| **2** | Why #1 | 왜 완성/증명이 필요한가 — 제약 이해, 부분 성공 vs 전체, 검증·생성 혼동 |
| **3** | Why #2 | 왜 프로그램인가 — 반복 가능성, 검증 자동화, 오류 방지, 규칙 기반 사고 |
| **4** | Why #3 (TDD) | 왜 TDD인가 — 통제 대상, 불변 조건, 입출력 명확성, **계약 우선** |
| **5** | 진짜 문제 정의 | 표면 vs 개선 정의, Invariant, 훈련하려는 사고 능력 |

### Why 체인

```
Why #1  조건을 증명해야 한다
   ↓
Why #2  같은 검증을 반복·자동화해야 한다
   ↓
Why #3  그 검증을 구현 전에 예시(계약)로 고정한다 (TDD)
```

---

## 핵심 Invariant

### 도메인

| ID | 내용 |
|----|------|
| **I1** | 1~16이 각각 정확히 한 번 |
| **I2** | 모든 행·열·두 대각선의 합이 동일 (= 34) |
| **I3** | 한 칸 변경이 여러 방향 합에 동시 영향 (전역 연동) |

### 판정·계약

| ID | 내용 |
|----|------|
| **I4** | “맞다”는 I1·I2에 해당하는 **모든** 검사 통과 후에만 |
| **I5** | 같은 배치 → 같은 판정 (결정성) |
| **T1~T4** | 예시당 명확한 기대 결과, 정답/반례 설계, 생성·UI와 검증 계약 분리 |

---

## 개선된 문제 정의 (STEP 5)

> 4×4 격자에 1부터 16까지 각각 한 번씩 배치된 상태가 주어졌을 때, 행·열·두 대각선의 합이 모두 같고 숫자 사용 규칙을 모두 만족하는지를 명시된 기준으로 판정하고, 그 판정을 동일한 절차로 반복할 수 있게 한다. 필요 시, 배치를 만드는 시도와 판정을 분리하고, 어떤 조건이 깨졌는지까지 드러내는 학습·검증 환경을 만든다.

---

## 입출력 계약 (설계 확정)

| 구분 | 규칙 |
|------|------|
| **입력** | `int[4][4]`, `0`=빈칸 **정확히 2개**, 값은 `0` 또는 `1~16`, 0 제외 중복 금지 |
| **출력** | `int[6]` = `[r1,c1,n1,r2,c2,n2]` (1-index), 누락 두 수의 배치 순서는 OUT-04 규칙 |

상세: [Report/02.MagicSquare_DualTrack_CleanArchitecture_Design.md](Report/02.MagicSquare_DualTrack_CleanArchitecture_Design.md)

## 아직 결정하지 않은 것

- **계약 SSOT (OI-01):** **확정** — `INVALID_SIZE`/`ERR_*` 유지, `E001~E007`는 설계 별칭만 ([Report/14](Report/14.MagicSquare_REFACTOR_Program_Report.md) §3)
- **Control 레이어 명칭:** `ApplicationService` vs `SolvePartialMagicSquare` (Report/09·`docs/test_plan.md`)

---

## 저장소 구조

```
MagicSquare_37/
├── README.md
├── docs/          # test_plan.md, PRD
├── src/magic_square/
│   ├── entity/    # domain (FR-02~05)
│   └── boundary/  # ScreenBoundary, PyQt UI
├── tests/         # boundary, entity, golden_master
├── Report/
└── Prompt/
```

| 경로 | 설명 |
|------|------|
| [Report/01.MagicSquare_ProblemDefinition_Report.md](Report/01.MagicSquare_ProblemDefinition_Report.md) | STEP 1~5 문제 정의 |
| [Report/02.MagicSquare_DualTrack_CleanArchitecture_Design.md](Report/02.MagicSquare_DualTrack_CleanArchitecture_Design.md) | Dual-Track · Clean Architecture 설계 (공식) |
| [Prompt/02.MagicSquare_DualTrack_CleanArchitecture_Transcript.md](Prompt/02.MagicSquare_DualTrack_CleanArchitecture_Transcript.md) | TDD/설계 세션 대화 Export |
| [Prompting/01.MagicSquare_ProblemDefinition_Reportt.md](Prompting/01.MagicSquare_ProblemDefinition_Reportt.md) | 문제 정의 세션 대화 Export |

---

## 현재 상태

| 항목 | 상태 |
|------|------|
| 문제 인식 (STEP 1) | 완료 |
| Why 분석 (STEP 2~4) | 완료 |
| 진짜 문제 정의 (STEP 5) | 완료 |
| Dual-Track · Clean Architecture 설계 | 완료 |
| 입출력 규약 (2-빈칸 솔버) | 완료 |
| AC-FR-01-01 RED 테스트 (`test_ac_fr_01_01_invalid_size.py`) | 완료 (33건) |
| AC-FR-01-01 GREEN (G1~G4, 33/33) | 완료 — [GREEN To-Do](#green-단계-to-do-리스트) |
| AC-FR-01-03 empty count / FR-05 success / Golden Master | 완료 |
| Entity FR-02~05 (validator, two-blank solver) | 완료 |
| REFACTOR Phase 0 Tier 1 | **충족** — [Report/14](Report/14.MagicSquare_REFACTOR_Program_Report.md) §2 |
| `tests/control/` RED (D-SOL, C3 전) | **작성** — Tier 1에서 `--ignore=tests/control` |
| `control/` 구현 | 미착수 (Wave 1 C3~C4) |
| 코드 리뷰 카테고리 A (잔여) | 미착수 — 비-list·열/값·STUB→`ERR_INTERNAL_CONTRACT` |

---

## 코드 리뷰 To-Do

> 출처: code-reviewer (2026-05-29).  
> **REFACTOR 프로그램:** [Report/14.MagicSquare_REFACTOR_Program_Report.md](Report/14.MagicSquare_REFACTOR_Program_Report.md) (Phase 0 · OI-01 · Wave 1 매핑).  
> **ECB 분석:** [Report/13.MagicSquare_ECB_Refactoring_Plan_Report.md](Report/13.MagicSquare_ECB_Refactoring_Plan_Report.md).  
> 규칙: `.cursor/rules/magicsquare-tdd-testing.mdc` §REFACTOR, `magicsquare-ecb-architecture.mdc`, `docs/test_plan.md` §6·§8.

### REFACTOR Phase 0 (게이트 — Report/14 §2)

| Tier | 용도 | 명령 | 상태 |
|------|------|------|------|
| **Tier 1** | Wave 1 C1~C2 (내부 구조, 계약 문자열 불변) | `python -m pytest tests/ --ignore=tests/control -q` + `python -m pytest tests/golden_master/ -q` | **충족** |
| **Tier 2** | Wave 1 C3~C4 · `control/` GREEN · 카테고리 A 잔여 | `python -m pytest tests/ -q` (control 포함) + README A·D | **미충족** |

> **고정:** “pytest+GM”만으로 전체 Phase 0 완료로 보지 않음. **Tier 1 → C1~C2**, **Tier 1+2 → C3~C4**.  
> `tests/control/`는 RED(C3 전)이므로 Tier 1에서 **반드시 `--ignore=tests/control`**.

### REFACTOR 카테고리 (4분류)

| 카테고리 | 이름 | 한 줄 | 우선순위 |
|----------|------|-------|----------|
| **A** | 계약·검증 | Boundary가 무엇을 거부·반환하는가 | P0 → P1 |
| **B** | ECB·책임 분리 | 누가 orchestration 하는가 (Control vs Entity) | P0~P1 |
| **C** | 조립·UI 경계 | Screen이 누구를 생성·주입하는가 | P1 → P2 |
| **D** | 테스트·REFACTOR 게이트 | 옮긴 뒤에도 행위가 같은가 | P0~P2 |

**권장 실행 순서:** `A` + `D`(선행 GREEN) → `B` → `C` → `D`(전체 게이트)

### A — 계약·검증

- [ ] **비-list 입력 가드** — `ScreenBoundary.solve()`: `grid`가 `list`가 아니면 `FailureResult` 반환 (`None`/`[]` 제외한 `"abcd"`, `{}`, `16` 등). PRD §13 예외 전파 금지.
- [ ] **열 수 검증 (IN-01 / AC-02)** — 각 행 `len(row) == 4` → `ERR_GRID_COLS` + 고정 message (`docs/test_plan.md` UT-A-05/06).
- [ ] **값 범위 검증 (IN-04 / AC-04)** — 셀 ∈ `{0} ∪ [1,16]` → `ERR_VALUE_RANGE`; `tests/boundary/test_ac_fr_01_04_*` 추가.
- [ ] **Domain 전제 위반 매핑** — `TypeError` / `IndexError` 등을 Boundary `FailureResult`로 변환 (uncaught exception 방지).
- [x] **계약 SSOT (OI-01)** — [Report/14 §3](Report/14.MagicSquare_REFACTOR_Program_Report.md): `INVALID_SIZE`/`ERR_*` 유지, `E001~E007` 별칭만 (Wave 1 rename 금지).
- [ ] **`STUB` 제거** — `screen_boundary.py` OUT 검증 실패 시 `ERR_INTERNAL_CONTRACT`(또는 DN-03 확정값)으로 매핑.

### B — ECB·책임 분리

- [ ] **`input_validator` 추출** — `screen_boundary.solve()` 인라인 검증 → 전용 클래스/모듈 (Extract Class).
- [ ] **ECB: `control/` 도입** — `SolvePartialMagicSquare` / `ApplicationService.solve_puzzle`; `boundary → control → entity` (직접 `entity` import 금지).
- [ ] **오케스트레이션 이동** — `two_blank_solver` / `puzzle_resolver`의 Step A/B·위임 → `control/solve_partial_magic_square.py`; 순수 배치는 `entity/services/two_cell_solver.py`.
- [ ] **`screen_boundary` → `ui_boundary`** — Boundary facade·rename; 검증·위임·OUT 매핑 역할 분리.

### C — 조립·UI 경계

- [ ] **`main_window.py` DI** — `PuzzleDomainResolver` 직접 생성 제거; injected `ScreenBoundary`(또는 `ui_boundary`)만 사용.
- [ ] **도메인 상수 SSOT** — `boundary/invalid_size.py`, `grid_panel.py`의 `GRID_SIZE`/`EMPTY_CELL` 등 → `entity/constants` 또는 control 경유.
- [ ] **`main_window` UI 분기 단순화** — `code` 분기 중복 정리 (Simplify Conditional).

### D — 테스트·REFACTOR 게이트

> 구조 이동(B/C) 전에 관련 항목 GREEN. 테스트 없이 ECB 분리 금지.

- [x] **AC-FR-01-01 G1~G4** — `test_ac_fr_01_01_invalid_size.py` **33/33** green.
- [ ] **`tests/boundary/` 잔여** — AC-FR-01-04 + EX-02 비-list 케이스.
- [ ] **OUT contract (E007)** — `STUB` 대체 후 integration 검증.
- [ ] **Entity no-solution 단위 테스트** — `NoValidPlacementError` (GM-TC-05 격자, `tests/entity/`).
- [x] **`tests/control/` RED** — `test_solve_partial_magic_square.py` (D-SOL-01~04, SC-CTL-001); C3 GREEN 전 **RED** (`@pytest.mark.control_red`).
- [ ] **`tests/control/` GREEN** — `SolvePartialMagicSquare.execute` 구현 후 Tier 2 게이트.
- [ ] **Boundary facade 격리** — Control 추출 후 `ScreenBoundary` → `ApplicationService.solve_puzzle` **0회** spy (`test_plan.md` §6.3).
- [ ] **`tests/` for `main_window`** — UI는 facade mock만; entity 직접 wiring 금지 검증 (pytest-qt 또는 로직 분리).
- [ ] **REFACTOR 게이트** — `pytest -m golden_master` + boundary/entity/control 스위트 green, 커버리지 Boundary≥85% / Control≥85%.

### 잘 유지할 것 (리뷰 통과 — 작업 불필요)

- [x] Boundary mock 격리 (`tests/boundary/conftest.py`, `resolve` 0회)
- [x] Golden Master GM-TC-01~05 (`tests/golden_master/`)
- [x] Domain `deepcopy`·FR-02~05 핵심 (`tests/entity/`)
- [x] Forbidden 패턴 준수 (`print`, bare except, skip/xfail 없음)

### 한 줄 원칙

REFACTOR는 계약·행위 불변 하에 구조만 옮기므로, GREEN 스위트 없이 ECB 분리 시 계약 붕괴를 검출할 수 없다.

---

## 다음 단계 (권장 순서)

1. **REFACTOR C1 (RF-01)** — Tier 1 게이트 유지, `ValidationResult` / `input_validator` ([Report/14](Report/14.MagicSquare_REFACTOR_Program_Report.md) Wave 1 C1)
2. **REFACTOR C2 (RF-02)** — `STUB` → `ERR_INTERNAL_CONTRACT`, ErrorMapper
3. **Tier 2 + C3~C4** — `control/` GREEN, 카테고리 A 잔여(비-list·열/값)
4. **카테고리 C + D(전체 게이트)** — `main_window` DI·커버리지 Boundary/Control ≥85%

---

## RED 단계 To-Do 리스트

> 이 체크리스트는 test_plan.md 기반으로 생성되었습니다.
> 각 항목은 RED(실패 테스트 작성) 완료 시 체크합니다.

### Track A — UI / Boundary 테스트
- [ ] TC-A-01: grid=None 입력 → 실패 결과 반환 (Happy Path of Failure)
- [ ] TC-A-02: code가 정확히 "INVALID_SIZE" 문자열인지 검증
- [ ] TC-A-03: message가 "Grid must be 4x4." 와 문자 단위 동일한지 검증
- [ ] TC-A-04: grid=None 시 Domain 진입점 0회 호출 (mock/spy 검증)
- [ ] TC-A-05: grid=[] 빈 리스트 → 실패 결과 반환
- [ ] TC-A-06: grid=3×4 크기 불일치 → 실패 결과 반환
- [ ] TC-A-07: 반환 객체 타입이 지정 실패 결과 구조체인지 검증

### Track B — Domain / Logic 테스트
- [ ] TC-B-01: resolve()가 None grid를 직접 받지 않음을 격리 검증
- [ ] TC-B-02: Boundary가 None 분기를 처리 후 resolve() 미호출 확인
- [ ] TC-B-03: resolve() mock이 호출됐을 경우 테스트 실패 처리
- [ ] TC-B-04: AC-FR-01-02~05 범위의 케이스는 이 커밋에 포함하지 않음 확인

### 커버리지 목표
- [ ] Domain Logic: 95%+ (pip install pytest-cov)
- [ ] Boundary Layer: 85%+
- [ ] 전체 TOTAL: 90%+

### 결함 목록 연결
- [ ] defect_list.md 생성 및 발견 결함 기록
- [ ] 모든 결함 수정 후 회귀 테스트 통과 확인

---

## Golden Master 회귀 안전장치

> Refactoring 시작 전 구축. GREEN 완료 후 즉시 적용.

### 기준 파일 생성
- [x] GM-01: `golden_master_expected.txt` 생성
- [x] GM-02: 정상/역순/오류 시나리오 추가
- [x] GM-03: `git add tests/golden_master_expected.txt`

### 테스트 코드
- [x] GM-04: `test_golden_master_magic_square` 작성
- [x] GM-05: approve 패턴 적용
- [x] GM-06: Golden Master 테스트 PASS 확인

### 회귀 보호
- [x] GM-07: row-major 규칙 보호
- [x] GM-08: 1-index 출력 보호
- [x] GM-09: reverse 조합 fallback 보호
- [x] GM-10: Error Contract 보호

---

## GREEN 단계 To-Do 리스트

> 대상: `tests/boundary/test_ac_fr_01_01_invalid_size.py` (AC-FR-01-01, **33 tests**)  
> 계약: `code="INVALID_SIZE"`, `message="Grid must be 4x4."`, 실패 시 `resolve()` **0회**  
> 각 커밋(G2~G4)마다: 해당 wave 테스트 통과 → 전체 파일 회귀 → 커밋 (테스트 수정 금지)

### 진행 요약

| 커밋 | 구현 범위 | 신규 GREEN | 누적 | 상태 |
|------|-----------|------------|------|------|
| **G1** | `grid is None` | 11 (+ Scope 5) | 16/33 | ✅ |
| **G2** | `grid == []` (행 수 0) | +6 | 22/33 | ✅ |
| **G3** | `grid == [[]]*4` (4행·0열) | +5 | 27/33 | ✅ |
| **G4** | `grid == THREE_BY_FOUR_GRID` (3행) | +6 | 33/33 | ✅ |

전체 회귀: `python -m pytest tests/boundary/test_ac_fr_01_01_invalid_size.py -q`

---

### G1 — `grid is None` ✅ (16/33)

#### 구현
- [x] `src/magic_square/boundary/invalid_size.py` 추가 (`INVALID_SIZE_CODE`, `INVALID_SIZE_MESSAGE`)
- [x] `ScreenBoundary.solve()`: `grid is None` → `FailureResult` 반환, `resolve()` 미호출

#### 테스트 — `TestAcFr0101NormalFailureReturn` (5)
- [x] `test_none_grid_returns_failure_invalid_size_code`
- [x] `test_none_grid_returns_failure_prd_message`
- [x] `test_none_grid_returns_failure_not_success_tuple`
- [x] `test_none_grid_returns_failure_result_type`
- [x] `test_none_grid_returns_failure_without_unhandled_exception`

#### 테스트 — `TestAcFr0101DomainIsolation` (2)
- [x] `test_none_grid_resolve_zero_calls_spy`
- [x] `test_none_grid_resolve_assert_not_called_mock`

#### 테스트 — `TestAcFr0101MessageIdentity` (2)
- [x] `test_none_grid_message_exact_prd_section_8_1`
- [x] `test_none_grid_message_length_matches_prd_literal`

#### 테스트 — `TestAcFr0101ParametrizedContract` (2)
- [x] `test_param_grid_returns_failure_invalid_size_code[None]`
- [x] `test_param_grid_resolve_zero_calls[None]`

#### 테스트 — `TestAcFr0101ScopeLimit` (5, 구현 불필요)
- [x] `test_scope_param_grids_exclude_valid_four_by_four`
- [x] `test_scope_param_grids_exclude_wrong_empty_count`
- [x] `test_scope_param_grids_exclude_value_range_violation`
- [x] `test_scope_param_grids_exclude_duplicate_values`
- [x] `test_scope_contract_code_is_only_invalid_size_constant`

---

### G2 — `grid == []` ✅ (22/33)

#### 구현
- [x] 빈 리스트(`grid == []`) 거부 → `INVALID_SIZE` + `"Grid must be 4x4."`
- [x] 실패 시 `resolve()` 미호출

#### 테스트 (6)
- [x] `TestAcFr0101BoundaryValues::test_empty_list_grid_returns_failure_invalid_size_code`
- [x] `TestAcFr0101BoundaryValues::test_empty_list_grid_returns_failure_prd_message`
- [x] `TestAcFr0101DomainIsolation::test_empty_list_grid_resolve_zero_calls_spy`
- [x] `TestAcFr0101MessageIdentity::test_empty_list_grid_message_exact_prd_section_8_1`
- [x] `TestAcFr0101ParametrizedContract::test_param_grid_returns_failure_invalid_size_code[grid1]`
- [x] `TestAcFr0101ParametrizedContract::test_param_grid_resolve_zero_calls[grid1]`

#### 검증
- [x] wave 6건 PASSED
- [x] 전체 파일 **22 passed** (G3·G4 진행 시 잔여 failed)

---

### G3 — `grid == [[]]*4` ✅ (27/33)

#### 구현
- [x] 4행·0열(`[[]]*4`) 거부 → 동일 `INVALID_SIZE` 계약
- [x] 실패 시 `resolve()` 미호출

#### 테스트 (5)
- [x] `TestAcFr0101BoundaryValues::test_four_empty_row_lists_grid_returns_failure_invalid_size_code`
- [x] `TestAcFr0101DomainIsolation::test_four_empty_row_lists_resolve_zero_calls_spy`
- [x] `TestAcFr0101MessageIdentity::test_four_empty_row_lists_message_exact_prd_section_8_1`
- [x] `TestAcFr0101ParametrizedContract::test_param_grid_returns_failure_invalid_size_code[grid2]`
- [x] `TestAcFr0101ParametrizedContract::test_param_grid_resolve_zero_calls[grid2]`

#### 검증
- [x] wave 5건 PASSED
- [x] 전체 파일 **27 passed** (G4 진행 시 잔여 failed)

---

### G4 — `grid == THREE_BY_FOUR_GRID` ✅ (33/33)

#### 구현
- [x] 3행 격자(`len(grid) == 3`) 거부 → 동일 `INVALID_SIZE` 계약
- [x] 실패 시 `resolve()` 미호출
- [x] AC-FR-01-01 파일 전체 GREEN

#### 테스트 (6)
- [x] `TestAcFr0101BoundaryValues::test_three_by_four_grid_returns_failure_invalid_size_code`
- [x] `TestAcFr0101BoundaryValues::test_three_by_four_grid_returns_failure_result_type`
- [x] `TestAcFr0101DomainIsolation::test_three_by_four_grid_resolve_zero_calls_spy`
- [x] `TestAcFr0101MessageIdentity::test_three_by_four_grid_message_exact_prd_section_8_1`
- [x] `TestAcFr0101ParametrizedContract::test_param_grid_returns_failure_invalid_size_code[grid3]`
- [x] `TestAcFr0101ParametrizedContract::test_param_grid_resolve_zero_calls[grid3]`

#### 검증
- [x] wave 6건 PASSED
- [x] 전체 파일 **33 passed / 0 failed**

---

### 커밋당 워크플로 (G2~G4 반복)

- [ ] 해당 wave 테스트만 먼저 실행
- [ ] 최소 프로덕션 변경 (`screen_boundary.py`, 상수는 `invalid_size.py`)
- [ ] 테스트 수정 없음 (skip / xfail / assertion 약화 금지)
- [ ] 전체 파일 회귀 실행
- [ ] wave당 커밋 1개

### pytest 노드 ID 빠른 참조

> 접두사: `tests/boundary/test_ac_fr_01_01_invalid_size.py::`  
> 구분자: `::` (콜론 **두 개** — `.py:Class`는 파일 없음 오류)

**G2**
```
TestAcFr0101BoundaryValues::test_empty_list_grid_returns_failure_invalid_size_code
TestAcFr0101BoundaryValues::test_empty_list_grid_returns_failure_prd_message
TestAcFr0101DomainIsolation::test_empty_list_grid_resolve_zero_calls_spy
TestAcFr0101MessageIdentity::test_empty_list_grid_message_exact_prd_section_8_1
TestAcFr0101ParametrizedContract::test_param_grid_returns_failure_invalid_size_code[grid1]
TestAcFr0101ParametrizedContract::test_param_grid_resolve_zero_calls[grid1]
```

**G3**
```
TestAcFr0101BoundaryValues::test_four_empty_row_lists_grid_returns_failure_invalid_size_code
TestAcFr0101DomainIsolation::test_four_empty_row_lists_resolve_zero_calls_spy
TestAcFr0101MessageIdentity::test_four_empty_row_lists_message_exact_prd_section_8_1
TestAcFr0101ParametrizedContract::test_param_grid_returns_failure_invalid_size_code[grid2]
TestAcFr0101ParametrizedContract::test_param_grid_resolve_zero_calls[grid2]
```

**G4**
```
TestAcFr0101BoundaryValues::test_three_by_four_grid_returns_failure_invalid_size_code
TestAcFr0101BoundaryValues::test_three_by_four_grid_returns_failure_result_type
TestAcFr0101DomainIsolation::test_three_by_four_grid_resolve_zero_calls_spy
TestAcFr0101MessageIdentity::test_three_by_four_grid_message_exact_prd_section_8_1
TestAcFr0101ParametrizedContract::test_param_grid_returns_failure_invalid_size_code[grid3]
TestAcFr0101ParametrizedContract::test_param_grid_resolve_zero_calls[grid3]
```

---

## 문서 이력

| 버전 | 날짜 | 내용 |
|------|------|------|
| 보고서 1.0 | 2026-05-28 | STEP 1, 2, 3, 5 |
| 보고서 1.1 | 2026-05-28 | STEP 4 (Why #3, TDD) 추가 |
| README 1.0 | 2026-05-28 | 프로젝트 개요 최초 작성 |
| 보고서 2.0 | 2026-05-28 | Dual-Track · Clean Architecture 설계 |
| README 1.1 | 2026-05-28 | 설계·Prompt Export 반영 |
| README 1.2 | 2026-05-29 | AC-FR-01-01 GREEN 단계 To-Do (G1~G4) 추가 |
| README 1.3 | 2026-05-29 | 코드 리뷰 To-Do (### REFACTOR 카테고리 (4분류)

| 카테고리 | 이름 | 한 줄 | 우선순위 |
|----------|------|-------|----------|
| **A** | 계약·검증 | Boundary가 무엇을 거부·반환하는가 | P0 → P1 |
| **B** | ECB·책임 분리 | 누가 orchestration 하는가 (Control vs Entity) | P0~P1 |
| **C** | 조립·UI 경계 | Screen이 누구를 생성·주입하는가 | P1 → P2 |
| **D** | 테스트·REFACTOR 게이트 | 옮긴 뒤에도 행위가 같은가 | P0~P2 |

**권장 실행 순서:** `A` + `D`(선행 GREEN) → `B` → `C` → `D`(전체 게이트)~P2), 현재 상태·저장소 구조 갱신 |
| README 1.4 | 2026-05-29 | 코드 리뷰 To-Do 4분류 (A~D), Report/13 링크·권장 실행 순서 반영 |
| README 1.5 | 2026-05-29 | Report/14 Phase 0 Tier 1/2, OI-01 확정, G2~G4 33/33, tests/control RED |
| Report 14.0 | 2026-05-29 | REFACTOR 프로그램·Phase 0·OI-01·Wave 1 매핑 |
| Report 15.0 | 2026-05-29 | REFACTOR 프로그램 준비 구현·control RED·Tier 1 검증 |

---

## 라이선스 / 기여

미정. 학습·과제 맥락의 개인/수업 프로젝트로 시작되었습니다.
