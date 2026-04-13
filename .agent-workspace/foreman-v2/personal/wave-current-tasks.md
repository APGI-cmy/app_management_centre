# Wave Current Tasks — layer-down-404c78fa

wave: layer-down-404c78fa
agent: foreman-v2-agent (orchestration) + governance-liaison-amc (execution)
session: session-023
date: 20260413
iaa_prebrief_path: .agent-admin/assurance/iaa-prebrief-layer-down-404c78fa.md
iaa_prebrief_status: COMMITTED

## Wave Description

Layer-down propagation for canonical commit `404c78fa15ba6cc82d65132086e3d04ea70c400f`
from `APGI-cmy/maturion-foreman-governance`.

Changed canonical file: `.github/agents/foreman-v2.agent.md`
Consumer file: `.github/agents/foreman-v2-agent.md`
Change: foreman-v2 canonical contract v2.8.0 → v3.0.0 (size reduction + strengthened pattern alignment)
Consumer action: UPDATE agent contract file — CS2 APPROVAL REQUIRED

## Task Breakdown

| ID | Task | Agent | Status |
|----|------|-------|--------|
| TASK-LD-404C-001 | Fetch canonical foreman-v2 contract (v3.0.0) from commit 404c78fa | governance-liaison-amc | COMPLETE |
| TASK-LD-404C-002 | Update consumer copy at .github/agents/foreman-v2-agent.md | governance-liaison-amc | COMPLETE |
| TASK-LD-404C-003 | Resolve merge conflict in sync_state.json | governance-liaison-amc | COMPLETE |
| TASK-LD-404C-004 | Update sync_state.json with new canonical commit | governance-liaison-amc | COMPLETE |
| TASK-LD-404C-005 | Create/update GOVERNANCE_ALIGNMENT_INVENTORY.json | governance-liaison-amc | COMPLETE |
| TASK-LD-404C-006 | Create ripple archive entry for 404c78fa | governance-liaison-amc | COMPLETE |
| TASK-LD-404C-007 | Session memory + PREHANDOVER proof | foreman-v2-agent | IN PROGRESS |
| TASK-LD-404C-008 | IAA audit (PHASE_B_BLOCKING) | independent-assurance-agent | PENDING |

## Agent File Guard

TRIGGERED: `.github/agents/foreman-v2-agent.md` is an agent contract file.
CS2 approval required. PR must be DRAFT. Only CS2 may merge.

## Status: IN PROGRESS
