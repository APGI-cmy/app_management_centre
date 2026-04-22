# App Description Creation Checklist

## Status Header

| Field | Value |
|-------|-------|
| **Version** | 1.1 |
| **Status** | Active Canonical |
| **Authority** | Johan Ras |
| **Policy Authority** | `governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md` v2.1 |
| **Last Updated** | 2026-04-22 |
| **Enforcement** | Foreman / admin ceremony / IAA — Stage 1 review gate |
| **Blocking Condition** | ANY unchecked item is a governance defect blocking Build Authorization |

---

## Purpose

This checklist is the **executable Stage 1 review mechanism** for App Description completeness. It maps every §5.1 required section and every §5.3 mandatory governance section to a binary pass/fail check. It must be completed and filed before Build Authorization is granted. It is the gate artifact for Pre-FRS and Pre-Architecture enforcement (§11.1, §11.2).

**Section count**: 27 mandatory governance sections (§AD-01 through §AD-27).

> A single unchecked item constitutes a governance defect that BLOCKS Build Authorization.

---

## Part A — §5.1 Required Sections

### A.1 — Status Header

- [ ] Status Header is present and populated (version, status, owner, approval date, last updated, authority, canonical location, policy authority)
- [ ] Status field is one of the allowed values: `Draft` / `Consolidated — Pending CS2 Approval` / `Authoritative` / `Superseded`
- [ ] Policy Authority references `governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md` v2.1 (or current canonical version)

### A.2 — Application Identity

- [ ] Application name is explicitly stated
- [ ] Purpose statement is present (what the application does)
- [ ] Target users / audience are named
- [ ] Core value proposition is stated

### A.3 — Scope Definition

- [ ] In-scope capabilities are listed
- [ ] Out-of-scope items are explicitly listed (not inferred)
- [ ] Boundaries and constraints are stated

### A.4 — Success Criteria

- [ ] Success criteria are stated (how successful delivery is measured)
- [ ] Key outcomes expected are named
- [ ] Definition of "done" for the application is present

### A.5 — Strategic Context

- [ ] Reason the application exists is stated (business / operational driver)
- [ ] Relationship to other applications or systems is declared
- [ ] No strategic context claim contradicts earlier CS2-approved positioning without §AD-26 reconciliation

---

## Part B — §5.3 Mandatory Governance Sections

> **Enforcement rule**: Every section §AD-01 through §AD-27 must be present as a named section with populated content. A placeholder, "TBD", or empty section does NOT satisfy the requirement.

---

### B.1 — §AD-01: Build Lifecycle Stages

- [ ] All 12 canonical build lifecycle stages are listed verbatim and in sequence
- [ ] Stage names exactly match `PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0 — no paraphrasing, abbreviating, or partial listing
- [ ] Stages are numbered in order: 1 through 12
- [ ] A prohibition statement against skipping or reordering stages without documented CS2 approval is present

**Hard gate**: Paraphrasing, abbreviating, or listing fewer than 12 stages explicitly FAILS this gate.

---

### B.2 — §AD-02: Requirements Derivation Chain

- [ ] Derivation chain (App Description → UX Workflow → FRS → TRS → Architecture) is explicitly stated as a diagram or table
- [ ] Each transition names the expected cross-linking artifact
- [ ] No gap in the chain

---

### B.3 — §AD-03: Technology Stack

- [ ] All frameworks, languages, databases, infrastructure components, and external services are named
- [ ] The App Description declares this as the upstream technology baseline for the TRS
- [ ] No technology contradiction between App Description and TRS is documented without resolution

---

### B.4 — §AD-04: Deliverable Artifacts

- [ ] All expected deliverable outputs are named (application, docs, test suites, runbooks, governance evidence)
- [ ] "Is the deployable app a non-negotiable deliverable?" is explicitly present as a line item

---

### B.5 — §AD-05: Component Definition of Done

- [ ] "Done" is defined at component level for each major component
- [ ] Definition covers: implemented, integrated, tested (red-green), manually verified, and PREHANDOVER-proved

---

### B.6 — §AD-06: Test-First Guarantee

- [ ] Test-first mandate for every build wave (including remediation) is stated
- [ ] The QA agent / role responsible is named
- [ ] Minimum passing threshold before builder allocation is stated

---

### B.7 — §AD-07: Physical Verification Gate

- [ ] Browser-based physical verification is mandated for all UI waves
- [ ] Screenshot / walkthrough evidence filing requirement is stated
- [ ] The role responsible for execution is named

---

### B.8 — §AD-08: PBFAG Checklist

- [ ] PBFAG checklist of at minimum 8 checks is mandated for every wave
- [ ] Checks cover: test-suite completeness, prior-wave defect closure, auth wiring readiness, schema alignment, RLS coverage, and PREHANDOVER proof from prior wave

---

### B.9 — §AD-09: Agent Authority Chain

- [ ] Named authority rules for this module are present (which agent can do what)
- [ ] Gating points where authority transitions must be verified are stated
- [ ] No builder may begin without Foreman allocation evidence

---

### B.10 — §AD-10: Schema-to-Hook Validation

- [ ] Column-by-column schema/migration validation is mandated
- [ ] No migration may be merged without a schema-to-hook alignment check

---

### B.11 — §AD-11: Table Pathway Audit

- [ ] Table Pathway Audit is mandated before closing any wave that touches the database
- [ ] Audit requirements cover: table inventory, migration coverage, test coverage, RLS coverage

---

### B.12 — §AD-12: RLS Audit Gate

- [ ] Table-by-table RLS audit gate before production deployment is mandated
- [ ] Responsible agent / role is named
- [ ] Sign-off authority is named

---

### B.13 — §AD-13: Auth Wiring Checklist

- [ ] Auth Wiring Checklist mandate is present for every wave
- [ ] Mandatory items cover: AuthProvider wrapping, ProtectedRoute / HOC on all authenticated routes, login/logout tested end-to-end, real auth (no mock auth in production)

---

### B.14 — §AD-14: AI Integration Requirements

- [ ] All AI/LLM calls must route via AIMC Gateway — stated explicitly
- [ ] Direct provider calls are explicitly prohibited
- [ ] AIMC Gateway endpoint is named

---

### B.15 — §AD-15: Edge Function Registry

- [ ] Edge Function Registry mandate is present
- [ ] Registry must be filed before PREHANDOVER
- [ ] Calls to unregistered or non-deployed functions are declared a blocking defect

---

### B.16 — §AD-16: Deployment Wave

- [ ] Deployment and Commissioning wave is mandated as the final implementation wave
- [ ] Wave requirements include: production provisioning, configuration injection, CWT execution, production smoke testing, and CWT closure report

---

### B.17 — §AD-17: Secret Naming Convention

- [ ] UPPERCASE secret/env naming convention is stated
- [ ] `.env.example` is declared canonical reference for all required environment variables
- [ ] No production env variables outside `.env.example` rule is stated

---

### B.18 — §AD-18: Deployment Runbook

- [ ] Deployment runbooks are mandated for all deployable components
- [ ] Runbook contents are specified: deploy steps, rollback steps, re-deploy instructions, environment-specific notes
- [ ] Canonical runbook location is named

---

### B.19 — §AD-19: Notification/UX Patterns

- [ ] `alert()` is explicitly prohibited for user notifications
- [ ] A toast notification system (or equivalent) is named
- [ ] Integration confirmation before UI wave closure is mandated

---

### B.20 — §AD-20: Shared State Architecture

- [ ] State management approach is named (e.g., React Context, Redux, Zustand)
- [ ] Global state flows (auth state, user preferences, cross-component data) are described
- [ ] No undocumented global state patterns are permitted

---

### B.21 — §AD-21: API Authentication

- [ ] JWT (or equivalent) authentication is mandated for all user/session-context API endpoints
- [ ] PREHANDOVER check for endpoint authentication coverage is required

---

### B.22 — §AD-22: Audit Log Design

- [ ] Action types to be logged are stated (create, update, delete, auth events, etc.)
- [ ] Audit log query / surfacing method is stated
- [ ] Deduplication strategy is stated (event ID, idempotency keys)

---

### B.23 — §AD-23: Tracker Update Requirement

- [ ] Module progress tracker update is mandated at every wave closure
- [ ] Wave closure without tracker update is explicitly prohibited

---

### B.24 — §AD-24: State Persistence Specification

- [ ] Storage location is specified for each user-configurable or device-specific state
- [ ] Retention policy is specified (session / permanent / TTL-based)
- [ ] Ownership (which component or service is authoritative) is specified per state item

---

### B.25 — §AD-25: Cross-System Topology Declaration

> **Gate**: Vague integration references (e.g., "AMC integrates with AIMC") without ownership, flow direction, initiating system, and governance controls do NOT satisfy this gate.

- [ ] A named topology table or diagram explicitly mapping every adjacent system is present
- [ ] For AMC-class applications, **all five** of the following systems are covered: AMC, AIMC, AIMCC, Knowledge Upload Centre, knowledge/memory subsystems. (For non-AMC-class applications, all adjacent systems the application integrates with are covered.)
- [ ] For **each row** in the topology table:
  - [ ] The system's role and ownership is explicitly defined (not implied or inferred)
  - [ ] Inbound flows across the boundary are named
  - [ ] Outbound flows across the boundary are named
  - [ ] The **initiating system** for each interaction is explicitly stated
  - [ ] The governance controls at the boundary are named
- [ ] Write authority for knowledge/memory subsystems is stated with a single authoritative system (not multiple conflicting sources)
- [ ] No adjacent system that the application interacts with is omitted from the table
- [ ] Boundary Confirmation Checklist within §AD-25 is fully checked off

**Hard gate**: An §AD-25 section that marks "initiating system stated" in the checklist but does not include an Initiating System column (or equivalent per-row statement) in the table is internally inconsistent and explicitly fails this gate.

---

### B.26 — §AD-26: Original-Intent Reconciliation

> **Gate**: An App Description that introduces a broader strategic framing without reconciling predecessor commitments does NOT satisfy this gate. Silent descoping is a blocking defect.

*This section is mandatory for all App Descriptions. If there are no predecessor commitments (new build with no prior product description), that must be explicitly stated and is sufficient to satisfy the gate.*

- [ ] All predecessor product descriptions are named by artifact path, version, and current status
- [ ] A Commitment Reconciliation Table is present with an explicit row for every earlier CS2-approved capability commitment
- [ ] Each row in the reconciliation table states: the earlier commitment, source artifact (fully-qualified path + version), disposition (Preserved / Superseded / Descoped / Deferred), and rationale
- [ ] Source artifact references use fully-qualified paths (not bare filenames) and the correct current version
- [ ] The Carry-Forward Confirmation list names only source-supported predecessor commitments — items that do not appear in predecessor artifacts are not asserted as predecessor commitments
- [ ] The Carry-Forward Confirmation distinguishes between: (a) source-supported predecessor commitments carried forward, and (b) current-scope clarifications or extensions that are NOT asserted as predecessor commitments
- [ ] The Explicit Descope Record is present. If no earlier commitment has been descoped, this is explicitly stated (not omitted)
- [ ] No earlier CS2-approved capability commitment from any predecessor artifact has been silently dropped
- [ ] The gate condition statement is present: "No earlier CS2-approved capability commitment has been silently dropped"

**Hard gate**: A Carry-Forward Confirmation list that includes items not present in the predecessor artifact(s) as predecessor commitments (without distinguishing them as extensions) explicitly fails this gate.

---

### B.27 — §AD-27: Stage 1 Source-of-Truth and Transition Posture

> **Gate**: "This document is authoritative" alone is insufficient. The posture relative to prior artifacts must be explicit. Declaring a predecessor document as "Superseded" when it identifies itself as "Active Canonical — Temporary pending CS2 migration decision" creates an authority conflict and explicitly fails this gate.

- [ ] The canonical Stage 1 source-of-truth artifact is identified by path and version
- [ ] The artifact status is declared using one of the allowed values: `Draft` / `Consolidated — Pending CS2 Approval` / `Authoritative` / `Superseded`
- [ ] The Transition Posture is declared as one of: `New Build` / `Successor` / `Extension` / `Replacement`
- [ ] **If `Successor`, `Extension`, or `Replacement`**:
  - [ ] All prior system(s) and their governance artifacts are named with path, version, and current status
  - [ ] Supersession is stated as **conditional on CS2 approval** if this document is not yet Authoritative — no unconditional supersession claim may be made for a document in `Draft` or `Consolidated — Pending CS2 Approval` status
  - [ ] Prior artifacts that remain "Active Canonical — Temporary" are not declared "Superseded" in this document; conditional supersession language is used instead
  - [ ] Explicit transition rules are stated for each prior artifact (e.g., "conditional supersession: takes effect only on CS2 approval of this document")
- [ ] **Authorized Downstream Derivation Table** is present naming downstream artifacts (FRS, TRS, Architecture, UX Workflow & Wiring Spec) authorized to derive from this document
- [ ] **Prior-System Artifact Status Register** is present if Transition Posture is not `New Build`
- [ ] No prior-system artifact is referenced as an active upstream derivation source for downstream artifacts without explicit CS2 authorization recorded in this section
- [ ] Status/approval fields are consistent across the document (source-of-truth declaration, approval record, and predecessor table are not contradictory)

**Hard gate**: Declaring a predecessor "Superseded" when that predecessor identifies itself as the authoritative source pending CS2 migration decision creates an authority conflict and explicitly fails this gate. Use conditional supersession language instead.

---

## Part C — Stage 1 Gate Summary

### Resolution Criteria

**PASS** — ALL items in Parts A and B are checked, and no hard-gate condition has been triggered.

**FAIL** — ANY item in Parts A or B is unchecked, OR any hard-gate condition has been triggered.

> There is no "partial pass", "conditional pass", or "pass with warnings". Build Authorization is BLOCKED on any FAIL.

### Gate Table

| Gate | Requirement | Status |
|------|------------|--------|
| A.1–A.5 | §5.1 Required Sections | `[ ] PASS / [ ] FAIL` |
| B.1 (§AD-01) | Exact 12-stage listing | `[ ] PASS / [ ] FAIL` |
| B.2 (§AD-02) | Requirements derivation chain | `[ ] PASS / [ ] FAIL` |
| B.3 (§AD-03) | Technology stack | `[ ] PASS / [ ] FAIL` |
| B.4 (§AD-04) | Deliverable artifacts | `[ ] PASS / [ ] FAIL` |
| B.5 (§AD-05) | Component definition of done | `[ ] PASS / [ ] FAIL` |
| B.6 (§AD-06) | Test-first guarantee | `[ ] PASS / [ ] FAIL` |
| B.7 (§AD-07) | Physical verification gate | `[ ] PASS / [ ] FAIL` |
| B.8 (§AD-08) | PBFAG checklist | `[ ] PASS / [ ] FAIL` |
| B.9 (§AD-09) | Agent authority chain | `[ ] PASS / [ ] FAIL` |
| B.10 (§AD-10) | Schema-to-hook validation | `[ ] PASS / [ ] FAIL` |
| B.11 (§AD-11) | Table pathway audit | `[ ] PASS / [ ] FAIL` |
| B.12 (§AD-12) | RLS audit gate | `[ ] PASS / [ ] FAIL` |
| B.13 (§AD-13) | Auth wiring checklist | `[ ] PASS / [ ] FAIL` |
| B.14 (§AD-14) | AI integration requirements | `[ ] PASS / [ ] FAIL` |
| B.15 (§AD-15) | Edge function registry | `[ ] PASS / [ ] FAIL` |
| B.16 (§AD-16) | Deployment wave | `[ ] PASS / [ ] FAIL` |
| B.17 (§AD-17) | Secret naming convention | `[ ] PASS / [ ] FAIL` |
| B.18 (§AD-18) | Deployment runbook | `[ ] PASS / [ ] FAIL` |
| B.19 (§AD-19) | Notification/UX patterns | `[ ] PASS / [ ] FAIL` |
| B.20 (§AD-20) | Shared state architecture | `[ ] PASS / [ ] FAIL` |
| B.21 (§AD-21) | API authentication | `[ ] PASS / [ ] FAIL` |
| B.22 (§AD-22) | Audit log design | `[ ] PASS / [ ] FAIL` |
| B.23 (§AD-23) | Tracker update requirement | `[ ] PASS / [ ] FAIL` |
| B.24 (§AD-24) | State persistence specification | `[ ] PASS / [ ] FAIL` |
| B.25 (§AD-25) | **Cross-system topology declaration** | `[ ] PASS / [ ] FAIL` |
| B.26 (§AD-26) | **Original-intent reconciliation** | `[ ] PASS / [ ] FAIL` |
| B.27 (§AD-27) | **Stage 1 source-of-truth and transition posture** | `[ ] PASS / [ ] FAIL` |
| **Overall** | **All 27 gates PASS** | `[ ] PASS / [ ] FAIL` |

---

## Part D — Completion Record

```
App Description Path: ___________________________________________
Version reviewed:     ___________________________________________
Module:               ___________________________________________
Reviewer:             ___________________________________________
Review date:          ___________________________________________
Overall result:       [ ] PASS     [ ] FAIL
```

**If FAIL**:
- [ ] Gap report generated listing all unchecked items and triggered hard gates
- [ ] Gap report filed at: `{module}/00-app-description/stage1-review-gap-report-{date}.md`
- [ ] Build Authorization BLOCKED — no FRS, TRS, or Architecture work may commence
- [ ] App Description owner notified of required remediation
- [ ] Re-review scheduled upon remediation

**If PASS**:
- [ ] This completed checklist filed at: `{module}/00-app-description/stage1-review-evidence-{date}.md`
- [ ] Build Authorization pre-condition satisfied (other gate conditions per BUILD_AUTHORIZATION_GATE.md still apply)

---

## Part E — Hard Gate Quick Reference

The following conditions are **immediately blocking** regardless of all other checklist items:

| Hard Gate | Condition |
|-----------|-----------|
| §AD-01 | Fewer than 12 stages listed, or any stage name differs from `PRE_BUILD_STAGE_MODEL_CANON.md` |
| §AD-25 | Topology table exists but does not include an Initiating System column (or equivalent per-row statement), AND checklist claims initiating system is stated — internally inconsistent |
| §AD-25 | Any adjacent system the application interacts with is omitted from the topology table |
| §AD-25 | Write authority for knowledge/memory subsystems is stated inconsistently in different sections of the document |
| §AD-26 | Any earlier CS2-approved capability commitment is not accounted for in the reconciliation table |
| §AD-26 | Carry-Forward Confirmation asserts items as predecessor commitments that do not appear in the predecessor artifact(s) |
| §AD-27 | A predecessor artifact that identifies itself as "Active Canonical — Temporary pending CS2 migration decision" is declared "Superseded" without conditional language |
| §AD-27 | Status and approval fields are contradictory across sections of the document |

---

## Part F — References

| Artifact | Path |
|----------|------|
| Policy | `governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md` v2.1 |
| Template | `governance/templates/APP_DESCRIPTION_TEMPLATE.md` v1.1 |
| FRS Alignment Checklist | `governance/contracts/app-description-frs-alignment-checklist.md` |
| Architecture Compilation Contract | `governance/architecture/ARCHITECTURE_COMPILATION_CONTRACT.md` |
| Build Authorization Gate | `governance/build/BUILD_AUTHORIZATION_GATE.md` |
| Pre-Build Stage Model Canon | `PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0 |

---

**Document Metadata**  
- Checklist ID: `APP_DESCRIPTION_CREATION_CHECKLIST`  
- Version: 1.1  
- Authority: `governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md` v2.1  
- Section count enforced: 27 (§AD-01 through §AD-27)  
- Version history: v1.0 — 24 mandatory sections (§AD-01–§AD-24); v1.1 — 27 mandatory sections, added §AD-25 (Cross-System Topology Declaration), §AD-26 (Original-Intent Reconciliation), §AD-27 (Stage 1 Source-of-Truth and Transition Posture) + hard gates for all three new sections
