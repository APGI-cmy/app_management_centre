# AMC Stage 11 Infrastructure Verification — Issue #1222

## Scope

Read-only verification only. No credential values, environment mutation, database mutation, migration or deployment was performed.

## GitHub and Vercel

- PR #1220 head: `55dda91f5c1493f3219a9e1b91961e31755c29f0`.
- PR #1220 merge commit: `4546f65e80aca5e80e7f95717b8fe69bbf317cdc`.
- GitHub combined status reports Vercel success on both exact commits.
- Target URLs identify team `rassie-ras-projects` and project `app-management-centre`.
- The connected Vercel team lists only `apgi-public-website`.
- Fetching Vercel project `app-management-centre` returns 404.
- Fetching the two deployment targets through the connector returns deployment not found.

**Disposition:** B5 remains blocking. Ownership, Git mapping, environment assignment, domains and variable scopes are not independently verified. Proposed remediation: #1227.

## Supabase Production

Project `icawesooswoqzepcdevg` is `ACTIVE_HEALTHY` in `eu-west-1` on Postgres 17; it has migration `20260721144840_remote_schema`, no application base tables in `public`, enabled event trigger `ensure_rls`, and `public.rls_auto_enable()` is `SECURITY DEFINER` with EXECUTE granted to `PUBLIC`, `anon` and `authenticated`. Security advisors report both external-facing warnings.

- https://supabase.com/docs/guides/database/database-linter?lint=0028_anon_security_definer_function_executable
- https://supabase.com/docs/guides/database/database-linter?lint=0029_authenticated_security_definer_function_executable

## Supabase develop

Recorded project `kkksclwvbmyexpsdyejj` is absent from the current project list and direct retrieval returns `Project not found`. Migration, trigger, privilege, schema and RLS parity cannot be verified.

**Disposition:** B4 remains blocking. Proposed remediation: #1227. No risk is accepted and no database change is authorized.

## Render

The Stage 5/5a authority defines W1 through GitHub-hosted runners, Vercel and Supabase Cloud. No Render surface, workflow owner, environment or W1 evidence obligation exists.

**Disposition:** B6 closed as out of W1 scope. Any future Render surface requires an explicit Stage 5a amendment.
