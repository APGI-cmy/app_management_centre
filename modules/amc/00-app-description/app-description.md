# AMC App Description — Stage 1

## Status Header

| Field | Value |
|---|---|
| **Document Title** | AMC App Description |
| **Application Name** | App Management Centre (AMC) |
| **Document Type** | Stage 1 App Description |
| **Version** | 1.0 |
| **Status** | Consolidated — Pending CS2 Approval |
| **Owner** | Johan Ras (CS2) |
| **Approval Date** | Pending CS2 approval |
| **Last Updated** | 2026-04-08 |
| **Canonical Location** | `modules/amc/00-app-description/app-description.md` |
| **Policy Authority** | `governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md §5.1` |
| **Primary AI Executive** | Maturion |
| **Supervisory Orchestration Layer** | Foreman |
| **Stage** | Stage 1 of 12 — App Description |
| **Purpose** | Single authoritative Stage 1 source artifact for FRS, TRS, Architecture, and build planning derivation |
| **Lineage** | Successor to the Foreman App / Foreman Office App |

---

> **⚠️ AUTHORITY TRANSITION NOTE**
> This document is the **approval target** for AMC Stage 1 and is currently a candidate for CS2 approval.
> It is **NOT YET** the approved authoritative source for downstream derivation.
> No downstream artifact (FRS, TRS, Architecture, Build Planning) may treat this document as approved truth until CS2 records explicit approval.
> **Where approval is recorded**: CS2 approval must be recorded in `modules/amc/00-app-description/app-description-approval.md` (the Stage 1 approval record for this module). The `Approved By`, `Approval Date`, `Approved Version`, and `Canonical Source` fields in that document must all be populated before this document carries authoritative status.
> Once CS2 approval is recorded there, this file becomes the single authoritative AMC Stage 1 source and all transitional FM-era Stage 1 files in this directory are superseded.

---

## §1 — Application Identity

### Application Name
App Management Centre (AMC)

### Purpose
AMC is the executive control centre of the Maturion estate. It exists to provide a single governed environment through which Johan Ras, and progressively Maturion as resident AI executive, can supervise system wellbeing, monitor execution, manage interventions, approve governance-sensitive actions, and coordinate ongoing application evolution.

AMC is intended to be the place from which the overall application estate is watched, guided, protected, and improved. It is not only a dashboard surface. It is the command, communication, approval, escalation, and wellbeing centre of the estate.

### Target Users/Audience
- **Johan Ras** as constitutional authority, owner of reserved matters, and human executive authority
- **Maturion** as resident AI executive operating within AMC
- **Foreman** as supervised orchestration authority operating beneath Maturion
- **Internal specialist agents** operating under governed supervision
- **Independent assurance agents** performing scheduled and event-driven checks
- **Maintenance and operational agents** responsible for upkeep, scans, reporting, and remediation support

### Core Value Proposition
AMC provides a persistent, mobile-accessible, governance-sensitive executive operating surface for the Maturion system, enabling proactive oversight, two-way communication, escalation handling, approval control, and coordinated action across the application estate.

Its value is that Johan does not have to manually interrogate the system to discover problems. AMC, through Maturion and supporting agents, is expected to surface important matters proactively, support rapid governed intervention, and preserve authority boundaries while increasing operational autonomy over time.

### Executive Layer Boundary Definitions

AMC is the executive supervisory application for the **live ISMS and Maturion operating estate**. It operates as the outermost executive surface of the estate. It does not internally implement the AI, knowledge ingestion, or persistent memory capabilities it supervises.

The following layer boundary definitions apply across this document and all downstream derivations:

| Layer | Definition |
|---|---|
| **AMC** | Executive supervisory application and operating surface. Provides oversight, alerts, approvals, interventions, and executive visibility. Does not own AI execution, knowledge ingestion, or persistent memory truth. |
| **AIMC** | AI capability / gateway layer. The sole governed AI execution gateway for the estate. All AI-model interactions must route through AIMC. AMC does not execute AI models directly. |
| **AIMCC** | Knowledge ingestion + knowledge/memory operating layer. Governs the ingestion, organization, and memory operations of the estate's knowledge base. AIMCC may own workflow-state and ingestion/curation metadata required to run those processes, but the canonical owner of persistent knowledge/memory truth remains the **knowledge / memory system**. AMC may surface or reference knowledge managed through AIMCC-governed workflows, but does not become the canonical owner. |
| **Knowledge Upload Centre** | Governed ingestion surface. The approved entry point for uploading and submitting knowledge/documents to the estate's knowledge base. Operates within AIMCC governance. |
| **knowledge / memory system** | Persistent substrate for estate knowledge and memory. This is an **estate capability**, not an AMC-private silo. AMC may present or query it but must not silently duplicate or claim canonical ownership of its contents. |

These boundaries are non-negotiable. All downstream derivation must preserve them. No section of this document or any downstream artifact may imply that AMC internalizes, bypasses, or replaces these governed layers.

---

## §2 — Scope Definition

### In Scope
- Executive oversight of the Maturion application estate
- Mobile and desktop access to supervisory controls and visibility
- Proactive two-way communication between Johan and Maturion
- Visibility into system health, execution health, governance health, security posture, compliance posture, and operational alerts
- Governance-sensitive approval and intervention workflows
- Oversight of specialist-agent ecosystems and sandboxed AI workspaces
- Support for maintenance, assurance, compliance, and operational reporting
- Controlled build/job initiation and execution visibility
- Audit-aware management of app evolution and operational wellbeing
- Surfacing early warnings, exceptions, anomalies, and required decisions before explicit user inquiry
- Controlled coordination of post-approval execution across the Maturion estate

### Explicitly Out of Scope
- AMC as a direct code editor
- AMC as a replacement for governance canon
- AMC as a replacement for consumer-facing applications
- AMC as an uncontrolled bypass around approved build governance
- AMC as a direct substitute for implementation repos or CI/CD tooling
- AMC as a substantive code-quality validator in place of assurance agents
- AMC as an uncontrolled direct prompt surface for unmanaged AI execution
- AMC as a hidden authority-transfer mechanism that bypasses explicit approval rules

### Boundaries and Constraints
- Governance canon remains external authority and must be referenced, not absorbed as product identity
- Reserved matters remain subject to Johan Ras approval unless formally delegated
- AI integrations must comply with AIMC and AIMC Gateway controls
- AMC must preserve separation between executive control, orchestration, assurance, and implementation
- AMC must not collapse specialist-agent roles into a single undifferentiated AI runtime
- Operational autonomy may expand over time, but only through explicit governance and approval

### AMC / AIMC / AIMCC Boundary

This subsection makes explicit what AMC owns versus what it supervises, integrates with, or routes through.

**AMC owns:**
- executive visibility surfaces and dashboards
- approval and intervention workflow surfaces
- escalation routing and alerting surfaces
- executive conversation surfaces with Maturion
- audit event generation for AMC-originated actions
- its own operational state (alert records, approval records, intervention records, audit events)

**AMC supervises but does not own:**
- AI model execution (routed through AIMC)
- knowledge ingestion and memory operations (routed through AIMCC / Knowledge Upload Centre)
- persistent knowledge / memory truth (owned by the knowledge / memory system)
- specialist agent workspaces (supervised, not absorbed)

**AMC explicitly does NOT:**
- execute AI models directly without routing through AIMC
- ingest knowledge or documents without routing through AIMCC / Knowledge Upload Centre
- become the canonical long-term owner of estate knowledge or memory truth
- present generated text as authoritative memory without provenance attribution
- silently bypass AIMC for AI actions
- silently bypass AIMCC or Knowledge Upload Centre for knowledge ingestion

**What AMC supervises within its executive scope:**
- upload status and governed ingestion outcomes (surfaced from AIMCC)
- AI action outcomes (routed through AIMC and reported back to AMC)
- memory-aware operations (referenced from the knowledge / memory system via governed APIs)
- executive approval of certain knowledge / memory actions where governance requires it

**Explicit prohibitions:**
- Unmanaged AI bypass: any AI action taken from AMC context that does not route through AIMC is a governance violation
- Unmanaged knowledge-ingestion bypass: any knowledge upload or ingestion action initiated from AMC context that does not route through AIMCC / Knowledge Upload Centre is a governance violation

---

## §3 — Success Criteria

### Delivery success measures
- A complete App Description exists and is canon-compliant
- The description is sufficient to derive FRS, TRS, architecture, and build planning artifacts
- AMC role, boundaries, and authority model are explicitly defined
- Scope is stable enough to support downstream design without major ambiguity
- AMC’s relationship to Maturion, Foreman, AIMC, specialist agents, and assurance agents is explicit
- The product identity is cleanly separated from legacy governance mixing and build-history clutter

### Operating success measures
- AMC provides meaningful executive visibility over the Maturion estate
- Maturion can proactively surface risks, events, and decisions before being asked
- Governance-sensitive decisions are surfaced for approval at the correct authority boundary
- AMC supports rapid, governed operational intervention from mobile and desktop contexts
- Johan can remain in continuous contact with the estate without becoming the direct operator of every execution detail
- Specialist, assurance, and maintenance capabilities can be supervised through AMC in a coherent manner

### Definition of Done for the Application
The application is considered aligned at Stage 1 when its identity, scope, authority chain, governance boundaries, lifecycle requirements, AI integration model, notification model, and state/audit expectations are clearly defined and approved.

Stage 1 is not complete merely because an outline exists. It is complete only when the product truth is sufficiently clear that downstream requirements and architecture work can proceed without guessing the intent of AMC.

### Measurable Integration and Operating Success Criteria

In addition to the general delivery and operating success measures above, AMC must satisfy the following measurable integration-specific criteria:

**Executive alerting:**
- alerts are generated and surfaced proactively without requiring manual interrogation
- critical alerts reach the correct authority within defined SLA
- alert acknowledgment and escalation are recorded in the audit trail

**Approval / intervention flows:**
- every governance-sensitive action that requires approval is blocked until approval is explicitly granted
- approval decisions are recorded with actor, timestamp, basis, and outcome
- intervention actions are traceable from initiation through to completion or cancellation

**AIMC-routed AI actions:**
- zero AI model executions occur from AMC context that do not route through AIMC
- AIMC unavailability is handled gracefully with explicit degraded-mode behavior
- all AIMC-routed actions are recorded in the audit trail with source and outcome

**AIMCC / Knowledge Upload Centre oversight:**
- AMC surfaces upload status and ingestion outcomes sourced from AIMCC
- no unmanaged knowledge ingestion pathway exists within AMC
- AIMCC unavailability is handled gracefully with explicit degraded-mode behavior

**Memory-aware operational clarity:**
- AMC surfaces knowledge / memory references with provenance, not as anonymous authoritative facts
- AMC does not silently cache or duplicate knowledge / memory truth beyond transient presentation state
- memory retrieval degradation is surfaced, not silently suppressed

**State / audit / provenance clarity:**
- every consequential action in AMC has a traceable audit event
- state ownership is explicit: AMC-owned state is distinguishable from AIMCC-owned or knowledge-system-owned state
- no audit event is orphaned (every event has an identified actor, source system, object, and timestamp)

---

## §4 — Strategic Context

### Why this application exists
AMC exists because the Maturion estate requires a persistent executive control centre rather than a loose collection of repo artifacts, dashboards, build utilities, chat threads, and governance fragments.

The estate is intended to evolve into a governed multi-agent operating environment in which autonomous and semi-autonomous actors can design, supervise, maintain, assure, and progressively improve applications across the estate. That environment cannot be safely or effectively operated through fragmented tooling alone. It requires a single executive surface through which system wellbeing, intervention, approval, escalation, and strategic direction are coordinated.

AMC is therefore created to be the principal executive operating environment of the estate. Its function is not merely to display status. Its function is to maintain governed executive contact with the estate at all times, support proactive awareness, route decisions to the correct authority, and enable rapid but controlled operational action.

### Relationship to other applications
AMC is not a replacement for domain applications, consumer applications, or specialist work surfaces. Those applications exist to perform business, operational, or domain-specific functions.

AMC sits above those applications as the executive management and wellbeing centre of the estate. It exists to:
- supervise estate health and behavior
- coordinate intervention and escalation
- surface governance-sensitive decisions
- maintain executive visibility across the estate
- manage the relationship between human authority, AI executive capability, orchestration capability, and specialist-agent capability

AMC is therefore an estate-level control plane and executive operating surface, not a domain workflow application.

### Replacement/extension of
AMC is the matured successor to the Foreman App / Foreman Office App lineage.

The earlier Foreman App vision correctly identified the need for a continuous supervisory control centre, persistent executive awareness, two-way communication, and governed intervention capability. However, earlier artifacts mixed together product intent, governance canon, runtime experimentation, and historical build evidence in ways that obscured the true product boundary.

AMC carries forward the enduring intent of that lineage while correcting the boundary model. Under AMC:
- product identity is separated from governance canon
- executive control is separated from implementation tooling
- supervisory authority is separated from builder activity
- historical lineage is preserved without being mistaken for current product truth

AMC is therefore both a continuation and a refinement of the original Foreman-App concept.

### Strategic Evolution Path
AMC shall support a staged executive evolution model.

**Current state**
- Johan Ras acts as CS2 and constitutional authority over reserved matters
- Maturion is being shaped as the resident AI executive but does not yet hold full autonomous executive authority
- Foreman operates as supervised orchestration authority beneath the current human constitutional authority

**Transition state**
- Maturion progressively assumes approved operational executive responsibilities
- routine supervision, coordination, maintenance routing, specialist oversight, and estate reporting move increasingly into Maturion’s managed domain
- governance-sensitive or constitutionally reserved decisions continue to escalate to Johan Ras unless explicitly re-governed

**Future state**
- Maturion becomes the primary day-to-day AI executive of the estate
- Foreman remains an orchestration/supervision layer beneath Maturion rather than the top-level executive intelligence
- Johan Ras moves upward into a higher-order constitutional and strategic role, retaining reserved authority over fundamental change, governance amendment, authority-transfer boundaries, and major product-direction decisions

This evolution path is intentional and must be treated as part of AMC’s product purpose, not an incidental future possibility.

### Strategic Positioning
AMC shall be positioned as the executive operating system of the Maturion estate.

Its strategic role is to combine:
- executive visibility
- proactive communication
- governed approvals
- intervention launch capability
- orchestration supervision
- specialist-agent ecosystem oversight
- maintenance and assurance reporting
- estate wellbeing intelligence
- continuity of control across desktop, mobile, and live field contexts

AMC must make it possible for Johan Ras to remain in meaningful control of the estate without becoming the direct operator of every technical process, and must progressively make it possible for Maturion to assume more of that executive burden within governed limits.

### Strategic Design Consequence
Because AMC is an executive operating system rather than a simple admin console, downstream design must prioritize:
- mobile-first and always-available executive access
- proactive awareness rather than passive query-only interaction
- strong authority clarity
- strong auditability
- safe progressive delegation
- controlled integration with specialist and sandboxed AI teams
- support for real-world intervention scenarios, including client-context decision and execution initiation

### Original AMC Intent Reconciliation

The following AMC capabilities were identified in earlier intent documents and governance records. This subsection explicitly reconciles each with the current strategic framing.

| Original AMC Capability | Status | Current Framing |
|---|---|---|
| **ARC Trigger Governance** | ✅ Preserved and expanded | AMC supervises and triggers ARC-related governance actions within the estate. This capability is absorbed into AMC's intervention launch, escalation routing, and approval workflow model. ARC trigger governance is a first-class AMC executive function. |
| **Dynamic Upload Quota Management** | ✅ Preserved and expanded | AMC surfaces and supervises upload quota state sourced from AIMCC / Knowledge Upload Centre. AMC may execute quota-related governance actions through approved AIMCC pathways. Not silently retired — expanded into the AIMCC oversight model. |
| **Alert Dashboard** | ✅ Preserved and elevated | The Alert Dashboard is explicitly preserved and elevated as the proactive executive alerting surface of AMC. It is now positioned as a core executive operating commitment, not a secondary utility. |
| **Audit Trail** | ✅ Preserved and expanded | The Audit Trail is explicitly preserved as a constitutional operating requirement. AMC must produce a comprehensive audit trail covering all consequential actions across its executive, approval, intervention, AIMC, AIMCC, and knowledge-reference pathways. |
| **Progressive Automation Control** | ✅ Preserved and expanded | Progressive Automation Control is preserved as the progressive autonomy model. AMC must support the progressive delegation of approved operational responsibilities to Maturion and other governed agents, with explicit approval boundaries, rollback capability, and audit traceability at each delegation step. |

No original AMC capability commitment has been silently retired. All five original capabilities are explicitly reconciled and carried forward into the current strategic framing.


## §5 — Build Lifecycle Stages (§AD-01)

AMC shall follow a governed lifecycle in which each major artifact stage establishes truth that the next stage is required to inherit, preserve, and deepen.

This section exists because AMC is not a routine application that can safely emerge through informal iteration alone. It is intended to become the executive operating centre of the Maturion estate. As a result, lifecycle order is not just a delivery convenience. It is a governance control that prevents downstream work from outrunning product truth, authority truth, approval truth, audit truth, and AI-boundary truth.

For AMC, the lifecycle order must therefore be explicit, normative, and enforced.

### Purpose of the Lifecycle Model
The lifecycle model shall exist to ensure that AMC is built in the right order and that each stage performs its proper role before the next stage begins.

The lifecycle must ensure that:
- product identity is settled before functional behavior is derived
- functional behavior is settled before technical obligations are specified
- technical obligations are settled before structural architecture is approved
- architecture is settled before detailed build decomposition proceeds
- build execution does not become the place where constitutional product meaning is improvised
- verification and assurance can test against stable approved truth
- deployment and operationalization inherit governed design rather than creating it retroactively

If the lifecycle is bypassed, AMC becomes vulnerable to downstream drift and hidden constitutional defects.

### Core Principle
Later lifecycle stages may elaborate earlier truth, but they may not replace it.

No stage may proceed responsibly if the immediately preceding stage remains too ambiguous, too incomplete, or too contradictory to serve as a stable upstream source.

For AMC, this is especially important because the application’s most important characteristics are not superficial features. They are constitutional product characteristics:
- executive operating purpose
- human and AI authority boundaries
- approval significance
- audit significance
- shared-state significance
- mobile/proactive operating behavior
- sandbox and specialist boundary significance

These must be established in the correct order.

### Normative Lifecycle Order
AMC shall follow the full canonical 12-stage lifecycle order:

1. **App Description**
2. **UX Workflow & Wiring Spec**
3. **Functional Requirements Specification (FRS)**
4. **Technical Requirements Specification (TRS)**
5. **Architecture**
6. **QA-to-Red**
7. **PBFAG**
8. **Implementation Plan**
9. **Builder Checklist**
10. **IAA Pre-Brief**
11. **Builder Appointment**
12. **Build**

This order is normative. It is not a loose recommendation. No stage may be skipped, collapsed, or reordered without explicit CS2 approval.

### Stage 1 — App Description
The App Description stage defines the constitutional product truth of AMC.

This stage shall establish:
- what AMC is
- why AMC exists
- what executive role it serves in the estate
- which actors matter
- how authority is structured
- what AI role model applies
- what approval, audit, state, and UX significance attaches to the product
- what strategic direction and boundaries must govern all later work

Stage 1 is complete only when AMC’s product truth is clear enough for downstream artifacts to derive from it without guesswork.

### Stage 2 — UX Workflow & Wiring Spec
The UX Workflow & Wiring Spec stage defines the user-facing interaction model and system-level wiring for AMC before functional requirements are formally specified.

For AMC, this means defining:
- executive user journeys across dashboard, alerts, approvals, and interventions
- conversation and escalation interaction patterns
- AIMC-mediated AI interaction surfaces
- upload / ingestion status surfaces (sourced from AIMCC)
- mobile and desktop operating patterns
- how executive actions connect to backend execution pathways

The UX Workflow & Wiring Spec must remain faithful to Stage 1 identity. It may not narrow AMC into a simpler product than was approved. It must be approved before FRS derivation begins.

### Stage 3 — Functional Requirements Specification (FRS)
The FRS stage translates approved Stage 1 truth and the UX Workflow & Wiring Spec into concrete functional capability requirements.

For AMC, this means deriving requirements for:
- executive visibility
- proactive notifications and alert classes
- approval flows and intervention launch
- escalation behavior
- conversation with Maturion
- AIMC-routed AI action results
- AIMCC / Knowledge Upload Centre oversight surfaces
- memory-aware operational surfaces
- wellbeing, maintenance, and assurance reporting
- continuity across devices and contexts

The FRS must remain faithful to Stage 1 and may not narrow AMC into a simpler product than was approved.

### Stage 4 — Technical Requirements Specification (TRS)
The TRS stage translates functional requirements into technical obligations and constraints.

For AMC, the TRS must define the technical requirements needed to preserve:
- authority separation
- approval enforcement
- governed AI integration through AIMC
- AIMCC / Knowledge Upload Centre integration
- knowledge / memory system integration
- notification behavior
- shared-state continuity
- authentication and authorization controls
- auditability
- sandbox boundary integrity
- cross-device continuity where applicable

TRS may not dilute constitutional significance into vague technical aspiration.

### Stage 5 — Architecture
The Architecture stage defines the structural realization of approved product and technical truth.

For AMC, Architecture must express:
- how Maturion, Foreman, and other agent layers remain structurally distinct
- how AIMC is integrated as the sole governed AI gateway
- how AIMCC and Knowledge Upload Centre are integrated as governed knowledge pathways
- how the knowledge / memory system is surfaced without AMC becoming its canonical owner
- how shared state is organized across AMC, AIMC, AIMCC, and the knowledge / memory system
- how approvals, escalations, and interventions are routed
- how auth, audit, and sandbox boundaries are made real
- how the executive UX model is technically supported

Architecture is the stage at which the product becomes structurally credible, but it must not become a substitute for upstream product-definition approval.

### Stage 6 — QA-to-Red
The QA-to-Red stage requires that a comprehensive test suite be written and placed in RED (failing) state before any implementation begins.

For AMC, the QA-to-Red suite must include:
- tests for executive alerting behavior
- tests for approval and intervention flows
- tests for AIMC-routed AI action pathways
- tests for AIMCC / upload oversight surfaces
- tests for memory-aware retrieval behavior
- tests for degraded-dependency behavior (AIMC unavailable, AIMCC unavailable, memory degraded)
- tests for audit event generation
- tests for authority boundary enforcement

QA-to-Red is signed off by Foreman before any builder is appointed. Implementation must make these tests GREEN.

### Stage 7 — PBFAG
The Pre-Build Functionality Assessment Gate (PBFAG) is a hard readiness gate that must PASS before any builder is appointed.

For AMC, the PBFAG must confirm:
- all Stage 1 through 5 artifacts exist, are approved, and are sufficiently stable
- the Red QA suite (Stage 6) exists and is signed off
- AIMC integration readiness is confirmed
- AIMCC / Knowledge Upload Centre integration readiness is confirmed
- memory-system dependency clarity exists
- audit model readiness is confirmed
- state ownership readiness is confirmed
- no materially unresolved design gaps block implementation

PBFAG is a constitutional gate. It is not a situational advisory review.

### Stage 8 — Implementation Plan
The Implementation Plan stage decomposes approved architecture into executable work packages and sequencing decisions.

For AMC, build planning must preserve:
- lifecycle fidelity
- authority fidelity
- approval fidelity
- audit fidelity
- AI-role fidelity (all AI flows through AIMC)
- knowledge-ingestion fidelity (all ingestion through AIMCC / Knowledge Upload Centre)
- shared-state fidelity
- mobile/proactive operating intent

Detailed planning must not optimize away strategically important requirements merely because they are harder to build.

### Stage 9 — Builder Checklist
The Builder Checklist stage formalizes the specific delivery obligations, acceptance criteria, and evidence requirements that each builder must satisfy.

For AMC, the builder checklist must explicitly include:
- implementation of all Red QA tests (must be GREEN at handover)
- AIMC integration evidence
- AIMCC / Knowledge Upload Centre integration evidence
- audit trail evidence
- authority boundary evidence
- mobile / desktop verification evidence

No builder may be considered done without completing the builder checklist.

### Stage 10 — IAA Pre-Brief
The IAA Pre-Brief stage requires that the Independent Assurance Agent is briefed before builder work begins on qualifying tasks.

For AMC, the IAA Pre-Brief must cover:
- the wave scope
- the artifact bundle expected
- the authority and boundary checks IAA must verify
- the AIMC / AIMCC / knowledge integration checks
- the audit and state ownership checks

IAA Pre-Brief publication is a blocking gate. No qualifying builder work may begin before it is published.

### Stage 11 — Builder Appointment
The Builder Appointment stage is Foreman issuing the formal "Build to Green" order to the appointed builder, after all gates 1-10 are satisfied.

For AMC, builder appointment must reference:
- the wave record and pre-brief
- the approved architecture
- the Red QA suite (to be made GREEN)
- the builder checklist obligations

No builder may self-appoint. Foreman appoints after confirming all prerequisite stages are gate-passed.

### Stage 12 — Build
Build is the stage at which the appointed builder implements approved design under Foreman supervision, turning the Red QA suite GREEN.

For AMC, implementation is subordinate to approved upstream artifacts and must not:
- invent new product roles
- silently transfer authority
- bypass approval significance
- omit audit-critical behavior
- bypass AIMC for AI execution
- bypass AIMCC / Knowledge Upload Centre for knowledge ingestion
- collapse state, auth, or AI separation for convenience

Where implementation finds contradiction or insufficiency upstream, it must escalate rather than improvise.

### Entry and Exit Logic
Each lifecycle stage must have an entry condition and an exit condition, whether defined formally in later artifacts or as governance gates.

At minimum:
- a stage may not begin until its required upstream truth exists in usable form
- a stage may not be treated as complete merely because work has started
- a downstream stage must not silently compensate for an incomplete upstream stage
- completion claims must be supported by artifacts, not by implied momentum

For AMC, this is critical because Stage 1 truth is carrying constitutional product meaning, not just descriptive text.

### Stage-Gate Integrity Rule
AMC shall operate with stage-gate integrity.

This means:
- unresolved Stage 1 (App Description) truth blocks reliable Stage 2 (UX Workflow & Wiring Spec) derivation
- unresolved Stage 2 truth blocks reliable Stage 3 (FRS) derivation
- unresolved Stage 3 (FRS) truth blocks reliable Stage 4 (TRS) derivation
- unresolved Stage 4 (TRS) truth blocks reliable Stage 5 (Architecture)
- unresolved Architecture blocks reliable Stage 8 (Implementation Plan) planning
- unresolved Implementation Plan blocks Stage 9 (Builder Checklist) formalization
- unresolved pre-build stages (1–9) block Stage 10 (IAA Pre-Brief) and Stage 11 (Builder Appointment)
- Stage 12 (Build) may not begin until all stages 1–11 are gate-passed

Where overlap occurs for practical workflow reasons, the overlap must not erase gate discipline.

### Lifecycle Drift Prevention
The lifecycle model must explicitly prevent the following failure patterns:
- Architecture redefining the product
- implementation redefining authority
- build planning weakening audit or approval significance
- technical convenience collapsing AI role separation
- frontend convenience replacing shared-state design
- build or deployment urgency bypassing readiness gates

AMC is particularly vulnerable to these drifts because its most important requirements concern control, authority, and executive behavior rather than simple CRUD functionality.

### Relationship to PBFAG and Derivation Discipline
The lifecycle model is coupled to the PBFAG gate (Stage 7) and the Requirements Derivation Chain.

This means:
- Stage 1 must be pre-build ready before derivation proceeds
- each later stage must be traceable to upstream truth
- unresolved contradictions must be escalated upstream
- stage progression must be evidence-based rather than assumed

The lifecycle section should therefore be read as the operating order of the derivation chain, not as a separate informal planning note.

### Minimum Lifecycle Checklist
The following minimum conditions must hold for all 12 stages:

- [ ] Stage 1 (App Description) is approved or sufficiently stabilized for derivation
- [ ] Stage 2 (UX Workflow & Wiring Spec) is approved before FRS derivation begins
- [ ] Stage 3 (FRS) derives functional behavior from Stage 1 and Stage 2 truth
- [ ] Stage 4 (TRS) derives technical obligations from approved FRS and governance constraints
- [ ] Stage 5 (Architecture) derives structural design from approved FRS, TRS, and App Description
- [ ] Stage 6 (QA-to-Red) exists, is signed off by Foreman, and covers all critical AMC behaviors
- [ ] Stage 7 (PBFAG) gate has PASSED — no stage 8 or beyond begins without this
- [ ] Stage 8 (Implementation Plan) does not rewrite product meaning or authority
- [ ] Stage 9 (Builder Checklist) reflects all acceptance criteria from upstream artifacts
- [ ] Stage 10 (IAA Pre-Brief) is published before any qualifying builder work begins
- [ ] Stage 11 (Builder Appointment) is formally issued by Foreman after stages 1–10 are gate-passed
- [ ] Stage 12 (Build) remains subordinate to approved design; contradictions are escalated, not resolved unilaterally
- [ ] All stage completion claims are supported by artifacts and evidence

### Downstream Design Consequence
All teams and agents contributing to AMC must work as participants in a governed lifecycle, not as independent authors of product meaning.

The lifecycle order exists to protect the product from constitutional drift. Where speed pressures arise, lifecycle discipline remains mandatory.

### Non-Negotiable Principle
AMC build lifecycle stages must enforce the correct order of truth formation, design formation, build formation, and verification.

Any approach that allows the executive operating centre of the estate to be substantially defined by downstream improvisation rather than approved staged development is non-compliant with the intended purpose of AMC.


## §6 — Requirements Derivation Chain (§AD-02)

The AMC App Description is the upstream source authority for the downstream requirements and design stack.

This section exists to prevent a common failure pattern in complex builds: later artifacts begin to invent product truth, shift authority boundaries, soften approval significance, or reinterpret strategic intent because the derivation chain from Stage 1 was not made explicit. For AMC, that risk is especially serious because the application is not a routine dashboard. It is intended to become the executive operating surface of the Maturion estate, with deep implications for authority, AI behavior, approvals, audit, state, and operational control.

The requirements derivation chain for AMC shall therefore be explicit, governed, and traceable.

### Purpose of the Derivation Chain
The derivation chain shall exist to ensure that downstream artifacts do not become independent sources of product truth.

Its purpose is to preserve:
- the identity of AMC as the executive control centre of the estate
- the authority model involving Johan Ras, Maturion, Foreman, and other governed actors
- the significance of approval and reserved-matter boundaries
- the governed role of AI within the estate
- the need for auditability, shared-state coherence, and proactive executive awareness
- the distinction between product truth, technical realization, and implementation detail

Downstream work may deepen, specify, and operationalize Stage 1 truth, but it may not silently replace it.

### Core Principle
Each downstream artifact shall derive from an upstream approved artifact and must remain traceable back to Stage 1 product truth.

No downstream artifact may:
- invent a materially new product role without approval
- redefine authority relationships without approval
- weaken approval or audit requirements by omission
- reinterpret AMC as a narrower or different type of application than approved
- convert reserved-matter significance into routine implementation detail
- collapse AI role distinctions that Stage 1 established

If downstream work discovers that Stage 1 is incomplete or contradictory, the correct response is to amend Stage 1 through governance, not to improvise product truth elsewhere.

### Authoritative Derivation Order
The authoritative derivation order for AMC shall be:

1. **Stage 1 — App Description** (this document — authoritative product truth)
2. **Stage 2 — UX Workflow & Wiring Spec** (derived from App Description)
3. **Stage 3 — Functional Requirements Specification (FRS)** (derived from App Description and UX Workflow & Wiring Spec)
4. **Stage 4 — Technical Requirements Specification (TRS)** (derived from FRS and App Description technology baseline)
5. **Stage 5 — Architecture** (derived from FRS, TRS, and App Description)
6. **Stage 6 — QA-to-Red** (derived from Architecture and approved requirements; test suite placed RED before build)
7. **Stage 7 — PBFAG** (readiness gate — all stages 1–6 must be complete and approved)
8. **Stage 8 — Implementation Plan** (derived from approved Architecture; decomposes into work packages)
9. **Stage 9 — Builder Checklist** (derived from Implementation Plan; formalizes acceptance criteria per builder)
10. **Stage 10 — IAA Pre-Brief** (derived from wave scope; briefing of Independent Assurance Agent before builder work begins)
11. **Stage 11 — Builder Appointment** (Foreman issues "Build to Green" order after stages 1–10 gate-passed)
12. **Stage 12 — Build** (builder implements approved design; turns Red QA suite GREEN)

This order is normative. Later artifacts may not leapfrog earlier unresolved truth or treat later-stage assumptions as if they were equivalent to approved upstream intent.

### Role of the App Description
The AMC App Description defines:
- what AMC is
- why AMC exists
- what problem it solves
- what operating role it serves in the estate
- which authority relationships matter
- what kinds of actions and decisions are constitutionally significant
- what AI role model applies
- what state, audit, and notification significance attaches to the application

The App Description is therefore the constitutional product-definition artifact for AMC.

### Role of the Functional Requirements Specification (FRS)
The FRS shall derive functional behavior from the approved App Description.

For AMC, the FRS must translate Stage 1 truth into concrete functional capabilities such as:
- executive visibility capabilities
- proactive notification behavior
- approval and escalation flows
- conversation and executive interaction capabilities
- intervention-launch and follow-through capabilities
- specialist and sandbox oversight functions
- audit-facing functional behavior
- stateful continuity behavior across devices and contexts

The FRS may not decide that AMC is “just a dashboard” or “just a chat interface” if Stage 1 defines it as an executive operating environment.

### Role of the Technical Requirements Specification (TRS)
The TRS shall derive technical obligations from the FRS and the governance-constrained meaning of the App Description.

For AMC, the TRS must define technical requirements that preserve:
- authority separation
- approval enforcement
- AI integration discipline
- auditability
- shared-state coherence
- authentication and authorization controls
- sandbox boundary integrity
- notification and continuity requirements

The TRS must not reduce governance-significant requirements into vague non-functional aspirations.

### Role of Architecture
The Architecture artifact shall define the technical structure required to realize the TRS while preserving the product and governance truth defined upstream.

For AMC, architecture must express:
- how the executive operating model is structurally supported
- how Maturion, Foreman, and other agent layers remain distinguishable
- how shared state is organized
- how approval, escalation, and intervention flows are routed
- how AIMC-based AI integration is enforced
- how audit, auth, and sandbox boundaries are made real
- how mobile and desktop continuity are supported

Architecture may not rewrite the product by “solving” ambiguity with unapproved structural shortcuts.

### Role of Detailed Design and Build Planning
Detailed design and build planning shall decompose the approved architecture into deliverable work packages without changing the governing truth of the product.

For AMC, detailed planning must remain faithful to:
- the authority chain
- the notification model
- the approval model
- the audit model
- the shared-state model
- the AI role model
- the control-plane identity of AMC

This means work planning must not optimize away constitutional significance in the name of speed or convenience.

### Role of Implementation Artifacts
Implementation artifacts realize the approved design. They are not the place where product identity or authority theory is discovered for the first time.

For AMC, implementation must remain subordinate to:
- approved Stage 1 truth
- approved FRS
- approved TRS
- approved Architecture
- approved design and governance decisions

Where implementation encounters a conflict, it must escalate rather than silently reinterpret the product.

### Role of Verification, Assurance, and Operationalization
Verification and assurance artifacts confirm that delivered behavior remains aligned with approved truth.

For AMC, verification and assurance must be able to test or inspect whether:
- authority boundaries were preserved
- approval-sensitive behavior was implemented correctly
- AI role separation was preserved
- audit expectations were satisfied
- shared-state coherence was achieved
- mobile/proactive executive-awareness behavior exists as intended
- sandbox and specialist boundaries remain governed

Operationalization artifacts, including runbooks and rollout materials, must also derive from the approved design rather than introducing fresh authority assumptions.

### Traceability Requirement
Each materially significant requirement introduced downstream must be traceable back to at least one approved upstream source.

Acceptable upstream sources are:
- this App Description
- approved governance canon
- an approved amendment to this App Description
- an approved decision record that formally clarifies an ambiguity

Traceability must be strong enough that a reviewer can answer:
- where did this requirement come from
- what approved product truth does it preserve
- what downstream artifact implements it
- what verification activity confirms it

A requirement with no traceable source is a governance defect.

### Non-Derivable Assumption Rule
The following may not be introduced downstream as casual assumptions:
- changes to AMC’s core identity
- changes to the Maturion/Foreman relationship
- hidden expansion or contraction of reserved-matter significance
- changes to approval obligations
- ungoverned AI-role collapsing
- removal of proactive-awareness behavior
- removal of mobile-context significance
- weakening of audit or shared-state expectations

If such a change is desired, it must be proposed and approved at the correct upstream layer.

### External Integration Derivation Rule

All downstream artifacts that involve external integrations must explicitly derive their integration scope from this App Description.

Specifically, downstream artifacts must explicitly address derivation for:

- **AIMC integration**: the FRS, TRS, Architecture, and Implementation Plan must each derive their AIMC integration scope from this document. No downstream artifact may independently invent AIMC integration scope without traceable derivation from Stage 1.
- **AIMCC / Knowledge Upload Centre integration**: similarly, all downstream derivation of AIMCC integration scope must trace back to this document's AIMCC boundary definitions.
- **Knowledge / memory operating model**: downstream artifacts that involve knowledge retrieval, memory surfacing, or knowledge-aware operations must derive from this document's estate-capability model for the knowledge / memory system.
- **Executive alerts**: FRS and TRS must derive alert classes, priorities, and escalation behavior from Stage 1 success criteria and scope.
- **Approvals / interventions**: every approval gate and intervention pathway in downstream artifacts must be traceable to a Stage 1 authority or scope declaration.
- **Audit / provenance**: downstream audit design must derive from Stage 1 audit significance declarations, not be invented independently.
- **State ownership**: downstream state models must derive from Stage 1 state-boundary declarations. AMC-owned state, AIMCC-owned state, and knowledge-system-owned state must remain distinguishable in all downstream artifacts.

A downstream artifact that introduces new external integration scope without tracing back to this document represents a governance defect and must trigger an upstream amendment request.

### Contradiction / Ambiguity Handling Rule
If a downstream artifact encounters contradiction, incompleteness, or ambiguity in upstream material, the correct handling path is:

1. identify the ambiguity or contradiction explicitly
2. suspend the affected downstream assumption
3. escalate for Stage 1 or governance clarification
4. record the resulting decision or amendment
5. resume derivation only once the upstream truth is stable enough

Downstream improvisation is not an acceptable contradiction-handling strategy for AMC.

### Derivation Integrity Across Sections
For AMC, the derivation chain must preserve the connection between the most strategically significant Stage 1 sections and later artifacts.

At minimum, downstream work must remain faithful to:
- `§4 Strategic Context`
- `§12 PBFAG Checklist Requirements`
- `§13 Agent Authority Chain`
- `§17 Auth Wiring Checklist`
- `§18 AI Integration Requirements`
- `§23 Notification/UX Patterns`
- `§24 Shared State Architecture`
- `§25 API Authentication`
- `§26 Audit Log Design`

These sections carry much of the constitutional and executive meaning of the application and must not be diluted downstream.

### Minimum Derivation Checklist
The following minimum conditions must hold for derivation integrity:

- [ ] App Description is treated as the upstream product-definition authority
- [ ] FRS derives functional capability from approved Stage 1 truth
- [ ] TRS derives technical obligations from approved FRS and governance constraints
- [ ] Architecture derives structural design from approved TRS and upstream product truth
- [ ] Detailed design and implementation planning do not rewrite product meaning
- [ ] Requirements are traceable across artifacts
- [ ] Contradictions are escalated rather than improvised away
- [ ] No downstream artifact weakens authority, approval, audit, AI, or state requirements by omission
- [ ] Verification artifacts can test against traceable approved requirements
- [ ] Operationalization artifacts do not introduce unapproved authority assumptions

### Downstream Design Consequence
All downstream artifact authors working on AMC must understand that they are not authoring against a blank slate. They are deriving from a constitutionally significant Stage 1 artifact.

This means that speed, convenience, framework defaults, and technical elegance are all subordinate to derivation fidelity where a conflict arises.

### Non-Negotiable Principle
The AMC requirements derivation chain must ensure that the executive operating centre of the estate is built from approved truth, not from downstream improvisation.

Any derivation process that allows later artifacts to redefine AMC’s role, authority model, AI behavior, approval significance, audit expectations, or state responsibilities without upstream approval is non-compliant with the intended purpose of AMC.


## §7 — Technology Stack (§AD-03)

> **Rule**: TRS is the downstream authoritative realization of this baseline. Any discrepancy between this section and TRS is a blocking defect that must be resolved before Architecture commences.

### Authoritative Technology Stack

| Layer | Technology | Notes |
|-------|------------|-------|
| **Frontend Framework** | React 18 + Vite | Executive dashboard and mobile-capable presentation layer |
| **Language** | TypeScript 5.x | Type-safe authority-aware frontend and edge code |
| **State Management** | React Context / Zustand | Auth state and UI state — see §AD-20 |
| **Database** | Supabase (PostgreSQL) | Tenant-isolated relational persistence |
| **Auth** | Supabase Auth | JWT-based; identity separation required — see §AD-14 |
| **AI Integration** | AIMC Gateway | Direct provider calls prohibited — see §AD-14 |
| **Edge Functions** | Supabase Edge Functions | Serverless orchestration boundary — see §AD-15 |
| **Deployment** | Vercel | Governed deployment environment |
| **CI/CD** | GitHub Actions | Foreman-governed build pipeline |
| **Notification/UX** | react-hot-toast | Executive feedback surface — see §AD-19 |

AMC shall declare a governed technology-stack baseline that is strong enough to constrain downstream design, but disciplined enough not to pretend that Stage 1 is the final architecture.

### Cross-System Platform Dependencies

AMC depends on the following governed external platform systems. These are not optional integrations. They are constitutional platform dependencies that AMC must interact with through governed interfaces only.

| Platform System | Role in AMC | AMC Constraint |
|---|---|---|
| **AIMC Gateway / AIMC services** | Sole governed AI execution pathway | AMC must route all AI model interactions through AIMC. Direct model provider calls from AMC are prohibited. |
| **AIMCC services** | Knowledge ingestion and memory operations layer | AMC must route all knowledge ingestion and memory operation requests through AIMCC. AMC may surface AIMCC-sourced data but must not become the canonical owner. |
| **Knowledge Upload Centre** | Governed ingestion surface | All document / knowledge upload actions from AMC context must route through the Knowledge Upload Centre, which operates under AIMCC governance. |
| **Knowledge / memory system** | Persistent estate knowledge and memory substrate | AMC may query and present knowledge / memory references through governed APIs. AMC must not duplicate or privately cache persistent knowledge truth. |

**Non-bypass rule**: AMC must not circumvent any of the above governed layers, even for operational convenience, degraded-mode workarounds, or implementation efficiency. Any pathway that bypasses a governed layer is a governance violation.

These cross-system dependencies must be explicitly addressed in TRS and Architecture. They are not implementation details to be decided later.

This section exists because AMC is not a neutral technical shell into which any convenient stack may be dropped. AMC is intended to become the executive operating centre of the Maturion estate. Its technical baseline must therefore support authority integrity, AI governance, auditability, shared-state coherence, mobile continuity, proactive notification, sandbox-aware operation, and progressive delegation.

For AMC, the technology stack is not merely an implementation preference. It is part of the product’s governance and operational feasibility model.

### Purpose of the Technology Stack Baseline
The AMC technology-stack baseline shall exist to ensure that downstream FRS, TRS, and Architecture work begin inside an approved technical envelope rather than drifting into convenience-driven or governance-weak implementation choices.

The baseline must:
- define the major technical capability layers AMC requires
- constrain architectural drift
- preserve compatibility with governance canon
- preserve compatibility with AIMC-governed AI integration
- preserve the possibility of mobile and desktop executive operation
- preserve the possibility of audit-first and authority-aware system behavior

If the technical baseline is left undefined, downstream design may accidentally choose tools or patterns that are structurally hostile to AMC’s intended operating model.

### Core Principle
The AMC technology stack must be selected for governance compatibility, authority safety, auditability, continuity, and controlled extensibility, not merely for implementation convenience.

This means technology choices must support:
- executive control rather than uncontrolled automation
- identity and authority separation rather than flattened access models
- audit-linked consequential action rather than opaque side effects
- controlled AI integration rather than direct unmanaged provider coupling
- coherent shared state rather than fragmented local truth
- bounded sandbox operation rather than blurred environment boundaries
- safe progressive delegation rather than hidden privilege expansion

A technically fashionable stack that weakens these properties is non-compliant.

### Baseline Stack Categories
AMC shall be expected to include, at minimum, the following stack categories:

- **presentation layer**
- **application and orchestration layer**
- **identity and access-control layer**
- **data and persistence layer**
- **shared-state and synchronization layer**
- **audit and observability layer**
- **notification and communication layer**
- **AI integration and routing layer**
- **integration and service-boundary layer**
- **deployment and environment-management layer**

The specific technologies chosen for these categories will be finalized in downstream artifacts, but these layers themselves are mandatory.

### Presentation Layer
AMC requires a presentation layer capable of executive operation across desktop and mobile contexts.

The presentation layer must support:
- responsive operation across device classes
- dashboard and drill-down workflows
- conversation surfaces with Maturion
- approval and escalation interaction patterns
- intervention initiation and follow-through visibility
- continuity of executive context across navigation
- clear distinction between informational, warning, approval, and emergency states

Technology choices for the presentation layer must be evaluated not only for UI productivity, but also for their ability to support governed executive operation and shared-state coherence.

### Application and Orchestration Layer
AMC requires an application layer capable of coordinating stateful executive workflows, approval-sensitive actions, escalation routing, intervention handling, and agent-aware operations.

This layer must support:
- authority-aware action handling
- workflow coordination across multiple actor classes
- clear separation between executive coordination and implementation execution
- enforceable business logic around approvals, escalation, and bounded delegation
- reliable connection to audit, notification, state, and AI-routing services

The application layer must not be designed as a loose collection of ad hoc handlers with hidden privilege assumptions.

### Identity and Access-Control Layer
AMC requires a strong identity and access-control layer that can distinguish between human, AI, agent, sandbox, and service identities.

This layer must support:
- strong authentication for privileged human activity
- distinguishable identities for Maturion, Foreman, maintenance, assurance, specialist, and service actors
- authority evaluation beyond simple login status
- reserved-matter protection
- approval-gated action enforcement
- sandbox-bound identity and scope control
- least-privilege internal service behavior

Any stack choice that makes these distinctions difficult to implement or reason about is a poor fit for AMC.

### Data and Persistence Layer
AMC requires a persistence layer capable of supporting:
- executive context continuity
- conversation continuity where appropriate
- approval and escalation state
- intervention state
- audit records
- agent and environment metadata
- notification history
- sandbox and bounded-environment data where relevant
- restoration of operational continuity across sessions and devices

The persistence layer must be selected with governance-sensitive access control, traceability, and structural clarity in mind.

### Shared-State and Synchronization Layer
AMC requires a shared-state model that can preserve one coherent operating picture across multiple surfaces and interaction modes.

The stack baseline must therefore support:
- clearly defined state domains
- reliable synchronization between surfaces
- freshness and stale-view handling
- consistent representation of pending vs resolved matters
- cross-device continuity where required
- clear relationship between durable state and real-time or transient state

A stack that encourages isolated page-local truth at the expense of estate-level coherence is not appropriate for AMC.

### Audit and Observability Layer
AMC requires a first-class audit and observability layer.

This layer must support:
- structured audit trails for consequential actions
- authority-linked event attribution
- approval and intervention traceability
- AI-mediated action traceability
- notification and escalation traceability
- diagnostic visibility into operational health
- support for assurance, maintenance, and governance review

Audit and observability must not be bolted on later as secondary concerns. The technical stack must make them feasible from the start.

### Notification and Communication Layer
AMC requires a notification and communication layer capable of supporting:
- proactive executive notifications
- escalation prompts
- approval prompts
- multi-context delivery, including mobile-relevant operation
- conversational interaction patterns with Maturion
- reliable linkages between notifications, actions, and audit records

This layer must be designed for signal quality, prioritization, and governance sensitivity rather than generic message blasting.

### AI Integration and Routing Layer
AMC requires a governed AI integration layer.

This layer must:
- route AI capability through AIMC and AIMC Gateway patterns
- preserve provider abstraction
- support role distinction between executive AI, orchestration AI, specialist AI, maintenance AI, and assurance AI
- prevent direct uncontrolled provider coupling in app code
- support auditability and policy enforcement
- allow future evolution of model selection without rewriting the product

This requirement is non-negotiable because AMC is intended to be deeply AI-enabled without becoming AI-governance-fragile.

### Integration and Service-Boundary Layer
AMC requires controlled integration with internal services, estate components, sandboxes, notifications, AI services, audit services, and operational tooling.

The integration layer must support:
- governed service-to-service identity
- bounded API interaction
- environment separation
- clear contracts between components
- safe ingress and egress of operational events
- controlled interaction with consumer apps and bounded sandboxes

Integration boundaries must remain explicit so that executive control does not degrade into uncontrolled backend sprawl.

### Deployment and Environment-Management Layer
AMC requires a disciplined deployment and environment-management layer.

This layer must support:
- environment separation
- governed secret handling
- rollout control
- rollback capability
- operational verification
- compatibility with audit and monitoring requirements
- safe management of privileged configuration, routing policy, and AI-service connectivity

Deployment technology must reinforce operational control rather than weaken it.

### Baseline Technical Characteristics
Regardless of the final specific tools chosen, the AMC stack must exhibit the following characteristics:

- **governance compatibility**
- **strong identity separation**
- **authority-aware enforcement capability**
- **audit-first design compatibility**
- **shared-state support**
- **mobile-aware delivery capability**
- **AI-routing discipline**
- **sandbox-aware extensibility**
- **operational observability**
- **deployment discipline**
- **future-evolution flexibility**

These characteristics are more important at Stage 1 than naming a final vendor for every layer.

### Technology Selection Constraints
Downstream stack selection must respect the following constraints:

- no uncontrolled direct LLM/provider calls from application logic where AIMC-governed routing is required
- no identity model that collapses human, AI, agent, and service roles into indistinct access principals
- no state model that makes executive context coherence impractical
- no audit model dependent solely on scattered infrastructure logs
- no notification mechanism that cannot support governed executive awareness patterns
- no sandbox model that makes environment or authority boundaries technically weak
- no deployment pattern that undermines rollback, secret discipline, or environment separation

These are exclusion constraints as much as they are positive requirements.

### Stage 1 Stack Declaration vs Later Stack Finalization
Stage 1 does not need to freeze every library, framework, or hosting choice. However, it must define the technology-stack envelope tightly enough that later stages cannot plausibly claim that AMC could be delivered on a stack that contradicts its governing intent.

Accordingly:
- Stage 1 defines the required stack categories and governing technical characteristics
- FRS clarifies which product capabilities drive those categories
- TRS defines the technical requirements those capabilities impose
- Architecture selects and structures the final implementation approach within the approved envelope

This prevents premature overcommitment while still preserving governance discipline.

### Minimum Technology Stack Checklist
The following minimum conditions must hold for AMC stack readiness:

- [ ] Presentation-layer needs for desktop and mobile executive operation are recognized
- [ ] Application-layer needs for approvals, escalations, interventions, and actor-aware workflows are recognized
- [ ] Identity and access-control needs for multiple actor classes are recognized
- [ ] Persistence needs for state, audit, approvals, and continuity are recognized
- [ ] Shared-state and synchronization needs are recognized
- [ ] Audit and observability are recognized as first-class stack concerns
- [ ] Notification and communication capability is recognized as a dedicated stack concern
- [ ] AIMC-governed AI integration is recognized as mandatory
- [ ] Integration and service-boundary control is recognized as necessary
- [ ] Deployment and environment-management discipline is recognized as necessary
- [ ] No selected or implied technology direction contradicts AMC’s authority, audit, AI, or state requirements

### Downstream Design Consequence
Downstream FRS, TRS, and Architecture work must interpret the technology stack section as a governed baseline, not as a blank slate and not as a fully frozen final architecture.

This means:
- stack selection must be justified against AMC’s constitutional and operational needs
- technical convenience cannot override authority, audit, or AI-governance requirements
- later artifacts must show how the selected stack preserves the baseline characteristics established here

### Non-Negotiable Principle
AMC’s technology stack must be chosen to support governed executive operation of the estate, not merely to make implementation easy.

Any stack direction that weakens authority separation, auditability, AI-governance discipline, executive continuity, or bounded extensibility is non-compliant with the intended purpose of AMC.


## §8 — Deliverable Artifacts (§AD-04)

AMC shall define an explicit downstream artifact stack so that its executive operating model, authority model, AI model, approval model, audit model, and state model can be translated into governed build reality without omission or drift.

This section exists because AMC is not a simple single-document product. It is intended to become the executive operating centre of the Maturion estate. That means the App Description alone is not sufficient to carry the full build burden. A structured set of downstream artifacts must be produced so that Stage 1 truth becomes functionally specified, technically constrained, architecturally realized, operationally governed, and verifiably delivered.

For AMC, deliverable artifacts are therefore not optional documentation extras. They are part of the governed delivery system.

### Purpose of the Deliverable Artifact Stack
The AMC deliverable artifact stack shall exist to ensure that no strategically important part of the product is left implicit during delivery.

The artifact stack must make it possible to:
- derive functional behavior from Stage 1 truth
- derive technical obligations from approved functional truth
- define structure without rewriting product meaning
- preserve authority, approval, audit, and AI-role boundaries
- coordinate build execution in a traceable way
- verify what was actually delivered
- operate the application under governed conditions once live

If a strategically important product concern exists but no artifact is responsible for carrying it downstream, that is a governance defect.

### Core Principle
Each deliverable artifact must have a clear role in the lifecycle and derivation chain.

No artifact may exist merely because it is customary, and no strategically necessary artifact may be omitted merely because it feels administratively inconvenient.

For AMC, the artifact stack must preserve:
- executive operating purpose
- authority fidelity
- AI integration discipline
- approval significance
- audit significance
- shared-state coherence
- sandbox and specialist boundary integrity
- mobile and proactive operating behavior
- deployment and operational readiness

### Minimum Required Artifact Categories
AMC shall produce, at minimum, artifacts in the following categories:

- **product-definition artifacts**
- **requirements artifacts**
- **technical-design artifacts**
- **build-planning artifacts**
- **implementation and evidence artifacts**
- **verification and assurance artifacts**
- **deployment and operational artifacts**
- **governance and approval-trace artifacts**
- **tracking and stage-control artifacts**

The exact filenames and repository locations may be finalized later, but the categories themselves are mandatory.

### Product-Definition Artifacts
The product-definition layer shall include the artifacts that define what AMC is and how its executive operating model is intended to function.

At minimum, this includes:
- the AMC App Description
- the AMC role, authority, and operating-model companion artifact
- approval records for key Stage 1 decisions
- any recorded decision artifacts required to clarify authority, scope, canonical location, or strategic direction

These artifacts define the governing truth from which all other artifacts derive.

### Requirements Artifacts
The requirements layer shall define what AMC must do.

At minimum, this includes:
- Functional Requirements Specification (FRS)
- Technical Requirements Specification (TRS)

For AMC, these artifacts must explicitly carry forward:
- executive dashboard and visibility behavior
- proactive notification behavior
- conversation behavior with Maturion
- approval and escalation behavior
- intervention-related capabilities
- specialist and sandbox oversight requirements
- auth, audit, and state expectations
- cross-device and continuity expectations

Requirements artifacts must not flatten AMC into a generic admin application.

### Technical-Design Artifacts
The technical-design layer shall define how the approved requirements will be structurally realized.

At minimum, this includes:
- Architecture document
- data and state design artifacts
- API and auth design artifacts
- audit design artifacts
- notification and UX workflow design artifacts
- AI-integration design artifacts
- sandbox-boundary and specialist-agent design artifacts where relevant

For AMC, this layer is especially important because many of the most important product truths are structural rather than cosmetic.

### Build-Planning Artifacts
The build-planning layer shall define how approved design is decomposed into executable work.

At minimum, this includes:
- implementation planning documents
- stage or wave plans
- work-package decomposition
- task sequencing artifacts
- dependency mapping
- delivery coordination artifacts
- pre-build checklist evidence where required

Build-planning artifacts must remain subordinate to approved product and technical truth. They may not silently weaken strategically significant requirements in the name of delivery efficiency.

### Implementation and Evidence Artifacts
The implementation layer shall include the artifacts produced during delivery that evidence what was actually built.

At minimum, this may include:
- implementation code and configuration
- migration artifacts
- test artifacts
- screenshots, recordings, or physical-verification evidence where relevant
- build evidence logs
- job completion artifacts
- structured evidence packages where required by governance

For AMC, implementation evidence must be capable of showing that executive, approval, audit, and state behaviors were not merely claimed but actually realized.

### Verification and Assurance Artifacts
The verification and assurance layer shall define and evidence how AMC was checked against approved expectations.

At minimum, this includes:
- test plans and results
- verification reports
- assurance reviews or assurance tokens where applicable
- rejection or remediation artifacts where applicable
- evidence of behavior validation for approvals, notifications, audit, shared state, and mobile continuity where relevant

Verification artifacts must be able to answer whether AMC’s constitutional product requirements were preserved, not just whether a page rendered successfully.

### Deployment and Operational Artifacts
The deployment and operational layer shall define how AMC is introduced into use and managed once live.

At minimum, this includes:
- deployment runbooks
- rollout plans
- rollback plans
- operational readiness checklists
- notification and escalation readiness checks
- monitoring and maintenance guidance
- authority-aware operational procedures
- environment and secret management references

Because AMC itself is a control centre, its deployment and operational artifacts must be especially disciplined.

### Governance and Approval-Trace Artifacts
AMC must maintain explicit artifacts that preserve governance and approval lineage.

At minimum, this includes:
- approval records
- decision logs where materially relevant
- tracker-linked stage approvals
- governance review notes where required
- evidence of reserved-matter handling where such matters were involved
- formal records of changes to scope, authority assumptions, or strategic intent

This category is essential because AMC is intended to manage decision significance across the estate. Its own evolution must therefore be governable and reviewable.

### Tracking and Stage-Control Artifacts
AMC shall maintain artifacts that track stage progression and readiness truthfully.

At minimum, this includes:
- stage trackers
- artifact indexes
- completion-status records
- pending-item records where appropriate
- pre-build readiness records
- stage gate records
- linkage between completed content and claimed status

Tracking artifacts must not be treated as cosmetic. They are part of the mechanism by which lifecycle and readiness discipline are enforced.

### Required Cross-System Integration Artifacts

In addition to the standard artifact categories, AMC must produce the following explicitly named integration and operating artifacts:

- **AIMC integration contract**: defines the governed interface between AMC and AIMC, including action types, routing rules, error handling, and audit requirements
- **AIMCC / Knowledge Upload Centre integration contract**: defines the governed interface between AMC and AIMCC / Knowledge Upload Centre, including upload flows, ingestion status surfacing, quota management, and error handling
- **Knowledge / memory operating contract**: defines how AMC queries, caches, presents, and attributes knowledge / memory references, and what provenance requirements apply
- **Executive alert taxonomy**: defines the complete set of alert classes, priorities, escalation routes, acknowledgment requirements, and retry/expiry behavior
- **Approval / autonomy matrix**: defines which actions require explicit approval, which are delegated, to whom, under what conditions, and with what rollback capability
- **Audit event model**: defines the complete set of audit event types, required fields (actor, source system, object, action, outcome, timestamp), retention, and provenance requirements
- **State ownership matrix**: defines which state is owned by AMC, which by AIMCC, which by the knowledge / memory system, and which is transient/cached
- **Degraded-mode runbooks**: define the fallback behavior for each external dependency (AIMC unavailable, AIMCC unavailable, Knowledge Upload Centre failure, memory retrieval degraded)
- **Stage 1 source-of-truth / cleanup decision note**: a governance note documenting the transition from FM-era Stage 1 fragments to this consolidated document as the single authoritative source after CS2 approval

### Artifact Ownership Principle
Each required artifact must have a clear ownership purpose in the lifecycle.

For every major artifact, AMC delivery should be able to answer:
- why this artifact exists
- what upstream truth it derives from
- what downstream work depends on it
- who is responsible for maintaining it
- what stage gate it supports
- what governance or assurance significance it carries

An artifact without lifecycle purpose is noise. A needed artifact without ownership is a delivery risk.

### Artifact Interdependence Rule
AMC artifact categories are interdependent and must not be treated as isolated silos.

For example:
- the App Description must inform the FRS
- the FRS must inform the TRS
- the TRS must inform Architecture
- Architecture must inform build planning
- build planning must inform implementation evidence expectations
- implementation and verification evidence must support deployment readiness
- trackers and approval records must reflect actual stage truth across all artifact layers

The artifact stack must therefore be managed as one governed system of delivery evidence.

### Artifact Completeness and Omission Rule
For AMC, omission of a strategically necessary artifact category shall be treated as a governance defect.

In particular, no delivery path is compliant if it lacks artifact coverage for:
- authority definition
- approval behavior
- AI integration control
- audit behavior
- shared-state design
- notification and UX behavior
- authentication and API control
- operationalization and rollback discipline

These are not optional themes. They are constitutive elements of AMC.

### Minimum Deliverable Artifact Checklist
The following minimum artifact expectations must be satisfied for AMC delivery readiness:

- [ ] App Description exists as the upstream product-definition artifact
- [ ] Role/authority/operating-model artifact exists or its content is fully absorbed into approved Stage 1 material
- [ ] FRS is planned or produced as the next functional derivation artifact
- [ ] TRS is planned or produced as the next technical derivation artifact
- [ ] Architecture artifact is planned or produced
- [ ] Data/state/auth/audit/notification design artifacts are identified as required downstream outputs
- [ ] Build-planning artifacts are identified as required before execution
- [ ] Verification and assurance artifacts are identified as required before acceptance
- [ ] Deployment and operational artifacts are identified as required before live use
- [ ] Approval, decision, and tracker artifacts are identified as part of governed progression
- [ ] No strategically significant concern is left without an artifact category responsible for carrying it

### Downstream Design Consequence
Downstream teams working on AMC must understand that the artifact stack is part of the product-delivery constitution.

This means:
- product truth must be preserved through artifacts
- governance significance must be preserved through artifacts
- stage progression must be evidenced through artifacts
- delivery claims must be defensible through artifacts

AMC cannot credibly become the executive operating centre of the estate if its own delivery chain is artifact-thin, weakly evidenced, or structurally unclear.

### Non-Negotiable Principle
AMC deliverable artifacts must collectively carry the full weight of the product from approved Stage 1 truth through governed delivery, verification, and operation.

Any delivery approach that leaves strategically significant parts of AMC without explicit artifact coverage is non-compliant with the intended purpose of AMC.


## §9 — Component Definition of Done (§AD-05)

An AMC component shall not be considered complete merely because it renders, responds, or appears functional in isolation.

This section exists because AMC is intended to become the executive operating centre of the Maturion estate. In such a system, a component may appear technically finished while still being constitutionally incomplete, operationally unsafe, weakly auditable, authority-ambiguous, or structurally misaligned with the executive operating model. “Definition of Done” for AMC must therefore be broader than implementation completeness. It must include governance completeness, authority completeness, audit completeness, state completeness, and operational readiness appropriate to the component’s role.

For AMC, completion is a governed standard, not a superficial delivery claim.

### Purpose of the Component Definition of Done
The AMC Component Definition of Done shall exist to ensure that each delivered component is complete in the ways that matter for this product.

The purpose of the definition is to prevent:
- technically functional but authority-unsafe components
- UI-complete but audit-incomplete components
- integrated-looking but state-incoherent components
- AI-enabled but governance-weak components
- mobile-visible but action-incomplete components
- approval-relevant features that do not actually enforce approval logic
- superficially finished components that still undermine executive-operating truth

A component that fails in any of these ways is not done for AMC.

### Core Principle
For AMC, “done” means fit for governed participation in the executive operating environment.

A component is complete only when it:
- implements approved purpose
- respects authority boundaries
- integrates correctly with approval, audit, state, and auth expectations where relevant
- behaves coherently in the larger estate-control model
- is evidentially supportable
- is ready to be reasoned about by reviewers, assurance actors, and future maintainers

The definition of done must therefore be evaluated against product meaning, not just local code completion.

### Scope of the Definition
The Component Definition of Done applies to all meaningful AMC components, including but not limited to:
- UI components with executive significance
- workflow components
- approval-related components
- notification and escalation components
- conversation-related components
- intervention-related components
- API endpoints and action handlers
- stateful service components
- agent-facing coordination components
- audit-related components
- sandbox-boundary components
- operational and integration components

The precise checklist emphasis may differ by component type, but the governing standard remains the same.

### Requirement Traceability Condition
A component is not done unless its purpose is traceable to approved upstream truth.

This means the component must be traceable to:
- the AMC App Description
- approved governance canon where relevant
- approved FRS requirements
- approved TRS requirements
- approved Architecture decisions
- approved design decisions where applicable

A component whose purpose exists only because it seemed convenient during implementation is not done.

### Purpose and Boundary Clarity Condition
A component is not done unless its purpose and operational boundary are clear.

For each component, it should be possible to answer:
- what this component exists to do
- what this component does not do
- which actors interact with it
- what authority domain it participates in
- whether it is routine, approval-gated, reserved-matter-adjacent, or sandbox-bounded
- what other components or workflows depend on it

Boundary ambiguity is especially dangerous in AMC because components often sit close to approval, audit, or executive-significance pathways.

### Authority and Approval Condition
Any component that affects decision-making, approvals, execution authority, escalation routing, or intervention behavior is not done unless authority behavior is explicitly correct.

This includes verification that:
- the component respects the authority model
- reserved-matter significance is not bypassed
- approval-gated actions are correctly gated
- delegated actions remain within delegated scope
- escalation occurs where authority is insufficient
- AI-generated suggestions are not confused with approved decisions

In AMC, a component that works but misroutes authority is incomplete.

### Authentication and Access-Control Condition
Any component that exposes, triggers, or influences consequential action is not done unless its auth expectations are clear and correctly wired.

This includes confirmation that:
- acting identities are distinguishable where required
- access is limited to the correct role and scope
- sandbox or boundary limitations are respected
- internal service interactions do not create hidden privilege expansion
- sensitive operations can enforce stronger control where required

A component with undefined or weak auth assumptions is incomplete even if the UI appears finished.

### Shared-State and Continuity Condition
Any component participating in executive awareness, alerts, approvals, conversations, interventions, or estate status is not done unless its state behavior is coherent.

This includes verification that:
- the component interacts correctly with shared-state domains
- its local state does not create contradictory truth
- pending vs resolved conditions are handled clearly
- it preserves or restores context appropriately where relevant
- cross-device or cross-surface continuity implications are understood

AMC components cannot be considered done if they locally “work” while globally fragmenting estate truth.

### Audit and Traceability Condition
Any consequential component is not done unless it preserves or supports appropriate auditability.

Depending on component type, this includes ensuring that:
- meaningful actions can be attributed
- approvals can be traced
- intervention initiation can be traced
- escalation behavior can be traced
- AI-mediated consequential behavior can be traced
- audit-linked references exist where relevant

For AMC, auditability is not a late add-on. Components that evade meaningful audit consequence are incomplete.

### Notification and UX Condition
Any user-facing or executive-facing component is not done unless it supports AMC’s intended executive-operating UX model.

This includes verification that:
- the component supports clarity of meaning
- severity or class distinctions are visible where relevant
- the user can tell whether awareness, approval, escalation, or action is involved
- mobile-context implications have been considered where relevant
- the component does not push the user back into manual system interrogation to understand what matters

A visually polished but operationally obscure component is not done.

### AI and Agent Role Discipline Condition
Any component that integrates AI or agent behavior is not done unless AI role discipline is preserved.

This includes confirmation that:
- Maturion, Foreman, specialist, maintenance, and assurance roles are not collapsed inappropriately
- AI observation, recommendation, routing, and execution behavior are distinguishable where relevant
- AIMC-governed routing assumptions are preserved
- component behavior does not silently imply broader AI authority than approved

In AMC, AI-enabled does not mean done. Governed AI-enabled is the standard.

### Sandbox and Boundary Integrity Condition
Any component operating in or across sandboxed or bounded environments is not done unless its boundaries are explicit and preserved.

This includes ensuring:
- sandbox scope is respected
- cross-boundary movement is deliberate and controlled
- estate-level significance is not silently triggered from sandbox-local activity
- boundary implications are visible in state, auth, and audit behavior where relevant

A boundary-blurring component is incomplete.

### Integration Condition
A component is not done unless its dependencies and integration points behave correctly in the governed product context.

This includes verification that:
- upstream and downstream interactions are understood
- errors and degraded states are handled meaningfully
- service integrations preserve authority and audit assumptions
- no hidden coupling undermines executive control or operational reliability

A component cannot be declared done merely by unit behavior if its integrated behavior is still unsafe or incoherent.

### Test and Verification Condition
A component is not done unless the relevant tests or verification activities for its type have been defined and completed.

Depending on component type, this may include:
- unit verification
- integration verification
- approval-path verification
- auth-path verification
- audit-path verification
- mobile interaction verification
- end-to-end workflow verification
- physical or real-environment verification where relevant

Verification depth should be proportionate to consequence, but some form of relevant evidence is always required.

### Operational Readiness Condition
Where a component materially affects live executive operation, it is not done unless operational implications are understood.

This may include:
- failure behavior
- degraded-mode behavior
- escalation behavior
- supportability
- logging or observability relevance
- deployment sensitivity
- rollback implications

AMC components that become invisible or uncontrollable under operational strain are incomplete.

### Documentation and Evidence Condition
A component is not done unless enough documentation or evidence exists to support review, maintenance, and later assurance.

This does not require bloated documentation for every small item, but it does require that consequential components have:
- identifiable design intent
- identifiable requirement source
- identifiable integration context
- identifiable test or verification evidence
- identifiable tracker impact where relevant

An undocumented consequential component is a future governance and maintenance risk.

### Minimum Definition-of-Done Checklist
The following minimum checklist must be satisfied, adapted as appropriate to component type:

- [ ] Component purpose is traceable to approved upstream truth
- [ ] Component purpose and boundary are clear
- [ ] Authority and approval behavior are correct where relevant
- [ ] Authentication and access expectations are defined where relevant
- [ ] Shared-state behavior is coherent where relevant
- [ ] Audit and traceability implications are addressed where relevant
- [ ] Notification/UX meaning is clear where relevant
- [ ] AI or agent role discipline is preserved where relevant
- [ ] Sandbox and boundary integrity is preserved where relevant
- [ ] Integrations behave correctly in context
- [ ] Relevant verification has been completed
- [ ] Operational implications are understood where relevant
- [ ] Supporting evidence or documentation exists where required

### Component-Type Sensitivity Rule
Not every component carries the same consequence, so the exact evidence burden may vary. However, lower consequence does not mean no consequence.

For AMC:
- a purely presentational low-consequence component may have a lighter completion burden
- an approval, notification, audit, auth, intervention, AI-routing, or executive-context component has a much higher completion burden
- any component touching authority, decision significance, or estate truth must be reviewed against the stricter interpretation of done

The definition of done must therefore be proportionate, but never casual.

### Downstream Design Consequence
Downstream FRS, TRS, Architecture, and build-planning artifacts must define component classes and ensure that the delivery process evaluates completion against this governed standard.

This means implementation teams and supervising agents must not use “works on my branch” or “UI complete” as substitutes for AMC component completion.

### Non-Negotiable Principle
AMC components are done only when they are technically, operationally, and constitutionally fit to participate in the executive operating environment of the estate.

Any delivery practice that treats code completion or UI completion as sufficient without authority, audit, state, approval, and integration completeness is non-compliant with the intended purpose of AMC.

### Integration and Executive Component-Family DoD

In addition to general component-level DoD, the following component families have specific DoD requirements:

**Executive alerting components:**
- alert is generated from the correct trigger condition
- alert is routed to the correct authority
- alert acknowledgment is recorded
- alert escalation path is implemented
- alert retry / expiry behavior is correct
- audit event is written on alert generation, acknowledgment, escalation, and expiry
- "renders" alone is not sufficient — behavioral correctness must be verified

**Approval / intervention components:**
- approval gate blocks the governed action until approval is explicitly granted
- approval decision is recorded with actor, timestamp, basis, and outcome
- intervention launch is correctly scoped and authorized
- rollback or cancellation paths are implemented
- audit event is written on every approval decision and intervention state change

**AIMC-routed AI action components:**
- all AI requests route through AIMC gateway
- AIMC unavailable → graceful degraded mode, not silent failure
- AIMC response is attributed (not presented as anonymous AMC output)
- audit event is written for each AIMC-routed action

**AIMCC / upload flow components:**
- all upload / ingestion requests route through AIMCC / Knowledge Upload Centre
- upload status is surfaced from AIMCC, not locally fabricated
- AIMCC unavailable → graceful degraded mode
- quota state is sourced from AIMCC, not locally guessed
- audit event is written for each upload / ingestion action

**Memory / knowledge retrieval surfaces:**
- knowledge / memory references include provenance attribution
- AMC does not present retrieved knowledge as internally generated facts
- stale or unavailable memory is surfaced explicitly, not silently suppressed
- no silent caching of persistent knowledge truth beyond transient presentation state

**Cross-system state components:**
- state ownership is explicit: AMC-owned vs AIMCC-owned vs knowledge-system-owned
- cross-system state is sourced from the authoritative owner, not duplicated
- state staleness or unavailability is handled gracefully

AMC shall adopt a test-first guarantee in which expected behavior is defined before implementation is treated as complete, and in which consequence-bearing flows are verified against approved upstream truth rather than post-hoc intuition.

This section exists because AMC is intended to become the executive operating centre of the Maturion estate. In such a system, many of the most important failures are not simple rendering bugs. They are failures of authority enforcement, approval gating, AI-role separation, state coherence, audit traceability, escalation handling, or executive-operating continuity. If these are left to be “tested later” after implementation convenience has already shaped the product, the result is predictable: behavior drifts away from product truth and governance significance becomes expensive to recover.

For AMC, test-first is therefore not just an engineering quality preference. It is a governance-preserving delivery discipline.

### Purpose of the Test-First Guarantee
The AMC test-first guarantee shall exist to ensure that implementation does not become the place where expected behavior is discovered for the first time.

The guarantee must ensure that:
- expected behavior is defined before completion is claimed
- approval-sensitive and authority-sensitive paths are specified before implementation convenience hardens them
- audit and traceability expectations are testable
- executive and mobile operating behavior can be verified against prior intent
- AI-mediated and agent-mediated flows are constrained by pre-declared expectations
- delivery teams and supervising agents know what “correct” means before they begin calling work done

A product as constitutionally significant as AMC must not rely on retrospective “it seems fine” judgment as its primary quality method.

### Core Principle
For AMC, no consequential behavior is truly complete unless its expected behavior was defined early enough that implementation could be judged against it rather than rationalized after the fact.

Test-first does not require that every tiny component begin with a fully written automated test file before a line of code is written. It does require that the expected behavior, success conditions, failure conditions, and boundary conditions of meaningful functionality are established before implementation is accepted as done.

This principle is especially important where AMC touches:
- authority
- approvals
- escalation
- intervention
- auditability
- shared state
- AI-mediated recommendation or action
- sandbox boundaries
- mobile and cross-context continuity

### Scope of the Guarantee
The test-first guarantee applies to all consequential AMC behavior, including but not limited to:
- approval workflows
- reserved-matter protection pathways
- authentication and authorization pathways
- AI-mediated recommendation, routing, and action pathways
- notification and escalation flows
- intervention initiation and follow-through
- audit-producing behavior
- shared-state transitions
- cross-device continuity behavior
- sandbox and specialist-boundary enforcement
- executive dashboard and drill-down decision workflows

Low-consequence UI details may carry a lighter burden, but any feature that can alter estate truth, decision significance, or authority consequence must fall under the stricter interpretation of test-first.

### Upstream Truth Coupling
All test-first expectations must derive from approved upstream truth.

For AMC, this means expected behavior should be traceable to:
- the AMC App Description
- approved governance canon where relevant
- approved FRS requirements
- approved TRS requirements
- approved Architecture decisions
- approved design decisions

Tests and verification expectations must not invent a different product than the one approved upstream. Where expected behavior is unclear, upstream clarification is required before “correctness” can be claimed.

### Behavior-First Definition Requirement
Before implementation of a consequential AMC capability is accepted, the following must be defined for that capability where relevant:
- intended behavior
- disallowed behavior
- authority or approval conditions
- identity conditions
- state-transition expectations
- audit consequences
- notification or escalation consequences
- success criteria
- failure conditions
- degraded-mode or boundary conditions

Without this pre-declared behavior model, implementation cannot be meaningfully verified.

### Authority and Approval Path Testing
Any capability touching authority, approval, or reserved-matter significance must be testable against those conditions.

This includes verifying, where relevant:
- correct approval is required when expected
- missing approval blocks action
- stale approval does not incorrectly authorize action
- delegated scope is respected
- reserved-matter protections are enforced
- escalation occurs where execution authority is insufficient
- UI and API layers agree about approval significance

For AMC, authority drift is a constitutional defect. Test-first must therefore cover authority behavior explicitly.

### Authentication and Access-Control Testing
Any consequential AMC action must have pre-declared expectations for identity and access behavior.

This includes, where relevant:
- who can access the pathway
- who cannot
- what authority evaluation occurs
- what happens under insufficient privilege
- what happens under sandbox-bound identity
- how service-to-service identity is treated
- how privileged actions are protected

A feature that “works” but has undefined or untested access semantics is incomplete.

### AI and Agent Behavior Testing
Because AMC relies heavily on AI and agent roles, test-first must also apply to AI-mediated behavior.

Where AI or agents are involved, the expected behavior model should define:
- whether the AI is observing, recommending, routing, coordinating, or acting
- what approval is required before action if action is consequential
- how the AI role is distinguished from other AI or agent roles
- what audit or traceability consequence follows
- what should happen when AI confidence, context, or authorization is insufficient
- what behavior is prohibited

AMC must not normalize “the AI did something surprising” as acceptable emergent quality.

### Notification and Escalation Testing
AMC’s executive-operating value depends heavily on notification and escalation quality. These behaviors must be test-defined before delivery is treated as complete.

This includes defining and verifying:
- what conditions produce proactive notification
- what class of notification should be produced
- when escalation rather than mere notification is required
- what information must accompany notification
- how acknowledgment changes state
- how follow-up escalation is triggered if needed
- how mobile and desktop experiences handle the same event coherently

A notification system that merely emits events without verified meaning is not sufficient for AMC.

### Shared-State and Continuity Testing
Test-first must cover state behavior for consequential flows.

This includes defining and verifying:
- how shared state changes across workflows
- how pending vs resolved states are represented
- how approval, escalation, and intervention state propagate across surfaces
- how conversation context and executive context persist where required
- how stale or conflicting state is handled
- how state restoration behaves after interruption, reconnect, or device switch where relevant

Because AMC is an executive operating environment, state incoherence is a high-consequence defect and must be tested as such.

### Audit and Traceability Testing
Consequential AMC behavior must include pre-declared audit expectations.

This includes verifying where relevant:
- whether the action generates an audit record
- whether the correct identity and authority information is captured
- whether approval or escalation linkage is preserved
- whether AI-mediated consequential behavior is attributable
- whether conversation-to-action traceability exists where required
- whether rejection, rollback, failure, or exception states are audit-visible

An action that “works” but leaves governance-blind history behind is not done.

### Sandbox and Boundary Testing
Where AMC features touch sandboxed environments or specialist-agent boundaries, those boundaries must be test-defined and verified.

This includes validating:
- sandbox-local actions remain sandbox-local
- cross-boundary actions are blocked or escalated when appropriate
- specialist roles cannot silently operate as estate-level actors
- state, auth, and audit behavior preserve boundary integrity

For AMC, sandbox safety must be demonstrable, not assumed.

### Mobile and Real-Context Testing
Because AMC is intended for desktop and mobile executive use, some behaviors require more than abstract technical verification.

Where relevant, expected behavior must include:
- mobile notification reception and interpretation
- mobile drill-down into context
- mobile approval or rejection pathways
- continuity across device changes
- real-world usability in fast decision contexts
- operational comprehension under time pressure

AMC cannot claim success if it only works well in calm desktop development conditions.

### Failure and Degraded-Mode Testing
Test-first for AMC must include failure and degraded-mode expectations, not just happy-path success.

This includes defining and verifying:
- what happens when approval is missing
- what happens when identity is invalid
- what happens when AI routing is unavailable
- what happens when state is stale or partially unavailable
- what happens when notification delivery fails
- what happens when audit logging is impaired
- what happens when sandbox boundary checks fail
- what happens when downstream execution is blocked or delayed

A control centre that has no pre-declared degraded-mode behavior is operationally weak even if the happy path looks good.

### Evidence Requirement
For consequential AMC features, the test-first guarantee must be supported by evidence.

Evidence may include, as appropriate:
- explicit acceptance criteria
- test plans
- structured verification scenarios
- automated tests
- integration tests
- manual validation records
- physical verification records
- screenshots or recordings where operationally meaningful
- assurance findings or review notes

The exact evidence format may vary, but evidence must exist before completion claims are trusted.

### Minimum Test-First Checklist
The following minimum conditions must hold for consequential AMC behavior:

- [ ] Expected behavior is defined before completion is claimed
- [ ] Disallowed or boundary behavior is defined where relevant
- [ ] Approval and authority expectations are defined where relevant
- [ ] Auth and identity expectations are defined where relevant
- [ ] AI and agent behavior expectations are defined where relevant
- [ ] Notification or escalation behavior is defined where relevant
- [ ] Shared-state and continuity behavior is defined where relevant
- [ ] Audit consequences are defined where relevant
- [ ] Sandbox or boundary behavior is defined where relevant
- [ ] Failure and degraded-mode behavior is defined where relevant
- [ ] Appropriate verification evidence exists
- [ ] Completion is judged against pre-declared behavior rather than post-hoc convenience

### Proportionate Rigor Rule
The intensity of test-first evidence may vary with consequence, but the guarantee itself still applies.

For AMC:
- low-consequence presentational details may use lighter forms of behavior definition and verification
- executive, approval, auth, audit, AI, intervention, notification, state, and sandbox features require heavier and more explicit pre-declared behavior and verification
- any component or workflow that can materially affect estate truth must be held to the stricter standard

The guarantee must therefore be proportionate, but never optional where consequence is high.

### Downstream Design Consequence
Downstream FRS, TRS, Architecture, and build-planning artifacts must make testing and verification part of the definition of the work, not an afterthought appended at the end.

This means work packages for AMC must be framed in ways that allow supervising agents, reviewers, and assurance actors to determine whether expected behavior was declared early enough and evidenced clearly enough.

### Non-Negotiable Principle
AMC’s test-first guarantee must ensure that consequential behavior is built against pre-declared truth rather than post-hoc rationalization.

Any delivery practice that allows authority-sensitive, audit-sensitive, AI-mediated, or executive-operating behavior to become “correct” only because implementation has already hardened is non-compliant with the intended purpose of AMC.

### AMC-Specific Test-First Requirements

The following AMC-specific behaviors must have tests written and RED before any implementation begins:

**Alerting:**
- alert generation triggers for each defined alert class
- alert routing to correct authority
- alert acknowledgment recording
- alert escalation behavior
- alert retry / expiry behavior

**Approvals:**
- approval gate blocks action until approval granted
- approval decision recording (actor, basis, timestamp)
- unauthorized approval attempt is rejected

**Interventions:**
- intervention launch authorization check
- intervention state tracking
- intervention cancellation

**AIMC flows:**
- all AI requests route through AIMC (no direct model calls)
- AIMC unavailable → degraded mode behavior
- AIMC response attribution

**AIMCC / upload flows:**
- upload routes through Knowledge Upload Centre / AIMCC
- AIMCC unavailable → degraded mode behavior
- quota state sourced from AIMCC

**Memory-aware retrieval:**
- knowledge references include provenance
- memory retrieval degraded → explicit surfacing, not suppression

**Degraded dependency behavior:**
- AIMC unavailable: AMC enters defined degraded mode, surfaces status
- AIMCC unavailable: AMC enters defined degraded mode, surfaces status
- Knowledge / memory system degraded: AMC surfaces explicit degraded status

No AMC component is build-ready if it has no RED tests for the above behaviors relevant to that component.


## §11 — Physical Verification Gate (§AD-07)

AMC shall include a physical verification gate for behaviors whose success depends on real interaction conditions, real device contexts, real notification delivery, and real executive-operating usability rather than abstract correctness alone.

This section exists because AMC is intended to become the executive operating centre of the Maturion estate. Many of its most important behaviors cannot be fully trusted merely because they pass unit tests, integration tests, or simulated workflows. AMC is expected to support mobile access, proactive notification, approval handling, escalation review, conversational interaction with Maturion, and real-world intervention in live contexts such as client engagements or on-the-move decision scenarios. Those behaviors must be verified in conditions that meaningfully resemble actual use.

For AMC, physical verification is therefore not optional polish. It is a reality-check gate that prevents the estate’s executive control surface from being approved solely on abstract or lab-only success.

### Purpose of the Physical Verification Gate
The AMC physical verification gate shall exist to confirm that the product behaves acceptably in real operating conditions where user perception, timing, context-switching, and device realities materially affect success.

The gate must ensure that:
- mobile and desktop operation behave as intended in practice
- notifications reach the user meaningfully and at the right level of urgency
- approval and escalation flows are intelligible under real attention conditions
- conversation and intervention workflows remain usable outside ideal development conditions
- the executive operating model is observable in reality rather than only in theory
- design claims about continuity, awareness, and operational readiness are evidence-backed

If AMC only works convincingly in simulated or developer-controlled conditions, it is not ready.

### Core Principle
Physical verification is required wherever real-world operating conditions materially influence whether AMC fulfills its purpose.

A capability that is technically correct but practically unusable in live executive conditions is not complete for AMC.

This principle is especially important for:
- mobile notification and action flows
- approval decisions made away from desktop environments
- real-time escalations
- intervention launch and follow-through
- executive comprehension under time pressure
- conversation with Maturion in operational contexts
- continuity when switching devices or reconnecting after interruption

### Scope of the Gate
The physical verification gate applies to any AMC feature or workflow whose value depends significantly on real environment conditions, including but not limited to:
- mobile surfaces
- cross-device continuity
- push or equivalent notifications
- escalation prompts
- approval prompts
- conversational workflows with Maturion
- intervention initiation and monitoring workflows
- dashboard-to-drill-down decision workflows
- high-consequence alert handling
- user experience under interruption or degraded connectivity where relevant

Not every low-consequence internal behavior needs a physical gate, but any feature central to AMC’s executive-operating role must be assessed for physical verification relevance.

### Why Abstract Verification Is Not Enough
AMC’s strategic purpose includes “tell me before I ask,” “keep me in contact wherever I go,” and “support governed action in real contexts.”

These are not purely logical properties. They depend on:
- whether the user actually notices the signal
- whether the signal is understandable at speed
- whether the next action is available and safe
- whether context is preserved when shifting device or location
- whether the workflow remains intelligible under interruption
- whether executive meaning survives real interface constraints

A design that passes automated checks but fails these realities is non-compliant with AMC’s intended purpose.

### Mobile Verification Requirement
Where AMC supports mobile executive operation, physical verification must confirm that mobile use is genuinely viable.

This includes, where relevant:
- notification reception on mobile devices
- readability and meaning of notifications on mobile
- ability to drill into sufficient context from mobile
- ability to approve, reject, defer, or escalate safely from mobile
- continuity of conversation with Maturion on mobile
- continuity between mobile and desktop usage
- usability under short-attention or on-the-move conditions

AMC must not claim mobile support if mobile reality is reduced to “the page technically opens on a phone.”

### Notification and Escalation Verification Requirement
Physical verification must confirm that notifications and escalations behave meaningfully in practice.

This includes checking, where relevant:
- whether the right class of event generates notification
- whether urgency is communicated clearly
- whether acknowledgment pathways are visible and usable
- whether escalation pathways are understandable under time pressure
- whether signal quality remains acceptable
- whether users can distinguish between informational, warning, approval, intervention, and emergency events
- whether follow-up actions are reachable from the notification context

Because AMC depends on proactive awareness, notification behavior must be proven as lived behavior, not assumed from technical dispatch success.

### Approval Workflow Verification Requirement
Approval-sensitive behaviors must be physically verified where interaction quality affects governance safety.

This includes confirmation that:
- the user can understand what is being approved
- the authority significance is visible
- the consequences of approval or rejection are understandable
- the approval interaction is usable under realistic operating conditions
- approval actions do not become dangerously easy or confusing on constrained interfaces
- reserved-matter significance is not obscured in real interaction flows

An approval system that is technically wired but practically confusing is unsafe for AMC.

### Conversation and Executive Understanding Verification Requirement
Because AMC uses a conversational operating pattern with Maturion, physical verification must also assess whether the conversation layer supports real executive understanding.

This includes, where relevant:
- whether proactive messages are understandable in context
- whether conversation preserves the difference between observation, recommendation, request, and decision
- whether conversation helps the user move to correct governed action
- whether the user can recover context quickly after interruption
- whether the conversation remains intelligible across desktop and mobile contexts

Conversation quality in AMC is not cosmetic. It is part of how authority and awareness operate.

### Intervention Workflow Verification Requirement
Where AMC supports governed intervention, physical verification must confirm that intervention workflows are usable under live conditions.

This includes checking, where relevant:
- whether an intervention can be understood and initiated from the available context
- whether required approvals are visible
- whether status after launch is understandable
- whether the user can tell what happens next
- whether interruption or device-switching breaks the executive flow
- whether rollback or failure visibility is adequate

This is especially important for the intended scenario where intervention may be launched while Johan Ras is with a client or away from a desktop environment.

### Cross-Device and Interruption Verification Requirement
AMC is intended to preserve executive continuity across device changes and interruptions.

Physical verification should therefore assess:
- switching from mobile to desktop
- resuming after interruption
- reconnecting after temporary loss of session or context
- preserving enough continuity to continue the executive workflow safely
- preventing misleading restoration of stale or partial truth

Continuity claims must be demonstrated, not merely designed.

### Real-Context Verification Scenarios
AMC physical verification should be structured around meaningful real-context scenarios rather than generic UI walkthroughs.

Examples of suitable scenario classes include:
- receiving a high-priority estate alert while away from a desk
- reviewing and responding to an approval request on mobile
- moving from proactive Maturion notification into drill-down and action
- monitoring a governed fix after initiating it in a live external context
- resuming an interrupted executive workflow across devices
- handling an escalation that requires quick understanding but governed restraint

The purpose of scenario-driven physical verification is to test AMC in the kinds of situations it explicitly claims to support.

### Evidence Requirement
Physical verification must be evidenced.

Acceptable evidence may include, as appropriate:
- structured physical verification checklists
- scenario run records
- screenshots or recordings from real devices
- notes from observed usability validation
- confirmation of notification delivery and actionability
- cross-device continuity demonstrations
- issue records for behaviors that failed physical verification
- remediation evidence after correction

Evidence should make it possible for a reviewer to determine not only that verification occurred, but whether the result was acceptable.

### Blocking Rule
Where physical verification is required for a capability, failure to pass the gate is a blocking defect for that capability’s claim of readiness.

For AMC, this is especially true where failure affects:
- approval safety
- escalation clarity
- intervention usability
- proactive awareness quality
- mobile executive operation
- cross-device continuity
- executive comprehension under real conditions

A physically unverified or physically failed high-consequence workflow is not ready simply because it passed abstract testing.

### Minimum Physical Verification Checklist
The following minimum conditions must hold where physical verification is relevant:

- [ ] Real-device or real-context verification needs have been identified
- [ ] Mobile executive interaction has been physically assessed where relevant
- [ ] Notification and escalation behavior has been physically assessed where relevant
- [ ] Approval interaction quality has been physically assessed where relevant
- [ ] Conversation with Maturion has been physically assessed where relevant
- [ ] Intervention workflow usability has been physically assessed where relevant
- [ ] Cross-device continuity has been physically assessed where relevant
- [ ] Evidence of physical verification exists
- [ ] Failures found through physical verification are tracked and not hidden
- [ ] Readiness claims reflect physical-verification outcomes truthfully

### Downstream Design Consequence
Downstream FRS, TRS, Architecture, and verification planning must identify which AMC capabilities require physical verification and must plan for that work explicitly.

Physical verification may not be treated as a last-minute optional demo activity. It is part of how AMC proves that it can function as a real executive operating surface.

### Non-Negotiable Principle
AMC’s physical verification gate must ensure that the executive operating centre of the estate works in the real conditions it claims to support.

Any delivery practice that approves high-consequence mobile, approval, escalation, conversation, or intervention behavior without meaningful physical verification is non-compliant with the intended purpose of AMC.

### Executive-Critical Desktop and Mobile Verification Requirements

The following AMC surfaces must be verified on both desktop and mobile device classes before any build is considered complete:

- **Critical alerts**: alert display, priority indication, acknowledgment action, escalation trigger
- **Approval prompts**: approval presentation, decision recording, unauthorized attempt rejection
- **Intervention actions**: intervention launch, state visibility, cancellation or rollback
- **Upload / ingestion status views**: upload status from AIMCC, progress indication, failure surfacing
- **Memory-aware operational surfaces**: knowledge reference display with provenance, degraded-state surfacing

Mobile verification must confirm that executive actions (approvals, acknowledgments, interventions) are executable from mobile contexts, not just visible.


## §12 — PBFAG Checklist Requirements (§AD-08)

AMC shall not proceed into substantive downstream design or build activity unless the required pre-build governance gate has been satisfied.

This section exists because AMC is not a routine internal utility. It is intended to become the executive operating surface of a governed multi-agent estate. That means downstream work must not begin on the basis of partial intent, blurred authority, unresolved AI boundary questions, or undefined approval and audit expectations.

The PBFAG requirement for AMC therefore functions as a hard readiness gate, not an advisory planning note.

### Purpose of the PBFAG Gate
The AMC PBFAG gate shall exist to confirm that Stage 1 has produced enough stable, approved truth for downstream artifacts to be derived without guesswork.

The gate must ensure that:
- product identity is stable enough to derive requirements
- authority boundaries are clear enough to design enforcement
- AI integration boundaries are clear enough to design safely
- approval, audit, and state implications are known
- downstream teams are not forced to invent product truth during FRS, TRS, or Architecture work

If those conditions are not met, AMC is not ready to move forward.

### Core Principle
For AMC, pre-build readiness means more than “we have written something.”

Readiness means the application has been described clearly enough that downstream work can preserve:
- product intent
- governance integrity
- authority integrity
- approval integrity
- audit integrity
- state coherence
- AI-role separation
- sandbox and boundary discipline

A document that exists but still leaves fundamental operating questions unresolved does not satisfy the gate.

### Stage 1 Readiness Requirement
The PBFAG gate for AMC shall require that Stage 1 truth is sufficiently mature to support derivation into FRS, TRS, Architecture, and later build planning.

At minimum, Stage 1 must establish:
- what AMC is
- what AMC is not
- why AMC exists
- who its principal actors are
- how authority is structured
- how AI is intended to operate within it
- what kinds of actions require approval
- what must be auditable
- what shared state and continuity obligations exist
- what the intended executive operating pattern is

If any of those are materially unresolved, the gate is not satisfied.

### Mandatory Readiness Domains
The PBFAG gate for AMC shall evaluate readiness across the following mandatory domains:

- **application identity readiness**
- **scope and boundary readiness**
- **authority-model readiness**
- **AI integration readiness**
- **approval and reserved-matter readiness**
- **notification and UX readiness**
- **audit readiness**
- **shared state readiness**
- **authentication and authorization readiness**
- **sandbox and specialist-boundary readiness**
- **downstream derivation readiness**
- **approval-record and tracker readiness**
- **AIMC integration readiness**
- **AIMCC / Knowledge Upload Centre integration readiness**
- **memory-system dependency clarity**

AMC should not be treated as pre-build ready if any one of these domains is materially under-defined.

### Application Identity Readiness
The gate must confirm that AMC has a stable identity as the executive control centre of the Maturion estate, rather than remaining an unresolved blend of dashboard, governance repo, orchestration layer, or experimental runtime.

The gate should verify that:
- AMC is defined as the executive operating surface of the estate
- the relationship to Foreman-App lineage is clear
- product identity is separated from governance canon
- product identity is separated from historical experimentation artifacts

### Scope and Boundary Readiness
The gate must confirm that AMC’s in-scope and out-of-scope boundaries are sufficiently explicit.

This includes confirmation that:
- AMC is not being treated as a direct code editor
- AMC is not being treated as a replacement for governance canon
- AMC is not being treated as a substitute for consumer applications
- AMC’s control-plane role is clear
- mobile, proactive, approval, intervention, and oversight expectations are recognized as part of scope

### Authority-Model Readiness
The gate must confirm that AMC’s authority structure is explicit enough to guide all later design.

This includes confirmation that:
- Johan Ras remains the constitutional authority over reserved matters
- Maturion is defined as resident AI executive
- Foreman is defined as supervised orchestration authority beneath Maturion
- specialist, maintenance, and assurance roles are distinguishable
- delegation intent is explicit
- no silent or accidental authority transfer is implied

Because AMC is meant to support progressive autonomy, unclear authority at Stage 1 is a blocking defect.

### AI Integration Readiness
The gate must confirm that AMC’s AI role model is sufficiently defined to prevent unsafe downstream assumptions.

This includes confirmation that:
- AIMC and AIMC Gateway are recognized as the governed AI integration route
- Maturion’s executive role is defined
- AI role separation is defined
- proactive AI communication is part of the intended design
- sandboxed specialist-AI environments are recognized where relevant
- uncontrolled direct provider coupling is excluded

AMC is not ready if the downstream team would still need to guess whether the product is “just chat in a dashboard” or a governed executive AI system.

### Approval and Reserved-Matter Readiness
The gate must confirm that reserved matters and approval-gated actions are sufficiently acknowledged.

This includes confirmation that:
- reserved matters are named or categorically defined
- governance-sensitive actions are expected to route through approval
- the distinction between routine delegated action and reserved-matter action is visible
- approval consequences are recognized as product requirements, not merely workflow preferences

If approval significance is not yet structurally recognized, Stage 1 is incomplete.

### Notification and UX Readiness
The gate must confirm that AMC’s UX model is sufficiently defined to guide later design.

This includes confirmation that:
- AMC is designed for proactive awareness, not just reactive querying
- mobile and desktop contexts are both relevant
- approval prompts, escalation prompts, and executive notifications are recognized
- conversation with Maturion is part of the operating model
- dashboard plus drill-down behavior is expected

Because AMC’s value depends heavily on how it communicates meaning, weak UX definition at Stage 1 is a serious readiness gap.

### Audit Readiness
The gate must confirm that audit is recognized as a first-class design concern.

This includes confirmation that:
- approvals must be auditable
- AI-mediated consequential actions must be auditable
- interventions and escalations must be auditable
- authority attribution is expected
- conversation-to-action traceability is acknowledged where materially relevant
- audit visibility itself is understood to require governance

If audit is still treated as something to “add later,” AMC is not ready.

### Shared State Readiness
The gate must confirm that AMC’s need for coherent cross-surface state is understood.

This includes confirmation that:
- executive context continuity is recognized
- approval, alert, escalation, intervention, and conversation states are expected to be shared
- cross-device continuity matters
- contradictory local truths are understood as a risk
- source-of-truth and state-domain design will be required downstream

Because AMC is an executive operating environment, fragmented state is not a minor implementation detail.

### Authentication and Authorization Readiness
The gate must confirm that auth design is understood as a governance mechanism, not just an access feature.

This includes confirmation that:
- multiple identity classes exist
- authority mapping is needed
- reserved-matter enforcement must be real at the system boundary
- approval state must influence execution ability
- sandbox and service-to-service pathways require identity discipline
- auth outcomes must couple to audit

If Stage 1 still treats auth as generic login plumbing, the gate is not satisfied.

### Sandbox and Specialist-Boundary Readiness
The gate must confirm that specialist-agent and sandbox boundaries are recognized where relevant.

This includes confirmation that:
- sandboxed AI work environments are part of the intended future direction
- specialist roles are bounded, not free-floating
- cross-boundary movement requires governance
- bounded workspaces must not silently inherit estate-wide authority

This is important because sandbox design assumptions, once left vague, tend to harden into unsafe architecture later.

### Downstream Derivation Readiness
The gate must confirm that FRS, TRS, and Architecture can be derived from Stage 1 without inventing product truth.

This includes confirmation that:
- section structure is sufficiently complete
- the most strategic sections are materially filled, not just outlined
- downstream artifact expectations are known
- there are no known unresolved contradictions that would invalidate derivation work

Stage 1 does not need to answer every downstream technical detail, but it must answer the questions that define the product and its constitutional shape.

### Approval-Record and Tracker Readiness
The gate must confirm that Stage 1 readiness is evidenced through governance hygiene, not just document content.

This includes confirmation that:
- approval record expectations exist
- tracker artifacts are updated
- placeholder status is not falsely represented as complete
- readiness claims can be defended with artifacts, not memory

AMC cannot be credibly positioned as a wellbeing and truth-management platform if its own foundational stage is administratively unclear.

### AIMC Integration Readiness
The gate must confirm that the AIMC integration model is sufficiently defined for Architecture and build to proceed.

This requires:
- the AIMC gateway interface is defined in the TRS
- all AI action pathways are confirmed to route through AIMC
- AIMC unavailability behavior is explicitly defined
- AIMC audit requirements are specified

### AIMCC / Knowledge Upload Centre Integration Readiness
The gate must confirm that the AIMCC / Knowledge Upload Centre integration model is sufficiently defined.

This requires:
- the AIMCC interface for upload status, quota management, and ingestion outcomes is defined
- the Knowledge Upload Centre interface for upload submission is defined
- AIMCC unavailability behavior is explicitly defined
- upload / ingestion audit requirements are specified

### Memory-System Dependency Clarity
The gate must confirm that AMC's relationship to the knowledge / memory system is explicitly defined.

This requires:
- the knowledge / memory retrieval API and provenance model is defined
- AMC's non-ownership of persistent knowledge / memory truth is explicit
- memory retrieval degradation behavior is defined
- no section implies AMC is the canonical private owner of estate knowledge

### Audit Model Readiness
The gate must confirm that the audit model is sufficiently defined for implementation.

This requires:
- the audit event taxonomy covers all consequential action types
- required audit fields (actor, source, object, action, timestamp, outcome) are specified
- cross-system provenance requirements are defined
- audit retention requirements are specified

### State Ownership Readiness
The gate must confirm that the state ownership model is sufficiently explicit.

This requires:
- AMC-owned state is identified
- AIMCC-owned state is identified
- knowledge / memory system-owned state is identified
- transient / cached state vs persistent state boundaries are defined

### Minimum PBFAG Checklist
The following minimum checklist items must be satisfied before AMC may be treated as pre-build ready:

- [ ] AMC identity as the executive control centre is clearly established
- [ ] In-scope and out-of-scope boundaries are explicitly defined
- [ ] Foreman-App lineage is acknowledged without confusing lineage with current scope
- [ ] Johan, Maturion, Foreman, assurance, maintenance, and specialist roles are distinguishable
- [ ] Reserved matters are named or categorically defined
- [ ] Approval-gated action significance is recognized
- [ ] AIMC-governed AI integration is recognized as mandatory
- [ ] Proactive communication and mobile-context operation are recognized as product requirements
- [ ] Audit obligations for approvals, interventions, and AI-mediated actions are recognized
- [ ] Shared state domains are recognized as necessary
- [ ] Auth and authority enforcement are recognized as first-class design concerns
- [ ] Sandbox and specialist-boundary implications are acknowledged where relevant
- [ ] Downstream artifact expectations are identified
- [ ] Approval record and tracker updates are in place or explicitly pending with visibility
- [ ] No known unresolved contradiction makes downstream derivation unsafe

### Blocking Rule
Any materially incomplete checklist item shall be treated as a blocking defect for downstream progression.

For AMC, “close enough” is not sufficient if the unresolved gap concerns:
- authority
- AI role boundaries
- approval significance
- audit significance
- state coherence
- sandbox boundaries
- executive operating intent

These are not polishing issues. They are constitutional product-definition issues.

### Evidence Requirement
PBFAG completion for AMC must be evidenced through artifacts rather than asserted informally.

Acceptable evidence may include:
- completed Stage 1 sections
- companion authority-model artifacts
- approval records
- tracker updates
- governance review notes
- explicit recorded decisions on unresolved canonical-location or authority questions

The gate is satisfied by defensible readiness, not by optimism.

### Downstream Design Consequence
Once the PBFAG gate is satisfied, downstream FRS, TRS, and Architecture work may proceed on the basis that Stage 1 truth is sufficiently stable.

Until then, downstream teams must not fill gaps in authority, AI behavior, approval significance, audit expectation, or executive UX intent through assumption.

### Non-Negotiable Principle
The AMC PBFAG gate must prevent the estate’s executive operating centre from being built on unresolved constitutional ambiguity.

Any attempt to proceed while Stage 1 still leaves core authority, AI, approval, audit, or operating-model questions materially unclear is non-compliant with the intended purpose of AMC.


## §13 — Agent Authority Chain (§AD-09)

AMC shall operate under an explicit, non-ambiguous authority chain. Authority may be delegated in defined domains, but it may not become implicit, hidden, or structurally unclear.

### Constitutional Authority
**Johan Ras** remains the constitutional human authority of the estate unless and until governance is explicitly amended.

Johan Ras retains authority over reserved matters, including at minimum:
- governance changes
- agent-file changes
- App Description changes that materially alter scope or identity
- major architectural direction changes
- constitutional boundary changes
- authority-transfer changes
- any other matter explicitly designated as reserved by governance canon

No AMC workflow may silently convert a reserved matter into a routine operational matter.

### Resident AI Executive
**Maturion** is the resident AI executive within AMC.

Maturion’s role is to:
- maintain executive awareness of the estate
- surface risks, decisions, and anomalies proactively
- coordinate reporting from subordinate operational and specialist agents
- supervise estate-level wellbeing signals
- support decision preparation for Johan Ras
- progressively assume approved operational executive responsibilities
- manage ongoing operational oversight once authority for those domains has been explicitly delegated

Maturion is not a hidden builder runtime. Maturion is an executive intelligence and estate-management role operating within governance and approval boundaries.

### Supervisory Orchestration Layer
**Foreman** operates as a supervised orchestration authority beneath Maturion.

Foreman’s role is to:
- coordinate execution sequencing
- supervise build and delivery orchestration
- manage builder-side execution flows within approved authority
- maintain operational discipline during execution
- return governed outcomes upward for executive awareness, approval, or escalation where required

Foreman does not become the constitutional authority, and under the AMC model Foreman is not the top-order executive intelligence. Foreman remains subordinate to the executive layer represented by Maturion, and ultimately subordinate to Johan Ras on reserved matters.

### Independent Assurance Layer
**IAA agents** remain independent assurance authorities.

IAA agents:
- do not become cleanup-authoring substitutes
- do not become hidden producers of delivery work
- remain outside the producing/orchestrating chain when issuing assurance judgments
- report findings, rejection packages, assurance results, and integrity concerns upward through the governed operating model

Where assurance outcomes require executive or reserved-matter attention, AMC must route those outcomes to the correct authority without collapsing IAA independence.

### Maintenance and Operational Support Layer
**Maintenance agents** perform upkeep, health checks, scanning, diagnostics, and operational maintenance functions within approved scope.

They may:
- inspect health and integrity conditions
- surface issues
- perform approved maintenance actions
- report status and exceptions upward

They may not:
- self-authorize governance-sensitive changes
- silently alter authority structures
- bypass approval gates on reserved matters

### Specialist-Agent Layer
**Specialist agents** perform domain-specific, app-specific, or sandbox-specific work under governed supervision.

Specialist agents may include:
- AIMC-based specialists
- app-domain specialists
- workflow-design specialists within sandboxed environments
- analysis, compliance, security, or operational specialists

Specialist agents are subordinate operational capabilities. They are not independent constitutional actors. Their work must be bounded by approved scope, clear tenancy or sandbox limits where relevant, and explicit reporting/traceability expectations.

### Builder Layer
**Builders** are implementation actors only.

Builders may:
- implement approved work
- execute build tasks
- produce artifacts
- respond to orchestrated instructions

Builders may not:
- self-approve reserved matters
- redefine app scope on their own authority
- rewrite governance implicitly through implementation
- assume executive authority merely because they are operationally active

### Reporting and Escalation Model
AMC shall support a clear upward reporting structure:

- builders report through execution/orchestration structures
- Foreman supervises orchestration and execution readiness
- specialist, maintenance, and assurance actors report through governed pathways into Maturion’s executive layer
- Maturion synthesizes estate-level meaning, decision need, and executive awareness
- Johan Ras receives escalations, approvals, and reserved-matter decisions at the constitutional layer

This chain must remain explainable in product behavior, not just in governance theory.

### Delegation Rule
Progressive delegation is permitted only when:
- the delegated domain is explicitly defined
- governance permits that delegation
- approval boundaries remain clear
- audit and traceability remain intact
- escalation routes remain available
- revocation or rollback of delegated authority is possible

AMC must support increased autonomy without ever making it impossible to determine who had authority for a given action.

### Non-Negotiable Principle
AMC must preserve separation between:
- constitutional authority
- executive intelligence
- orchestration authority
- assurance authority
- specialist capability
- builder implementation activity

A design that blurs those layers is non-compliant with the intended AMC operating model.

### Authority Matrix

The following matrix defines read / propose / approve / trigger / ingest / remember / retrieve / act authority boundaries across the key actors in the AMC operating model.

| Actor | Read | Propose | Approve | Trigger | Ingest Knowledge | Remember / Store | Retrieve / Surface | Act (Autonomous) |
|---|---|---|---|---|---|---|---|---|
| **Johan / CS2** | All estate state, governance, and artifacts | All governance proposals and escalations | All reserved matters and constitutionally significant decisions | All governed operations | Authorized via AIMCC pathway | Authorized via knowledge/memory system | All estate state and knowledge (with provenance) | Constitutional authority over all domains |
| **Maturion** | All estate operational state and reporting | Executive proposals (alerts, recommendations, escalations) | Delegated operational matters (explicitly approved domains only) | Delegated operations within approved autonomy | Via AIMCC only | Via knowledge/memory system only | All estate state and knowledge (with provenance) | Within approved autonomy scope only |
| **Foreman** | Architecture, governance | Build plans | QP/IAA gates only | Build waves | None | Build evidence | Build-relevant knowledge | Orchestration only |
| **AMC (application)** | Estate operational state | Alerts, escalations | None — surfaces to human/Maturion | Alert triggers, intervention routing | Via AIMCC / KUC only | AMC operational state only | Via governed APIs (with provenance) | Approval-gated executive actions |
| **AIMC** | AI requests | AI responses | None | AI model execution | None | None | AI model context | AI execution within governed scope |
| **AIMCC** | Knowledge state and ingestion workflow-state | Ingestion outcomes and curation metadata | Knowledge governance actions within AIMCC scope | Ingestion pipelines | Yes — governs ingestion and owns ingestion metadata/workflow-state; **persistent knowledge/memory truth canonical owner is the knowledge / memory system** | Governs memory operations and owns ingestion/curation metadata; does NOT hold canonical ownership of persistent knowledge/memory truth | Knowledge retrieval via governed API | Within knowledge governance scope |
| **Knowledge Upload Centre** | Upload submissions | Upload status | None | Ingestion submission to AIMCC | Submission gateway | None | None | Upload submission only |
| **knowledge / memory system** | Persistent memory | None | None | None | Via AIMCC | **Canonical persistent store — sole canonical owner of persistent knowledge/memory truth** | Retrieval via governed API | None |
| **Specialist / Builder** | Task-scoped | Implementation proposals | None | Build execution | None | Build artifacts | Task-relevant | Implementation only |
| **Assurance (IAA)** | All artifacts | Assurance findings | Assurance verdicts | None | None | Assurance records | All (for audit purposes) | None (advisory only) |

**Key rules:**
- AMC must not approve its own governance actions (approvals route to Johan / Maturion)
- AMC must not ingest knowledge directly (always via AIMCC / Knowledge Upload Centre)
- AMC must not store persistent knowledge truth (knowledge / memory system is the sole canonical owner; AIMCC governs ingestion workflows and owns ingestion metadata, not persistent truth)
- AIMC is the sole AI execution actor — no other actor executes AI models directly
- AIMCC governs knowledge ingestion and memory operations but does NOT own persistent knowledge/memory truth — the knowledge / memory system is canonical


## §14 — Schema-to-Hook Validation (§AD-10)

AMC shall require explicit schema-to-hook validation so that data structures, shared-state models, and implementation pathways remain faithful to approved product truth rather than drifting into convenience-driven behavior.

This section exists because AMC is intended to become the executive operating centre of the Maturion estate. In such a system, seemingly small implementation decisions about schemas, state objects, hooks, stores, derived values, action handlers, and synchronization pathways can quietly alter authority meaning, approval significance, audit visibility, continuity behavior, or sandbox boundaries. If the relationship between approved structural truth and actual implementation pathways is not reviewed deliberately, the system can appear correct at a high level while behaving constitutionally incorrectly at runtime.

For AMC, schema-to-hook validation is therefore not a narrow frontend engineering concern. It is part of the mechanism by which product truth survives implementation.

### Purpose of Schema-to-Hook Validation
The AMC schema-to-hook validation requirement shall exist to ensure that the structures used in implementation correctly represent the approved meanings established upstream.

The requirement must ensure that:
- state structures reflect approved state domains
- hooks and action pathways preserve authority and approval logic
- derived state does not distort executive meaning
- persistence and restoration behavior remain faithful to design intent
- notification, escalation, audit, and intervention flows remain structurally coherent
- sandbox and specialist boundaries are not eroded by implementation shortcuts

If a schema or hook implementation changes the meaning of the product in practice, the implementation is non-compliant even if the code compiles and the UI appears functional.

### Core Principle
Every materially significant implementation pathway in AMC must be able to show that its runtime behavior is structurally justified by approved schemas, approved state meaning, and approved action semantics.

This means:
- no critical hook may invent authority significance ad hoc
- no state pathway may collapse meaningful distinctions merely because they are inconvenient to model
- no derived convenience abstraction may blur pending vs approved, alert vs escalation, recommendation vs decision, sandbox-local vs estate-wide, or AI suggestion vs executed action
- no persistence or synchronization structure may silently change the intended operating model

Schema-to-hook validation is therefore a guard against semantic drift between design and runtime behavior.

### Scope of Validation
Schema-to-hook validation applies to any material implementation structure that connects approved data/state design to runtime behavior.

This includes, where relevant:
- persisted schemas
- in-memory shared-state structures
- hook interfaces
- derived selectors or computed state
- action handlers
- approval and escalation state transitions
- notification state pathways
- conversation and executive-context state pathways
- intervention state pathways
- agent and identity state pathways
- sandbox-bound state pathways
- audit-linkage structures

Not every trivial local UI flag requires formal scrutiny, but any structure that can alter executive understanding, authority consequence, or estate truth falls within scope.

### Upstream Truth Coupling
Schema-to-hook validation must derive from approved upstream truth.

The structures being validated must be traceable to:
- the AMC App Description
- approved FRS requirements
- approved TRS requirements
- approved Architecture decisions
- approved state and data design artifacts
- approved auth, audit, notification, or AI-integration decisions where relevant

If an implementation structure cannot be traced to approved design meaning, that is a design-governance defect.

### State-Domain Fidelity Requirement
Implementation structures must preserve the meaning of AMC’s major state domains.

Validation must ensure that the implementation does not incorrectly merge, flatten, or blur state domains such as:
- executive context
- conversation state
- alert and notification state
- escalation state
- approval state
- intervention state
- estate wellbeing state
- job and execution state
- identity and authority state
- sandbox and bounded-environment state
- audit-linked state references

A runtime model that treats all these as generic loose blobs or ad hoc stores is likely to undermine the operating model of AMC.

### Authority Semantics Validation
Any schema or hook pathway that touches authority, approval, or execution significance must be validated for authority correctness.

This includes ensuring that:
- authority-relevant fields and states are explicit
- approval state is represented distinctly from recommendation or request state
- delegated scope is represented clearly where relevant
- reserved-matter significance is not lost in translation between layers
- escalation-required conditions remain representable and visible
- acting identity and approving identity are not conflated

If the structure cannot faithfully represent the authority model, the implementation approach is not fit for AMC.

### Approval-State Validation
Approval-related schema and hook pathways must be validated with special rigor.

Validation should confirm, where relevant:
- pending, approved, rejected, deferred, withdrawn, expired, and superseded states are representable
- approval scope can be represented explicitly
- approval state can be rechecked before consequential action
- approval-related UI, API, and audit views can derive from consistent truth
- stale or mismatched approval can be identified rather than silently treated as valid

An approval model that works only in the happy path and becomes ambiguous under revision or timing changes is insufficient for AMC.

### Identity and Auth-State Validation
Schemas and hooks that represent acting identities, roles, scopes, or privileges must be validated for clarity and correctness.

This includes ensuring that:
- human, AI, agent, sandbox, and service identities remain distinguishable
- current authority state is representable where needed
- delegated domain state can be represented if used
- restricted or sandbox-bounded identity context remains visible to the logic that needs it
- privilege or role assumptions are not hidden in incidental UI state

AMC cannot preserve its auth model if runtime structures flatten who is acting and under what authority.

### Notification and Escalation Validation
Notification and escalation structures must be validated to ensure they preserve signal meaning.

Validation should confirm that schemas and hooks can represent:
- notification class
- severity
- acknowledgement state
- escalation state
- routing destination or target
- relationship to underlying issue or action
- resulting follow-up or closure state

If notifications and escalations are represented too loosely, the executive-operating value of AMC will erode at runtime even if the surface looks polished.

### Conversation and Executive-Context Validation
Because conversation and executive context are first-class operating mechanisms in AMC, their structures must be validated carefully.

This includes ensuring that:
- conversational state can preserve materially relevant context
- action-linked conversational meaning is not discarded too early
- executive-context summaries can be derived coherently
- state restoration does not recreate false certainty from stale conversational fragments
- conversation state and consequential action state can be linked where required

A conversational operating model cannot be trusted if its structural pathways are semantically weak.

### Intervention and Execution Pathway Validation
Any schema or hook pathway that supports intervention, execution monitoring, or job status must be validated for lifecycle correctness.

This includes ensuring that:
- intervention proposal, approval, initiation, in-flight, completion, rollback, and failure states can be represented
- execution state does not lose connection to approval or audit state
- downstream orchestration linkage remains visible where needed
- partial or degraded states can be represented safely

AMC’s intervention model is too important to be left to loosely structured runtime assumptions.

### Sandbox and Boundary Validation
Where AMC supports sandboxed environments or bounded specialist domains, schema-to-hook validation must preserve boundary integrity.

Validation must ensure that:
- sandbox identity and scope are structurally visible
- sandbox-local state is distinguishable from estate-global state
- cross-boundary proposals can be represented without silently becoming direct cross-boundary actions
- boundary-sensitive hooks do not operate on incomplete or flattened context

If a structure cannot preserve boundary meaning, the sandbox model is not being implemented safely.

### Audit-Linkage Validation
Where consequential actions occur, schemas and hooks must preserve enough structure to support audit linkage.

Validation should confirm that:
- relevant actions can be associated with identities
- approval and escalation references can be retained
- intervention or execution records can link to audit-relevant events
- AI-mediated actions remain attributable
- consequential transitions are not happening in structures that leave no meaningful trace

A runtime pathway that destroys audit-connectable meaning is non-compliant with AMC’s intended design.

### Derived-State and Selector Validation
Computed state, selectors, summaries, and derived values must also be validated.

Derived-state validation should ensure that:
- executive summaries do not hide material nuance needed for action
- convenience labels do not invert or oversimplify approval/alert/escalation meaning
- derived states remain faithful to authoritative underlying state
- stale or partially synchronized inputs do not create false decision confidence
- summarized views remain explainable

Derived convenience is useful, but in AMC it must never become semantic distortion.

### Synchronization and Persistence Validation
Where schemas and hooks interact with persistence or synchronization, validation must ensure continuity correctness.

This includes confirming that:
- persisted shapes support intended restoration behavior
- synchronization pathways do not create contradictory truths across surfaces
- stale state detection is possible
- optimistic or transient states are clearly distinguishable from durable states
- restored state cannot silently bypass renewed checks where those checks are required

AMC must preserve continuity without manufacturing false certainty.

### Validation Evidence Requirement
Schema-to-hook validation must be evidenced.

Evidence may include, as appropriate:
- traceability notes
- design review notes
- schema-to-state mapping documents
- hook contract definitions
- validation checklists
- review comments
- test scenarios targeting semantic correctness
- issue records for discovered mismatch between schema meaning and runtime behavior

The exact form may vary, but consequential structure should never rest entirely on undocumented intuition.

### Minimum Schema-to-Hook Checklist
The following minimum conditions must hold for materially significant AMC structures:

- [ ] Important schemas and state structures are traceable to approved design meaning
- [ ] Major state domains remain distinguishable in implementation structures
- [ ] Authority and approval semantics remain representable and clear
- [ ] Identity and scope semantics remain distinguishable where relevant
- [ ] Notification and escalation meaning is preserved structurally
- [ ] Conversation and executive-context structures preserve material meaning where relevant
- [ ] Intervention and execution pathways preserve lifecycle meaning where relevant
- [ ] Sandbox and boundary semantics are preserved where relevant
- [ ] Audit-linkage viability is preserved where relevant
- [ ] Derived-state abstractions do not distort approved meaning
- [ ] Persistence and synchronization structures preserve continuity without semantic drift
- [ ] Evidence of validation exists for consequential structures

### Downstream Design Consequence
Downstream Architecture and implementation planning must define which schemas, state pathways, hooks, selectors, and action handlers require formal validation review and how that review will be evidenced.

This means schema-to-hook validation cannot be deferred until late bug-fixing. It must be part of the structural review discipline of the build.

### Non-Negotiable Principle
AMC schema-to-hook validation must ensure that implementation pathways faithfully carry the approved meaning of the executive operating environment into runtime behavior.

Any implementation approach that allows schemas, hooks, selectors, or state pathways to silently distort authority, approval, audit, continuity, or boundary meaning is non-compliant with the intended purpose of AMC.


## §15 — Table Pathway Audit (§AD-11)

All persistent data pathways used by AMC must be explicitly identified, declared, and auditable.

### Required Pathway Declaration

Every AMC data pathway must declare the following before it is considered design-ready:

| Field | Definition |
|---|---|
| **Purpose** | Why this pathway exists and what executive or operational function it serves |
| **Owner** | Which system or layer is the canonical owner of the data (AMC, AIMCC, knowledge/memory system, etc.) |
| **Source of Truth** | Where the authoritative version of this data lives |
| **Read Actors** | Which actors are permitted to read this data |
| **Write Actors** | Which actors are permitted to write this data |
| **Integration Dependency** | Whether this pathway depends on AIMC, AIMCC, knowledge/memory system, or another external system |
| **Audit Expectation** | What audit events must be generated for read/write actions on this pathway |

### Pathway Coverage Requirement

This requirement covers all pathways including:
- user/account state
- agent/account state
- conversation history
- alerts and escalations
- approvals and decisions
- interventions
- AIMC action records
- upload / ingestion records and status
- AIMCC-sourced knowledge references
- audit events
- sandbox state
- operational jobs
- maintenance/assurance reports
- notification history
- device / session continuity
- memory / knowledge references presented by AMC
- operator conversation or session state where relevant

### Non-Negotiable Rule
No table or persistent storage pathway may be introduced without a complete pathway declaration satisfying all seven fields above. An undeclared or ambiguously owned pathway is a governance defect.

## §16 — RLS Audit Gate (§AD-12)

AMC shall require an explicit RLS audit gate, or an equivalent row- and record-level access-control audit gate where a different storage technology is used, so that data-access behavior remains faithful to AMC’s authority model, sandbox model, approval model, and executive-operating boundaries.

This section exists because AMC is intended to become the executive operating centre of the Maturion estate. In such a system, much of the most sensitive meaning lives not only in interfaces and workflows, but in who can see, read, modify, approve, acknowledge, escalate, or restore specific records. If access control is handled loosely at the data layer, then even well-designed UI and API logic can be undermined by storage-level overexposure, hidden privilege expansion, or inadequate boundary enforcement.

For AMC, the RLS audit gate is therefore not a technical hardening extra. It is a constitutional control that helps make authority, approval, audit, and sandbox boundaries real in persisted data behavior.

### Purpose of the RLS Audit Gate
The AMC RLS audit gate shall exist to confirm that data-layer access rules are:
- explicit
- reviewable
- aligned to approved authority meaning
- aligned to sandbox and bounded-environment meaning
- aligned to approval and audit significance
- resistant to accidental overexposure or uncontrolled privilege

The gate must ensure that persisted records are not only structurally correct, but access-correct.

### Core Principle
No materially significant persisted record in AMC may rely solely on UI courtesy, client assumptions, or informal service discipline for access protection.

Where row-level or equivalent record-level access control is relevant, the system must be able to show:
- who can read a record
- who can update a record
- who cannot
- under what scope or environment the access applies
- what special handling applies for approval-, audit-, or sandbox-sensitive data
- how service or agent exceptions are governed

If these questions cannot be answered clearly, the design is not ready.

### Scope of the Gate
The RLS audit gate applies to any persisted pathways where access boundaries materially affect governance, executive truth, or operational safety.

This includes, where relevant:
- approval records
- escalation records
- intervention records
- notification history
- executive context records
- conversation continuity records
- audit-linked records
- identity and role metadata
- sandbox and bounded-environment data
- job and execution state
- maintenance or assurance findings
- state-restoration records
- any table or equivalent structure containing sensitive role-, scope-, or decision-relevant meaning
- upload records (who submitted, what was submitted, outcome)
- ingestion status records (AIMCC-sourced, surfaced in AMC)
- AIMC action records (AI requests, responses, attribution)
- memory / knowledge reference data surfaced within AMC
- executive alert records
- operator session or conversation state where access boundaries are material

If a record can affect authority, awareness, or action, its access model falls within scope.

### Upstream Truth Coupling
RLS or equivalent record-level access rules must derive from approved upstream truth.

The access model must be traceable to:
- the AMC App Description
- approved FRS requirements
- approved TRS requirements
- approved Architecture decisions
- approved auth, authority, sandbox, audit, or state-design decisions where relevant

Access control must not invent a different authority model than the one approved upstream.

### Authority-Model Alignment Requirement
The RLS audit gate must confirm that data-access rules align with AMC’s intended authority model.

This includes ensuring that persisted records respect the distinctions between:
- Johan Ras as constitutional authority
- Maturion as resident AI executive
- Foreman as supervised orchestration authority
- independent assurance actors
- maintenance actors
- specialist agents
- sandbox-bound actors
- service identities

A data-access model that flattens these roles into overly broad shared visibility is not fit for AMC.

### Least-Privilege Requirement
The RLS audit gate must confirm that data access is designed according to least privilege.

This means:
- actors should see only what they need for their approved role
- write access should be narrower than broad operational convenience would suggest
- service identities should not inherit excessive blanket access
- sandbox-local actors should not gain estate-wide record visibility by default
- executive-only or approval-sensitive records should not become widely readable without explicit basis

AMC cannot safely support progressive autonomy if its data layer assumes everybody trusted can see everything.

### Approval-Record Access Requirement
Approval-bearing and authority-bearing records must be audited with special rigor.

The access model must ensure, where relevant, that:
- approval requests are visible to the correct approving authority
- approval history is visible to the correct reviewing roles
- approval-sensitive records are not writable by actors who should only observe them
- stale, rejected, superseded, or withdrawn approval states cannot be casually overwritten without audit significance
- actors cannot infer or manipulate approval significance through overly broad access

If approval access rules are weak, the constitutional model of AMC is weak.

### Audit-Record Access Requirement
AMC requires strong auditability, but audit visibility itself must be governed.

The RLS audit gate must therefore confirm that:
- not all actors automatically receive all audit visibility
- audit records can be exposed appropriately to executive, assurance, or maintenance roles where justified
- sensitive audit context is protected where required
- audit access itself is treated as meaningful and potentially reviewable
- boundary-sensitive audit data does not leak across sandbox or role limits

A strong audit model does not mean indiscriminate audit exposure.

### Executive-Context and Conversation Access Requirement
Where executive context or conversation continuity is persisted, the access model must preserve meaning and privacy.

This includes ensuring, where relevant, that:
- executive context records are visible to the right executive roles
- conversation-linked context is not overexposed to unrelated actors
- action-relevant context remains available where needed for continuity or review
- persisted conversation state does not become a general-purpose uncontrolled memory pool
- restoration-sensitive records remain bounded to appropriate identities and contexts

Because AMC uses a conversational operating model, weak access control here could easily undermine executive trust and boundary clarity.

### Notification and Escalation Access Requirement
Notification and escalation records must also be access-controlled in a way that preserves role meaning.

The audit gate should confirm that:
- actors can access the notifications relevant to their role and scope
- acknowledgements or escalations cannot be manipulated by unauthorized actors
- executive or reserved-matter-sensitive escalations are not broadly exposed without need
- notification history remains available for review where justified

The goal is not maximum visibility. The goal is correct visibility.

### Intervention and Execution Access Requirement
Intervention and execution records often carry operational, approval, and audit significance and must be protected accordingly.

The access model must ensure that:
- intervention proposals and outcomes are visible to the right roles
- orchestration records remain visible to supervising actors without overexposure
- execution state cannot be altered by unauthorized actors
- service or background writes do not imply uncontrolled broad read/write capability
- the relationship between intervention, approval, and execution remains protected

AMC’s intervention model is too important to rest on weak record access assumptions.

### Sandbox and Bounded-Environment Requirement
Sandbox and bounded-environment integrity must be enforceable at the data layer.

The RLS audit gate must confirm that:
- sandbox-local records remain sandbox-local by default
- specialist actors do not automatically gain estate-wide data visibility
- cross-boundary access requires explicit controlled pathways
- tenant, app, workflow, or environment scope can be represented and enforced
- estate-wide views do not accidentally absorb sandbox-local data without authorized routing

A sandbox boundary that exists only in UI logic is not adequate for AMC.

### Service and Background-Process Requirement
Where service identities, background jobs, or orchestration mechanisms need broader access, those exceptions must be governed and reviewable.

The audit gate must check that:
- service-level access is explicitly justified
- broad internal access is minimized
- exception pathways are documented
- background processes do not silently bypass role or scope assumptions
- service access still preserves audit attribution for consequential outcomes

Internal convenience must not become a hidden superuser channel.

### Policy Completeness and Conflict Check
The RLS audit gate must look for policy gaps and conflicts.

This includes checking for:
- records with no clear access policy
- overlapping policies with contradictory meaning
- broad catch-all policies that defeat least privilege
- missing policies for newly introduced state domains
- access rules that contradict UI, API, or auth assumptions
- access rules that make approval, audit, or sandbox meaning ambiguous

AMC requires policy completeness because incomplete access logic is itself a governance defect.

### Validation Evidence Requirement
RLS audit must be evidenced.

Evidence may include, as appropriate:
- access-policy inventories
- policy-to-role mapping notes
- role/read/write matrices
- review notes
- boundary-condition test scenarios
- issue records for overbroad or conflicting access
- approval notes for justified exceptions
- documentation of service-level access rationale

The exact evidence form may vary, but materially significant access policy must never remain implicit.

### Minimum RLS Audit Checklist
The following minimum conditions must hold for materially significant persisted records:

- [ ] Material records with access significance are identified
- [ ] Access rules are traceable to approved authority and boundary meaning
- [ ] Human, AI, agent, sandbox, and service roles remain distinguishable in access logic
- [ ] Least-privilege access has been considered
- [ ] Approval-bearing records have explicit access discipline
- [ ] Audit-bearing records have explicit visibility discipline
- [ ] Executive-context and conversation persistence have bounded access rules where relevant
- [ ] Notification and escalation records have role-appropriate access rules
- [ ] Intervention and execution records have role-appropriate access rules
- [ ] Sandbox and bounded-environment integrity is enforced at the data layer where relevant
- [ ] Service or background-process exceptions are justified and reviewable
- [ ] Policy gaps and contradictions have been checked
- [ ] Evidence of access-policy audit exists

### Downstream Design Consequence
Downstream TRS, Architecture, and data/access design artifacts must explicitly show how row-level or equivalent record-level protection is implemented and how it was audited against AMC’s authority model.

The RLS audit gate cannot be deferred until after database implementation is already entrenched. It must be part of the structural access design of the product.

### Non-Negotiable Principle
AMC’s RLS audit gate must ensure that persisted data access reflects the approved authority, approval, audit, and sandbox boundaries of the executive operating environment.

Any design that leaves record-level access overly broad, weakly reasoned, or misaligned with the intended operating model of AMC is non-compliant with the intended purpose of AMC.


## §17 — Auth Wiring Checklist (§AD-13)

AMC must define an explicit authentication and authorization wiring checklist before downstream build work is considered ready.

This section exists to ensure that identity, authority, approval, and boundary controls are not left to ad hoc implementation decisions or generic framework defaults. In AMC, authentication and authorization are constitutional controls as much as technical controls. They are part of how reserved matters, executive delegation, orchestration scope, sandbox containment, and auditability are enforced in real system behavior.

### Purpose of the Auth Wiring Checklist
The AMC auth wiring checklist shall exist to confirm, before substantive implementation proceeds, that the application’s identity and authority design has been translated into concrete build expectations.

The checklist must ensure that downstream design and implementation can answer, at minimum:
- who can act
- under what identity
- with what authority
- within what scope
- subject to what approval conditions
- with what audit traceability
- across which environments or boundaries

A design that leaves those questions to later inference is non-compliant.

### Core Principle
AMC authentication wiring must be explicit, reviewable, and traceable.

It is not sufficient to state that the application “uses auth.” The checklist must verify that the intended authority model is actually wired into:
- user-facing flows
- AI and agent flows
- API pathways
- service-to-service pathways
- sandbox-bounded pathways
- approval-gated actions
- audit-linked enforcement points

### Required Identity Wiring Checks
The auth wiring checklist must confirm that all required identity classes are explicitly represented in the design.

At minimum, wiring must account for:
- Johan Ras as human executive authority
- future approved human roles if introduced
- Maturion as resident executive AI identity
- Foreman as orchestration identity
- IAA or equivalent assurance identities where applicable
- maintenance agent identities
- specialist-agent identities
- sandbox-bound identities
- governed service identities for internal infrastructure actions

The checklist must reject any design that collapses these materially different roles into an indistinct access model where authority can no longer be clearly enforced.

### Required Authority Mapping Checks
The checklist must confirm that each important identity class has a defined authority mapping.

This includes verification that the design defines:
- what the identity is allowed to do
- what it is explicitly not allowed to do
- what approval-gated actions apply
- what reserved-matter restrictions apply
- what sandbox or environment limits apply
- what escalation path applies when authority is insufficient

An identity without an explicit authority map is an unresolved governance defect.

### Required Reserved-Matter Wiring Checks
The checklist must confirm that reserved matters are not merely described in documents but protected in real system pathways.

This includes confirmation that:
- reserved-matter actions are identified
- those actions are classified consistently across UI, API, and workflow layers
- approval requirements for those actions are enforced
- execution is blocked if valid approval is absent
- the relevant authority boundary is visible to the acting user or agent
- audit records capture the reserved-matter pathway

Reserved-matter enforcement must never depend solely on UI wording or user goodwill.

### Required Approval-Flow Wiring Checks
The checklist must confirm that approval-gated actions are fully wired from detection to enforcement.

This includes validation that:
- approval-requiring actions are classified at design time
- the correct approving authority is identified
- approval requests can be generated and surfaced
- approval state can be stored and re-evaluated
- execution pathways verify approval state before action
- approval expiry, revision mismatch, or scope mismatch can invalidate stale approvals
- approval outcomes are audit-linked

A button, endpoint, or AI action that can proceed without re-checking relevant approval state is non-compliant.

### Required Agent and AI Wiring Checks
The checklist must confirm that agent and AI identities are explicitly wired and bounded.

This includes confirmation that:
- Maturion actions are distinguishable from human actions
- Foreman actions are distinguishable from Maturion actions
- specialist agents are distinguishable from estate-level executive or orchestration actors
- maintenance and assurance pathways remain distinct
- AI recommendation, routing, and execution behaviors are not conflated
- delegated AI authority, if any, is explicit rather than implicit

AMC must not allow “the AI did it” to become an untraceable explanation for consequential action.

### Required Sandbox and Boundary Wiring Checks
Where sandboxed environments or bounded specialist domains exist, the checklist must confirm that auth wiring preserves those limits.

This includes validation that:
- sandbox identities are limited to their own scope
- cross-boundary actions are blocked or escalated
- tenant, app, workflow, or environment boundaries are identifiable in access logic
- estate-level actions cannot be performed from sandbox scope without explicit elevation
- sandbox actions remain attributable and auditable

Sandbox containment must be technically wired, not merely described conceptually.

### Required Service-to-Service Wiring Checks
The checklist must confirm that internal services do not bypass the intended authority model.

This includes confirmation that:
- service identities are governed
- machine pathways are attributable
- privileged internal actions are bounded by least privilege
- background jobs do not silently exercise broader authority than approved
- service-to-service calls preserve audit linkage for consequential behavior

No internal integration path may function as a hidden superuser shortcut.

### Required Session and Step-Up Checks
Because AMC is intended for mobile and desktop executive use, the checklist must confirm that session handling is compatible with authority sensitivity.

This includes validation that:
- sensitive actions can require step-up authentication or equivalent confidence checks where appropriate
- session restoration does not silently restore privileged capability beyond allowed boundaries
- interrupted approval or intervention flows preserve context safely
- read-oriented awareness access is distinguished from write-capable privileged action paths
- cross-device continuity does not weaken control over consequential actions

Convenience is valuable in AMC, but not at the cost of constitutional or operational integrity.

### Required Failure-Handling Checks
The checklist must confirm that auth-related failure cases are deliberately designed.

This includes verification that the system can distinguish and handle:
- unauthenticated state
- invalid identity
- insufficient authority
- missing approval
- expired or mismatched approval
- sandbox-boundary violation
- policy-based restriction
- escalation-required conditions

Failure handling must preserve clarity for users and agents without leaking sensitive control information inappropriately.

### Required Audit Coupling Checks
The checklist must confirm that authentication and authorization outcomes are linked to the audit model.

This includes validation that consequential actions can record:
- authenticated identity
- authority classification
- evaluated approval state
- execution or rejection result
- timing and context
- related workflow, escalation, or intervention reference

An auth design that enforces control but leaves no meaningful record is incomplete for AMC.

### Minimum Checklist Items
The following minimum checklist items must be satisfied before downstream implementation is considered auth-ready:

- [ ] Identity classes are enumerated and named
- [ ] Authority domains are mapped for each identity class
- [ ] Reserved-matter actions are identified and protected
- [ ] Approval-gated actions are identified and enforced
- [ ] Maturion, Foreman, specialist, maintenance, and assurance identities are distinguishable
- [ ] Sandbox-bound identities and boundaries are defined where applicable
- [ ] Service-to-service identity design is defined
- [ ] Session and step-up requirements are identified
- [ ] Failure-handling states are identified
- [ ] Audit linkages for consequential auth decisions are defined
- [ ] UI, API, workflow, and state layers use consistent authority classifications
- [ ] Auth wiring assumptions are documented for downstream FRS/TRS/Architecture work

### Downstream Design Requirement
Downstream FRS, TRS, and architecture work must not merely mention authentication in broad terms. They must explicitly satisfy this checklist and show how AMC’s authority model becomes real in:
- routes
- screens
- action handlers
- APIs
- service integrations
- approval flows
- sandbox pathways
- audit records

Checklist completion must be evidenced, not assumed.

### Non-Negotiable Principle
AMC’s auth wiring checklist must make identity, authority, approval, and boundary enforcement testable before build execution.

Any design that leaves those controls vague, inconsistent across layers, or dependent on implementation convenience is non-compliant with the intended purpose of AMC.

### Auth Boundary Definitions

AMC must explicitly distinguish between the following authentication and authorization contexts:

| Auth Context | Definition |
|---|---|
| **Human user auth** | Authentication of Johan Ras or other human principals accessing AMC. JWT-based; must support session continuity across desktop and mobile. |
| **Executive approval authority** | Authorization model for governance-sensitive decisions that require explicit approval. Must be distinct from general operational access. Must produce audit records. |
| **AMC internal service auth** | Auth model for AMC backend services communicating internally. Must use service-level credentials, not user JWT. |
| **AIMC service auth** | Auth model for AMC communicating with AIMC. Must use approved AIMC gateway credentials. AMC must not impersonate a user to AIMC. |
| **AIMCC / knowledge service auth** | Auth model for AMC communicating with AIMCC and knowledge / memory system. Must use approved AIMCC service credentials. AMC must not impersonate a user to AIMCC. |
| **Privileged operational actions** | Actions that require elevated authority (e.g., triggering interventions, approving governance actions). Must require explicit approval-authority validation, not just presence of a valid session. |

These distinctions must be preserved in TRS, Architecture, and implementation. Collapsing them is a governance defect.


## §18 — AI Integration Requirements (§AD-14)

AMC is an AI-intensive application, but all AI integration must remain governed, auditable, and architecturally disciplined.

### Core AI Integration Principle
All AMC AI capability shall be integrated through approved AIMC and AIMC Gateway pathways. AMC shall not embed uncontrolled direct model-provider coupling in client or server logic.

This requirement exists to preserve:
- centralized control of model access
- policy enforcement
- provider abstraction
- credential discipline
- auditability
- future portability of specialist and executive AI capabilities

### Executive AI Role
AMC shall host **Maturion** as the resident AI executive.

Maturion shall be capable of:
- maintaining conversational continuity with Johan Ras
- proactively surfacing risks, decisions, events, and anomalies
- synthesizing reports from subordinate agents
- supporting executive understanding and decision preparation
- coordinating operational follow-through after approved decisions
- maintaining estate-level wellbeing awareness over time

Maturion’s role is executive and supervisory. It is not merely a chat assistant embedded in a dashboard.

### Orchestration AI Separation
Foreman-related orchestration intelligence, where present, must remain distinct from Maturion’s executive role.

AMC must preserve a clear difference between:
- executive AI responsible for estate-level awareness and decision support
- orchestration AI responsible for coordinating execution processes
- specialist AI responsible for bounded domain work
- assurance AI responsible for independent evaluation
- maintenance AI responsible for upkeep and scan-oriented activity

No implementation shortcut may collapse these roles into a single undifferentiated “AI backend” if doing so destroys accountability, traceability, or governance clarity.

### Specialist-Agent Integration
AMC shall support specialist-agent integration through controlled patterns.

Supported specialist patterns may include:
- AIMC-based specialists
- sandboxed app-environment specialists
- workflow-design specialists inside tenant or app sandboxes
- compliance, security, maintenance, or analysis specialists
- future capability-specific specialists introduced through approved governance

Each specialist integration must define:
- purpose
- scope boundary
- authority boundary
- data boundary
- reporting path
- escalation path
- audit expectations

### Sandboxed AI Environments
AMC shall support the concept of sandboxed AI working environments inside or adjacent to consumer applications where bounded specialist teams can operate safely.

Sandboxed AI environments must:
- remain isolated from broader estate authority by default
- operate within explicit tenancy, app, workflow, or environment boundaries
- report outcomes through governed pathways
- prevent uncontrolled propagation of changes outside approved boundaries
- support human and executive oversight where required

The presence of sandboxed AI must not weaken global governance or estate-level control.

### Proactive Communication Requirement
AMC AI integration must support proactive communication behavior, not just reactive answer generation.

Maturion and other approved AI layers must be able to:
- notify before being asked where justified
- surface emerging issues early
- request approval when thresholds are crossed
- recommend action when action is warranted
- escalate when executive attention is required

The product is non-compliant with intended purpose if it only supports passive, query-only interaction.

### Approval and Action Boundaries
AI within AMC may support recommendation, routing, preparation, and coordination of action, but governance-sensitive actions must respect approval boundaries.

Where an action touches:
- governance
- agent files
- constitutional boundaries
- major design or scope changes
- other reserved matters

the AI layer must surface the action for the correct approval authority rather than silently proceeding.

### AI Traceability and Audit
All AI-originated or AI-mediated significant actions shall be traceable.

Traceability expectations include:
- which AI role acted or recommended
- what context informed the action or recommendation
- what approval, if any, was required
- what downstream operational consequence followed
- what audit record was created

AI-driven opacity is not acceptable in AMC because the application is intended to manage progressively autonomous operations.

### Model and Provider Discipline
AMC must not assume permanent coupling to any single underlying provider or model family.

AI integration design should support:
- provider abstraction through AIMC
- governed model selection
- specialist-to-model alignment where appropriate
- replacement or evolution of model providers without rewriting product identity
- controlled handling of credentials, quotas, routing policies, and safety controls

### Human-in-the-Loop and Future Delegation
AMC must support today’s human-in-the-loop reality and tomorrow’s progressive delegation model.

Therefore the AI integration design must:
- preserve Johan Ras approval on reserved matters
- support gradual expansion of Maturion’s operational authority where explicitly approved
- make delegated domains visible and auditable
- allow authority rollback where required
- avoid hidden transfer of decision rights through technical convenience

### Non-Negotiable Principle
AI in AMC exists to strengthen governed executive capability, not to create an unbounded autonomous black box.

Any AI integration that weakens governance, obscures authority, bypasses AIMC controls, or makes executive accountability harder to determine is non-compliant with AMC’s intended design.

### Multi-Layer AI Integration Model

AMC’s AI integration operates in a strict multi-layer model. This must be explicit in all downstream artifacts.

**Layer definitions:**
- **AMC (application layer)**: executive supervisory surface. Initiates AI-assisted actions, surfaces AI results, routes requests. Does NOT execute AI models.
- **AIMC (sole governed AI gateway)**: the only actor permitted to execute AI model requests within the estate. All AI execution from AMC context must route through AIMC. No exceptions.
- **AIMCC (governed knowledge and memory layer)**: governs knowledge ingestion, knowledge storage, and memory operations. AI-assisted knowledge operations are governed by AIMCC in conjunction with AIMC.
- **Knowledge Upload Centre (governed ingestion surface)**: the submission gateway for knowledge uploads. Routes to AIMCC.
- **Knowledge / memory system (persistent substrate)**: the authoritative persistent store for estate knowledge and memory. Not a component of AMC. AMC surfaces it, not owns it.

**Explicit prohibitions:**
- AMC must NOT execute AI model calls directly, bypassing AIMC
- AMC must NOT ingest knowledge directly, bypassing AIMCC / Knowledge Upload Centre
- AMC must NOT present AI-generated or retrieved text as authoritative estate memory without provenance attribution
- AMC must NOT silently duplicate canonical memory / knowledge truth in AMC-private storage
- AMC must NOT treat AIMC unavailability as a license to fall back to direct model calls

**Degraded mode requirements:**
- AIMC unavailable: AMC must surface AIMC degraded status to the operator. AI-dependent features must enter a defined degraded mode, not fail silently.
- AIMCC unavailable: AMC must surface AIMCC degraded status. Upload and knowledge-reference features must enter a defined degraded mode.
- Memory / knowledge system degraded: AMC must surface degraded status. Knowledge retrieval surfaces must explicitly indicate stale or unavailable state.


## §19 — Edge Function Registry (§AD-15)

AMC shall maintain an explicit Edge Function Registry, or equivalent callable-service registry where a different execution model is used, so that consequential backend behavior remains visible, governed, reviewable, and aligned with the executive operating model of the estate.

This section exists because AMC is intended to become the executive operating centre of the Maturion estate. In such a system, many of the most consequential actions will not occur only in visible UI flows. They may occur through server-side actions, orchestration endpoints, notification dispatchers, approval handlers, audit writers, AI-routing services, sandbox coordinators, and background-triggered execution paths. If those callable behaviors are allowed to emerge as hidden plumbing, the product can appear governed at the surface while critical authority, approval, audit, or boundary logic is actually happening in opaque technical channels.

For AMC, the edge-function registry is therefore not an implementation convenience list. It is part of the governance surface of the application.

### Purpose of the Edge Function Registry
The AMC Edge Function Registry shall exist to ensure that every materially significant callable function or service pathway can be understood in terms of:
- what it does
- why it exists
- what authority significance it carries
- who or what may invoke it
- what approvals, identities, or scopes govern it
- what state it reads or writes
- what audit consequences it produces
- what environment or sandbox boundaries apply

The registry must make consequential execution surfaces visible before they harden into undocumented operational power.

### Core Principle
No materially significant callable behavior in AMC may remain hidden, unnamed, or semantically vague.

Any function, action handler, edge routine, service operation, or equivalent backend execution surface that can materially influence:
- authority
- approval
- notification
- escalation
- intervention
- audit
- AI behavior
- sandbox boundaries
- estate truth

must be explicitly registered and reviewable.

If a callable pathway exists but its operational meaning cannot be clearly explained, the design is not ready.

### Scope of the Registry
The registry applies to all materially significant callable execution surfaces, including where relevant:
- edge functions
- server actions
- orchestration actions
- approval handlers
- escalation handlers
- intervention launch actions
- audit-writing functions
- notification dispatch functions
- AI-routing or AI-invocation gateway functions
- sandbox coordination functions
- state-restoration or continuity functions
- maintenance and assurance ingestion functions
- service-to-service operational endpoints
- background-triggered execution routines

The exact implementation technology may vary, but the governing requirement is that consequential callable behavior must be inventoried and governed.

### Upstream Truth Coupling
Registered callable behaviors must be traceable to approved upstream truth.

Each significant function or equivalent execution surface must be traceable to:
- the AMC App Description
- approved FRS requirements
- approved TRS requirements
- approved Architecture decisions
- approved auth, audit, state, notification, AI, or sandbox design decisions where relevant

A callable pathway that exists solely because it was convenient to implement, but has no clear traceable product meaning, is a governance defect.

### Required Registry Fields
For each materially significant registered function or equivalent execution surface, the registry should record at minimum:
- function or action name
- purpose
- owning domain or component
- invocation type
- triggering actor class
- permitted caller identities or roles
- required approval state where relevant
- authority classification
- data/state touched
- audit consequence
- notification or escalation consequence where relevant
- sandbox or boundary implications where relevant
- failure or rejection behavior summary
- deployment/environment relevance
- current status, such as draft, active, deprecated, or superseded

The exact registry format may evolve, but these meanings must be preserved.

### Purpose and Authority Requirement
Each registered function must have a clear purpose and authority classification.

It must be possible to determine:
- whether the function is informational, operational, approval-gated, audit-writing, AI-routing, notification-related, or intervention-related
- whether it acts in a routine delegated domain
- whether it touches reserved-matter-adjacent pathways
- whether it merely prepares action or can cause consequential state change
- whether it is sandbox-local, estate-wide, or cross-boundary

AMC cannot safely govern callable behavior if it does not know what authority significance each function carries.

### Invocation and Caller Requirement
The registry must define who or what may invoke each registered function.

This includes clarifying:
- human executive invocation
- Maturion invocation
- Foreman or orchestration invocation
- maintenance or assurance invocation
- specialist or sandbox-bound invocation
- internal service invocation
- background or scheduled invocation

Caller identity is crucial because the same function may have different governance meaning depending on who or what triggered it.

### Approval and Gating Requirement
Functions that touch approval-sensitive or authority-sensitive behavior must have explicit gating semantics recorded in the registry.

The registry should indicate where relevant:
- whether the function requires prior approval
- what authority must approve
- whether the function can only prepare a request rather than execute change
- whether stale or missing approval must block execution
- whether escalation is required when approval is absent

A callable execution surface that can materially act without clear approval semantics is non-compliant for AMC.

### Data and State Interaction Requirement
The registry must identify the major data and state domains affected by each function.

This includes, where relevant:
- approval state
- escalation state
- intervention state
- audit state
- conversation-linked state
- executive-context state
- job or execution state
- sandbox-bound state
- notification state
- restoration or continuity state

This requirement exists so that functions are reviewed not merely as code entry points, but as operators on constitutionally meaningful product truth.

### Audit and Traceability Requirement
The registry must record the audit significance of each consequential function.

This includes clarifying:
- whether invocation is auditable
- whether downstream action is auditable
- whether approval linkage must be recorded
- whether acting identity must be preserved
- whether the function creates, updates, or depends on audit-bearing records

AMC requires callable surfaces to be reviewable not only at design time but in historical consequence as well.

### AI Routing and AI Action Requirement
Any function that routes to, invokes, mediates, or operationalizes AI capability must be registered with special care.

The registry should clarify where relevant:
- whether the function invokes AIMC-governed AI pathways
- which AI role it serves, such as Maturion, orchestration, specialist, maintenance, or assurance
- whether it merely requests AI analysis or can trigger consequential operational behavior
- what approval or authority restrictions apply
- what audit requirements apply

This is necessary to prevent AI-enabled execution surfaces from becoming opaque power channels.

### Notification and Escalation Requirement
Functions involved in notification or escalation must preserve signal meaning and role significance.

The registry should identify:
- what kinds of notifications or escalations the function may generate
- what triggers apply
- who may receive the resulting signal
- whether the function merely emits or also changes state
- whether follow-up acknowledgement or escalation logic depends on it

AMC’s proactive-awareness model is too important to leave its execution surfaces undocumented.

### Intervention and Orchestration Requirement
Functions that launch, coordinate, or update interventions or execution flows must be explicitly governed.

The registry must clarify where relevant:
- whether the function can initiate intervention
- whether it can update intervention lifecycle state
- what relationship it has to Foreman or orchestration pathways
- whether it can affect job or execution status
- what approval and audit requirements constrain it

This is particularly important because AMC is expected to support governed intervention from real executive contexts.

### Sandbox and Boundary Requirement
Any callable surface that operates within or across sandbox boundaries must declare those implications explicitly.

The registry should identify:
- whether the function is sandbox-local
- whether it can propose cross-boundary effects
- whether it can operate on estate-wide state
- what safeguards prevent sandbox-local invocation from silently producing estate-level consequence
- what role and scope limitations apply

A sandbox model is not real if callable execution surfaces can bypass it invisibly.

### Failure and Rejection Requirement
The registry must describe the failure and rejection meaning of each consequential function.

This includes, where relevant:
- what happens if approval is missing
- what happens if caller identity is insufficient
- what happens if sandbox boundaries forbid execution
- what happens if downstream dependencies are unavailable
- whether failure is auditable
- whether escalation or retry paths exist

A function registry that only describes happy-path intent is insufficient for AMC.

### Lifecycle and Status Requirement
Registered functions must carry lifecycle status.

The registry should make clear whether a function is:
- planned
- active
- restricted
- deprecated
- superseded
- disabled
- lineage-only or historical

This prevents stale or legacy callable surfaces from being mistaken for approved active capability.

### Validation Evidence Requirement
The function registry must be evidenced and reviewable.

Evidence may include, as appropriate:
- a formal registry document or table
- design-review notes
- route/function inventories
- auth and approval review notes
- audit-linkage notes
- issue records for unregistered or ambiguous callable surfaces
- deprecation or supersession notes for retired functions

The exact form may vary, but consequential callable behavior must not remain unregistered.

### Minimum Edge Function Registry Checklist
The following minimum conditions must hold for materially significant callable surfaces:

- [ ] Significant functions or equivalent callable surfaces are inventoried
- [ ] Each function has a defined purpose
- [ ] Each function has a defined authority classification
- [ ] Caller identities or roles are identified
- [ ] Approval and gating semantics are identified where relevant
- [ ] Data/state touched is identified at a meaningful level
- [ ] Audit consequences are identified where relevant
- [ ] AI-routing functions are explicitly recognized where relevant
- [ ] Notification and escalation functions are explicitly recognized where relevant
- [ ] Intervention/orchestration functions are explicitly recognized where relevant
- [ ] Sandbox and boundary implications are identified where relevant
- [ ] Failure and rejection behavior is acknowledged where relevant
- [ ] Lifecycle status of each function is visible
- [ ] Evidence of registry maintenance exists

### Downstream Design Consequence
Downstream TRS, Architecture, API/auth design, audit design, and operational planning artifacts must explicitly identify AMC’s consequential callable surfaces and keep the registry aligned with reality.

The registry may not be treated as optional documentation added after implementation. It is part of how AMC prevents invisible execution power from accumulating outside governance.

### Non-Negotiable Principle
AMC’s Edge Function Registry must make consequential callable behavior visible, governable, and reviewable as part of the executive operating environment.

Any design that allows important backend execution surfaces to remain hidden, weakly classified, or detached from authority, approval, audit, or boundary meaning is non-compliant with the intended purpose of AMC.

### Required AMC Edge Function Families

The following server-side function families must be defined and registered before build proceeds:

| Function Family | Purpose |
|---|---|
| **Alert handlers** | Generate, route, acknowledge, escalate, and expire executive alerts |
| **Approval / intervention handlers** | Process approval decisions, record outcomes, route interventions, handle cancellation |
| **AIMC adapters** | Proxy AI requests from AMC to AIMC gateway; handle AIMC responses; record audit events; handle AIMC degraded state |
| **AIMCC / upload adapters** | Submit uploads to Knowledge Upload Centre; retrieve ingestion status from AIMCC; surface quota state; handle AIMCC degraded state |
| **Audit write functions** | Write audit events for all consequential AMC actions with required fields (actor, source, object, action, timestamp, outcome) |
| **Memory-reference / knowledge-resolution services** | Query knowledge / memory system via governed API; attach provenance to returned references; handle memory degraded state |
| **Degraded-mode handlers** | Implement defined degraded-mode behavior for each external dependency; surface degraded status to operator |

Each function family must have its own QA-to-Red test coverage and must not execute AI or ingest knowledge outside its governed pathway.


## §20 — Deployment Wave (§AD-16)

AMC shall be delivered through a governed deployment-wave model so that the executive operating centre of the Maturion estate emerges through controlled, reviewable capability increments rather than a monolithic all-at-once release.

This section exists because AMC is not a routine internal application with low constitutional significance. It is intended to become the executive operating surface through which authority, approvals, proactive awareness, intervention, audit visibility, AI-mediated reporting, and long-lived estate continuity are managed. Releasing all of that in one undifferentiated deployment motion would create unnecessary governance risk, operational risk, and design incoherence. A wave model is therefore required to stage capability growth in a way that preserves truth, reviewability, and rollback discipline.

For AMC, deployment waves are not merely scheduling convenience. They are part of the control framework by which ambition is converted into safe, governable operational reality.

### Purpose of the Deployment Wave Model
The AMC deployment-wave model shall exist to ensure that:
- capability is introduced in a controlled sequence
- earlier waves establish dependable foundations for later waves
- high-consequence functionality is not released before its supporting controls exist
- rollout risk is segmented and reviewable
- operational learning can inform subsequent waves
- executive trust is earned through stable progression rather than claimed through premature breadth

If AMC attempts to leap directly into its full long-term vision without staged control, the result is likely to be brittle delivery and blurred operational readiness.

### Core Principle
Each deployment wave must introduce a coherent and governable slice of AMC capability, not a random bundle of partially related features.

A valid wave for AMC must:
- have a clear purpose
- have clear boundaries
- have explicit dependencies
- have explicit readiness expectations
- preserve authority, approval, audit, and state integrity appropriate to its scope
- leave the estate in a more usable and governable state than before

A wave that merely accumulates unfinished capability without operational coherence is not acceptable.

### Relationship to Lifecycle and Derivation
The deployment-wave model sits downstream of the App Description, FRS, TRS, Architecture, and build-planning stages.

This means deployment waves do not create product truth. They operationalize already approved truth in controlled increments.

Accordingly:
- Stage 1 defines the governing intent of the wave model
- FRS and TRS define the capabilities and constraints each wave must preserve
- Architecture defines the structural enablers and boundaries
- build planning decomposes delivery into wave-ready work packages
- deployment waves introduce those packages into live or live-like operation under governed conditions

A deployment wave may sequence capability, but it may not rewrite approved product meaning.

### Wave Design Requirement
Each AMC deployment wave must be designed as a meaningful operational increment.

For each wave, the design should be able to answer:
- what new executive capability becomes available
- what remains intentionally out of scope
- what foundations this wave depends on
- what new risks this wave introduces
- what new approvals or operational controls become necessary
- what rollback or containment options exist
- what evidence will show that the wave succeeded or failed

This prevents wave planning from becoming arbitrary sequencing with no operational accountability.

### Indicative Wave Model
AMC’s precise waves will be finalized in downstream artifacts, but Stage 1 shall define an indicative governing wave structure.

#### Wave 1 — Foundation and Executive Baseline
This wave establishes the minimum governed executive baseline for AMC.

Indicative capability focus:
- approved Stage 1 truth and essential downstream design baseline
- initial executive operating surface
- initial estate visibility foundation
- foundational auth, audit, and shared-state scaffolding
- initial conversation surface with Maturion where appropriate
- initial tracker and operational truth discipline

Wave 1 must not overclaim maturity. Its purpose is to establish the control-plane foundation, not to simulate the full future estate.

#### Wave 2 — Core Executive Interaction and Awareness
This wave introduces core interaction capability required for AMC to begin functioning as an executive operating environment.

Indicative capability focus:
- meaningful dashboard and drill-down visibility
- proactive awareness foundations
- notification-class handling foundations
- usable executive conversation flows
- initial approval and escalation surfaces
- foundational cross-surface context continuity

Wave 2 should make AMC meaningfully usable for supervised awareness without yet requiring full delegated operational breadth.

#### Wave 3 — Approval, Escalation, and Intervention Control
This wave introduces governed action capability.

Indicative capability focus:
- stronger approval workflows
- escalation handling
- intervention initiation pathways
- status follow-through for governed actions
- tighter coupling between notification, approval, and audit
- stronger authority-aware action controls

Wave 3 is significant because it begins to move AMC from awareness-only into governed executive action.

#### Wave 4 — Specialist and Sandbox Oversight
This wave introduces more of AMC’s multi-agent and bounded-environment operating model.

Indicative capability focus:
- visibility into specialist-agent domains
- bounded sandbox oversight
- sandbox-aware state and access behaviors
- clearer relationship between estate-wide executive oversight and local specialist environments
- improved role clarity for specialist and bounded actors

Wave 4 should not weaken boundary discipline in the name of broader visibility.

#### Wave 5 — Maintenance, Assurance, and Estate Wellbeing Integration
This wave strengthens AMC as a genuine wellbeing centre for the estate.

Indicative capability focus:
- maintenance reporting integration
- assurance finding integration
- integrity, compliance, performance, or health visibility where relevant
- stronger estate wellbeing synthesis
- clearer operational review and follow-up pathways

Wave 5 should make AMC better able to act as a long-lived oversight environment rather than merely a control dashboard.

#### Wave 6 — Progressive Delegation and Higher Autonomy
This wave introduces carefully governed expansion of autonomous or semi-autonomous operating capability where approved.

Indicative capability focus:
- broader Maturion executive operating scope within approved domains
- richer coordination across subordinate operational actors
- tighter supervised response loops
- stronger automation inside clearly bounded authority envelopes
- more mature operational continuity across the estate

Wave 6 must be treated with special governance discipline because it touches the long-term transition toward greater operational delegation.

### Wave Dependency Requirement
Each deployment wave must explicitly declare its dependencies.

Dependencies may include:
- required upstream artifacts
- prior wave completion
- auth or audit foundations
- shared-state foundations
- AI-routing readiness
- notification readiness
- sandbox-boundary controls
- operational runbooks
- approval or governance decisions

A wave may not proceed just because its visible features are attractive if its foundational controls are still missing.

### Wave Readiness Requirement
Each wave must satisfy explicit readiness conditions before release or promotion.

Readiness should include, where relevant:
- artifact readiness
- implementation readiness
- verification readiness
- physical verification readiness where applicable
- auth and audit readiness
- rollback readiness
- tracker and approval-record readiness
- known-risk visibility

For AMC, “wave ready” must mean operationally defensible, not merely technically mergeable.

### Wave Integrity Rule
A deployment wave must preserve AMC’s constitutional integrity within its current scope.

This means a wave may not:
- introduce action capability without appropriate authority and approval controls
- introduce AI-mediated capability without appropriate routing, traceability, and policy discipline
- introduce cross-boundary capability without sandbox and access controls
- introduce executive visibility that is materially misleading due to weak state or audit foundations
- imply readiness or autonomy beyond what the wave actually supports

A smaller but honest wave is better than a broader but constitutionally fragile wave.

### Rollback and Containment Requirement
Each wave must have a rollback or containment posture appropriate to its consequence.

The wave design should define, where relevant:
- what can be disabled or rolled back
- what data or state implications exist
- what user or agent expectations would be affected
- what fallback mode exists
- how failed wave behavior is surfaced and governed

For AMC, rollback is not only technical. It is also an executive-trust mechanism.

### Operational Learning Requirement
Deployment waves must support learning between increments.

After each significant wave, the delivery model should allow for review of:
- what behaved as expected
- what governance assumptions held or failed
- what executive UX worked or failed in practice
- what authority or boundary issues emerged
- what should change before the next wave

This matters because AMC is intentionally ambitious and will mature through governed learning, not one-shot certainty.

### Wave Status and Governance Visibility
Wave state must be visible in governance and tracking artifacts.

For each wave, it should be possible to determine:
- whether it is planned, in progress, ready, deployed, limited, rolled back, or superseded
- what capabilities it included
- what approvals governed it
- what blockers or issues remain
- whether later waves depend on unresolved issues from it

Wave planning without status truthfulness is not compatible with AMC’s intended operating discipline.

### Minimum Deployment Wave Checklist
The following minimum conditions must hold for AMC wave planning:

- [ ] The wave has a clear purpose
- [ ] The wave has explicit scope boundaries
- [ ] Dependencies are identified
- [ ] Required controls, such as auth, audit, approval, and state foundations, are considered
- [ ] Readiness conditions are defined
- [ ] Rollback or containment posture is considered
- [ ] Wave-specific risks are visible
- [ ] The wave does not imply greater authority or autonomy than it truly supports
- [ ] Wave status can be tracked truthfully
- [ ] Evidence and learning from the wave can inform later waves

### Downstream Design Consequence
Downstream Architecture, build planning, verification planning, deployment planning, and tracker artifacts must explicitly model AMC delivery in waves rather than treating deployment as a single undifferentiated event.

Wave design must remain subordinate to the governing truth established in Stage 1, but detailed enough to control risk and progression in later stages.

### Non-Negotiable Principle
AMC’s deployment wave model must ensure that the executive operating centre of the estate is introduced through controlled, reviewable, and governable increments.

Any deployment approach that attempts to release broad consequential capability without wave discipline, readiness discipline, and rollback discipline is non-compliant with the intended purpose of AMC.

### Cross-System Commissioning Checks

Before any AMC deployment wave is declared complete, the following commissioning checks must pass:

- **AIMC reachability**: AIMC gateway is reachable from the deployed AMC environment; a test AI request routes correctly
- **AIMCC / Knowledge Upload Centre reachability**: AIMCC and Knowledge Upload Centre services are reachable; a test upload submission routes correctly
- **Memory-system availability**: knowledge / memory system is reachable via governed API; a test knowledge query returns with provenance
- **Audit write integrity**: audit events are being written correctly; at minimum one test event per major event class is verified
- **Dependency degradation safety**: AIMC simulated unavailability → AMC enters defined degraded mode (NOT silent failure); AIMCC simulated unavailability → AMC enters defined degraded mode

These checks must be recorded in the deployment evidence bundle before the deployment wave is closed.


## §21 — Secret Naming Convention (§AD-17)

AMC requires strict secret management. All credentials, tokens, and keys must be classified, named consistently, and bounded by the governed layer they authenticate.

### Core Rule
AMC must NOT hold unmanaged direct model-provider credentials. When AIMC is the approved AI gateway, all AI execution credentials are held by AIMC, not by AMC. AMC holds only the approved AIMC gateway credentials for routing requests.

### Secret Classes

| CLASS token | Purpose | Owner | Notes |
|---|---|---|---|
| `RUNTIME` | AMC application runtime credentials (database connection, session keys, etc.) | AMC | Scoped to AMC's own operational needs |
| `AIMC` | Credentials for AMC → AIMC gateway communication | AMC (holds); AIMC (issues) | Must NOT be direct model-provider credentials |
| `AIMCC` | Credentials for AMC → AIMCC, AMC → Knowledge Upload Centre, AMC → knowledge/memory system communication | AMC (holds); AIMCC (issues) | Must not grant write access to canonical knowledge truth |
| `AUDIT` | Credentials for AMC → audit log or observability platform | AMC | Scoped to write-only audit events |

### Naming Convention
Secret names must follow the pattern: `AMC_[CLASS]_[PURPOSE]_[ENVIRONMENT]`

Where:
- `CLASS` = one of the class tokens listed above: `RUNTIME`, `AIMC`, `AIMCC`, or `AUDIT`
- `PURPOSE` = the specific purpose within the class (e.g., `DATABASE`, `GATEWAY_KEY`, `SERVICE_KEY`, `WRITE_KEY`)
- `ENVIRONMENT` = deployment environment (e.g., `PROD`, `STAGING`, `DEV`)

Examples:
- `AMC_RUNTIME_DATABASE_PROD` (CLASS=`RUNTIME`, PURPOSE=`DATABASE`, ENVIRONMENT=`PROD`)
- `AMC_AIMC_GATEWAY_KEY_PROD` (CLASS=`AIMC`, PURPOSE=`GATEWAY_KEY`, ENVIRONMENT=`PROD`)
- `AMC_AIMCC_SERVICE_KEY_PROD` (CLASS=`AIMCC`, PURPOSE=`SERVICE_KEY`, ENVIRONMENT=`PROD`)
- `AMC_AUDIT_WRITE_KEY_PROD` (CLASS=`AUDIT`, PURPOSE=`WRITE_KEY`, ENVIRONMENT=`PROD`)

### Non-Bypass Rule
Secret design must make it structurally impossible for AMC to call AI model providers directly. If AIMC is the governed gateway, AMC must not hold or use model-provider API keys.

## §22 — Deployment Runbook (§AD-18)

Before live deployment or production-like rollout, AMC must have a deployment runbook covering:
- deployment sequence
- prerequisites and approvals
- rollback procedure
- operational verification checks
- notification verification
- audit verification
- incident escalation routes
- authority checkpoints for governance-sensitive rollout steps

Because AMC is itself a control centre, its deployment quality standard must be higher than that of a routine internal dashboard.

### Degraded-Mode Runbooks

AMC must maintain specific degraded-mode runbooks for each critical external dependency:

**AIMC Unavailable / Degraded:**
- AMC enters AI-degraded mode: all AI-assisted features are suspended
- Operator is notified via alert that AIMC is unavailable
- AI-dependent approval surfaces display degraded status, not blank or error
- No direct model calls are attempted as fallback
- Recovery procedure: confirm AIMC restoration, re-run AIMC commissioning check, exit degraded mode with operator acknowledgment

**AIMCC Unavailable / Degraded:**
- AMC enters knowledge-ingestion-degraded mode
- Upload submissions are queued or blocked (not silently failed)
- Ingestion status surfaces display unavailable status
- Operator is notified via alert
- Recovery procedure: confirm AIMCC restoration, flush queued submissions if applicable, re-run AIMCC commissioning check

**Knowledge Upload Centre Failure:**
- Upload submission pathway is suspended
- Operator is notified
- Queued uploads are preserved, not discarded
- Recovery procedure: confirm KUC restoration, resubmit queued uploads, verify ingestion outcomes

**Memory Retrieval Degraded / Stale:**
- Knowledge reference surfaces display explicit staleness or unavailability indicator
- AMC does not silently present stale knowledge as current
- Operator is notified if memory retrieval is significantly impaired
- Recovery procedure: confirm knowledge/memory system restoration, invalidate stale cache, re-query

**Alerting or Approval Pipeline Degradation:**
- If alert generation is impaired, the degradation is itself surfaced as a priority alert via alternative channel
- Approval pipelines must not silently unblock on degradation — failure must be safe (block, not bypass)
- Recovery procedure: restore pipeline, replay queued alerts if applicable, verify approval audit integrity

**Operator-Safe Fallback Mode:**
- In total external-dependency failure, AMC must provide an operator-safe mode in which core executive visibility remains available for AMC-owned state, even when AIMC, AIMCC, and knowledge systems are unavailable
- Human approval pathways must remain open in degraded mode

## §23 — Notification/UX Patterns (§AD-19)

Notification and UX are core operating mechanisms of AMC, not presentation-layer afterthoughts.

AMC exists in part so that Johan Ras can remain in continuous governed contact with the Maturion estate without having to manually interrogate multiple systems, dashboards, repos, or logs to discover what matters. For that reason, AMC shall be designed around proactive executive awareness, clear actionability, and governed decision routing.

### Executive UX Principle
AMC shall provide an executive user experience rather than a developer-console experience.

Its UX must help Johan Ras and, over time, Maturion as resident AI executive:
- understand the current wellbeing of the estate
- detect meaningful change quickly
- distinguish between informational, warning, approval, and emergency states
- move from awareness to governed action without confusion
- preserve authority clarity while reducing operational friction

AMC must not force the primary executive user to behave like a log reader, CI operator, or implementation mechanic merely to remain in control of the estate.

### Proactive Awareness Requirement
AMC shall support proactive notification behavior.

Where context, severity, or evolving risk justifies it, AMC must surface matters before the user explicitly asks. This includes, at minimum:
- emerging issues that may require intervention
- governance-sensitive actions awaiting approval
- maintenance or assurance findings that materially affect estate wellbeing
- execution anomalies, stalls, or failure conditions
- security, compliance, or integrity concerns
- time-sensitive opportunities for decision or intervention

The intended AMC operating model is non-compliant if it only supports passive “ask to know” interaction.

### Two-Way Conversational Interaction
AMC shall support a two-way conversational operating pattern between Johan Ras and Maturion.

This conversational surface must support:
- executive inquiry
- AI-initiated notification
- clarification dialogue
- approval requests
- escalation dialogue
- intervention discussion
- action confirmation
- status follow-up

Conversation in AMC is not merely a convenience feature. It is part of the executive operating model through which understanding, direction, and approval flow between the human constitutional authority and the resident AI executive.

### Notification Classes
AMC notifications shall be structured into clear operating classes so that urgency, consequence, and required action are immediately understandable.

The design shall differentiate at least between:
- **informational notifications** for awareness with no immediate action required
- **warning notifications** for developing issues requiring attention or monitoring
- **approval notifications** for governance-sensitive or reserved-matter decisions
- **operational intervention notifications** where action may be required to protect progress, quality, or wellbeing
- **emergency notifications** for critical conditions requiring urgent executive attention

Additional classes may be introduced later, but the baseline design must prevent ambiguous “all alerts look the same” behavior.

### Approval-Centred UX
AMC shall make approval-requiring matters explicit, explainable, and easy to act on.

Where approval is required, the UX must clearly communicate:
- what is being proposed
- why it is being proposed
- which authority boundary applies
- what consequence follows from approval
- what consequence follows from rejection or delay
- what supporting evidence or context is available

Reserved-matter approvals must never be buried inside generic notifications or disguised as routine task prompts.

### Mobile and Cross-Context Responsiveness
AMC shall be designed for meaningful operation across desktop and mobile contexts.

This requirement exists because AMC is intended to support real executive intervention scenarios, including those in which Johan Ras is away from desk-bound environments, including live client or field situations.

The UX must therefore support:
- concise but meaningful mobile notifications
- rapid drill-down from mobile alerts into governed context
- quick but safe approval/rejection paths
- continuity between mobile and desktop sessions
- context preservation when switching devices or locations

A mobile surface that merely mirrors desktop visuals without supporting real executive action is insufficient.

### Dashboard and Drill-Down Pattern
AMC shall combine overview visibility with governed drill-down capability.

The UX shall provide:
- estate-level wellbeing summaries
- status concentration points for health, execution, governance, maintenance, and assurance
- alert prioritization
- clear transition from high-level signal to root-cause or decision context
- action pathways from insight to approval, escalation, or intervention

Dashboards must not become passive report galleries. They must function as executive situation-awareness tools.

### Escalation and Intervention Pattern
Where escalation is necessary, AMC shall make the escalation path explicit.

Escalation UX must communicate:
- what condition triggered escalation
- which role or subsystem surfaced it
- whether approval is required
- what recommended actions exist
- what timing sensitivity applies
- what operational pathway will be invoked if action is taken

Where intervention is launched, AMC must provide confirmation that the action entered a governed execution path and preserve visibility into its downstream status.

### AI-Mediated UX Discipline
Because AMC includes Maturion and other AI-enabled layers, AI-generated interactions must remain disciplined.

AI-generated UX behavior must:
- align with authority boundaries
- avoid manipulative or ambiguous language
- distinguish clearly between observation, recommendation, request, and decision
- avoid implying approval where approval has not been given
- avoid masking uncertainty where uncertainty exists
- support traceable executive decision-making rather than emotional pressure

AI conversation and notifications must strengthen governed operation, not create ambiguity or false confidence.

### Noise-Control Principle
AMC must minimize noise while preserving early awareness.

Notification design shall aim to:
- reduce low-value interruption
- group related signals where appropriate
- escalate based on significance
- preserve visibility into high-consequence matters
- avoid desensitization through constant undifferentiated alerting

A noisy control centre becomes operationally blind over time. AMC must therefore privilege signal quality, prioritization, and clarity.

### Accessibility of Meaning
AMC’s UX must make the meaning of state visible, not just the presence of data.

Users should be able to understand:
- what is happening
- why it matters
- whether action is needed
- who has authority to act
- what options are available
- what will happen next

The system is not successful if it is technically rich but operationally obscure.

### Prohibited UX Patterns
The following patterns are non-compliant with AMC’s intended operating model:
- crude unmanaged `alert()`-style interaction as a primary notification mechanism
- passive dashboards with no action pathway
- approval flows that obscure authority boundaries
- notification language that hides urgency or consequence
- AI interaction that blurs recommendation and authorization
- mobile experiences that notify but do not support governed action
- fragmented UX that forces the user to reconstruct meaning from multiple disconnected surfaces

### Non-Negotiable Principle
AMC notification and UX design must make governed executive awareness faster, clearer, and safer.

If a proposed UX pattern increases ambiguity, weakens authority clarity, hides approval significance, or forces the executive user back into manual system interrogation, it is non-compliant with the purpose of AMC.

### Alert Class and Priority Framework

Proactive executive alerting is a **first-class product commitment** of AMC. The following alert framework must be preserved and implemented:

**Alert Classes:**
- **Critical**: immediate action required; governance-sensitive or safety-impacting event; routes directly to Johan / Maturion
- **High**: important operational event requiring attention within a defined SLA; may require approval or intervention
- **Medium**: monitoring event requiring awareness; no immediate action but must be acknowledged within SLA
- **Low / Informational**: routine operational event; logged and surfaced but does not require interruption

**Priority Rules:**
- Critical alerts must interrupt the operator even on mobile
- High alerts must be visible on the dashboard and trigger notification
- All alerts must be acknowledged — silent expiry of unacknowledged Critical or High alerts is prohibited

**Escalation:**
- Unacknowledged Critical alerts escalate after defined timeout
- Escalation routing is pre-defined and tested (not improvised at runtime)
- Escalation actions are recorded in the audit trail

**Acknowledgment:**
- Acknowledgment is an explicit operator action (not implicit on view)
- Acknowledgment is recorded with actor and timestamp
- Post-acknowledgment follow-through requirements (e.g., linked approval or intervention) are surfaced

**Retry / Expiry:**
- Alerts that require delivery confirmation have defined retry behavior
- Expired unacknowledged alerts are logged with expiry reason
- Alert expiry does not silently resolve the underlying condition

**Desktop / Mobile Continuity:**
- Alert state is consistent across desktop and mobile — no alert visible on desktop is invisible on mobile
- Approval and acknowledgment actions are executable from both contexts


## §24 — Shared State Architecture (§AD-20)

AMC requires a deliberate shared state architecture because it is intended to function as a continuous executive operating environment rather than a set of disconnected screens.

Shared state in AMC is not just a UI convenience. It is the structural mechanism that allows executive awareness, conversation, approvals, escalations, interventions, and estate-health visibility to remain coherent across views, workflows, devices, and time.

### Purpose of Shared State
The shared state architecture shall exist to ensure that AMC can preserve a consistent executive picture of the estate.

It must support:
- continuity of awareness
- continuity of decision context
- continuity of approval context
- continuity of conversation context
- continuity of intervention context
- continuity across desktop and mobile usage
- continuity across human and AI-mediated operating flows

AMC must not behave like a collection of unrelated pages that each reconstruct their own local truth in isolation.

### Core Shared State Principle
Any state that materially affects executive understanding, authority routing, approval logic, escalation behavior, or operational intervention must be treated as governed shared state.

If fragmentation of state would cause:
- contradictory status presentations
- lost approval context
- broken escalation logic
- duplicate or conflicting interventions
- conversation context loss
- authority ambiguity
- audit discontinuity

then that state must be designed as part of the explicit shared-state model.

### State Domains
AMC shared state shall be organized into clear state domains. At minimum, the architecture must account for the following:

- **executive context state**
- **conversation state**
- **alert and notification state**
- **escalation state**
- **approval state**
- **intervention state**
- **estate wellbeing state**
- **job and execution state**
- **agent status state**
- **sandbox and bounded-environment state**
- **identity and authority state**
- **cross-device continuity state**
- **audit-linked state references**

These domains may be implemented through multiple technical mechanisms, but they must be conceptually coherent and explicitly designed.

### Executive Context State
AMC shall maintain executive context state so that the current high-level operating picture of the estate remains stable and understandable.

Executive context state should include, where relevant:
- current estate posture
- top-priority issues
- current approval queue summary
- active escalations
- operational interventions in flight
- notable maintenance or assurance findings
- active strategic or governance-sensitive matters requiring awareness

This state is what allows Johan Ras and, over time, Maturion to remain oriented without reassembling the estate picture from scratch on each screen.

### Conversation State
Because AMC is intentionally conversational, conversation state is a first-class domain.

Conversation state must support:
- continuity of dialogue with Maturion
- traceable relationship between conversational context and actions
- preservation of meaningful context across navigation
- preservation of relevant context across device changes where appropriate
- distinction between casual conversation, decision preparation, approval request, escalation dialogue, and action-confirmation dialogue

Conversation state must not be treated as disposable if it materially affects executive understanding or later action.

### Alert and Notification State
Alerts and notifications shall have shared state sufficient to preserve coherent awareness.

The state model must support:
- active alerts
- alert class and severity
- notification acknowledgement state
- notification routing state
- suppression, grouping, or prioritization state where applicable
- relationship between notifications and underlying issues or actions

This is required so that the mobile surface, dashboard surface, and conversational surface do not tell conflicting stories about what currently matters.

### Escalation State
Escalation state shall preserve the lifecycle of escalated matters.

Escalation-related state should include:
- escalation trigger
- escalation source
- escalation class
- escalation target authority
- acknowledgement state
- timing sensitivity
- recommended action context
- resolution or closure state

AMC must not allow escalations to become detached from their initiating conditions or their downstream outcomes.

### Approval State
Approval state is a constitutional feature of AMC and must be treated with special rigor.

Approval state must preserve:
- pending approval items
- approval class
- authority boundary
- decision options
- supporting context
- expiry or timing conditions where relevant
- approved, rejected, deferred, or withdrawn status
- downstream execution linkage

Approval state must be shared consistently across dashboard, conversation, notification, and action surfaces so that the system never presents a matter as both pending and resolved at the same time.

### Intervention State
AMC is intended to support governed intervention, including in mobile and live client contexts. Intervention state must therefore be explicit and durable.

Intervention state should include:
- intervention proposal
- intervention authorization status
- intervention initiation state
- intervention in-flight state
- downstream orchestration linkage
- completion, rollback, or failure state
- related alerts, approvals, and audit references

This ensures that intervention is treated as a governed estate action rather than an isolated UI event.

### Estate Wellbeing State
AMC shall maintain estate wellbeing state as a synthesized operating picture rather than a raw metric dump.

Wellbeing state should combine signals from:
- execution health
- governance health
- maintenance health
- assurance health
- security posture
- compliance posture
- agent ecosystem health
- app/environment health
- trend or anomaly indicators where relevant

This state should support both executive overview and drill-down without losing coherence.

### Job and Execution State
Where AMC launches, supervises, or observes jobs, fixes, maintenance runs, or other estate activity, the corresponding execution state must be shared.

Execution state should include:
- job identity
- initiating source
- current phase
- orchestrating actor
- blocking conditions
- notable anomalies
- completion or failure state
- relationship to approvals, interventions, and audit trails

This is especially important for the intended scenario in which a governed fix may be discussed, approved, launched, and then monitored through AMC.

### Agent Status State
AMC must maintain shared awareness of relevant agent roles and their current posture where needed.

Agent status state may include:
- active or inactive status
- role classification
- health or availability indicators
- last meaningful report or signal
- exception state
- sandbox or domain assignment
- reporting relationship

This supports a living picture of the operational ecosystem without collapsing specialist identities into a single opaque runtime mass.

### Sandbox and Bounded-Environment State
Where AMC supervises sandboxed AI teams or bounded app-specific environments, shared state must preserve those boundaries.

Sandbox-related state should include:
- sandbox identity
- parent application or domain
- scope boundary
- participating specialist roles
- current activity state
- escalation or approval conditions
- cross-boundary proposal state where relevant

State architecture must prevent accidental leakage of sandbox-local meaning into estate-wide meaning without explicit routing.

### Identity and Authority State
Identity and authority state must be shared where necessary to preserve correct action routing and visibility.

This includes:
- current authenticated user identity
- acting AI or agent identity where relevant
- current authority level
- delegated-domain status where applicable
- reserved-matter classification state
- action eligibility state

AMC must not rely on hidden assumptions about “who is acting” or “what authority applies” at the moment of decision.

### Cross-Device Continuity State
AMC is intended for meaningful mobile and desktop use. State architecture must therefore support continuity across devices and sessions where appropriate.

Cross-device continuity should preserve, subject to security and privacy rules:
- current executive context
- relevant conversation continuity
- outstanding alerts and approvals
- active interventions
- recent navigation or working context where useful
- acknowledgement and attention state where appropriate

A user who moves from mobile to desktop should not feel that they are entering a different operational universe.

### Audit-Linked State References
Shared state and audit design must be aligned.

Where shared state leads to consequential action, the architecture should preserve references or linkage to relevant audit records so that stateful operation and later review remain connected.

Examples include linkage between:
- approval state and approval audit records
- intervention state and intervention audit records
- escalation state and escalation audit records
- AI-mediated decision support state and action audit records

Shared state must support reviewability, not undermine it.

### State Freshness and Consistency
AMC’s shared state architecture must define how freshness, synchronization, and consistency are handled.

The design must address:
- when state is authoritative
- how stale views are detected
- how conflicting updates are resolved
- how pending vs final states are represented
- how multi-surface consistency is preserved
- how real-time signals interact with durable state

Because AMC is an executive control surface, stale or contradictory state is not a cosmetic bug. It is a governance and decision-quality defect.

### State Ownership and Source of Truth
Each shared state domain must have a clear source-of-truth model.

The architecture must define, for each important domain:
- which subsystem owns the authoritative record
- which surfaces may present it
- which surfaces may update it
- what events change it
- what audit consequences attach to those changes

This prevents accidental duplication of authority and helps preserve operational coherence.

### Downstream Design Requirement
Downstream FRS, TRS, and architecture work must treat shared state as a first-class design concern.

That work must explicitly define:
- state domains
- state transitions
- state ownership
- synchronization model
- persistence boundaries
- authority implications
- audit linkages
- cross-device behavior
- sandbox boundary behavior

Shared state may not be left to emerge ad hoc from frontend implementation convenience.

### Non-Negotiable Principle
AMC shared state architecture must preserve one coherent governed picture of the estate across people, AI roles, devices, workflows, and time.

Any design that allows executive context, approvals, alerts, conversations, or interventions to fragment into contradictory local truths is non-compliant with the intended purpose of AMC.

### State Ownership Separation

AMC must maintain explicit separation between the following state ownership classes:

**Local UI state:**
- transient presentation state held in the browser/app client
- not persisted beyond the current session
- must not be treated as authoritative operational state

**AMC-owned persistent operational state:**
- alert records
- approval records
- intervention records
- audit events generated by AMC
- operator session state where persisted
- AMC configuration and operational settings
- This state is persisted in AMC's own storage and is the canonical source for these records

**AIMCC / knowledge-memory-owned persistent state:**
- ingested knowledge records
- memory operations and memory store contents
- upload records and ingestion outcomes
- knowledge organization and taxonomy
- This state is owned by AIMCC and the knowledge / memory system. AMC may cache or present it for display purposes but must not become the silent canonical owner

**Non-ownership rule:**
AMC may cache or present AIMCC-owned or knowledge/memory-owned state for executive visibility, but it must:
- clearly source that state from the canonical owner
- not allow its cached copy to diverge from the canonical owner's state in ways that affect operational truth
- handle cache invalidation explicitly
- not write back to AIMCC-owned state through AMC's own persistence layer

Any design where it becomes unclear whether state is AMC-owned or AIMCC/knowledge-system-owned is a governance defect.


## §25 — API Authentication (§AD-21)

All AMC APIs, orchestration actions, service entry points, and machine-callable operational pathways must enforce authentication and authorization consistent with AMC’s authority model.

API authentication in AMC is not a narrow technical access-control concern. It is one of the primary mechanisms through which constitutional authority, executive delegation, orchestration scope, sandbox boundaries, and approval gates are made real in system behavior.

### Purpose of API Authentication
The AMC API authentication model shall exist to ensure that every action entering the system can be:
- attributed
- authenticated
- authorized
- classified by authority domain
- constrained by role and scope
- traced into audit and operational state

AMC must not allow important actions to enter the estate through poorly defined, weakly attributed, or authority-ambiguous endpoints.

### Core Principle
Authentication alone is insufficient.

AMC must enforce a combined model of:
- **identity authentication**
- **role and authority evaluation**
- **scope and boundary validation**
- **approval-state verification where required**
- **audit-linked action attribution**

An authenticated actor must still be prevented from performing actions outside their approved authority, role, environment, or delegation boundary.

### Identity Classes
AMC must support authenticated identity classes appropriate to its multi-layer operating model.

At minimum, the API design must account for:
- **human executive identity** for Johan Ras
- **future approved human identities** if introduced
- **Maturion executive AI identity**
- **Foreman orchestration identity**
- **IAA identity** or equivalent assurance-role identity where machine pathways are used
- **maintenance agent identities**
- **specialist-agent identities**
- **sandbox-bound agent identities**
- **service or system identities** for governed internal infrastructure pathways

These identities must not be flattened into a single generic service principal model if doing so would destroy authority clarity.

### Authentication Requirements by Identity Class
Each identity class must authenticate through a method appropriate to its risk and authority profile.

The design shall ensure that:
- human executive actions are strongly authenticated
- privileged AI or agent actions are cryptographically attributable to governed identities
- sandbox agents cannot impersonate estate-level agents
- maintenance, assurance, and specialist identities remain distinguishable
- machine-to-machine actions are still attributable to a governed role, not to an anonymous backend blur

The final mechanisms will be detailed downstream, but the Stage 1 requirement is that identity distinction is mandatory.

### Authorization and Authority Evaluation
Authorization in AMC must evaluate more than just role labels.

For any consequential action, the API layer must be able to determine:
- who or what is attempting the action
- what role they hold
- what authority domain applies
- whether the action is within routine delegated scope
- whether the action is sandbox-bound
- whether approval is required
- whether approval exists
- whether escalation is required instead of execution

An API pathway that only checks “logged in yes/no” or “token valid yes/no” is insufficient for AMC.

### Reserved-Matter Protection
Actions that touch reserved matters must be explicitly protected at the API layer.

Where an action would affect:
- governance
- agent files
- constitutional boundaries
- major app-description or scope changes
- major design changes
- authority transfer or delegation structure
- other explicitly reserved domains

the API layer must reject direct execution unless the correct approval condition is satisfied through the proper authority pathway.

Reserved-matter protection must not depend solely on frontend restraint or user-interface courtesy.

### Approval-Bound Action Enforcement
For approval-gated actions, the API layer must verify approval state before execution.

This includes confirming:
- whether approval is required
- which authority must approve
- whether valid approval was granted
- whether the approval still applies to the exact requested action and scope
- whether timing, revision, or context has invalidated the approval

This prevents approval drift, stale approval reuse, and silent execution based on outdated decision context.

### Executive AI and Agent Action Authentication
Maturion and other agents may initiate, recommend, route, or in approved cases execute certain actions, but those actions must remain attributable and bounded.

The API layer must ensure that AI and agent identities:
- authenticate as their own governed identities
- do not inherit human authority by implication
- do not silently exceed delegated scope
- are distinguishable from one another in audit and enforcement
- are constrained by their approved operational domain

Maturion may hold executive AI status, but executive AI status is not equivalent to unconstrained system privilege.

### Foreman and Orchestration Pathway Protection
Foreman-related orchestration actions must be authenticated and authorized as orchestration actions, not confused with human executive actions or independent assurance actions.

The API layer must preserve the distinction between:
- a human executive approval
- an executive AI recommendation or coordination step
- an orchestration command
- a builder-side execution action
- an assurance event
- a maintenance action

This separation is necessary to keep the authority chain enforceable in real system behavior.

### Sandbox and Bounded-Environment Authentication
Where sandboxed AI teams or bounded app environments exist, API authentication must preserve boundary integrity.

Sandbox-bound pathways must ensure:
- sandbox identities are limited to their own environment and scope
- cross-sandbox or sandbox-to-estate actions are blocked or escalated unless explicitly authorized
- tenant or environment boundaries are enforced
- specialist agents cannot silently operate as estate-level actors

Authentication and authorization must make sandbox containment technically real, not merely conceptually documented.

### Service-to-Service Authentication
AMC will likely require internal service-to-service pathways between UI surfaces, orchestration layers, audit services, notification services, and AI routing layers.

Such pathways must:
- use governed service identities
- avoid shared anonymous backend trust
- preserve action attribution where possible
- respect least privilege
- support audit linkage for consequential activity

A hidden internal service path must not become a loophole through which governance-sensitive behavior bypasses normal controls.

### Session and Continuity Considerations
Because AMC is designed for both mobile and desktop executive use, session handling must support continuity without weakening authority protection.

The downstream design must consider:
- secure session continuity across devices where appropriate
- re-authentication or step-up authentication for sensitive actions
- handling of interrupted approval or intervention flows
- separation between read-oriented awareness access and write-capable privileged action flows
- safe restoration of working context without silent privilege carryover

Convenience must not silently override constitutional or operational protection.

### Authentication Failure and Escalation Behavior
AMC API design must define what happens when authentication or authorization fails.

The system should distinguish between:
- identity failure
- insufficient authority
- missing approval
- expired approval
- sandbox-boundary violation
- policy restriction
- escalation-required conditions

These outcomes should be surfaced in ways that preserve clarity for users and agents while avoiding accidental information leakage.

### Audit Coupling Requirement
API authentication and authorization outcomes must be coupled to AMC’s audit model.

For consequential API actions, the system should preserve auditability of:
- authenticated identity
- evaluated role
- authority classification
- approval state check
- execution or rejection result
- timing and context
- downstream effects where relevant

Authentication decisions that materially affect system behavior must not disappear into opaque infrastructure logs only.

### Downstream Design Requirement
Downstream FRS, TRS, and architecture work must explicitly define:
- identity classes
- authentication mechanisms
- authorization logic
- authority-domain mapping
- reserved-matter enforcement patterns
- approval-verification patterns
- sandbox-boundary enforcement
- service-to-service identity design
- audit linkages for API decisions

API authentication may not be deferred to generic framework defaults without review against AMC’s authority and governance model.

### Non-Negotiable Principle
AMC API authentication must make authority real at the action boundary.

Any design that allows consequential action to enter the estate without clear identity, clear authority evaluation, correct approval enforcement, and trustworthy attribution is non-compliant with the intended purpose of AMC.

### Trust Boundary Definitions

AMC must define explicit trust boundaries for all API interactions:

| Boundary | Trust Model | Requirements |
|---|---|---|
| **Human user → AMC** | User JWT via Supabase Auth | Session validation on every request; authority-level checked per action |
| **AMC internal services** | Service-to-service token | Not user-impersonating; scoped to AMC internal operations |
| **AMC → AIMC** | AIMC gateway credentials | AMC authenticates to AIMC as a service caller; does not pass raw user JWT to AI models |
| **AMC → AIMCC / knowledge services** | AIMCC service credentials | AMC authenticates to AIMCC as a service caller; scoped to the specific operations AMC is permitted |
| **Privileged executive actions** | Elevated approval authority | Actions that require approval-level authority must validate approval authority independently of session presence; session presence alone is not sufficient |

**Non-impersonation rule:** AMC must not impersonate a user to downstream services (AIMC, AIMCC). AMC calls these services as a service principal, with its own identity, and routes user context through metadata where required.


## §26 — Audit Log Design (§AD-22)

AMC must maintain a structured, trustworthy audit model because it is intended to become the executive operating surface through which progressively autonomous activity is supervised, approved, challenged, and reviewed.

Audit logging in AMC is not a secondary technical concern. It is part of the constitutional integrity of the application. Without strong audit design, AMC cannot safely support executive delegation, AI-mediated action, reserved-matter approvals, or estate-wide intervention.

### Audit Design Purpose
The AMC audit model shall exist to ensure that significant activity across the estate can be:
- reconstructed
- explained
- attributed
- reviewed
- challenged
- escalated
- used as evidence for assurance, governance, maintenance, and operational learning

The audit model must allow Johan Ras, Maturion, assurance agents, and other approved reviewers to determine not just that something happened, but:
- what happened
- why it happened
- who or what initiated it
- under what authority it occurred
- what approvals were involved
- what downstream consequences followed

### Core Audit Principle
Every governance-relevant, authority-relevant, operationally significant, or AI-mediated consequential action within AMC shall produce an audit trail sufficient to support later review.

AMC shall not rely on informal memory, ephemeral chat context, or scattered subsystem logs as a substitute for a formal executive audit model.

### Audit Event Classes
AMC audit design shall cover, at minimum, the following event classes:

- **approval events**
- **intervention events**
- **agent action events**
- **governance-sensitive events**
- **maintenance events**
- **assurance events**
- **build/job initiation events**
- **build/job completion events**
- **notification dispatch events**
- **escalation events**
- **authentication and authorization events**
- **state-changing executive decisions**
- **sandbox-bound significant actions**
- **authority-delegation or authority-boundary events**
- **failure, rejection, rollback, or cancellation events**

Additional event classes may be added later, but these are the minimum baseline for AMC compliance.

### Approval Audit Requirement
All approval-requiring activity must be auditable in a way that clearly distinguishes:
- proposal
- review context
- approving or rejecting authority
- decision outcome
- timestamp
- affected scope
- resulting execution path

Reserved-matter approvals must be especially explicit. The audit log must make it impossible to confuse:
- recommendation with approval
- approval request with approval granted
- delegated operational permission with constitutional reserved-matter approval

### AI-Mediated Action Audit Requirement
Where AI participates in a meaningful way, the audit model must capture the AI role involved.

For AI-mediated significant events, audit records shall identify:
- which AI role participated, such as Maturion, Foreman-side orchestration intelligence, maintenance AI, assurance AI, or specialist AI
- whether the AI observed, recommended, prepared, routed, or executed an action
- whether human approval was required
- whether human approval was obtained
- what downstream consequence resulted

AMC must not allow important AI-mediated activity to disappear into opaque conversational flow.

### Authority Attribution Requirement
Every significant audit record must preserve authority attribution.

The audit model shall support explicit identification of:
- the initiating actor
- the acting actor
- the approving actor, where different
- the relevant authority domain
- whether the action was routine, delegated, approval-gated, or reserved-matter-bound
- whether escalation occurred

This is especially important in AMC because multiple layers of agency exist simultaneously:
- human constitutional authority
- executive AI
- orchestration authority
- assurance authority
- maintenance authority
- specialist-agent authority
- builder activity

### Conversation-to-Action Traceability
Where conversation leads to approval, intervention, or execution, AMC must preserve traceability between discussion and action.

This does not require storing every conversational token forever in all contexts, but it does require that materially relevant decision context be traceable. For significant actions, the system should preserve or reference:
- the decision conversation or instruction source
- the action that followed
- the approval or confirmation state
- the execution or escalation outcome

AMC’s conversational operating model is not trustworthy if actions cannot later be related back to meaningful decision context.

### Notification and Escalation Audit
Notifications and escalations that materially affect decision-making or operational response must also be auditable.

Audit design shall record, where relevant:
- what notification or escalation was issued
- to whom it was directed
- what class of notification it was
- whether it was acknowledged
- whether it resulted in action, delay, or non-response
- whether follow-up escalation occurred

This ensures that proactive executive awareness is reviewable rather than ephemeral.

### Sandbox and Specialist Audit Boundaries
Where AMC supervises sandboxed AI teams or specialist-agent work, audit design must preserve boundary clarity.

Audit records for sandbox or specialist activity must make clear:
- which sandbox, tenant, or bounded environment was involved
- which specialist role acted
- what scope the action was limited to
- whether any proposed change crossed out of sandbox scope
- what escalation or approval path applied if boundary crossing was attempted

Sandboxing without boundary-aware audit is non-compliant with AMC’s intended design.

### Immutable and Append-Oriented Audit Expectations
For consequential events, AMC audit design should favor append-oriented, tamper-resistant logging patterns wherever feasible.

The system must not make it easy to silently rewrite:
- who approved something
- whether approval existed
- what action occurred
- what assurance verdict was issued
- what escalation or rejection happened

Where correction or clarification is needed, the preferred model is an additive corrective record rather than silent mutation of history.

### Audit Review Utility
AMC’s audit model must support practical review use, not just raw data capture.

Audit design should make it possible to:
- review activity by actor
- review activity by app or sandbox
- review activity by authority domain
- review activity by event class
- reconstruct timelines
- inspect approval chains
- inspect AI-mediated action histories
- support assurance review and governance challenge
- support maintenance analysis and operational learning

If audit data is technically present but practically unusable, the design is insufficient.

### Privacy, Sensitivity, and Access Control
Audit visibility must itself be governed.

AMC audit design shall define:
- who may see which audit classes
- which audit records are executive-only
- which records are available to assurance or maintenance agents
- how sensitive context is protected
- how sandbox or tenant boundaries affect audit visibility
- how audit access itself is logged where appropriate

A strong audit model does not mean indiscriminate exposure of all history to all actors.

### Non-Repudiation and Trustworthiness
The audit model should make later denial of significant actions difficult where governance, approval, or operational safety depends on reliable attribution.

For major events, AMC should preserve enough integrity signals to support confidence in:
- who acted
- under what approval
- through what governed pathway
- with what result

This is essential if AMC is to support progressive delegation without losing trust.

### Audit Design Consequence for Downstream Architecture
Downstream FRS, TRS, architecture, and implementation work must treat audit as a first-class system concern.

This means:
- audit requirements must be traced explicitly
- state changes must be designed with audit consequences in mind
- AI interactions must be classifiable for audit purposes
- approval flows must generate formal records
- intervention workflows must preserve traceability
- notification and escalation systems must integrate with the audit model

Audit cannot be added late as a decorative compliance layer.

### Non-Negotiable Principle
AMC audit design must make significant action across the estate attributable, reviewable, and governable.

Any design that allows consequential action, AI-mediated intervention, approval-sensitive change, or authority transfer to occur without a trustworthy audit trail is non-compliant with the intended purpose of AMC.

### Cross-System Provenance Requirements

Every audit event in AMC must include the following fields as a minimum:

| Field | Definition |
|---|---|
| **actor** | The human or agent who initiated the action |
| **source_system** | The system where the action originated (AMC, AIMC, AIMCC, etc.) |
| **approval_basis** | The approval or authorization basis for the action (where applicable) |
| **timestamp** | ISO 8601 UTC timestamp |
| **object** | The entity or record affected by the action |
| **action** | The specific action type |
| **state_transition** | The before/after state of the affected object (where applicable) |
| **outcome** | Success, failure, partial, or pending |

### Required Audit Event Coverage

AMC must generate audit events for all of the following:
- alert generation, acknowledgment, escalation, expiry
- approval granted, approval rejected, approval escalated
- intervention initiated, intervention completed, intervention cancelled
- AIMC-routed AI action (request, response, error)
- upload submitted via Knowledge Upload Centre
- ingestion outcome received from AIMCC
- memory / knowledge reference retrieved and presented in a decision-support context
- auth events (login, session expiry, unauthorized access attempt)
- degraded-mode entry and exit for each external dependency
- any executive action that changes persisted state

### Cross-System Event Integrity
Where an audit event spans multiple systems (e.g., AMC initiates an action that AIMC executes), the audit record must contain sufficient provenance to link the AMC-originating event with the downstream execution event. The audit trail must not lose the chain of custody at system boundaries.


## §27 — Tracker Update Requirement (§AD-23)

AMC shall maintain truthful, current, and governance-aligned trackers so that document status, stage status, approval status, and actual delivery reality remain synchronized.

This section exists because AMC is intended to become the executive operating centre of the Maturion estate. A system that aspires to supervise estate wellbeing, executive awareness, and governed progression cannot itself be built on stale, misleading, or cosmetically updated stage records. Tracker discipline is therefore not clerical overhead. It is part of the integrity model of the application.

For AMC, tracker truthfulness is a governance requirement.

### Purpose of the Tracker Update Requirement
The tracker update requirement shall exist to ensure that everyone operating on AMC can determine, from artifacts rather than assumption:
- what stage AMC is actually in
- which artifacts exist
- which artifacts remain pending
- what has been approved
- what is draft only
- what has changed materially
- what is blocked
- what is ready to progress
- what still requires clarification or decision

Trackers must preserve operational truth about the document and build lifecycle, not merely offer a comforting impression of progress.

### Core Principle
Tracker artifacts must reflect substantive reality, not optimistic narrative.

No AMC tracker may imply that:
- a stage is complete when it is still materially unresolved
- an artifact is authoritative when it is still placeholder-only
- an approval exists when only discussion exists
- downstream readiness exists when upstream truth is still unstable
- an issue is resolved when it has merely become less visible

For AMC, misleading tracker state is not a minor administrative flaw. It is a governance defect because it distorts executive and delivery awareness.

### Scope of Tracker Coverage
The tracker update requirement applies to all artifacts and records that communicate lifecycle or readiness truth for AMC.

This includes, at minimum:
- stage trackers
- artifact indexes
- app-description status records
- approval records
- stage gate records
- readiness checklists
- pending-item or blocker records
- linked governance notes where they materially affect status
- downstream artifact progress records once those stages begin

If a record materially influences whether AMC appears ready, blocked, complete, pending, approved, or authoritative, it falls within this requirement.

### Stage Truthfulness Requirement
Trackers must accurately represent stage state.

For AMC, this means trackers must clearly distinguish between:
- not started
- placeholder only
- draft in progress
- materially filled but not approved
- under review
- approved
- blocked
- superseded
- legacy / lineage only

A tracker that compresses these different states into a vague “done” or “in progress” label is insufficient for AMC’s needs.

### Artifact Truthfulness Requirement
Trackers must accurately represent artifact status and role.

For each major AMC artifact, tracker logic should make clear:
- whether the artifact exists
- whether it is placeholder-only or materially developed
- whether it is authoritative or supporting
- whether it is draft, reviewed, approved, or superseded
- what lifecycle stage it belongs to
- whether downstream artifacts may rely on it yet

This is especially important for AMC because Stage 1 has included placeholder artifacts, migrated lineage, and pending canonical-source decisions that must not be collapsed into one misleading status.

### Approval-State Truthfulness Requirement
Trackers must not imply approval where approval has not actually been granted.

This includes clear differentiation between:
- discussed
- drafted
- internally aligned in conversation
- awaiting review
- reviewed with comments
- approved
- approved with conditions
- rejected
- superseded by later approval

For AMC, this matters because approval significance is part of the product’s operating model. Its own delivery chain must therefore model approval truth correctly.

### Blocker and Dependency Visibility Requirement
Trackers must preserve visibility into blockers, dependencies, and unresolved questions.

This includes visibility into:
- unresolved authority questions
- unresolved canonical-location decisions
- unresolved scope contradictions
- unresolved Stage 1 sections
- missing companion artifacts
- pending governance decisions
- dependencies that prevent safe downstream progression

A tracker that hides blockers behind generic progress percentages or cosmetic stage labels is non-compliant.

### Change-Significance Requirement
Tracker updates must reflect material change, not just document touch activity.

For AMC, a tracker update should be triggered not only by file creation, but by meaningful progression such as:
- a placeholder section becoming materially filled
- a strategic section being hardened
- a new blocking issue being identified
- an approval record being created or updated
- an artifact becoming authoritative
- a previously unresolved contradiction being formally settled
- a stage gate moving from unsatisfied to satisfied

This prevents “edited recently” from being mistaken for “meaningfully progressed.”

### Governance Coupling Requirement
Tracker state must remain coupled to governance state.

For AMC, trackers should make it possible to determine:
- whether Stage 1 is truly pre-build ready
- whether downstream work is permitted yet
- whether required approvals are still pending
- whether a document is safe to derive from
- whether a stage claim is supported by evidence
- whether any material governance condition remains unmet

Trackers are therefore part of the governance-control surface for the build, not merely project-management convenience.

### Lifecycle Coupling Requirement
Trackers must remain consistent with the lifecycle and derivation chain.

This means tracker records must not allow:
- Stage 2 artifacts to appear fully valid if Stage 1 is still unstable
- Architecture to appear authoritative if TRS is not ready
- implementation progress to imply product readiness where verification is incomplete
- deployment readiness to appear real where runbook or approval conditions remain unresolved

AMC’s tracker system must reinforce lifecycle discipline rather than erode it.

### Minimum Update Events
At minimum, AMC trackers shall be updated when any of the following occurs:

- a new major artifact is created
- an artifact changes from placeholder to materially developed
- an artifact changes authority status
- a stage gate status changes
- a blocking issue is opened, resolved, or reclassified
- a major section affecting downstream derivation is materially revised
- an approval is granted, denied, withdrawn, or superseded
- a canonical-source decision is made or reversed
- downstream progression becomes allowed or blocked
- a legacy artifact is reclassified as lineage-only or superseded

Failure to update trackers after such events is a process defect.

### Ownership and Discipline Requirement
Tracker maintenance must be treated as owned work, not leftover work.

For each tracker or index relevant to AMC, it should be possible to determine:
- who is responsible for updating it
- what events should trigger updates
- what other artifacts it depends on
- what claims it is allowed to make
- how stale state is recognized and corrected

An unowned tracker will inevitably drift into unreliability.

### Evidence-Based Status Requirement
Tracker claims must be defensible through artifact evidence.

For example:
- a section marked hardened should correspond to materially hardened text
- a stage marked ready should correspond to completed prerequisite artifacts
- an approval-marked artifact should have an approval record
- a blocker-cleared status should correspond to a recorded resolution

AMC trackers must not become symbolic confidence markers detached from evidence.

### Minimum Tracker Checklist
The following minimum conditions must hold for tracker compliance:

- [ ] Major AMC artifacts have visible status
- [ ] Stage status distinguishes placeholder, draft, review, approved, blocked, and superseded states
- [ ] Tracker status reflects real artifact authority, not just file existence
- [ ] Approval state is represented truthfully
- [ ] Blockers and dependencies are visible
- [ ] Material progress updates trigger tracker updates
- [ ] Lifecycle and derivation dependencies are reflected accurately
- [ ] Tracker claims are evidence-defensible
- [ ] Canonical-source ambiguity is visible where unresolved
- [ ] Legacy or lineage artifacts are not misrepresented as current authority

### Downstream Design Consequence
As AMC progresses into later stages, tracker discipline must continue.

Downstream FRS, TRS, Architecture, build-planning, verification, and operational artifacts must be reflected in trackers in a way that preserves:
- lifecycle truth
- approval truth
- readiness truth
- blocker truth
- artifact-authority truth

A sophisticated product built on unreliable trackers is structurally misaligned with AMC’s purpose.

### Non-Negotiable Principle
AMC tracker updates must keep stage truth, artifact truth, approval truth, and readiness truth synchronized with reality.

Any approach that allows stale, optimistic, or materially misleading tracker state to shape executive or delivery decisions is non-compliant with the intended purpose of AMC.

### Stage 1 Authority Migration and Repo Cleanup

As part of the Stage 1 authority transition (from FM-era fragments to this consolidated App Description as the single authoritative source), the following tracker and repo cleanup actions must be executed in the same wave as CS2 approval:

**Source-of-truth stabilization:**
- Upon CS2 approval of this document, `modules/amc/00-app-description/app-description.md` becomes the single authoritative AMC Stage 1 source
- All transitional FM-era Stage 1 files in this directory must be deprecated or archived. The files to be treated are:
  - `AMC_Stage 1_outline.md`
  - `AMC_ROLE_AUTHORITY_AND_OPERATING_MODEL.md`
  - `amc-role-authority-and-operating-model.md`
  - `amc_stage1_filled_skeleton.md`
  - `amc_stage1_hardened_sections.md`
  - `amc_stage1_hardened_section5.md` through `amc_stage1_hardened_section28.md` (all individual hardened section files)
- Deprecation options (choose one per file, document choice in wave record):
  - **Deprecate in place**: add the following header to the top of the file and leave it in the directory: `> ⚠️ DEPRECATED — This file was a transitional draft. The single authoritative AMC Stage 1 source is now \`modules/amc/00-app-description/app-description.md\` (approved by CS2 on [DATE]). This file must not be used for downstream derivation.`
  - **Archive**: move to `modules/amc/00-app-description/archive/` and add the same deprecation header
  - Files must NOT be silently deleted without a trace in the wave record

**Downstream derivation protection:**
- A repo note or README must be placed in `modules/amc/00-app-description/` clarifying which file is the canonical source after approval
- Any consolidation scaffolding files used during Stage 1 drafting may be cleaned up after approval, but cleanup must be recorded in the wave record

**Tracker updates required:**
- The AMC stage tracker must be updated to reflect Stage 1 as in-approval or approved (as appropriate)
- Any issue or project tracker entries referencing FM-era Stage 1 fragments as authoritative must be updated to point to the canonical source
- The Stage 1 authority migration must be logged in the wave record of the approval wave

**Note**: This cleanup is out of scope for this amendment wave. It is documented here so that the cleanup obligation is explicit and cannot be silently deferred after approval.


## §28 — State Persistence Specification (§AD-24)

AMC shall define an explicit state-persistence model so that executive awareness, approvals, conversations, interventions, and estate-operating continuity do not depend on fragile session memory or ephemeral UI state.

This section exists because AMC is intended to become the executive operating centre of the Maturion estate. Such an application cannot rely on short-lived in-memory state alone. It must preserve the right forms of continuity across time, devices, interruptions, and governed workflows, while also respecting authority boundaries, audit requirements, privacy, and sandbox separation.

For AMC, persistence is not merely a convenience feature. It is part of the continuity, accountability, and executive-operability model of the product.

### Purpose of the State Persistence Model
The AMC state-persistence model shall exist to ensure that materially important state survives in a controlled and intelligible way.

The persistence model must support:
- continuity of executive awareness
- continuity of approval and escalation context
- continuity of conversations where materially relevant
- continuity of interventions and operational follow-through
- continuity across desktop and mobile contexts where appropriate
- restoration after interruption, reconnect, or device change
- preservation of auditable state transitions where required

If AMC cannot preserve the right forms of state across time, it cannot reliably function as an executive operating environment.

### Core Principle
Only the right state should persist, and persisted state must remain governed.

AMC must avoid both extremes:
- losing materially important state too easily, and
- persisting excessive or uncontrolled state without purpose, boundary, or retention logic

Persistence design must therefore be intentional, domain-specific, and governed by product meaning rather than technical convenience alone.

### Persistent State Domains
AMC shall define persistence expectations for all materially important state domains.

At minimum, the persistence model must account for:
- **user preference state**
- **executive context state**
- **conversation continuity state**
- **alert and notification history**
- **approval history and approval context**
- **escalation history and escalation context**
- **intervention history and operational follow-through state**
- **audit-linked state references**
- **device and session continuity state**
- **sandbox and bounded-environment state**
- **agent and environment metadata state**
- **operational restoration state**

These domains may differ in retention horizon, visibility, sensitivity, and storage pattern, but they must be explicitly recognized.

### User Preference State
AMC shall persist user preference state where needed to support continuity of executive operation.

This may include:
- preferred views
- notification preferences
- dashboard configuration preferences
- device or interface preferences
- attention-routing preferences where appropriate

User preference persistence must support continuity without becoming a hidden source of authority or workflow behavior that bypasses governance.

### Executive Context State
AMC shall persist enough executive context state to preserve meaningful continuity of estate awareness.

This may include:
- recent estate posture summaries
- currently active high-priority matters
- relevant working context for ongoing executive review
- recently surfaced approval or escalation queues
- recently active intervention context

The purpose of persisting executive context is to reduce reorientation cost without manufacturing false continuity where the underlying estate state has materially changed.

### Conversation Continuity State
Because AMC includes a conversational operating model with Maturion, conversation continuity state is a first-class persistence concern.

Persistence design must define:
- what conversational context should persist
- when it should persist
- how long it should persist
- which parts are materially important for future action or review
- how conversation links to approvals, interventions, or audit trails where relevant

AMC does not need to treat every conversational exchange as equally durable, but it must preserve enough continuity to support executive operating coherence and action traceability where materially significant.

### Alert and Notification History
AMC shall persist alert and notification history sufficiently to support review, continuity, and operational accountability.

This should include, where relevant:
- notification issuance
- alert class and severity
- acknowledgement state
- dismissal or resolution state
- linkage to underlying matter or issue
- follow-up escalation state where applicable

Notification history is important because AMC is designed around proactive awareness. Without durable record of what was surfaced and when, that model becomes operationally weak.

### Approval History and Approval Context
Approval history must be durably persisted.

Persistence design must preserve, at minimum:
- what was proposed
- what required approval
- which authority approved, rejected, deferred, or withdrew
- when the decision occurred
- what scope the decision applied to
- what downstream action followed
- whether later revision invalidated earlier approval

Approval persistence is a constitutional requirement for AMC, not merely a workflow convenience.

### Escalation History and Escalation Context
Escalation state shall be durably persisted where it materially affects decision-making, intervention, or audit.

Persistence should preserve:
- escalation source
- escalation reason
- escalation class
- timing significance
- acknowledgement or non-response state
- resulting action or resolution outcome

Escalation persistence is necessary to support both accountability and learning across repeated operational patterns.

### Intervention History and Operational Follow-Through
AMC is intended to support governed intervention, including in mobile and live client contexts. Intervention-related state must therefore persist sufficiently to preserve continuity from proposal to closure.

Persistence should support:
- intervention proposal
- approval linkage
- initiation timestamp and actor
- orchestration linkage
- in-flight status
- completion, rollback, or failure state
- associated evidence or audit references where relevant

A system that loses intervention continuity after initiation is non-compliant with AMC’s executive-operating purpose.

### Audit-Linked State References
Where persisted state relates to consequential actions, the model should preserve linkage to audit records or auditable identifiers.

This includes, where applicable:
- approval state linking to approval audit records
- intervention state linking to intervention audit records
- escalation state linking to escalation audit records
- AI-mediated action context linking to consequential action records

Persistence and audit must reinforce one another rather than drift apart into disconnected systems of truth.

### Device and Session Continuity State
AMC shall support cross-device and cross-session continuity where appropriate, subject to security and authority controls.

Persistence may support:
- restoration of relevant working context
- continuity of conversation state
- preservation of outstanding approvals and alerts
- continuity of active intervention review
- restoration of last meaningful executive workspace state where helpful

However, continuity persistence must not silently restore unsafe privilege or bypass step-up controls required for sensitive actions.

### Sandbox and Bounded-Environment State
Where AMC supervises sandboxed AI teams or bounded specialist environments, persistence must preserve those boundaries.

Sandbox persistence design must ensure:
- sandbox identity is durable
- boundary context is preserved
- specialist activity context remains scoped
- cross-boundary proposals are distinguishable from intra-boundary activity
- sandbox-local state does not silently become estate-global state

Boundary-respecting persistence is necessary if sandbox governance is to remain real over time.

### Agent and Environment Metadata State
AMC should persist appropriate metadata about relevant agents and environments where continuity of supervision depends on it.

This may include:
- role classification
- environment assignment
- bounded scope
- recent status signals
- known exception or degraded state
- relevant operational posture markers

Such persistence supports executive awareness without requiring the estate to be rediscovered from zero on every session.

### Retention and Sensitivity Rules
Different persistent state domains require different retention logic, visibility rules, and sensitivity handling.

Persistence design must therefore define, downstream:
- which state is short-lived
- which state is long-lived
- which state is executive-only
- which state is visible to assurance or maintenance actors
- which state is sandbox-restricted
- which state must be archived, rotated, or minimized

AMC must not default to “persist everything forever” or “drop everything quickly” without regard to meaning, governance, or operational need.

### Source-of-Truth and Restoration Rules
For each important persisted state domain, AMC must define:
- what the authoritative stored form is
- how it is restored
- when restoration is allowed
- how stale persisted state is detected
- how persisted state is reconciled against newer real-time truth

Persistence must support recovery and continuity without causing misleading resurrection of outdated executive context.

### Persistence and Security
Persistence design must remain subordinate to authority, privacy, and security requirements.

This means persisted state must not:
- leak reserved-matter context inappropriately
- expose sandbox-sensitive data across boundaries
- create uncontrolled agent-memory surfaces
- store privileged state in unsafe locations
- silently extend authority through durable credentials or unsafe session reuse

Persistent convenience that weakens constitutional or operational protection is non-compliant.

### Minimum Persistence Checklist
The following minimum conditions must hold for AMC persistence readiness:

- [ ] User preference persistence needs are identified
- [ ] Executive context continuity needs are identified
- [ ] Conversation continuity and significance rules are identified
- [ ] Alert and notification history persistence is identified
- [ ] Approval history persistence is identified
- [ ] Escalation history persistence is identified
- [ ] Intervention history and follow-through persistence is identified
- [ ] Audit-linked state references are identified where required
- [ ] Cross-device and cross-session continuity needs are identified
- [ ] Sandbox and bounded-environment persistence boundaries are identified
- [ ] Retention and sensitivity variation across state domains is acknowledged
- [ ] Source-of-truth and restoration rules are recognized as required downstream design concerns

### Downstream Design Consequence
Downstream FRS, TRS, and Architecture work must explicitly define how persistence behaves for each material state domain.

Persistence may not be left to default framework behavior or to incidental database design. It must be shaped by the executive operating model of AMC.

### Non-Negotiable Principle
AMC state persistence must preserve the right operational memory of the estate without weakening governance, authority, auditability, or boundary integrity.

Any persistence design that causes AMC to forget materially important executive context too easily, or to retain state in ways that blur authority, boundary, or truth, is non-compliant with the intended purpose of AMC.

### Required Persistence Matrix

AMC must define a persistence matrix covering all stateful data classes before Architecture is finalized:

| Data Class | Canonical Owner | Persistence Layer | AMC Role | Audit Required | Notes |
|---|---|---|---|---|---|
| **Alert records** | AMC | AMC database | Create, read, update (status) | Yes — generation, ack, escalation, expiry | Retention policy required |
| **Approval records** | AMC | AMC database | Create, read | Yes — every approval decision | Immutable once recorded |
| **Intervention records** | AMC | AMC database | Create, read, update (status) | Yes — initiation, progress, completion, cancellation | |
| **Upload records** | AIMCC | AIMCC storage | Surface only (read from AIMCC) | Yes — submission event in AMC audit | AMC does not own |
| **Ingestion status** | AIMCC | AIMCC storage | Surface only (read from AIMCC) | Yes — status change events surfaced | AMC does not own |
| **Audit events** | AMC | Audit log (AMC-owned or governed audit service) | Write-only (create) | Self-auditing not required — events are the audit | Immutable; retention policy required |
| **Operator conversation / session state** | AMC | AMC database (or session store) | Manage | Yes — session events where governance-significant | Lifetime / expiry policy required |
| **Memory / knowledge references** | Knowledge / memory system | Knowledge/memory system storage | Surface only (read via governed API) | Yes — retrieval in decision-support context | AMC does not own; provenance required |
| **Persistent knowledge / memory truth** | Knowledge / memory system | Knowledge/memory system storage | No direct write access | Not applicable from AMC side | AIMCC governs writes; AMC may not write |
| **AIMC action records** | AMC (for AMC-originated requests) | AMC audit log | Create | Yes — every AIMC-routed action | Attribution and outcome required |

**Persistence Design Rule**: No data class may be implemented without completing its row in this matrix and having the matrix reviewed by Foreman before Architecture is finalized.


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
- Job initiation and status-tracking surfaces
- Strategic oversight and wellbeing indicators

### User Personas
- **Johan Ras:** constitutional authority, executive decision-maker, reserved-matter approver
- **Maturion:** resident AI executive and principal operational intelligence presence within AMC
- **Foreman:** supervised orchestration actor for execution coordination
- **Specialist agents:** domain-focused or sandbox-focused contributors
- **Assurance agents:** independent evaluators of integrity, compliance, and quality
- **Maintenance agents:** monitoring and upkeep actors for continuous system health

### Key Use Cases
- Receive proactive notification before asking for status
- Approve or reject governance-sensitive changes
- Initiate a governed fix while in a mobile or client context
- Review estate health and drill into root causes
- Oversee sandboxed specialist-agent work within application environments
- Review maintenance, assurance, compliance, and security findings surfaced through Maturion
- Move from discussion to governed execution without losing authority traceability
- Maintain executive contact with the estate while away from desktop environments

### Non-Functional Priorities
- Mobile accessibility
- Persistent availability
- Clear authority boundaries
- Strong auditability
- Controlled AI integration
- Reliable notification and escalation behavior
- Safe delegation and progressive automation
- Explainable operational state
- Strong continuity across devices and sessions

### Future Evolution Considerations
- Progressive expansion of Maturion’s executive authority
- Broader specialist-agent ecosystems
- Deeper sandbox support inside consumer applications
- Expanded autonomous maintenance and assurance capability
- Formalized transition of day-to-day operational control away from Johan while preserving reserved constitutional authority
- More advanced estate-level predictive wellbeing and risk surfacing
- Greater client-context responsiveness during live intervention scenarios

---

## Approval Record

- **Prepared by:** ______________________
- **Reviewed by:** ______________________
- **Approved by:** ______________________
- **Approval Date:** ______________________
- **Approval Reference:** ______________________
