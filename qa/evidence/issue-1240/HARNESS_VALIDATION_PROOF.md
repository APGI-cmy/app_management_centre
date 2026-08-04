# Harness Validation Proof — Issue #1240 / PR #1241

## Bindings

- PR: `#1241`
- Issue: `#1240`
- Branch: `foreman/issue-1240-harness-yaml-marker`
- Substantive implementation head: `45d7f1ed44fb8a63425ef04de2768f658cb4c7f1`
- Accepted base: `ff5ec09024210789c2d2941a4aa6fe1ddb166515`
- A1 compatibility head: `cf6b276898d8e9d761f8c38f5c4ee421c1d5a122`
- Validation time: `2026-07-29T10:55:00Z`
- Merge authority: **NOT GRANTED**

## Authorised implementation

The substantive correction remains limited to:

- `requirements.txt`: add `PyYAML>=6.0`;
- `pytest.ini`: register `subwave_3_3: Subwave 3.3 Governance Dashboard V2 tests` while retaining `--strict-markers`.

## Exact-head harness proof

- Python 3.12.3, pytest 9.1.1 and PyYAML 6.0.3 were used in a clean virtual environment.
- `pip check` reported no broken requirements.
- `import yaml` exited `0` and printed `6.0.3`.
- The exact frozen collection command selected 13 P1 nodes and completed with zero collection errors.
- The previous YAML import and unregistered-marker failures were absent.
- Strict-marker enforcement remained active.

The PR #1241-only P1 execution encountered the pre-existing missing-`Optional` defect because PR #1239 is not part of this branch. This was classified separately and was not changed in Issue #1240.

## Isolated combined-state proof

A disposable worktree combined PR #1239 head `cf6b276898d8e9d761f8c38f5c4ee421c1d5a122` with only the two Issue #1240 harness deltas.

The combined state:

- selected the same 13 P1 nodes;
- completed collection with zero errors;
- showed no YAML import failure;
- showed no strict-marker failure;
- showed no `Optional` `NameError`;
- retained only the separately frozen missing-`UTC` A2-R defect across the 13 selected tests.

No combined branch was pushed. The disposable worktree and virtual environments were removed after evidence capture.

## Anti-dodging and scope result

- no tests changed;
- no application/runtime files changed;
- no `Optional` or `UTC` correction was made;
- no skip, xfail, alternate pytest configuration, `PYTEST_ADDOPTS`, assertion weakening, or collection narrowing was used;
- PR #1239 was not modified.

## Raw evidence

- `qa/evidence/issue-1240/01_ENVIRONMENT_SETUP.txt`
- `qa/evidence/issue-1240/02_YAML_IMPORT.txt`
- `qa/evidence/issue-1240/03_P1_COLLECTION_EXACT_HEAD.txt`
- `qa/evidence/issue-1240/04_P1_EXECUTION_EXACT_HEAD.txt`
- `qa/evidence/issue-1240/05_COMBINED_A1_HARNESS_COLLECTION.txt`
- `qa/evidence/issue-1240/06_COMBINED_A1_HARNESS_EXECUTION.txt`
- `qa/evidence/issue-1240/07_SCOPE_AND_ANTI_DODGING_SCAN.txt`
- `qa/evidence/issue-1240/08_CHANGED_FILES.txt`
- `qa/evidence/issue-1240/HARNESS_VALIDATION_SUMMARY.md`

## Validation disposition

The executable evidence supports Foreman QP review of the bounded harness correction. This record does not authorise merge, change the Stage 6 disposition, or expand the Issue #1240 scope.