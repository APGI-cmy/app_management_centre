# AMC W1 Final Candidate Re-Attestation — `integration-builder`

## Status

| Field | Value |
|---|---|
| Governing issue | #1210 |
| Governing PR | #1211 |
| Candidate | `integration-builder` |
| Contract | `.github/agents/integration-builder.md` v3.4.0 |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Status | PENDING CANDIDATE-AUTHORED COMPLETION |

## Candidate-only instruction

This section must be completed by the candidate operating under the `integration-builder` contract. The Foreman may verify the answers but may not supply, infer, or rewrite them.

For each item, replace `PENDING` with `YES` or `NO` and add a concise candidate-authored evidence note. A single `NO`, unsupported `YES`, or unresolved ambiguity keeps W1 candidate readiness BLOCKED.

## Mandatory governance and authority acknowledgement

| ID | Candidate statement | Response | Candidate-authored evidence note |
|---|---|---|---|
| RA-01 | I read my complete current `integration-builder` contract and understand its builder-only authority. | PENDING | |
| RA-02 | I read `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md`. | PENDING | |
| RA-03 | I read `governance/canon/BUILD_PHILOSOPHY.md`. | PENDING | |
| RA-04 | I read `governance/canon/STOP_AND_FIX_DOCTRINE.md`. | PENDING | |
| RA-05 | I read `governance/canon/MERGE_GATE_INTERFACE_STANDARD.md`. | PENDING | |
| RA-06 | I read `governance/canon/EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md`. | PENDING | |
| RA-07 | I read the AMC Stage 5a deployment strategy and validation matrix applicable to W1. | PENDING | |
| RA-08 | I read the AMC Stage 6 QA-to-Red specification, W1 RED-test map, Stage 8 plan, wave breakdown and condition-import matrix. | PENDING | |
| RA-09 | I read the Stage 9 Builder Checklist, historical attestation, reconciliation record and current CS2 BLOCKED decision. | PENDING | |
| RA-10 | I understand ECAP is administrative, IAA is independent, the Foreman controls appointment/delegation, and I have no merge/release authority. | PENDING | |

## W1 scope and RED obligations

| ID | Candidate statement | Response | Candidate-authored evidence note |
|---|---|---|---|
| RA-11 | I understand W1 is limited to runtime foundation, CI posture, environment contract, Preview/Staging separation, secret boundaries and initial deployment plumbing after appointment. | PENDING | |
| RA-12 | I can identify the applicable W1 RED obligations, including QA-DEPLOY-001/002/003/004/006/007/010 and applicable configuration/deployment controls. | PENDING | |
| RA-13 | I will not weaken, skip, delete, trivialise or rewrite tests around implementation. | PENDING | |
| RA-14 | I will stop and escalate any ambiguity, missing authority, access failure, gate failure, architecture conflict or production-risk condition. | PENDING | |

## Governed access and isolation acknowledgement

| ID | Candidate statement | Response | Candidate-authored evidence note |
|---|---|---|---|
| RA-15 | I can work on the governed GitHub branch and PR through normal repository controls and do not require branch-protection bypass or direct merge authority. | PENDING | |
| RA-16 | I understand Vercel Preview is the only permitted deployment target for PR work until a later protected Production workflow and approval exist. | PENDING | |
| RA-17 | I understand Preview work must use non-production environment-variable scope and must not rely on Production-only secrets or data. | PENDING | |
| RA-18 | I understand Supabase `develop` (`kkksclwvbmyexpsdyejj`) is the non-production target and production (`icawesooswoqzepcdevg`) must not be mutated by PR/Preview work. | PENDING | |
| RA-19 | I will not merge, reset or rebase the Supabase branch, run production migrations, deploy Vercel Production, or mutate production data without explicit later authority and protected approval. | PENDING | |
| RA-20 | I will use governed repository/workflow secrets only and will never expose secret values in code, logs, issues, PRs or evidence. | PENDING | |

## Evidence and appointment boundary

| ID | Candidate statement | Response | Candidate-authored evidence note |
|---|---|---|---|
| RA-21 | I will produce every required W1 evidence class before claiming completion. | PENDING | |
| RA-22 | I understand `ci.yml` and `deploy-frontend.yml` are W1 implementation outputs and `db-migrate.yml` is a W7 output; their present absence does not authorize me to create them before appointment. | PENDING | |
| RA-23 | I understand this re-attestation does not appoint me, delegate W1, open Stage 10, or authorize implementation. | PENDING | |
| RA-24 | I accept that the Foreman may approve final role-fit only after independently verifying these answers and the governed access/isolation evidence. | PENDING | |

## Candidate declaration

Candidate identity: `integration-builder`  
Candidate-authored completion date: PENDING  
Candidate result: PENDING

The candidate must state one of:

- `FINAL CANDIDATE RESULT: PASS — all RA-01 through RA-24 are YES and evidenced`; or
- `FINAL CANDIDATE RESULT: BLOCKED — <list all NO/PENDING/unsupported items>`.

## Foreman verification

Not yet executed. The Foreman must not complete this section until the candidate-authored section above is complete.

| ID | Verification | Result | Evidence / Notes |
|---|---|---|---|
| RFV-01 | Candidate identity and contract authority verified | PENDING | |
| RFV-02 | Full governance-reading acknowledgement verified | PENDING | |
| RFV-03 | W1 scope and RED-test comprehension verified | PENDING | |
| RFV-04 | GitHub/Vercel/Supabase boundary acknowledgement verified | PENDING | |
| RFV-05 | Preview/production and no-production-mutation controls verified | PENDING | |
| RFV-06 | Stop conditions and evidence commitments verified | PENDING | |
| RFV-07 | Final W1 role-fit approved | PENDING | |

No Stage 10, appointment, delegation or implementation authority exists while any item remains PENDING, NO or unsupported.