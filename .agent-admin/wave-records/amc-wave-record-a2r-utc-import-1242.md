# AMC Wave Record — A2-R UTC Runtime Repair — PR #1242

Issue: #1233
PR: #1242
Wave: amc-a2r-utc-import-1233
Branch: apgi-cmy-issue-1233-a2r-utc-imports
Base: d8fb71a33540d7a5e25380949fa9b6e74ff0c5f4
Package head: 45edccf8ce2d440a69e399162ba522322814f182
Substantive implementation head: 45edccf8ce2d440a69e399162ba522322814f182
Foreman QP head: 45edccf8ce2d440a69e399162ba522322814f182

Verdict: PASS
PHASE: A2R_REPAIR
adoption_phase: PHASE_B_BLOCKING
PHASE_B_BLOCKING_TOKEN: IAA-session-1242-A2R-20260806-PASS
Reviewed SHA: 45edccf8ce2d440a69e399162ba522322814f182

delta_assurance_verdict: PASS
delta_classification: token-recording-only
base_head: 45edccf8ce2d440a69e399162ba522322814f182
final_head: 37dc65dc3f9f77dd41c5e7693958272eb290101f

## Disposition

- Phase 1 attestation: PASS
- Production diff: PASS — bounded datetime import-line repair only
- Allowlist compliance: PASS
- Anti-dodging: PASS — no test/workflow/dependency/infrastructure mutation
- Evidence completeness: PASS
- Foreman QP: PASS
- ECAP: PASS
- IAA final assurance: PASS — token IAA-session-1242-A2R-20260806-PASS

## Assurance bindings

Foreman QP: PASS — `.agent-admin/quality/amc-a2r-utc-import-1233-foreman-qp.md`
ECAP: PASS / ADMIN_VALIDATED — `.agent-admin/prehandover/ecap-reconciliation-1242.md`
IAA: PASS — token `IAA-session-1242-A2R-20260806-PASS` — `.agent-admin/assurance/iaa-wave-record-amc-a2r-utc-import-1233.md`
