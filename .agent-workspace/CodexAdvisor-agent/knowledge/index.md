# CodexAdvisor-agent — Tier 2 Knowledge Index

**Agent**: CodexAdvisor-agent
**Version**: 1.0.0
**Created**: 2026-04-06 (session-010-20260406)
**Purpose**: Tier 2 knowledge index for CodexAdvisor-agent — living agent factory overseer

---

## Top-Level Knowledge References

### 1. Governance Authority Chain

- **CANON_INVENTORY**: `.governance-pack/CANON_INVENTORY.json` — 157 canon entries, version 1.0.0
- **Consumer Registry**: `.governance-pack/CONSUMER_REPO_REGISTRY.json`
- **Gate Requirements**: `.governance-pack/GATE_REQUIREMENTS_INDEX.json`
- **Canon Home**: `APGI-cmy/maturion-foreman-governance`

### 2. Agent Contract Standards

- **Pattern**: `four_phase_canonical` — all agent contracts must follow this pattern
- **Character limit**: 30,000 (hard blocking), 25,000 (warning)
- **QP Gates**: S1–S8 (all must PASS before any file write)
- **IAA trigger**: all agent contract creations or updates

### 3. Known Agents in AMC

| Agent ID | Class | File |
|---|---|---|
| CodexAdvisor-agent | overseer | `.github/agents/CodexAdvisor-agent.md` |
| foreman-v2-agent | supervisor | `.github/agents/foreman-v2-agent.md` |
| governance-liaison-amc-agent | liaison | `.github/agents/governance-liaison-amc-agent.md` |
| independent-assurance-agent | assurance | `.github/agents/independent-assurance-agent.md` |
| ui-builder | builder | `.github/agents/ui-builder.md` |
| api-builder | builder | `.github/agents/api-builder.md` |
| schema-builder | builder | `.github/agents/schema-builder.md` |
| integration-builder | builder | `.github/agents/integration-builder.md` |
| qa-builder | builder | `.github/agents/qa-builder.md` |

### 4. Session Memory Location

- Path: `.agent-workspace/CodexAdvisor-agent/memory/`
- Pattern: `session-NNN-YYYYMMDD.md`
- Breach registry: `.agent-workspace/CodexAdvisor-agent/memory/breach-registry.md`

### 5. Handover Artifacts

- PREHANDOVER proof: `.agent-workspace/CodexAdvisor-agent/memory/PREHANDOVER-session-NNN-YYYYMMDD.md`
- IAA token: `.agent-admin/assurance/iaa-token-session-NNN-waveY-YYYYMMDD.md`
- Parking station: `.agent-workspace/CodexAdvisor-agent/parking-station/suggestions-log.md`

### 6. Session History

| Session | Date | Task |
|---|---|---|
| session-004 | 2026-02-11 | (see session file) |
| session-005 | 2026-02-12 | (see session file) |
| session-006 | 2026-02-12 | (see session file) |
| session-007 | 2026-02-17 | (see session file) |
| session-008 | 2026-02-17 | Governance Liaison LAS v6.2.0 alignment |
| session-009 | 2026-04-06 | foreman-v2-agent AMC alignment |
| session-010 | 2026-04-06 | CANON_INVENTORY.json governance pack sync |
| session-011 | 2026-04-07 | .github/agents/ cleanup — archive extraneous files, metadata reduction |
| session-012 | 2026-04-07 | Upgrade all builder agent contracts to v3.4.0 pattern (AMC) |
| session-013 | 2026-04-07 | Foreman v2 Tier 2 knowledge layer-down from maturion-isms (FAIL-ONLY-ONCE v4.1.0, prehandover-template v1.7.0, wave-reconciliation-checklist v1.0.0, domain-flag-index v1.0.0) |

---

*This index is a living document. Update at the start of each session.*
*Authority: CS2 (@APGI-cmy) | CodexAdvisor-agent Tier 2 Knowledge*
