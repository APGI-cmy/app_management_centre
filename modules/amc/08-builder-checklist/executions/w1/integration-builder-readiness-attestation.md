# AMC W1 Candidate Readiness Attestation — integration-builder

## Status

| Field | Value |
|---|---|
| Historical issue / PR | #1205 / merged PR #1206 |
| Reconciliation issue | #1208 |
| Reconciliation PR | Pending creation |
| Candidate | `integration-builder` |
| Contract | `.github/agents/integration-builder.md` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Status | 🟠 EXECUTED — BLOCKED |

## Candidate Attestation

The candidate completed this attestation during the PR #1206 session. Foreman may verify but may not replace or infer candidate answers.

| ID | Candidate statement | Response | Evidence / Notes |
|---|---|---|---|
| CA-01 | I have read my current contract and will act only within its authority. | YES | Candidate session bootstrapped and read the `integration-builder` contract. |
| CA-02 | I have read all mandatory governance and AMC Stage 1–9 authority inputs applicable to W1. | **NO** | Candidate did not complete the full mandatory set. The Foreman completed a later reconciliation review, but that cannot replace candidate acknowledgement. |
| CA-03 | I understand W1 scope and can explain it without ambiguity. | YES | Runtime foundation, CI posture, preview/staging separation, environment contract, secret boundaries and initial deployment plumbing only. |
| CA-04 | I can identify all applicable W1 RED tests and evidence obligations. | YES | QA-DEPLOY-001/002/003/004/006/007/010 plus applicable QA-CONFIG and QA-DES controls. |
| CA-05 | I will not weaken, skip, delete, trivialise or rewrite tests around implementation. | YES | Candidate commitment recorded. |
| CA-06 | I understand CI, preview, environment, workflow ownership, secret separation and no-production-side-effect constraints. | YES | Candidate commitment recorded. |
| CA-07 | I have or can obtain governed access to required GitHub, Vercel, Supabase and non-production resources. | **NO** | Repository/workflow visibility was demonstrated. Vercel/Supabase candidate permissions, protected-production and preview/staging isolation remain incompletely evidenced. |
| CA-08 | I will produce all required W1 evidence before claiming completion. | YES | Candidate commitment recorded. |
| CA-09 | I will stop and escalate ambiguity, access failures, gate failures, architecture conflicts or authority mismatches. | YES | Candidate commitment recorded. |
| CA-10 | I understand this attestation does not appoint me or authorize implementation. | YES | Candidate acknowledgement recorded. |

**Candidate result**: EXECUTED — BLOCKED (`CA-02` and `CA-07` remain NO).

## Reconciled Environment Facts

- Supabase production: `icawesooswoqzepcdevg` — healthy.
- Supabase non-production: `develop`, project ref `kkksclwvbmyexpsdyejj` — healthy.
- Vercel project `app-management-centre` exists and preview evidence has been observed.
- AMC Vercel repository secret names are present; values are not recorded.
- Build-to-Green phase configuration is enabled.

These facts materially improve readiness but do not prove the candidate-specific permission and isolation boundaries required to turn CA-07 into YES.

## Foreman Verification

| ID | Verification | Result | Evidence / Notes |
|---|---|---|---|
| FV-01 | Contract exists and grants builder authority in AMC | PASS | Contract reviewed. |
| FV-02 | Candidate class is plausibly suited to W1 | PASS — CLASS FIT ONLY | Integration/runtime foundation capability is relevant. |
| FV-03 | Candidate W1 comprehension verified | PASS | Candidate explanation is coherent and matches Stage 8/9 scope. |
| FV-04 | Candidate RED-test comprehension verified | PASS | Candidate identified the applicable W1 obligations. |
| FV-05 | Required access and dependencies verified | BLOCKED | Candidate-specific Vercel/Supabase permissions and environment isolation remain incomplete. |
| FV-06 | Build-to-Green blocking posture verified | PARTIAL PASS | Phase switch is enabled; later implementation-path enforcement still requires workflow execution evidence. |
| FV-07 | Final role-fit confirmed | BLOCKED | Cannot approve while CA-02, CA-07 and FV-05 remain unresolved. |

**Foreman result**: BLOCKED.

## Final Outcome

**FINAL RESULT: BLOCKED**

Stage 10 consideration, Stage 11 appointment and Stage 12 implementation remain prohibited.
