# Wave Current Tasks — wave-placeholder-check-future-layerdown-20260420

> **Authority**: CS2 (@APGI-cmy) — Issue #1094  
> **Wave Verb**: assess / plan / scaffold  
> **Classification**: POLC-Orchestration — future layer-down pre-activation governance  
> **Date**: 2026-04-20  
> **Foreman Session**: session-027-20260420

---

## Status: PRE-ACTIVATION — TRIGGER CONDITIONS NOT YET MET

This wave responds to Issue #1094 "[Future Layer-Down] Adopt canonical placeholder-check exception model after upstream governance canon is finalized."

The issue is explicitly future-scoped. Trigger conditions (see Issue #1094) are **NOT YET MET**:
- ❌ Upstream governance canon for placeholder-check exception classes: NOT MERGED
- ❌ First consumer repo layer-down: NOT COMPLETE
- ❌ Canonical class model: NOT FINALIZED

**Foreman action**: Create pre-activation governance scaffolding and trigger-condition assessment. No builder delegation and no implementation work until all trigger conditions are met.

---

## Task List

```
- [x] TASK-027-01 — Trigger condition assessment: document current AMC placeholder-check state
      builder: foreman-v2-agent (POLC: Planning)
      qp_verdict: PASS
      notes: Assessment complete — trigger conditions NOT MET; current check uses ad-hoc patterns in CORE-007

- [x] TASK-027-02 — Create wave governance scaffolding (current-tasks, wave record, session memory)
      builder: foreman-v2-agent (POLC: Organizing)
      qp_verdict: PASS
      notes: This file; wave record at .agent-admin/wave-records/amc-wave-record-wave-placeholder-check-future-layerdown-20260420.md

- [x] TASK-027-03 — IAA Pre-Brief and final assurance invocation
      builder: independent-assurance-agent (synchronous tool call)
      qp_verdict: PASS
      notes: Invoked per Phase 2.4 and Phase 4.4 of Foreman contract
```

---

## Pre-Activation Plan (for when trigger conditions ARE met)

When all three trigger conditions are met, the activation wave should:

1. **TASK-ACTIVATE-01** — Import canonical exception-class reference from upstream
   - builder: CodexAdvisor-agent or qa-builder (to be determined at activation time)
   - scope: layer down the finalized canonical exception-class reference document

2. **TASK-ACTIVATE-02** — Update `agent-contract-format-gate.yml` CORE-007 check
   - builder: api-builder or integration-builder
   - scope: Replace ad-hoc grep exclusion (`iaa_audit_token` only) with named exception-class logic aligned to the canonical model

3. **TASK-ACTIVATE-03** — Update `governance/scripts/validate-architecture-compilation.py`
   - builder: qa-builder
   - scope: Align placeholder pattern matching to canonical exception classes

4. **TASK-ACTIVATE-04** — Proof-of-operation demonstration
   - builder: qa-builder
   - scope: One AMC agent-contract validation path demonstrating false-positive reduction and true-positive preservation

5. **TASK-ACTIVATE-05** — Remove/normalize any AMC-local exception logic not fitting the canonical model
   - builder: CodexAdvisor-agent (if `.github/agents/*.md` files are involved) or integration-builder
   - scope: Audit all current ad-hoc exception phrases; retain only those that fit canonical classes with documented justification

---

*Filed by*: foreman-v2-agent (session-027) | *Date*: 2026-04-20
