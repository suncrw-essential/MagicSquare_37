# MagicSquare_30

4×4 마방진(Magic Square)을 다루는 학습·실습 프로젝트입니다.  
현재 단계는 **Dual-Track TDD · Clean Architecture 설계**까지 완료되었으며, **구현·테스트 코드는 아직 없습니다.**

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

- **언어·런타임·테스트 프레임워크:** 미정
- **UI 실제 화면:** Boundary 계약만 정의됨

---

## 저장소 구조

```
MagicSquare_30/
├── README.md
├── Report/
│   ├── 01.MagicSquare_ProblemDefinition_Report.md
│   └── 02.MagicSquare_DualTrack_CleanArchitecture_Design.md
├── Prompt/
│   └── 02.MagicSquare_DualTrack_CleanArchitecture_Transcript.md
└── Prompting/
    └── 01.MagicSquare_ProblemDefinition_Reportt.md
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
| 구현 / 테스트 코드 | 없음 |

---

## 다음 단계 (권장 순서)

1. **RED 테스트** — Domain `DT-*` → UI `UT-*` → Data `ST-*` → Integration `IT-*`
2. **구현** — Domain 솔버 → UI Boundary → File `MatrixRepository`
3. **커버리지** — Domain 95%+ / UI 85%+ / Data 80%+

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

## 문서 이력

| 버전 | 날짜 | 내용 |
|------|------|------|
| 보고서 1.0 | 2026-05-28 | STEP 1, 2, 3, 5 |
| 보고서 1.1 | 2026-05-28 | STEP 4 (Why #3, TDD) 추가 |
| README 1.0 | 2026-05-28 | 프로젝트 개요 최초 작성 |
| 보고서 2.0 | 2026-05-28 | Dual-Track · Clean Architecture 설계 |
| README 1.1 | 2026-05-28 | 설계·Prompt Export 반영 |

---

## 라이선스 / 기여

미정. 학습·과제 맥락의 개인/수업 프로젝트로 시작되었습니다.
