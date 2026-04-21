# CodexAdvisor-agent — Session Memory Template

**Agent**: CodexAdvisor-agent
**Version**: 1.1.0
**Last Updated**: 2026-04-21
**Authority**: CS2 (@APGI-cmy)
**Protocol**: CodexAdvisor contract Phase 4 Step 4.3 (live contract, not superseded)
**Governance Ref**: AMC Issue #1068

---

## Purpose

This template defines the session memory structure required by the live CodexAdvisor
contract Phase 4 Step 4.3.

**Usage**: Copy the template below for each new session.
File naming: `session-NNN-YYYYMMDD.md`
Replace all `[...]` values. No field may be left blank — blank required fields are
handover blockers per the live contract.

---

## Template

```markdown
# CodexAdvisor-agent — Session Memory — session-NNN — YYYY-MM-DD

## Session Identity

- `session_id`: CodexAdvisor-session-NNN
- `wave_id`: [wave-slug — e.g. tier2-bootstrap-20260421]
- `date`: [YYYY-MM-DD]
- `phase_1_preflight`: PREFLIGHT COMPLETE
- `triggering_issue`: "[#NNN — title — opened by @APGI-cmy (CS2)]"

## CS2 Authorization Reference

- **Issue**: [issue title or PR title]
- **Opened by**: @APGI-cmy (CS2)
- **Authorization type**: [Issue opened and assigned to CodexAdvisor-agent by CS2 — VALID]

## Prior Sessions Reviewed

| Session | Date | Summary |
|---------|------|---------|
| [session-NNN] | [YYYY-MM-DD] | [one-line summary] |

## Unresolved Carried-Forward Items

- [list, or 'None carried forward']

## Roles Invoked

- [list agent-ids invoked this session, or 'CodexAdvisor-agent (this agent) only']

## Agents Created or Updated

- [list with file paths and version changes, or 'None']

## Delegations or Invocations Made

- [list delegation targets and outcomes, or 'None']

## Escalations Triggered

- [list escalation targets and reasons, or 'None']

## Exact IAA Invocation Result

- `iaa_classification`: [YES / REVIEW / NO]
- `iaa_required`: [YES / NO]
- `iaa_invocation_result`: [ASSURANCE-TOKEN: IAA-session-NNN-YYYYMMDD-PASS / NOT REQUIRED / PENDING]
- `iaa_token_location`: [wave record section 5 path, or 'N/A']

## Improvement Suggestions

- [MANDATORY — never blank. At minimum one concrete suggestion, or: 'No degradation observed. Continuous improvement note: [specific observation].']

## Breach Notes

- [Any breach or near-miss this session, or 'None']

## Session Outcome

- `outcome`: [COMPLETE | PARTIAL | ESCALATED]
- `branch`: [branch name]
- `coverage_summary`: [1-2 sentences: what was delivered this session]
```

---

## Field Definitions

| Field | Required | Blank = handover blocker? |
|-------|----------|--------------------------|
| `session_id` | YES | YES |
| `wave_id` | YES | YES |
| `date` | YES | YES |
| `triggering_issue` | YES | YES |
| CS2 authorization reference | YES | YES |
| prior sessions reviewed | YES | YES |
| unresolved carried-forward items | YES | YES |
| roles invoked | YES | YES |
| agents created or updated | YES | YES |
| delegations or invocations made | YES | YES |
| escalations triggered | YES | YES |
| exact IAA invocation result | YES | YES |
| improvement suggestions | YES | YES |
| breach notes | YES | YES |
| outcome + coverage_summary | YES | YES |

---

## Note on "Blank required fields are handover blockers"

Per CodexAdvisor contract Phase 4 Step 4.3:
> "Blank required fields are handover blockers."

A field is not blank if it states 'None', 'None carried forward', 'Not required', or
provides an explicit negative. A field IS blank if it is empty, omitted, or set to
a placeholder string.

---

*Authority: CS2 (@APGI-cmy) | CodexAdvisor-agent Tier 2 Knowledge*
