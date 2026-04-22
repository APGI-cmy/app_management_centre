# AMC Repo Realignment Note

**Produced By**: Maturion Foreman  
**Date**: 2026-04-08  
**Authority**: CS2 (Johan Ras)  
**Issue Reference**: #1022 — Establish AMC 12-stage pre-build directory structure

---

## Purpose

This document records the governance-alignment decisions made when establishing the AMC 12-stage pre-build directory structure. It defines:

- What remains active
- What is legacy
- What is reference-only
- What becomes the new lifecycle root

---

## 1. What Remains Active

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| FM App Description | `docs/governance/FM_APP_DESCRIPTION.md` | **Active Canonical — Temporary** | v2.1. This is the current authoritative Stage 1 source. Remains active until migration to `modules/amc/00-app-description/app-description.md` is completed and CS2-approved. |
| AMC Governance Canon | `governance/canon/` | Active | Includes `PRE_BUILD_STAGE_MODEL_CANON.md` and supporting canons. |

---

## 2. What is Legacy (FM-Origin Era)

The following artifacts originate from the early "Foreman App" / "FM-origin" era of the AMC project. They contain historically useful context and provenance but are superseded by current governance structures.

**Holding Location**: `modules/amc/_legacy/foreman-app-origin/`

Legacy artifacts identified:

| Artifact | Original Location | Notes |
|----------|-------------------|-------|
| FM App Description (root copy) | `APP_DESCRIPTION.md` | Convenience reference only — points to `docs/governance/FM_APP_DESCRIPTION.md`. Preserved for navigational continuity. |
| FM Architecture documents | `docs/architecture/` | Architecture artifacts from the FM Office era. Classified as FM-era reference material — see §3 below. These artifacts do **not** constitute an active or in-progress Stage 5 in the new AMC 12-stage lifecycle. Preserved for traceability. |

> **Note**: No files have been moved to `_legacy/foreman-app-origin/` in this wave. This directory has been created as the designated holding location for future migrations. Silent deletion is prohibited. Provenance must be preserved when artifacts are moved here.

---

## 3. What is Reference-Only

| Artifact | Location | Notes |
|----------|----------|-------|
| `APP_DESCRIPTION.md` (root) | `APP_DESCRIPTION.md` | Reference pointer only — canonical is `docs/governance/FM_APP_DESCRIPTION.md` |
| FM Office Architecture | `docs/architecture/` | FM-era / pre-12-stage reference material. These architecture documents were produced for the FM Office app during the FM-origin era. They are preserved for historical context and traceability, but they are **not** active Stage 5 lifecycle input for the new `modules/amc/` lifecycle. Stage 5 (Architecture) remains **Not Started** until CS2 explicitly adopts, migrates, or commissions new architecture artifacts through the canonical 12-stage sequence. |
| ISMS-level module tracker | `maturion-isms` repo | AMC module status is tracked there; this repo's `BUILD_PROGRESS_TRACKER.md` is the repo-local authority |

---

## 4. What Becomes the New Lifecycle Root

**New AMC Lifecycle Root**: `modules/amc/`

The `modules/amc/` directory is the AMC module's new canonical lifecycle container, aligned to the 12-stage pre-build model.

```
modules/amc/
├── BUILD_PROGRESS_TRACKER.md       ← Repo-local stage status
├── AMC_PRE_BUILD_ARTIFACT_INDEX.md ← Pre-build artifact inventory
├── REPO_REALIGNMENT_NOTE.md        ← This file
├── 00-app-description/             ← Stage 1 (pending migration)
├── 01-ux-workflow-wiring-spec/     ← Stage 2
├── 02-frs/                         ← Stage 3
├── 03-trs/                         ← Stage 4
├── 04-architecture/                ← Stage 5
├── 05-qa-to-red/                   ← Stage 6
├── 06-pbfag/                       ← Stage 7 (gate)
├── 07-implementation-plan/         ← Stage 8
├── 08-builder-checklist/           ← Stage 9
├── 09-iaa-pre-brief/               ← Stage 10
├── 10-builder-appointment/         ← Stage 11
├── 11-build/                       ← Stage 12
└── _legacy/
    └── foreman-app-origin/         ← FM-era historical artifacts
```

---

## 5. Stage 1 Authority Decision (RESOLVED — 2026-04-22)

The Stage 1 App Description authority migration decision has been made by CS2 via Issue #1117 (2026-04-22).

| Location | Role |
|----------|------|
| `modules/amc/00-app-description/app-description.md` | **✅ APPROVED CANONICAL SOURCE** (v1.0, CS2-approved 2026-04-22) |
| `docs/governance/FM_APP_DESCRIPTION.md` | **📦 Superseded** — retained as historical/provenance reference only |

**Decision**: CS2 approved Option A — `modules/amc/00-app-description/app-description.md` v1.0 is the sole authoritative AMC Stage 1 source. All downstream derivation (FRS, TRS, Architecture, Build Planning) must reference this canonical location.

**Approval Reference**: app_management_centre#1117 — "Stage 2 kickoff — create AMC pre-build strategy and progress tracker, and finalize Stage 1 approval record alignment"

**Follow-on housekeeping** (does not block Stage 2):
- [ ] Add deprecation marker to `docs/governance/FM_APP_DESCRIPTION.md` — to be completed as follow-on housekeeping
- [ ] Update `APP_DESCRIPTION.md` root pointer to reference the new canonical location

**Formal approval record**: See `modules/amc/00-app-description/app-description-approval.md`

---

## 6. Constraints and Prohibitions

- ❌ No silent deletion of legacy artifacts
- ❌ No rewriting of FM-era artifact provenance
- ❌ No governance weakening
- ❌ No production code changes
- ✅ All migrations require explicit CS2 approval before execution
- ✅ Traceability must be preserved at all times
