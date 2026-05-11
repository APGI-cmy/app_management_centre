# Builder Task Template — Foreman-v2-agent Tier 2 Knowledge

> **Version**: 1.0.0
> **Authority**: CS2 — Issue #1172 (startup-parity fix)
> **Created**: 2026-05-11
> **Purpose**: Standard template Foreman uses when delegating implementation tasks to builder-class agents. Fill in all fields before task delegation. Do not delegate until stages 1–10 of the pre-build model are complete (HALT-008).

---

## Usage

Foreman creates one task record per delegated task and commits it to the wave checklist before invoking the builder agent. This record is the machine-readable contract between Foreman and the builder.

---

## Template

```markdown
## Builder Task: TASK-<WAVE>-<SEQ>

| Field | Value |
|---|---|
| task_id | TASK-<WAVE>-<SEQ> |
| wave_id | wave-<slug>-<YYYYMMDD> |
| governing_issue | #<NNNN> |
| wave_record_path | .agent-admin/wave-records/amc-wave-record-<slug>-<YYYYMMDD>.md |
| delegated_by | foreman-v2-agent |
| assigned_builder | <builder-agent-id> |
| delegation_timestamp | <YYYY-MM-DDTHH:MM:SSZ> |

### Scope

<Single-sentence description of what the builder must deliver.>

### Acceptance Criteria

| AC# | Criterion | Verification Method |
|-----|-----------|---------------------|
| AC-01 | <criterion text> | <how Foreman verifies> |
| AC-02 | <criterion text> | <how Foreman verifies> |

### Artifacts to Produce

- `<path/to/file>` — <description>
- `<path/to/file>` — <description>

### Forced-Ceremony Check

Before accepting the task, builder must confirm:

```bash
git diff --name-only origin/main...HEAD | grep -E "^governance/|^\.github/agents/|^\.governance-pack/|^\.agent-workspace/.*/knowledge/|supabase/migrations/|^schema/|^migrations/|BUILD_PROGRESS_TRACKER"
```

If ANY result: full ceremony required — DO NOT use simple admin.

### Definition of Done (Builder Reports to Foreman)

- [ ] All acceptance criteria met and evidence committed
- [ ] No forced-ceremony paths touched without ceremony in place
- [ ] Session memory updated: `session-<NNN>-<YYYYMMDD>.md` with `fail_only_once_attested: true`
- [ ] QP evaluation ready for Foreman

### Stop Conditions

- Any task touching `.github/agents/**` requires CS2 stop-gate — escalate to Foreman immediately
- Any blocking gate failure: halt and report to Foreman before continuing
```

---

## Builder Agent IDs (from specialist-registry.md)

| ID | Scope |
|---|---|
| `api-builder` | API routes, handlers, business logic |
| `schema-builder` | Database schemas, models, migrations |
| `ui-builder` | React UI components, layouts, wizards |
| `integration-builder` | Inter-module integrations, external connections |
| `qa-builder` | Test suites, QA infrastructure |
| `governance-liaison-amc-agent` | Governance canon layer-downs, ripple PRs |

---

## POLC Boundary Reminder

Foreman PLANS and DELEGATES — the builder IMPLEMENTS. Foreman never writes production code, CI scripts, migrations, or test files. Any task requiring implementation is delegated to the appropriate builder.
