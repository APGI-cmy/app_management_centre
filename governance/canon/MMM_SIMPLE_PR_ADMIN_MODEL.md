
**Status**: CANONICAL | **Version**: 1.2.0 | **Authority**: CS2
**Date**: 2026-05-05
**Amended**: 2026-05-06 — v1.1.0: Added `execution_model` field to schema and Check 13 enforcement per POLC_EXECUTION_MODEL_CANON.md; authority: CS2 — Canon alignment: require explicit execution_model for implementation PRs.
**Amended**: 2026-05-07 — v1.2.0: Expanded governance-control path coverage to include `governance/**` (all sub-paths) and `.agent-admin/**`; aligned with upstream validator parity; updated Tier 1/2 policy bindings for single-source-of-truth and manifest-era product-fix simplification.
**Canon ID**: SPAM-001
**Issue**: #1163
**Layered Down**: APGI-cmy/maturion-foreman-governance commit 77a8297bc2408bbc1c224083fd6028affb052107

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
| `execution_model` | string | enum (see §3.4) | Execution control model. **Required when implementation files are changed** (see §3.4 and §7). |
| `implementing_agent` | string | — | Required when `execution_model` is `builder-governed` or `foreman-orchestrated`. |
| `orchestrating_agent` | string | — | Required when `execution_model` is `foreman-orchestrated`. |
| `cs2_justification` | string | — | Required when `execution_model` is `cs2-hotfix-override`. Non-empty justification text or issue/PR reference. |

No additional properties are allowed (`additionalProperties: false`).

### 3.4 Execution Model Values

When `execution_model` is declared, it MUST be one of:

| Value | When to use | Required companion fields |
|-------|-------------|--------------------------|
| `builder-governed` | PR directly owned and executed by an authorised builder agent | `implementing_agent` |
| `foreman-orchestrated` | Foreman scopes work and delegates to a builder | `orchestrating_agent`, `implementing_agent` |
| `cs2-hotfix-override` | Scoped CS2-approved emergency exception | `cs2_justification` |

**Authority**: `governance/canon/POLC_EXECUTION_MODEL_CANON.md`

### 3.5 Examples

#### product-fix (no implementation files):
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

#### product-fix with implementation files (builder-governed):
```json
{
  "type": "product-fix",
  "requires_iaa": false,
  "requires_ecap": false,
  "governing_issue": "#1234",
  "scope_summary": "Fix pagination bug in dashboard module.",
  "created_by": "api-builder",
  "created_at": "2026-05-07T10:00:00Z",
  "execution_model": "builder-governed",
  "implementing_agent": "api-builder"
}
```

#### product-fix with implementation files (foreman-orchestrated):
```json
{
  "type": "product-fix",
  "requires_iaa": false,
  "requires_ecap": false,
  "governing_issue": "#1234",
  "scope_summary": "Foreman-delegated fix for ISMS module.",
  "created_by": "foreman-v2-agent",
  "created_at": "2026-05-07T10:00:00Z",
  "execution_model": "foreman-orchestrated",
  "orchestrating_agent": "foreman-v2-agent",
  "implementing_agent": "api-builder"
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
| `.github/workflows/**` | CI gate workflow modifications |
| `.github/scripts/**` | CI gate script modifications |
| `governance/**` | Governance canon modifications (all sub-paths) |
| `.governance-pack/**` | Governance pack / CANON_INVENTORY modifications |
| `.agent-workspace/**/knowledge/**` | Agent Tier 2 knowledge modifications |
| `.agent-admin/**` | Wave records, ECAP bundles, ceremony evidence |
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

## 7. Execution Model Requirement (Check 13)

**Authority**: `governance/canon/POLC_EXECUTION_MODEL_CANON.md`

Any PR whose diff (or scope) contains implementation files MUST include an `execution_model` field
in `.admin/pr.json`. The validator enforces this as Check 13.

**Implementation file patterns** (triggers `execution_model` enforcement):

```
apps/
src/
modules/
lib/
packages/
```

PRs that only change governance-control paths (`.github/`, `governance/`, `*.agent.md`) or
docs-only content do not require `execution_model`.

**Enforcement rules**:

- If implementation files are detected in the diff AND `execution_model` is missing → FAIL.
- If `execution_model` is present but not one of the accepted values → FAIL.
- If `execution_model = builder-governed` and `implementing_agent` is missing or empty → FAIL.
- If `execution_model = foreman-orchestrated` and `orchestrating_agent` or `implementing_agent` is missing or empty → FAIL.
- If `execution_model = cs2-hotfix-override` and `cs2_justification` is missing or empty → FAIL.

---

## 8. Business Rules

| ID | Rule |
|----|------|
| BR-01 | `requires_iaa` MUST be `true` if `type` is `governance-control`, `agent-contract`, `migration`, `deployment`, or `high-risk`. |
| BR-02 | `requires_ecap` MUST be `true` if `type` is `governance-control`, `agent-contract`, `migration`, `deployment`, or `high-risk`. |
| BR-03 | If `.admin/pr.json` is absent → full ceremony (same as current behavior). |
| BR-04 | If `.admin/pr.json` is present but fails JSON parse, is missing any required field (`type`, `requires_iaa`, `requires_ecap`, `governing_issue`, `scope_summary`), has non-boolean values for `requires_iaa`/`requires_ecap`, or has a `type` value outside the recognised enum (`product-fix`, `docs-only`, `governance-control`, `agent-contract`, `migration`, `deployment`, `high-risk`) → treat as absent → full ceremony. CI gates MUST validate field types, not just parse JSON. |
| BR-05 | If `.admin/pr.json` declares `requires_iaa: false` but forced-ceremony paths are detected in the diff → full ceremony reinstated; CI gate must log an override warning. |
| BR-06 | CI gates must use `python3` or `jq` to parse `.admin/pr.json`. String matching on the raw file content is prohibited. |
| BR-07 | If implementation files are detected in the PR diff AND `execution_model` is absent → FAIL (Check 13). Authority: `governance/canon/POLC_EXECUTION_MODEL_CANON.md`. |
| BR-08 | `execution_model` companion fields are mandatory per the model: `implementing_agent` for `builder-governed`; `orchestrating_agent` + `implementing_agent` for `foreman-orchestrated`; `cs2_justification` for `cs2-hotfix-override`. |

---

## 9. Validator

The validator script `.github/scripts/validate-simple-pr-admin.sh`:

- Fails if `.admin/pr.json` is missing
- Validates all required JSON fields exist
- Validates `requires_iaa` and `requires_ecap` are boolean
- Validates `type` is one of the accepted values
- Validates `governing_issue` matches pattern `^#[0-9]+$`
- Validates `scope_summary` is 10–500 characters
- Fails if governance-control files are changed and `requires_iaa`/`requires_ecap` are not `true`
- **Fails if implementation files are in the diff and `execution_model` is missing** (Check 13)
- Fails if `execution_model` is present but is not one of the accepted values
- Fails if `execution_model = builder-governed` and `implementing_agent` is missing or empty
- Fails if `execution_model = foreman-orchestrated` and `orchestrating_agent` or `implementing_agent` is missing or empty
- Fails if `execution_model = cs2-hotfix-override` and `cs2_justification` is missing or empty

**Governance-control file patterns** (triggers `requires_iaa`/`requires_ecap` enforcement):

```
.github/workflows/
.github/scripts/
.github/agents/
governance/           (all sub-paths: canon/, templates/, policies/, checklists/, etc.)
.agent-admin/
*.agent.md files (agent contracts)
```

---

## 10. References

- `governance/canon/POLC_EXECUTION_MODEL_CANON.md` — Execution model canon: defines the three
  allowed execution models and their enforcement requirements.
- `governance/canon/AGENT_HANDOVER_AUTOMATION.md` §4.3f — Simple Admin Model Exception: defines which
  Phase 4 ceremony steps are waived and which remain required for Simple Admin PRs.
- `governance/canon/EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` (ECAP-001) §2.4 — Product-Fix PR
  Exception: defines when ECAP appointment is not required.
- `governance/canon/INDEPENDENT_ASSURANCE_AGENT_CANON.md` — IAA canon: defines IAA invocation rules.

---

**Version**: 1.2.0
**Authority**: CS2 (Johan Ras)
**Effective**: 2026-05-05
**Last Amended**: 2026-05-07
