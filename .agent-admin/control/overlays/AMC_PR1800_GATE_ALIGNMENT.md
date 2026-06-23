# AMC PR #1800 Gate Alignment Overlay

## Purpose

This overlay adapts the ISMS PR #1800 gate model to `APGI-cmy/app_management_centre`.

## Active rules

1. Foreman orchestrates and does not build.
2. Builder implementation requires canonical IAA pre-brief, builder appointment, and delegation order evidence.
3. Implementation-only work is not handover.
4. Handover/completion/merge-readiness language is gated by `handover-allowed.json`.
5. ECAP validates administrative completeness only and cannot issue readiness or assurance verdicts.
6. IAA pre-briefs for new work belong in wave records under `## PRE-BRIEF` / `IAA_PREFLIGHT_BRIEF`.
7. Legacy standalone `iaa-prebrief-*` references are tolerated as history, but active guidance must not create new standalone artifacts.
8. Push-only watchdog findings are advisory; PR-triggered gates determine merge readiness once a PR exists.

## AMC path calibration

Implementation-like paths include:

```text
modules/amc/src/**
apps/**/src/**
packages/**/src/**
supabase/functions/**
api/**
lib/**
*.test.*
*.spec.*
```

Admin/gate paths include:

```text
.agent-admin/control/**
.agent-admin/assurance/**
.agent-admin/scope-declarations/**
.agent-admin/builder-appointments/**
.agent-admin/ecap/**
.agent-admin/quality/**
```

## Build readiness reminder

AMC remains build-blocked until Stage 5, Stage 5a, Stage 6, and Stage 7 are explicitly dispositioned by CS2 and Stage 8/9/10/11 artifacts exist.
