# IAA Pre-Brief — Stage 10

**Stage**: 10 — IAA Pre-Brief  
**Module**: App Management Centre (AMC)  
**Status**: ✅ Complete / Current — `PREFLIGHT_BRIEF_COMPLETE` accepted through merged PR #1218  
**Governing issue / PR**: #1217 / merged #1218  
**Post-merge reconciliation**: #1219  
**Final assurance token**: `IAA-session-1218-R2-20260723-PASS`  
**Prerequisite**: Stage 9 Builder Checklist complete and accepted in merged PR #1216

---

## Purpose

Stage 10 defines the independent assurance pre-brief required before AMC builder appointment.

Under the AMC PR #1800 alignment model, the active IAA pre-brief is not a standalone `iaa-prebrief-*` file. It is recorded in the canonical wave record using:

```text
## PRE-BRIEF
IAA_PREFLIGHT_BRIEF
```

Canonical active carrier for W1:

```text
.agent-admin/assurance/iaa-wave-record-amc-w1-runtime-foundation.md
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

The W1 Stage 10 entry conditions are satisfied:

1. Stage 8 Implementation Plan exists and is approved with conditions;
2. Stage 9 Builder Checklist exists and W1 readiness PASS was accepted in merged PR #1216;
3. the W1 scope is known;
4. the expected QA-to-Red scope is current;
5. CS2 explicitly authorized Stage 10 in issue #1217.

---

## Required pre-brief contents

The canonical W1 wave-record pre-brief includes:

- wave/job identifier;
- issue and PR reference;
- branch and authority context;
- schema-conformant `IAA_PREFLIGHT_BRIEF` JSON payload;
- qualifying tasks;
- expected QA scope;
- high-risk failure modes;
- required builder evidence;
- required Foreman QP checks;
- ECAP requirement status;
- final IAA focus;
- stop and escalation conditions;
- disposition `PREFLIGHT_BRIEF_COMPLETE`.

---

## Current disposition

```text
PREFLIGHT_BRIEF_COMPLETE
```

This means the W1 assurance expectations are sufficiently defined for Stage 11 consideration. PR #1218 is merged and Stage 10 is accepted.

Stage 11 remains unstarted and requires a separate explicit CS2-authorized appointment issue.

It does not appoint or delegate `integration-builder`, authorize Stage 12, create implementation outputs, run migrations, or deploy Production.
