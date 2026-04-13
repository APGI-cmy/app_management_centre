# Wave Current Tasks — wave-amc-admin-90-10

wave: wave-amc-admin-90-10
agent: foreman-v2-agent
session: session-023
date: 20260413
iaa_prebrief_path: .agent-admin/wave-records/amc-wave-record-amc-admin-90-10-20260413.md
iaa_prebrief_status: CONSOLIDATED_INTO_WAVE_RECORD

## Wave Description

Restructure AMC admin artifact/process model to align with 90/10 evaluation-to-admin
principle per Issue #1063. Consolidates legacy multi-file admin model into single
wave-record artifacts, reduces session memory from 18+ fields to 6, creates CI enforcement
for allowed artifact paths, and archives deprecated templates.

## Allowed Artifact Paths

Per AMC 90/10 Admin Protocol v1.0.0, this wave may create/modify:

- `.agent-admin/wave-records/amc-wave-record-*.md`
- `.agent-admin/templates/amc-wave-record-template.md`
- `.agent-admin/archive/**`
- `.agent-workspace/foreman-v2/knowledge/session-memory-template.md`
- `.agent-workspace/foreman-v2/knowledge/index.md`
- `.agent-workspace/foreman-v2/personal/wave-current-tasks.md`
- `.github/workflows/governance-artifact-enforcement.yml`
- `governance/protocols/AMC_90_10_ADMIN_PROTOCOL.md`

## Task Breakdown

| ID | Task | Agent | Status |
|----|------|-------|--------|
| TASK-9010-001 | Create consolidated wave-record template | foreman-v2-agent | COMPLETE |
| TASK-9010-002 | Reduce session memory template to 6-field model | foreman-v2-agent | COMPLETE |
| TASK-9010-003 | Create AMC 90/10 Admin Protocol document | foreman-v2-agent | COMPLETE |
| TASK-9010-004 | Create CI workflow for artifact path enforcement | foreman-v2-agent | COMPLETE |
| TASK-9010-005 | Archive deprecated legacy templates | foreman-v2-agent | COMPLETE |
| TASK-9010-006 | Create wave-records directory with README | foreman-v2-agent | COMPLETE |
| TASK-9010-007 | Update preflight-evidence-gate for wave-record acceptance | foreman-v2-agent | COMPLETE |

## Status: COMPLETE
