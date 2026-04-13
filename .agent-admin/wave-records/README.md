# AMC Wave Records

> **Authority**: CS2 (@APGI-cmy) — Issue #1063
> **Effective**: 2026-04-13
> **Supersedes**: Legacy separate prebrief, token, rejection, and handover artifacts

## Purpose

This directory contains **consolidated wave records** — a single artifact per governance wave
that replaces the legacy multi-file admin model (separate iaa-prebrief, iaa-token,
iaa-rejection, PREHANDOVER_PROOF, and session memory files).

## Naming Convention

```
amc-wave-record-{wave-slug}-{YYYYMMDD}.md
```

Example: `amc-wave-record-layer-down-529d541f-20260413.md`

## What Goes Here

Each wave record includes:
- Wave identity (ID, date, agent, branch, issue)
- Scope and classification
- Evaluation summary (QP verdict, evidence)
- Session outcome and learning
- IAA assurance reference (if applicable)
- Failure trail (if applicable — inline, not separate file)

## What Does NOT Go Here

- Legacy standalone prebrief files → archived under `.agent-admin/archive/`
- Legacy standalone token files → archived under `.agent-admin/archive/`
- Legacy standalone rejection files → archived under `.agent-admin/archive/`
- Separate PREHANDOVER_PROOF files → consolidated into wave record
- Separate session memory files → consolidated into wave record

## CI Enforcement

The `governance-artifact-enforcement.yml` workflow enforces that new governance artifacts
are only created in allowed paths. Wave records are an allowed path.
