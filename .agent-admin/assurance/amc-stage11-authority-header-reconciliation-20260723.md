# AMC Stage 11 Active Authority-Header Reconciliation

## Rule

Only current authority surfaces are normalized. Historical decision, PR, assurance, session and evidence records remain unchanged.

| Stage | Normalized surfaces | Current authority |
|---|---|---|
| 2 | Wiring index; CTA/API/Data/Audit matrix | #1121; PR #1186 retrofit input |
| 3 | App Description-to-FRS traceability | #1123 |
| 4 | TRS and traceability | Treated-as-approved progression #1131 |
| 5 | Architecture primary/supporting artifacts | #1197 / merged PR #1198 |
| 5a | DES primary/supporting artifacts | #1197 / merged PR #1198 |
| 6 | QA-to-Red primary/supporting artifacts | #1197 / merged PR #1198 |
| 7 | PBFAG primary/supporting artifacts | #1197 / merged PR #1198 |
| 8 | Implementation Plan family | Already aligned |
| 9 | Checklist, W1 correction and RED/evidence map | PR #1204 / merged PR #1216 |
| 10 | IAA carrier and pointer | Already aligned through merged PR #1218 |

## Legacy/protected surfaces

- `WAVE_1_IMPLEMENTATION_PROGRESS.md` is classified historical/legacy without rewriting its evidence.
- Root operating/alignment documents receive current lifecycle normalization.
- `.github/agents/foreman-v2-agent.md` retains stale protected posture wording and is not modified under #1222.
- The required-check manifest contains stale posture wording and no bootstrap-specific check; protected correction is routed to #1228.

## Result

Active Stage 1–10 module headers agree with live decisions. Protected agent/gate drift remains separately CS2-gated.
