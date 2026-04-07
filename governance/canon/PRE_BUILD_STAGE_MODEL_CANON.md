# PRE_BUILD_STAGE_MODEL_CANON

## Status
**Type**: Canonical Governance Definition
**Version**: 1.0.0
**Authority**: CS2 (Johan Ras / Maturion)
**Effective Date**: 2026-04-05
**Owner**: Maturion Engineering Leadership
**Applies To**: All modules — FM App, SlotMaster, MAT, ROADMAP, PIT, AIMC, RADAM, and any future Maturion delivery modules
**Precedence**: Subordinate only to GOVERNANCE_PURPOSE_AND_SCOPE.md
**Derived From**: `governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md` §AD-01 — this canon is the binding canonical realization of that policy requirement
**Layer Down Status**: PUBLIC_API — applies to all consumer repositories
**GOVERNANCE_CANON_MANIFEST Entry**: `PRE_BUILD_STAGE_MODEL_CANON.md | 1.0.0 | PUBLIC_API | FM App, SlotMaster, All Repos | 2026-04-05`

---

## 1. Purpose

This canon defines the **canonical 12-stage pre-build sequence** that every Maturion module delivery MUST follow before any implementation (build) work may begin.

The stage model exists to ensure that all prerequisite thinking, specification, quality assurance planning, and governance preparation work is complete before builders are appointed and code is written. Each stage builds on the previous; skipping or reordering stages introduces delivery risk and is prohibited without documented CS2 approval.

This canon is the single authoritative reference for the 12-stage sequence. All templates, agent contracts, governance artifacts, and app descriptions MUST align with the order defined here.

---

## 2. Constitutional Mandate

This canon derives authority from and complements:

- **GOVERNANCE_PURPOSE_AND_SCOPE.md** — Governance as canonical memory and delivery guardrail
- **APP_DESCRIPTION_REQUIREMENT_POLICY.md** §AD-01 — Mandates that every App Description declares this lifecycle order
- **PRE_BUILD_REALITY_CHECK_CANON.md** v1.1.0 — The PBFAG gate (Stage 7) is defined and governed by this canon; the two canons are complementary and non-contradictory

---

## 3. The Canonical 12-Stage Pre-Build Sequence

### 3.1 Ordered Stage List

| Stage | Name | Purpose |
|-------|------|---------|
| 1 | **App Description** | Define the application's purpose, scope, users, components, technology stack, and deliverables. The upstream authoritative baseline for all downstream artifacts. |
| 2 | **UX Workflow & Wiring Spec** | Define the user experience flows, screen states, interactions, and wiring between UI components and backend. Derived from the App Description. |
| 3 | **FRS (Functional Requirements Specification)** | Enumerate all functional requirements with acceptance criteria. Derived from App Description and UX Workflow & Wiring Spec. |
| 4 | **TRS (Technical Requirements Specification)** | Define the technical requirements, constraints, infrastructure, and technology realization. Must be consistent with the App Description technology stack. |
| 5 | **Architecture** | Define the canonical frozen architecture — components, data flows, API contracts, persistence layer, integration points. Must not contradict FRS or TRS. |
| 6 | **QA-to-Red** | Write the full test suite to red (failing) before any implementation begins. Tests must cover all FRS acceptance criteria. |
| 7 | **PBFAG (Pre-Build Functionality Assessment Gate)** | Independent gate review confirming all prior stages are complete, consistent, and sufficient before build authorization. Governed by `PRE_BUILD_REALITY_CHECK_CANON.md` v1.1.0. |
| 8 | **Implementation Plan** | Define the wave structure, builder assignments, sequencing, and delivery milestones for the build phase. |
| 9 | **Builder Checklist** | Complete the pre-appointment builder readiness checklist confirming governance alignment, scope clarity, and build readiness. |
| 10 | **IAA Pre-Brief** | Independent Assurance Agent pre-briefs the wave — classifies tasks, confirms IAA oversight posture, and commits pre-brief artifact before builder delegation. |
| 11 | **Builder Appointment** | Foreman formally appoints builders with scoped issues, specifying wave, tasks, acceptance criteria, and merge gate requirements. |
| 12 | **Build** | Builders implement the scoped work according to the Architecture, FRS, TRS, QA suite, and Implementation Plan. |

### 3.2 Stage Dependencies

Each stage MUST be completed before the next begins:

```
App Description
  └─► UX Workflow & Wiring Spec
        └─► FRS
              └─► TRS
                    └─► Architecture
                          └─► QA-to-Red
                                └─► PBFAG ◄── Gate: all prior stages verified complete
                                      └─► Implementation Plan
                                            └─► Builder Checklist
                                                  └─► IAA Pre-Brief
                                                        └─► Builder Appointment
                                                              └─► Build
```

### 3.3 Shorthand Reference

The canonical sequence expressed as an arrow chain:

> App Description → UX Workflow & Wiring Spec → FRS → TRS → Architecture → QA-to-Red → PBFAG → Implementation Plan → Builder Checklist → IAA Pre-Brief → Builder Appointment → Build

---

## 4. Ordering Rules

### 4.1 Strict Sequential Ordering
Stages MUST be executed in the canonical order defined in §3. No stage may commence until all preceding stages are complete and have passed their respective quality gates.

### 4.2 Prohibition on Skipping
No stage may be skipped. If a stage is deemed not applicable for a specific delivery context, a formal waiver with documented CS2 approval is required. The waiver must be committed to the repository before the dependent stage begins.

### 4.3 Prohibition on Reordering
Stages MUST NOT be reordered. The dependency structure in §3.2 is non-negotiable. Reordering constitutes a governance breach and MUST be escalated to CS2.

### 4.4 Re-entry Rules
If a later stage reveals a defect or gap in an earlier stage, the earlier stage MUST be corrected and re-verified before the later stage may proceed. This is not skipping — it is rework. Document re-entry in session memory.

### 4.5 CS2 Approval Requirement
Any deviation from the canonical order (skip, reorder, or parallel execution of sequential stages) requires documented CS2 approval committed to the repository BEFORE the deviation occurs. Retroactive approval is not valid.

---

## 5. Scope and Applicability

This canon applies to:
- All Maturion module deliveries (FM App, SlotMaster, MAT, ROADMAP, PIT, AIMC, RADAM)
- All builder agent contracts
- All App Description governance artifacts
- All template files (BUILD_PROGRESS_TRACKER_TEMPLATE.md, BUILDER_CHECKLIST_TEMPLATE.md, UX_WORKFLOW_WIRING_SPEC_TEMPLATE.md, APP_DESCRIPTION_TEMPLATE.md)
- All consumer repositories receiving governance layer-down

---

## 6. Enforcement

### 6.1 Foreman Gate
Foreman-v2-agent MUST verify that the canonical stage sequence has been followed before authorizing builder appointment (Stage 11). Any missing stage is a blocking defect.

### 6.2 IAA Verification
The IAA Pre-Brief (Stage 10) and IAA audit (Phase 4) MUST confirm stage sequence compliance. A REJECTION-PACKAGE is issued for any stage sequence violation.

### 6.3 Template Alignment
All templates that reference the build lifecycle MUST reflect the 12-stage sequence defined in this canon. Discrepancies in templates are governance drift and MUST be corrected.

---

## 7. Cross-References

- `governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md` §AD-01 — Policy source for this canon
- `governance/canon/PRE_BUILD_REALITY_CHECK_CANON.md` v1.1.0 — Governs the PBFAG gate (Stage 7); complementary, non-contradictory
- `governance/templates/BUILD_PROGRESS_TRACKER_TEMPLATE.md` — 12-stage aligned tracker template
- `governance/templates/APP_DESCRIPTION_TEMPLATE.md` — App Description template with §AD-01 section
- `governance/templates/BUILDER_CHECKLIST_TEMPLATE.md` — Builder readiness checklist (Stage 9)
- `governance/templates/UX_WORKFLOW_WIRING_SPEC_TEMPLATE.md` — UX Workflow & Wiring Spec template (Stage 2)
- `governance/GOVERNANCE_CANON_MANIFEST.md` — Canonical manifest listing this file as PUBLIC_API

---

**End of Document**
