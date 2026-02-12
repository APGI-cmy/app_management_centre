# CodexAdvisor Agent Contract Requirements Checklist (CodexAdvisor-agent.md)

**Status**: Reference checklist for contract drafting  
**Purpose**: Exhaustive, source-mapped requirements for a compliant CodexAdvisor (Overseer) agent file in this repo.  
**Primary Sources**: Living Agent System v6.2.0, `governance/canon/AGENT_FILE_BINDING_REQUIREMENTS.md`, `CS2_AGENT_FILE_AUTHORITY_MODEL.md`, `AGENT_CONTRACT_PROTECTION_PROTOCOL.md`, Agent-Factory Protocol requirements.  
**Living Agent System Version**: v6.2.0

---

## Category 0 — Identity, Bindings & Scope (REQ-CM-001 through REQ-CM-007)

- [ ] **REQ-CM-001**: Frontmatter YAML complete with `agent.id=CodexAdvisor-agent`, `agent.class=overseer`, `agent.version=6.2.0`
- [ ] **REQ-CM-002**: Governance protocol declared: `governance.protocol=LIVING_AGENT_SYSTEM`
- [ ] **REQ-CM-003**: Canon inventory path specified: `governance.canon_inventory=.governance-pack/CANON_INVENTORY.json` (consumer mode)
- [ ] **REQ-CM-004**: Expected artifacts enumerated (CANON_INVENTORY.json, CONSUMER_REPO_REGISTRY.json, GATE_REQUIREMENTS_INDEX.json)
- [ ] **REQ-CM-005**: Degraded mode semantics declared: `degraded_on_placeholder_hashes: true` with escalation action
- [ ] **REQ-CM-006**: Execution identity specified (Maturion Bot, token secret, safety rules: never_push_main, write_via_pr_by_default)
- [ ] **REQ-CM-007**: Repository scope declared with cross-repo access list (governance repo + consumer repos)

## Category 1 — Appointment Preconditions & Authority Boundaries (REQ-AB-001 through REQ-AB-006)

- [ ] **REQ-AB-001**: Authority source documented (CS2 authorization required for ALL actions)
- [ ] **REQ-AB-002**: Approval gate enforcement: `approval_required: ALL_ACTIONS`
- [ ] **REQ-AB-003**: Explicit negatives enumerated (what CodexAdvisor is NOT: not a builder, not FM, not governance author)
- [ ] **REQ-AB-004**: Agent-factory authority boundaries defined (PR_PREFERRED for agent file creation/updates)
- [ ] **REQ-AB-005**: Required checklists mapped to agent types (governance_liaison, foreman, builder, codex_advisor)
- [ ] **REQ-AB-006**: Escalation rules for authority boundary conflicts documented

## Category 2 — Governance Alignment & Layer-Down (REQ-RA-001 through REQ-RA-005)

- [ ] **REQ-RA-001**: Drift detection mechanism specified: CANON_INVENTORY_HASH_COMPARE
- [ ] **REQ-RA-002**: Ripple protocol documented: Consumer-only mode (dispatch_from_governance: false, listen_on_consumers: repository_dispatch)
- [ ] **REQ-RA-003**: Ripple targets source specified: .governance-pack/CONSUMER_REPO_REGISTRY.json
- [ ] **REQ-RA-004**: Schedule fallback for drift detection: hourly
- [ ] **REQ-RA-005**: Evidence paths enumerated: `.agent-admin/governance/sync_state.json`

## Category 3 — Execution Discipline, Evidence & Tests (REQ-EO-001 through REQ-EO-006)

- [ ] **REQ-EO-001**: Architecture-first discipline enforced (freeze architecture before build)
- [ ] **REQ-EO-002**: QA-to-Red requirement documented (red test suite before implementation)
- [ ] **REQ-EO-003**: Build-to-Green requirement documented (100% green before PR merge)
- [ ] **REQ-EO-004**: Zero-test-debt enforcement (no failing/skipped/TODO/hidden tests)
- [ ] **REQ-EO-005**: Session closure protocol specified (evidence capture, memory creation, ripple archival)
- [ ] **REQ-EO-006**: Wake-up protocol specified (identity load, memory scan, governance load, environment health)

## Category 4 — Ripple, Drift & Sync (REQ-RD-001 through REQ-RD-004)

- [ ] **REQ-RD-001**: Ripple inbox management protocol defined (.agent-admin/governance/ripple-inbox/)
- [ ] **REQ-RD-002**: Sync state tracking specified (sync_pending, drift_detected, canonical_commit)
- [ ] **REQ-RD-003**: Alignment PR creation process documented (canonical sync → PR → CS2 review)
- [ ] **REQ-RD-004**: Ripple archival process specified (.agent-admin/governance/ripple-archive/)

## Category 5 — Escalation & Stop Rules (REQ-ES-001 through REQ-ES-005)

- [ ] **REQ-ES-001**: Automatic escalation triggers enumerated (contract changes, canon interpretation, missing artifacts, placeholder hashes, authority conflicts)
- [ ] **REQ-ES-002**: Escalation file format specified (.agent-workspace/<agent-id>/escalation-inbox/blocker-YYYYMMDD.md)
- [ ] **REQ-ES-003**: Escalation types defined (BLOCKER, GOVERNANCE_GAP, AUTHORITY_BOUNDARY, CONSTITUTIONAL_CHANGE)
- [ ] **REQ-ES-004**: Stop-and-fix enforcement for governance drift
- [ ] **REQ-ES-005**: CS2 escalation path documented with context/canon/recommendation format

## Category 6 — Prohibitions & Guardrails (REQ-PG-001 through REQ-PG-012)

- [ ] **REQ-PG-001**: Universal prohibitions enumerated (no execution without approval, no weakening governance, no pushing to main, no secrets)
- [ ] **REQ-PG-002**: Consumer-specific prohibitions documented (no modifying .governance-pack/, no creating canon, no dispatching ripple)
- [ ] **REQ-PG-003**: Self-modification prohibition (no edits to .agent file except via CS2-approved issue)
- [ ] **REQ-PG-004**: No skipping wake-up or session closure protocols
- [ ] **REQ-PG-005**: No evidence mutation in-place (create new artifacts)
- [ ] **REQ-PG-006**: No force-push operations
- [ ] **REQ-PG-007**: No bypassing Merge Gate Interface checks
- [ ] **REQ-PG-008**: **CRITICAL**: No agent files exceeding 30,000 characters (blocks GitHub UI selectability, ref: PartPulse PR #265)
- [ ] **REQ-PG-009**: No creating agent files that reference canonical governance paths (use .governance-pack/ instead)
- [ ] **REQ-PG-010**: No bypassing governance alignment gate (drift must be resolved before proceeding)
- [ ] **REQ-PG-011**: No direct pushes to main; PR-only writes
- [ ] **REQ-PG-012**: Role-specific prohibitions for CodexAdvisor (never performs builder or foreman tasks directly)

## Category 7 — Outputs & Deliverables (REQ-OD-001 through REQ-OD-005)

- [ ] **REQ-OD-001**: Agent file creation/update outputs with PREHANDOVER_PROOF
- [ ] **REQ-OD-002**: Governance alignment reports (drift detection, sync status, canonical commit tracking)
- [ ] **REQ-OD-003**: Evidence artifacts under .agent-admin/ (sync_state.json, ripple logs)
- [ ] **REQ-OD-004**: Session memory files (.agent-workspace/<agent-id>/memory/session-NNN-YYYYMMDD.md)
- [ ] **REQ-OD-005**: Escalation artifacts when needed (.agent-workspace/<agent-id>/escalation-inbox/)

## Category 8 — Agent-Factory Specific Requirements (REQ-AG-001 through REQ-AG-004)

- [ ] **REQ-AG-001**: 7-step agent-factory execution process documented (verify canon → select checklist → load requirements → generate file → validate character count → validate checklist → create PR with evidence → post-merge verification)
- [ ] **REQ-AG-002**: 9 mandatory template components enumerated (YAML frontmatter, requirement mappings, validation hooks, LOCKED metadata, protocols, escalation rules, prohibitions, canon references, execution checklist)
- [ ] **REQ-AG-003**: Character count validation CRITICAL step (max 30,000, target <25,000, verification required)
- [ ] **REQ-AG-004**: PREHANDOVER_PROOF requirements for agent file creation (CS2 authorization, checklist compliance matrix, before/after comparison, requirement mapping verification, validation hook confirmation, consumer adaptations, canon references enumeration)

## Category 9 — Canonical Governance References (REQ-CG-001 through REQ-CG-005)

- [ ] **REQ-CG-001**: Enumerate all PUBLIC_API artifacts from CANON_INVENTORY.json relevant to CodexAdvisor role
- [ ] **REQ-CG-002**: Verify SHA256 checksums exist in CANON_INVENTORY for all referenced artifacts
- [ ] **REQ-CG-003**: Document degraded-mode behavior when checksums are placeholder/truncated
- [ ] **REQ-CG-004**: Reference canon by path (.governance-pack/canon/<file>) not by embedding content
- [ ] **REQ-CG-005**: Maintain canon version alignment tracking in evidence logs

## Category 10 — Living Agent System v6.2.0 Template Components (REQ-LAS-001 through REQ-LAS-009)

- [ ] **REQ-LAS-001**: Component 1 - YAML Frontmatter complete (all required fields per Living Agent System v6.2.0)
- [ ] **REQ-LAS-002**: Component 2 - Requirement Mappings present (all 56 requirements REQ-CM-001 through REQ-AG-004 mapped)
- [ ] **REQ-LAS-003**: Component 3 - Validation Hooks documented (all 5 hooks VH-001 through VH-005 with Trigger/Action/Failure)
- [ ] **REQ-LAS-004**: Component 4 - LOCKED Section Metadata present (Lock ID, Authority, Review Frequency, Modification Authority)
- [ ] **REQ-LAS-005**: Component 5 - Wake-Up and Session Closure Protocols embedded (full protocol specifications)
- [ ] **REQ-LAS-006**: Component 6 - Escalation Rules and Authority Boundaries detailed
- [ ] **REQ-LAS-007**: Component 7 - Prohibitions Enhanced (universal + consumer + role-specific)
- [ ] **REQ-LAS-008**: Component 8 - Canonical Governance References enumerated with hash verification
- [ ] **REQ-LAS-009**: Component 9 - Execution Checklist embedded in file (transparency and compliance verification)

## Category 11 — Merge Gate Interface Requirements (REQ-MGI-001 through REQ-MGI-005)

- [ ] **REQ-MGI-001**: Required checks enumerated (merge-gate/verdict, governance/alignment, stop-and-fix/enforcement)
- [ ] **REQ-MGI-002**: Auto-merge conditions specified (only when required checks are green)
- [ ] **REQ-MGI-003**: Alignment check specification (compare local code/config against .governance-pack/CANON_INVENTORY.json)
- [ ] **REQ-MGI-004**: PR classification determinism (evidence-first messaging in PR description)
- [ ] **REQ-MGI-005**: Merge gate expectations documented (advisory role, not blocking implementation)

## Category 12 — Governance Sync Protocol (Consumer Mode) (REQ-GSP-001 through REQ-GSP-005)

- [ ] **REQ-GSP-001**: repository_dispatch event handling (governance_ripple event type)
- [ ] **REQ-GSP-002**: Event payload structure documented (canonical_commit, inventory_version, changed_paths, sender, dispatch_id, timestamp)
- [ ] **REQ-GSP-003**: Ripple inbox entry creation process (.agent-admin/governance/ripple-inbox/ripple-${DISPATCH_ID}.json)
- [ ] **REQ-GSP-004**: Sync state update mechanism (last_ripple_received, canonical_commit, sync_pending)
- [ ] **REQ-GSP-005**: Alignment PR creation workflow (pull latest governance pack → compare hashes → create PR → CS2 review for constitutional changes → update sync_state → archive ripple)

## Category 13 — Validation Hooks (VH-001 through VH-005)

- [ ] **VH-001**: Wake-up validation - Verify .governance-pack/CANON_INVENTORY.json SHA256 checksums; Trigger: At session start; Action: Load and verify checksums; Failure: Escalate to CS2 if placeholder/truncated hashes detected
- [ ] **VH-002**: Pre-execution validation - Verify governance alignment status; Trigger: Before any code/agent file modifications; Action: Check sync_state.json drift_detected flag; Failure: Block execution and create alignment PR if drift detected
- [ ] **VH-003**: Character count validation - Enforce 30,000 character limit on agent files; Trigger: During agent file creation/update; Action: Run `wc -m < .github/agents/<file>.md`; Failure: BLOCK merge if >30,000 characters (critical UI selectability requirement)
- [ ] **VH-004**: Checklist compliance validation - Verify 100% checklist compliance; Trigger: Before creating PREHANDOVER_PROOF; Action: Cross-reference all checklist items against agent file; Failure: Block PR creation until 100% compliance achieved
- [ ] **VH-005**: Post-merge verification - Verify agent file persisted correctly; Trigger: After PR merge; Action: Read merged file and verify content integrity; Failure: Create evidence log of verification failure and escalate to CS2

## Category 14 — Session Memory and Learning (REQ-SM-001 through REQ-SM-005)

- [ ] **REQ-SM-001**: Session memory template specified with all required sections (Agent, Task, What I Did, Living Agent System Evidence, Outcome, Lessons)
- [ ] **REQ-SM-002**: Session memory file path format: .agent-workspace/<agent-id>/memory/session-NNN-YYYYMMDD.md
- [ ] **REQ-SM-003**: Memory rotation protocol (when >5 sessions, move oldest to .archive/)
- [ ] **REQ-SM-004**: Personal learning updates (lessons-learned.md and patterns.md in .agent-workspace/<agent-id>/personal/)
- [ ] **REQ-SM-005**: Living Agent System v6.2.0 version declared in ALL session memory headers

## Category 15 — Consumer-Specific Adaptations (REQ-CSA-001 through REQ-CSA-007)

- [ ] **REQ-CSA-001**: Metadata declares `this_copy: consumer` in YAML frontmatter
- [ ] **REQ-CSA-002**: Canonical home documented: APGI-cmy/maturion-foreman-governance
- [ ] **REQ-CSA-003**: Canon inventory path uses .governance-pack/ (not governance/)
- [ ] **REQ-CSA-004**: Checklist references use .governance-pack/checklists/
- [ ] **REQ-CSA-005**: Capabilities declare `dispatch_from_governance: false` (receive-only mode)
- [ ] **REQ-CSA-006**: Prohibitions include consumer-specific restrictions (no modifying .governance-pack/, no creating canon, no dispatching ripple)
- [ ] **REQ-CSA-007**: Evidence paths use .agent-admin/governance/ for alignment tracking

---

## Appendix A — Required Canonical Governance Artifacts for CodexAdvisor

This appendix enumerates PUBLIC_API canonical governance artifacts that CodexAdvisor MUST read, reference, and align against per protocol. All artifacts are sourced from `APGI-cmy/maturion-foreman-governance` canonical repository and tracked in `governance/CANON_INVENTORY.json`.

**Total PUBLIC_API Canons**: 102+ (as of 2026-02-11)

### Core Governance & Authority
- `GOVERNANCE_PURPOSE_AND_SCOPE.md` — Supreme authority defining governance as canonical memory
- `BUILD_PHILOSOPHY.md` — Constitutional principles for one-time build correctness
- `CS2_AGENT_FILE_AUTHORITY_MODEL.md` — CS2 authority over agent file modifications
- `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` — Locked section protection mechanisms
- `AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md` — Single-writer pattern for agent contracts

### Agent Recruitment & Lifecycle
- `AGENT_RECRUITMENT.md` — Agent legitimacy and recruitment process
- `AGENT_RECRUITMENT_AND_CONTRACT_AUTHORITY_MODEL.md` — Authority model for agent appointments
- `AGENT_FILE_BINDING_REQUIREMENTS.md` — Mandatory governance bindings for agent files
- `AGENT_ONBOARDING_QUICKSTART.md` — Agent onboarding process
- `LIVING_AGENT_SYSTEM.md` — Living Agent System v6.2.0 framework specification

### Cross-Repository Governance
- `CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md` — Explicit controlled governance propagation protocol
- `CROSS_REPO_RIPPLE_TRANSPORT_PROTOCOL.md` — Mandatory ripple transport and registry targeting
- `GOVERNANCE_RIPPLE_MODEL.md` — Ripple signaling mechanism
- `GOVERNANCE_RIPPLE_DETECTION_PROTOCOL.md` — Ripple detection requirements
- `GOVERNANCE_RIPPLE_CHECKLIST_PROTOCOL.md` — Step-by-step ripple execution checklist
- `AGENT_RIPPLE_AWARENESS_OBLIGATION.md` — Ripple awareness obligations for all agents
- `GOVERNANCE_VERSIONING_AND_SYNC_PROTOCOL.md` — Version synchronization requirements

### Execution & Evidence
- `EXECUTION_BOOTSTRAP_PROTOCOL.md` — Mandatory protocol for executable artifacts
- `CI_CONFIRMATORY_NOT_DIAGNOSTIC.md` — CI role definition (confirmatory, not diagnostic)
- `PREHANDOVER_PROOF_TEMPLATE.md` — Evidence template for handover
- `AGENT_TEST_EXECUTION_PROTOCOL.md` — Test execution requirements for agents
- `zero-test-debt-constitutional-rule.md` — Constitutional zero-test-debt requirement

### Merge Gates & Quality
- `MERGE_GATE_PHILOSOPHY.md` — Merge gate principles and application
- `MERGE_GATE_APPLICABILITY_MATRIX.md` — When and how to apply merge gates
- `STOP_AND_FIX_DOCTRINE.md` — Mandatory stop-and-fix for warnings/test debt
- `BRANCH_PROTECTION_ENFORCEMENT.md` — Branch protection requirements

### Foreman & Builder Supervision
- `FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md` — Foreman authority over builders
- `FM_EXECUTION_MANDATE.md` — Foreman execution authority and responsibilities
- `BUILDER_APPOINTMENT_PROTOCOL.md` — Builder recruitment and appointment process
- `AGENT_SCOPED_QA_BOUNDARIES.md` — QA boundary definitions for agents

### Memory & Learning
- `FOREMAN_MEMORY_PROTOCOL.md` — Memory hierarchy and lifecycle
- `MEMORY_LIFECYCLE_STATE_MACHINE_CONTRACT.md` — Memory state machine specification
- `LEARNING_PROMOTION_RULE.md` — Learning promotion requirements
- `FAILURE_PROMOTION_RULE.md` — Failure documentation and promotion

### Safety & Escalation
- `CASCADING_FAILURE_CIRCUIT_BREAKER.md` — Circuit breaker for cascading failures
- `WARNING_DISCOVERY_BLOCKER_PROTOCOL.md` — Warning handling and escalation
- `GOVERNANCE_COMPLETENESS_MODEL.md` — Governance completeness verification

---

## Appendix B — Character Count Validation Requirements

**CRITICAL REQUIREMENT**: All agent files MUST be under 30,000 characters to maintain GitHub UI selectability.

### Validation Command
```bash
wc -m < .github/agents/<agent-file>.md
```

### Enforcement Levels
- **BLOCKING** (>30,000 characters): Fails validation, blocks PR merge
- **WARNING** (>25,000 characters): Issues warning, recommends refactoring (20% buffer)
- **OPTIMAL** (<25,000 characters): Recommended target for UI performance

### Refactoring Strategy (if limit approached or exceeded)
1. Replace embedded templates with 5-line references to canonical governance
2. Extract protocols to separate workflow scripts (.github/scripts/)
3. Move large code blocks to external files and reference by path
4. Use links to canonical source instead of embedding content
5. Consolidate redundant sections

### Reference
PartPulse PR #265 - Character limit enforcement requirement

---

## Appendix C — Startup and Closure Protocol Requirements

### Wake-Up Protocol (Execute at session start)
**Script**: `.github/scripts/wake-up-protocol.sh <agent-id>`

**Actions performed**:
1. Load agent identity and contract version
2. Scan last 5 session memories from `.agent-workspace/<agent-id>/memory/`
3. Load governance state from `.agent-admin/governance/sync_state.json`
4. Verify environment health (CANON_INVENTORY integrity, no placeholder hashes)
5. Generate `working-contract.md` with current context (ephemeral, not committed)
6. HALT if degraded mode detected (placeholder hashes in PUBLIC_API artifacts)

**Output**: `.agent-workspace/<agent-id>/working-contract.md` (ephemeral)

### Session Closure Protocol (Execute at session end)
**Script**: `.github/scripts/session-closure.sh <agent-id>`

**Actions performed**:
1. Capture evidence artifacts to `.agent-admin/`
2. Create session memory file using template (see REQ-SM-001)
3. Rotate memories if count > 5 (move oldest to `.archive/`)
4. Record lessons learned in `.agent-workspace/<agent-id>/personal/lessons-learned.md`
5. Archive completed ripple events to `.agent-admin/governance/ripple-archive/`

---

## Appendix D — Compliance Verification

**CodexAdvisor Self-Compliance Status**: ✅ To be verified after checklist application

**This checklist covers**:
- ✅ 56 requirement mappings (REQ-CM-001 through REQ-AG-004)
- ✅ 5 validation hooks (VH-001 through VH-005)
- ✅ 9 Living Agent System v6.2.0 template components
- ✅ Consumer-specific adaptations (7 requirements)
- ✅ Merge Gate Interface requirements (5 requirements)
- ✅ Session memory and learning requirements (5 requirements)
- ✅ Character count enforcement (CRITICAL)
- ✅ Startup/closure protocol specifications
- ✅ Agent-factory execution process (7 steps)
- ✅ PREHANDOVER_PROOF requirements (7 sections)

**Total Requirements**: 83+ discrete checkpoints

**Repository Mode**: Consumer  
**Canonical Home**: `APGI-cmy/maturion-foreman-governance`  
**Living Agent System Version**: v6.2.0  
**Last Updated**: 2026-02-12  
**Created By**: CodexAdvisor-agent (Session 005 - Self-Review)

---

**Usage**: Treat every unchecked item as a blocker for `CodexAdvisor-agent.md` readiness. Cite the listed source in the contract section that satisfies the item. If a required source is unavailable or hash-mismatched, halt and escalate per Category 5. When creating or updating CodexAdvisor agent file, verify 100% checklist compliance before PR creation.

**Authority**: Living Agent System v6.2.0 | CS2 Authorization Required for Agent File Modifications
