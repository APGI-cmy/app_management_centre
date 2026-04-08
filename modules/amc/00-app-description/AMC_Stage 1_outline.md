# AMC — App Description

## Status Header

- **Document Title:** AMC App Description
- **Application Name:** App Management Centre (AMC)
- **Lineage:** Successor to the Foreman App / Foreman Office App
- **Document Type:** Stage 1 App Description
- **Status:** Draft
- **Authority:** Johan Ras (CS2)
- **Primary AI Executive:** Maturion
- **Supervisory Orchestration Layer:** Foreman
- **Current Canonical Source Decision:** Pending confirmation
- **Purpose of This Document:** Define the authoritative Stage 1 application description for AMC in alignment with governance canon and downstream derivation requirements

---

## §1 — Application Identity

### Application Name
App Management Centre (AMC)

### Purpose
AMC is the executive control centre of the Maturion estate. It exists to provide a single governed environment through which Johan Ras, and over time Maturion as resident AI executive, can supervise system wellbeing, monitor execution, manage interventions, approve governance-sensitive actions, and coordinate ongoing application evolution.

### Target Users/Audience
- Johan Ras as constitutional authority and reserved-matter approver
- Maturion as resident AI executive within AMC
- Foreman as supervised orchestration authority
- Internal specialist agents operating under governed supervision
- Independent assurance and maintenance agents reporting into the AMC-managed estate

### Core Value Proposition
AMC provides a persistent, mobile-accessible, governance-sensitive executive operating surface for the Maturion system, enabling proactive oversight, two-way communication, escalation handling, approval control, and coordinated action across the application estate.

---

## §2 — Scope Definition

### In Scope
- Executive oversight of the Maturion application estate
- Mobile and desktop access to supervisory controls and visibility
- Proactive two-way communication between Johan and Maturion
- Visibility into system health, execution health, governance health, and operational alerts
- Governance-sensitive approval and intervention workflows
- Oversight of specialist-agent ecosystems and sandboxed AI workspaces
- Support for maintenance, assurance, compliance, and operational reporting
- Controlled build/job initiation and execution visibility
- Audit-aware management of app evolution and operational wellbeing

### Explicitly Out of Scope
- AMC as a direct code editor
- AMC as a replacement for governance canon
- AMC as a replacement for consumer-facing applications
- AMC as an uncontrolled bypass around approved build governance
- AMC as a direct substitute for implementation repos or CI/CD tooling
- AMC as a substantive code-quality validator in place of assurance agents

### Boundaries and Constraints
- Governance canon remains external authority and must be referenced, not absorbed as product identity
- Reserved matters remain subject to Johan Ras approval unless formally delegated
- AI integrations must comply with AIMC/AIMC Gateway controls
- AMC must preserve separation between executive control, orchestration, assurance, and implementation

---

## §3 — Success Criteria

### Delivery success measures
- A complete App Description exists and is canon-compliant
- The description is sufficient to derive FRS, TRS, architecture, and build planning artifacts
- AMC role, boundaries, and authority model are explicitly defined
- Scope is stable enough to support downstream design without major ambiguity

### Operating success measures
- AMC provides meaningful executive visibility over the Maturion estate
- Maturion can proactively surface risks, events, and decisions before being asked
- Governance-sensitive decisions are surfaced for approval at the correct authority boundary
- AMC supports rapid, governed operational intervention from mobile and desktop contexts

### Definition of Done for the Application
The application is considered aligned at Stage 1 when its identity, scope, authority chain, governance boundaries, lifecycle requirements, AI integration model, and state/audit expectations are clearly defined and approved.

---

## §4 — Strategic Context

### Why this application exists
AMC exists because the Maturion estate requires a persistent executive control centre rather than a collection of disconnected build tools, dashboards, or repo-level artifacts. It provides the operational, supervisory, and decision-control surface needed to manage a governed multi-agent system over time.

### Relationship to other applications
AMC is not a replacement for domain applications. It is the management and wellbeing centre through which the broader estate is supervised, coordinated, and improved.

### Replacement/extension of
AMC is the matured successor to the Foreman App / Foreman Office App lineage. It carries forward the enduring control-centre intent while separating product identity from legacy governance mixing and early build experimentation.

### Strategic Evolution Path
- **Current state:** Johan Ras acts as CS2 and constitutional authority over reserved matters
- **Transition state:** Maturion progressively assumes operational executive responsibilities within governed limits
- **Future state:** Johan retains reserved constitutional authority while Maturion manages day-to-day executive supervision of the application estate

---

## §5 — Build Lifecycle Stages (§AD-01)

Define the mandatory lifecycle order for AMC and all derived work products, ensuring that App Description approval precedes FRS, TRS, architecture, build planning, and implementation.

---

## §6 — Requirements Derivation Chain (§AD-02)

Define the authoritative derivation chain from App Description to FRS, TRS, architecture, implementation, and verification artifacts, including traceability expectations.

---

## §7 — Technology Stack (§AD-03)

Define the approved baseline technology stack categories for AMC, including frontend, backend, state, authentication, notification, audit, and AI-integration layers.

---

## §8 — Deliverable Artifacts (§AD-04)

Define the set of mandatory downstream artifacts that must be produced from this App Description, including FRS, TRS, architecture, operational runbooks, and governance-linked evidence artifacts.

---

## §9 — Component Definition of Done (§AD-05)

Define what it means for an AMC component to be complete, including implementation, test evidence, integration, auditability, and alignment to approved design intent.

---

## §10 — Test-First Guarantee (§AD-06)

Define the mandatory test-first expectations for derived implementation work and the relationship between requirements, tests, and build authorization.

---

## §11 — Physical Verification Gate (§AD-07)

Define the requirement for physical or real-environment verification where applicable, including interaction validation, end-to-end behavior confirmation, and operator-observable outcomes.

---

## §12 — PBFAG Checklist Requirements (§AD-08)

Define the mandatory pre-build governance checklist obligations that must be satisfied before downstream work may proceed.

---

## §13 — Agent Authority Chain (§AD-09)

Define the AMC authority model, including:
- Johan Ras as constitutional authority over reserved matters
- Maturion as resident AI executive within AMC
- Foreman as supervised orchestration authority beneath Maturion
- IAA, specialist, maintenance, and related agents reporting into the governed Maturion operating structure
- Builders as implementation actors only

---

## §14 — Schema-to-Hook Validation (§AD-10)

Define the requirement that any data structures, hooks, state pathways, or integration patterns be formally validated against approved architecture and downstream implementation design.

---

## §15 — Table Pathway Audit (§AD-11)

Define the requirement that all data storage pathways, table interactions, and persistence flows be explicitly documented and auditable.

---

## §16 — RLS Audit Gate (§AD-12)

Define the requirement for Row-Level Security or equivalent access-control validation across all stateful and user/agent-sensitive data interactions.

---

## §17 — Auth Wiring Checklist (§AD-13)

Define the mandatory authentication and authorization design expectations for AMC, including user authority, agent authority, reserved-matter approvals, and action traceability.

---

## §18 — AI Integration Requirements (§AD-14)

Define the mandatory AI integration model for AMC, including:
- Maturion as resident AI executive
- specialist-agent and sandbox-agent integration patterns
- AIMC/AIMC Gateway routing requirements
- prohibition of uncontrolled direct provider integration
- separation between executive AI, orchestration AI, specialist AI, and assurance AI

---

## §19 — Edge Function Registry (§AD-15)

Define the requirement that all edge/server functions, orchestrated actions, and externally callable operational endpoints be registered, named, and governed.

---

## §20 — Deployment Wave (§AD-16)

Define the approved deployment-wave strategy for AMC delivery and evolution, including sequencing, rollout discipline, and dependency-aware release governance.

---

## §21 — Secret Naming Convention (§AD-17)

Define the approved naming and governance expectations for secrets, keys, provider credentials, agent credentials, and environment-bound operational tokens.

---

## §22 — Deployment Runbook (§AD-18)

Define the deployment-runbook expectations required before live delivery, including rollback, escalation, operational checks, and approval gates.

---

## §23 — Notification/UX Patterns (§AD-19)

Define the AMC notification and user-experience patterns, including:
- proactive notification before user inquiry where appropriate
- escalation prompts
- approval prompts
- attention routing to mobile and desktop contexts
- conversational interaction with Maturion
- dashboard/drill-down supervision patterns
- avoidance of crude or non-governed alert mechanisms

---

## §24 — Shared State Architecture (§AD-20)

Define the shared state model required for AMC, including supervisory context, alert state, conversation state, intervention state, escalation state, and cross-surface continuity.

---

## §25 — API Authentication (§AD-21)

Define the authentication model for all API and orchestration actions, including user identity, agent identity, role-based restrictions, and reserved-matter protection.

---

## §26 — Audit Log Design (§AD-22)

Define the audit-log model for AMC, including:
- approvals
- interventions
- agent actions
- governance-sensitive events
- maintenance events
- assurance events
- build/job initiation and completion events

---

## §27 — Tracker Update Requirement (§AD-23)

Define the rule that trackers and stage-progress artifacts must be updated alongside substantive progress so AMC state, delivery state, and governance state remain synchronized.

---

## §28 — State Persistence Specification (§AD-24)

Define the persistence expectations for AMC, including:
- user preferences
- supervisory session context
- alert history
- approval history
- device-specific continuity
- sandbox context
- operational state restoration requirements

---

## Optional Sections

### High-Level Feature List (non-exhaustive)
- Executive dashboard
- Proactive alerting and escalation feed
- Conversational control interface with Maturion
- Approval centre for governance-sensitive actions
- Operational intervention launcher
- Estate health and drill-down views
- Sandbox management surfaces
- Maintenance and assurance reporting views

### User Personas
- Johan Ras
- Maturion
- Foreman
- Specialist agents
- Assurance agents
- Maintenance agents

### Key Use Cases
- Receive proactive notification before asking for status
- Approve or reject governance-sensitive changes
- Initiate a governed fix while in a mobile/client context
- Review estate health and drill into root causes
- Oversee sandboxed specialist-agent work within application environments
- Review maintenance, assurance, compliance, and security findings surfaced through Maturion

### Non-Functional Priorities
- Mobile accessibility
- Persistent availability
- Clear authority boundaries
- Strong auditability
- Controlled AI integration
- Reliable notification and escalation behavior
- Safe delegation and progressive automation

### Future Evolution Considerations
- Progressive expansion of Maturion’s executive authority
- Broader specialist-agent ecosystems
- Deeper sandbox support inside consumer applications
- Expanded autonomous maintenance and assurance capability
- Formalized transition of day-to-day operational control away from Johan while preserving reserved constitutional authority

---

## Approval Record

- **Prepared by:** ______________________
- **Reviewed by:** ______________________
- **Approved by:** ______________________
- **Approval Date:** ______________________
- **Approval Reference:** ______________________
