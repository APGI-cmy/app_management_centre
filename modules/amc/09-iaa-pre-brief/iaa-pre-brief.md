# IAA Pre-Brief — Stage 10

**Stage**: 10 — IAA Pre-Brief  
**Module**: App Management Centre (AMC)  
**Status**: ⬜ Not Started — canonical wave-record model adopted  
**Prerequisite**: Stage 9 Builder Checklist complete, unless CS2 explicitly authorizes earlier pre-brief preparation

---

## Purpose

Stage 10 defines the independent assurance pre-brief required before AMC builder appointment.

Under the AMC PR #1800 alignment model, the active IAA pre-brief is not a standalone `iaa-prebrief-*` file. It is recorded in the canonical wave record using:

```text
## PRE-BRIEF
IAA_PREFLIGHT_BRIEF
```

Canonical active carrier:

```text
.agent-admin/assurance/iaa-wave-record-<wave-id>.md
```

---

## Active protocol

Active protocol references:

```text
governance/canon/IAA_PRE_BRIEF_PROTOCOL.md
.agent-admin/control/protocols/IAA_PREFLIGHT_BRIEF_PROTOCOL.md
.agent-admin/control/schemas/iaa-preflight-brief.schema.json
.github/agents/independent-assurance-agent.md
```

Legacy standalone `.agent-admin/assurance/iaa-prebrief-*` artifacts are retained only as historical/provenance records.

---

## Stage 10 entry conditions

Stage 10 remains blocked until:

1. Stage 8 Implementation Plan exists;
2. Stage 9 Builder Checklist exists;
3. the intended build wave scope is known;
4. the expected QA-to-red scope is current;
5. CS2 has dispositioned any unresolved Stage 5 / Stage 5a / Stage 6 / Stage 7 blockers or explicitly authorized proceeding.

---

## Required pre-brief contents

The wave-record pre-brief must include:

- wave/job identifier;
- issue or PR reference;
- branch and current head SHA when available;
- qualifying tasks;
- expected QA scope;
- high-risk failure modes;
- required builder evidence;
- required Foreman QP checks;
- ECAP requirement status;
- final IAA focus;
- disposition: `PREFLIGHT_BRIEF_COMPLETE` or `PHASE_A_ADVISORY`.

---

## Status

Not started for the AMC build wave.

This Stage 10 placeholder has been migrated to the wave-record model so future build planning does not create new standalone `iaa-prebrief-*` files.
