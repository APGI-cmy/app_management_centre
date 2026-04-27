
**Status**: CANONICAL | **Version**: 1.0.0 | **Authority**: CS2
**Date**: 2026-04-27
**Canon ID**: SHIRR-001
**Issue**: app_management_centre#1139 — Hardening — PR handover must enforce governing-issue role separation, retire stale handover injectors, and block partial handover state

> **Amendment Authority**: Only CS2 (Johan Ras / repo owner) may amend this canon.
> Any PR modifying this file without CS2 sign-off is auto-FAIL at the merge gate.

---

# Stale Handover Injector Retirement Register

## Purpose

This register audits all PR-handover injection sources (bot comments, canned Copilot
instructions, token-ceremony references, wave-close prompts, and PR templates) and records:
- Which injection sources are **current** (aligned with the live AMC handover model)
- Which are **stale** (reference retired artifact locations, obsolete ceremony protocols,
  or deprecated token behavior)
- What the **current canonical equivalent** is for each retired element

**Rule**: No automation may continue instructing the agent to use a retired mechanism
if the live canon designates a replacement. A stale injector that contradicts the live
canon is a governance defect that must be corrected or retired before it can fire on
a live PR.

---

## 1. Live AMC Handover Model (Authority Reference)

The current handover model is defined by:

| Canon | ID | Governs |
|-------|----|---------|
| `PR_HANDOVER_CANONICAL_PACKAGE.md` | PHCP-001 | PR body schema, token carrier, bundle requirements, pre-PR blocking gate |
| `PR_HANDOVER_ISSUE_ROLE_REGISTRY.md` | PHIRR-001 | Machine-checkable issue-role registry schema |
| `END_OF_WAVE_CLOSEOUT_SWEEP_CANON.md` | EWCS-001 | End-of-wave closeout sweep, tracker parity, kickoff-state retirement |
| `GOVERNING_ISSUE_PARITY_PROTOCOL.md` | GIPC-001 | Governing-issue parity and overshadow detection |
| `STAGE_ENTRY_CONDITION_EXCEPTION_CANON.md` | SECC-001 | Entry-condition exception handling |
| `OPERATIONAL_STRATEGY_SANITY_CHECK_PROTOCOL.md` | OSSCP-001 | Literal implementation sanity-check for strategy docs |
| `AMC_90_10_ADMIN_PROTOCOL.md` | — | Wave record model, retired artifact list |
| `AGENT_HANDOVER_AUTOMATION.md` | — | Phase 4 handover automation structure |

---

## 2. Retired Artifact Locations

The following artifact locations have been retired and MUST NOT be used by any automation:

| Retired Artifact Pattern | Retired By | Retirement Issue | Current Replacement |
|--------------------------|------------|-----------------|---------------------|
| `.agent-admin/assurance/iaa-token-session-*.md` | AMC 90/10 Protocol | #1063 | Wave record section 5 (`PHASE_B_BLOCKING_TOKEN`) |
| `.agent-admin/assurance/iaa-prebrief-wave-*.md` | AMC 90/10 Protocol | #1063 | Wave record section 2 (IAA Pre-Brief) |
| `.agent-admin/assurance/iaa-rejection-*.md` | AMC 90/10 Protocol | #1063 | Wave record failure trail section (inline) |
| `PREHANDOVER_PROOF_*.md` (standalone root files) | AMC 90/10 Protocol | #1063 | Wave record evaluation section |
| `.agent-workspace/*/memory/session-*.md` (full) | AMC 90/10 Protocol | #1063 | Wave record session outcome section (6-field) |

---

## 3. Injector Audit Register

### 3.1 `.github/workflows/foreman-reanchor.yml`

| Item | Pre-Hardening State | Post-Hardening State | Status |
|------|---------------------|---------------------|--------|
| Token ceremony reference (obligation item 2) | Referenced `.agent-admin/assurance/iaa-token-*.md` as token location | Updated to wave record section 5 | ✅ CORRECTED — Issue #1139 |
| IAA invocation reference | Referenced "PREHANDOVER proof + session memory + evidence bundle" | Updated to "wave record path + session memory path + evidence bundle" | ✅ CORRECTED — Issue #1139 |
| Pre-PR blocking gate check | Absent | Added as obligation item 4 per PHCP-001 §4 | ✅ ADDED — Issue #1139 |

**Current Status**: COMPLIANT with live handover model.

### 3.2 `.github/workflows/iaa-prebrief-inject.yml`

| Item | Pre-Hardening State | Post-Hardening State | Status |
|------|---------------------|---------------------|--------|
| Idempotency guard (PR target) | Checked `.agent-admin/assurance/iaa-prebrief-*.md` for pre-brief existence | Updated to check wave record section 2 | ✅ CORRECTED — Issue #1139 |
| Idempotency guard (push/bash) | Checked `iaa-prebrief-wave-${WAVE_NUM}.md` existence | Updated to check wave records dir | ✅ CORRECTED — Issue #1139 |
| Injected comment step 2 (push) | `Wait for IAA to publish: .agent-admin/assurance/iaa-prebrief-wave${N}.md` | Updated to wave record section 2 | ✅ CORRECTED — Issue #1139 |
| Injected comment step 2 (issue_comment) | `Commit Pre-Brief to: .agent-admin/assurance/iaa-prebrief-wave${N}.md` | Updated to wave record section 2 | ✅ CORRECTED — Issue #1139 |
| Injected comment step 2 (pull_request_target) | `Commit: .agent-admin/assurance/iaa-prebrief-wave${N}.md` | Updated to wave record section 2 | ✅ CORRECTED — Issue #1139 |
| governance-watchdog Gap 2 reference | Referenced old prebrief artifact path in warning | Removed stale reference | ✅ CORRECTED — Issue #1139 |

**Current Status**: COMPLIANT with live handover model.

### 3.3 `.github/agent-templates/PREHANDOVER_PROOF_TEMPLATE.md`

| Item | State | Status |
|------|-------|--------|
| Standalone PREHANDOVER proof template | Still present as a template | ⚠️ LEGACY — superseded by wave record model (Issue #1063). Template retained for reference only. MUST NOT be used as the primary ceremony artifact. |
| `iaa_token_file` field | Points to `.agent-admin/assurance/iaa-token-*.md` | ⚠️ STALE REFERENCE — token now in wave record section 5. |

**Remediation**: This template has been superseded by:
- `governance/templates/execution-ceremony-admin/PREHANDOVER.template.md` (for ECAP-involved jobs)
- `.agent-admin/templates/amc-wave-record-template.md` (primary per-wave artifact)

### 3.4 `.github/PULL_REQUEST_TEMPLATE.md`

| Item | State | Status |
|------|-------|--------|
| Governance handover fields | Not present (general code PR template) | ℹ️ N/A — general code PR template. For governance/admin waves, use the governance PR body schema in PHCP-001 §1. |

**Current Status**: The PR template is a code PR template. Governance/admin PRs MUST use the governance handover schema from `PR_HANDOVER_CANONICAL_PACKAGE.md` §1 as a supplement or alternative body.

### 3.5 Agent Contracts (`.github/agents/`)

| Agent | Item | State | Status |
|-------|------|-------|--------|
| `foreman-v2-agent.md` | Phase 4 §4.5 Token Ceremony | References wave record section 5 (corrected in earlier work) | ✅ CURRENT |
| `execution-ceremony-admin-agent.md` | Token artifact reference | Contains both old and new references (mixed state) | ⚠️ REVIEW REQUIRED |
| `independent-assurance-agent.md` | Pre-Brief output location | May still reference old `.agent-admin/assurance/iaa-prebrief-*.md` | ⚠️ REVIEW REQUIRED |
| Builder agents (`ui-builder`, `api-builder`, etc.) | Token/prebrief references | Generally builder-role — do not generate ceremony artifacts | ✅ N/A |

> **Note**: Agent contract amendments require CodexAdvisor-agent authority (SELF-MOD-FM-001).
> Flagged agent contracts should be escalated to CodexAdvisor-agent for SELF-MOD-free amendment.

### 3.6 `governance/canon/AGENT_HANDOVER_AUTOMATION.md`

| Item | State | Status |
|------|-------|--------|
| §4.3b Token Update Ceremony | References `iaa-token-session-${IAA_SESSION}-wave${WAVE}-${TIMESTAMP}.md` as token file | ⚠️ STALE — token now in wave record section 5 (AMC 90/10 Protocol #1063). This is a known mixed state: AGENT_HANDOVER_AUTOMATION.md v1.7.2 predates AMC 90/10 consolidation. |

**Remediation Required**: `AGENT_HANDOVER_AUTOMATION.md` §4.3b needs amendment to reflect that AMC repositories use wave record section 5 as the token carrier. This amendment requires a separate CS2-authorized wave.

---

## 4. Known Outstanding Stale Injectors (Requires Follow-On Wave)

The following stale injectors were identified but require a separate CS2-authorized wave
to correct (they are in files requiring elevated amendment authority):

| File | Stale Element | Replacement | Required Action |
|------|--------------|-------------|-----------------|
| `governance/canon/AGENT_HANDOVER_AUTOMATION.md` §4.3b | Standalone `iaa-token-*.md` template script | Wave record section 5 | CS2-authorized amendment wave |
| `.github/agents/execution-ceremony-admin-agent.md` | Mixed old/new token references | Wave record section 5 | CodexAdvisor-agent amendment |
| `.github/agents/independent-assurance-agent.md` | Pre-Brief output to `.agent-admin/assurance/iaa-prebrief-*.md` | Wave record section 2 | CodexAdvisor-agent amendment |
| `governance/protocols/AMC_90_10_ADMIN_PROTOCOL.md` §2.2 | Template reference to `.agent-admin/templates/amc-wave-record-template.md` | Verify template exists | Verify or create template |

---

## 5. Anti-Pattern Detection Rules

An injection source is a **stale injector** if it instructs an agent to:

1. Create a standalone `iaa-token-session-*.md` file in `.agent-admin/assurance/`
2. Create a standalone `iaa-prebrief-wave-*.md` file in `.agent-admin/assurance/`
3. Create a standalone `iaa-rejection-*.md` file in `.agent-admin/assurance/`
4. Create a standalone `PREHANDOVER_PROOF_*.md` file in the repo root
5. Reference `PHASE_B_BLOCKING_TOKEN` as being in a standalone assurance file
6. Skip the pre-PR blocking gate fields from PHCP-001 §4
7. Skip the issue-role registry from PHIRR-001
8. Skip the end-of-wave closeout sweep fields from EWCS-001 §5

If an automation file contains any of the above patterns, it MUST be corrected before
it can fire on a live PR.

---

## 6. Maintenance Obligation

This register MUST be updated:
- Any time a new bot comment, workflow, or template is added that contains handover instructions
- Any time the live handover model changes (new canon or canon amendment)
- Any time a stale injector is corrected (mark as CORRECTED with issue reference)
- At minimum, every time a wave is completed that involved a handover failure traceable
  to stale injection guidance

**Custodian**: foreman-v2-agent | **Authority**: CS2 — Issue #1139

---

**Canon ID**: SHIRR-001
**Filed by**: foreman-v2-agent (POLC-Orchestration governance specification) | **Date**: 2026-04-27
**Authority**: CS2 — Issue #1139
**See also**: `PR_HANDOVER_CANONICAL_PACKAGE.md` (PHCP-001), `AMC_90_10_ADMIN_PROTOCOL.md`
