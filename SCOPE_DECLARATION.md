# SCOPE_DECLARATION

**Issue**: #1129 — Hardening — Foreman/ceremony must enforce governing-issue parity and issue-role separation across the full artifact chain
**Date**: 2026-04-23
**Agent**: foreman-v2-agent (session-031-20260423)
**Wave**: wave-governing-issue-parity-hardening

## Files Modified / Added

### Governance Canon (New)
- `governance/canon/GOVERNING_ISSUE_PARITY_PROTOCOL.md` — New GIPC-001 canon: issue-role separation, governing-issue parity check, labeled authority fields, tracker parity gate, overshadow detection, ceremony enforcement. Authority: CS2 — Issue #1129.

### Governance Templates (Modified)
- `.agent-admin/templates/amc-wave-record-template.md` — Updated to v1.1.0: added Governing Authority table (§1a) and Governing-Issue Parity Evidence block (§3a) per GIPC-001 §3.3 and §2.4. Authority: CS2 — Issue #1129.

### Tier 2 Operational Knowledge (Modified)
- `.agent-workspace/foreman-v2/knowledge/FAIL-ONLY-ONCE.md` — Added A-036 (GOVERNING-ISSUE-PARITY-MANDATORY), A-037 (OVERSHADOW-DETECTION-MANDATORY), A-038 (CEREMONY-PARITY-EVIDENCE-REQUIRED). Authority: CS2 — Issue #1129.

### Wave Ceremony Artifacts (New)
- `.agent-admin/waves/wave-governing-issue-parity-hardening-20260423-current-tasks.md` — Wave checklist for this wave.
- `.agent-admin/wave-records/amc-wave-record-governing-issue-parity-hardening-20260423.md` — Wave record with IAA Pre-Brief in section 2.
- `.agent-workspace/foreman-v2/memory/session-031-20260423.md` — Session memory.
- `SCOPE_DECLARATION.md` — This file (cleared and rewritten per A-029).

### Wake-Up Protocol Generated (auto-created by .github/scripts/wake-up-protocol.sh)
- `.agent-workspace/foreman-v2-agent/personal/lessons-learned.md` — Auto-generated template.
- `.agent-workspace/foreman-v2-agent/personal/patterns.md` — Auto-generated template.

- `PREHANDOVER_PROOF_session-031-20260423.md` — PREHANDOVER proof for this wave (pre-populated with expected IAA token per A-028)

## Pre-existing Issues (not introduced by this session)
- `.github/workflows/polc-boundary-gate.yml` — YAML validation warning "Missing required workflow structure (on: or jobs:)" — pre-existing on main branch, not introduced by this session. Evidence: running `validate-yaml-frontmatter.sh` on the stash-cleared working tree produced the same error.

## IAA Status
PENDING — to be invoked per Phase 4 §4.4.
