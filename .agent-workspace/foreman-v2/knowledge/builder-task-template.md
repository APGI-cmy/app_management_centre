# Foreman-v2 — Builder Task Template

**Version**: 1.0.0  
**Authority**: CS2 (@APGI-cmy) — Issue #1172  
**Date**: 2026-05-12  
**Usage**: Copy this template when creating a builder task specification. File naming: `.agent-workspace/foreman-v2/builder-tasks/<task-id>-<YYYYMMDD>.md`

---

## Template

```markdown
# Builder Task Specification — <TASK-ID>

**Wave**: wave-<slug>-<YYYYMMDD>
**Task ID**: TASK-<WAVE>-<SEQ>
**Date**: YYYY-MM-DD
**Assigned Builder**: <builder-agent-id>
**Governing Issue**: #<N>
**FM Orchestrator**: foreman-v2-agent

---

## Context and Scope

<1–3 sentences explaining why this task exists and what problem it solves.>

## Architecture Reference

<Path to the frozen architecture design document for this wave, if applicable.>
e.g. `.agent-admin/build-evidence/session-<NNN>-<YYYYMMDD>/architecture-<slug>-<YYYYMMDD>.md`

## Red QA Suite Reference

<Path to the QA-to-Red suite this builder must turn GREEN.>
e.g. `tests/test_<slug>.py` or `tests/<slug>/`

---

## Acceptance Criteria

Each criterion maps to a specific test or validator. The builder MUST produce REAL assertions — stubs are prohibited.

| ID | Criterion | Evidence Type | Test/Validator Path |
|----|-----------|--------------|---------------------|
| AC-01 | <criterion text> | CI_TEST | <path> |
| AC-02 | <criterion text> | STATIC_CODE | <path> |
| AC-03 | <criterion text> | ARTIFACT | <path> |

---

## Files to Create or Modify

| File | Action | Notes |
|------|--------|-------|
| `<path>` | CREATE/UPDATE/DELETE | <brief description> |

---

## Forbidden Actions

The builder MUST NOT:
- Modify `.github/agents/**` (CS2-gated — requires CodexAdvisor + CS2 approval regardless of Foreman direction)
- Modify `governance/**` unless explicitly listed in the task spec's "Files to Create or Modify" section and Foreman has confirmed scope authorization
- Skip or stub any test
- Introduce `// TODO`, `.skip()`, `.todo()` in test files
- Self-approve merge gates

---

## Build-to-Green Order

> **Foreman Build-to-Green Order**
>
> Builder: <builder-agent-id>
> Task: TASK-<WAVE>-<SEQ>
> Branch: <branch-name>
>
> The Red QA suite is ready. Your task is to implement the scope above until ALL tests are GREEN.
> Return a prehandover evidence bundle when complete.
> Do not merge. Foreman applies QP verdict before any merge gate action.

---

## Return Requirements (builder must provide all of these)

- [ ] 100% GREEN test results (CI output or local run proof)
- [ ] List of files created/modified
- [ ] Confirm no `.skip()`, `.todo()`, `// TODO` in test files
- [ ] Confirm no implementation artifacts added to repo root
- [ ] Wave record path
- [ ] Architecture design document reference (if applicable)

---

**QP Verdict**: PENDING (assigned by Foreman after builder returns)  
**Wave Checklist Tick**: Requires QP PASS before `[ ]` → `[x]`
```

---

## Usage Notes

1. **Always reference the frozen architecture design** before delegating — architecture must be approved before builder appointment (Stage 11 requires Stage 10 complete).
2. **Always have a Red QA suite** before issuing Build-to-Green order — Stage 6 (QA-to-Red) must be FM signed off.
3. **One task per builder spec** unless explicitly justified as non-overlapping scope.
4. **Store completed specs** at `.agent-workspace/foreman-v2/builder-tasks/` (per Foreman write access).
5. **Return requirements are non-negotiable** — QP verdict requires evidence, not assertions.

---

**Authority**: CS2 — Issue #1172  
**Canon Reference**: `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md` §3.1 (Stages 9–12)  
**Protocol Reference**: `governance/canon/FM_BUILDER_APPOINTMENT_PROTOCOL.md`  
