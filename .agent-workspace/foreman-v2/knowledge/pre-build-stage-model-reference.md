# Pre-Build Stage Model Reference — Foreman-v2-agent Tier 2 Knowledge

> **Version**: 1.0.0
> **Authority**: CS2 — Issue #1172 (startup-parity fix); canon source: `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md`
> **Created**: 2026-05-11
> **Purpose**: Quick reference card for the 12-stage pre-build derivation chain. Foreman uses this during Phase 3.1 to verify stage completion before builder delegation.

---

## The 12-Stage Pre-Build Chain

| Stage | Artifact | Gate Authority | HALT on Skip |
|---|---|---|---|
| 1 | App Description | CS2 / client approval | Yes |
| 2 | UX Workflow & Wiring Spec | CS2 approval (mandatory for user-facing builds) | Yes |
| 3 | Functional Requirements Specification (FRS) | CS2 approval | Yes |
| 4 | Technical Requirements Specification (TRS) | CS2 approval | Yes |
| 5 | Architecture Design | CS2 approval | Yes |
| 5a | Deployment Execution Strategy *(AMC-local mandatory stage)* | CS2 approval | Yes |
| 6 | QA-to-Red (Red test suite) | Foreman sign-off | Yes |
| 7 | Pre-Build Functionality Assessment Gate (PBFAG) | PASS gate | Yes |
| 8 | Implementation Plan | CS2 approval | Yes |
| 9 | Builder Checklist | Foreman created and signed | Yes |
| 10 | IAA Pre-Brief | Published (§2.4) | Yes |
| 11 | Builder Appointment | Foreman issues Build-to-Green order | Yes |
| 12 | Build | Builder executes under Foreman supervision | — |

> **AMC-local rule (Stage 5a)**: Stage 5a (Deployment Execution Strategy) is mandatory between Stage 5 and Stage 6. Stages 6 and above are blocked until Stage 5a is CS2-approved and committed.

---

## No-Delegation Rule (HALT-008)

Stages 1–10 **MUST** be complete and gate-passed before Foreman delegates Stage 11 (Builder Appointment) or initiates Stage 12 (Build).

Foreman checks this for **every wave** before builder appointment.

---

## Pre-Build Reality Check Gate (Between Stages 10 and 11)

**Authority**: `governance/canon/PRE_BUILD_REALITY_CHECK_CANON.md`

| Check | Description |
|---|---|
| App Description | Approved |
| FRS | Approved |
| TRS | Approved |
| Architecture Design | Approved |
| Implementation Plan | Approved |
| Red QA Suite | Foreman signed off |

Multi-party review quorum: **3 of 4** (Foreman + User/Client + Builder Lead + QP/Domain-Expert).

Gate record path: `<module-workspace>/05-build-readiness/pre-build-reality-check-YYYYMMDD.md`

---

## Governance-Control vs. Product-Fix Classification

Before determining which stages apply, classify the PR type:

| PR Type | Ceremony Level | Examples |
|---|---|---|
| **product-fix / docs-only** (no forced paths) | Simple admin — `.admin/pr.json` | Bug fixes, UI polish, non-governance docs |
| **governance-control** (forced paths touched) | Full ceremony — all 12 stages + wave record + IAA | `governance/**`, `.github/agents/**`, `.agent-workspace/**/knowledge/**`, CI scripts, migrations |

**Forced-ceremony path check** (run before every PR):

```bash
git diff --name-only origin/main...HEAD | grep -E \
  "^governance/|^\.github/agents/|^\.governance-pack/|^\.agent-workspace/.*/knowledge/|^\.agent-admin/|^\.github/workflows/|^\.github/scripts/|supabase/migrations/|^schema/|^migrations/|BUILD_PROGRESS_TRACKER"
```

Any result → full ceremony required → do NOT use simple admin.

---

## Stage Artifacts Reference

| Stage | Typical Artifact Location |
|---|---|
| 1 | `modules/<name>/governance-oversight/APP_DESCRIPTION.md` |
| 2 | `modules/<name>/governance-oversight/UX_WORKFLOW_AND_WIRING_SPEC.md` |
| 3 | `modules/<name>/governance-oversight/FUNCTIONAL_REQUIREMENTS_SPECIFICATION.md` |
| 4 | `modules/<name>/governance-oversight/TECHNICAL_REQUIREMENTS_SPECIFICATION.md` |
| 5 | `modules/<name>/governance-oversight/ARCHITECTURE_DESIGN.md` |
| 5a | `modules/<name>/governance-oversight/DEPLOYMENT_STRATEGY_OVERSIGHT.md` |
| 6 | `qa/<name>/red-suite/` |
| 7 | `modules/<name>/governance-oversight/PBFAG_EVIDENCE.md` |
| 8 | `modules/<name>/governance-oversight/IMPLEMENTATION_PLAN.md` |
| 9 | `.agent-admin/waves/wave-<N>-current-tasks.md` |
| 10 | Wave record Section 2 — IAA Pre-Brief subsection |
| 11 | Wave record Section 1 — Builder appointments |
| 12 | Builder evidence + QP verdict |

---

## POLC Boundary Reminder

Foreman's role at each stage is to **plan, organize, lead, and check** — never to implement. If any stage requires implementation artifacts (code, tests, migrations, CI scripts), delegate to the appropriate builder.
