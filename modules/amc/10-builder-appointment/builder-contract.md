# Builder Contract — Stage 11

**Stage**: 11 — Builder Appointment  
**Module**: App Management Centre (AMC)  
**Wave**: W1 — Runtime Foundation and Environment Setup  
**Builder**: `integration-builder`  
**Source Contract**: `.github/agents/integration-builder.md`  
**Governing Issue**: #1223  
**Status**: 🟡 PROPOSED W1 CONTRACT OVERLAY — binding after merge and CS2 acceptance

---

## 1. Contract Purpose

This W1 overlay narrows the existing `integration-builder` contract to the exact AMC W1 appointment. It supplements but does not replace the canonical builder contract.

## 2. Authority and Execution State

The builder is appointed for W1 only. After Stage 11 acceptance its state is:

```text
APPOINTED — AWAITING STAGE 12 AUTHORIZATION
```

The builder has no authority to execute, modify implementation files, run migrations, deploy, or change infrastructure until a separate Stage 12 authorization is issued.

## 3. Allowed W1 Paths After Stage 12 Authorization

- `.github/workflows/ci.yml`
- `.github/workflows/deploy-frontend.yml`
- `.env.example`
- approved W1 test/evidence paths
- `modules/amc/11-build/` evidence surfaces
- `modules/amc/BUILD_PROGRESS_TRACKER.md`
- `modules/amc/AMC_PRE_BUILD_ARTIFACT_INDEX.md`
- PR administration and evidence files required by repository gates

Any other path requires explicit Foreman confirmation or escalation before modification.

## 4. Restricted and Prohibited Paths/Actions

The builder must not:

- create or modify `db-migrate.yml` in W1;
- alter Supabase schemas or run Production migrations;
- expose or consume Production credentials in PR/Preview execution;
- create a direct Production deployment path;
- change approved architecture, FRS, TRS, QA-to-Red, PBFAG, or governance canon;
- edit its own agent contract;
- remove, skip, mute, weaken, or reclassify tests or gates;
- accept warnings, flaky tests, deferred work, placeholders, stubs, or test debt;
- operate outside W1;
- merge its own PR;
- claim GREEN or completion without reproducible evidence and Foreman validation.

## 5. Build Philosophy Binding

The builder commits to:

- Architecture → QA-to-Red → Build-to-Green → Validation;
- One-Time Build Law;
- OPOJD continuous execution once Stage 12 begins;
- terminal states `BLOCKED` or `COMPLETE` only;
- 100% GREEN, zero test debt, zero warnings;
- CI as confirmatory, not diagnostic;
- stop-and-fix on every defect;
- PREHANDOVER_PROOF for executable artifacts.

## 6. W1 Deliverables After Stage 12 Authorization

1. `ci.yml` with explicit triggers, permissions, required checks, and non-production-safe behavior.
2. `deploy-frontend.yml` with Preview/staging posture and protected Production behavior.
3. Validated or updated `.env.example` containing names/placeholders only, never secret values.
4. CI/type/lint/test/schema evidence.
5. Preview deployment evidence.
6. Proof Preview binds to Supabase `develop`.
7. Proof Production credentials are unavailable to PR/Preview jobs.
8. Proof PR/Preview work cannot deploy or mutate Production.
9. No-Production-side-effect evidence.
10. W1 RED-to-GREEN traceability and PREHANDOVER_PROOF.

## 7. Cross-Wave Obligations

- `ci.yml` is introduced and proven in W1, then consolidated/validated in W8.
- `deploy-frontend.yml` is introduced and proven in W1, then deployment-execution validated in W7.
- `db-migrate.yml` is created only in W7.

## 8. Acceptance Criteria

W1 may be handed over only when:

- every applicable W1 RED obligation is GREEN;
- all required workflows and configuration surfaces exist and are executable;
- every required check is green on the final implementation head;
- Preview/non-production and Production boundaries are separately inspected;
- no secret value is exposed;
- no Production side effect occurred;
- no unresolved review conversation remains;
- no scope drift, test debt, warning debt, placeholder, or deferred item exists;
- evidence is complete, reproducible, and bound to the final head;
- Foreman quality control passes;
- independent IAA assurance passes.

## 9. STOP Conditions

The builder must immediately stop and escalate when:

- scope, architecture, QA, or governance is ambiguous;
- an allowed-path boundary would be exceeded;
- required credentials or environment bindings are unavailable;
- Production credentials or mutation routes are visible;
- any test or gate fails;
- secret exposure is suspected;
- execution cannot be completed to 100% GREEN;
- practical capability or platform limits are reached.

## 10. Escalation Format

Every `BLOCKED` escalation must include:

- Category
- Severity
- Trigger
- Canonical references
- Exact context/evidence
- Resolution options
- Recommended safe next action

## 11. Foreman and IAA Boundary

The builder produces implementation and evidence only. It does not perform Foreman QP, issue ECAP judgments, issue independent IAA findings, approve its own work, or release merge authority.

## 12. Stage 11 Acknowledgment Requirement

Before Stage 12 authorization, `integration-builder` must explicitly acknowledge each of the following:

1. OPOJD continuous execution.
2. `BLOCKED` or `COMPLETE` terminal states only.
3. One-Time Build Law and 100% GREEN.
4. Zero test debt and zero warnings.
5. STOP and escalation conditions.
6. Execution Bootstrap Protocol and PREHANDOVER_PROOF.
7. W1 scope and cross-wave boundaries.
8. No Production credentials, mutation, migration, or direct deployment.
9. No implementation before Stage 12 authorization.

## 13. Contract Disposition

This overlay becomes binding only when the Stage 11 PR is merged and accepted by CS2. Until then, the builder remains nominated/readiness-approved but not appointed.
