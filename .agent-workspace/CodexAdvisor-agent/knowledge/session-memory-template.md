# CodexAdvisor-agent — Session Memory Template

**Agent**: CodexAdvisor-agent
**Version**: 1.0.0
**Last Updated**: 2026-04-21
**Authority**: CS2 (@APGI-cmy)
**Protocol**: AMC 90/10 Admin Protocol v1.0.0
**Governance Ref**: AMC Issue #1068, AMC Issue #1063

---

## Purpose

This template defines the 6-field AMC session memory model for CodexAdvisor.

Supersedes: legacy 18-field ISMS model (archived per AMC Issue #1063).

**Usage**: Copy the template below for each new session.
File naming: `session-NNN-YYYYMMDD.md`
Replace all `[...]` values. No field may be left blank.

---

## 90/10 Principle

Session memory captures only what is needed for real audit, traceability, and learning.
Ceremony fields removed. Detailed wave evidence is recorded in the consolidated
`amc-wave-record-{wave-slug}-{YYYYMMDD}.md` instead.

---

## Template

```markdown
# CodexAdvisor-agent — Session Memory — session-NNN — YYYY-MM-DD

session_id: CodexAdvisor-session-NNN
wave_id: [wave-slug — e.g. tier2-bootstrap-20260421]
date: [YYYY-MM-DD]
outcome: [COMPLETE | PARTIAL | ESCALATED]
coverage_summary: "[What was delivered this session — 1-2 sentences. Never blank.]"
learning: "[Key lesson or improvement note — mandatory, never blank. If no degradation observed: state 'No degradation observed. Continuous improvement note: [specific observation].'"]
```

---

## Field Definitions

| Field | Required | Rules |
|-------|----------|-------|
| `session_id` | YES | Format: `CodexAdvisor-session-NNN` — sequential number |
| `wave_id` | YES | Slug identifying the wave or job — e.g. `tier2-bootstrap-20260421` |
| `date` | YES | ISO 8601 date: `YYYY-MM-DD` |
| `outcome` | YES | One of: `COMPLETE`, `PARTIAL`, `ESCALATED` |
| `coverage_summary` | YES | 1-2 sentences: what was delivered or evaluated. Never blank. |
| `learning` | YES | Key lesson from the session. Never blank. Minimum: "No degradation observed. Continuous improvement note: [observation]." |

---

## Removed Fields (Legacy 18-Field Model)

The following fields are NOT used in the 6-field AMC model (removed per AMC Issue #1063):

- agent_version, contract_version
- fail_only_once_attested, fail_only_once_version, unresolved_breaches
- wave_verb, wave_classification
- implementation_guard_triggered
- prior_sessions_reviewed, unresolved_items_from_prior_sessions
- roles_invoked, mode_transitions, escalations_triggered
- separation_violations_detected
- iaa_prebrief_artifact, iaa_prebrief_wave, iaa_prebrief_tasks_count, iaa_final_audit_token
- QP Verdicts, Parking Station

These fields are captured in wave-record artifacts if needed.

---

## Example

```markdown
# CodexAdvisor-agent — Session Memory — session-027 — 2026-04-21

session_id: CodexAdvisor-session-027
wave_id: tier2-bootstrap-20260421
date: 2026-04-21
outcome: COMPLETE
coverage_summary: "All 6 required Tier 2 knowledge files created for CodexAdvisor-agent. index.md updated to PRESENT status for all files."
learning: "Tier 2 knowledge files must be bootstrapped in the same wave as the contract that declares them required. Delayed bootstrap creates recurring HALT-005 bypass exemptions that accumulate as technical debt."
```

---

*Authority: CS2 (@APGI-cmy) | CodexAdvisor-agent Tier 2 Knowledge*
