# Foreman-v2 — Pre-Build Stage Model Quick Reference

**Version**: 1.0.0  
**Authority**: CS2 (@APGI-cmy) — Issue #1172  
**Date**: 2026-05-12  
**Canon Source**: `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0  
**Usage**: Quick reference for Foreman-v2 session use. Canonical definition is in PRE_BUILD_STAGE_MODEL_CANON.md — this file is a Tier 2 operational digest.

---

## The 12-Stage Sequence (Canonical Order — No Skipping)

| Stage | Name | Foreman Action | Gate |
|-------|------|---------------|------|
| 1 | App Description | Review and confirm CS2/client approval | Must be CS2-approved |
| 2 | UX Workflow & Wiring Spec | Review and confirm approved (mandatory for user-facing builds) | Must be approved |
| 3 | FRS | Review and confirm approved | Must be approved |
| 4 | TRS | Review and confirm approved | Must be approved |
| 5 | Architecture | Design and freeze (FM PLAN role) | Must be CS2-approved |
| 5a | Deployment Execution Strategy | Design deployment strategy; confirm CS2-approved before Stage 6 (AMC-specific) | Must be CS2-approved before Stage 6 |
| 6 | QA-to-Red | Create full failing test suite (FM ORGANIZE/LEAD) | FM signed off |
| 7 | PBFAG | Pre-Build Functionality Assessment Gate — independent gate review | Must PASS |
| 8 | Implementation Plan | Define waves, builders, sequencing | Must be approved |
| 9 | Builder Checklist | Complete pre-appointment readiness checklist | FM created and signed |
| 10 | IAA Pre-Brief | IAA classifies tasks, confirms oversight posture | Must be published |
| 11 | Builder Appointment | Foreman issues Build-to-Green order | After stages 1–10 all complete |
| 12 | Build | Builder implements under FM supervision | FM supervises, QP verdicts |

---

## AMC-Specific Addition: Stage 5a

Per `modules/amc/governance-oversight/DEPLOYMENT_STRATEGY_OVERSIGHT.md`:  
AMC adds a mandatory local Stage 5a (Deployment Execution Strategy) between Stage 5 and Stage 6.  
Stage 6 and Stage 8 are **blocked** until Stage 5a is CS2-approved and committed.

---

## HALT-008 Rule

> **Stages 1–10 MUST be complete and gate-passed before FM delegates Stage 11 (Builder Appointment) or initiates Stage 12 (Build).**
>
> No-delegation rule: Any builder delegation before stages 1–10 are complete triggers HALT-008.

---

## Pre-Build Reality Check Gate (sits between Stage 10 and Stage 11)

Per `governance/canon/PRE_BUILD_REALITY_CHECK_CANON.md`:

**Multi-party review required (minimum quorum: 3 of 4)**:
1. Foreman — leads the check (POLC: Checking)
2. User / Client Representative — validates original intent
3. Builder Lead — technical feasibility assessment
4. Quality Professor or Domain-Expert — independent gap analysis

**Checklist prerequisites** (all must be complete before gate):
- App Description — approved
- FRS — approved
- TRS — approved
- Architecture Design — approved
- Implementation Plan — approved
- Red QA Suite — FM signed off

**Gate proceeds only when**: all CRITICAL and MAJOR gaps are RESOLVED.

**Record location**: `<module-workspace>/05-build-readiness/pre-build-reality-check-YYYYMMDD.md`

---

## Arrow Chain (Canonical Shorthand)

```
App Description → UX Workflow & Wiring Spec → FRS → TRS → Architecture → [Stage 5a: Deployment Strategy] → QA-to-Red → PBFAG → Implementation Plan → Builder Checklist → IAA Pre-Brief → Builder Appointment → Build
```

---

## Quick Delegation Checklist (before Stage 11)

Before issuing any Build-to-Green order, verify ALL:

- [ ] App Description: CS2-approved
- [ ] UX Workflow & Wiring Spec: approved (if user-facing)
- [ ] FRS: approved
- [ ] TRS: approved
- [ ] Architecture: frozen and CS2-approved
- [ ] Stage 5a (AMC): Deployment Execution Strategy — CS2-approved
- [ ] QA-to-Red: FM signed off — tests exist and are RED
- [ ] PBFAG: PASS
- [ ] Implementation Plan: approved
- [ ] Builder Checklist: FM created and signed
- [ ] IAA Pre-Brief: published in wave record section 2
- [ ] Builder task spec: created in `.agent-workspace/foreman-v2/builder-tasks/`

---

**Authority**: CS2 — Issue #1172  
**Canon Reference**: `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0  
**AMC Supplement**: `modules/amc/governance-oversight/DEPLOYMENT_STRATEGY_OVERSIGHT.md`  
