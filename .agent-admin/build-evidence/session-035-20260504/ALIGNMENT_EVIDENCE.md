# Alignment Evidence — session-035-20260504

**Agent**: governance-liaison-amc  
**Session**: session-035-20260504  
**Wave**: layer-down-d99e68e8-20260504  
**Date**: 2026-05-04  
**Canonical Commit**: d99e68e8759af5f619851116e583d768c4f4c1e1

---

## File Alignment Evidence

### Canon Files (UPDATED)

| File | Canonical Version | Consumer Before | Consumer After | SHA256 (first 32 chars) | Alignment Status |
|------|------------------|-----------------|----------------|------------------------|-----------------|
| SCOPE_DECLARATION_SCHEMA.md | v2.0.0 | v1 | v2.0.0 | 4c41a837aed825f4a0aa24e193de717aa | UPDATED |
| scope-declaration.template.md | v2.0.0 | (empty) | v2.0.0 | f233e0bd21d745f5e2df0d0c9625913 | UPDATED |
| AGENT_HANDOVER_AUTOMATION.md | 1.7.0 (canonical) | 1.7.2 (consumer ahead) | 1.7.3 | 144b4edb74ba707276b9e43efc449d04 | UPDATED (CONSUMER_AHEAD — merged per-PR changes) |

## Drift Evidence

| File | Before SHA256 (first 16 chars) | After SHA256 (first 16 chars) |
|------|-------------------------------|------------------------------|
| governance/canon/SCOPE_DECLARATION_SCHEMA.md | 96c0374ac4ee8d0c | 4c41a837aed825f4 |
| governance/canon/scope-declaration.template.md | 06e4173ff8485b6a | f233e0bd21d745f5 |
| governance/canon/AGENT_HANDOVER_AUTOMATION.md | c916049ae2faff9c | 144b4edb74ba7072 |

## Change Summary

### SCOPE_DECLARATION_SCHEMA.md v1 → v2.0.0
Changes from v1 → v2.0.0 (canonical d99e68e8):
1. §2 Core Invariants: added invariant 6 (per-PR immutable model)
2. §3 Artifact Location: updated from `governance/scope-declaration.md` to `.agent-admin/scope-declarations/pr-<PR_NUMBER>.md`; deprecated path notice added
3. §4 Required Sections: added section 7 (Files Changed)
4. §5.1 Header fields: SCOPE_SCHEMA_VERSION v1→v2; PR_ID→PR_NUMBER; ISSUE and BRANCH added
5. §5.7 Files Changed: new subsection with `## FILES_CHANGED`, `FILES_CHANGED: N`, bullet entries
6. §6 Validity Rules: added numeric field consistency checks
7. Status header: Amended line added with v2.0.0 date and authority

### scope-declaration.template.md (empty → v2.0.0)
New per-PR immutable scope declaration template:
1. SCOPE_SCHEMA_VERSION: v2 (v1 abolished)
2. PR_NUMBER, ISSUE, BRANCH header fields
3. ## FILES_CHANGED section with FILES_CHANGED: N numeric field
4. Footer with per-PR immutability notice

### AGENT_HANDOVER_AUTOMATION.md v1.7.2 → v1.7.3
Consumer was AHEAD at v1.7.2 (Stage 1 approval-alignment QA). Canonical amendment from d99e68e8 merged:
1. §4.3d Section 4.3d: Updated Purpose/Problem/Rule/Required Checks to per-PR scope model
   - Required Checks table: split into diff-vs-bullet-count and numeric-field-integrity rows
   - Gate script: PR_NUMBER env var required; SCOPE_FILE = .agent-admin/scope-declarations/pr-${PR_NUMBER}.md
   - Check 4b: validate FILES_CHANGED: N numeric field vs bullet count
   - Deprecated: governance/scope-declaration.md global model
2. §4.3e Check B: updated to use per-PR scope file with PR_NUMBER fallback discovery
   - BULLET_COUNT validation added (B2 failure code)
3. AAP-04: updated to reference per-PR path and include numeric field check
4. Handover Validation Checklist: scope-declaration item updated to per-PR model
5. Sequencing note (§4.3 overview): updated trigger condition for §4.3d
6. Checklist item (§4.1): updated scope file reference
7. Troubleshooting guide: stale scope entry updated

## Sync State

| Field | Value |
|-------|-------|
| canonical_commit | d99e68e8759af5f619851116e583d768c4f4c1e1 |
| local_commit | d99e68e8759af5f619851116e583d768c4f4c1e1 |
| drift_detected | false |
| needs_alignment | false |

## GOVERNANCE_ALIGNMENT_INVENTORY Verification

- `governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json`: last_layer_down_commit updated to d99e68e8 ✅
- SCOPE_DECLARATION_SCHEMA.md: added entry (v2.0.0, new) ✅
- scope-declaration.template.md (canon): added entry (v2.0.0, new) ✅
- AGENT_HANDOVER_AUTOMATION.md: updated to v1.7.3 ✅
- SCOPE_DECLARATION.template.md (templates/execution-ceremony-admin): unchanged ✅

---

*Alignment evidence created per layer-down protocol — governance-liaison-amc session-035-20260504*
