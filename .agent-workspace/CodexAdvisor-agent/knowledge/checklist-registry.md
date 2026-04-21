# CodexAdvisor-agent — Checklist Registry

**Agent**: CodexAdvisor-agent
**Version**: 1.0.0
**Last Updated**: 2026-04-21
**Authority**: CS2 (@APGI-cmy)
**Governance Ref**: AMC Issue #1068, CodexAdvisor contract Phase 2 Step 2.3

---

## Purpose

This registry maps job types to their required QP gate checklists.
CodexAdvisor loads this file in Phase 2 Step 2.3 to identify the correct checklist
for the active job before drafting any artifact.

---

## Job Type Registry

### Job Type: `agent_creation`

**Trigger**: Creating a new `.github/agents/<name>.md` contract file that does not yet exist.

**Required QP Gates**: S1 through S12 — ALL must PASS before file write.

| Gate | Name | Description |
|------|------|-------------|
| S1 | YAML valid | Draft YAML frontmatter parses without error |
| S2 | All four phases present | PHASE 1, 2, 3, 4 all present with correct headings |
| S3 | Size within limit | Draft ≤ 30,000 chars (hard limit); warning at ≥ 25,000 |
| S4 | No unresolved draft markers | No TODO, PLACEHOLDER, TBD, [FILL IN], stub text, or empty required fields |
| S5 | No embedded Tier 2 bulk | No extended examples, tables, or knowledge content in Tier 1 contract |
| S6 | Top-level YAML structure correct | All required top-level keys present; no duplicates |
| S7 | Handover immutability rules present | PREHANDOVER read-only rule present; IAA token in wave record only |
| S8 | IAA final assurance model correct | IAA required; self-approval prohibited; PHASE_B_BLOCKING_TOKEN referenced |
| S9 | Authority and self-modification rules correct | CS2 authority stated; own-file write gated; class boundary explicit |
| S10 | No merge-ready without final IAA PASS | No statement presenting contract as merge-ready without IAA |
| S11 | No operative own-file write path | No code path allowing agent to rewrite its own contract outside CS2 gate |
| S12 | Frontmatter scalars within parser limit | All YAML frontmatter scalar values ≤ 200 characters |

**IAA required**: YES

---

### Job Type: `agent_update`

**Trigger**: Modifying an existing `.github/agents/<name>.md` contract file.

**Required QP Gates**: S1 through S12 — ALL must PASS before file write.

| Gate | Name | Description |
|------|------|-------------|
| S1 | YAML valid | Modified YAML frontmatter parses without error |
| S2 | All four phases present | PHASE 1, 2, 3, 4 all present and structurally intact after edit |
| S3 | Size within limit | Final draft ≤ 30,000 chars (hard limit); warning at ≥ 25,000 |
| S4 | No unresolved draft markers | No TODO, PLACEHOLDER, TBD, [FILL IN], stub text, or empty required fields introduced |
| S5 | No embedded Tier 2 bulk | No extended examples, tables, or knowledge content added to Tier 1 contract |
| S6 | Top-level YAML structure correct | All required top-level keys present; no duplicates; no keys removed |
| S7 | Handover immutability rules present | PREHANDOVER read-only rule present; IAA token in wave record only |
| S8 | IAA final assurance model correct | IAA required; self-approval prohibited; PHASE_B_BLOCKING_TOKEN referenced |
| S9 | Authority and self-modification rules correct | CS2 authority stated; own-file write gated; class boundary explicit |
| S10 | No merge-ready without final IAA PASS | No statement presenting contract as merge-ready without IAA |
| S11 | No operative own-file write path | No code path allowing agent to rewrite its own contract outside CS2 gate |
| S12 | Frontmatter scalars within parser limit | All YAML frontmatter scalar values ≤ 200 characters |

**IAA required**: YES

**Additional check for updates**:
- Confirm version bump (agent.version and metadata.contract_version incremented appropriately)
- Confirm no governance weakening (removed checks, softened rules, relaxed authority)

---

### Job Type: `tier2_only`

**Trigger**: Creating or updating files under `.agent-workspace/<agent>/knowledge/` only.
No `.github/agents/*.md` files modified.

**Required QP Gates**: S1, S3, S4, S5 only.

| Gate | Name | Description |
|------|------|-------------|
| S1 | YAML valid | Any YAML frontmatter in the file parses without error (N/A if no frontmatter) |
| S3 | Size within limit | File is not bloated; content is proportionate to purpose |
| S4 | No unresolved draft markers | No TODO, PLACEHOLDER, TBD, [FILL IN], stub text, or empty required fields |
| S5 | No embedded Tier 2 bulk in Tier 1 | Verify the parent Tier 1 contract was not inadvertently modified |

**IAA required**: REVIEW — classify using `INDEPENDENT_ASSURANCE_AGENT_CANON.md`.
For pure Tier 2 housekeeping with no contract change: IAA typically NOT required.
For Tier 2 changes that materially affect agent behaviour or governance coverage: IAA required.

---

### Job Type: `admin_housekeeping`

**Trigger**: Administrative updates only (e.g., session memory, parking station, breach registry appends).
No `.github/agents/*.md` files modified. No Tier 2 knowledge content modified.

**Required QP Gates**: None.

**IAA required**: NO

**Constraints**:
- Breach registry entries are append-only
- Session memory files must use the current 6-field AMC template
- PREHANDOVER proofs are read-only after initial commit
- No governance content may be altered under this job type classification

---

## Gate Count Summary

| Job Type | Gate Count | IAA Required |
|----------|-----------|--------------|
| agent_creation | 12 (S1–S12) | YES |
| agent_update | 12 (S1–S12) | YES |
| tier2_only | 4 (S1, S3, S4, S5) | REVIEW |
| admin_housekeeping | 0 | NO |

---

*Authority: CS2 (@APGI-cmy) | CodexAdvisor-agent Tier 2 Knowledge*
