# Issue #1226 — Foreman QA Execution Carrier

## Authority

- Governing issue: #1226
- Parent disposition: merged PR #1229
- Accepted base commit: `1d93459509abb92467f91deb4eefb879c1497362`
- Execution branch: `qa/issue-1226-stage6-executable-red-r2`
- Role: `qa-builder`
- Stage: Stage 6 re-entry / executable QA-to-Red only
- `integration-builder`: NOT APPOINTED
- Stage 12 authority: false

## Purpose

This Foreman-owned carrier exists only to open the single governed draft PR for the bounded QA-builder session. It does not constitute QA-builder attestation, test evidence, Foreman QP, ECAP, IAA, or Stage 6 completion.

## Tool-compatible preflight rule

Because the Copilot session reported that it could not create the prescribed branch and could not post an issue comment, the branch and draft PR are created by the Foreman.

Before any substantive QA file write, Copilot must add the following builder-owned carrier as its first commit in this PR:

`qa/evidence/issue-1226/QA_BUILDER_PHASE1_ATTESTATION.md`

That file must record:

- `agent_id: qa-builder`
- contract path `.github/agents/qa-builder.md`
- accepted base commit `1d93459509abb92467f91deb4eefb879c1497362`
- contract blob `3c6ce22423ceeca872bbb156063bda2ffeccc223`
- `phase_1_preflight: PREFLIGHT COMPLETE`
- `fallback_used: agent-bootstrap-work-mode-fallback-1228`
- bounded Stage 6 scope acknowledged
- stop conditions acknowledged
- confirmation that no substantive QA write preceded the attestation commit

## Allowed builder paths

- `tests/amc/stage6/**`
- `qa/evidence/issue-1226/**`
- `PREHANDOVER_PROOF_QA_BUILDER_1226_20260724.md`

No other path is authorised.
