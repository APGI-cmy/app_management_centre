# AMC W1 Stage 6 Re-entry — QA Remediation IAA Pre-Brief

## Identity

| Field | Value |
|---|---|
| Governing issue | #1226 |
| Parent investigation | #1222 / PR #1229 |
| Lifecycle posture | Stage 6 re-entry under `PRE_BUILD_STAGE_MODEL_CANON.md` §4.4 |
| Proposed delegated role | `qa-builder` |
| Integration builder | NOT APPOINTED |
| Stage 12 authority | false |
| Infrastructure mutation | false |
| Status | PROPOSED PREFLIGHT BRIEF — PENDING INDEPENDENT IAA CONFIRMATION |

## Exact job

Create only the executable QA-to-Red tests and reproducible intended-RED evidence
specified in Issue #1226 and the corrected W1 RED/evidence map. Do not implement
the runtime, workflows, environment configuration, deployment, database objects,
or any Build-to-Green target.

### W1-targeted RED obligations

- `QA-DEPLOY-002/003/006/010`
- `QA-CONFIG-001/002/003`
- `QA-DES001-001`, `QA-DES002-001`, `QA-DES003-001`,
  `QA-DES006-001`, `QA-DES007-001`, `QA-DES008-001`
- W1 portions of `QA-DEPLOY-001` for `ci.yml` and
  `deploy-frontend.yml`

### Cross-wave guards created now, GREEN ownership retained in W7

- full-family `QA-DEPLOY-001` guard, with `db-migrate.yml` remaining W7;
- `QA-DEPLOY-004` migration-command freeze;
- `QA-DEPLOY-007` health/smoke evidence contract;
- `QA-DES001-002`, `QA-DES004-001`, `QA-DES005-001`.

An absent W7 target may be the intended RED reason. The QA role must not create
or implement that target.

## QA-to-Red success model

- The new target suite must execute and fail for the exact unmet, canonical
  reason recorded for each test ID.
- The test harness, syntax/type/lint checks, existing regression suite and
  anti-dodging validators must remain GREEN.
- Intended target RED is required QA-to-Red evidence, not accepted test debt.
  Any unrelated failure, unexpected pass, skipped/todo/stub test, warning,
  hidden exclusion or non-reproducible result is a blocker.
- The generic QA-builder Build-to-Green handover wording does not convert this
  bounded Stage 6 job into Build-to-Green authority.

## Mandatory entry controls

1. PR #1229 has zero unresolved review threads and exact-head required checks are
   GREEN.
2. This exact pre-brief receives independent IAA confirmation.
3. The Issue #1228 Work Mode fallback is CS2-approved and used when
   `agent_bootstrap` is not exposed.
4. The appointment instruction binds the exact issue, branch/base SHA, contract
   path/blob SHA, permitted files, prohibited surfaces and evidence commands.
5. The QA role attests Phase 1 before its first repository write.

## Required evidence

- exact test files and canonical test-ID mapping;
- command lines, dependency/runtime versions and unedited output;
- per-test intended failure reason and reproducibility result;
- proof existing regression/harness checks remain GREEN;
- zero skip/todo/stub/trivial-pass/hidden-exclusion evidence;
- changed-file scope proof;
- no credential, Production, deployment, migration or infrastructure access;
- Foreman QP, ECAP administrative validation where applicable, independent IAA
  result and CS2 acceptance package.

## Stop conditions

HALT and escalate on any contract/bootstrap mismatch, missing frozen source,
ambiguous test meaning, need to change a protected or prohibited surface,
unexpected GREEN target, unrelated RED regression, W7-to-W1 drift, credential
requirement, Production access, infrastructure mutation, or inability to
reproduce the intended failure.

## Exit and downstream reverification

Completion of this job may correct Stage 6 only. Foreman must then reverify:

1. Stage 7 PBFAG against the executable intended-RED evidence;
2. Stage 8 implementation-plan and W1/W7 ownership alignment;
3. Stage 9 candidate readiness and controls;
4. Stage 10 IAA pre-brief against the corrected Stage 6–9 chain.

Only after those reverifications and CS2 acceptance may Stage 11
`integration-builder` appointment be reconsidered. Stage 12 remains blocked.
