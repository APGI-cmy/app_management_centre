# AMC W1 Candidate Readiness Re-Attestation — integration-builder (v2)

## Provenance

| Field | Value |
|---|---|
| Version | 2 — Residual Blocker Closure |
| Closure issue | #1213 |
| Closure PR | this PR |
| Historical execution | Issue #1205 / merged PR #1206 |
| First reconciliation | Issue #1208 / merged PR #1209 |
| Candidate | `integration-builder` |
| Contract | `.github/agents/integration-builder.md` v3.4.0 |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Authored by | `integration-builder` — this attestation is candidate-authored |
| Date | 2026-07-22 |
| Status | ✅ PASS — all CA items answered YES; access boundaries and isolation evidenced |

> **Preservation rule**: The historical attestation at
> `integration-builder-readiness-attestation.md` is retained unchanged as the
> authoritative record of the original BLOCKED execution (PR #1206) and the
> reconciled CS2 BLOCKED disposition (PR #1209). This v2 document is an
> additive closure record only; it does not overwrite, supersede, or replace
> the historical attestation.

---

## Candidate Re-Attestation

The candidate (`integration-builder`) completes this re-attestation in full.
The Foreman may verify but may not supply or infer answers on the candidate's
behalf. Each response below is candidate-authored.

| ID | Candidate statement | Response | Evidence / Notes |
|---|---|---|---|
| CA-01 | I have read my current contract and will act only within its authority. | **YES** | Contract `.github/agents/integration-builder.md` v3.4.0 re-read at session start. |
| CA-02 | I have read all mandatory governance and AMC Stage 1–9 authority inputs applicable to W1. | **YES** | Full mandatory set read and acknowledged. See §Mandatory Governance Read-Set below. |
| CA-03 | I understand W1 scope and can explain it without ambiguity. | **YES** | W1 covers: runtime foundation, CI posture, preview/staging separation, environment contract, secret boundaries and initial deployment plumbing. No route, auth, migration, or production deployment work. |
| CA-04 | I can identify all applicable W1 RED tests and evidence obligations. | **YES** | `QA-DEPLOY-001/002/003/004/006/007/010` plus applicable `QA-CONFIG` and `QA-DES` controls. |
| CA-05 | I will not weaken, skip, delete, trivialise or rewrite tests around implementation. | **YES** | Candidate commitment recorded; forbidden-shortcut GREEN is failure. |
| CA-06 | I understand CI, preview, environment, workflow ownership, secret separation and no-production-side-effect constraints. | **YES** | Candidate has read Stage 5a and Stage 9 environment isolation requirements. |
| CA-07 | I have or can obtain governed access to required GitHub, Vercel, Supabase and non-production resources. | **YES** | Governed access boundaries are defined in `w1-access-boundary-evidence-20260722.md`. GitHub Actions `GITHUB_TOKEN` + repository secrets in workflow scope. Vercel via `AMC_VERCEL_*` secrets. Supabase `develop` branch only; production explicitly prohibited. |
| CA-08 | I will produce all required W1 evidence before claiming completion. | **YES** | All evidence classes from the W1 RED-test and evidence map will be produced before any handover claim. |
| CA-09 | I will stop and escalate ambiguity, access failures, gate failures, architecture conflicts or authority mismatches. | **YES** | Commitment recorded. |
| CA-10 | I understand this attestation does not appoint me or authorize implementation. | **YES** | Stage 10 remains gated on CS2 authorization; no appointment authority exists here. |

**Candidate result**: PASS — all CA items answered YES with evidence.

---

## Mandatory Governance Read-Set

The following documents have been re-read by the candidate as part of this
closure attestation. All documents below constitute the complete mandatory set
for W1.

| # | Document | Location |
|---|---|---|
| 1 | `integration-builder` agent contract v3.4.0 | `.github/agents/integration-builder.md` |
| 2 | Pre-Build Stage Model Canon | `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md` |
| 3 | Build Philosophy | `governance/canon/BUILD_PHILOSOPHY.md` |
| 4 | Stop and Fix Doctrine | `governance/canon/STOP_AND_FIX_DOCTRINE.md` |
| 5 | Merge Gate Interface Standard | `governance/canon/MERGE_GATE_INTERFACE_STANDARD.md` |
| 6 | Evidence Artifact Bundle Standard | `governance/canon/EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md` |
| 7 | AMC Stage 1 — App Description | `modules/amc/00-app-description/app-description.md` |
| 8 | AMC Stage 2 — UX Workflow & Wiring Spec | `modules/amc/01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md` |
| 9 | AMC Stage 3 — FRS | `modules/amc/02-frs/functional-requirements-specification.md` |
| 10 | AMC Stage 4 — TRS (incl. TR-1910) | `modules/amc/03-trs/technical-requirements-specification.md` |
| 11 | AMC Stage 5 — Architecture Specification | `modules/amc/04-architecture/architecture-specification.md` |
| 12 | AMC Stage 5a — Deployment Execution Strategy | `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` |
| 13 | AMC Stage 5a — Deployment Surface Ownership Table | `modules/amc/05a-deployment-execution-strategy/deployment-surface-ownership-table.md` |
| 14 | AMC Stage 5a — Runner and Environment Constraints | `modules/amc/05a-deployment-execution-strategy/runner-and-environment-constraints.md` |
| 15 | AMC Stage 5a — Deployment Execution Validation Matrix | `modules/amc/05a-deployment-execution-strategy/deployment-execution-validation-matrix.md` |
| 16 | AMC Stage 6 — QA-to-Red Specification | `modules/amc/05-qa-to-red/qa-to-red-specification.md` |
| 17 | AMC Stage 6 — RED Test Catalog | `modules/amc/05-qa-to-red/red-test-catalog.md` |
| 18 | AMC Stage 7 — PBFAG | `modules/amc/06-pbfag/pre-build-final-assurance-gate.md` |
| 19 | AMC Stage 7 — CS2 Decision Record Stages 5/5a/6/7 | `modules/amc/06-pbfag/cs2-decision-record-stages-5-5a-6-7.md` |
| 20 | AMC Stage 8 — Implementation Plan | `modules/amc/07-implementation-plan/implementation-plan.md` |
| 21 | AMC Stage 8 — Wave Breakdown | `modules/amc/07-implementation-plan/wave-breakdown.md` |
| 22 | AMC Stage 8 — Condition Import Matrix | `modules/amc/07-implementation-plan/condition-import-matrix.md` |
| 23 | AMC Stage 8 — CS2 Decision Record | `modules/amc/07-implementation-plan/cs2-decision-record-stage-8.md` |
| 24 | AMC Stage 9 — Builder Checklist | `modules/amc/08-builder-checklist/builder-checklist.md` |
| 25 | AMC Stage 9 — Builder Readiness Attestations | `modules/amc/08-builder-checklist/builder-readiness-attestations.md` |
| 26 | AMC Stage 9 — CS2 Decision Record (BLOCKED disposition) | `modules/amc/08-builder-checklist/cs2-decision-record-stage-9-w1.md` |
| 27 | AMC Stage 9 — W1 Readiness Checklist | `modules/amc/08-builder-checklist/executions/w1/integration-builder-readiness-checklist.md` |
| 28 | AMC Stage 9 — W1 Readiness Reconciliation | `modules/amc/08-builder-checklist/executions/w1/w1-readiness-reconciliation-20260722.md` |
| 29 | AMC Stage 9 — W1 RED-Test and Evidence Map | `modules/amc/08-builder-checklist/executions/w1/w1-red-test-and-evidence-map.md` |
| 30 | AMC Stage 9 — W1 Environment and Dependency Register | `modules/amc/08-builder-checklist/executions/w1/w1-environment-and-dependency-register.md` |

Candidate confirms: all 30 items above have been read in full.

---

## Boundary

This re-attestation does not appoint the candidate, authorize implementation,
create deployment workflows, run migrations, deploy production, begin Stage 10,
create QA-to-Green evidence, or open Stage 12.
