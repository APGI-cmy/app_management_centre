# CodexAdvisor-agent — Tier 2 Knowledge Index

**Agent**: CodexAdvisor-agent
**Contract version**: 4.1.0
**Updated**: 2026-04-13
**Purpose**: Tier 2 knowledge index for CodexAdvisor-agent — living agent factory overseer

---

## Required Tier 2 Files

The following 5 files are mandatory per the contract `tier2_knowledge.required_files`:

| # | File | Path | Status |
|---|---|---|---|
| 1 | checklist-registry.md | `.agent-workspace/CodexAdvisor-agent/knowledge/checklist-registry.md` | Required |
| 2 | agent-creation-template.md | `.agent-workspace/CodexAdvisor-agent/knowledge/agent-creation-template.md` | Required |
| 3 | requirement-mapping.md | `.agent-workspace/CodexAdvisor-agent/knowledge/requirement-mapping.md` | Required |
| 4 | session-memory-template.md | `.agent-workspace/CodexAdvisor-agent/knowledge/session-memory-template.md` | Required |
| 5 | agent-file-non-negotiables-checklist.md | `.agent-workspace/CodexAdvisor-agent/knowledge/agent-file-non-negotiables-checklist.md` | Required |

---

## Governance Authority Chain

- **CANON_INVENTORY**: `.governance-pack/CANON_INVENTORY.json`
- **Consumer Registry**: `.governance-pack/CONSUMER_REPO_REGISTRY.json`
- **Gate Requirements**: `.governance-pack/GATE_REQUIREMENTS_INDEX.json`
- **Canon Home**: `APGI-cmy/maturion-foreman-governance`

## Agent Contract Standards

- **Pattern**: `four_phase_canonical` — all agent contracts must follow this pattern
- **Character limit**: 30,000 (hard blocking), 25,000 (warning)
- **QP Gates**: S1–S9 (all must PASS before any file write)
- **IAA trigger**: all agent contract creations or updates

## Session Memory Location

- Path: `.agent-workspace/CodexAdvisor-agent/memory/`
- Pattern: `session-NNN-YYYYMMDD.md`
- Breach registry: `.agent-workspace/CodexAdvisor-agent/memory/breach-registry.md`

## Handover Artifacts

- PREHANDOVER proof: `.agent-workspace/CodexAdvisor-agent/memory/PREHANDOVER-session-NNN-YYYYMMDD.md`
- IAA token: `.agent-admin/assurance/iaa-token-session-NNN-waveY-YYYYMMDD.md`
- Parking station: `.agent-workspace/CodexAdvisor-agent/parking-station/suggestions-log.md`

---

*This index is a living document. Update at the start of each session.*
*Authority: CS2 (@APGI-cmy) | CodexAdvisor-agent Tier 2 Knowledge*
