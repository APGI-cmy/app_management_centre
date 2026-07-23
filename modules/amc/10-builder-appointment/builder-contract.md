# Builder Contract — Stage 11

**Stage**: 11 — Builder Appointment  
**Module**: App Management Centre (AMC)  
**Wave**: W1 — Runtime Foundation and Environment Setup  
**Builder**: `integration-builder`  
**Source Contract**: `.github/agents/integration-builder.md` v3.4.0  
**Governing Issue**: #1223  
**Governing PR**: #1224  
**Status**: 🟠 W1 CONTRACT OVERLAY COMPLETE — binding only after acknowledgment, merge and CS2 acceptance

---

## 1. Contract Purpose

This W1 overlay narrows the existing `integration-builder` contract to the exact AMC W1 appointment. It supplements but does not replace the canonical builder contract.

## 2. Authority and Execution State

The intended post-acceptance state is:

```text
APPOINTED — AWAITING STAGE 12 AUTHORIZATION
```

The builder has no authority to execute, modify implementation files, run migrations, deploy, or change infrastructure until a separate Stage 12 authorization is issued.

## 3. Exact Allowed W1 Paths After Stage 12 Authorization

The builder may modify only the following implementation and evidence paths unless the Foreman explicitly expands scope in the Stage 12 issue:

- `.github/workflows/ci.yml`
- `.github/workflows/deploy-frontend.yml`
- `.env.example`
- `modules/amc/11-build/build-evidence-index.md`
- `modules/amc/11-build/qa-to-green-evidence.md`
- `modules/amc/11-build/handover.md`
- `modules/amc/BUILD_PROGRESS_TRACKER.md`
- `modules/amc/AMC_PRE_BUILD_ARTIFACT_INDEX.md`
- `.admin/pr.json`
- `.agent-admin/prehandover/ecap-reconciliation-<stage12-pr>.md`
- `.agent-admin/wave-records/amc-wave-record-stage12-w1-<stage12-pr>.md`
- `.agent-workspace/independent-assurance-agent/memory/session-<stage12-pr>-<date>.md`

The builder may read but must not modify the following authority and test-definition paths:

- `modules/amc/00-app-description/`
- `modules/amc/01-ux-workflow-wiring-spec/`
- `modules/amc/02-frs/`
- `modules/amc/03-trs/`
- `modules/amc/04-architecture/`
- `modules/amc/05a-deployment-execution-strategy/`
- `modules/amc/05-qa-to-red/`
- `modules/amc/06-pbfag/`
- `modules/amc/07-implementation-plan/`
- `modules/amc/08-builder-checklist/`
- `modules/amc/09-iaa-pre-brief/`
- `modules/amc/10-builder-appointment/`
- `governance/`
- `.github/agents/`

Any path not expressly listed as writable is out of scope and requires STOP-and-escalate before modification.

## 4. Restricted and Prohibited Paths/Actions

The builder must not:

- create or modify `.github/workflows/db-migrate.yml` in W1;
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

- all nine mapped W1 RED obligations are GREEN;
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

The candidate-owned acknowledgment carrier is:

```text
modules/amc/10-builder-appointment/integration-builder-stage11-acknowledgment.md
```

Stage 11 cannot complete until the candidate explicitly acknowledges:

1. OPOJD continuous execution.
2. `BLOCKED` or `COMPLETE` terminal states only.
3. One-Time Build Law and 100% GREEN.
4. Zero test debt and zero warnings.
5. Architecture-as-Law and Design Freeze.
6. All nine mapped W1 RED obligations.
7. STOP and escalation conditions.
8. Execution Bootstrap Protocol and PREHANDOVER_PROOF.
9. The exact path allowlist and cross-wave boundaries.
10. No Production credentials, mutation, migration, direct deployment, or premature implementation.
11. Foreman supervision and independent IAA review.
12. No self-approval, self-merge, test weakening, or false GREEN claims.

## 13. Contract Disposition

This overlay becomes binding only when the acknowledgment is candidate-authored, independently verified, PR #1224 is merged, and CS2 accepts the Stage 11 appointment. Until then, the candidate remains readiness-approved but not constitutionally appointed.
