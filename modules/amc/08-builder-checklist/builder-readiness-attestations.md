# AMC Builder Readiness Attestations — Stage 9

## Status Header

| Field | Value |
|---|---|
| Module | App Management Centre (AMC) |
| Stage | 9 — Builder Checklist |
| Version | 1.1 |
| Status | 🟡 Produced for CS2 Review — No Candidate Attestations Executed |
| Governing Issue | `app_management_centre#1203` |
| Governing PR | `app_management_centre#1204` |
| Authority | CS2 — Johan Ras |
| Date Produced | 2026-07-10 |
| Canonical Location | `modules/amc/08-builder-checklist/builder-readiness-attestations.md` |

---

## 1. Purpose

This artifact defines the controlled attestation record to be completed later for each proposed AMC builder candidate after the Stage 9 checklist has been approved.

An attestation records the candidate's acknowledgement and the Foreman's independent verification. It is not a builder appointment, delegation order, IAA pre-brief, implementation authorisation, or build-readiness certificate.

---

## 2. Execution Rules

1. Complete one record per proposed candidate and proposed wave allocation.
2. Do not reuse an attestation across materially different scope, wave, contract version, or repository state.
3. Support every statement with exact paths, test IDs, environment references, or evidence links.
4. A candidate may not attest for another candidate or self-approve role fit.
5. Foreman independently verifies the candidate statements and suitability.
6. Any negative, conditional, unknown, unsupported, or unresolved statement produces FAIL/BLOCKED.
7. Stage 10 remains blocked until the approved Stage 9 process has produced PASS records for the intended candidate set.

---

## 3. Candidate Identity and Proposed Scope

| Field | Entry |
|---|---|
| Candidate agent ID | Not executed |
| Candidate contract path/version | Not executed |
| Proposed builder class | Not executed |
| Proposed AMC wave(s) | Not executed |
| Proposed technical scope | Not executed |
| Evaluation issue/PR | Not executed |
| Evaluation date | Not executed |
| Foreman evaluator | Not executed |

---

## 4. Candidate Attestation

| ID | Candidate statement | Response | Evidence / Notes |
|---|---|---|---|
| CA-01 | I have read and understood my current contract and will act only within its builder authority. | [ ] YES [ ] NO | |
| CA-02 | I have read all mandatory governance documents and AMC Stage 1–8 authority inputs listed in the approved Stage 9 checklist. | [ ] YES [ ] NO | |
| CA-03 | I understand the exact W1–W8 scope proposed for me and have no unresolved ambiguity. | [ ] YES [ ] NO | |
| CA-04 | I can identify every applicable existing, QA-FD, QA-DEPLOY, and PBFAG test/evidence obligation. | [ ] YES [ ] NO | |
| CA-05 | I will not weaken, skip, delete, trivialise, suppress, or rewrite tests to fit my implementation. | [ ] YES [ ] NO | |
| CA-06 | I will preserve canonical AMC boundaries, routes, events, tables, workflows, and authority controls. | [ ] YES [ ] NO | |
| CA-07 | I will not introduce direct model-provider access, direct AIMCC ingestion, unmanaged canonical knowledge storage, or another boundary bypass. | [ ] YES [ ] NO | |
| CA-08 | I understand the environment, secret, deployment, migration, rollback, health, smoke, dependency, and degraded-mode controls for my scope. | [ ] YES [ ] NO | |
| CA-09 | Required tools and environments are available, or governed access is explicitly arranged. | [ ] YES [ ] NO | |
| CA-10 | I will produce the complete evidence package applicable to my wave before claiming completion. | [ ] YES [ ] NO | |
| CA-11 | I will stop and escalate any ambiguity, defect, authority mismatch, inaccessible dependency, architecture change, test conflict, or governance blocker. | [ ] YES [ ] NO | |
| CA-12 | I understand this attestation does not appoint me or authorise implementation. | [ ] YES [ ] NO | |

**Candidate attestation result**: [ ] PASS [ ] FAIL [ ] NOT EXECUTED

**Candidate identifier/signature**: Not executed  
**Date**: Not executed

---

## 5. Wave-Specific Attestation

Every applicable row must be YES. `N/A` requires written rationale and Foreman acceptance.

| Wave | Required acknowledgement | Response | Evidence / Notes |
|---|---|---|---|
| W1 | I understand `.github/workflows/ci.yml`, `.github/workflows/deploy-frontend.yml`, `.github/workflows/db-migrate.yml`, preview/environment ownership, secret separation, and no-production-side-effect constraints. | [ ] YES [ ] NO [ ] N/A | |
| W2 | I understand auth, tenant isolation, RLS, server authority, state ownership, and atomic audit obligations. | [ ] YES [ ] NO [ ] N/A | |
| W3 | I understand material route, CTA, service, state, audit, visible-result, and degraded-mode closure requirements. | [ ] YES [ ] NO [ ] N/A | |
| W4 | I understand the complete `/alerts` acknowledgement E2E path and evidence package. | [ ] YES [ ] NO [ ] N/A | |
| W5 | I understand canonical ARC, approvals, interventions, quota lifecycle, authority, state, and audit requirements. | [ ] YES [ ] NO [ ] N/A | |
| W6 | I understand AIMC, AIMCC, KUC, knowledge, Foreman, specialist, push, service-token, provenance, and degraded-mode boundaries. | [ ] YES [ ] NO [ ] N/A | |
| W7 | I understand protected deployment, frozen migration command, rollback, environment isolation, health, smoke, and release-evidence requirements. | [ ] YES [ ] NO [ ] N/A | |
| W8 | I understand 100% GREEN, zero test debt, evidence consolidation, regression, tracker/index truth, and shortcut rejection. | [ ] YES [ ] NO [ ] N/A | |

**Wave-specific result**: [ ] PASS [ ] FAIL [ ] NOT EXECUTED

---

## 6. Foreman Verification

| ID | Verification | Result | Evidence / Notes |
|---|---|---|---|
| FV-01 | Candidate contract is current and authorises the proposed class and repository scope. | [ ] PASS [ ] FAIL | |
| FV-02 | Candidate accurately demonstrated the proposed AMC wave scope and boundaries. | [ ] PASS [ ] FAIL | |
| FV-03 | Candidate accurately identified applicable RED tests and evidence obligations. | [ ] PASS [ ] FAIL | |
| FV-04 | Required tools, environments, credentials, and dependencies are available or governed access is confirmed. | [ ] PASS [ ] FAIL | |
| FV-05 | Build-to-Green and required implementation gates are active and blocking. | [ ] PASS [ ] FAIL | |
| FV-06 | No unresolved ambiguity, dependency, authority mismatch, or governance blocker remains. | [ ] PASS [ ] FAIL | |
| FV-07 | Candidate competency and performance posture suit the proposed scope. | [ ] PASS [ ] FAIL | |
| FV-08 | Candidate is the correct role fit for the proposed allocation. | [ ] PASS [ ] FAIL | |

**Foreman verification result**: [ ] PASS [ ] FAIL [ ] NOT EXECUTED

**Foreman identifier/sign-off**: Not executed  
**Date**: Not executed

---

## 7. Final Outcome

| Component | Outcome |
|---|---|
| Candidate identity and contract | [ ] PASS [ ] FAIL |
| Candidate universal attestation | [ ] PASS [ ] FAIL |
| Wave-specific attestation | [ ] PASS [ ] FAIL |
| Foreman independent verification | [ ] PASS [ ] FAIL |

**FINAL RESULT**: [ ] PASS — candidate may be considered during Stage 10; [ ] FAIL/BLOCKED — Stage 10 consideration and appointment prohibited.

No result has been executed in PR #1204.

---

## 8. Re-evaluation Rule

Re-evaluation is mandatory after any failed check, contract change, scope change, repository-state change, gate change, environment change, dependency change, or new ambiguity.

---

## 9. Explicit Non-Scope

This artifact does not approve Stage 9, complete a candidate evaluation, create Stage 10, appoint or delegate to a builder, authorise implementation, create code or deployment changes, produce QA-to-Green/build evidence, or certify AMC build-ready, handover-ready, or merge-ready.
