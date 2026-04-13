# AMC Wave Record — [wave-slug] — [YYYY-MM-DD]

> **Template Version**: 1.0.0
> **Authority**: CS2 (@APGI-cmy) — Issue #1063
> **Protocol**: AMC 90/10 Admin Protocol v1.0.0

---

## 1. Wave Identity

| Field | Value |
|-------|-------|
| wave_id | [wave-slug] |
| date | [YYYY-MM-DD] |
| agent | [agent-id] |
| session_id | [session-NNN] |
| branch | [branch-name] |
| triggering_issue | [#NNN — title] |
| cs2_authorization | [source — issue/comment link] |

## 2. Scope & Classification

| Field | Value |
|-------|-------|
| wave_verb | [verb from request] |
| classification | [POLC-Orchestration / Implementation Guard / Quality Professor] |
| architecture_ref | [path to frozen architecture, or N/A] |
| allowed_artifact_paths | [list of paths this wave may create/modify] |

## 3. Evaluation Summary

| Check | Result |
|-------|--------|
| Tests 100% GREEN | [✅ / ❌ — detail] |
| Zero skipped/stub tests | [✅ / ❌] |
| Zero test debt | [✅ / ❌] |
| Architecture followed | [✅ / ❌] |
| Zero deprecation warnings | [✅ / ❌] |
| Zero linter warnings | [✅ / ❌] |

**QP Verdict**: [PASS / FAIL]

## 4. Outcome & Learning

| Field | Value |
|-------|-------|
| outcome | [COMPLETE / PARTIAL / ESCALATED] |
| coverage_summary | [what was delivered — 1-2 sentences] |
| learning | [key lesson — mandatory, never blank] |

## 5. Assurance

| Field | Value |
|-------|-------|
| iaa_verdict | [PASS / STOP-AND-FIX / ESCALATE / N/A] |
| iaa_token_ref | [token reference, or N/A] |
| merge_gate_parity | [PASS / FAIL] |

## 6. Failure Trail (if applicable)

> Only populate if QP FAIL, IAA STOP-AND-FIX, or merge gate failure occurred.
> This section replaces the legacy standalone rejection/failure files.

- **Failure type**: [QP FAIL / IAA STOP-AND-FIX / MERGE GATE FAIL]
- **Details**: [specific failures]
- **Remediation**: [actions taken]
- **Resolution**: [RESOLVED / PENDING]

---

**Filed by**: [agent-id] | **Date**: [YYYY-MM-DD]
