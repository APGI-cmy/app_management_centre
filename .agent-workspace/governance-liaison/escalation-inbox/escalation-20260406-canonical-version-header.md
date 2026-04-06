# CS2 Escalation — Canonical Source Version Header Inconsistency
**Type**: GOVERNANCE_GAP  
**Date**: 2026-04-06  
**Agent**: governance-liaison-amc  
**Session**: 018  
**Severity**: LOW (non-blocking escalation — file layered down as-is with SHA256 verified)

---

## Issue
The canonical file `governance/canon/AGENT_HANDOVER_AUTOMATION.md` at commit  
`843cc6dc4dd88bee911ea21d809e72f28e7b93cf` has an internal version inconsistency:

- **Line 3 (status header)**: `**Version**: 1.1.3`  
- **Line 910 (Authority & Version section)**: `**Version**: 1.1.4`

The canonical CANON_INVENTORY correctly records this file as v1.1.4 with SHA256  
`39867b98a8d68ceebc3676b8066070e3b410e6f68a954bfd28089e0ef3d24514`.

## Impact
Agents reading only the header line may believe they have v1.1.3. The canonical inventory is authoritative and declares v1.1.4, but the document body is ambiguous.

## Action Required from CS2
Please update the canonical source file `governance/canon/AGENT_HANDOVER_AUTOMATION.md`  
in `APGI-cmy/maturion-foreman-governance` to set the status header to `**Version**: 1.1.4`  
(consistent with the Authority section and canonical inventory entry).

## Current Layer-Down Status
File has been layered down as-is (SHA256-verified against canonical inventory). The SHA256 matches the declared hash in the canonical CANON_INVENTORY (v1.1.4). The local copy will be updated when the canonical source is corrected.

---
*Escalation raised by governance-liaison-amc | 2026-04-06T09:00:00Z*
