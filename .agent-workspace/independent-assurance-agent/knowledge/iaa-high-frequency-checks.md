# IAA High-Frequency Checks — CI Specification

**Agent**: independent-assurance-agent
**Version**: 1.0.0
**Status**: ACTIVE — Reference Only
**Last Updated**: 2026-04-14
**Authority**: CS2 (Johan Ras / @APGI-cmy)

---

## Purpose

This document lists all mechanical checks that have been moved from the IAA procedure to CI automation as part of the 90/10 evaluation-to-admin restructure (v2.5.0, 2026-04-14). These checks are no longer executed by IAA during invocation — they are enforced by CI gates before IAA is reached.

**This is a reference document, not an executable instruction set.**

---

## Tier: CI Mechanical Checks — Moved from IAA Procedure

---

### HFMC Checks (High-Frequency Mechanical Checks)

**CI Gate**: `preflight-evidence-gate.yml` (`agent-ceremony/artifact-checks` job)

| Check ID | Check Name | Condition |
|----------|-----------|-----------|
| HFMC-01 | PREHANDOVER proof exists | File exists at `.agent-admin/prehandover/` or `.agent-workspace/` |
| HFMC-02 | Session memory file exists | File exists at `.agent-workspace/<agent>/memory/session-*.md` |
| HFMC-03 | Phase 1 preflight field present | `phase_1_preflight: PREFLIGHT COMPLETE` present in session memory |
| HFMC-04 | IAA token file exists | File exists at `.agent-admin/assurance/iaa-token-session-*.md` |
| HFMC-05 | PHASE_B_BLOCKING_TOKEN non-PENDING | `PHASE_B_BLOCKING_TOKEN` line present and not PENDING in IAA token file |
| HFMC-06 | IAA pre-brief exists (foreman PRs) | `iaa-prebrief-wave*.md` exists in `.agent-admin/assurance/` for foreman PRs |

---

### CORE-001 to CORE-012 (YAML Frontmatter Checks)

**CI Gate**: `agent-contract-format-gate.yml` (`agent-contract/format-gate` job)

| Check ID | Check Name | Condition |
|----------|-----------|-----------|
| CORE-001 | YAML frontmatter valid | YAML frontmatter present and parseable (between `---` delimiters) |
| CORE-002 | Agent version correct | `agent.version` present and non-empty |
| CORE-003 | Contract version present | `contract_version` present in semver format |
| CORE-004 | Identity block complete | `identity.role`, `identity.mission`, `identity.class_boundary` all present and non-empty |
| CORE-005 | Governance block present | `governance.protocol`, `governance.version`, `governance.canon_inventory` all present |
| CORE-006 | CANON_INVENTORY alignment | All `expected_artifacts` paths present in repo |
| CORE-007 | No placeholder content | No STUB, TODO, FIXME, TBD in content |
| CORE-008 | Prohibitions block present | `prohibitions` block present with at least one `enforcement: CONSTITUTIONAL` entry |
| CORE-009 | Merge gate interface present | `merge_gate_interface.required_checks` non-empty; `parity_required: true` |
| CORE-010 | Tier 2 knowledge indexed | `tier2_knowledge.index` path present and `index.md` exists at that path |
| CORE-011 | Four-phase structure present | PHASE 1, PHASE 2, PHASE 3, PHASE 4 all present in contract body |
| CORE-012 | Self-modification lock present | `SELF-MOD-*` prohibition with `enforcement: CONSTITUTIONAL` present |

---

### CORE-013, CORE-015, CORE-016, CORE-018, CORE-019 (Artifact Existence Checks)

**CI Gate**: `preflight-evidence-gate.yml` (`agent-ceremony/artifact-checks` job)

| Check ID | Check Name | Condition |
|----------|-----------|-----------|
| CORE-013 | IAA invocation evidence | PREHANDOVER proof or IAA token reference present in PR artifacts |
| CORE-015 | Session memory in PR bundle | Session memory artifact present on branch |
| CORE-016 | IAA token file exists | Dedicated IAA token file at `.agent-admin/assurance/iaa-token-session-NNN-waveY-YYYYMMDD.md` |
| CORE-018 | Complete evidence artifact sweep | PREHANDOVER proof, session memory, IAA token file all present and non-empty |
| CORE-019 | IAA token cross-verification | Token file exists, references current PR, verdict = ASSURANCE-TOKEN |

---

### CERT-001 to CERT-004 (Ceremony Artifact Existence Checks)

**CI Gate**: `preflight-evidence-gate.yml` (`agent-ceremony/artifact-checks` job)

| Check ID | Check Name | Condition |
|----------|-----------|-----------|
| CERT-001 | PREHANDOVER proof exists | PREHANDOVER proof file committed on branch |
| CERT-002 | Session memory exists | Session memory file committed on branch |
| CERT-003 | FAIL-ONLY-ONCE attestation declared | `phase_1_preflight: PREFLIGHT COMPLETE` declared in session memory |
| CERT-004 | IAA audit token field present | `iaa_audit_token` field present in PREHANDOVER proof or dedicated token file exists |

---

## Notes

- IAA does NOT re-execute these checks during invocation. CI enforces them before IAA is reached.
- If a CI gate fails, the producing agent must resolve the failure and re-push before IAA is invoked.
- These checks implement the 10% ceremony-admin layer. IAA's 90% obligation is substantive review.
- For the IAA-retained subset (CORE-020, CORE-021), see `iaa-core-invariants-checklist.md`.

---

**Authority**: CS2 (Johan Ras) | **Contract Version**: 2.5.0 | **CI Restructure**: 2026-04-14
