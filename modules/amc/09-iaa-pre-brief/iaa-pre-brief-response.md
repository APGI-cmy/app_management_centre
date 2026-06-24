# IAA Pre-Brief Response — Stage 10

**Stage**: 10 — IAA Pre-Brief  
**Module**: App Management Centre (AMC)  
**Status**: ⬜ Not Started — canonical wave-record response model adopted

---

## Purpose

This document describes the expected IAA response posture for Stage 10. It is not itself the active pre-brief response.

Under the AMC PR #1800 model, the active IAA response is recorded in the same canonical wave record as the pre-brief:

```text
.agent-admin/assurance/iaa-wave-record-<wave-id>.md
```

The active response must use one of these dispositions:

```text
PREFLIGHT_BRIEF_COMPLETE
PHASE_A_ADVISORY
STOP_AND_FIX
ESCALATE_TO_CS2
```

---

## Required response contents

A Stage 10 IAA response must state:

- whether the work contains qualifying assurance tasks;
- whether the pre-brief is complete or advisory only;
- what builder evidence will be required later;
- what Foreman QP checks will be required later;
- whether ECAP admin validation will be required;
- what final IAA assurance will focus on;
- any blockers that must be resolved before builder appointment.

---

## Legacy suppression

Standalone `.agent-admin/assurance/iaa-prebrief-*` response artifacts are legacy/historical only. New active IAA response evidence must be recorded in the canonical wave record.

---

## Status

Not started for the AMC build wave.
