# Builder Appointment — Stage 11

**Stage**: 11 — Builder Appointment  
**Module**: App Management Centre (AMC)  
**Wave**: W1 — Runtime Foundation and Environment Setup  
**Builder**: `integration-builder`  
**Builder Class**: Integration Builder  
**Governing Issue**: #1223  
**Governing PR**: #1224  
**Status**: 🟠 APPOINTMENT PACKAGE COMPLETE — BLOCKED PENDING BUILDER ACKNOWLEDGMENT  
**Intended Post-Acceptance State**: `APPOINTED — AWAITING STAGE 12 AUTHORIZATION`

---

## 1. Appointment Authority

CS2 has authorized the Foreman to prepare the formal W1 appointment of `integration-builder`.

The appointment becomes constitutionally complete only when all of the following are true:

1. the Stage 11 appointment package is complete;
2. the builder has supplied the explicit Stage 11 acknowledgment required by the FM Builder Appointment Protocol;
3. independent assurance confirms the appointment package and acknowledgment;
4. PR #1224 is merged and accepted by CS2.

This Stage 11 package does **not** authorize implementation. No W1 execution may begin until a separate Stage 12 issue explicitly grants Build-to-Green authority.

## 2. Binding Sources

- `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md`
- `governance/canon/FM_BUILDER_APPOINTMENT_PROTOCOL.md`
- `governance/templates/FM_BUILDER_APPOINTMENT_INSTRUCTION.template.md`
- `governance/ROLE_APPOINTMENT_PROTOCOL.md`
- `.github/agents/integration-builder.md`
- `modules/amc/07-implementation-plan/implementation-plan.md`
- `modules/amc/07-implementation-plan/wave-breakdown.md`
- `modules/amc/07-implementation-plan/condition-import-matrix.md`
- `modules/amc/08-builder-checklist/executions/w1/integration-builder-readiness-checklist.md`
- `modules/amc/08-builder-checklist/executions/w1/w1-red-test-and-evidence-map.md`
- `.agent-admin/assurance/iaa-wave-record-amc-w1-runtime-foundation.md`

## 3. Appointment Instruction

APPOINTMENT: INTEGRATION-BUILDER

Role: Integration Builder  
Task ID: AMC-W1-RUNTIME-FOUNDATION  
Build Wave: W1

BUILD TO GREEN

Architecture Reference: `/modules/amc/04-architecture/architecture-specification.md`  
QA Suite Location: `/modules/amc/08-builder-checklist/executions/w1/w1-red-test-and-evidence-map.md`  
QA Current Status: RED — 9 mapped W1 obligations unresolved: 7 named QA-DEPLOY controls plus applicable QA-CONFIG and QA-DES controls  
RED Count Verification: Foreman verified the nine rows in the W1 RED-Test and Evidence Map on 2026-07-23  
Acceptance Criteria: All 9 mapped W1 obligations and every applicable repository gate must pass at 100%; zero test debt and zero warnings

The nine W1 RED obligations are:

1. `QA-DEPLOY-001`
2. `QA-DEPLOY-002`
3. `QA-DEPLOY-003`
4. `QA-DEPLOY-004`
5. `QA-DEPLOY-006`
6. `QA-DEPLOY-007`
7. `QA-DEPLOY-010`
8. applicable QA-CONFIG controls
9. applicable QA-DES controls

## 4. Scope Boundaries

### What is in scope after Stage 12 authorization

- Implement `.github/workflows/ci.yml`.
- Implement `.github/workflows/deploy-frontend.yml`.
- Validate or update root `.env.example` without secret values.
- Prove CI/type/lint/test/schema enforcement.
- Prove Vercel Preview uses the approved non-production Supabase `develop` resource.
- Prove Production credentials are unavailable to PR and Preview jobs.
- Prove no PR or Preview path can deploy to or mutate Production.
- Produce W1 RED-to-GREEN and PREHANDOVER_PROOF evidence in the exact Stage 12 evidence surfaces.
- Update the approved tracker and artifact index during the later Stage 12 handover.

### What is not in scope

- `db-migrate.yml`, which remains W7 scope.
- Database schema changes or Production migrations.
- Direct Production deployment or configuration mutation.
- Architecture, FRS, TRS, QA, PBFAG, or governance redesign.
- Test removal, weakening, bypass, dilution, or debt.
- Work belonging to W2–W8 except preserving the approved cross-wave mappings.
- Any implementation before separate Stage 12 authorization.

## 5. Cross-Wave Mapping

- `ci.yml` is introduced in W1 and remains subject to W8 consolidation and validation.
- `deploy-frontend.yml` is introduced in W1 and remains subject to W7 deployment-execution validation.
- `db-migrate.yml` remains a W7 output.

## 6. Constitutional Onboarding

The builder is explicitly bound to:

1. OPOJD continuous execution during an authorized build cycle.
2. Terminal states only: `BLOCKED` or `COMPLETE`.
3. One-Time Build Law and first-delivery completeness.
4. 100% QA GREEN, zero test debt, and zero-warning discipline.
5. Architecture-as-Law and active Design Freeze.
6. Execution Bootstrap Protocol and PREHANDOVER_PROOF.
7. Immediate STOP and escalation when authority, architecture, environment, credentials, scope, or evidence is ambiguous.
8. Foreman supervision and independent IAA review.

## 7. Ripple Intelligence Alignment Confirmation

Governance Canon Version: `1.0.0` from `governance/alignment/canonical_sync_status.json`  
Last Canonical Sync: `2026-01-02T10:40:00Z`  
Verification Date: `2026-07-23`  
Sync Status: `ALIGNED`  
Ripple Status: `STABLE`  
Active Builder Contract: `.github/agents/integration-builder.md` v3.4.0  
Alignment Registry Entry: updated to v3.4.0 in PR #1224  
Canonical Authorities Current: YES

Confirmation Statement:

- [x] Builder agent contract reflects current Ripple Intelligence obligations.
- [x] Builder scope is explicitly bound to `APGI-cmy/app_management_centre`.
- [x] Governance sync status is `ALIGNED`.
- [x] Ripple status is `STABLE` with no active or pending ripple.
- [x] No ripple ambiguity remains after the v3.4.0 alignment-registry correction.
- [x] Appointment preparation may proceed with governance-current context.

FM declares: Ripple Intelligence Alignment = CONFIRMED.

## 8. Builder Acknowledgment

The Stage 9 candidate attestation confirms readiness but does not substitute for the mandatory Stage 11 constitutional acknowledgment.

The exact acknowledgment request and response carrier is:

```text
modules/amc/10-builder-appointment/integration-builder-stage11-acknowledgment.md
```

Current acknowledgment status: `PENDING CANDIDATE RESPONSE`.

Until the candidate supplies the explicit response in that carrier, Stage 11 remains incomplete and PR #1224 must not be treated as merge-ready.

## 9. Stop and Escalation Conditions

The builder must STOP and report `BLOCKED` when:

- architecture or QA authority is missing, inconsistent, or ambiguous;
- required access or environment binding is unavailable;
- Production credentials or mutation paths appear in PR/Preview scope;
- work requires paths or capabilities outside W1;
- any gate or RED obligation fails;
- a secret may have been exposed;
- execution complexity exceeds practical capability;
- evidence cannot be reproduced.

Escalation must state: category, severity, trigger, canonical references, context, resolution options, and recommended safe next action.

## 10. Supervision

The Foreman retains non-delegable responsibility for scope control, active supervision, intervention, quality validation, review closure, gate verification, and handover to IAA.

## 11. Appointment Boundary

Only after builder acknowledgment, independent assurance, merge, and CS2 acceptance may the state become:

```text
Builder state: APPOINTED — AWAITING STAGE 12 AUTHORIZATION
Implementation authorized: false
Stage 12 status: BLOCKED
```

No “begin execution” instruction is issued in Stage 11. Execution-grant language is deferred to the separate Stage 12 authorization so the canonical 12-stage sequence remains intact.
