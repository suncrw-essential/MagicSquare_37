# PRD — Magic Square 4x4 TDD Practice

## 1. Executive Summary
Magic Square 4x4 TDD Practice는 정답 생성 중심 과제가 아니라, 불변식 기반 사고와 계약 기반 검증을 훈련하는 구현 전 기준 문서 프로젝트다. 본 PRD는 입력/출력 계약을 고정하고, Dual-Track TDD(Track A: Boundary/UI Contract, Track B: Domain/Logic Invariant)를 병렬 적용하며, RED-GREEN-REFACTOR 흐름과 Concept-to-Code Traceability를 강제한다. 모든 요구사항은 테스트 가능 문장으로 정의하며, Boundary와 Domain 책임을 분리하여 리팩토링 이후에도 계약이 유지되는 개발 체계를 구축한다.

## 2. Background
학습자는 마방진 문제를 풀 때 구현을 먼저 시작하고, 이후 테스트를 맞추는 순서로 진행하는 경향이 있다. 이 접근은 완성 기준의 불명확성, 실패 원인 비가시성, 그리고 회귀 시 계약 붕괴를 유발한다. 본 프로젝트는 4x4 마방진을 매개로 "정답 찾기"가 아니라 "조건 판정 체계 구축"을 훈련한다. 핵심은 1~16 사용 규칙, 10개 선(행/열/대각선) 합 규칙, 결정적 출력 형식을 사전에 고정하고 검증 가능한 단위로 분해하는 것이다.

## 3. Problem Statement
본 프로젝트의 문제는 "마방진을 만든다"가 아니라 "주어진 입력이 불변식 계약을 만족하는지 결정적 규칙으로 판정하고 결과를 계약된 형식으로 반환한다"로 정의한다.  
핵심 문제는 다음과 같다.

- 입력 계약이 고정되지 않으면 테스트가 기준을 잃는다.
- 출력 계약이 고정되지 않으면 리팩토링 후 호환성이 깨진다.
- Boundary와 Domain이 혼합되면 실패 원인 추적이 불가능해진다.
- 판정 규칙이 불완전하면 거짓 양성이 발생한다.

## 4. Why Now / Why Chain
- **Why #1 (학습 관점):** 학습자는 "완성"을 결과물로만 해석하고, 조건 충족 증명을 생략한다.
- **Why #2 (개발 관점):** 동일 입력에 동일 결과를 보장하는 자동 검증 경로가 없으면 회귀 결함이 반복된다.
- **Why #3 (아키텍처 관점):** Boundary 검증과 Domain 불변식이 분리되지 않으면 테스트 책임이 혼합되어 변경 영향이 확산된다.
- **Why Now:** 구현 선행 습관, 모호한 테스트 기준, 계층 책임 혼합, 리팩토링 후 계약 붕괴를 현재 단계에서 차단해야 한다.

## 5. Target Users
- TDD 학습자
- 코드 리뷰어
- Clean Architecture + ECB를 훈련하는 개발자

사용 환경:
- 콘솔 실행 및 테스트 실행 중심
- UI 화면, DB, Web/API는 범위 밖

## 6. Vision & Epic Goal
- **Vision:** 불변식과 계약을 우선 정의하고 테스트로 검증하는 학습형 소프트웨어 설계 체계를 확립한다.
- **Epic Goal:** "불변식 기반 사고 훈련 시스템 구축"
- **Success Condition:** 요구사항이 Concept → Rule → Use Case → Contract → Test → Component로 추적 가능해야 한다.

## 7. Persona
1. **Persona A — TDD Beginner Developer**
   - 구현 우선 습관이 있다.
   - 실패 기준 명시와 RED 단계 고정이 필요하다.

2. **Persona B — Architecture Learner**
   - Boundary/Control/Domain 분리를 실습하려고 한다.
   - 의존 방향 위반 방지 규칙이 필요하다.

3. **Persona C — Refactoring-focused Developer**
   - 기능 추가보다 계약 안정성을 우선한다.
   - 회귀 보호 테스트와 트레이서빌리티가 필요하다.

## 8. User Journey Summary

| Stage | Pain Point | Learning Outcome |
|---|---|---|
| 1. 문제 인식 | "맞는 것 같다" 수준의 주관적 판단 | 판정 기준을 명시적 규칙으로 전환 |
| 2. 계약 정의 | 입력/출력 형식이 구현 중 변경됨 | IN/OUT 계약 고정 |
| 3. 도메인 분리 | 검증 로직이 경계 계층에 섞임 | Boundary와 Domain 책임 분리 |
| 4. Dual-Track RED | UI 테스트와 Logic 테스트가 뒤섞임 | Track A/B 병렬 RED 수행 |
| 5. GREEN 최소 구현 | 과구현으로 리팩토링 비용 증가 | 테스트 통과 최소 구현 원칙 적용 |
| 6. REFACTOR | 구조 개선 중 계약 붕괴 | 계약 고정 + 회귀 보호 실행 |

## 9. Scope

### 9.1 In-Scope
- 빈칸 좌표 탐색
- 누락 숫자 탐색
- 마방진 판정
- 두 조합 시도 후 결과 반환
- Boundary 계층 입력 검증
- 출력 계약 검증
- RED-GREEN-REFACTOR 기반 테스트 가능 요구사항 정의

### 9.2 Out-of-Scope
- UI 화면 개발
- DB 저장/검색
- Web/API 서버 개발
- N×N 일반화
- 완전한 마방진 생성 알고리즘
- 사용자 인증/권한
- 네트워크 오류 처리
- QR 스캔
- 외부 서비스 연동

## 10. Functional Requirements

### FR-01 Input Verification
- **Description:** Boundary는 입력 행렬의 형식/값/중복/빈칸 규칙을 검증해야 한다.
- **Layer:** Boundary
- **Input:** `int[4][4]`
- **Processing Rules:** BR-01, BR-02, BR-03, BR-04
- **Output:** 검증 성공 또는 정의된 오류 응답
- **Acceptance Criteria:**
  - AC-01: 행 수가 4가 아니면 `ERR_GRID_ROWS`를 반환해야 한다.
  - AC-02: 어떤 행의 열 수가 4가 아니면 `ERR_GRID_COLS`를 반환해야 한다.
  - AC-03: `0`의 개수가 2가 아니면 `ERR_EMPTY_COUNT`를 반환해야 한다.
  - AC-04: 값이 `0` 또는 `1..16` 범위를 벗어나면 `ERR_VALUE_RANGE`를 반환해야 한다.
  - AC-05: `0` 제외 중복이 있으면 `ERR_DUPLICATE`를 반환해야 한다.
- **Error / Exception Policy:** 입력 검증 실패 시 Domain resolver를 호출하지 않는다.
- **Related Business Rules:** BR-01~BR-04
- **Related Test Direction:** UT-Input-Invalid 계열
- **Component Candidate:** BoundaryValidator

### FR-02 Blank Coordinate Discovery
- **Description:** Domain은 row-major 순서로 첫 번째/두 번째 빈칸 좌표를 결정해야 한다.
- **Layer:** Domain
- **Input:** 유효 입력 행렬
- **Processing Rules:** BR-05
- **Output:** `(r1,c1)`, `(r2,c2)` (1-index)
- **Acceptance Criteria:**
  - AC-06: 첫 번째 빈칸은 row-major 스캔 최초 `0`이어야 한다.
  - AC-07: 두 번째 빈칸은 row-major 스캔 두 번째 `0`이어야 한다.
- **Error / Exception Policy:** Domain 전제 위반은 `ERR_INTERNAL_CONTRACT`로 매핑한다.
- **Related Business Rules:** BR-05
- **Related Test Direction:** DT-BlankFinder
- **Component Candidate:** BlankFinder

### FR-03 Missing Number Discovery
- **Description:** Domain은 1..16 집합에서 누락된 두 숫자를 찾아 오름차순으로 반환해야 한다.
- **Layer:** Domain
- **Input:** 유효 입력 행렬
- **Processing Rules:** BR-06, BR-07
- **Output:** `(a,b)` where `a < b`
- **Acceptance Criteria:**
  - AC-08: 누락 숫자 개수는 정확히 2개여야 한다.
  - AC-09: 반환 순서는 오름차순이어야 한다.
- **Error / Exception Policy:** 누락 숫자 계산 불가 상태는 `ERR_INTERNAL_CONTRACT`로 매핑한다.
- **Related Business Rules:** BR-06, BR-07
- **Related Test Direction:** DT-MissingNumberFinder
- **Component Candidate:** MissingNumberFinder

### FR-04 Magic Square Validation
- **Description:** Domain은 완성 후보 격자가 마방진 불변식을 만족하는지 판정해야 한다.
- **Layer:** Domain
- **Input:** 두 조합으로 채운 완성 후보 격자
- **Processing Rules:** BR-08, BR-09
- **Output:** 유효/무효 판정
- **Acceptance Criteria:**
  - AC-10: 마방진 상수는 34로 판정해야 한다.
  - AC-11: 행 4개, 열 4개, 대각선 2개의 합이 모두 34여야 유효로 판정해야 한다.
- **Error / Exception Policy:** 판정 로직은 결정적이어야 한다.
- **Related Business Rules:** BR-08, BR-09
- **Related Test Direction:** DT-MagicSquareValidator
- **Component Candidate:** MagicSquareValidator

### FR-05 Two-Combination Solver and Result Formatting
- **Description:** Domain은 small-first 조합을 먼저 시도하고 실패 시 reverse 조합을 시도한 뒤, 성공 조합을 `int[6]` 형식으로 반환해야 한다.
- **Layer:** Domain + Boundary Output Contract
- **Input:** 유효 입력 행렬
- **Processing Rules:** BR-10, BR-11, BR-12, BR-13
- **Output:** `[r1,c1,n1,r2,c2,n2]`
- **Acceptance Criteria:**
  - AC-12: Attempt 1(`a→E1`, `b→E2`)이 유효면 해당 순서를 반환해야 한다.
  - AC-13: Attempt 1 무효이고 Attempt 2(`b→E1`, `a→E2`) 유효면 반대 순서를 반환해야 한다.
  - AC-14: 두 조합 모두 무효면 `ERR_NO_SOLUTION`을 반환해야 한다.
  - AC-15: 반환 좌표는 1-index여야 한다.
  - AC-16: 반환 길이는 6이어야 한다.
- **Error / Exception Policy:** 실패 정책은 예외 전파가 아니라 표준 오류 응답 반환으로 고정한다.
- **Related Business Rules:** BR-10~BR-13
- **Related Test Direction:** DT-Solver + UT-OutputContract
- **Component Candidate:** Solver, ResultFormatter

## 11. Business Rules / Domain Rules

| Rule ID | Rule (항상 참이어야 하는 규칙) |
|---|---|
| BR-01 | 입력은 정확히 4행이어야 한다. |
| BR-02 | 각 행은 정확히 4열이어야 한다. |
| BR-03 | 빈칸 값 `0`의 개수는 정확히 2개여야 한다. |
| BR-04 | 각 셀 값은 `0` 또는 `1..16`이어야 하며, `0` 제외 값은 중복되면 안 된다. |
| BR-05 | 첫 번째 빈칸(E1)은 row-major 스캔 최초 `0`, 두 번째 빈칸(E2)은 두 번째 `0`이어야 한다. |
| BR-06 | 누락 숫자 개수는 정확히 2개여야 한다. |
| BR-07 | 누락 숫자 쌍은 오름차순 `(a,b)`로 정의되며 `a<b`를 만족해야 한다. |
| BR-08 | 4x4 마방진 상수는 34여야 한다. |
| BR-09 | 완성 후보 유효성은 행 4개, 열 4개, 대각선 2개의 합이 모두 34인 경우에만 참이다. |
| BR-10 | Solver는 Attempt 1(`a→E1`, `b→E2`)을 Attempt 2보다 먼저 수행해야 한다. |
| BR-11 | Attempt 1 실패 시에만 Attempt 2(`b→E1`, `a→E2`)를 수행해야 한다. |
| BR-12 | 성공 출력은 `[r1,c1,n1,r2,c2,n2]` 형식의 `int[6]`이어야 한다. |
| BR-13 | 출력 좌표는 1-index여야 한다. |
| BR-14 | 동일 입력은 항상 동일 출력을 반환해야 한다(결정성). |
| BR-15 | Solver는 원본 입력 행렬을 변경하면 안 된다(부작용 금지). |

## 12. Input / Output Contract

### 12.1 Input Contract

| Field / Item | Type | Rule | Valid Example | Invalid Example | Related Error Code |
|---|---|---|---|---|---|
| `grid` rows | `int[4][4]` | 행 수 = 4 | `[[...],[...],[...],[...]]` | `[[...],[...],[...]]` | `ERR_GRID_ROWS` |
| `grid` cols | `int[4][4]` | 각 행 열 수 = 4 | `[1,2,3,0]` | `[1,2,3]` | `ERR_GRID_COLS` |
| empty count | integer count | `0` 개수 = 2 | 두 칸만 `0` | `0`이 1개/3개 | `ERR_EMPTY_COUNT` |
| value range | cell int | 각 값 ∈ `{0} ∪ [1,16]` | `0`, `1`, `16` | `-1`, `17` | `ERR_VALUE_RANGE` |
| uniqueness | set | `0` 제외 중복 금지 | `1..16` 중 중복 없음 | `5`가 두 번 등장 | `ERR_DUPLICATE` |

### 12.2 Output Contract

| Field / Item | Type | Rule | Valid Example | Invalid Example | Related Failure Policy |
|---|---|---|---|---|---|
| result length | `int[6]` | 길이 = 6 | `[1,1,1,4,4,16]` | `[1,1,1,4,4]` | `ERR_INTERNAL_CONTRACT` |
| coordinate range | int | `r1,c1,r2,c2` ∈ `[1,4]` | `1,1,4,4` | `0,1,5,4` | `ERR_INTERNAL_CONTRACT` |
| number range | int | `n1,n2` ∈ `[1,16]`, `n1!=n2` | `1,16` | `0,16` 또는 `7,7` | `ERR_INTERNAL_CONTRACT` |
| format | tuple order | `[r1,c1,n1,r2,c2,n2]` 고정 | `[1,1,1,4,4,16]` | `[n1,r1,c1,...]` | `ERR_INTERNAL_CONTRACT` |
| solving order | deterministic policy | Attempt 규칙 준수 | Attempt1 성공 시 small-first 반환 | Attempt1 성공인데 reverse 반환 | `ERR_INTERNAL_CONTRACT` |

## 13. Error / Failure Policy

| Case | Error Code | Message | Layer | Domain resolver 호출 여부 | Related AC |
|---|---|---|---|---|---|
| 4x4 아님 (행 수 오류) | `ERR_GRID_ROWS` | `Grid must have exactly 4 rows.` | Boundary | No | AC-01 |
| 4x4 아님 (열 수 오류) | `ERR_GRID_COLS` | `Each row must have exactly 4 columns.` | Boundary | No | AC-02 |
| 빈칸 개수 오류 | `ERR_EMPTY_COUNT` | `Grid must contain exactly 2 empty cells (0).` | Boundary | No | AC-03 |
| 값 범위 위반 | `ERR_VALUE_RANGE` | `Cell values must be 0 or between 1 and 16 inclusive.` | Boundary | No | AC-04 |
| 0 제외 중복 | `ERR_DUPLICATE` | `Non-zero values must be unique.` | Boundary | No | AC-05 |
| 두 조합 모두 실패 | `ERR_NO_SOLUTION` | `No valid magic square placement exists for the given grid.` | Domain 결과를 Boundary가 표준화 | Yes | AC-14 |
| 내부 계약 위반 | `ERR_INTERNAL_CONTRACT` | `Internal error: output contract violated.` | Boundary | Yes | AC-16 |

정책 고정:
- 입력 검증 실패 시 Domain resolver 호출은 금지한다.
- Solver 실패 정책은 `ERR_NO_SOLUTION` 반환으로 고정한다.
- PRD 범위에서 비정의 예외 전파 정책은 허용하지 않는다.

## 14. Non-Functional Requirements

| NFR ID | Requirement |
|---|---|
| NFR-01 | Domain Logic 테스트 커버리지는 95% 이상이어야 한다. |
| NFR-02 | Boundary Validation 테스트 커버리지는 85% 이상이어야 한다. |
| NFR-03 | 동일 입력은 동일 출력을 반환해야 한다(결정적 실행). |
| NFR-04 | Solver는 원본 입력 행렬을 변경하면 안 된다(부작용 금지). |
| NFR-05 | 4x4 단일 실행 처리 시간은 50ms 이하여야 한다(로컬 표준 환경 기준). |
| NFR-06 | Boundary와 Domain 책임 분리를 유지해야 한다. |
| NFR-07 | 하드코딩 도메인 상수는 금지하며, 명명된 상수를 사용해야 한다. |
| NFR-08 | 설명 없는 매직 넘버 사용은 금지한다. |

## 15. Dual-Track TDD Strategy

### 15.1 Track A — Boundary / UI Contract TDD
- 입력 검증 테스트를 먼저 작성해야 한다.
- 출력 형식 검증 테스트를 작성해야 한다.
- 실패 응답 코드/메시지 테스트를 작성해야 한다.
- 입력 검증 실패 시 Domain resolver 미호출 테스트를 작성해야 한다.

### 15.2 Track B — Domain / Logic TDD
- 빈칸 탐색 테스트를 작성해야 한다.
- 누락 숫자 탐색 테스트를 작성해야 한다.
- 마방진 검증 테스트를 작성해야 한다.
- small-first 성공 테스트를 작성해야 한다.
- small-first 실패 후 reverse 성공 테스트를 작성해야 한다.
- 두 조합 모두 실패 테스트를 작성해야 한다.

### 15.3 Parallel Progression Rules
- UI RED와 Logic RED를 분리해야 한다.
- UI GREEN과 Logic GREEN은 각 Track의 현재 실패 테스트를 통과하는 최소 구현으로 제한해야 한다.
- 구조 개선은 REFACTOR 단계에서만 수행해야 한다.
- Domain 완성 후 Boundary를 부착하는 단일 트랙 순차 방식은 금지한다.
- 테스트 삭제, skip, xfail, assertion 약화는 금지한다.

## 16. Test Plan / QA

### 16.1 Normal Scenarios
- TS-N-01: small-first 성공
- TS-N-02: small-first 실패 후 reverse 성공

### 16.2 Exception Scenarios
- TS-E-01: 4x4 아닌 입력
- TS-E-02: 빈칸 개수 오류
- TS-E-03: 값 범위 오류
- TS-E-04: 중복 값 오류
- TS-E-05: 두 조합 모두 실패

### 16.3 Boundary Scenarios
- TS-B-01: 최소값 1 처리
- TS-B-02: 최대값 16 처리
- TS-B-03: `0`은 빈칸으로만 처리
- TS-B-04: 출력 좌표 1-index 검증
- TS-B-05: 반환 배열 길이 6 검증

### 16.4 Representative Test Data
| Data ID | Description | Target Scenario |
|---|---|---|
| TD-01 | small-first 성공 행렬 | TS-N-01 |
| TD-02 | reverse 성공 행렬 | TS-N-02 |
| TD-03 | invalid size 행렬 | TS-E-01 |
| TD-04 | invalid blank count 행렬 | TS-E-02 |
| TD-05 | duplicate value 행렬 | TS-E-04 |
| TD-06 | invalid range 행렬 | TS-E-03 |
| TD-07 | no-solution 행렬 | TS-E-05 |

## 17. Architecture Overview, High-Level

- **Boundary Layer**
  - 입력 검증
  - 오류 응답 표준화
  - 출력 포맷 계약 검증
- **Domain Layer**
  - 빈칸 탐색
  - 누락 숫자 탐색
  - 마방진 불변식 판정
  - 조합 시도 및 결과 결정
- **Control / Application Layer**
  - Boundary와 Domain 호출 순서 조정
  - 오케스트레이션 담당
  - 도메인 규칙 계산 금지

의존 방향:
- Boundary → Control → Domain
- Domain은 Boundary를 알지 않아야 한다.
- Domain은 UI/DB/Web/파일시스템에 의존하면 안 된다.

## 18. Component Candidates

| Component | Responsibility | Layer | Input | Output | Related FR | Related Test |
|---|---|---|---|---|---|---|
| BoundaryValidator | IN 계약 검증 및 오류 코드 반환 | Boundary | `int[4][4]` | validation result / error | FR-01 | TS-E-01~04 |
| BlankFinder | E1/E2 빈칸 좌표 결정 | Domain | valid grid | `(r1,c1),(r2,c2)` | FR-02 | DT-BlankFinder |
| MissingNumberFinder | 누락 숫자 2개 오름차순 산출 | Domain | valid grid | `(a,b)` | FR-03 | DT-MissingNumberFinder |
| MagicSquareValidator | 10개 선 합 34 판정 | Domain | completed candidate grid | valid/invalid | FR-04 | DT-MagicSquareValidator |
| Solver | Attempt1/Attempt2 순차 시도 및 성공 조합 결정 | Domain | valid grid | solution or no-solution | FR-05 | DT-Solver |
| ResultFormatter | `int[6]` 및 1-index 계약 고정 | Boundary or Control | domain solution tuple | `[r1,c1,n1,r2,c2,n2]` | FR-05 | UT-OutputContract |

## 19. Risks & Ambiguities

| Risk | Impact | Decision / Mitigation |
|---|---|---|
| 1-index와 0-index 혼동 | 출력 계약 위반 | BR-13 고정, TS-B-04 필수 |
| row-major 첫 빈칸 정의 누락 | Solver 결과 비결정성 | BR-05 고정, FR-02 AC-06/07 필수 |
| small-first/reverse 테스트 데이터 혼동 | 잘못된 Green | TD-01/TD-02 분리 관리 |
| 입력 행렬 변경 여부 불명확 | 부작용 회귀 | BR-15와 NFR-04로 불변 정책 고정 |
| 두 조합 실패 정책 누락 | 오류 처리 불일치 | `ERR_NO_SOLUTION`으로 단일 정책 확정 |
| 34 상수 하드코딩 | 변경 취약성, 의도 불명확 | 명명된 상수 정책(NFR-07/08) |
| Boundary/Domain 책임 혼합 | 유지보수성 저하 | Layer 책임 및 의존 규칙 강제 |
| 문서명 불일치(Report/4 vs 실제 산출물) | 출처 추적 혼란 | Section 22에 Decision Needed 등록 |

## 20. Engineering Principles

- Python 코드는 PEP8을 준수해야 한다.
- 공개 API는 type hints를 포함해야 한다.
- 테스트 프레임워크는 `pytest`를 사용해야 한다.
- 테스트는 AAA 패턴을 따라야 한다.
- Coverage 목표는 Domain 95%+, Boundary 85%+를 만족해야 한다.
- ECB 계층 분리를 준수해야 한다.
- RED-GREEN-REFACTOR 순서를 위반하면 안 된다.
- `print()` 디버깅은 금지한다.
- bare `except`는 금지한다.
- 테스트 약화(skip/xfail/assertion dilution)는 금지한다.
- 설명 없는 magic number는 금지한다.
- 계약 변경 시 관련 테스트와 문서를 동시에 갱신해야 한다.

## 21. Traceability Matrix

| Concept / Invariant | Business Rule | Feature ID | Acceptance Criteria | Test Case Candidate | Component |
|---|---|---|---|---|---|
| 4x4 입력 | BR-01, BR-02 | FR-01 | AC-01, AC-02 | TS-E-01 | BoundaryValidator |
| 빈칸 2개 | BR-03 | FR-01 | AC-03 | TS-E-02 | BoundaryValidator |
| 값 범위 0 또는 1~16 | BR-04 | FR-01 | AC-04 | TS-E-03 | BoundaryValidator |
| 중복 금지 | BR-04 | FR-01 | AC-05 | TS-E-04 | BoundaryValidator |
| row-major 첫 번째 빈칸 | BR-05 | FR-02 | AC-06 | DT-BlankFinder | BlankFinder |
| row-major 두 번째 빈칸 | BR-05 | FR-02 | AC-07 | DT-BlankFinder | BlankFinder |
| 누락 숫자 2개 | BR-06 | FR-03 | AC-08 | DT-MissingNumberFinder | MissingNumberFinder |
| 누락 숫자 오름차순 | BR-07 | FR-03 | AC-09 | DT-MissingNumberFinder | MissingNumberFinder |
| 마방진 상수 34 | BR-08 | FR-04 | AC-10 | DT-MagicSquareValidator | MagicSquareValidator |
| 행/열/대각선 합 | BR-09 | FR-04 | AC-11 | DT-MagicSquareValidator | MagicSquareValidator |
| small-first 시도 | BR-10 | FR-05 | AC-12 | TS-N-01 | Solver |
| reverse 시도 | BR-11 | FR-05 | AC-13 | TS-N-02 | Solver |
| int[6] 반환 | BR-12 | FR-05 | AC-16 | TS-B-05 | ResultFormatter |
| 1-index 좌표 | BR-13 | FR-05 | AC-15 | TS-B-04 | ResultFormatter |
| 결정성 | BR-14 | FR-05 | AC-12~14 | DT-Solver-Deterministic | Solver |
| 무부작용 | BR-15 | FR-05 | AC-12~14 | DT-Solver-NoMutation | Solver |

## 22. Open Questions / Decision Needed

| ID | Decision Needed | Reason |
|---|---|---|
| DN-01 | 요구사항 기준 문서 `Report/4.UserJourney_Epic_to_TechnicalScenario_Report.md`의 실제 저장소 경로를 확정해야 한다. | 현재 확인 가능한 파일명은 `Report/06...`이며 출처 추적 충돌이 존재한다. |
| DN-02 | `.cursorrules`를 운영 SSOT로 복원할지, `.cursor/rules/*.mdc` 단일 SSOT로 유지할지 확정해야 한다. | 저장소 기준 `.cursorrules` 파일 부재 상태다. |
| DN-03 | `ERR_INTERNAL_CONTRACT`를 외부 공개 오류 코드로 유지할지 내부 로깅 전용으로 제한할지 확정해야 한다. | 운영 노출 정책이 문서별로 고정되지 않았다. |

## 23. Appendix

### 23.1 참고 문서 목록
- `Report/1.ProblemDefinition_Report.md` (Background/Problem/Why Chain)
- `Report/2.CleanArchitecture_DualTrack_TDD_Design_Report.md` (Functional Contract/Invariant/Layer)
- `Report/3.DevelopmentEnvironment_CursorRules_ECB_UserEntity_Report.md` (Quality/Method/Constraints)
- `Report/4.UserJourney_Epic_to_TechnicalScenario_Report.md` *(Decision Needed: 실제 경로 확인)*
- `.cursor/rules/magicsquare-project.mdc`
- `.cursor/rules/magicsquare-ecb-architecture.mdc`
- `.cursor/rules/magicsquare-tdd-testing.mdc`
- `.cursor/rules/magicsquare-python-code-style.mdc`
- `.cursor/rules/magicsquare-forbidden.mdc`

### 23.2 Cursor Rules 요약
- 프로젝트 전역 원칙: Report/02 기반 ID 정합성 유지
- ECB 의존성 방향 고정
- pytest + AAA + RED-GREEN-REFACTOR 강제
- 금지 패턴(`print`, bare except, test weakening) 차단
- 계약 우선, 최적화 후순위

### 23.3 대표 Gherkin Scenario 요약
- **GS-01:** Given 유효 입력, When solve, Then `int[6]` 성공 반환
- **GS-02:** Given invalid size, When solve, Then `ERR_GRID_ROWS|COLS` 반환 및 Domain 미호출
- **GS-03:** Given small-first 실패/reverse 성공 입력, When solve, Then reverse 순서 반환
- **GS-04:** Given no-solution 입력, When solve, Then `ERR_NO_SOLUTION` 반환

### 23.4 향후 RED Test ID 후보
- Track A: UT-A-01~UT-A-10 (입력 검증/오류 매핑/출력 계약)
- Track B: DT-B-01~DT-B-12 (빈칸/누락/34검증/조합 시도/결정성/무부작용)
- Integration: IT-01~IT-06 (Boundary→Control→Domain 흐름 검증)
