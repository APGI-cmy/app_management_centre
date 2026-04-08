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
