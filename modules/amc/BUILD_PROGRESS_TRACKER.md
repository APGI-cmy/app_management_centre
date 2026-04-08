# AMC Build Progress Tracker

**Module**: App Management Centre (AMC)  
**Lifecycle Model**: Canonical 12-Stage Pre-Build Sequence (PRE_BUILD_STAGE_MODEL_CANON.md v1.0.0)  
**Tracker Authority**: Repo-local — tracks AMC-specific stage completion within this repository  
**Last Updated**: 2026-04-08  
**Owner**: Maturion Foreman (Johan Ras / CS2)

> ⚠️ This tracker reflects the AMC repo-local pre-build state. It does not duplicate or replace the ISMS-level module tracker in `maturion-isms`. Both must remain consistent.

---

## Stage Summary

| Stage | Name | Status | Notes |
|-------|------|--------|-------|
| 1 | App Description | 🟡 In Progress | `docs/governance/FM_APP_DESCRIPTION.md` is the active canonical source. Migration to `modules/amc/00-app-description/app-description.md` is pending. See REPO_REALIGNMENT_NOTE.md. |
| 2 | UX Workflow & Wiring Spec | ⬜ Not Started | Awaiting Stage 1 authority clarification and migration completion. |
| 3 | FRS | ⬜ Not Started | |
| 4 | TRS | ⬜ Not Started | |
| 5 | Architecture | ⬜ Not Started | Pre-existing FM-era architecture material exists in `docs/architecture/` but is classified as historical/reference only — not active Stage 5 lifecycle input. See Stage Detail below. |
| 6 | QA-to-Red | ⬜ Not Started | |
| 7 | PBFAG | ⬜ Not Started | |
| 8 | Implementation Plan | ⬜ Not Started | |
| 9 | Builder Checklist | ⬜ Not Started | |
| 10 | IAA Pre-Brief | ⬜ Not Started | |
| 11 | Builder Appointment | ⬜ Not Started | |
| 12 | Build | ⬜ Not Started | |

**Legend**: ✅ Complete | 🟡 In Progress | ⬜ Not Started | 🔴 Blocked

---

## Stage Detail

### Stage 1 — App Description

**Status**: 🟡 In Progress  
**Active Canonical Source**: `docs/governance/FM_APP_DESCRIPTION.md` (v2.1, Authoritative Phase 4.1 Confirmed)  
**Target Canonical Location**: `modules/amc/00-app-description/app-description.md`  
**Migration Decision**: Pending — see `REPO_REALIGNMENT_NOTE.md` for options and constraints  
**Stage Completion Condition**: Migration completed and `modules/amc/00-app-description/app-description.md` declared canonical, OR explicit CS2 decision to retain `docs/governance/FM_APP_DESCRIPTION.md` as permanent canonical with pointer from this location.

### Stage 2 — UX Workflow & Wiring Spec

**Status**: ⬜ Not Started  
**Prerequisites**: Stage 1 complete (App Description authority resolved)  
**Artifacts to Create**: `modules/amc/01-ux-workflow-wiring-spec/`

### Stage 5 — Architecture

**Status**: ⬜ Not Started  
**Note — Pre-existing FM-era material**: The `docs/architecture/` directory contains architecture documents produced for the FM Office app during the FM-origin era. These artifacts are classified as historical/reference material for the purposes of the new `modules/amc/` 12-stage lifecycle. Their existence does **not** mean Stage 5 is complete or in progress. Stage 5 (Architecture) remains Not Started until CS2 explicitly adopts or commissions architecture artifacts through the canonical lifecycle sequence, which would require a classification decision, migration/adoption note, and tracker update.

### Stages 3–4 and 6–11

**Status**: ⬜ Not Started  
**Prerequisites**: Each stage requires the prior stage to be complete per canonical sequence dependency chain.

### Stage 12 — Build

**Status**: ⬜ Not Started  
**Note**: Build authorization requires all Stages 1–11 complete and PBFAG gate (Stage 7) passed.

---

## Next Action

1. Resolve Stage 1 authority: decide migration path for `FM_APP_DESCRIPTION.md`
2. Once Stage 1 is complete, begin Stage 2 (UX Workflow & Wiring Spec)
3. Progress sequentially through each stage per canonical order

---

## References

- [PRE_BUILD_STAGE_MODEL_CANON.md](../../governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md)
- [APP_DESCRIPTION_REQUIREMENT_POLICY.md](../../governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md)
- [FM_APP_DESCRIPTION.md](../../docs/governance/FM_APP_DESCRIPTION.md) — active Stage 1 source
- [REPO_REALIGNMENT_NOTE.md](./REPO_REALIGNMENT_NOTE.md)
