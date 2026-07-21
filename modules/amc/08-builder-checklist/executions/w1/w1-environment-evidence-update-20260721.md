# AMC W1 Environment Evidence Update — 2026-07-21

## Governance Context

| Field | Value |
|---|---|
| Issue | #1205 |
| PR | #1206 |
| Candidate | `integration-builder` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Evidence classification | CS2-provided configuration evidence plus connector-verified Supabase metadata |
| Candidate readiness effect | Partial blocker resolution only |

## Environment Evidence Recorded

1. Supabase project `AMC` exists with project reference `icawesooswoqzepcdevg` and is connector-verified as `ACTIVE_HEALTHY` in `eu-west-1`.
2. Vercel project `app-management-centre` exists under the CS2-controlled Vercel team.
3. Supabase and Vercel are linked and production-scoped environment-variable names were populated without exposing values in this PR.
4. The Vercel Framework Preset was corrected from `Vite` to `Other`; root directory remains `./` and no build/output command is claimed before W1 runtime implementation.
5. CS2 confirmed the repository-level AMC deployment secret namespace is now present:
   - `AMC_VERCEL_ORG_ID`
   - `AMC_VERCEL_PROJECT_ID`
   - `AMC_VERCEL_TOKEN`
   - `AMC_VERCEL_AUTOMATION_BYPASS_SECRET`
6. The screenshot records names and presence only. No secret value is stored in the PR.

## Boundary

The existence of the four `AMC_VERCEL_*` secrets resolves the secret-name and initial provisioning portion of the environment requirement. It does not prove candidate access, preview/staging isolation, protected-production approval, workflow consumption, or a deployable AMC runtime. Those items remain BLOCKED until separately evidenced.
