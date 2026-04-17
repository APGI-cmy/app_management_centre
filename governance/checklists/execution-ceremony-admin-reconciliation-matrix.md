# Execution Ceremony Admin — Reconciliation Matrix

**Version**: 1.0.0  
**Authority**: EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md v1.1.0 (ECAP-001) §3.7 + AGENT_HANDOVER_AUTOMATION.md v1.4.1 §4.3e  
**Effective**: 2026-04-17  
**Owner**: Maturion Engineering Lead  
**Consumer**: execution-ceremony-admin-agent, foreman-v2-agent (§14.6 QP checkpoint)

> **Amendment Authority**: Only CS2 may amend this matrix. Modifications without CS2 sign-off are auto-FAIL at the merge gate.

---

## Purpose

This matrix defines the reconciliation requirements that must be satisfied before the ceremony bundle is returned to the Foreman and before the Foreman may invoke IAA. Each row in this matrix maps a consistency dimension to a source, a verification target, and an action if mismatched.

All rows must show **PASS** before the §4.3e Admin Ceremony Compliance Gate is run.

---

## Matrix Legend

| Status | Meaning |
|--------|---------|
| **PASS** | Verified consistent — no action needed |
| **FAIL** | Inconsistency found — must be resolved before proceeding |
| **N/A** | Not applicable to this job |
| **BLOCKED** | Cannot verify — escalate to Foreman |

---

## R1 — Session Reference Consistency

| Dimension | Source | Verified Against | Required Match |
|-----------|--------|-----------------|----------------|
| Session ID | PREHANDOVER proof `session_id` field | Session memory filename (`session-NNN-YYYYMMDD.md`) | Exact match |
| Session ID | Session memory `session_id` field | Wave record `session_id` | Exact match |
| Session ID | Wave record `section_1` | IAA Pre-Brief `foreman_session` declaration | Exact match |
| Session date | Session memory filename date | PREHANDOVER `date` field | Same date (YYYY-MM-DD) |

**Fail condition**: Any mismatch in session ID or date across the four artifacts → FAIL, ACR-03, ACR-07  
**Resolution**: Correct the mismatched field, recommit, re-verify  

---

## R2 — Token Reference Consistency

| Dimension | Source | Verified Against | Required Match |
|-----------|--------|-----------------|----------------|
| IAA token format | PREHANDOVER `iaa_audit_token` field | Format: `IAA-session-NNN-YYYYMMDD-PASS` | Canonical format per A-015 |
| IAA token path | PREHANDOVER `iaa_audit_token` field | Wave record section 5 `PHASE_B_BLOCKING_TOKEN` | Same session-NNN |
| IAA token path | Wave record section 5 | Actual wave record file at HEAD | Must be committed |

> **Note**: At bundle-return time (before IAA invocation), the token is PENDING. The Foreman populates section 5 after IAA issues the verdict. Check that `iaa_audit_token` in the PREHANDOVER proof is pre-populated with the EXPECTED format, not blank.

**Fail condition**: Blank `iaa_audit_token` in PREHANDOVER proof → FAIL (AAP-01 guard), ACR-02  
**Resolution**: Pre-populate with expected session-based reference before bundle return  

---

## R3 — Issue / PR / Wave Reference Consistency

| Dimension | Source | Verified Against | Required Match |
|-----------|--------|-----------------|----------------|
| Triggering issue | Session memory `triggering_issue` | PREHANDOVER `issue_ref` | Same issue number |
| Wave ID | Session memory `wave_id` | Wave record filename | Same wave slug |
| PR reference | PREHANDOVER `pr_ref` | Wave record `pr_ref` | Same PR number (or "pending" consistently) |
| Branch | PREHANDOVER `branch` | `git rev-parse --abbrev-ref HEAD` | Exact match |

**Fail condition**: Inconsistent issue/PR/wave across artifacts → FAIL, ACR-03, ACR-07  
**Resolution**: Align all references before bundle return  

---

## R4 — Artifact Path Consistency

| Dimension | Source | Verified Against | Required Match |
|-----------|--------|-----------------|----------------|
| PREHANDOVER proof path | PREHANDOVER proof filename | Wave record section 3 `prehandover_path` | Same path |
| Session memory path | Session memory filename | Wave record section 3 `session_memory_path` | Same path |
| Gate results path | Gate results filename | PREHANDOVER `gate_results_path` | Same path |
| ECAP reconciliation path | ECAP summary filename | PREHANDOVER `ecap_reconciliation_path` | Same path |
| Scope declaration path | `governance/scope-declaration.md` | PREHANDOVER `scope_declaration_path` | Same path |
| Each declared path | PREHANDOVER artifact list | `git ls-files --error-unmatch <path>` | File exists on branch |

**Fail condition**: Any path declared but not committed → FAIL, AAP-03, ACR-08  
**Resolution**: Commit missing artifacts, or remove false declarations  

---

## R5 — Version and Hash Consistency

| Dimension | Source | Verified Against | Required Match |
|-----------|--------|-----------------|----------------|
| File version | PREHANDOVER proof `artifacts` table | File header version field | Must match |
| File hash | PREHANDOVER proof `artifacts` table | `sha256sum <file>` on committed file | Must match |
| CANON_INVENTORY version | `governance/CANON_INVENTORY.json` version field | Changed canon files' header versions | Updated versions must be reflected |
| GOVERNANCE_ALIGNMENT_INVENTORY | `governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json` | Changed artifact versions | Inventory entries updated |

**Fail condition**: Hash mismatch or version mismatch after file edits → FAIL, AAP-02, AAP-05, ACR-05  
**Resolution**: Re-record correct hash/version after all file edits are final  

---

## R6 — Scope Declaration Parity

| Dimension | Source | Verified Against | Required Match |
|-----------|--------|-----------------|----------------|
| FILES_CHANGED count | `governance/scope-declaration.md` | `git diff --name-only origin/main...HEAD \| wc -l` | Exact numeric match |
| Changed file list | `governance/scope-declaration.md` | `git diff --name-only origin/main...HEAD` | List subset match (scope may be narrower than total diff if explained) |

**Fail condition**: Declared count ≠ actual diff count → FAIL, AAP-04, ACR-04  
**Resolution**: Update `governance/scope-declaration.md` FILES_CHANGED after final file set is known  

---

## R7 — Final-State Normalization

| Dimension | Check |
|-----------|-------|
| PREHANDOVER proof `final_state` field | Must be `COMPLETE` (not PENDING/IN_PROGRESS) |
| PREHANDOVER proof `status` field | Must not contain `PENDING`, `TODO`, `TBD`, `in progress` |
| Session memory `outcome` field | Must be `COMPLETE` or equivalent (not PENDING) |
| ECAP reconciliation `Final State` | Must be `COMPLETE` |
| Wave record sections 1–4 | No PENDING or IN_PROGRESS in settled fields |

**Fail condition**: Any provisional wording in final-state artifacts → FAIL, AAP-01, ACR-02  
**Resolution**: Normalize all provisional wording before bundle return  

---

## R8 — Ripple / Registry Obligation

| Dimension | Check |
|-----------|-------|
| Changed files with `layer_down_status: PUBLIC_API` in CANON_INVENTORY | Each must have a ripple assessment block in ECAP reconciliation summary C4 |
| No PUBLIC_API files changed | C4 must declare `NOT-APPLICABLE` with reason |
| GOVERNANCE_ALIGNMENT_INVENTORY.json | If governance artifacts were created or updated, inventory must be updated |

**Fail condition**: PUBLIC_API files changed but no ripple assessment → FAIL, AAP-08, ACR-06  
**Resolution**: Complete C4 block in ECAP reconciliation summary  

---

## Resolution Priority

| Severity | Description | Action |
|----------|-------------|--------|
| **BLOCKING** | Any FAIL in rows R1–R8 | Must be resolved before bundle return to Foreman |
| **CRITICAL** | Any AAP anti-pattern present | Must be resolved before §4.3e gate run |
| **WARNING** | Informational inconsistency | Document and explain, Foreman decides |

---

*Matrix Version: 1.0.0 | Authority: ECAP-001 v1.1.0, AGENT_HANDOVER_AUTOMATION.md v1.4.1 | Effective: 2026-04-17*
