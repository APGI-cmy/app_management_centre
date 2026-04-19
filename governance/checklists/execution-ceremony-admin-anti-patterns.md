# Execution Ceremony Admin — Anti-Patterns Reference

**Version**: 1.1.0  
**Authority**: AGENT_HANDOVER_AUTOMATION.md v1.4.1 §4.3e + EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md v1.1.0 (ECAP-001)  
**Effective**: 2026-04-19  
**Owner**: Maturion Engineering Lead  
**Consumer**: execution-ceremony-admin-agent, foreman-v2-agent (§14.6 QP checkpoint), independent-assurance-agent (ACR regime)

> **Amendment Authority**: Only CS2 may amend this reference. Modifications without CS2 sign-off are auto-FAIL at the merge gate.

---

## Purpose

This reference documents the **9 known admin anti-patterns (AAP-01 through AAP-09)** that are auto-fail conditions for the §4.3e Admin Ceremony Compliance Gate. Each pattern describes:
- the exact condition that triggers a FAIL
- the corresponding IAA rejection trigger (ACR-xx) if the condition reaches IAA
- detection method for the execution-ceremony-admin-agent
- required resolution before bundle return

---

## Anti-Pattern Table

### AAP-01 — Issued Token But Provisional Wording Remains

**Description**: The ceremony bundle contains a PASS/COMPLETE/ISSUED status somewhere but provisional wording (`PENDING`, `in progress`, `in-progress`, `TODO`, `TBD`) remains in the final-state PREHANDOVER proof or latest session memory.

**Exemption**: Pre-token PREHANDOVER proofs retained immutably under the append-only model (i.e., superseded by a post-token proof with a `Supersedes: <filename>` declaration) are exempt from this check.

**IAA Trigger**: ACR-02  
**Detection**: `grep -iE "\bTODO\b|\bTBD\b|\bin[ _-]?progress\b|\bPENDING\b" .agent-admin/prehandover/proof-<latest>.md .agent-workspace/foreman-v2/memory/session-<latest>.md`  
**Resolution**: Normalize all provisional wording before committing the final-state bundle. Replace `PENDING` with actual values, `TODO` with completed content.

---

### AAP-02 — Mixed Internal Version Labels

**Description**: Multiple different version strings for the same artifact appear within a single document (e.g., "v1.2.0" and "v1.3.0" both appear as the current version of the same file).

**IAA Trigger**: ACR-05  
**Detection**: Manual scan — check all `Version:` / `**Version**:` fields in each ceremony artifact. Automated check: `grep -n "Version:" <file> | sort -u`  
**Resolution**: Determine the correct current version and normalize all occurrences. The file header version is authoritative.

---

### AAP-03 — Stale Artifact Path References

**Description**: A path declared in the PREHANDOVER proof, session memory, wave record, or ECAP reconciliation summary does not exist as a committed file on the branch.

**IAA Trigger**: ACR-08  
**Detection**: For each declared path: `git ls-files --error-unmatch <path>` — any failure indicates a stale reference.  
**Resolution**: Either commit the missing artifact at the declared path, or remove the stale reference. Never declare a path that hasn't been committed.

---

### AAP-04 — Stale Scope Declaration After File Changes

**Description**: The `FILES_CHANGED` count in `governance/scope-declaration.md` does not match the actual number of files changed in the PR: `git diff --name-only origin/main...HEAD | wc -l`.

**IAA Trigger**: ACR-04  
**Detection**: `DECLARED=$(grep -E "^FILES_CHANGED:" governance/scope-declaration.md | awk '{print $2}'); ACTUAL=$(git diff --name-only origin/main...HEAD | wc -l | tr -d ' '); [ "$DECLARED" != "$ACTUAL" ] && echo "MISMATCH: declared=$DECLARED actual=$ACTUAL"`  
**Resolution**: Update `governance/scope-declaration.md` FILES_CHANGED to match the actual diff count. Always update this as the last step before bundle return, after all file edits are final.

---

### AAP-05 — Stale Hash After File Finalization

**Description**: A SHA256 hash declared in the PREHANDOVER proof or CANON_INVENTORY for a specific file does not match the actual hash of that file in the committed branch state.

**IAA Trigger**: ACR-05  
**Detection**: For each file with a declared hash: `echo "<declared_hash>  <path>" | sha256sum -c` — any FAILED output indicates a stale hash.  
**Resolution**: Re-compute the hash after all file edits are final: `sha256sum <file>`. Update the declared hash before bundle return. Never compute hashes on draft artifacts.

---

### AAP-06 — Requested vs Completed Assurance Session Mismatch

**Description**: The PREHANDOVER proof cites a specific IAA session ID (in `iaa_audit_token`) that does not match the IAA session that actually issued the token in the token file or wave record section 5.

**IAA Trigger**: ACR-07  
**Detection**: Compare `iaa_audit_token` field in PREHANDOVER proof against the actual `PHASE_B_BLOCKING_TOKEN` in wave record section 5 and/or the IAA token file content.  
**Resolution**: Before IAA invocation, the `iaa_audit_token` field must reference the EXPECTED session (session-NNN format per A-015). After IAA responds, verify the token file matches. If they diverge, the wave record section 5 is authoritative.

---

### AAP-07 — Declared File/Artifact Count Mismatch

**Description**: A declared count of files, artifacts, or changed items in any ceremony artifact does not match the actual count.

**IAA Trigger**: ACR-04 (scope parity) / ACR-07 (general)  
**Detection**: Check all numeric claims: 
- `FILES_CHANGED` in scope-declaration.md vs actual diff count
- Artifact count in PREHANDOVER proof vs actual artifact count
- File count in session memory coverage summary vs actual deliverables  
**Resolution**: Update all declared counts to match actual values after all file edits are final.

---

### AAP-08 — PUBLIC_API Ripple Obligations Omitted or Silently Skipped

**Description**: Any file changed in this PR has `layer_down_status: PUBLIC_API` in CANON_INVENTORY but the ECAP reconciliation summary C4 has no ripple assessment block, or the block is absent or incomplete.

**IAA Trigger**: ACR-06  
**Detection**: 
1. Get changed PUBLIC_API files: `git diff --name-only origin/main...HEAD | while read f; do jq -r ".artifacts[] | select(.path==\"$f\") | select(.layer_down_status==\"PUBLIC_API\") | .path" governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json; done`
2. Verify each found file appears in ECAP reconciliation summary C4.  
**Resolution**: For each PUBLIC_API file changed, add a row in C4 with the layer_down_status, ripple action taken or deferred reason, and linked downstream issue/PR if deferred.

---

### AAP-09 — Committed Truth Not Matching Proof/Session Memory Claims

**Description**: The branch's actual committed file state contradicts a declared artifact path, hash, or status in a ceremony document. This is the general case covering any discrepancy between what ceremony documents claim and what is actually on the branch.

**IAA Trigger**: ACR-08 (path), ACR-05 (hash/version), ACR-07 (general)  
**Detection**: Run `git ls-files .agent-admin/ .agent-workspace/ governance/scope-declaration.md` and cross-reference every path declared in ceremony artifacts. Run `sha256sum` on key artifacts and compare to declared hashes.  
**Resolution**: Bring ceremony documents into alignment with actual committed state. Committed truth is always authoritative. Do not adjust committed state to match ceremony documents without Foreman approval.

---

### AAP-10 — Missing ECAP Reconciliation Summary

**Description**: The ceremony bundle is missing the ECAP reconciliation summary at `.agent-admin/prehandover/ecap-reconciliation-<PR#>.md` when an ECAP ceremony admin was appointed for this job.

**IAA Trigger**: ACR-01 (missing required ceremony artifact)  
**Detection**: `ls .agent-admin/prehandover/ecap-reconciliation-*.md 2>/dev/null || echo "MISSING"`  
**Resolution**: Create ECAP reconciliation summary with C1–C5 populated before bundle return.

---

### AAP-11 — Incomplete ECAP Reconciliation Summary (Blank C-Fields)

**Description**: The ECAP reconciliation summary exists but one or more of C1–C5 is blank, has a placeholder, or contains stub content.

**IAA Trigger**: ACR-01 (missing required content), ACR-07 (general coherence)  
**Detection**: Read C1–C5 fields in `.agent-admin/prehandover/ecap-reconciliation-<PR#>.md`. Any blank or placeholder field → FAIL.  
**Resolution**: Complete all C1–C5 fields before bundle return. C5 specifically requires Foreman sign-off.

---

### AAP-12 — Foreman §14.6 QP Checkpoint Not Completed

**Description**: C5 in the ECAP reconciliation summary is present but does not contain the Foreman §14.6 QP Admin-Compliance Checkpoint completion evidence.

**IAA Trigger**: ACR-01 (missing required content)  
**Detection**: Check C5 for Foreman §14.6 checkpoint signature text. Placeholder or "PENDING" in C5 → FAIL.  
**Resolution**: Foreman must complete C5 via §14.6 before ceremony admin returns bundle.

---

### AAP-13 — Session Memory Wave Record Path Mismatch

**Description**: The `wave_record_path` field in session memory does not point to the actual wave record file committed on the branch.

**IAA Trigger**: ACR-07 (general coherence), ACR-08 (stale path reference)  
**Detection**: `git ls-files --error-unmatch "$(grep 'wave_record_path:' .agent-workspace/foreman-v2/memory/session-*.md | tail -1 | awk '{print $2}' | tr -d '\r')" 2>&1`  
**Resolution**: Update `wave_record_path` in session memory to match actual committed wave record path.

---

### AAP-14 — Wave Record Assurance Section Not Pre-Filled

**Description**: Wave record section 5 was left with empty/missing `PHASE_B_BLOCKING_TOKEN` field instead of pre-filled with `PENDING` before IAA invocation.

**IAA Trigger**: ACR-07 (general), ACR-08 (structural gap)  
**Detection**: `grep "PHASE_B_BLOCKING_TOKEN:" .agent-admin/wave-records/amc-wave-record-*.md | grep -E ":[[:space:]]*$"` (flags empty/blank value) — OR — verify the field exists at all with `grep -L "PHASE_B_BLOCKING_TOKEN:" .agent-admin/wave-records/amc-wave-record-*.md` (files missing the field). Note: any non-empty terminal value (PENDING, PASS, REJECTION-PACKAGE, etc.) is valid at detection time; only a missing or empty field is an AAP-14 violation.  
**Resolution**: Pre-fill section 5 `PHASE_B_BLOCKING_TOKEN: PENDING` before IAA invocation. IAA will update to actual token.

---

### AAP-15 — Gate Set Not Explicitly Identified

**Description**: The final-state wave record evaluation section references gate results generically (e.g., "all required gates pass", "merge gate: PASS") without listing each required gate from `merge_gate_interface.required_checks` by name with its individual final state.

**IAA Trigger**: ACR-09  
**Detection**: Read Section 3 (Evaluation Summary) of the wave record. If the gate inventory does not list each required check from the contract's `merge_gate_interface.required_checks` with per-gate PASS/FAIL/N/A status → FAIL.  
**Resolution**: Replace generic gate claims with an explicit gate inventory table listing every required check by name with its final state and CI evidence reference.

---

### AAP-16 — Stale Gate Wording in Final-State Proof

**Description**: The final-state wave record evaluation section or session memory contains PENDING, in-progress, in_progress, verify-gates, or equivalent provisional wording for any gate entry. This typically occurs when a pre-IAA draft is committed without replacing all provisional placeholders.

**IAA Trigger**: ACR-10  
**Detection**: `grep -iE "\bPENDING\b|\bin[ _-]?progress\b|\bverify.gates\b" .agent-admin/wave-records/amc-wave-record-*-<latest>.md | grep -v "PHASE_B_BLOCKING_TOKEN: PENDING"` (the token pre-fill exemption applies — only gate-state fields are in scope)  
**Resolution**: Replace all provisional gate-state entries with explicit final states (PASS, FAIL, or N/A with reason). Do not commit bundle while any gate entry remains provisional.

---

## IAA Rejection Trigger Cross-Reference

| AAP | Triggers ACR(s) |
|-----|----------------|
| AAP-01 | ACR-02 |
| AAP-02 | ACR-05 |
| AAP-03 | ACR-08 |
| AAP-04 | ACR-04 |
| AAP-05 | ACR-05 |
| AAP-06 | ACR-07 |
| AAP-07 | ACR-04, ACR-07 |
| AAP-08 | ACR-06 |
| AAP-09 | ACR-05, ACR-07, ACR-08 |
| AAP-10 | ACR-01 |
| AAP-11 | ACR-01, ACR-07 |
| AAP-12 | ACR-01 |
| AAP-13 | ACR-07, ACR-08 |
| AAP-14 | ACR-07, ACR-08 |
| AAP-15 | ACR-09 |
| AAP-16 | ACR-10 |

---

## Quick-Check Script

Run before returning bundle to Foreman:

```bash
#!/bin/bash
# AAP Quick-Check — execution-ceremony-admin-agent
# Run from repo root before bundle return to Foreman

echo "=== AAP Anti-Pattern Quick-Check ==="
FAILS=()

# AAP-01/AAP-07: Provisional wording in final-state ceremony artifacts
LATEST_PROOF=$(ls -t .agent-admin/prehandover/proof-*.md 2>/dev/null | head -1)
LATEST_SESSION=$(ls -t .agent-workspace/foreman-v2/memory/session-*.md 2>/dev/null | head -1)
for f in "$LATEST_PROOF" "$LATEST_SESSION"; do
  [ -f "$f" ] || continue
  if grep -qiE "\bTODO\b|\bTBD\b|\bin[ _-]?progress\b|\bPENDING\b" "$f"; then
    FAILS+=("AAP-01: Provisional wording found in $f")
  fi
done

# AAP-03: Stale artifact path references
if [ -f "$LATEST_PROOF" ]; then
  while IFS= read -r path; do
    git ls-files --error-unmatch "$path" >/dev/null 2>&1 || \
      FAILS+=("AAP-03: Path not committed: $path")
  done < <(grep -oE '`\.agent-admin/[^`]+`|`\.agent-workspace/[^`]+`|`governance/[^`]+`' "$LATEST_PROOF" 2>/dev/null | tr -d '`' || true)
fi

# AAP-04: Stale scope declaration
if [ -f "governance/scope-declaration.md" ]; then
  DECLARED=$(grep -E "^FILES_CHANGED:" governance/scope-declaration.md | awk '{print $2}' | head -1)
  ACTUAL=$(git diff --name-only origin/main...HEAD 2>/dev/null | wc -l | tr -d ' ')
  [ -n "$DECLARED" ] && [ "$DECLARED" != "$ACTUAL" ] && \
    FAILS+=("AAP-04: Scope FILES_CHANGED=$DECLARED but actual=$ACTUAL")
fi

# Gate result
if [ ${#FAILS[@]} -gt 0 ]; then
  echo "❌ AAP QUICK-CHECK FAILED"
  for f in "${FAILS[@]}"; do echo "  - $f"; done
  exit 1
fi
echo "✅ AAP Quick-Check PASSED — no anti-patterns detected"
```

### AAP-15 and AAP-16 Detection (append to script above):

```bash
# AAP-15: Gate set not explicitly identified
# Sourced from merge_gate_interface.required_checks in foreman-v2-agent.md (all 7 required checks).
LATEST_WAVE=$(ls -t .agent-admin/wave-records/amc-wave-record-*.md 2>/dev/null | head -1)
if [ -f "$LATEST_WAVE" ]; then
  # Check that wave record evaluation section has explicit per-gate entries for ALL required gates.
  MISSING_GATES=()
  for gate in \
    "merge-gate/verdict" \
    "governance/alignment" \
    "stop-and-fix/enforcement" \
    "foreman-implementation-check" \
    "builder-involvement-check" \
    "session-memory-check" \
    "prehandover-proof-check"; do
    if ! grep -q "$gate" "$LATEST_WAVE"; then
      MISSING_GATES+=("$gate")
    fi
  done
  if [ ${#MISSING_GATES[@]} -gt 0 ]; then
    FAILS+=("AAP-15: Gate set not explicitly identified — missing: ${MISSING_GATES[*]}")
  fi
fi

# AAP-16: Stale gate wording (excluding PHASE_B_BLOCKING_TOKEN: PENDING which is valid pre-fill)
if [ -f "$LATEST_WAVE" ]; then
  if grep -iE "\bPENDING\b|\bin[ _-]?progress\b|\bverify.gates\b" "$LATEST_WAVE" | grep -qv "PHASE_B_BLOCKING_TOKEN: PENDING"; then
    FAILS+=("AAP-16: Stale gate wording found in $LATEST_WAVE")
  fi
fi
```

---

*Reference Version: 1.1.0 | Authority: AGENT_HANDOVER_AUTOMATION.md v1.4.1, ECAP-001 v1.1.0 | Effective: 2026-04-19*
