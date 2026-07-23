# AMC W1 Executable QA-to-Red Gap Analysis

## Verdict

The W1 RED obligations are specified and mapped, but they are not executable and have no observed intended-RED run evidence. This is a real prerequisite gap, not test debt that may be deferred past the `integration-builder` appointment.

## Exact W1 inventory

| ID / family | W1 failure focus | Pre-integration-builder evidence required |
|---|---|---|
| `QA-DEPLOY-001` | Required workflow family missing | Executable static/config test fails because required W1 workflow path is absent |
| `QA-DEPLOY-002` | Production action not protected/manual | Executable test detects missing protected-production contract |
| `QA-DEPLOY-003` | Production secrets visible to PR/staging | Executable policy test proves current unmet/isolation state without reading values |
| `QA-DEPLOY-004` | Migration command drift | Executable static test enforces the approved command contract; W7 implementation remains out of W1 |
| `QA-DEPLOY-006` | Required variable absent from `.env.example` | Executable configuration-contract test |
| `QA-DEPLOY-007` | Missing health/smoke validation | Executable evidence-contract test fails on absent W1 proof |
| `QA-DEPLOY-010` | Placeholder counted as proof | Executable placeholder/stub evidence rejection |
| Applicable `QA-CONFIG` | Runtime and environment configuration | Executable required-variable and no-secret tests |
| Applicable `QA-DES` | Stage 5a execution design | Executable trigger, ownership and environment-boundary tests |

## Lifecycle conflict

The original Stage 6 pack states that actual test code is a Stage 12 qa-builder responsibility. Issue #1222 establishes a later and narrower sequencing requirement: executable intended-RED proof must exist before `integration-builder` appointment. The safe reconciliation is a bounded Stage 11 QA-builder appointment before the integration builder—not a waiver and not Foreman-authored tests.

## Proposed QA-builder work package

Proposed Issue #1226 must receive explicit CS2 authorization, carry a canonical IAA pre-brief, appoint a QA builder only for executable W1 RED creation, prohibit workflow/runtime implementation, capture reproducible intended-RED evidence, obtain QP/ECAP/IAA, and return to CS2 before any `integration-builder` appointment.

## Anti-dodging controls

No skip, todo, stub-only, trivial-pass, test deletion, weakening, renaming-around, mocking-away, hidden deferral or Production access is permitted.
