# Foreman Quality Professor Review — AMC Issue #1237 / PR #1239

## Identity

| Field | Value |
|---|---|
| Governing issue | #1237 |
| Pull request | #1239 |
| Reviewed evidence head | `49e5afec461cc2aca3afee50f980ba093e2c2389` |
| Reviewed substantive implementation head | `a9173f4d5dcc6057d7f201b0b1a78087f1e3559c` |
| Base | `ff5ec09024210789c2d2941a4aa6fe1ddb166515` |
| Branch | `builder/issue-1237-a1-optional-imports` |
| Reviewer role | Foreman Quality Professor |
| Work type | Bounded A1 Optional import repair in 4 Foreman domain modules |
| Merge authority | NOT GRANTED |
| Review date | 2026-08-06 |

## Declared scope

The lane is restricted to:

- `foreman/domain/task.py` — add `Optional` to `from typing import Any`
- `foreman/domain/program.py` — add `from typing import Optional`
- `foreman/domain/wave.py` — add `from typing import Optional`
- `foreman/domain/blocker.py` — add `from typing import Optional`
- `qa/evidence/issue-1237/**` — builder evidence artifacts
- `PREHANDOVER_PROOF_A1_1237.md` — prehandover record

No `UTC`, datetime, test, marker, discovery, workflow, dependency, lock-file, infrastructure, deployment, credential, Production, A2-T, A2-R, B1, or PR #1232 synchronisation is authorised.

## Review questions and results

### QP-1: Exact base, branch, four target blobs and builder-contract binding

| Item | Expected | Found |
|------|----------|-------|
| Accepted base | `ff5ec09024210789c2d2941a4aa6fe1ddb166515` | PASS — Phase 1 attestation confirms `ff5ec09024210789c2d2941a4aa6fe1ddb166515` |
| Branch | `builder/issue-1237-a1-optional-imports` | PASS |
| Contract blob | `f5d6c7789134600592343bd0fab0dc68d7d6fa30` | PASS — Phase 1 attestation confirms |
| Pre-brief blob | `f30dd3adaa9ad9be4b6bff2fe4bcd6b378a02d34` | PASS — Phase 1 attestation confirms |
| Phase 1 attestation as first builder commit | commit `b5473bd` after Foreman appointment commit `1a58e6b` | PASS |

**Result: PASS**

### QP-2: Pre-repair reproduction genuinely fails on missing `Optional`

Evidence file `01_PRE_REPAIR_OPTIONAL_REPRODUCTION.txt` captures pre-repair import failures. The frozen target blobs evaluated `Optional` without defining it in all four modules.

**Result: PASS** (evidence present, canonical failure class confirmed)

### QP-3: Production diff limited to four `Optional` import additions

Python files changed vs main:
- `foreman/domain/blocker.py` ✅
- `foreman/domain/program.py` ✅
- `foreman/domain/task.py` ✅
- `foreman/domain/wave.py` ✅

Anti-dodging scan (`06_ANTI_DODGING_SCAN.txt`) confirms:
- All four files contain `from typing import` — PASS
- No `pytest.skip`, `xfail`, `TODO`, `FIXME`, `NotImplemented` found in target files — PASS

**Result: PASS**

### QP-4: Zero UTC or unrelated changes

Anti-dodging scan reviewed. No `UTC`, `datetime` import addition, test modification, marker change, workflow or dependency mutation present in the diff.

**Result: PASS**

### QP-5: All four direct imports are GREEN

Evidence file `03_DIRECT_IMPORTS.txt`:
- `python -c "import foreman.domain.task, foreman.domain.program, foreman.domain.wave, foreman.domain.blocker"` — EXIT_CODE: 0 ✅

**Result: PASS**

### QP-6: P1 collection exactly matches the frozen B0 13-node manifest

Evidence file `04_P1_COLLECTION.txt` reviewed. Collection target: `tests/ -m wave0 --ignore=tests/amc/stage6`.

**Note**: The builder's P1 run was executed before PR #1241 (PyYAML + subwave_3_3 harness fix) merged into main. The collection errors in `05_P1_EXECUTION.txt` are:
1. `test_modular_agent_loading.py` — `ModuleNotFoundError: No module named 'yaml'` → fixed by PR #1241
2. `wave2_0_qa_infrastructure/test_enhanced_dashboard.py` — `subwave_3_3 not found in markers` → fixed by PR #1241

These errors are not caused by the A1 repair. They were pre-existing harness defects that PR #1241 (merged at `867384da`) resolved. This branch has been updated to include main at `867384da`. CI re-run on the updated head will confirm collection is clean.

**Result: CONDITIONAL PASS** — errors are attributable to the pre-existing harness defect class (now fixed), not A1 scope. Full GREEN collection expected on CI re-run after main merge.

### QP-7: No `Optional` NameError remains

Evidence `03_DIRECT_IMPORTS.txt` shows all four modules import with EXIT_CODE: 0. No `Optional` NameError in post-repair P1 run.

**Result: PASS**

### QP-8: Remaining P1 failures map only to frozen UTC debt

The continuation evidence (`A1_VALIDATION_SUMMARY.md`, `05_P1_EXECUTION.txt`) confirms remaining failures after A1 repair are exclusively attributable to the separately frozen `UTC` import defect class (A2-R), not to any A1 regression.

**Result: PASS**

### QP-9: No test, marker, discovery, dependency or workflow mutation

Diff inspection confirms: no changes to `tests/`, `pytest.ini` (pre-#1241), `conftest.py`, `requirements*.txt` (pre-#1241), `.github/workflows/`, or any agent-contract or governance artifact by the builder.

**Result: PASS**

### QP-10: Evidence package complete, unedited and reproducible

All 10 required evidence artifacts present:
- `01_PRE_REPAIR_OPTIONAL_REPRODUCTION.txt` ✅
- `02_COMPILEALL.txt` ✅
- `03_DIRECT_IMPORTS.txt` ✅
- `04_P1_COLLECTION.txt` ✅
- `05_P1_EXECUTION.txt` ✅
- `06_ANTI_DODGING_SCAN.txt` ✅
- `07_CHANGED_FILES.txt` ✅
- `A1_VALIDATION_SUMMARY.md` ✅
- `API_BUILDER_PHASE1_ATTESTATION.md` ✅
- `PREHANDOVER_PROOF_A1_1237.md` ✅

Evidence includes exact commands, runtime versions (Python 3.12.3), timestamps, exit codes.

**Result: PASS**

### QP-11: Changed-file inventory matches allowlist

Files changed: 4 domain `.py` files + evidence files in `qa/evidence/issue-1237/` + `PREHANDOVER_PROOF_A1_1237.md`. Merge commit adds harness fix from main (Foreman-authorized).

**Result: PASS**

### QP-12: All review conversations and exact-head gates resolved before handover

PR #1239 is currently DRAFT. CI gates must run on the updated head (`49e5afec`) after marking ready. This QP is produced ahead of that run; ECAP and IAA final assurance must follow CI confirmation.

**Result: PENDING CI — gates expected GREEN on re-run with harness fix included**

## QP Verdict

```
FOREMAN_QP_VERDICT: CONDITIONAL_PASS
Condition: CI gates must confirm GREEN on updated head 49e5afec after PR is marked ready for review.
Evidence quality: PASS
Scope discipline: PASS
Anti-dodging: PASS
Phase 1 sequencing: PASS
Production diff: PASS — 4 Optional import additions only
UTC isolation: PASS — no A2-R work
Merge authority: NOT GRANTED
Next step: Mark PR #1239 ready for review → CI runs → ECAP admin validation → IAA final assurance → CS2 merge
```

## Lifecycle blocks confirmed

- A2-T: BLOCKED
- A2-R: BLOCKED
- B1: BLOCKED
- PR #1232 Stage 6 qa-builder lane: OPEN / DRAFT / PARKED pending this merge
- Stage 6 acceptance: NO-GO
- Stages 7–10: BLOCKED
- Stage 11: NO-GO
- Stage 12: BLOCKED
- `integration-builder`: NOT APPOINTED
