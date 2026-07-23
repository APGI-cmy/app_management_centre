# AMC W1 Executable QA-to-Red Gap Analysis

## Verdict

The applicable pre-appointment RED obligations are now mapped to their canonical
Stage 6 meanings and separated from later GREEN implementation ownership. They
are not executable and have no observed intended-RED run evidence. This is a
real prerequisite gap, not test debt that may be silently deferred past the
`integration-builder` appointment.

## Traceability correction

IAA finding `IAA-1229-B1-TRACE-001` identified that the earlier W1 map attached
the wrong meanings to six canonical IDs. The corrected source of truth is:

| ID | Canonical Stage 6 meaning |
|---|---|
| `QA-DEPLOY-002` | Protected Production environment |
| `QA-DEPLOY-003` | Production secret isolation |
| `QA-DEPLOY-004` | Migration command freeze |
| `QA-DEPLOY-006` | `.env.example` coverage |
| `QA-DEPLOY-007` | Runtime health/smoke evidence |
| `QA-DEPLOY-010` | No placeholder evidence |

The corrected W1 map also enumerates exact `QA-CONFIG` and `QA-DES` IDs rather
than leaving the families ambiguous.

## Exact pre-appointment inventory

| ID / family | Intended RED focus | Lifecycle class |
|---|---|---|
| `QA-DEPLOY-001` | Missing required workflow family | Cross-wave guard. W1 owns `ci.yml` and `deploy-frontend.yml`; `db-migrate.yml` remains W7. |
| `QA-DEPLOY-002` | Existing Production job is not protected | W1 for frontend deployment; W7 for migration. |
| `QA-DEPLOY-003` | PR/staging can access Production secrets | W1. |
| `QA-DEPLOY-004` | Migration command differs from the approved stateless command | Cross-wave guard created early; W7 GREEN owner. |
| `QA-DEPLOY-006` | Required variable absent from `.env.example` | W1. |
| `QA-DEPLOY-007` | Health/smoke evidence absent | Cross-wave evidence guard created early; W7 GREEN owner. |
| `QA-DEPLOY-010` | Placeholder accepted as proof | W1 and ongoing. |
| `QA-CONFIG-001/002/003` | Missing required configuration is accepted or not named | W1. |
| `QA-DES001-001`, `QA-DES002-001`, `QA-DES003-001`, `QA-DES006-001`, `QA-DES007-001`, `QA-DES008-001` | Frontend ownership, hosted runner, no self-hosted runner, no frontend DB mutation, protected frontend Production, fail-fast config | W1. |
| `QA-DES001-002`, `QA-DES004-001`, `QA-DES005-001` | Migration ownership, exact command and manual-only trigger | Cross-wave guards created early; W7 GREEN owner. |

## W1/W7 reconciliation

Stage 8 makes `db-migrate.yml`, migration execution/rollback and health/smoke
GREEN evidence W7 outputs. Issue #1222 does not move them into W1. It requires
the bounded QA-builder lane to create their correctly targeted executable RED
guards before the integration builder is appointed. Those guards may remain RED
through W1 for an absent W7 target and must not be used to fail W1 exit or force
the W1 builder to implement W7 work.

## Lifecycle conflict

The original Stage 6 pack states that actual test code is a Stage 12 qa-builder
responsibility. Issue #1222 establishes a later and narrower sequencing
requirement: executable intended-RED proof must exist before
`integration-builder` appointment. The safe reconciliation is a bounded Stage
11 QA-builder appointment before the integration builder—not a waiver and not
Foreman-authored tests.

## Proposed QA-builder work package

Proposed Issue #1226 must receive explicit CS2 authorization, carry a canonical
IAA pre-brief, appoint a QA builder only for executable RED creation, prohibit
workflow/runtime implementation, capture reproducible intended-RED evidence for
each exact row above, distinguish W1 GREEN obligations from W7 cross-wave RED
guards, obtain QP/ECAP/IAA, and return to CS2 before any
`integration-builder` appointment.

## Anti-dodging controls

No skip, todo, stub-only, trivial-pass, test deletion, weakening,
renaming-around, mocking-away, hidden deferral, Production access, or
reclassification of W7 implementation into W1 is permitted.
