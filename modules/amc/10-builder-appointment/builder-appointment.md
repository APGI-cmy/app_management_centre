# Builder Appointment — Stage 11

**Stage**: 11 — Builder Appointment  
**Module**: App Management Centre (AMC)  
**Wave**: W1 — Runtime Foundation and Environment Setup  
**Builder**: `integration-builder`  
**Builder Class**: Integration Builder  
**Governing Issue**: #1223  
**Status**: 🟡 APPOINTMENT PROPOSED — authoritative only after merge and CS2 acceptance  
**Execution State After Acceptance**: `APPOINTED — AWAITING STAGE 12 AUTHORIZATION`

---

## 1. Appointment Authority

The Foreman formally appoints `integration-builder` to W1 subject to merge and CS2 acceptance of the Stage 11 PR.

This appointment establishes constitutional role, scope, accountability, and operating constraints. It does **not** authorize implementation. The builder may not begin W1 execution until a separate Stage 12 issue explicitly grants Build-to-Green authority.

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
- `.agent-admin/assurance/iaa-wave-record-amc-w1-runtime-foundation.md`

## 3. Appointment Instruction

APPOINTMENT: INTEGRATION-BUILDER

Role: Integration Builder  
Task ID: AMC-W1-RUNTIME-FOUNDATION  
Build Wave: W1

BUILD TO GREEN

Architecture Reference: `modules/amc/04-architecture/architecture-specification.md`  
QA Authority: `modules/amc/05-qa-to-red/qa-to-red-specification.md` and W1 RED/evidence map  
QA Current Status: RED obligations defined; implementation proof not yet produced  
Acceptance Criteria: All applicable W1 QA and governance gates must pass at 100%

## 4. Scope Boundaries

### What is in scope after Stage 12 authorization

- Implement `.github/workflows/ci.yml`.
- Implement `.github/workflows/deploy-frontend.yml`.
- Validate or update root `.env.example` without secret values.
- Prove CI/type/lint/test/schema enforcement.
- Prove Vercel Preview uses the approved non-production Supabase `develop` resource.
- Prove Production credentials are unavailable to PR and Preview jobs.
- Prove no PR or Preview path can deploy to or mutate Production.
- Produce W1 RED-to-GREEN and PREHANDOVER_PROOF evidence.
- Update approved W1 evidence, tracker, and index surfaces as part of the later build handover.

### What is not in scope

- `db-migrate.yml`, which remains W7 scope.
- Database schema changes or Production migrations.
- Direct Production deployment or configuration mutation.
- Architecture, FRS, TRS, QA, or governance redesign.
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

## 7. Required Builder Acknowledgment

Before Stage 12 authority may be granted, the builder must explicitly acknowledge:

- OPOJD continuous execution;
- `BLOCKED` or `COMPLETE` terminal-state discipline;
- One-Time Build Law;
- 100% GREEN and zero test debt;
- all STOP and escalation conditions;
- Execution Bootstrap Protocol and PREHANDOVER_PROOF;
- the prohibition on Production credentials, Production mutation, and premature implementation.

The Stage 9 attestation supports readiness but does not replace this Stage 11 constitutional acknowledgment.

## 8. Stop and Escalation Conditions

The builder must STOP and report `BLOCKED` when:

- architecture or QA authority is missing, inconsistent, or ambiguous;
- required access or environment binding is unavailable;
- Production credentials or mutation paths appear in PR/Preview scope;
- work requires paths or capabilities outside W1;
- any gate or RED obligation fails;
- a secret may have been exposed;
- execution complexity exceeds practical capability;
- evidence cannot be reproduced.

Escalation must state: category, severity, trigger, canonical references, context, and resolution options.

## 9. Supervision

The Foreman retains non-delegable responsibility for scope control, active supervision, intervention, quality validation, review closure, gate verification, and handover to IAA.

## 10. Appointment Boundary

Upon merge and CS2 acceptance:

```text
Builder state: APPOINTED — AWAITING STAGE 12 AUTHORIZATION
Implementation authorized: false
Stage 12 status: BLOCKED
```

No “begin execution” instruction is issued in Stage 11. Execution-grant language from the generic appointment protocol is deferred to the separate Stage 12 authorization so the canonical 12-stage sequence remains intact.
