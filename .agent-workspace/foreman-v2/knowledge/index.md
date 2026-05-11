# Foreman-v2-agent — Tier 2 Knowledge Index

> **Version**: 1.4.0 — AMC Consumer Copy
> **Last Updated**: 2026-05-11
> **Amendment**: v1.4.0 — Added `builder-task-template.md` and `pre-build-stage-model-reference.md` to resolve Tier 2 parity with contract v3.3.1 required_files; authority: CS2 — Issue #1172 (startup-parity fix PR).
> **Previous**: v1.3.0 — Added SPAM-001 reference (MMM_SIMPLE_PR_ADMIN_MODEL.md); added behavioral guidance for simple-admin PRs; authority: CS2 — Issue #1163.
> **Canon Home**: APGI-cmy/maturion-foreman-governance
> **Canon Commit**: `038546344e8d67823c63464dc038841bd947405b` (maturion-isms)
> **Staleness Policy**: Flag for refresh if canon version exceeds this by 1 minor version.

---

## Knowledge Table

| File | Purpose | Status |
|---|---|---|
| `domain-flag-index.md` | POLC orchestration mode flags per domain | ✅ PRESENT — layered down 2026-04-07 (v1.0.0) |
| `specialist-registry.md` | Builder agent registry for task delegation | ✅ PRESENT — created 2026-04-10 (v1.0.0) |
| `FAIL-ONLY-ONCE.md` | Breach registry and A-rules for foreman-v2 | ✅ PRESENT — layered down 2026-04-07 (v4.1.0); amended 2026-04-27 (v4.3.0 — A-039 WAVE-RESULT-COHERENCE-MANDATORY (Issue #1143) + A-040/A-041/A-042 (Issue #1145) added) |
| `session-memory-template.md` | Session memory template (reduced 6-field model per 90/10 principle) | ✅ PRESENT — v2.0.0 (updated 2026-04-13, Issue #1063) |
| `prehandover-template.md` | PREHANDOVER proof template (v1.7.0) | ✅ PRESENT — layered down 2026-04-07 (v1.7.0) |
| `wave-reconciliation-checklist.md` | Wave close checklist — incidents, niggles, liveness, closeout sweep | ✅ PRESENT — v1.2.0 (updated 2026-04-26, Issue #1134 — Section E closeout sweep added) |
| `builder-task-template.md` | Standard template for delegating tasks to builder-class agents | ✅ PRESENT — v1.0.0 (created 2026-05-11 — startup-parity fix, Issue #1172) |
| `pre-build-stage-model-reference.md` | Quick-reference card for the 12-stage pre-build model and HALT-008 gate | ✅ PRESENT — v1.0.0 (created 2026-05-11 — startup-parity fix, Issue #1172) |

---

## Can Do (from agent contract YAML)

- Plan waves (POLC-Orchestration)
- Delegate to builder-class agents
- Supervise builders and evaluate deliverables
- Release merge gates (after IAA PASS and QP PASS)
- Invoke IAA for wave handovers (mandatory)
- Issue QP (Quality Professor) PASS/FAIL verdicts

---

## Cannot Do (from agent contract YAML)

- Write production code, schemas, migrations, tests, or CI scripts
- Modify `.github/agents/*.md` files (CodexAdvisor + CS2 only)
- Self-modify (SELF-MOD-FM-001 — CONSTITUTIONAL)
- Write IAA assurance token files (IAA agent only)
- Push directly to main
- Self-certify IAA verdicts

---

## Required Files (from `tier2_knowledge.required_files` in contract v3.3.1)

- `FAIL-ONLY-ONCE.md` ✅ PRESENT
- `session-memory-template.md` ✅ PRESENT
- `builder-task-template.md` ✅ PRESENT (v1.0.0 — created 2026-05-11)
- `pre-build-stage-model-reference.md` ✅ PRESENT (v1.0.0 — created 2026-05-11)

---

## Notes

Tier 2 knowledge layer-down executed 2026-04-07 (CodexAdvisor session-013).
Source commit: `038546344e8d67823c63464dc038841bd947405b` (APGI-cmy/maturion-isms).
Files layered down: `FAIL-ONLY-ONCE.md` (v4.1.0), `prehandover-template.md` (v1.7.0),
`wave-reconciliation-checklist.md` (v1.0.0), `domain-flag-index.md` (v1.0.0).
Stubs resolved 2026-04-10 (wave-ecap001-amc-downstream): `specialist-registry.md` (v1.0.0),
`session-memory-template.md` (v1.0.0). All required Tier 2 files now PRESENT.

---

## SPAM-001 — Simple PR Admin Model (CS2 — Issue #1163 — 2026-05-05)

### Tier 1 Reference

The AMC Simple PR Admin Model is defined in:
- `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` (SPAM-001 v1.0.0) — normative definition
- `governance/canon/AGENT_HANDOVER_AUTOMATION.md` §4.3f — Phase 4 exception for product-fix PRs
- `governance/canon/EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` §2.4 — ECAP exception

### Foreman Behavioral Guidance

**When to create `.admin/pr.json`**:
- Only for product-fix or docs-only PRs that do NOT touch any forced-ceremony path
- Never create `.admin/pr.json` with `requires_iaa: false` if the diff contains `governance/**`, `.github/agents/**`, `.governance-pack/**`, `.agent-workspace/**/knowledge/**`, migrations, or `BUILD_PROGRESS_TRACKER`

**Before proceeding without ceremony**:
1. Verify PR type is `product-fix` or `docs-only`
2. Run forced-ceremony path check manually: `git diff --name-only origin/main...HEAD | grep -E "^governance/|^\.github/agents/|^\.governance-pack/|^\.agent-workspace/.*/knowledge/|supabase/migrations/|^schema/|^migrations/|BUILD_PROGRESS_TRACKER"`
3. If ANY results: do NOT use simple admin; create full ceremony wave instead
4. Only proceed without ceremony if the grep returns zero results

**Preserved controls (ALWAYS blocking regardless of `.admin/pr.json`)**:
- POLC boundary: foreman-implementation-check, builder-involvement-check
- build-to-green enforcement
- agent-contract-format-gate
- agent-boundary-gate
- agent-bootstrap-inject gate

**Authority**: SPAM-001 — `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` v1.0.0
