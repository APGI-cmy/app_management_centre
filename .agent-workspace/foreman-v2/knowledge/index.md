# Foreman-v2-agent — Tier 2 Knowledge Index

> **Version**: 1.1.0 — AMC Consumer Copy
> **Last Updated**: 2026-04-07
> **Canon Home**: APGI-cmy/maturion-foreman-governance
> **Canon Commit**: `038546344e8d67823c63464dc038841bd947405b` (maturion-isms)
> **Staleness Policy**: Flag for refresh if canon version exceeds this by 1 minor version.

---

## Knowledge Table

| File | Purpose | Status |
|---|---|---|
| `domain-flag-index.md` | POLC orchestration mode flags per domain | ✅ PRESENT — layered down 2026-04-07 (v1.0.0) |
| `specialist-registry.md` | Builder agent registry for task delegation | ✅ PRESENT — created 2026-04-10 (v1.0.0) |
| `FAIL-ONLY-ONCE.md` | Breach registry and A-rules for foreman-v2 | ✅ PRESENT — layered down 2026-04-07 (v4.1.0) |
| `session-memory-template.md` | Session memory template (reduced 6-field model per 90/10 principle) | ✅ PRESENT — v2.0.0 (updated 2026-04-13, Issue #1063) |
| `prehandover-template.md` | PREHANDOVER proof template (v1.7.0) | ✅ PRESENT — layered down 2026-04-07 (v1.7.0) |
| `wave-reconciliation-checklist.md` | Wave close checklist — incidents, niggles, liveness | ✅ PRESENT — layered down 2026-04-07 (v1.0.0) |

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

## Required Files (from `tier2_knowledge.required_files` in contract)

- `domain-flag-index.md`
- `specialist-registry.md`
- `FAIL-ONLY-ONCE.md`
- `session-memory-template.md`

---

## Notes

Tier 2 knowledge layer-down executed 2026-04-07 (CodexAdvisor session-013).
Source commit: `038546344e8d67823c63464dc038841bd947405b` (APGI-cmy/maturion-isms).
Files layered down: `FAIL-ONLY-ONCE.md` (v4.1.0), `prehandover-template.md` (v1.7.0),
`wave-reconciliation-checklist.md` (v1.0.0), `domain-flag-index.md` (v1.0.0).
Stubs resolved 2026-04-10 (wave-ecap001-amc-downstream): `specialist-registry.md` (v1.0.0),
`session-memory-template.md` (v1.0.0). All required Tier 2 files now PRESENT.
