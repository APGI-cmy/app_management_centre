# AMC — App Description

## Status Header

- **Document Title:** AMC App Description
- **Application Name:** App Management Centre (AMC)
- **Lineage:** Successor to the Foreman App / Foreman Office App
- **Document Type:** Stage 1 App Description
- **Status:** Draft for structured completion and approval
- **Authority:** Johan Ras (CS2)
- **Primary AI Executive:** Maturion
- **Supervisory Orchestration Layer:** Foreman
- **Current Canonical Source Decision:** Pending final governance decision on permanent canonical location
- **Purpose of This Document:** Define the authoritative Stage 1 application description for AMC in alignment with governance canon and downstream derivation requirements
- **Stage Intent:** Establish the authoritative product, governance, authority, and operating baseline from which FRS, TRS, Architecture, and delivery planning may be derived

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

---

## §4 — Strategic Context

### Why this application exists
AMC exists because the Maturion estate requires a persistent executive control centre rather than a collection of disconnected build tools, dashboards, repo artifacts, and governance fragments.

The estate is intended to evolve into a governed multi-agent operating system with autonomous execution, specialist support, assurance layers, maintenance layers, and sandboxed AI work environments. Such an estate requires a central executive surface through which wellbeing, intervention, escalation, and authority are managed.

### Relationship to other applications
AMC is not a replacement for domain applications. It is the management and wellbeing centre through which the broader estate is supervised, coordinated, and improved.

Domain applications serve operational business functions. AMC serves executive oversight, control, orchestration supervision, decision routing, notification, and estate-level governance-sensitive management.

### Replacement/extension of
AMC is the matured successor to the Foreman App / Foreman Office App lineage. It carries forward the enduring control-centre intent while separating product identity from legacy governance mixing, early build experimentation, and historical artifact clutter.

### Strategic Evolution Path
- **Current state:** Johan Ras acts as CS2 and constitutional authority over reserved matters
- **Transition state:** Maturion progressively assumes operational executive responsibilities within governed limits
- **Future state:** Johan retains reserved constitutional authority while Maturion manages day-to-day executive supervision of the application estate

### Strategic Positioning
AMC should be understood as an executive operating system for the estate rather than a static admin console. It is intended to combine:
- visibility
- proactive communication
- governed approvals
- intervention launch capability
- supervisory coordination
- agent ecosystem oversight
- estate wellbeing intelligence

---

## §5 — Build Lifecycle Stages (§AD-01)

AMC shall follow the mandatory governance lifecycle in which App Description approval precedes all downstream design and implementation artifacts.

The expected lifecycle order for AMC is:

1. App Description
2. Functional Requirements Specification (FRS)
3. Technical Requirements Specification (TRS)
4. Architecture
5. Detailed design and implementation planning
6. Build execution
7. Verification and assurance
8. Deployment and operationalization

No downstream artifact may contradict the approved App Description. If a downstream artifact reveals missing or conflicting intent, the App Description must be updated through proper approval before continuation.

---

## §6 — Requirements Derivation Chain (§AD-02)

The AMC App Description is the upstream authority for all later requirements and design work.

The required derivation chain is:

- **App Description** defines product identity, scope, authority model, operating purpose, and governance constraints
- **FRS** derives functional capabilities from the approved App Description
- **TRS** derives technical requirements from the FRS and approved governance constraints
- **Architecture** defines the implementation structure required to satisfy TRS and preserve authority/governance boundaries
- **Build planning and implementation** derive from approved architecture and traced requirements
- **Verification artifacts** confirm delivery against approved requirement sources

Every major requirement introduced downstream must be traceable back to either:
1. this App Description,
2. approved governance canon, or
3. a later approved amendment.

---

## §7 — Technology Stack (§AD-03)

The final technology stack will be confirmed in downstream architecture, but AMC must declare the baseline stack categories required to support its product intent.

AMC is expected to require:
- a responsive frontend capable of mobile and desktop operation
- secure backend services for orchestration, state, audit, and notifications
- governed authentication and authorization services
- persistent state and audit storage
- notification and escalation mechanisms
- AI integration via AIMC and AIMC Gateway, not direct uncontrolled model/provider coupling
- agent-safe and sandbox-aware runtime patterns
- observability and operational reporting support

No technology choice may bypass required governance, auditability, or authority protections.

---

## §8 — Deliverable Artifacts (§AD-04)

This App Description must drive the creation of the following downstream artifacts, at minimum:

- AMC Functional Requirements Specification (FRS)
- AMC Technical Requirements Specification (TRS)
- AMC Architecture document
- AMC role/authority/operating-model companion artifact
- UX and workflow design artifacts
- data/state design artifacts
- authentication and authorization design artifacts
- audit and notification design artifacts
- deployment and operational runbooks
- verification and assurance evidence artifacts
- tracker and stage-approval artifacts

Additional artifacts may be required where AMC functionality touches sandboxing, specialist-agent ecosystems, maintenance automation, or assurance orchestration.

---

## §9 — Component Definition of Done (§AD-05)

An AMC component shall not be considered complete unless all of the following are true:

- its purpose is traceable to approved requirements
- its authority boundaries are clear
- its inputs, outputs, and state interactions are documented
- its authentication and authorization rules are defined
- its audit implications are defined
- its notification or interaction effects are understood
- its tests are defined and implemented where applicable
- its behavior is validated against the approved design intent
- its tracker and evidence records are updated

For AMC specifically, “done” also requires that a component not silently undermine reserved-matter control, governance-sensitive approval flows, or separation between executive, orchestration, assurance, and implementation roles.

---

## §10 — Test-First Guarantee (§AD-06)

AMC delivery shall follow the governance requirement that test expectations are defined before implementation is considered complete.

Derived build work must define:
- expected user behavior
- expected agent behavior
- expected authorization behavior
- expected state transitions
- expected audit outcomes
- expected notification outcomes
- expected failure and escalation behavior

No component may be treated as production-ready if its expected behavior cannot be verified in a structured way.

---

## §11 — Physical Verification Gate (§AD-07)

AMC includes workflows whose value depends on real operator experience and real interaction surfaces, especially mobile access, proactive notification, approval handling, escalation review, and conversation-driven intervention.

For this reason, physical or real-environment verification shall be required where relevant, including:
- mobile interaction validation
- desktop interaction validation
- real notification delivery checks
- end-to-end conversation and approval flow checks
- operator-observable behavior confirmation
- intervention workflow confirmation in realistic usage contexts

AMC must not be approved purely on abstract design claims where real interaction quality is material to success.

---

## §12 — PBFAG Checklist Requirements (§AD-08)

Before downstream build work proceeds, AMC must satisfy the required pre-build governance checklist and any equivalent mandatory gating controls defined by governance canon.

For AMC, checklist readiness shall explicitly include confirmation that:
- Stage 1 scope is stable
- authority boundaries are clear
- reserved matters are clearly identified
- AI integration path is governed
- notification and audit obligations are identified
- state and authentication concerns are acknowledged
- downstream artifact expectations are known

A missing checklist item shall be treated as a blocking defect, not an advisory note.

---

## §13 — Agent Authority Chain (§AD-09)

AMC shall operate under the following authority model:

- **Johan Ras** remains constitutional authority over reserved matters
- **Maturion** operates as resident AI executive within AMC
- **Foreman** operates as supervised orchestration authority beneath Maturion
- **IAA agents** remain independent assurance actors and do not become cleanup-authoring substitutes
- **Maintenance agents** perform maintenance and health-related duties within approved boundaries
- **Specialist agents** perform domain-specific or sandbox-specific work under governed supervision
- **Builders** are implementation actors and do not become constitutional or supervisory authorities

Reserved matters shall include, at minimum:
- governance changes
- agent-file changes
- major app-description changes
- major design changes
- constitutional authority changes
- authority-transfer changes
- other explicitly reserved matters defined by governance

AMC must support progressive delegation, but it must not hide or blur where final authority still resides.

---

## §14 — Schema-to-Hook Validation (§AD-10)

Any data model, state model, hook pattern, orchestration interface, or integration pathway proposed for AMC must be validated against approved requirements and architecture.

AMC is expected to contain rich cross-surface state, approval state, alert state, conversation state, and operational context. Because of that, careless hook/state design could easily create hidden authority defects, inconsistent behavior, or audit gaps.

All schema-to-hook or schema-to-state pathways must therefore be:
- named
- documented
- reviewed
- traceable to approved design intent

---

## §15 — Table Pathway Audit (§AD-11)

All persistent data pathways used by AMC must be explicitly identified and auditable.

This includes pathways for:
- user/account state
- agent/account state
- conversation history
- alerts and escalations
- approvals and decisions
- audit events
- sandbox state
- operational jobs
- maintenance/assurance reports
- notification history
- device continuity or session continuity

No table or persistent storage pathway may be introduced without clear purpose, ownership, access rules, and audit awareness.

---

## §16 — RLS Audit Gate (§AD-12)

Where relational or persistent user/agent data is used, Row-Level Security or equivalent access-control validation must be explicitly designed and reviewed.

AMC will handle sensitive executive, operational, and potentially client-linked information. Therefore:
- access must be least-privilege by default
- agent access must be bounded to approved roles and scopes
- user access must respect authority level and context
- sandbox segregation must be respected
- approval-sensitive data must be protected against unauthorized reads and writes

No assumption of “internal app therefore trusted” is acceptable.

---

## §17 — Auth Wiring Checklist (§AD-13)

AMC must define a formal authentication and authorization model covering:
- Johan Ras as human executive authority
- future approved human roles if introduced
- Maturion as executive AI identity
- Foreman as orchestration identity
- specialist, assurance, and maintenance agent identities
- sandbox-restricted identities where needed
- privileged-action approval flows
- reserved-matter protection

Authentication alone is not enough. AMC requires authorization rules that preserve governance boundaries and trace who did what, under which authority, in what context.

---

## §18 — AI Integration Requirements (§AD-14)

AMC is deeply AI-dependent, but its AI model must remain governed.

AMC AI integration shall include:
- Maturion as resident AI executive
- specialist-agent and sandbox-agent integration patterns
- AIMC and AIMC Gateway routing requirements
- prohibition of uncontrolled direct provider integration
- separation between executive AI, orchestration AI, specialist AI, maintenance AI, and assurance AI
- governed approval boundaries for sensitive actions
- traceability for AI-triggered recommendations, alerts, and operational actions

Maturion must be able to communicate proactively, support decision-making, coordinate action, and manage reporting flows, but must do so through a controlled architecture that preserves auditability, authority, and policy enforcement.

---

## §19 — Edge Function Registry (§AD-15)

All edge functions, orchestration actions, operational endpoints, and externally callable service entry points used by AMC must be registered and governed.

For AMC, likely registered function classes will include:
- notification dispatch functions
- conversation/action routing functions
- approval handling functions
- orchestration dispatch functions
- audit/event recording functions
- sandbox coordination functions
- maintenance/report collection functions
- assurance reporting ingestion functions

No operational endpoint may exist as undocumented hidden plumbing.

---

## §20 — Deployment Wave (§AD-16)

AMC delivery shall be staged in controlled deployment waves.

An indicative wave pattern is:
- **Wave 1:** Stage 1 definition, authority model, and design baseline
- **Wave 2:** core executive dashboard, conversation surface, and audit foundation
- **Wave 3:** approval workflows, proactive notifications, and estate-health visibility
- **Wave 4:** specialist-agent oversight and sandbox visibility
- **Wave 5:** maintenance and assurance reporting integration
- **Wave 6:** expanded delegated operations and higher autonomy features

Actual wave definitions will be finalized later, but AMC must be designed as a progressively delivered governed platform rather than a monolithic one-shot build.

---

## §21 — Secret Naming Convention (§AD-17)

AMC will require strict handling of secrets, credentials, tokens, and environment-bound operational keys.

Secret design shall ensure:
- clear naming conventions
- separation by environment
- separation by capability
- no leakage of provider credentials into client surfaces
- no direct unmanaged model/provider credentials in app code
- traceable ownership and usage of privileged secrets
- compatibility with AIMC and governance controls

Secret naming and handling must be formalized before live integration work proceeds.

---

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

---

## §23 — Notification/UX Patterns (§AD-19)

Notification and UX are central to AMC’s purpose, not secondary polish items.

AMC shall support:
- proactive notification before the user asks, where justified by context or severity
- escalation prompts when intervention is required
- approval prompts for governance-sensitive or reserved-matter actions
- attention routing to mobile and desktop contexts
- conversational interaction with Maturion
- dashboard and drill-down supervision patterns
- clear differentiation between informational, warning, approval, and emergency states
- deliberate avoidance of crude or non-governed alert mechanisms

AMC UX shall be executive in nature. It must help Johan remain informed and decisive without forcing him to become a log reader, code operator, or control-plane mechanic.

---

## §24 — Shared State Architecture (§AD-20)

AMC requires a shared state architecture capable of maintaining coherent executive context across screens, surfaces, sessions, and devices.

Shared state is expected to include:
- supervisory context
- active conversation context
- alert state
- escalation state
- intervention state
- approval queue state
- estate health summaries
- sandbox context
- role/identity context
- continuity state across mobile and desktop experiences

This architecture must prevent contradictory views of estate status and support reliable action-taking.

---

## §25 — API Authentication (§AD-21)

All AMC APIs and orchestration actions must enforce authentication and authorization that match the approved authority model.

This includes:
- authenticated human actions
- authenticated agent actions
- role-based restrictions
- reserved-matter protections
- sandbox-bound restrictions where applicable
- traceable initiation of build or maintenance jobs
- explicit approval enforcement for sensitive actions

API authentication design must not be treated as a late technical afterthought. It is part of the product’s constitutional integrity.

---

## §26 — Audit Log Design (§AD-22)

AMC must maintain a structured audit model capable of recording, at minimum:
- approvals
- interventions
- agent actions
- governance-sensitive events
- maintenance events
- assurance events
- build/job initiation and completion events
- notification dispatches
- escalation acknowledgements
- authority-relevant decision records

Audit logging is essential because AMC is expected to become the surface through which increasingly autonomous operations are governed. Without trustworthy auditability, AMC cannot safely support progressive delegation.

---

## §27 — Tracker Update Requirement (§AD-23)

Trackers and stage-progress artifacts must be updated alongside substantive work so AMC state, delivery state, and governance state remain synchronized.

No major Stage 1, Stage 2, or later progress claim is valid if the corresponding trackers, approval records, or stage artifacts are stale or misleading.

For AMC, tracker discipline matters especially because the application is intended to manage wellbeing, visibility, and operational truth. The application’s own design process must model that discipline.

---

## §28 — State Persistence Specification (§AD-24)

AMC must define persistence expectations for the state it manages and presents.

This includes:
- user preferences
- supervisory session context
- conversation history and context continuity
- alert history
- approval history
- audit history
- device-specific continuity
- sandbox context
- operational status continuity
- restoration expectations after interruption or reconnect

State persistence must be designed to support continuity without compromising governance, privacy, authority boundaries, or audit integrity.

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
