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
| Target path | `foreman/domain/task.py` |
| Target blob | `6994d9713058afbb69805ccb1fb6f74ea6ba92bf` |
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

This pre-brief is scoped independently from implementation. It defines the evidence and assurance conditions that a later appointed builder must satisfy. It does not appoint the builder, perform the repair, accept A1, or grant merge authority.

### Exact qualifying task

Repair one import defect in `foreman/domain/task.py`:

```diff
-from typing import Any
+from typing import Any, Optional
```

No other semantic or formatting change is authorised.

The file also references `UTC` without importing it. That defect belongs exclusively to later A2-R and must remain unchanged in A1.

### Defect reproduction

Accepted-base source state:

```python
from typing import Any
...
def get_by_id(cls, task_id: str) -> Optional['Task']:
```

Canonical pre-repair command:

```bash
python -c "import foreman.domain.task"
```

Expected pre-repair outcome:

```text
NameError: name 'Optional' is not defined
```

The appointed builder must capture the unedited failure output before implementation.

### Write boundary

Permitted implementation and evidence paths only:

```text
foreman/domain/task.py
qa/evidence/issue-1237/**
PREHANDOVER_PROOF_A1_1237.md
```

The active pre-brief carrier itself is:

```text
.agent-admin/assurance/iaa-wave-record-amc-a1-optional-import-1237.md
```

No other file is authorised.

### Prohibited scope

- no `UTC` import or datetime repair;
- no test creation, editing, deletion, move, rename or marker change;
- no `pytest.ini`, `conftest.py`, workflow, dependency, lock-file, infrastructure or deployment change;
- no skip, xfail, ignore, deselection, assertion weakening or changed test discovery;
- no refactor of `Task`, `TaskState`, registry behaviour, timestamps or annotations beyond importing `Optional`;
- no A2-T, A2-R, B1 or PR #1232 synchronisation;
- no builder appointment until this pre-brief is reviewed and accepted.

### Expected QA scope

Mandatory commands after appointment:

```bash
python -m compileall -q foreman/domain/task.py
python -c "from foreman.domain.task import Task; assert Task.get_by_id('__a1_missing__') is None"
python -m pytest tests/ --collect-only -q -m wave0 --ignore=tests/amc/stage6
python -m pytest tests/ -v -m wave0 --ignore=tests/amc/stage6
rg -n "(pytest\.skip|xfail|TODO|FIXME|NotImplemented|from typing import)" foreman/domain/task.py qa/evidence/issue-1237 PREHANDOVER_PROOF_A1_1237.md
git diff --name-status 34b1af8feef4a7f8d0a93859c45f797e21507c84...HEAD
```

Required outcomes:

1. `foreman/domain/task.py` compiles.
2. Direct import and `Task.get_by_id` lookup complete without an `Optional` NameError.
3. P1 collection remains exactly the frozen 13-node B0 population.
4. P1 output contains zero `Optional` NameError occurrences.
5. Any remaining P1 failure is attributable only to the separately frozen missing-`UTC` A2-R defect.
6. Production diff is exactly the one-line `Optional` import addition.
7. No file outside the allowlist changes.

A1 does not claim or require full P1/P2 GREEN. Full baseline GREEN remains downstream of A2-T and A2-R.

### High-risk failure modes

- builder repairs `UTC` opportunistically and collapses A1/A2-R separation;
- builder modifies tests or markers to conceal remaining failures;
- direct import still fails after the nominal change;
- P1 node population drifts;
- a new failure class appears;
- production diff includes refactoring or formatting churn;
- accepted base, target blob or builder contract changes before appointment;
- evidence reports GREEN by excluding or reclassifying tests;
- PR #1232 is synchronised prematurely.

Each condition is a mandatory halt and escalation.

### Required builder evidence

```text
qa/evidence/issue-1237/01_PRE_REPAIR_OPTIONAL_REPRODUCTION.txt
qa/evidence/issue-1237/02_COMPILEALL.txt
qa/evidence/issue-1237/03_DIRECT_IMPORT_LOOKUP.txt
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

1. exact base, branch, target blob and builder-contract binding;
2. pre-repair reproduction genuinely fails on missing `Optional`;
3. production diff is limited to `Any, Optional` import addition;
4. zero `UTC` or unrelated changes;
5. direct import and lookup are GREEN;
6. P1 collection exactly matches the frozen B0 13-node manifest;
7. no `Optional` NameError remains;
8. remaining failures, if any, map only to frozen `UTC` debt;
9. no test, marker, discovery, dependency or workflow mutation;
10. evidence package is complete, unedited and reproducible;
11. changed-file inventory matches the allowlist;
12. all review conversations and exact-head gates are resolved before handover.

### ECAP applicability

ECAP is **REQUIRED** and administrative only. ECAP validates:

- issue, branch, accepted base and exact final head;
- builder identity and contract binding;
- changed-file inventory and allowlist;
- evidence filenames, timestamps, command presence and exit codes;
- Foreman QP and final IAA carrier completeness.

ECAP must not decide defect semantics, expand A1 scope, accept `UTC` work, declare Stage 6 complete or grant merge authority.

### Final independent IAA focus

Final IAA must evaluate the exact implementation head and independently confirm:

- one-line import-only repair;
- no `UTC` or cross-lane work;
- successful direct import and lookup;
- frozen P1 population integrity;
- zero `Optional` NameError;
- no test-debt concealment or weakening;
- complete Foreman QP and ECAP separation;
- exact-head workflow and review closure;
- retained lifecycle blocks for A2-T, A2-R, B1, PR #1232 and Stages 6–12.

A final IAA PASS may recommend only A1 merge. It may not appoint an integration builder, accept Stage 6, synchronise PR #1232, authorise B1 or progress Stages 7–12.

### Entry conditions for later appointment

A builder may be appointed only after all of the following are true:

1. Issue #1237 remains open with unchanged scope.
2. This wave record is merged and accepted.
3. Its exact final blob is bound in the appointment instruction.
4. The accepted base remains `34b1af8feef4a7f8d0a93859c45f797e21507c84`, or a new Foreman disposition rebases the lane explicitly.
5. Target blob remains `6994d9713058afbb69805ccb1fb6f74ea6ba92bf`.
6. Proposed builder contract remains blob `f5d6c7789134600592343bd0fab0dc68d7d6fa30`.
7. CS2 explicitly authorises the bounded appointment.

### Disposition

```text
IAA preflight brief: PREFLIGHT_BRIEF_COMPLETE
A1 scope: BOUNDED
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
