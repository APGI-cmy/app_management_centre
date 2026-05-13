# .admin/ — AMC PR Administration Manifest Directory

**Authority**: CS2 (@APGI-cmy) — Issue #1163 | SPAM-001 (MMM_SIMPLE_PR_ADMIN_MODEL.md v1.2.0)
**Purpose**: Per-PR manifest for the AMC Simple PR Admin Model ceremony level declaration.

## Overview

The `.admin/` directory contains a per-PR manifest file (`pr.json`) that declares the PR's
type and ceremony requirements. CI gates read this manifest to determine whether the PR
qualifies for the Simple Admin Model (reduced ceremony) or requires full governance ceremony.

## Usage

When creating a PR, add `.admin/pr.json` to declare:
- PR type: `product-fix`, `docs-only`, or one of the full-ceremony types
- Whether IAA and ECAP ceremony are required
- A brief scope summary and reference to the governing issue
- **Execution model** (required when implementation files are changed)

## `.admin/pr.json` Schema

See `.admin/pr.json.schema.json` for the full JSON Schema.

### Minimal product-fix example (no implementation files):
```json
{
  "type": "product-fix",
  "requires_iaa": false,
  "requires_ecap": false,
  "governing_issue": "#1234",
  "scope_summary": "Fix button label typo on dashboard",
  "created_by": "api-builder",
  "created_at": "2026-05-05T10:00:00Z"
}
```

### Product-fix with implementation files (builder-governed):
```json
{
  "type": "product-fix",
  "requires_iaa": false,
  "requires_ecap": false,
  "governing_issue": "#1234",
  "scope_summary": "Fix pagination bug in the dashboard module.",
  "created_by": "api-builder",
  "created_at": "2026-05-07T10:00:00Z",
  "execution_model": "builder-governed",
  "implementing_agent": "api-builder"
}
```

### Product-fix with implementation files (foreman-orchestrated):
```json
{
  "type": "product-fix",
  "requires_iaa": false,
  "requires_ecap": false,
  "governing_issue": "#1234",
  "scope_summary": "Foreman-delegated fix for ISMS module pagination.",
  "created_by": "foreman-v2-agent",
  "created_at": "2026-05-07T10:00:00Z",
  "execution_model": "foreman-orchestrated",
  "orchestrating_agent": "foreman-v2-agent",
  "implementing_agent": "api-builder"
}
```

### CS2 hotfix override (emergency use only):
```json
{
  "type": "product-fix",
  "requires_iaa": false,
  "requires_ecap": false,
  "governing_issue": "#9999",
  "scope_summary": "Emergency fix for production outage in login flow.",
  "created_by": "cs2",
  "created_at": "2026-05-07T10:00:00Z",
  "execution_model": "cs2-hotfix-override",
  "cs2_justification": "CS2 approved emergency exception per issue #9999 — production login failure affecting all users"
}
```

### Governance-control PR (full ceremony):
```json
{
  "type": "governance-control",
  "requires_iaa": true,
  "requires_ecap": true,
  "governing_issue": "#1172",
  "scope_summary": "Layer-down POLC execution model canon and update Simple PR Admin Model to v1.2.0.",
  "created_by": "governance-liaison-amc-agent",
  "created_at": "2026-05-12T10:00:00Z"
}
```

## Execution Model Field

**Authority**: `governance/canon/POLC_EXECUTION_MODEL_CANON.md` v1.0.0

Any PR whose diff contains implementation files (`apps/`, `src/`, `modules/`, `lib/`, `packages/`)
MUST include an `execution_model` field. The validator enforces this as Check 13.

| `execution_model` value | When to use | Required companion fields |
|------------------------|-------------|--------------------------|
| `builder-governed` | PR directly owned by an authorised builder agent | `implementing_agent` |
| `foreman-orchestrated` | Foreman scopes and delegates to a builder | `orchestrating_agent`, `implementing_agent` |
| `cs2-hotfix-override` | Scoped CS2-approved emergency exception | `cs2_justification` |

PRs that only change governance-control paths (`.github/`, `governance/`, `*.agent.md`) do not
require `execution_model`.

## When simple admin does NOT apply

Even with `requires_iaa: false`, full ceremony is reinstated if the PR diff touches:
- `.github/agents/**`
- `.github/workflows/**`
- `.github/scripts/**`
- `governance/**`
- `.governance-pack/**`
- `.agent-workspace/**/knowledge/**`
- `.agent-admin/**`
- `supabase/migrations/**`
- `schema/` or `migrations/` paths
- `BUILD_PROGRESS_TRACKER*`

For governance, agent-contract, migration, deployment, and high-risk PRs, always use
`requires_iaa: true` and `requires_ecap: true`.

## Preserved Controls

The following CI gates are NEVER downgraded regardless of `.admin/pr.json`:
- POLC boundary validation (foreman-implementation-check, builder-involvement-check)
- Build-to-green enforcement
- Agent contract format gate
- Agent boundary gate
- Agent bootstrap inject gate

## Validator

Run the validator locally:
```bash
.github/scripts/validate-simple-pr-admin.sh --manifest .admin/pr.json
```

With explicit changed-files list:
```bash
.github/scripts/validate-simple-pr-admin.sh \
  --manifest .admin/pr.json \
  --changed-files /tmp/changed_files.txt
```

## Authority

SPAM-001 — `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` v1.2.0
POLC Execution Model — `governance/canon/POLC_EXECUTION_MODEL_CANON.md` v1.0.0

