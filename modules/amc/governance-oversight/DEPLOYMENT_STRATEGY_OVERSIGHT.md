# AMC Deployment-Strategy Oversight Record & Governance Correction Definition

**Document ID**: AMC-GOV-OVERSIGHT-001  
**Type**: Governance Oversight Record + Corrective Governance Specification  
**Status**: ACTIVE — Defines Stage 5a (Deployment Execution Strategy) for AMC  
**Version**: 1.0  
**Date**: 2026-04-26  
**Authority**: CS2 (Johan Ras / @APGI-cmy)  
**CS2 Authorization**: app_management_centre#1133  
**Produced By**: foreman-v2-agent (session-033 — POLC_ORCHESTRATION)  
**Wave**: amc-governance-deployment-oversight-20260426  
**Mirrors**: maturion-isms#1468 (same class of oversight, applied to AMC)

---

## 1. Formal Oversight Declaration (Scope A)

### 1.1 The Gap

> **Oversight**: The AMC pre-build governance model captures the **target architecture** but does
> not yet sufficiently capture the **deployment execution strategy**.

The canonical 12-stage pre-build model (PRE_BUILD_STAGE_MODEL_CANON.md v1.0.0) defines the
following sequence:

> App Description → UX Workflow & Wiring Spec → FRS → TRS → Architecture → QA-to-Red → PBFAG
> → Implementation Plan → Builder Checklist → IAA Pre-Brief → Builder Appointment → Build

This sequence is sound for capturing **what** the system must do (FRS), **how it must work
technically** (TRS), and **what components it will have** (Architecture). However, it does not
contain a dedicated mandatory step that freezes the **deployment execution strategy** — the
operational "how" layer that governs:

- which deployment surface each workflow owns
- which automation is CI-safe vs preview-safe vs live-operational-only
- which actions require self-hosted runners or protected environments
- how database migrations are executed (Supabase CLI / direct `psql` / other)
- what requires manual CS2 approval before execution
- how environment and network assumptions are validated before build execution

### 1.2 Evidence of Gap

At the point this oversight was recorded, Stage 5 (Architecture) for AMC is being produced.
Stage 5 includes "deployment-shaping architectural decisions" (per the tracker) but these are
architectural in character (technology choice, component responsibility) — not operational deployment
execution rules (workflow ownership, runner restrictions, migration path, surface boundaries).

Without freezing the deployment execution strategy before build execution begins, later builders
face the same ambiguities that caused drift in analogous situations:

- Uncertainty about which CI workflow owns which deployment surface
- Uncertainty about whether GitHub-hosted runners may touch live infrastructure
- Uncertainty about whether frontend deploy workflows may perform live database mutations
- Uncertainty about the approved migration execution path
- Uncertainty about what is CI-safe, preview-safe, and live-operational-only
- Uncertainty about what must remain manual, protected, or self-hosted
- Uncertainty about how environment/network assumptions are validated

### 1.3 Formal Declaration

This document formally records that:

1. **Architecture/platform topology alone is insufficient** — a deployment execution strategy
   document is also required before build execution begins.

2. **Deployment execution strategy must be frozen before build execution** — the strategy must be
   a CS2-approved, committed artifact, not an informal assumption.

3. **Lack of this step causes downstream ambiguity and workflow drift** — this oversight is the
   root cause pattern of the deployment-surface conflicts identified in maturion-isms#1468 and
   must not be repeated in AMC.

4. **There is a single, discoverable place to find this oversight** — this document is that place.

---

## 2. Governance Correction Definition (Scope B)

### 2.1 New Stage: Stage 5a — Deployment Execution Strategy

A new mandatory stage is defined for AMC as **Stage 5a — Deployment Execution Strategy**,
placed between Stage 5 (Architecture) and Stage 6 (QA-to-Red).

**Placement rationale**:

- Stage 5a derives from Stage 5 (Architecture): the deployment execution strategy must be
  consistent with and informed by the approved architecture.
- Stage 5a must precede Stage 6 (QA-to-Red): the QA-to-Red suite must test the approved
  deployment model, not an assumed one. Without Stage 5a, QA-to-Red cannot adequately cover
  deployment-surface boundary violations.
- Stage 5a must precede Stage 7 (PBFAG): the PBFAG gate must verify that the deployment
  execution strategy exists, is complete, and is non-contradictory with Architecture.
- Stage 5a must precede Stage 8 (Implementation Plan): the Implementation Plan must reference
  the approved deployment execution strategy and may not substitute a different operational model.

**Classification**:

- AMC-local mandatory stage — defined in this document as an AMC-specific extension of the
  canonical 12-stage sequence.
- Pending formal adoption into PRE_BUILD_STAGE_MODEL_CANON.md (follow-on wave required).
- Until the canon is formally updated, Stage 5a is enforced via the AMC BUILD_PROGRESS_TRACKER.md
  and this oversight record.

**Stage definition**:

| Field | Value |
|-------|-------|
| Stage Number | 5a |
| Stage Name | Deployment Execution Strategy |
| Inputs | Stage 5 Architecture (approved) |
| Primary Output | `deployment-execution-strategy.md` — committed, CS2-approved artifact |
| Supporting Outputs | `deployment-surface-ownership-table.md`, `runner-and-environment-constraints.md` |
| Gate Condition | CS2-approved Deployment Execution Strategy committed to branch before Stage 6 begins |
| Failure Mode | QA-to-Red cannot test deployment boundaries; Implementation Plan may drift |
| Anti-Drift Rule | Any deviation from the approved deployment execution strategy requires a formal governance update — ad hoc operational model substitution in later build waves is prohibited |

### 2.2 Position in the AMC Stage Sequence

The AMC-local stage sequence, incorporating Stage 5a, is:

```
App Description (1)
  └─► UX Workflow & Wiring Spec (2)
        └─► FRS (3)
              └─► TRS (4)
                    └─► Architecture (5)
                          └─► Deployment Execution Strategy (5a)  ◄── NEW MANDATORY STAGE
                                └─► QA-to-Red (6)
                                      └─► PBFAG (7)
                                            └─► Implementation Plan (8) [must ref 5a]
                                                  └─► Builder Checklist (9)
                                                        └─► IAA Pre-Brief (10)
                                                              └─► Builder Appointment (11)
                                                                    └─► Build (12)
```

### 2.3 Stage 5a Entry Condition

Stage 5a may not begin until:

- [ ] Stage 5 (Architecture) is complete and **CS2-approved**
- [ ] The Architecture Specification (`modules/amc/04-architecture/architecture-specification.md`)
      is available as the canonical Stage 5 artifact

Stage 5a completion requires:

- [ ] `deployment-execution-strategy.md` produced, substantively populated, and CS2-approved
- [ ] All 8 mandatory content fields (§3.1 below) explicitly answered — no "TBD" permitted
- [ ] Deployment surface ownership table complete
- [ ] Runner and environment constraints table complete

---

## 3. Required Content Specification (Scope C)

### 3.1 Mandatory Fields

The `deployment-execution-strategy.md` artifact produced by Stage 5a **MUST** provide
explicit, non-deferrable answers to the following 8 mandatory fields:

| Field ID | Field Name | Required Answer |
|----------|-----------|-----------------|
| DES-001 | Workflow Surface Ownership | For each deployment surface (frontend deploy, backend deploy, DB migration, schema verification, live operational validation): which specific workflow or manual process owns execution? |
| DES-002 | GitHub-Hosted Runner Authorization | Are GitHub-hosted runners permitted to touch live infrastructure? If yes: which surfaces? If no: what surfaces require self-hosted runners? |
| DES-003 | Self-Hosted Runner Requirement | Which surfaces require self-hosted runners? What are the runner capability requirements? |
| DES-004 | Migration Execution Path | Are database migrations executed via Supabase CLI, direct `psql`, GitHub Action migration job, or another approved mechanism? Specify the exact approved path. |
| DES-005 | CI/Preview/Production Execution Boundaries | What runs on PRs? On preview deploys? On pushes to main? On manual workflow dispatches? On protected environments? |
| DES-006 | Safety Classification | Classify each workflow/surface as: CI-safe, preview-safe, or live-only. Frontend mutation workflows may not cross this boundary without explicit authorization. |
| DES-007 | Manual/Protected Approval Boundaries | What requires CS2 or manual human approval before execution? What is protected under GitHub protected environments? What may never be automated? |
| DES-008 | Environment/Network Assumption Validation | How are environment and network assumptions validated before build execution? What pre-flight checks are required? What fails safe if an assumption is invalid? |

### 3.2 Prohibitions

The following are explicitly prohibited in the `deployment-execution-strategy.md` artifact:

- **No TBD fields**: All 8 mandatory fields must be answered before CS2 approval. A TBD in any
  mandatory field is a blocking defect.
- **No internal inconsistency**: The deployment execution strategy must not contradict the
  approved Stage 5 Architecture.
- **No migration path ambiguity**: The migration execution path (DES-004) must be a single
  approved mechanism, not a list of alternatives.
- **No surface ownership gaps**: Every deployment surface listed in DES-001 must have exactly
  one owning workflow or process. No surface may be unowned.

### 3.3 Traceability Requirement

The `deployment-execution-strategy.md` artifact must include a traceability section referencing:

- The Stage 5 Architecture Specification that it derives from
- Any Architecture Decision Records (ADRs) that constrain deployment choices
- The TRS deployment requirements that informed this strategy

---

## 4. Implementation Planning Requirements (Scope D)

### 4.1 Stage 8 (Implementation Plan) Mandatory Reference

The Stage 8 Implementation Plan (`modules/amc/07-implementation-plan/implementation-plan.md`)
**MUST** include a dedicated section that:

1. References the approved Stage 5a Deployment Execution Strategy document by path and version
2. Confirms that the wave structure and builder assignments are consistent with the approved
   deployment execution strategy
3. Explicitly states which wave(s) will implement each deployment surface
4. Identifies any deployment surface that requires protected/manual execution
5. Prohibits any build wave from silently substituting a different operational model

An Implementation Plan that lacks this section, or that proposes a deployment model inconsistent
with Stage 5a, is a **blocking defect** and must be returned to the Foreman for correction before
Stage 9 (Builder Checklist) begins.

### 4.2 Stage 9 (Builder Checklist) Attestation

The Stage 9 Builder Checklist **MUST** include an attestation item confirming that the assigned
builder(s) have read and understood the approved Stage 5a Deployment Execution Strategy and
will implement only the approved deployment model.

### 4.3 Stage 12 (Build) Constraint

During Stage 12 (Build), builder agents are bound to the approved Stage 5a Deployment Execution
Strategy. Any deviation — including choosing a different migration path, using a different runner
type, or introducing a new deployment surface — requires:

1. A formal Stage 5a amendment (return to Stage 5a, amend the strategy, obtain CS2 re-approval)
2. A Stage 8 Implementation Plan update referencing the amended strategy
3. IAA notification of the strategy amendment

Builders may not proceed past a deployment surface decision point using an unapproved operational
model. If a builder encounters a scenario not covered by the approved strategy, the builder must
HALT and escalate to the Foreman.

---

## 5. Anti-Drift / Governance Language (Scope E)

### 5.1 Conformance Mandate

> **CONFORMANCE MANDATE (AMC-DEPLOY-001)**: All AMC workflow implementation in Stage 12 (Build)
> and all AMC operational deployments after build MUST conform to the approved Stage 5a
> Deployment Execution Strategy (`deployment-execution-strategy.md`). Deviations from the approved
> strategy require a formal Stage 5a governance update — ad hoc operational model substitution,
> undocumented runner changes, or unilateral migration path changes are prohibited.

### 5.2 Drift Detection Rule

Any of the following in a builder PR constitutes a deployment-strategy drift violation and MUST
cause a QP FAIL verdict by the Foreman:

- A workflow file that touches a deployment surface not covered in the approved strategy
- A migration execution mechanism different from the approved DES-004 path
- A runner type (GitHub-hosted or self-hosted) inconsistent with DES-002/DES-003
- An environment trigger (PR / push / manual dispatch / protected) inconsistent with DES-005
- A frontend workflow that performs a live database mutation if DES-006 prohibits this
- An automated deployment of a surface that DES-007 requires to be manual/protected

### 5.3 Amendment Process

If a legitimate requirement arises that conflicts with the approved Stage 5a strategy:

1. Builder HALTS and escalates to Foreman
2. Foreman raises a Stage 5a Amendment issue with CS2
3. CS2 approves or rejects the amendment
4. If approved: the `deployment-execution-strategy.md` is updated, versioned, and committed
5. Implementation Plan is updated to reference the new version
6. Builder is unblocked with the amended strategy

Amendment is the only permitted path. Silent deviation is prohibited (AMC-DEPLOY-001).

### 5.4 Future Foremen and Builders Reference

This document is the **primary reference** for any future Foreman or builder agent who needs to
understand why Stage 5a exists. When hardening the next AMC build process, consult this document
first. The deployment-strategy oversight is a known class of risk that MUST be resolved before
build execution authorization.

---

## 6. Corrective Action Roadmap

### 6.1 Immediate Actions (this wave — issue #1133)

- [x] Formal oversight recorded in this document
- [x] Stage 5a defined with placement rationale and content requirements
- [x] BUILD_PROGRESS_TRACKER.md updated: Stage 5a row added (DEFINED status)
- [x] AMC_PRE_BUILD_ARTIFACT_INDEX.md updated: Stage 5a section added

### 6.2 Next Required Actions (follow-on waves)

| Action | Trigger | Priority |
|--------|---------|----------|
| Produce Stage 5a Deployment Execution Strategy | After Stage 5 CS2 approval | HIGH |
| Adopt Stage 5a into PRE_BUILD_STAGE_MODEL_CANON.md | Future canon update wave | HIGH |
| Add Stage 5a verification to PBFAG checklist | Before Stage 7 begins | MEDIUM |
| Ensure IAA overlays cover Stage 5a artifact | Before Stage 10 IAA Pre-Brief | MEDIUM |

### 6.3 Canon Update Required

A future governance wave must formally add Stage 5a (or equivalent) to
`governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md`. Until that canon update is merged:

- Stage 5a is enforced AMC-locally via BUILD_PROGRESS_TRACKER.md and this document
- The Foreman must treat Stage 5a completion as a hard gate before Stage 6 for AMC
- No builder may be delegated Stage 6 work without Stage 5a being complete and CS2-approved

---

## 7. Cross-References

- `modules/amc/BUILD_PROGRESS_TRACKER.md` — Stage 5a row added (this issue #1133)
- `modules/amc/AMC_PRE_BUILD_ARTIFACT_INDEX.md` — Stage 5a section added (this issue #1133)
- `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0 — Source canonical model (pending amendment)
- app_management_centre#1133 — Authorizing issue (CS2 @APGI-cmy)
- maturion-isms#1468 — Mirror oversight in ISMS repo (same class)

---

**End of Document**

*AMC-GOV-OVERSIGHT-001 v1.0 — 2026-04-26 — CS2 authorization: app_management_centre#1133*
