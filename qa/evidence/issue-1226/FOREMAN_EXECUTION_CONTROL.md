# Foreman Execution Control — Issue #1226 / PR #1232

## Authority

- Governing issue: #1226
- Active PR: #1232
- Accepted base: `1d93459509abb92467f91deb4eefb879c1497362`
- Active branch: `qa/issue-1226-stage6-executable-red-r2`
- Role: `qa-builder`
- Lifecycle lane: Stage 6 re-entry only
- Integration builder: NOT APPOINTED
- Stage 12 authority: false

## Execution sequence

1. The qa-builder's first commit must add only `qa/evidence/issue-1226/QA_BUILDER_PHASE1_ATTESTATION.md`.
2. No substantive QA file may precede that attestation commit.
3. Subsequent commits may change only:
   - `tests/amc/stage6/**`
   - `qa/evidence/issue-1226/**`
   - `PREHANDOVER_PROOF_QA_BUILDER_1226_20260724.md`
4. The executable target suite must run RED twice for the same intended canonical reasons.
5. Compile, collection, existing non-target regression tests and anti-dodging checks must remain GREEN.
6. PR #1232 remains draft until Foreman confirms the delivery package is complete.

## Required evidence commands

```bash
python -m compileall -q tests/amc/stage6
python -m pytest tests/amc/stage6 --collect-only -q
python -m pytest tests/amc/stage6 -vv
python -m pytest tests/amc/stage6 -vv
python -m pytest tests/ -v -m 'not wave0' --ignore=tests/amc/stage6
python -m pytest tests/ -v -m wave0 --ignore=tests/amc/stage6
rg -n "(\.skip|xfail|pytest\.skip|TODO|FIXME|pass[[:space:]]*#|NotImplemented)" tests/amc/stage6
git diff --name-status 1d93459509abb92467f91deb4eefb879c1497362...HEAD
```

## Stop conditions

Halt and report on any contract/blob mismatch, unexpected GREEN target, unrelated RED, regression failure, allowlist insufficiency, need to modify protected surfaces, credential or Production requirement, infrastructure mutation, W7 implementation pressure, or inability to reproduce the intended RED result.

## Foreman acceptance gates

The Foreman will not recommend readiness until all of the following are present and verified:

- valid Phase 1 attestation commit ordering;
- exact canonical test-ID coverage;
- two reproducible intended-RED executions;
- GREEN compile, collection and non-target regressions;
- no skip/todo/stub/xfail/trivial-pass or hidden exclusion;
- allowlist-only changed-file set;
- complete command logs and validation summary;
- complete PREHANDOVER proof;
- Foreman QP PASS;
- ECAP administrative validation;
- independent IAA PASS bound to the final exact head.
