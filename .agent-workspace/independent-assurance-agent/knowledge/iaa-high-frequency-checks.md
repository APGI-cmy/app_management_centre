# IAA High-Frequency Checks — CI Specification

**Agent**: independent-assurance-agent
**Version**: 1.3.0
**Status**: ACTIVE — Reference Only
**Last Updated**: 2026-04-19
**Authority**: CS2 (Johan Ras / @APGI-cmy)

> **Note (v1.1.0)**: CI already implements the dual-path check for HFMC-04 and HFMC-05 — accepting both the legacy standalone token file (pre-90/10 waves) and the wave-record model (post-90/10 waves). The checks below reflect the updated dual-path behaviour.

> **Note (v1.2.0)**: Standalone iaa-prebrief-*.md is DEPRECATED per AMC 90/10 Admin Protocol v1.0.0. For all post-90/10 waves, wave record section 2 is the SOLE pre-brief carrier. HFMC-06 CI check enforces wave-record section 2 population; standalone pre-brief files are no longer accepted for new waves.

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
| HFMC-04 | IAA assurance carrier exists | Wave record with `PHASE_B_BLOCKING_TOKEN` exists at `.agent-admin/wave-records/amc-wave-record-*.md` (section 5). Legacy path `.agent-admin/assurance/iaa-token-session-*.md` accepted for pre-90/10 waves only. |
| HFMC-05 | PHASE_B_BLOCKING_TOKEN non-PENDING | `PHASE_B_BLOCKING_TOKEN` line present, non-PENDING, non-empty in wave record section 5 (or legacy token file for pre-90/10 waves) |
| HFMC-06 | IAA pre-brief exists (foreman PRs) | Wave record section 2 (`## Section 2 — Pre-Brief Scope`) is populated with substantive pre-brief content for foreman PRs. Legacy path `.agent-admin/assurance/iaa-prebrief-wave*.md` is deprecated per AMC 90/10 Admin Protocol v1.0.0 — wave record section 2 is the sole pre-brief carrier. |
| HFMC-07 | Gate set explicitly identified | Wave record Section 3 (Evaluation Summary) lists all required gates from `merge_gate_interface.required_checks` by name with per-gate final state (PASS/FAIL/N/A). Generic "all gates pass" without individual gate names is a FAIL condition for ACR-09. |

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
| CORE-016 | IAA assurance token in wave record | Wave record section 5 (`PHASE_B_BLOCKING_TOKEN`) is present, non-empty, and non-PENDING. Standalone `.agent-admin/assurance/iaa-token-session-NNN-waveY-YYYYMMDD.md` is deprecated per AMC 90/10 Admin Protocol v1.0.0. |
| CORE-018 | Complete evidence artifact sweep | PREHANDOVER proof, session memory, and wave record with `PHASE_B_BLOCKING_TOKEN` (section 5) all present and non-empty |
| CORE-019 | IAA token cross-verification | `PHASE_B_BLOCKING_TOKEN` in wave record section 5 references current PR session, verdict = ASSURANCE-TOKEN |

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
