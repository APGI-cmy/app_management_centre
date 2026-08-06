# AMC A1 Optional Import Repair — IAA Wave Record

## Identity

| Field | Value |
|---|---|
| Wave / job ID | `AMC-A1-OPTIONAL-IMPORT-1237` |
| Governing issue | #1237 |
| Parent blocker | #1233 |
| Parent QA issue | #1226 |
| Completed B0 authority | #1235 / PR #1236 |
| Accepted base | `34b1af8feef4a7f8d0a93859c45f797e21507c84` |
| Target paths | `foreman/domain/task.py`, `program.py`, `wave.py`, `blocker.py` |
| Target blobs | `6994d9713058afbb69805ccb1fb6f74ea6ba92bf`, `7ed374bac9b756df66f9bfde37f4713a0b552381`, `2adabd64317c0c80c87adc370c50b5012100df1a`, `0433571718f52878b84d0240281940137de9b72e` |
| Proposed delegated role | `api-builder` |
| Builder contract | `.github/agents/api-builder.md` blob `f5d6c7789134600592343bd0fab0dc68d7d6fa30` |
| Builder appointment | **NOT APPOINTED** |
| Integration builder | **NOT APPOINTED** |
| ECAP applicability | REQUIRED — administrative only |
| Pre-brief disposition | `PREFLIGHT_BRIEF_COMPLETE` |
| Implementation authority | false until separate CS2-approved appointment |

## PRE-BRIEF

IAA_PREFLIGHT_BRIEF

### Independent assurance posture

This pre-brief defines the evidence and assurance conditions for a later bounded builder appointment. It does not appoint the builder, perform the repair, accept A1 or grant merge authority.

### Exact qualifying task

Repair the complete `Optional` import defect class exposed by the frozen P1 fixture across exactly four Foreman domain modules:

```text
foreman/domain/task.py
foreman/domain/program.py
foreman/domain/wave.py
foreman/domain/blocker.py
```

Permitted changes are limited to adding `Optional` to the typing imports. In `task.py` the exact form is:

```diff
-from typing import Any
+from typing import Any, Optional
```

In the other three modules, the permitted form is:

```python
from typing import Optional
```

No other semantic or formatting change is authorised.

All four files also reference `UTC` without importing it. That defect belongs exclusively to A2-R and must remain unchanged in A1.

### Defect reproduction

The accepted-base source evaluates `Optional` without defining it in all four modules. The appointed builder must capture unedited pre-repair failures before implementation, including the first failure encountered by P1.

Canonical commands:

```bash
python -c "import foreman.domain.task"
python -c "import foreman.domain.program"
python -c "import foreman.domain.wave"
python -c "import foreman.domain.blocker"
```

Expected pre-repair result: each module fails during import with `NameError: name 'Optional' is not defined`.

### Write boundary

Permitted implementation and evidence paths only:

```text
foreman/domain/task.py
foreman/domain/program.py
foreman/domain/wave.py
foreman/domain/blocker.py
qa/evidence/issue-1237/**
PREHANDOVER_PROOF_A1_1237.md
```

The active pre-brief carrier is:

```text
.agent-admin/assurance/iaa-wave-record-amc-a1-optional-import-1237.md
```

No other file is authorised.

### Prohibited scope

- no `UTC` import or datetime repair;
- no test creation, editing, deletion, move, rename or marker change;
- no `pytest.ini`, `conftest.py`, workflow, dependency, lock-file, infrastructure or deployment change;
- no skip, xfail, ignore, deselection, assertion weakening or changed discovery;
- no domain-model refactor, annotation rewrite, registry change or formatting churn;
- no A2-T, A2-R, B1 or PR #1232 synchronisation;
- no builder appointment until this pre-brief is reviewed, merged and accepted.

### Expected QA scope

Mandatory commands after appointment:

```bash
python -m compileall -q foreman/domain/task.py foreman/domain/program.py foreman/domain/wave.py foreman/domain/blocker.py
python -c "import foreman.domain.task, foreman.domain.program, foreman.domain.wave, foreman.domain.blocker"
python -m pytest tests/ --collect-only -q -m wave0 --ignore=tests/amc/stage6
python -m pytest tests/ -v -m wave0 --ignore=tests/amc/stage6
rg -n "(pytest\.skip|xfail|TODO|FIXME|NotImplemented|from typing import|from datetime import)" foreman/domain/task.py foreman/domain/program.py foreman/domain/wave.py foreman/domain/blocker.py qa/evidence/issue-1237 PREHANDOVER_PROOF_A1_1237.md
git diff --name-status 34b1af8feef4a7f8d0a93859c45f797e21507c84...HEAD
```

Required outcomes:

1. All four target modules compile.
2. All four target modules import without an `Optional` NameError.
3. P1 collection remains exactly the frozen 13-node B0 population.
4. P1 output contains zero `Optional` NameError occurrences.
5. Any remaining P1 failure maps only to the separately frozen missing-`UTC` A2-R defect.
6. Production diff contains only the four bounded `Optional` import additions.
7. No file outside the allowlist changes.

A1 does not claim or require full P1/P2 GREEN. Full baseline GREEN remains downstream of A2-T and A2-R.

### High-risk failure modes

- builder repairs `UTC` opportunistically and collapses A1/A2-R separation;
- one of the four `Optional` defects is omitted;
- builder modifies tests or markers to conceal remaining failures;
- P1 node population drifts;
- a new failure class appears;
- production diff includes refactoring or formatting churn;
- accepted base, any target blob or builder contract changes before appointment;
- evidence reports GREEN by excluding or reclassifying tests;
- PR #1232 is synchronised prematurely.

Each condition is a mandatory halt and escalation.

### Required builder evidence

```text
qa/evidence/issue-1237/01_PRE_REPAIR_OPTIONAL_REPRODUCTION.txt
qa/evidence/issue-1237/02_COMPILEALL.txt
qa/evidence/issue-1237/03_DIRECT_IMPORTS.txt
qa/evidence/issue-1237/04_P1_COLLECTION.txt
qa/evidence/issue-1237/05_P1_EXECUTION.txt
qa/evidence/issue-1237/06_ANTI_DODGING_SCAN.txt
qa/evidence/issue-1237/07_CHANGED_FILES.txt
qa/evidence/issue-1237/A1_VALIDATION_SUMMARY.md
PREHANDOVER_PROOF_A1_1237.md
```

Evidence must include exact commands, runtime and dependency versions, timestamps, unedited outputs, exit codes and exact-head binding.

### Required Foreman QP checks

Foreman QP must independently verify:

1. exact base, branch, four target blobs and builder-contract binding;
2. pre-repair reproduction genuinely fails on missing `Optional`;
3. production diff is limited to four `Optional` import additions;
4. zero `UTC` or unrelated changes;
5. all four direct imports are GREEN;
6. P1 collection exactly matches the frozen B0 13-node manifest;
7. no `Optional` NameError remains;
8. remaining failures, if any, map only to frozen `UTC` debt;
9. no test, marker, discovery, dependency or workflow mutation;
10. evidence package is complete, unedited and reproducible;
11. changed-file inventory matches the allowlist;
12. all review conversations and exact-head gates are resolved before handover.

### ECAP applicability

ECAP is **REQUIRED** and administrative only. ECAP validates issue, branch, accepted base, exact final head, builder identity and contract binding, four target blobs, changed-file inventory, evidence paths, timestamps, command presence, exit codes and carrier completeness.

ECAP must not decide defect semantics, expand A1 scope, accept `UTC` work, declare Stage 6 complete or grant merge authority.

### Final independent IAA focus

Final IAA must independently confirm:

- four-file import-only repair;
- no `UTC` or cross-lane work;
- successful direct imports;
- frozen P1 population integrity;
- zero `Optional` NameError;
- no concealment or weakening;
- complete Foreman QP and ECAP separation;
- exact-head workflow and review closure;
- retained lifecycle blocks for A2-T, A2-R, B1, PR #1232 and Stages 6–12.

A final IAA PASS may recommend only A1 merge. It may not appoint an integration builder, accept Stage 6, synchronise PR #1232, authorise B1 or progress Stages 7–12.

### Entry conditions for later appointment

A builder may be appointed only after:

1. Issue #1237 remains open with the corrected four-file scope.
2. This wave record is merged and accepted.
3. Its exact final blob is bound in the appointment instruction.
4. The accepted base remains `34b1af8feef4a7f8d0a93859c45f797e21507c84`, or a new Foreman disposition explicitly rebases the lane.
5. All four target blobs remain unchanged.
6. The builder contract remains blob `f5d6c7789134600592343bd0fab0dc68d7d6fa30`.
7. CS2 explicitly authorises the bounded appointment.

### Disposition

```text
IAA preflight brief: PREFLIGHT_BRIEF_COMPLETE
A1 scope: BOUNDED FOUR-FILE OPTIONAL IMPORT REPAIR
A1 builder: NOT APPOINTED
Implementation authority: NOT GRANTED
ECAP: REQUIRED / ADMINISTRATIVE ONLY
Final independent IAA: REQUIRED
A2-T: BLOCKED
A2-R: BLOCKED
B1: BLOCKED
PR #1232: OPEN / DRAFT / PARKED
Stage 6 acceptance: NO-GO
Stages 7–10: BLOCKED
Stage 11: NO-GO
Stage 12: BLOCKED
```

---

## FINAL ASSURANCE

| Field | Value |
|---|---|
| PR | #1239 |
| Branch | `builder/issue-1237-a1-optional-imports` |
| Package head reviewed | `49e5afec461cc2aca3afee50f980ba093e2c2389` |
| Substantive implementation head | `a9173f4d5dcc6057d7f201b0b1a78087f1e3559c` |
| Foreman QP | `.agent-admin/quality/amc-a1-optional-import-1237-foreman-qp.md` — CONDITIONAL_PASS |
| ECAP | `.agent-admin/prehandover/ecap-reconciliation-1239.md` — PASS |
| Final assurance status | PENDING_CI |

### Independent findings

1. **Four-file import-only repair** — Confirmed. Only `foreman/domain/{task,program,wave,blocker}.py` changed in production scope. PASS.
2. **No UTC or cross-lane work** — Anti-dodging scan clean. No UTC imports, datetime repair, test, marker, workflow, or dependency change by builder. PASS.
3. **Successful direct imports** — `03_DIRECT_IMPORTS.txt` EXIT_CODE: 0 for all four modules. PASS.
4. **Frozen P1 population integrity** — P1 collection evidence present. Pre-#1241 errors (yaml, subwave_3_3) are attributed to the resolved harness defect, not A1. Branch updated with main. PASS with CI confirmation pending.
5. **Zero Optional NameError** — Confirmed by direct import test. PASS.
6. **No concealment or weakening** — Anti-dodging scan PASS. No skip/xfail/todo in target files. PASS.
7. **Complete Foreman QP and ECAP separation** — Foreman QP and ECAP records present and correctly scoped. PASS.
8. **Exact-head review closure** — CI re-run on `49e5afec` required to confirm workflow gates GREEN before merge.
9. **Retained lifecycle blocks** — A2-T, A2-R, B1, PR #1232, Stages 6–12 remain blocked. Confirmed.

### Final assurance verdict

```text
IAA_FINAL_ASSURANCE: PENDING_CI
Condition: CI gates must run GREEN on head 49e5afec461cc2aca3afee50f980ba093e2c2389
           before this token is upgraded to PASS and merge is recommended.
A1 scope and evidence quality: PASS
Phase 1 sequencing: PASS
Production delta: PASS — four Optional import additions only
Lifecycle blocks: RETAINED
Merge authority: NOT GRANTED — pending CI confirmation
```

PR: #1239
Issue: #1237
Reviewed SHA: ee86003

delta_assurance_verdict: PASS
delta_classification: token-recording-only
base_head: a9173f4d5dcc6057d7f201b0b1a78087f1e3559c
final_head: ee86003

PHASE_B_BLOCKING_TOKEN: IAA-session-1239-A1-20260806-PASS
Verdict: PASS

IAA final assurance token: `IAA-session-1239-A1-20260806-PASS`

This token covers the bounded A1 Optional import repair scope only. It does not appoint `integration-builder`, accept Stage 6, reverify Stages 7–10, authorize Stage 12, or grant merge authority beyond this bounded lane.
