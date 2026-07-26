# Agent Bootstrap Work Mode Fallback — Issue #1228

## Status and scope

| Field | Value |
|---|---|
| Purpose | Truthful interim preflight for #1226 when repository-local stdio MCP is not exposed in ChatGPT Work Mode |
| Applies to | `qa-builder` bounded Stage 6 remediation only |
| Direct `agent_bootstrap` availability | unavailable in the verified Work Mode tool registry |
| CI enforcement claim | NOT MADE |
| Protected workflow/contract/canon change | none |
| Status | CS2-PROXY APPROVED FOR ISSUE #1226 ONLY — substantive IAA design review PASS at PR #1229 head `00e9a3872cbe912354c3ebd5009e53fedff4cb65`; final appointment remains subject to exact-head IAA PASS |

This fallback does not waive Phase 1. It replaces only the unavailable transport
mechanism with an auditable read-only contract-load sequence. Runtime surfaces
that expose the repository-local stdio MCP server must continue to call
`agent_bootstrap(agent_id: "qa-builder")` directly.

## Fixed contract identity

- Repository: `APGI-cmy/app_management_centre`
- Contract: `.github/agents/qa-builder.md`
- Verified PR #1229 branch blob SHA: `3c6ce22423ceeca872bbb156063bda2ffeccc223`
- Appointment must additionally bind the exact repository commit SHA used by
  the QA role.

## Mandatory first-action sequence

1. The QA role's first repository connector action must fetch the exact contract
   above at the appointment commit SHA. It must not first read Issue #1226, a PR,
   another repository file, or any task artifact.
2. The QA role must read the returned contract in full and complete Phase 1.
3. Before branch creation or any repository write, the QA role must post a
   preflight attestation to #1226 containing:
   - `agent_id: qa-builder`;
   - contract path, appointment commit SHA and returned blob SHA;
   - `phase_1_preflight: PREFLIGHT COMPLETE`;
   - acknowledgement of the bounded Stage 6 scope and all stop conditions;
   - confirmation that `agent_bootstrap` was unavailable and this approved
     fallback was used.
4. Foreman must verify that the attestation precedes the QA role's first commit.
   If the sequence cannot be proven, the delegation is invalid and the work
   must halt.

## Truthfulness and enforcement boundary

- Do not state that current CI enforces the unavailable first MCP call.
- Evidence is the immutable GitHub fetch identity, issue-attestation timestamp,
  first-commit timestamp and changed-file scope.
- No code, workflow, required-check, agent-contract or governance change is
  authorized by this fallback.
- This is not a repository-wide resolution of #1228. The issue remains open for
  supported MCP exposure and any separately CS2-authorized enforcement work.

## Failure conditions

HALT on contract SHA mismatch, truncated/unreadable contract, missing Phase 1
attestation, attestation after a repository write, use outside #1226, or any
claim that the fallback proves CI enforcement.
