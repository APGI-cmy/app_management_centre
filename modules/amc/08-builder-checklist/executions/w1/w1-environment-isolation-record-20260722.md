# AMC W1 Environment Isolation and Protected-Production Readiness Record

## Governance Context

| Field | Value |
|---|---|
| Model-correction issue / PR | #1215 / #1216 |
| Candidate | `integration-builder` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Corrected authority | `w1-bootstrap-readiness-model-correction-20260723.md` |
| Assessed by | Foreman proxy |
| Date reassessed | 2026-07-23 |
| Status | ✅ PASS AS STAGE 9 DESIGN/POLICY READINESS |

## 1. Confirmed Resources and Ownership

- Vercel project `app-management-centre` exists and produces PR previews.
- Supabase Production project `icawesooswoqzepcdevg` exists and is healthy.
- Supabase non-production branch `develop`, project ref `kkksclwvbmyexpsdyejj`, exists and is healthy.
- AMC Vercel repository secret names exist; no values are recorded.
- CS2 is the resource owner/custodian and Production approval authority.
- `ci.yml` and `deploy-frontend.yml` are W1 implementation outputs.
- `db-migrate.yml` is a W7 implementation output.

## 2. Binding Isolation Design

1. PR/Preview execution must use non-production credentials and the Supabase `develop` resource.
2. PR/Preview jobs must not receive Production credentials or mutate Production.
3. Production deployment requires a separately protected and approved path.
4. Production database migration remains outside W1 and requires authorized W7 controls.
5. Secret values may not appear in commits, logs, PR text or evidence artifacts.
6. Any ambiguity or failed binding requires immediate stop and escalation.

## 3. Stage 9 Readiness Assessment

| Requirement | Evidence | Result |
|---|---|---|
| Preview and Production resources are separately identified | Vercel Preview scope; Supabase `develop` and Production refs | PASS |
| Owners/custodians are identified | CS2-controlled resource ownership | PASS |
| Intended credential scopes are explicit | Preview/non-production versus protected Production design | PASS |
| Production approval path is explicit | Reviewed merge and CS2-controlled Production path | PASS AS POLICY |
| Candidate Production authority is prohibited | Contract, W1 scope and stop conditions | PASS |
| Failure/escalation path is explicit | Stop before side effect; escalate to Foreman/CS2 | PASS |
| Required implementation proof is enumerated | W1 build-exit evidence register | PASS |

## 4. Mandatory W1 Build-Exit Proof

The following remain mandatory after Stage 10, appointment and authorized W1 implementation:

- committed `ci.yml` and `deploy-frontend.yml`;
- inspected workflow environment and secret scopes;
- actual Preview-to-`develop` binding;
- proof Preview cannot receive Production credentials;
- proof PR work cannot deploy or migrate Production;
- executed CI/deployment/isolation logs;
- no-Production-side-effect evidence.

Failure to produce any item keeps W1 delivery RED and blocks completion.

## 5. Blocker Disposition

| Blocker | Corrected Stage 9 disposition |
|---|---|
| W1-BLK-003 — Preview/staging versus Production isolation | CLOSED AS READINESS DESIGN; executed enforcement remains W1 build-exit evidence |
| W1-BLK-004 — Protected Production and no-Production-mutation controls | CLOSED AS READINESS POLICY; executed enforcement remains W1/W7 evidence |

This record does not authorize Stage 10, appointment, implementation, migration or deployment.
