# ALIGNMENT_EVIDENCE — session-036-20260512

**Session**: session-036-20260512
**Wave**: wave-layer-down-77a8297b-20260512
**Agent**: governance-liaison-amc-agent
**Date**: 2026-05-12
**Governing Issue**: #1172
**Canonical Source Commit**: `77a8297bc2408bbc1c224083fd6028affb052107`
**Canonical Repo**: `APGI-cmy/maturion-foreman-governance`

---

## Canonical Change Analysis

### 1. `governance/canon/POLC_EXECUTION_MODEL_CANON.md` — NEW (v1.0.0)

- **Upstream status**: NEW artifact, layer_down_status=PUBLIC_API
- **Consumer action**: CREATED
- **AMC adaptation**: Added local forward references; retained all canonical sections
- **Hash alignment**: SHA256 computed and recorded in GOVERNANCE_ALIGNMENT_INVENTORY.json

### 2. `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` — UPDATED (v1.0.0 → v1.2.0)

- **Upstream version**: 1.2.0
- **Consumer prior version**: 1.0.0
- **Change summary**:
  - v1.1.0 amendment (2026-05-06): Added `execution_model` field, Check 13 enforcement
  - v1.2.0 amendment (2026-05-07): Expanded governance-control path coverage to include
    `governance/**` (all sub-paths) and `.agent-admin/**`; aligned with validator parity
- **Consumer action**: UPDATED — full version bump with all amendments incorporated
- **Hash alignment**: SHA256 computed and recorded in GOVERNANCE_ALIGNMENT_INVENTORY.json

---

## Operationalization Evidence (per CS2 clarification in issue #1172)

### Schema Extension
- `.admin/pr.json.schema.json` extended with `execution_model`, `implementing_agent`,
  `orchestrating_agent`, `cs2_justification` fields per POLC_EXECUTION_MODEL_CANON.md §3

### Validator
- `.github/scripts/validate-simple-pr-admin.sh` created with Check 13 (execution_model
  enforcement). Implements all checks from SPAM-001 v1.2.0 §9 Validator specification.

### CI Gate Wiring
- `.github/workflows/polc-boundary-gate.yml` updated so Check 0 uses `execution_model`
  as the primary signal, satisfying the mandatory layer-down operationalization
  requirement in POLC_EXECUTION_MODEL_CANON.md §7.

### Tests — All 6 CS2 AC categories passing
```
AC1  — missing execution_model fails for implementation paths   ✅
AC2  — invalid execution_model value fails                      ✅
AC3  — builder-governed passes with implementing_agent          ✅
AC4  — foreman-orchestrated passes with all companion fields    ✅
AC5  — cs2-hotfix-override requires non-empty cs2_justification ✅
AC6  — docs-only/canon-only not forced into execution_model     ✅
AC7  — missing implementing_agent for builder-governed fails    ✅
AC8  — missing orchestrating_agent for foreman-orchestrated fails ✅
AC9  — missing cs2_justification for cs2-hotfix-override fails  ✅
AC10 — missing required fields fail                             ✅
AC11 — invalid type enum fails                                  ✅
AC12 — full-ceremony types require requires_iaa/requires_ecap   ✅
AC13 — governance-control files in diff require full ceremony   ✅

Total: 81 tests, 81 PASS, 0 FAIL
```

---

## Agent File Detection Gate

No `.github/agents/*.md` files in the changed artifact list.
→ Auto-close eligible per issue #1172 §Auto-Close Eligibility criteria.

---

## GOVERNANCE_ALIGNMENT_INVENTORY.json Update

| Artifact | Prior | After | Action |
|----------|-------|-------|--------|
| POLC_EXECUTION_MODEL_CANON.md | not present | v1.0.0 | CREATED |
| MMM_SIMPLE_PR_ADMIN_MODEL.md | not present (v1.0.0) | v1.2.0 | UPDATED |
| total_artifacts | 41 | 43 | +2 |
| last_layer_down_commit | d99e68e8... | 77a8297b... | UPDATED |

---

**Filed by**: governance-liaison-amc-agent | **Date**: 2026-05-12
