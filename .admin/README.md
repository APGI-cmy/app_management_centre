# .admin/ — AMC PR Administration Manifest Directory

**Authority**: CS2 (@APGI-cmy) — Issue #1163 | SPAM-001 (MMM_SIMPLE_PR_ADMIN_MODEL.md)
**Purpose**: Per-PR manifest for the AMC Simple PR Admin Model ceremony level declaration.

## Overview

The `.admin/` directory contains a per-PR manifest file (`pr.json`) that declares the PR's
type and ceremony requirements. CI gates read this manifest to determine whether the PR
qualifies for the Simple Admin Model (reduced ceremony) or requires full governance ceremony.

## Usage

When creating a product-fix PR, add `.admin/pr.json` to declare:
- PR type: `product-fix` or `docs-only`
- Whether IAA and ECAP ceremony are required
- A brief scope summary and reference to the governing issue

## `.admin/pr.json` Schema

See `.admin/pr.json.schema.json` for the full JSON Schema.

### Minimal product-fix example:
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

### When simple admin does NOT apply:

Even with `requires_iaa: false`, full ceremony is reinstated if the PR diff touches:
- `.github/agents/**`
- `governance/**`
- `.governance-pack/**`
- `.agent-workspace/**/knowledge/**`
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

## Authority

SPAM-001 — `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` v1.0.0
