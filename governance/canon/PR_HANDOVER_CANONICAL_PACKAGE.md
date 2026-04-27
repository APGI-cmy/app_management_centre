
**Status**: CANONICAL | **Version**: 1.0.0 | **Authority**: CS2
**Date**: 2026-04-27
**Canon ID**: PHCP-001
**Issue**: app_management_centre#1139 — Hardening — PR handover must enforce governing-issue role separation, retire stale handover injectors, and block partial handover state

> **Amendment Authority**: Only CS2 (Johan Ras / repo owner) may amend this canon.
> Any PR modifying this file without CS2 sign-off is auto-FAIL at the merge gate.

---

# PR Handover Canonical Package

## Purpose

This canon is the **single authoritative source** for all AMC PR handover logic. It defines
the PR body schema, governing-issue role mapping, handover bundle requirements, token-carrier
rules, wave checklist retirement rules, tracker/index parity requirements, exception-handling
schema, and the current wave-context source of truth.

**All automation, bots, re-anchor comments, PR openers, and closeout templates MUST derive
from this package**. Hardcoded or drift-prone handover logic in any other file is superseded
by this document.

> **Anti-pattern**: Any automation, canned comment, or template that carries handover
> instructions WITHOUT referencing this package is a stale injector. See
> `STALE_HANDOVER_INJECTOR_RETIREMENT_REGISTER.md` for the audit register.

---

## 1. PR Body Schema (Governance / Admin Waves)

Every PR opened for a governance or admin wave MUST include the following labeled fields in
the PR body. Fields marked MANDATORY may not be blank, N/A, or placeholder.

```markdown
## Governance Handover

| Field                    | Value                                                      |
|--------------------------|------------------------------------------------------------|
| governing_delivery_issue | #NNN — [Issue title]                                       |
| stage_definition_issue   | #NNN or N/A                                                |
| related_hardening_issue  | #NNN or N/A                                                |
| related_harmonization_issue | #NNN or N/A                                             |
| related_oversight_issue  | #NNN or N/A                                                |
| approval_reference       | #NNN or N/A                                                |
| wave_record_path         | .agent-admin/wave-records/amc-wave-record-{slug}-{date}.md |
| wave_checklist_status    | ALL TICKED / [documented exceptions]                       |
| qp_verdict               | PASS                                                       |
| iaa_result               | PHASE_B_BLOCKING_TOKEN: IAA-[session]-[date]-PASS          |
| parity_check_verdict     | PASS                                                       |
| closeout_sweep_verdict   | PASS                                                       |
| pre_pr_blocking_gate     | PASS                                                       |
| entry_condition_status   | NORMAL / EXCEPTION — [see §5 schema]                       |
```

### 1.1 Mandatory vs Conditional Fields

| Field | Requirement |
|-------|-------------|
| `governing_delivery_issue` | MANDATORY — never blank |
| `wave_record_path` | MANDATORY — never blank |
| `wave_checklist_status` | MANDATORY — never blank or PENDING |
| `qp_verdict` | MANDATORY — must be PASS |
| `iaa_result` | MANDATORY — must reference a valid PHASE_B_BLOCKING_TOKEN |
| `parity_check_verdict` | MANDATORY — must be PASS |
| `closeout_sweep_verdict` | MANDATORY — must be PASS |
| `pre_pr_blocking_gate` | MANDATORY — must be PASS |
| `entry_condition_status` | MANDATORY — NORMAL or EXCEPTION with fields per §5 |
| `stage_definition_issue` | Conditional — if stage definition issue differs from delivery issue |
| `related_hardening_issue` | Conditional — cite if a hardening issue directly relates |
| `related_harmonization_issue` | Conditional — cite if a harmonization issue directly relates |
| `related_oversight_issue` | Conditional — cite if an oversight issue directly relates |
| `approval_reference` | Conditional — blank until formal approval is recorded |

---

## 2. Governing-Issue Role Mapping

Every issue referenced in the PR body or artifact chain MUST be classified into exactly one
role. The role determines which field that issue number may populate.

| Role | Allowed Field(s) | May Be `governing_delivery_issue`? |
|------|-----------------|-------------------------------------|
| **Governing Delivery Issue** | `governing_delivery_issue` | ✅ YES — this is the only valid value |
| **Stage Definition Issue** | `stage_definition_issue` | ❌ NO |
| **Approval Reference** | `approval_reference` | ❌ NO |
| **Hardening Issue** | `related_hardening_issue` | ❌ NO |
| **Harmonization Issue** | `related_harmonization_issue` | ❌ NO |
| **Oversight Issue** | `related_oversight_issue` | ❌ NO |

> **Rule**: The governing delivery issue is the issue that authorized and scoped this
> specific wave. Stage definition, hardening, harmonization, and oversight issues are
> cited for traceability only — they MUST NOT replace the governing delivery issue.

See `PR_HANDOVER_ISSUE_ROLE_REGISTRY.md` for the machine-checkable registry schema
that must be embedded in every wave record and PR artifact.

---

## 3. Handover Bundle Requirements

A PR may not be opened as review-ready until the following bundle is complete and committed:

| Bundle Item | Required State |
|-------------|---------------|
| Wave record (sections 1–5) | COMMITTED and complete — path recorded in PR body |
| Wave checklist | All tasks `[x]` or annotated `[~]` with documented reason |
| Pre-PR blocking gate | PASS — all evidence fields populated (see §4) |
| End-of-wave closeout sweep | PASS — per `END_OF_WAVE_CLOSEOUT_SWEEP_CANON.md` §1 and §5 |
| Governing-issue parity check | PASS — per `GOVERNING_ISSUE_PARITY_PROTOCOL.md` §2 |
| Overshadow detection check | CLEAN — per `GOVERNING_ISSUE_PARITY_PROTOCOL.md` §5 |
| Entry-condition status | Declared — NORMAL or EXCEPTION with schema per §5 |
| IAA PHASE_B_BLOCKING_TOKEN | Recorded in wave record section 5 |

---

## 4. Pre-PR Blocking Gate

This gate is a **producer-side prerequisite to PR-open / ready-for-review**. It must pass
before a PR is opened or transitioned to ready-for-review. It is not discoverable by external
review after the fact.

### 4.1 Required Evidence Fields

The following fields MUST be populated in the wave record §3c as a fenced YAML block labelled
`pre_pr_blocking_gate` before QP PASS is declared and before the PR is opened. This fenced
YAML block is required in addition to (not instead of) any existing Markdown table entries in
§3c. Automation and IAA MUST parse the fenced YAML block as the authoritative evidence record:

```yaml
pre_pr_blocking_gate:
  closeout_sweep_performed: "YES"          # YES / FAIL — [reason]
  tracker_header_parity_verified: "PASS"   # PASS / FAIL / N/A — [reason]
  tracker_body_parity_verified: "PASS"     # PASS / FAIL / N/A — [reason]
  wave_checklist_retired_from_kickoff_state: "YES"  # YES / NO — [reason if NO]
  control_surfaces_finalized: "YES"        # YES / PARTIAL — [list incomplete surfaces]
  handover_bundle_self_consistent: "YES"   # YES / NO — [list inconsistencies]
  governing_issue_role_registry_completed: "YES"    # YES / NO
  stale_injector_check_performed: "CLEAN"  # CLEAN / STALE — [list stale injectors found]
  entry_condition_status: "NORMAL"         # NORMAL / EXCEPTION — [see §5]
  operational_sanity_check_performed: "YES / N/A"   # for strategy docs; N/A otherwise
  pre_pr_blocking_gate_verdict: "PASS"     # PASS / FAIL — PASS only if all sub-fields above are YES/PASS/CLEAN
```

### 4.2 Blocking Rule

A PR MUST NOT be opened as review-ready if any of the following are absent or non-pass:
- `closeout_sweep_performed` is not `YES`
- `wave_checklist_retired_from_kickoff_state` is not `YES`
- `control_surfaces_finalized` is not `YES`
- `handover_bundle_self_consistent` is not `YES`
- `governing_issue_role_registry_completed` is not `YES`
- `stale_injector_check_performed` is absent or `STALE`
- `pre_pr_blocking_gate_verdict` is not `PASS`

Partial handover state MUST fail at this gate — not be discovered during external review.

---

## 5. Entry-Condition Exception Schema

When CS2 authorizes a stage to be produced before its normal entry condition is satisfied,
that authorization MUST be recorded explicitly in all artifact surfaces.

See `STAGE_ENTRY_CONDITION_EXCEPTION_CANON.md` for full rules. The schema fields that
MUST appear in the PR body, wave record, and main artifact header when an exception applies:

```yaml
entry_condition_exception:
  normal_entry_condition: "[Description of the normal prerequisite]"
  exception_authorized_by: "CS2 — #NNN [Issue reference or comment URL]"
  exception_scope: "[Exactly which stage entry condition was bypassed]"
  exception_reason: "[Why the exception was granted]"
  parallel_production_authorized: "YES / NO"
  exception_changes_next_stage_gate: "YES — [how] / NO"
  exception_recorded_in_artifact_chain: "YES"
```

When `entry_condition_status: NORMAL`, this block is omitted or recorded as N/A.

---

## 6. Token-Carrier / Evidence-Carrier Rule

### 6.1 Current Token Carrier (Active)

**The wave record is the token carrier.** The PHASE_B_BLOCKING_TOKEN is recorded in:

```
.agent-admin/wave-records/amc-wave-record-{wave-slug}-{YYYYMMDD}.md
```

Specifically in **wave record section 5**, in the format:

```
PHASE_B_BLOCKING_TOKEN: IAA-[session-ID]-[date]-PASS
```

### 6.2 Retired Token Carriers (Prohibited)

The following artifact locations for IAA tokens are **retired and prohibited**:

| Retired Location | Retired By | Current Authority |
|-----------------|------------|-------------------|
| `.agent-admin/assurance/iaa-token-*.md` (standalone file) | AMC 90/10 Protocol — Issue #1063 | Wave record section 5 |
| `PREHANDOVER_PROOF_*.md` token field | AMC 90/10 Protocol — Issue #1063 | Wave record section 5 |
| `.agent-admin/assurance/iaa-prebrief-*.md` | AMC 90/10 Protocol — Issue #1063 | Wave record section 2 |

**No automation or agent may instruct creation of retired token artifacts.**

---

## 7. Wave Checklist Retirement Rule

### 7.1 Retirement Requirements

A wave checklist is considered retired from kickoff state when:
1. All tasks are ticked `[x]` OR marked `[~]` with documented justification
2. No tasks remain in `[ ]` (unchecked) state
3. `qp_verdict` for each task reflects final result (not `PENDING`)
4. The checklist header authority line cites the governing delivery issue

### 7.2 Kickoff-State Items

Kickoff-state text (such as scaffolding `[ ]` items added at wave start that have since
been superseded, scoped out, or merged with other tasks) MUST be explicitly retired:
- Use `[~]` with a documented reason, OR
- Remove entirely if the item was scaffolding-only and never constituted a real deliverable

**A PR opened with wave checklist tasks still in `[ ]` PENDING state violates this rule.**

---

## 8. Tracker / Index Parity Requirements

Build progress trackers and artifact indexes are first-class wave deliverables. They MUST
be updated as part of the wave — not as post-merge cleanup.

| Requirement | Detail |
|------------|--------|
| Tracker header reflects governing delivery issue | `Issue:` field matches `governing_delivery_issue` |
| Tracker body stage rows match stage detail sections | No inconsistency between summary status and detail status |
| Artifact index governing-issue reference matches tracker | Same issue number in both |
| Tracker and index updated at wave close | Not deferred to a future wave |

See `END_OF_WAVE_CLOSEOUT_SWEEP_CANON.md` §2 for tracker header/body parity binary gate details.

---

## 9. Wave-Context Source of Truth

The **current** wave-context source of truth is the wave record:

```
.agent-admin/wave-records/amc-wave-record-{wave-slug}-{YYYYMMDD}.md
```

This file supersedes all earlier separate artifacts (prebrief, token, rejection, session memory,
PREHANDOVER proof) as the single per-wave authority. See `AMC_90_10_ADMIN_PROTOCOL.md` §2
for the full replacement mapping.

---

## 10. Automation / Template Compliance Rule

Any automation, bot comment, re-anchor comment, PR opener, or closeout template that instructs
an agent to perform handover MUST:

1. Reference this package (`PR_HANDOVER_CANONICAL_PACKAGE.md` / PHCP-001) as its authority
2. Not contain hardcoded handover logic that contradicts this package
3. Not reference any retired artifact location listed in §6.2
4. Not instruct creation of any artifact type superseded by the wave record model

If an automation file contains logic that contradicts this package, it is a **stale injector**.
Record it in `STALE_HANDOVER_INJECTOR_RETIREMENT_REGISTER.md` and correct or retire it.

---

## Appendix A: Cross-Reference to Related Canons

| Concern | Governing Canon |
|---------|----------------|
| Issue-role registry and machine-checkable schema | `PR_HANDOVER_ISSUE_ROLE_REGISTRY.md` |
| Governing-issue parity across artifact chain | `GOVERNING_ISSUE_PARITY_PROTOCOL.md` (GIPC-001) |
| End-of-wave closeout sweep definition | `END_OF_WAVE_CLOSEOUT_SWEEP_CANON.md` (EWCS-001) |
| Stale injector audit register | `STALE_HANDOVER_INJECTOR_RETIREMENT_REGISTER.md` |
| Entry-condition exception rules | `STAGE_ENTRY_CONDITION_EXCEPTION_CANON.md` |
| Literal implementation sanity-check | `OPERATIONAL_STRATEGY_SANITY_CHECK_PROTOCOL.md` |
| Wave record model and 90/10 principle | `AMC_90_10_ADMIN_PROTOCOL.md` |
| Token ceremony | `INDEPENDENT_ASSURANCE_AGENT_CANON.md` |
| ECAP ceremony administration | `EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` |

---

**Canon ID**: PHCP-001
**Filed by**: foreman-v2-agent (POLC-Orchestration governance specification) | **Date**: 2026-04-27
**Authority**: CS2 — Issue #1139
**See also**: All canons listed in Appendix A
