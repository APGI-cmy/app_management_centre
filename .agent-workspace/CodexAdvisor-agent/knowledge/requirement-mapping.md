# CodexAdvisor-agent — Requirement Mapping

**Agent**: CodexAdvisor-agent
**Version**: 1.0.0
**Last Updated**: 2026-04-21
**Authority**: CS2 (@APGI-cmy)
**Governance Ref**: AMC Issue #1068, CodexAdvisor contract Phase 3 Step 3.4

---

## Purpose

This file provides traceability from AMC governance requirements to the specific
CodexAdvisor contract sections that enforce them.

CodexAdvisor uses this file to verify coverage during Phase 2 alignment checks and
Phase 3 Step 3.4 (requirement mapping is mandatory per `capabilities.alignment`).

---

## Requirement Mapping Table

| Requirement ID | Requirement Name | Governing Document | Enforcing Contract Section |
|----------------|------------------|--------------------|---------------------------|
| AGCFPP-001 | Agent Contract Factory and Production Policy | `governance/canon/AGENT_CONTRACT_ARCHITECTURE.md` | `capabilities.agent_factory.sole_authority` — CodexAdvisor is the sole writer of `.github/agents/*.md`; `prohibitions.NO-BUILD-001`; `merge_gate_interface.required_checks`; Phase 3 S9 (taxonomy) |
| ECAP-001 | Execution Ceremony Administration Protocol | `governance/canon/EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` | `capabilities.ecap_role_boundary` — governed contracts listed; non-substitution invariants enforced; `can_invoke` and `cannot_invoke` boundaries; Phase 4 Step 4.5 ECAP statement |
| INDEPENDENT_ASSURANCE_AGENT_CANON.md | IAA Canon — independent assurance requirement | `.governance-pack/INDEPENDENT_ASSURANCE_AGENT_CANON.md` | `iaa_oversight` block — required=true; self-approval prohibited; `prohibitions.NO-SELF-APPROVE-001`; `prohibitions.NO-MERGEREADY-WITHOUT-IAA-001`; Phase 4 Step 4.4 IAA invocation |
| GOVERNANCE_ARTIFACT_TAXONOMY.md | Taxonomy of governed artifacts and write scope | `governance/canon/GOVERNANCE_ARTIFACT_TAXONOMY.md` | `scope.write_paths` — declared write scope; `scope.protected_paths`; Phase 3 S9 (taxonomy and write-scope sanity check); `capabilities.alignment.requirement_mapping` = MANDATORY |
| AMC_90_10_ADMIN_PROTOCOL.md | AMC 90/10 Admin Protocol — session memory 6-field model | `governance/protocols/AMC_90_10_ADMIN_PROTOCOL.md` | Session memory uses 6-field AMC model (session_id, wave_id, date, outcome, coverage_summary, learning); `tier2_knowledge.required_files` includes `session-memory-template.md`; Phase 4 Step 4.3 session memory |

---

## Coverage Notes

### AGCFPP-001 Coverage

AGCFPP-001 mandates that all `.github/agents/*.md` modifications go through
CodexAdvisor + IAA. The contract enforces this through:

- `capabilities.agent_factory.sole_authority.prohibited_writers` — lists all agents
  that may not write agent contract files
- `merge_gate_interface.required_checks` — CI gates block non-compliant writes
- `capabilities.agent_factory.sole_authority.ci_enforcement` — CI workflow path
- Phase 3 QP gate S9 — taxonomy and write-scope sanity check before file write

### ECAP-001 Coverage

ECAP-001 defines the three-role split: CodexAdvisor (drafts), ECA (ceremony admin),
IAA (independent assurance). The contract enforces this through:

- `capabilities.ecap_role_boundary.governed_contracts` — lists all governed contracts
- `capabilities.ecap_role_boundary.non_substitution_invariants` — explicit role boundaries
- `cannot_invoke` — CodexAdvisor cannot invoke IAA as a builder task or substitute
- Phase 4 Step 4.5 ECAP statement — required in every PR touching governed contracts

### INDEPENDENT_ASSURANCE_AGENT_CANON.md Coverage

The IAA canon requires independent assurance for all agent contract changes.
The contract enforces this through:

- `iaa_oversight.required: true`
- `iaa_oversight.trigger: all_agent_contract_creations_or_updates`
- `prohibitions.NO-SELF-APPROVE-001` — constitutional prohibition on self-approval
- `prohibitions.NO-MERGEREADY-WITHOUT-IAA-001` — blocking prohibition on merge-ready
  state without final IAA PASS

### GOVERNANCE_ARTIFACT_TAXONOMY.md Coverage

The taxonomy defines what types of artifacts CodexAdvisor may produce and where
they may be written. The contract enforces this through:

- `scope.write_paths` — explicit list of writable paths
- `scope.protected_paths` — paths requiring CS2 authorization
- QP gate S9 — taxonomy check before every file write
- Phase 2 Step 2.7 — governance prerequisite check (Tier 3 canon existence)

### AMC_90_10_ADMIN_PROTOCOL.md Coverage

The 90/10 protocol mandates lean session memory with 6 required fields only.
The contract enforces this through:

- `tier2_knowledge.required_files` includes `session-memory-template.md`
- Phase 4 Step 4.3 references the template for session memory assembly
- The 6-field model eliminates the legacy 18-field ISMS model

---

## Traceability Matrix (Compact)

| Requirement | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|-------------|---------|---------|---------|---------|
| AGCFPP-001 | Step 1.2 (Tier 2 load) | Step 2.7 (prereq check) | Step 3.4 (draft), S9 (QP) | Step 4.5 (PR statement) |
| ECAP-001 | Step 1.1 (identity) | Step 2.4 (IAA class) | S8 (IAA model), S9 (taxonomy) | Step 4.5 (ECAP statement) |
| IAA Canon | Step 1.1 (identity) | Step 2.4 (IAA class) | S8 (IAA model), S10 (no merge-ready) | Step 4.4 (IAA invocation) |
| Taxonomy | Step 1.2 (Tier 2 load) | Step 2.7 (prereq), 2.6 (size) | S5 (no bulk), S9 (taxonomy) | Step 4.1 (bundle) |
| 90/10 Protocol | Step 1.4 (session memory) | — | Step 3.7 (parking station) | Step 4.3 (session memory) |

---

*Authority: CS2 (@APGI-cmy) | CodexAdvisor-agent Tier 2 Knowledge*
