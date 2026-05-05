
**Status**: CANONICAL | **Version**: 1.0.0 | **Authority**: CS2
**Date**: 2026-05-05
**Canon ID**: SPAM-001
**Issue**: #1163

> **Amendment Authority**: Only CS2 (Johan Ras / repo owner) may amend this canon. Any PR
> modifying this file without CS2 sign-off is auto-FAIL at the merge gate.

---

# AMC Simple PR Admin Model (SPAM-001)

## 1. Purpose

This canon defines the **two-tier PR ceremony model** for AMC. It establishes lightweight
("Simple Admin") ceremony for low-risk PRs, while preserving full ceremony for PRs that touch
governance, agent contracts, migrations, deployments, and other high-risk change surfaces.

**Product-fix** and **docs-only** PRs may use Simple Admin mode via `.admin/pr.json`.
**Governance, agent-contract, migration, deployment, and high-risk PRs always require full
ceremony** regardless of any `.admin/pr.json` declaration.

This model is the AMC equivalent of the `maturion-isms#1530` Simple PR Admin Model.

---

## 2. PR Type Classification

The following PR types are recognised by this model. The `Ceremony Level` column is normative.

| Type | Ceremony Level | `requires_iaa` | `requires_ecap` | Notes |
|------|---------------|-----------------|-----------------|-------|
| `product-fix` | Simple Admin | false | false | Small functional fixes, minor UI/config changes |
| `docs-only` | Simple Admin | false | false | Documentation-only changes (no governance artifacts) |
| `governance-control` | Full Ceremony | true | true | Governance canon or control infrastructure changes |
| `agent-contract` | Full Ceremony | true | true | Changes to `.github/agents/**` |
| `migration` | Full Ceremony | true | true | Database schema changes |
| `deployment` | Full Ceremony | true | true | Infrastructure/deployment configuration |
| `high-risk` | Full Ceremony | true | true | Any PR classified as high-risk by author/Foreman |

---

## 3. `.admin/pr.json` Schema

### 3.1 File Location

`.admin/pr.json` — per-PR manifest, created by the PR author (or by the Foreman/builder on behalf
of the PR author). This file lives in the repo root `.admin/` directory and is committed as part
of the PR branch.

### 3.2 Required Fields

| Field | Type | Constraint | Description |
|-------|------|-----------|-------------|
| `type` | string | enum (see §2) | PR classification type |
| `requires_iaa` | boolean | — | Whether IAA final assurance is required |
| `requires_ecap` | boolean | — | Whether ECAP ceremony is required |
| `governing_issue` | string | pattern `^#[0-9]+$` | Reference to governing issue (e.g., `"#1163"`) |
| `scope_summary` | string | 10–500 chars | Brief human-readable description of what this PR does |

### 3.3 Optional Fields

| Field | Type | Constraint | Description |
|-------|------|-----------|-------------|
| `created_by` | string | — | Agent or user ID that created this manifest |
| `created_at` | string | ISO-8601 datetime | Timestamp when manifest was created |

No additional properties are allowed (`additionalProperties: false`).

### 3.4 Example

```json
{
  "type": "product-fix",
  "requires_iaa": false,
  "requires_ecap": false,
  "governing_issue": "#1163",
  "scope_summary": "Fix typo in dashboard label and correct off-by-one in pagination count.",
  "created_by": "copilot",
  "created_at": "2026-05-05T10:00:00Z"
}
```

---

## 4. Simple Admin Mode Activation

Simple Admin mode is active **only** when ALL of the following conditions are simultaneously true:

1. `.admin/pr.json` **exists** at the PR branch HEAD and is **valid JSON**.
2. `.admin/pr.json` `type` field is `product-fix` or `docs-only`.
3. `.admin/pr.json` `requires_iaa` is `false`.
4. `.admin/pr.json` `requires_ecap` is `false`.
5. **No forced-ceremony path** is detected in the PR diff (see §5).

If any condition is not met, full ceremony applies.

---

## 5. Forced-Ceremony Override

The following paths in the PR diff **always reinstate full ceremony**, regardless of any
`.admin/pr.json` declaration. CI gates MUST check for these paths after reading `.admin/pr.json`.

| Path Pattern | Reason |
|-------------|--------|
| `.github/agents/**` | Agent contract modifications |
| `governance/**` | Governance canon modifications |
| `.governance-pack/**` | Governance pack / CANON_INVENTORY modifications |
| `.agent-workspace/**/knowledge/**` | Agent Tier 2 knowledge modifications |
| `supabase/migrations/**` | Database migration files |
| `schema/` (path prefix) | Schema directory changes |
| `migrations/` (path prefix) | Migrations directory changes |
| `BUILD_PROGRESS_TRACKER*` | Build progress tracker files |

When a forced-ceremony path is detected after reading `.admin/pr.json`:
- CI gate **must log an override warning** identifying the forced-ceremony path.
- Full ceremony is reinstated as if `.admin/pr.json` had not been provided.
- The Foreman and ECAP must verify forced-ceremony path status before proceeding without ceremony.

---

## 6. Preserved Controls

The following CI gates are **NEVER downgraded** regardless of `.admin/pr.json` declarations.
These controls remain active and blocking for all PRs regardless of ceremony level:

| Gate | File | What it protects |
|------|------|-----------------|
| POLC boundary validation (`foreman-implementation-check` and `builder-involvement-check`) | `polc-boundary-gate.yml` | POLC constitution boundary |
| Build-to-green enforcement | `build-to-green-enforcement.yml` | Green CI requirement |
| Agent contract format gate | `agent-contract-format-gate.yml` | Agent contract structure |
| Agent boundary gate | `agent-boundary-gate.yml` | Agent class boundary enforcement |
| Agent bootstrap inject gate | `agent-bootstrap-inject.yml` | Agent bootstrap directive enforcement |

---

## 7. Business Rules

| ID | Rule |
|----|------|
| BR-01 | `requires_iaa` MUST be `true` if `type` is `governance-control`, `agent-contract`, `migration`, `deployment`, or `high-risk`. |
| BR-02 | `requires_ecap` MUST be `true` if `type` is `governance-control`, `agent-contract`, `migration`, `deployment`, or `high-risk`. |
| BR-03 | If `.admin/pr.json` is absent → full ceremony (same as current behavior). |
| BR-04 | If `.admin/pr.json` is present but invalid JSON or fails schema validation → treat as absent → full ceremony. |
| BR-05 | If `.admin/pr.json` declares `requires_iaa: false` but forced-ceremony paths are detected in the diff → full ceremony reinstated; CI gate must log an override warning. |
| BR-06 | CI gates must use `python3` or `jq` to parse `.admin/pr.json`. String matching on the raw file content is prohibited. |

---

## 8. References

- `governance/canon/AGENT_HANDOVER_AUTOMATION.md` §4.3f — Simple Admin Model Exception: defines which
  Phase 4 ceremony steps are waived and which remain required for Simple Admin PRs.
- `governance/canon/EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` (ECAP-001) §2.4 — Product-Fix PR
  Exception: defines when ECAP appointment is not required.
- `governance/canon/INDEPENDENT_ASSURANCE_AGENT_CANON.md` — IAA canon: defines IAA invocation rules.

---

**Version**: 1.0.0
**Authority**: CS2 (Johan Ras)
**Effective**: 2026-05-05
