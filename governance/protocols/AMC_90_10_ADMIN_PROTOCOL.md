# AMC 90/10 Admin Protocol

> **Version**: 1.0.0
> **Authority**: CS2 (@APGI-cmy) — Issue #1063
> **Effective**: 2026-04-13
> **Status**: ACTIVE
> **Supersedes**: Legacy multi-artifact admin model (prebrief + token + rejection + handover + session memory as separate files)

---

## 1. Purpose

This protocol establishes the **90/10 evaluation-to-admin principle** for the AMC repository:

- **90%** of agent effort goes to **evaluation, building, and quality work**
- **10%** of agent effort goes to **admin, ceremony, and artifact tracking**

The legacy admin model created unsustainable file and evidence overhead through fragmented artifact
requirements per wave (separate prebrief, token, rejection, handover, and session memory files).
This protocol consolidates all per-wave admin into a single artifact and reduces session memory
to the minimum fields needed for real audit.

---

## 2. Consolidated Wave Record Model

### 2.1 Single Artifact Per Wave

Each governance wave produces exactly **one** consolidated artifact:

```
.agent-admin/wave-records/amc-wave-record-{wave-slug}-{YYYYMMDD}.md
```

This single file replaces:
- ~~`.agent-admin/assurance/iaa-prebrief-*.md`~~ (scope section in wave record)
- ~~`.agent-admin/assurance/iaa-token-*.md`~~ (assurance section in wave record)
- ~~`.agent-admin/assurance/iaa-rejection-*.md`~~ (failure trail section in wave record)
- ~~`.agent-admin/prehandover/PREHANDOVER_PROOF_*.md`~~ (evaluation section in wave record)
- ~~`.agent-workspace/*/memory/session-*.md`~~ (reduced session memory — see §3)

### 2.2 Template

Use: `.agent-admin/templates/amc-wave-record-template.md`

### 2.3 Failure Trail

Rejection packages and failure details are recorded **inline** in the wave record's
failure trail section — not as separate files. Only persistent invalidated artifacts
(e.g., a revoked token that must remain for audit) are kept separately under
`.agent-admin/archive/invalidated/`.

---

## 3. Reduced Session Memory (6-Field Model)

Session memory is reduced from 18+ fields to 6 essential fields plus CI-gated fields:

| # | Field | Purpose |
|---|-------|---------|
| 1 | `session_id` + `wave_id` + `date` | Identity triple — who, what, when |
| 2 | `phase_1_preflight` | CI-gated field — proves preflight was executed |
| 3 | `triggering_issue` | Traceability — links to governing issue |
| 4 | `outcome` | Result — COMPLETE / PARTIAL / ESCALATED |
| 5 | `coverage_summary` + `agents_delegated_to` | What was delivered and by whom |
| 6 | `learning` | Mandatory improvement note — never blank |

**Removed fields** (ceremony overhead — no longer required):
- `agent_version`, `contract_version` (derivable from git)
- `fail_only_once_attested`, `fail_only_once_version`, `unresolved_breaches` (internal ceremony)
- `wave_verb`, `wave_classification`, `implementation_guard_triggered` (internal mode tracking)
- `prior_sessions_reviewed`, `unresolved_items_from_prior_sessions` (ceremony)
- `roles_invoked`, `mode_transitions` (internal state tracking)
- `escalations_triggered` (moved to wave record failure trail)
- `separation_violations_detected` (ceremony)
- `iaa_prebrief_artifact`, `iaa_prebrief_wave`, `iaa_prebrief_tasks_count`, `iaa_final_audit_token` (moved to wave record)
- `QP Verdicts` (moved to wave record)
- `Parking Station` (ceremony)

---

## 4. Allowed Governance Artifact Paths

### 4.1 Allowed Paths (CI-enforced)

New governance artifacts may only be created in these paths:

| Path Pattern | Purpose |
|-------------|---------|
| `.agent-admin/wave-records/amc-wave-record-*.md` | Consolidated wave records |
| `.agent-admin/archive/**` | Archived/deprecated artifacts |
| `.agent-admin/governance/**` | Governance state (sync_state, ripple, etc.) |
| `.agent-admin/templates/**` | Approved templates |
| `.agent-workspace/*/memory/session-*.md` | Reduced session memory |
| `.agent-workspace/*/personal/wave-current-tasks.md` | Wave task tracking |

### 4.2 Deprecated Paths (CI-blocked for new files)

No new files may be created in these paths:

| Path Pattern | Reason |
|-------------|--------|
| `.agent-admin/assurance/iaa-prebrief-*.md` | Replaced by wave record scope section |
| `.agent-admin/assurance/iaa-token-*.md` | Replaced by wave record assurance section |
| `.agent-admin/assurance/iaa-rejection-*.md` | Replaced by wave record failure trail |
| `.agent-admin/prehandover/PREHANDOVER_PROOF_*.md` | Replaced by wave record evaluation section |

### 4.3 CI Enforcement

The `governance-artifact-enforcement.yml` workflow:
1. Detects new files in PRs
2. Checks against the allowed paths taxonomy
3. Blocks merge if new files are created in deprecated paths
4. Requires `allowed_artifact_paths` field in `wave-current-tasks.md`

---

## 5. Migration Rules

### 5.1 Existing Artifacts

All existing artifacts in `.agent-admin/assurance/` and `.agent-admin/prehandover/` are
**preserved as-is** for audit trail. They are not deleted or moved.

### 5.2 New Waves

All waves started after this protocol's effective date MUST use the consolidated
wave record model. The legacy separate-file model is discontinued.

### 5.3 Archive

Legacy templates are archived under `.agent-admin/archive/legacy-templates/` with
a README explaining the deprecation.

---

## 6. Cross-References

- Issue: #1063
- ISMS references: maturion-isms#1347, #1354, #1356
- Governance Artifact Taxonomy: `governance/canon/GOVERNANCE_ARTIFACT_TAXONOMY.md`
- Wave record template: `.agent-admin/templates/amc-wave-record-template.md`
- Session memory template: `.agent-workspace/foreman-v2/knowledge/session-memory-template.md` (v2.0.0)

---

## 7. Version History

| Version | Date | Change | Authority |
|---------|------|--------|-----------|
| 1.0.0 | 2026-04-13 | Initial — 90/10 principle, consolidated wave records, 6-field session memory | CS2 (@APGI-cmy) — Issue #1063 |
