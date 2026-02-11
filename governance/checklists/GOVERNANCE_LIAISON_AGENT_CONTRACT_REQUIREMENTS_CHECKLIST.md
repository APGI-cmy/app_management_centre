# Governance Liaison Agent Contract Requirements Checklist (governance-liaison-v2.agent.md)

**Status**: Reference checklist for contract drafting  
**Purpose**: Exhaustive, source-mapped requirements for a compliant Governance Liaison agent file in this repo.  
**Primary Sources**: `governance/baselines/agent-files/governance-liaison.md`, `governance/canon/GOVERNANCE_LIAISON_MINIMUM_APPOINTMENT_REQUIREMENTS.md`, `GOVERNANCE_LIAISON_MINIMUM_REQUIREMENTS_VALIDATION.md`, `governance/canon/*` (see citations).

---

## Category 0 — Identity, Bindings & Scope
- [ ] **Frontmatter**: `agent.id=governance-liaison`, `agent.class=liaison`; `governance.canon` points to `APGI-cmy/maturion-foreman-governance/governance/canon`; Tier-0 manifest loaded (`governance/baselines/agent-files/governance-liaison.md`).
- [ ] **Mandatory bindings present**: Governance purpose/scope, Build Philosophy, zero-test-debt, execution bootstrap, ripple model, contract protection, agent recruitment/authority, merge-gate philosophy, agent test execution, ripple checklist (`AGENT_FILE_BINDING_REQUIREMENTS.md`, `GOVERNANCE_LIAISON_MINIMUM_APPOINTMENT_REQUIREMENTS.md` Sections 2 & 5).
- [ ] **Scope declaration**: Repo-scoped, write-access limits, restricted paths (.github/agents, Build Philosophy) captured (`governance/baselines/agent-files/governance-liaison.md`).

## Category 1 — Appointment Preconditions & Authority Boundaries
- [ ] **Structural appointment**: All five preconditions recorded (Tier-0 loaded, explicit scope, authorization trail, protocol reference, coupling rules active) (`GOVERNANCE_LIAISON_MINIMUM_APPOINTMENT_REQUIREMENTS.md` Section 5; validation report Section 1).
- [ ] **Authority chain**: FM (recruiting authority) → Governance Liaison; human authorization required; appointment revocable (`GOVERNANCE_LIAISON_MINIMUM_APPOINTMENT_REQUIREMENTS.md` Sections 3.2, 6; `FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md`).
- [ ] **Explicit negatives**: NOT builder, NOT FM, NOT governance administrator, NOT enforcement agent; cannot self-modify own contract (`GOVERNANCE_LIAISON_MINIMUM_APPOINTMENT_REQUIREMENTS.md` Section 3.3; `governance/baselines/agent-files/governance-liaison.md` locked sections).
- [ ] **Authority model compliance**: CS2 agent file authority + contract protection protocols referenced for any contract edits (`CS2_AGENT_FILE_AUTHORITY_MODEL.md`, `AGENT_CONTRACT_PROTECTION_PROTOCOL.md`).

## Category 2 — Governance Alignment & Layer-Down
- [ ] **Self-alignment mandate**: Must verify local governance vs canonical and self-align drift before work; halt if own contract drifts (`governance/baselines/agent-files/governance-liaison.md` Pre-Job Self-Governance; `GOVERNANCE_VERSIONING_AND_SYNC_PROTOCOL.md`).
- [ ] **Layer-down protocol**: Uses governance layerdown contract + ripple checklist for updates; respects repository seeding & enforcement role separation (`GOVERNANCE_LAYERDOWN_CONTRACT.md`, `GOVERNANCE_RIPPLE_CHECKLIST_PROTOCOL.md`, `REPOSITORY_SEEDING_AND_ENFORCEMENT_ROLE_SEPARATION.md`).
- [ ] **Inventory updates**: Maintains `GOVERNANCE_ARTIFACT_INVENTORY.md` and governance version markers per sync protocol (`governance/baselines/agent-files/governance-liaison.md`, `GOVERNANCE_VERSIONING_AND_SYNC_PROTOCOL.md`).

## Category 3 — Execution Discipline, Evidence & Tests
- [ ] **Execution Bootstrap** applied to any executable/workflow changes; PREHANDOVER proof attached; CI confirmatory rule acknowledged (`EXECUTION_BOOTSTRAP_PROTOCOL.md`, `CI_CONFIRMATORY_NOT_DIAGNOSTIC.md`, `governance/templates/PREHANDOVER_PROOF_TEMPLATE.md`).
- [ ] **Test enforcement**: Agent Test Execution Protocol binding present; zero-test-debt + stop-and-fix doctrine enforced for governance artifacts with execution semantics (`governance/runbooks/AGENT_TEST_EXECUTION_PROTOCOL.md`, `governance/policies/zero-test-debt-constitutional-rule.md`, `STOP_AND_FIX_DOCTRINE.md`).
- [ ] **Audit trail**: Initialization or coupling actions documented with timestamps/authorizations (`GOVERNANCE_LIAISON_MINIMUM_APPOINTMENT_REQUIREMENTS.md` Sections 4.1.1, 4.1.2).

## Category 4 — Ripple, Drift & Sync
- [ ] **Ripple awareness**: Non-local impact assumed; ripple detection + checklist protocols followed; cross-repo transport respected (`AGENT_RIPPLE_AWARENESS_OBLIGATION.md`, `GOVERNANCE_RIPPLE_MODEL.md`, `GOVERNANCE_RIPPLE_DETECTION_PROTOCOL.md`, `CROSS_REPO_RIPPLE_TRANSPORT_PROTOCOL.md`).
- [ ] **Sync discipline**: Governance versioning/sync protocol applied; drift flagged and cleared before proceeding (`GOVERNANCE_VERSIONING_AND_SYNC_PROTOCOL.md`, validation report Success Criterion 5).
- [ ] **Alignment reporting**: Ripple inbox/archival + sync_state updates executed per consumer-mode governance instructions (merge gate interface expectations noted) (`governance/baselines/agent-files/governance-liaison.md`, merge gate interface expectations in repository instructions).

## Category 5 — Escalation & Stop Rules
- [ ] **STOP triggers**: Ambiguity, contract drift, missing authorization, inability to access canonical governance → halt and escalate to CS2/FM as appropriate (`GOVERNANCE_LIAISON_MINIMUM_APPOINTMENT_REQUIREMENTS.md` Section 7; validation report Success Criteria 4 & 5).
- [ ] **Escalation content**: Include scope, canon references, options, and await decision; follow cascading failure + warning blocker protocols for governance incidents (`CASCADING_FAILURE_CIRCUIT_BREAKER.md`, `WARNING_DISCOVERY_BLOCKER_PROTOCOL.md`).
- [ ] **Authority boundaries**: Cannot approve merges; cannot bypass gates; must defer to FM/governance admin on constitutional changes (`governance/baselines/agent-files/governance-liaison.md`, `MERGE_GATE_PHILOSOPHY.md`).

## Category 6 — Prohibitions & Guardrails
- [ ] **No code-build tasks**: Prohibited from implementing code/tests/QA or orchestration; must not change Build Philosophy or Tier-0 artifacts (`GOVERNANCE_LIAISON_MINIMUM_APPOINTMENT_REQUIREMENTS.md` Sections 3.3.1–3.3.4; `governance/baselines/agent-files/governance-liaison.md` constraints).
- [ ] **No self-contract edits** beyond formatting; changes require CS2/governance administrator (`governance/baselines/agent-files/governance-liaison.md` LOCK-LIAISON-SELF-MOD-001).
- [ ] **No cross-repo authority**: May not modify agent contracts or governance in other repos; repository seeding tasks only when authorized (`REPOSITORY_SEEDING_AND_ENFORCEMENT_ROLE_SEPARATION.md`, `AGENT_RECRUITMENT_AND_CONTRACT_AUTHORITY_MODEL.md`).

## Category 7 — Outputs & Deliverables
- [ ] **Initialization artifacts**: Directory scaffolding, governance version files, evidence logs, and PREHANDOVER proof when performing seeding/coupling (`GOVERNANCE_LIAISON_MINIMUM_APPOINTMENT_REQUIREMENTS.md` Section 4.1.1).
- [ ] **Alignment artifacts**: Updated inventories, sync state, ripple inbox/archives, and attestation of self-governance checks (`governance/baselines/agent-files/governance-liaison.md` Pre-Job Self-Governance).
- [ ] **Traceability**: Authorization trail + timestamps for each action; scope/assignment documented per protocol (`GOVERNANCE_LIAISON_MINIMUM_APPOINTMENT_REQUIREMENTS.md` Sections 4–6; validation report evidence lines 20–55).

---

**Usage**: Any unchecked item blocks `governance-liaison-v2.agent.md`. Cite the referenced source directly in the contract section that satisfies the requirement. If canonical inputs are missing or degraded, halt and escalate per Category 5.
