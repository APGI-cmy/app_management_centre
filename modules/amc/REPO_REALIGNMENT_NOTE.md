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
| FM Office Architecture | `docs/architecture/` | **Pending Classification** | Architecture documents produced for the FM Office app. These originated in the FM-origin era; their active vs. legacy status requires a CS2 decision before any content is moved or reclassified. |

---

## 2. What is Legacy (FM-Origin Era)

The following artifacts originate from the early "Foreman App" / "FM-origin" era of the AMC project. They contain historically useful context and provenance but are superseded by current governance structures.

**Holding Location**: `modules/amc/_legacy/foreman-app-origin/`

Legacy artifacts identified:

| Artifact | Original Location | Notes |
|----------|-------------------|-------|
| FM App Description (root copy) | `APP_DESCRIPTION.md` | Convenience reference only — points to `docs/governance/FM_APP_DESCRIPTION.md`. Preserved for navigational continuity. |
| FM Architecture documents | `docs/architecture/` | Architecture artifacts from the FM Office era. Pending classification decision — see §1 note above. Preserved for traceability until CS2 determination is made. |

> **Note**: No files have been moved to `_legacy/foreman-app-origin/` in this wave. This directory has been created as the designated holding location for future migrations. Silent deletion is prohibited. Provenance must be preserved when artifacts are moved here.

---

## 3. What is Reference-Only

| Artifact | Location | Notes |
|----------|----------|-------|
| `APP_DESCRIPTION.md` (root) | `APP_DESCRIPTION.md` | Reference pointer only — canonical is `docs/governance/FM_APP_DESCRIPTION.md` |
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

## 5. Stage 1 Authority Decision (Pending)

The Stage 1 App Description currently has two locations:

| Location | Role |
|----------|------|
| `docs/governance/FM_APP_DESCRIPTION.md` | **Active authoritative canonical** (v2.1, Phase 4.1 Confirmed) |
| `modules/amc/00-app-description/app-description.md` | **Intended future canonical** (placeholder, not yet populated) |

**Migration Options** (CS2 decision required):

**Option A — Full Migration**: Migrate content from `FM_APP_DESCRIPTION.md` to `modules/amc/00-app-description/app-description.md`, update all references, and mark `FM_APP_DESCRIPTION.md` as legacy.

**Option B — Pointer Retention**: Keep `FM_APP_DESCRIPTION.md` as the permanent canonical source; add pointer from `modules/amc/00-app-description/app-description.md`. Update `BUILD_PROGRESS_TRACKER.md` to reflect Stage 1 as complete.

**Current Decision**: Pending CS2 approval. `FM_APP_DESCRIPTION.md` remains active canonical until explicit migration decision is made and executed.

---

## 6. Constraints and Prohibitions

- ❌ No silent deletion of legacy artifacts
- ❌ No rewriting of FM-era artifact provenance
- ❌ No governance weakening
- ❌ No production code changes
- ✅ All migrations require explicit CS2 approval before execution
- ✅ Traceability must be preserved at all times
