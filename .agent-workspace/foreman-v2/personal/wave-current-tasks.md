# Wave Current Tasks — wave-amc-90-10-complete-alignment

wave: wave-amc-90-10-complete-alignment
agent: foreman-v2-agent
session: session-024
date: 20260414
governance_evidence_path: .agent-admin/wave-records/amc-wave-record-amc-90-10-complete-alignment-20260414.md
governance_evidence_status: CONSOLIDATED_INTO_WAVE_RECORD

## Wave Description

Complete AMC 90/10 operating-model alignment with ISMS standard per Issue #1075.
Deploy live execution-ceremony-admin-agent, update IAA to wave-record token model,
wire Foreman Phase 4 to ceremony-admin delegation, align governance-liaison to wave-record model,
and run cross-contract hardening pass per ECAP-001 and AMC 90/10 Admin Protocol v1.0.0.

## Allowed Artifact Paths

Per AMC 90/10 Admin Protocol v1.0.0, this wave may create/modify:

- `.github/agents/independent-assurance-agent.md`
- `.github/agents/execution-ceremony-admin-agent.md`
- `.github/agents/foreman-v2-agent.md`
- `.github/agents/governance-liaison-amc-agent.md`
- `.agent-workspace/execution-ceremony-admin-agent/knowledge/index.md`
- `.agent-workspace/execution-ceremony-admin-agent/knowledge/ceremony-bundle-checklist.md`
- `.agent-workspace/independent-assurance-agent/knowledge/iaa-high-frequency-checks.md`
- `.agent-admin/wave-records/amc-wave-record-amc-90-10-complete-alignment-20260414.md`
- `.agent-workspace/CodexAdvisor-agent/memory/session-020-20260414.md`
- `.agent-workspace/foreman-v2/memory/session-024-20260414.md`
- `.agent-workspace/foreman-v2/personal/wave-current-tasks.md`

## Task Breakdown

| ID | Task | Agent | Status |
|----|------|-------|--------|
| TASK-90-001 | Update IAA contract to wave-record token model (v2.5.0 → v2.6.0) | CodexAdvisor | [x] COMPLETE |
| TASK-90-002 | Create execution-ceremony-admin-agent.md (v1.0.0 NEW) | CodexAdvisor | [x] COMPLETE |
| TASK-90-003 | Create ECA Tier 2 knowledge (index.md, ceremony-bundle-checklist.md) | CodexAdvisor | [x] COMPLETE |
| TASK-90-004 | Update foreman-v2-agent.md Phase 4 — ceremony-admin delegation (v3.0.1 → v3.1.0) | CodexAdvisor | [x] COMPLETE |
| TASK-90-005 | Update governance-liaison-amc-agent.md — wave-record model (v3.2.0 → v3.3.0) | CodexAdvisor | [x] COMPLETE |
| TASK-90-006 | Update iaa-high-frequency-checks.md — HFMC-04/05 dual-path (v1.0.0 → v1.1.0) | CodexAdvisor | [x] COMPLETE |
| TASK-90-007 | Hardening pass — fix remaining stale PREHANDOVER refs in governance-liaison | foreman-v2 | [x] COMPLETE |
| TASK-90-008 | Create wave record and session memory | foreman-v2 | [x] COMPLETE |

## Status: COMPLETE — IAA ASSURANCE-TOKEN issued (session-040, 2026-04-15) — all 27 checks PASS
