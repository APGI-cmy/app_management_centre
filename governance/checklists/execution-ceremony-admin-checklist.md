# Execution Ceremony Admin — Operational Checklist

**Version**: 1.0.0  
**Authority**: EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md v1.1.0 (ECAP-001)  
**Effective**: 2026-04-17  
**Owner**: Maturion Engineering Lead  
**Consumer**: execution-ceremony-admin-agent  

> **Amendment Authority**: Only CS2 may amend this checklist. Modifications without CS2 sign-off are auto-FAIL at the merge gate.

---

## Purpose

Operational checklist for the `execution-ceremony-admin-agent` to complete the full ceremony administration cycle for a job. Each item must be verified and ticked before the bundle is returned to the Foreman.

---

## Phase 1 — Receive Job Appointment

- [ ] **ECA-1.1** Receive job appointment from Foreman with: wave/job identifier, artifact scope, task ref list, expected return artifacts
- [ ] **ECA-1.2** Confirm job is substantively complete (builders have delivered, QP PASS recorded) — do NOT start ceremony before substantive readiness
- [ ] **ECA-1.3** Confirm the IAA Pre-Brief is present in wave record section 2 (`.agent-admin/wave-records/amc-wave-record-{wave-slug}-{YYYYMMDD}.md` — per AMC 90/10 Admin Protocol v1.0.0; no standalone iaa-prebrief-*.md file)
- [ ] **ECA-1.4** Record appointment in session memory preamble

---

## Phase 2 — Session Memory Assembly

- [ ] **ECA-2.1** Create or populate session memory at `.agent-workspace/foreman-v2/memory/session-NNN-YYYYMMDD.md`
- [ ] **ECA-2.2** Confirm all 6 mandatory fields are present and non-blank:
  - `session_id`
  - `wave_id`
  - `date`
  - `phase_1_preflight` (must be `PREFLIGHT COMPLETE`)
  - `triggering_issue`
  - `outcome`
- [ ] **ECA-2.3** Confirm `coverage_summary` field is present and describes artifacts delivered
- [ ] **ECA-2.4** Confirm `agents_delegated_to` field lists all delegated agents
- [ ] **ECA-2.5** Confirm `learning` field is non-blank
- [ ] **ECA-2.6** Confirm `wave_record_path` field references the wave record file
- [ ] **ECA-2.7** Verify no provisional wording (`PENDING`, `TODO`, `TBD`, `in progress`) in the session memory

---

## Phase 3 — Wave Record Assembly (Sections 1–4)

- [ ] **ECA-3.1** Create or locate wave record at `.agent-admin/wave-records/amc-wave-record-{wave-slug}-{YYYYMMDD}.md`
- [ ] **ECA-3.2** Section 1 — Job Scope: wave identifier, triggering issue, branch, agents, artifact scope
- [ ] **ECA-3.3** Section 2 — Substantive Evidence: QP PASS evidence, test results, builder handover evidence
- [ ] **ECA-3.4** Section 3 — Administrative Evidence: PREHANDOVER proof path, session memory path, scope declaration path
- [ ] **ECA-3.5** Section 4 — Ripple Assessment: PUBLIC_API files changed → ripple assessed; if none → `NOT-APPLICABLE` declared
- [ ] **ECA-3.6** Section 5 (placeholder) — Assurance Block: `PHASE_B_BLOCKING_TOKEN: PENDING` initially
- [ ] **ECA-3.7** Verify wave record sections 1–4 are committed to HEAD before IAA invocation

---

## Phase 4 — Artifact Inventory Collation

- [ ] **ECA-4.1** List all job artifacts in the completeness table:
  - PREHANDOVER proof
  - Session memory
  - Gate results JSON
  - ECAP reconciliation summary (this session)
  - Scope declaration
  - IAA token file (status: pending at this stage)
- [ ] **ECA-4.2** Verify each listed artifact exists as a committed file on the branch using `git ls-files --error-unmatch`
- [ ] **ECA-4.3** Record any missing artifacts — do NOT proceed if required artifacts are absent

---

## Phase 5 — Checksum and Evidence Collation

- [ ] **ECA-5.1** Compute SHA256 hashes for all committed artifacts listed in the PREHANDOVER proof
- [ ] **ECA-5.2** Compare declared hashes (if any) against computed hashes — flag any mismatch
- [ ] **ECA-5.3** Confirm `iaa_audit_token` field in PREHANDOVER proof is pre-populated (not blank or `PENDING`)
- [ ] **ECA-5.4** Confirm `final_state` field in PREHANDOVER proof is `COMPLETE` (not PENDING/IN_PROGRESS)

---

## Phase 6 — Commit-State Administration

- [ ] **ECA-6.1** Confirm working tree is clean: `git status` shows no unstaged changes
- [ ] **ECA-6.2** Confirm no staged but uncommitted diffs: `git diff --cached` shows nothing
- [ ] **ECA-6.3** Confirm wave record (sections 1–4) is committed at HEAD
- [ ] **ECA-6.4** Confirm session memory is committed at HEAD
- [ ] **ECA-6.5** Confirm all builder evidence artifacts are committed and tracked
- [ ] **ECA-6.6** Record HEAD commit SHA for audit trail

---

## Phase 7 — ECAP Reconciliation Summary

- [ ] **ECA-7.1** Complete the ECAP Reconciliation Summary using template at `governance/templates/execution-ceremony-admin/ECAP_RECONCILIATION_SUMMARY.template.md`
- [ ] **ECA-7.2** Populate C1 (Final-State Declaration) — must be `COMPLETE`
- [ ] **ECA-7.3** Populate C2 (Artifact Completeness Table) — all artifacts listed with presence/committed status
- [ ] **ECA-7.4** Populate C3 (Cross-Artifact Consistency Table) — session ID, token reference, paths all consistent
- [ ] **ECA-7.5** Populate C4 (Ripple Assessment Block) — PUBLIC_API files assessed or `NOT-APPLICABLE` declared
- [ ] **ECA-7.6** Section C5 (Foreman Administrative Readiness Block) — leave blank for Foreman to complete at §14.6 checkpoint
- [ ] **ECA-7.7** Save ECAP reconciliation summary to `.agent-admin/prehandover/ecap-reconciliation-<PR#>.md`
- [ ] **ECA-7.8** Commit the reconciliation summary before returning bundle to Foreman

---

## Phase 8 — Bundle Return to Foreman

- [ ] **ECA-8.1** Prepare bundle summary with:
  - Wave record path
  - Session memory path
  - ECAP reconciliation summary path
  - PREHANDOVER proof path
  - Scope declaration path
  - Open items (if any, with severity — none should be CRITICAL)
- [ ] **ECA-8.2** Confirm all BLOCKING items in the reconciliation matrix (see `execution-ceremony-admin-reconciliation-matrix.md`) are RESOLVED
- [ ] **ECA-8.3** Return bundle summary to Foreman
- [ ] **ECA-8.4** Do NOT invoke IAA — IAA invocation is exclusively Foreman's responsibility

---

## Anti-Pattern Guard (quick-check before bundle return)

Review `governance/checklists/execution-ceremony-admin-anti-patterns.md` and confirm none of AAP-01 through AAP-09 are present in the bundle.

- [ ] AAP-01: No provisional wording in final-state artifacts
- [ ] AAP-02: No mixed version labels for the same artifact
- [ ] AAP-03: No stale artifact path references
- [ ] AAP-04: No stale scope declaration FILE count
- [ ] AAP-05: No stale hashes after file finalization
- [ ] AAP-06: No session ID mismatch between PREHANDOVER and token file
- [ ] AAP-07: No declared count mismatches
- [ ] AAP-08: No PUBLIC_API ripple obligations omitted
- [ ] AAP-09: No committed truth contradicting ceremony claims

---

*Checklist Version: 1.0.0 | Authority: ECAP-001 v1.1.0 | Effective: 2026-04-17*
