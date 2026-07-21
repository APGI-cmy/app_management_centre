# AMC W1 Candidate Readiness Attestation — integration-builder

## Status

| Field | Value |
|---|---|
| Issue | #1205 |
| PR | #1206 |
| Candidate | `integration-builder` |
| Contract | `.github/agents/integration-builder.md` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Status | 🟠 EXECUTED — BLOCKED |

---

## Candidate Attestation

The candidate must complete each statement directly. No statement may be inferred by Foreman.

| ID | Candidate statement | Response | Evidence / Notes |
|---|---|---|---|
| CA-01 | I have read my current contract and will act only within its authority. | [x] YES [ ] NO | Executed `agent_bootstrap(agent_id: "integration-builder")` and read the returned contract in full during this session. |
| CA-02 | I have read all mandatory governance and AMC Stage 1–9 authority inputs applicable to W1. | [ ] YES [x] NO | Reviewed and understood in this session:<br>- issue `#1205` authority/scope/non-scope<br>- `integration-builder-readiness-checklist.md` (Stage 9 remains evaluation-only; PASS requires full evidence)<br>- `w1-red-test-and-evidence-map.md` (QA-DEPLOY/QA-CONFIG/QA-DES obligations)<br>- `w1-environment-and-dependency-register.md` (candidate-specific access and boundary evidence requirements)<br><br>Unverified governance-reading gaps that keep this item at NO:<br>- `modules/amc/08-builder-checklist/builder-checklist.md`<br>- `modules/amc/08-builder-checklist/builder-readiness-attestations.md`<br>- `modules/amc/07-implementation-plan/{implementation-plan.md,wave-breakdown.md,condition-import-matrix.md,cs2-decision-record-stage-8.md}`<br>- `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md`<br>- `governance/templates/BUILDER_CHECKLIST_TEMPLATE.md` |
| CA-03 | I understand W1 scope and can explain it without ambiguity. | [x] YES [ ] NO | W1 scope is runtime foundation/environment setup only: repository/runtime foundation, CI posture, preview/staging separation, environment contract, secret-boundary setup, and initial deployment plumbing. It explicitly excludes appointment, Stage 10, and implementation authorization. |
| CA-04 | I can identify all applicable W1 RED tests and evidence obligations. | [x] YES [ ] NO | From `w1-red-test-and-evidence-map.md`: QA-DEPLOY-001/002/003/004/006/007/010 plus applicable QA-CONFIG and QA-DES controls, with required evidence classes defined in that map. |
| CA-05 | I will not weaken, skip, delete, trivialise or rewrite tests around implementation. | [x] YES [ ] NO | Confirmed. I will treat any test weakening/bypass as prohibited and blocking. |
| CA-06 | I understand CI, preview, environment, workflow ownership, secret separation and no-production-side-effect constraints. | [x] YES [ ] NO | Confirmed. I understand readiness evidence must prove no production mutation side effects and environment/secret boundaries without exposing secret values. |
| CA-07 | I have or can obtain governed access to required GitHub, Vercel, Supabase and non-production resources. | [ ] YES [x] NO | Demonstrated in-session:<br>- local repository/branch visibility: `foreman/amc-stage9-w1-builder-readiness`<br>- GitHub Actions run visibility via MCP<br><br>Still BLOCKED (required proof not yet available in this session):<br>- ENV-01/ENV-02: candidate-specific GitHub repo/workflow access evidence record<br>- ENV-06/ENV-07: governed Vercel project access plus preview/staging isolation/protection evidence<br>- ENV-08/ENV-09: governed Supabase candidate access plus separate non-production project/branch evidence |
| CA-08 | I will produce all required W1 evidence before claiming completion. | [x] YES [ ] NO | Confirmed. No completion claim will be made without required W1 evidence classes. |
| CA-09 | I will stop and escalate ambiguity, access failures, gate failures, architecture conflicts or authority mismatches. | [x] YES [ ] NO | Confirmed stop-and-escalate posture for any ambiguity/failure condition. |
| CA-10 | I understand this attestation does not appoint me or authorize implementation. | [x] YES [ ] NO | Confirmed: this is Stage 9 candidate evaluation only; no appointment/delegation/implementation authority is created here. |

**Candidate result**: EXECUTED — BLOCKED (`CA-02` and `CA-07` unresolved)

---

## Foreman Verification

| ID | Verification | Result | Evidence / Notes |
|---|---|---|---|
| FV-01 | Contract exists and grants builder authority in AMC | PASS | Contract reviewed |
| FV-02 | Candidate class is plausibly suited to W1 | CONDITIONAL | Runtime/integration fit plausible; evidence pending |
| FV-03 | Candidate W1 comprehension verified | BLOCKED | Candidate response provided; Foreman verification still required |
| FV-04 | Candidate RED-test comprehension verified | BLOCKED | Candidate response provided; Foreman verification still required |
| FV-05 | Required access and dependencies verified | BLOCKED | Candidate cannot directly demonstrate governed Vercel/Supabase/non-production access in this session |
| FV-06 | Build-to-Green blocking posture verified for later implementation | BLOCKED | Evidence absent |
| FV-07 | Final role-fit confirmed | BLOCKED | Preconditions unresolved |

**Foreman result**: BLOCKED

---

## Final Outcome

**FINAL RESULT: BLOCKED**

Stage 10 consideration is prohibited until the candidate attestation is completed and every Foreman verification item is PASS.
