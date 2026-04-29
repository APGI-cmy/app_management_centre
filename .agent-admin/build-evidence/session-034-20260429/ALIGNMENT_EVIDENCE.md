# Alignment Evidence — session-034-20260429

**Agent**: governance-liaison-amc  
**Session**: session-034-20260429  
**Wave**: layer-down-2ba1d6a3-20260429  
**Date**: 2026-04-29  
**Canonical Commit**: 2ba1d6a3cf9c97dd67fff483ca04a90549cba293

---

## File Alignment Evidence

### Canon Files (CONSUMER_AHEAD — no overwrite)

| File | Canonical Version | Consumer Version | SHA256 (first 32 chars) | Alignment Status |
|------|------------------|-----------------|------------------------|-----------------|
| AGENT_HANDOVER_AUTOMATION.md | 1.6.0 | 1.7.2 | c916049ae2faff9c6eed83242260d5b4 | CONSUMER_AHEAD |
| INDEPENDENT_ASSURANCE_AGENT_CANON.md | 1.8.0 | 1.12.0 | cf1e94e2a7db1137a9f726fba65f6307 | CONSUMER_AHEAD |

### Template Files

| File | Canonical Version | Consumer Version | SHA256 (first 32 chars) | Alignment Status |
|------|------------------|-----------------|------------------------|-----------------|
| PREHANDOVER.template.md | 1.2.0 | 1.2.0 | 910c785643fa6d643ba4e41154e8c9dc | ALIGNED (updated) |

## Drift Evidence

| File | Before SHA256 (first 16 chars) | After SHA256 (first 16 chars) |
|------|-------------------------------|------------------------------|
| governance/templates/execution-ceremony-admin/PREHANDOVER.template.md | 54f03b12129f5e71 | 910c785643fa6d64 |

## PREHANDOVER.template.md v1.2.0 — Change Summary

Changes from v1.1.0 → v1.2.0:
1. Authority line in yaml: `EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md v1.2.0` → `v1.1.0` (canonical correction)
2. IAA Assurance section: removed separate `iaa_token_file:` field; consolidated into `iaa_audit_token:` with path reference; added `active_bundle_iaa_coherence:` field (required for §4.3e Check L)
3. Added full "## Ripple / Cross-Agent Assessment" markdown section with Ripple Obligations table, Cross-Agent Impact table, and Assessment Verdict
4. Replaced "## Embedded ECAP Reconciliation Summary (if not separate file)" heading with canonical placement note
5. Updated footer: Template Version 1.1.0 → 1.2.0; Authority updated to include AGENT_HANDOVER_AUTOMATION.md v1.6.0 reference; Effective date updated to 2026-04-21

## Sync State

| Field | Value |
|-------|-------|
| canonical_commit | 2ba1d6a3cf9c97dd67fff483ca04a90549cba293 |
| local_commit | 2ba1d6a3cf9c97dd67fff483ca04a90549cba293 |
| drift_detected | false |
| needs_alignment | false |

## GOVERNANCE_ALIGNMENT_INVENTORY Verification

- `governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json`: last_layer_down_commit updated to 2ba1d6a3 ✅
- `.agent-admin/governance/GOVERNANCE_ALIGNMENT_INVENTORY.json`: all 3 artifact entries updated ✅
- PREHANDOVER.template.md hash updated to 910c785643... ✅
- AGENT_HANDOVER_AUTOMATION.md marked CONSUMER_AHEAD (canonical v1.6.0, consumer v1.7.2) ✅
- INDEPENDENT_ASSURANCE_AGENT_CANON.md marked CONSUMER_AHEAD (canonical v1.8.0, consumer v1.12.0) ✅

---

*Alignment evidence created per layer-down protocol — governance-liaison-amc session-034-20260429*
