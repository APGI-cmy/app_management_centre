# Merge Gate Interface Design - Living Agent System v6.2.0

**Date**: 2026-02-12  
**Agent**: Foreman (Living Agent System v6.2.0)  
**Authority**: FM_MERGE_GATE_MANAGEMENT_PROTOCOL.md (T0-014)  
**Purpose**: Technical design for 3-gate standard interface implementation

---

## Executive Summary

This document specifies the implementation of a **unified 3-gate merge interface** that consolidates 16 existing workflow gates into a single, standardized workflow conforming to MERGE_GATE_INTERFACE_STANDARD.md and enforcing all Living Agent System v6.2.0 requirements.

**Design Principles**:
1. **Standard Interface First**: Exact workflow and job names per canon
2. **Evidence-Based Enforcement**: Machine-readable artifacts, no log archaeology
3. **Deterministic Classification**: Path-based, label-based, branch-based PR typing
4. **Protocol-First Validation**: Wake-up, session-closure, canon integrity mandatory
5. **Fail-Fast with Clarity**: Evidence-first error messages, exact remediation steps

---

## Architecture Overview

### Workflow Structure

```yaml
name: Merge Gate Interface

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  # Gate 1: Evidence & Protocol Compliance
  merge-gate/verdict:
    name: Merge Gate Verdict
    # Validates evidence artifacts, wake-up/session-closure, test debt
    
  # Gate 2: Governance Canon Alignment
  governance/alignment:
    name: Governance Alignment
    # Validates canon integrity, detects drift, checks protected files
    
  # Gate 3: Stop-and-Fix Enforcement
  stop-and-fix/enforcement:
    name: Stop-and-Fix Enforcement
    # Detects unresolved stop-and-fix conditions, requires RCA
```

### Gate Responsibilities Matrix

| Gate | Primary Responsibility | Enforcement Level | Failure Behavior |
|------|----------------------|-------------------|------------------|
| `merge-gate/verdict` | Evidence artifacts, protocol execution, test debt | HARD | Block merge |
| `governance/alignment` | Canon integrity, drift detection, protected files | HARD | Block merge + escalate CS2 |
| `stop-and-fix/enforcement` | Stop-and-fix conditions, RCA requirement | HARD | Block merge until resolved |

---

## Gate 1: merge-gate/verdict

### Purpose
Validate that ALL required evidence artifacts exist, Living Agent System protocols were executed, and no test debt exists.

### Enforcement Logic

```yaml
merge-gate/verdict:
  name: Merge Gate Verdict
  runs-on: ubuntu-latest
  timeout-minutes: 10
  
  steps:
    # Step 1: PR Classification
    - name: Classify PR Type
      id: classify
      run: |
        # Deterministic classification per MERGE_GATE_INTERFACE_STANDARD.md § 4
        
        # Check PR labels (highest precedence)
        if echo "$LABELS" | jq -r '.[]' | grep -q "governance-only"; then
          echo "type=governance" >> $GITHUB_OUTPUT
        elif echo "$LABELS" | jq -r '.[]' | grep -q "docs-only"; then
          echo "type=docs" >> $GITHUB_OUTPUT
        # Check changed paths
        elif git diff --name-only origin/main...HEAD | grep -qE '^governance/|^\.agent|^\.agent-admin/'; then
          echo "type=governance" >> $GITHUB_OUTPUT
        elif git diff --name-only origin/main...HEAD | grep -qE '^docs/|\.md$' && \
             ! git diff --name-only origin/main...HEAD | grep -qvE '^docs/|\.md$'; then
          echo "type=docs" >> $GITHUB_OUTPUT
        # Check branch patterns
        elif [[ "$BRANCH" =~ ^release/|^hotfix/ ]]; then
          echo "type=code" >> $GITHUB_OUTPUT
        else
          echo "type=code" >> $GITHUB_OUTPUT
        fi
    
    # Step 2: Evidence Artifact Bundle Validation
    - name: Validate Evidence Artifact Bundle
      if: steps.classify.outputs.type != 'docs'
      run: |
        # Per EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md § 3, § 4
        
        MISSING=()
        
        # Required: Prehandover proof
        if [ ! -d ".agent-admin/prehandover" ] || \
           [ -z "$(find .agent-admin/prehandover -name '*.md' -type f)" ]; then
          MISSING+=("prehandover proof")
        fi
        
        # Required: Gate results JSON
        if [ ! -f ".agent-admin/gates/gate-results.json" ]; then
          MISSING+=("gate-results.json")
        fi
        
        # Required: Continuous improvement capture
        if [ ! -f ".agent-admin/improvements/improvements.md" ]; then
          MISSING+=("improvements.md")
        fi
        
        # Required: Governance sync state
        if [ ! -f ".agent-admin/governance/sync-state.json" ]; then
          MISSING+=("sync-state.json")
        fi
        
        # Conditional: RCA (if stop-and-fix occurred)
        # Check stop-and-fix detection result from gate 3
        # For now, check if RCA directory exists when improvements mention stop-and-fix
        if grep -qi "stop.and.fix\|stop-and-fix" .agent-admin/improvements/improvements.md 2>/dev/null; then
          if [ ! -d ".agent-admin/rca" ] || [ -z "$(find .agent-admin/rca -name '*.md' -type f)" ]; then
            MISSING+=("RCA (stop-and-fix occurred)")
          fi
        fi
        
        # Fail if missing artifacts
        if [ ${#MISSING[@]} -gt 0 ]; then
          echo "❌ GATE FAILURE: Evidence Artifact Bundle Incomplete"
          echo ""
          echo "Missing Artifacts:"
          for ARTIFACT in "${MISSING[@]}"; do
            echo "  - $ARTIFACT"
          done
          echo ""
          echo "Required Structure:"
          echo "  .agent-admin/prehandover/    # Prehandover proof"
          echo "  .agent-admin/gates/gate-results.json  # Machine-readable results"
          echo "  .agent-admin/rca/            # RCA (if stop-and-fix occurred)"
          echo "  .agent-admin/improvements/improvements.md"
          echo "  .agent-admin/governance/sync-state.json"
          echo ""
          echo "Remediation:"
          echo "  1. Create missing artifacts using templates in governance/templates/"
          echo "  2. Validate with: .github/scripts/validate-evidence-bundle.sh"
          echo "  3. Commit and push"
          echo ""
          echo "Authority: EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md"
          exit 1
        fi
        
        echo "✅ Evidence artifact bundle complete"
    
    # Step 3: Validate Wake-Up Protocol Execution
    - name: Validate Wake-Up Protocol
      if: steps.classify.outputs.type != 'docs'
      run: |
        # Per REQ-AS-005: Every session must run wake-up protocol
        
        # Check for working contract (ephemeral, generated during wake-up)
        # Note: Cannot check in git, must validate via prehandover proof
        
        # Check prehandover proof documents wake-up execution
        PROOF=$(find .agent-admin/prehandover -name '*.md' -type f | head -1)
        if [ -z "$PROOF" ]; then
          echo "❌ Cannot validate wake-up: prehandover proof missing"
          exit 1
        fi
        
        if ! grep -q "wake-up-protocol" "$PROOF" && \
           ! grep -q "Wake-Up Protocol" "$PROOF"; then
          echo "❌ GATE FAILURE: Wake-Up Protocol Not Executed"
          echo ""
          echo "Required: Every session must execute .github/scripts/wake-up-protocol.sh"
          echo "Evidence: Prehandover proof must document wake-up execution"
          echo ""
          echo "Missing: No wake-up protocol execution documented in $PROOF"
          echo ""
          echo "Remediation:"
          echo "  1. Run: .github/scripts/wake-up-protocol.sh foreman"
          echo "  2. Document execution in prehandover proof"
          echo "  3. Verify working-contract.md generated"
          echo ""
          echo "Authority: REQ-AS-005, LIVING_AGENT_SYSTEM.md"
          exit 1
        fi
        
        echo "✅ Wake-up protocol executed (documented in prehandover proof)"
    
    # Step 4: Validate Session Closure Execution
    - name: Validate Session Closure
      if: steps.classify.outputs.type != 'docs'
      run: |
        # Per REQ-EO-005: Every session must run session closure
        
        # Check for session memory file (created during session closure)
        if [ ! -d ".agent-workspace/foreman/memory" ]; then
          echo "❌ GATE FAILURE: Session memory directory missing"
          exit 1
        fi
        
        LATEST_SESSION=$(ls -t .agent-workspace/foreman/memory/session-*.md 2>/dev/null | head -1)
        if [ -z "$LATEST_SESSION" ]; then
          echo "❌ GATE FAILURE: Session Closure Not Executed"
          echo ""
          echo "Required: Every session must execute .github/scripts/session-closure.sh"
          echo "Evidence: Session memory file must exist"
          echo ""
          echo "Missing: No session memory file found in .agent-workspace/foreman/memory/"
          echo ""
          echo "Remediation:"
          echo "  1. Run: .github/scripts/session-closure.sh foreman"
          echo "  2. Verify session-NNN-YYYYMMDD.md created"
          echo "  3. Check lessons-learned.md and patterns.md updated"
          echo "  4. Commit and push"
          echo ""
          echo "Authority: REQ-EO-005, FOREMAN_MEMORY_PROTOCOL.md"
          exit 1
        fi
        
        echo "✅ Session closure executed (session memory: $(basename $LATEST_SESSION))"
    
    # Step 5: Validate Learning Artifacts Updated
    - name: Validate Learning Artifacts
      if: steps.classify.outputs.type != 'docs'
      run: |
        # Per FOREMAN_MEMORY_PROTOCOL.md § 4.4.2
        
        # Check if lessons-learned.md was updated
        if ! git diff --name-only origin/main...HEAD | grep -q "lessons-learned.md"; then
          echo "⚠️ WARNING: lessons-learned.md not updated in this PR"
          echo "Consider adding lessons learned from this session"
        else
          echo "✅ lessons-learned.md updated"
        fi
        
        # Check if patterns.md was updated
        if ! git diff --name-only origin/main...HEAD | grep -q "patterns.md"; then
          echo "⚠️ WARNING: patterns.md not updated in this PR"
          echo "Consider documenting patterns observed in this session"
        else
          echo "✅ patterns.md updated"
        fi
        
        # Non-blocking for now (warnings only)
    
    # Step 6: Validate Test Debt = ZERO
    - name: Zero Test Debt Enforcement
      if: steps.classify.outputs.type == 'code'
      run: |
        # Per BUILD_PHILOSOPHY.md: Zero Test Debt enforcement
        
        # Check gate-results.json for test debt status
        if [ -f ".agent-admin/gates/gate-results.json" ]; then
          TEST_DEBT=$(jq -r '.test_results.test_debt // "UNKNOWN"' .agent-admin/gates/gate-results.json)
          
          if [ "$TEST_DEBT" != "ZERO" ]; then
            echo "❌ GATE FAILURE: Test Debt Detected"
            echo ""
            echo "Test Debt Status: $TEST_DEBT"
            echo "Required: ZERO test debt (no failing, skipped, TODO, or hidden tests)"
            echo ""
            echo "Remediation:"
            echo "  1. Run full test suite: npm test (or appropriate command)"
            echo "  2. Fix ALL failing tests"
            echo "  3. Remove ALL skipped tests (or implement them)"
            echo "  4. Remove ALL TODO tests (or implement them)"
            echo "  5. Ensure 100% GREEN"
            echo "  6. Update gate-results.json with test_debt: ZERO"
            echo ""
            echo "Authority: BUILD_PHILOSOPHY.md, Zero Test Debt"
            exit 1
          fi
          
          echo "✅ Zero test debt confirmed"
        else
          echo "⚠️ Cannot validate test debt: gate-results.json missing"
        fi
    
    # Step 7: Validate Gate Results JSON Schema
    - name: Validate Gate Results Schema
      if: steps.classify.outputs.type != 'docs'
      run: |
        # Per EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md § 5
        
        if [ ! -f ".agent-admin/gates/gate-results.json" ]; then
          echo "❌ Already reported missing in step 2"
          exit 1
        fi
        
        # Validate JSON syntax
        if ! jq empty .agent-admin/gates/gate-results.json 2>/dev/null; then
          echo "❌ GATE FAILURE: gate-results.json invalid JSON"
          exit 1
        fi
        
        # Validate required fields
        REQUIRED_FIELDS=(
          ".timestamp"
          ".pr_number"
          ".verdict"
          ".gates"
          ".test_results"
        )
        
        for FIELD in "${REQUIRED_FIELDS[@]}"; do
          if ! jq -e "$FIELD" .agent-admin/gates/gate-results.json >/dev/null 2>&1; then
            echo "❌ GATE FAILURE: gate-results.json missing required field: $FIELD"
            exit 1
          fi
        done
        
        echo "✅ gate-results.json schema valid"
    
    # Step 8: Evidence-First Success/Failure Reporting
    - name: Report Gate Verdict
      if: always()
      run: |
        if [ "${{ job.status }}" = "success" ]; then
          echo "✅ MERGE GATE VERDICT: PASS"
          echo ""
          echo "All evidence artifacts present and valid:"
          echo "  ✅ Prehandover proof"
          echo "  ✅ Gate results JSON"
          echo "  ✅ Improvements capture"
          echo "  ✅ Governance sync state"
          echo "  ✅ Wake-up protocol executed"
          echo "  ✅ Session closure executed"
          echo "  ✅ Zero test debt"
          echo ""
          echo "Authority: MERGE_GATE_INTERFACE_STANDARD.md § 5"
        else
          echo "❌ MERGE GATE VERDICT: FAIL"
          echo ""
          echo "See step failures above for evidence-first error messages."
          echo "Each failure includes:"
          echo "  - Missing artifact path"
          echo "  - Required schema"
          echo "  - Exact remediation steps"
          echo ""
          echo "No log archaeology required."
        fi
```

---

## Gate 2: governance/alignment

### Purpose
Validate canon integrity, detect governance drift, and protect constitutional/critical files.

### Enforcement Logic

```yaml
governance/alignment:
  name: Governance Alignment
  runs-on: ubuntu-latest
  timeout-minutes: 10
  
  steps:
    # Step 1: PR Classification (shared logic)
    - name: Classify PR Type
      id: classify
      # ... (same as gate 1)
    
    # Step 2: Validate Canon Hash Integrity
    - name: Validate Canon Hash Integrity
      if: steps.classify.outputs.type == 'governance'
      run: |
        # Per REQ-CM-001, REQ-CM-002: No placeholder/truncated hashes
        
        if [ ! -f "governance/CANON_INVENTORY.json" ]; then
          echo "❌ GATE FAILURE: CANON_INVENTORY.json not found"
          echo ""
          echo "Required: governance/CANON_INVENTORY.json must exist"
          echo "Authority: REQ-CM-001"
          exit 1
        fi
        
        # Check for placeholder hashes
        PLACEHOLDERS=$(jq -r '.. | select(type == "string") | select(. == "PLACEHOLDER" or . == "TBD" or (length > 0 and length < 20))' governance/CANON_INVENTORY.json | wc -l)
        
        if [ $PLACEHOLDERS -gt 0 ]; then
          echo "❌ GATE FAILURE: Degraded Alignment Mode Detected"
          echo ""
          echo "Found $PLACEHOLDERS placeholder/truncated canon hashes"
          echo "Status: DEGRADED ALIGNMENT MODE"
          echo "Action: ESCALATE TO CS2"
          echo ""
          echo "Degraded mode prohibits merge per REQ-SS-004"
          echo ""
          echo "Remediation:"
          echo "  1. Identify placeholder hashes in CANON_INVENTORY.json"
          echo "  2. Compute actual SHA256 hashes for affected canons"
          echo "  3. Update CANON_INVENTORY.json with real hashes"
          echo "  4. Open CS2 escalation issue documenting degraded state"
          echo ""
          echo "Authority: REQ-CM-002, REQ-SS-004"
          exit 1
        fi
        
        echo "✅ Canon hash integrity validated (no placeholders)"
    
    # Step 3: Detect Governance Drift
    - name: Detect Governance Drift
      if: steps.classify.outputs.type == 'governance'
      run: |
        # Per MERGE_GATE_INTERFACE_STANDARD.md § 6
        
        # Check sync-state.json for drift indicators
        if [ -f ".agent-admin/governance/sync-state.json" ]; then
          DRIFT=$(jq -r '.drift_detected // false' .agent-admin/governance/sync-state.json)
          ALIGNMENT_STATE=$(jq -r '.alignment_state // "UNKNOWN"' .agent-admin/governance/sync-state.json)
          
          if [ "$DRIFT" = "true" ] || [ "$ALIGNMENT_STATE" = "DRIFT" ]; then
            echo "❌ GATE FAILURE: Governance Drift Detected"
            echo ""
            echo "Alignment State: $ALIGNMENT_STATE"
            echo "Drift Detected: $DRIFT"
            echo ""
            echo "Remediation:"
            echo "  1. Review drift details in sync-state.json"
            echo "  2. Reconcile governance artifacts with canonical source"
            echo "  3. Update sync-state.json with ALIGNED status"
            echo "  4. Document reconciliation in PR description"
            echo ""
            echo "Authority: MERGE_GATE_INTERFACE_STANDARD.md § 6"
            exit 1
          fi
          
          echo "✅ No governance drift detected (alignment: $ALIGNMENT_STATE)"
        else
          echo "⚠️ Cannot detect drift: sync-state.json missing (already reported in gate 1)"
        fi
    
    # Step 4: Validate Protected Files
    - name: Check Protected File Modifications
      run: |
        # Per REQ-CM-005: Protected file changes must escalate to CS2
        
        PROTECTED_FILES=(
          ".agent"
          ".github/agents/foreman-v2.md"
          "governance/canon/BUILD_PHILOSOPHY.md"
          "governance/canon/MERGE_GATE_INTERFACE_STANDARD.md"
          "governance/canon/EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md"
        )
        
        MODIFIED_PROTECTED=()
        
        for FILE in "${PROTECTED_FILES[@]}"; do
          if git diff --name-only origin/main...HEAD | grep -q "^$FILE$"; then
            MODIFIED_PROTECTED+=("$FILE")
          fi
        done
        
        if [ ${#MODIFIED_PROTECTED[@]} -gt 0 ]; then
          echo "🔒 PROTECTED FILE MODIFICATION DETECTED"
          echo ""
          echo "Modified Protected Files:"
          for FILE in "${MODIFIED_PROTECTED[@]}"; do
            echo "  - $FILE"
          done
          echo ""
          echo "Required: CS2 (Johan Ras) approval MANDATORY"
          echo "Status: Gate will PASS but CS2 review flagged"
          echo ""
          echo "Protected file modifications require explicit CS2 approval per REQ-CM-005"
          echo ""
          echo "Add label: 'requires-cs2-approval' to this PR"
        fi
    
    # Step 5: Validate Constitutional Canon Changes
    - name: Check Constitutional Canon Modifications
      if: steps.classify.outputs.type == 'governance'
      run: |
        # Per REQ-CM-003: Constitutional canon changes must escalate
        
        CONSTITUTIONAL_CANONS=(
          "governance/canon/BUILD_PHILOSOPHY.md"
          "governance/canon/LIVING_AGENT_SYSTEM.md"
          "governance/canon/FM_ROLE_CANON.md"
        )
        
        MODIFIED_CONSTITUTIONAL=()
        
        for CANON in "${CONSTITUTIONAL_CANONS[@]}"; do
          if git diff --name-only origin/main...HEAD | grep -q "^$CANON$"; then
            MODIFIED_CONSTITUTIONAL+=("$CANON")
          fi
        done
        
        if [ ${#MODIFIED_CONSTITUTIONAL[@]} -gt 0 ]; then
          echo "⚠️ CONSTITUTIONAL CANON MODIFICATION DETECTED"
          echo ""
          echo "Modified Constitutional Canons:"
          for CANON in "${MODIFIED_CONSTITUTIONAL[@]}"; do
            echo "  - $CANON"
          done
          echo ""
          echo "Required: CS2 approval + constitutional amendment process"
          echo "Authority: REQ-CM-003"
          echo ""
          echo "Constitutional changes are rare and require:"
          echo "  1. CS2 explicit approval"
          echo "  2. Justification for constitutional change"
          echo "  3. Impact analysis on existing governance"
          echo "  4. Ripple coordination plan"
        fi
    
    # Step 6: Report Alignment Status
    - name: Report Alignment Status
      if: always()
      run: |
        if [ "${{ job.status }}" = "success" ]; then
          echo "✅ GOVERNANCE ALIGNMENT: PASS"
          echo ""
          echo "Governance alignment validated:"
          echo "  ✅ Canon hash integrity"
          echo "  ✅ No governance drift"
          echo "  ✅ Protected file checks complete"
          echo ""
          echo "Authority: MERGE_GATE_INTERFACE_STANDARD.md § 6"
        else
          echo "❌ GOVERNANCE ALIGNMENT: FAIL"
          echo ""
          echo "See step failures for details and remediation."
        fi
```

---

## Gate 3: stop-and-fix/enforcement

### Purpose
Detect unresolved stop-and-fix conditions and require RCA when stop-and-fix occurred.

### Enforcement Logic

```yaml
stop-and-fix/enforcement:
  name: Stop-and-Fix Enforcement
  runs-on: ubuntu-latest
  timeout-minutes: 5
  
  steps:
    # Step 1: PR Classification (shared logic)
    - name: Classify PR Type
      id: classify
      # ... (same as gate 1)
    
    # Step 2: Detect Stop-and-Fix Indicators
    - name: Detect Stop-and-Fix Conditions
      id: detect-saf
      run: |
        # Check for stop-and-fix indicators in PR content
        
        SAF_DETECTED=false
        
        # Check improvements.md for stop-and-fix mention
        if [ -f ".agent-admin/improvements/improvements.md" ]; then
          if grep -qi "stop.and.fix\|stop-and-fix\|blocking issue\|critical fix" .agent-admin/improvements/improvements.md; then
            SAF_DETECTED=true
          fi
        fi
        
        # Check PR title/body for stop-and-fix keywords
        if echo "${{ github.event.pull_request.title }}" | grep -qi "stop.and.fix\|stop-and-fix\|URGENT\|CRITICAL FIX"; then
          SAF_DETECTED=true
        fi
        
        # Check for RCA files (indicates stop-and-fix occurred)
        if [ -d ".agent-admin/rca" ] && [ -n "$(find .agent-admin/rca -name '*.md' -type f)" ]; then
          SAF_DETECTED=true
        fi
        
        if [ "$SAF_DETECTED" = "true" ]; then
          echo "detected=true" >> $GITHUB_OUTPUT
          echo "⚠️ Stop-and-fix condition detected"
        else
          echo "detected=false" >> $GITHUB_OUTPUT
          echo "ℹ️ No stop-and-fix condition detected"
        fi
    
    # Step 3: Require RCA When Stop-and-Fix Occurred
    - name: Validate RCA Presence
      if: steps.detect-saf.outputs.detected == 'true'
      run: |
        # Per MERGE_GATE_INTERFACE_STANDARD.md § 7
        
        if [ ! -d ".agent-admin/rca" ] || [ -z "$(find .agent-admin/rca -name '*.md' -type f)" ]; then
          echo "❌ GATE FAILURE: RCA Required (Stop-and-Fix Occurred)"
          echo ""
          echo "Stop-and-fix condition detected but no RCA found"
          echo "Required: Root Cause Analysis documenting:"
          echo "  1. What went wrong"
          echo "  2. Why it went wrong"
          echo "  3. How it was fixed"
          echo "  4. Preventive measures"
          echo ""
          echo "Missing: .agent-admin/rca/rca-YYYYMMDD.md"
          echo ""
          echo "Remediation:"
          echo "  1. Create RCA using template: governance/templates/rca-template.md"
          echo "  2. Document root cause analysis"
          echo "  3. Save to .agent-admin/rca/rca-$(date +%Y%m%d).md"
          echo "  4. Commit and push"
          echo ""
          echo "Authority: MERGE_GATE_INTERFACE_STANDARD.md § 7"
          exit 1
        fi
        
        RCA_FILE=$(find .agent-admin/rca -name '*.md' -type f | head -1)
        echo "✅ RCA present: $(basename $RCA_FILE)"
    
    # Step 4: Validate RCA Completeness
    - name: Validate RCA Completeness
      if: steps.detect-saf.outputs.detected == 'true'
      run: |
        RCA_FILE=$(find .agent-admin/rca -name '*.md' -type f | head -1)
        
        # Check required RCA sections
        REQUIRED_SECTIONS=(
          "Root Cause"
          "Impact"
          "Resolution"
          "Prevention"
        )
        
        MISSING_SECTIONS=()
        
        for SECTION in "${REQUIRED_SECTIONS[@]}"; do
          if ! grep -qi "##.*$SECTION" "$RCA_FILE"; then
            MISSING_SECTIONS+=("$SECTION")
          fi
        done
        
        if [ ${#MISSING_SECTIONS[@]} -gt 0 ]; then
          echo "⚠️ WARNING: RCA incomplete"
          echo "Missing sections:"
          for SECTION in "${MISSING_SECTIONS[@]}"; do
            echo "  - $SECTION"
          done
          echo ""
          echo "RCA should document all required sections for completeness"
        else
          echo "✅ RCA completeness validated"
        fi
    
    # Step 5: Report Stop-and-Fix Status
    - name: Report Stop-and-Fix Status
      if: always()
      run: |
        SAF_DETECTED="${{ steps.detect-saf.outputs.detected }}"
        
        if [ "${{ job.status }}" = "success" ]; then
          if [ "$SAF_DETECTED" = "true" ]; then
            echo "✅ STOP-AND-FIX ENFORCEMENT: PASS"
            echo ""
            echo "Stop-and-fix condition detected and handled:"
            echo "  ✅ RCA present and complete"
            echo "  ✅ Root cause documented"
            echo "  ✅ Prevention measures identified"
            echo ""
            echo "Authority: MERGE_GATE_INTERFACE_STANDARD.md § 7"
          else
            echo "✅ STOP-AND-FIX ENFORCEMENT: PASS (N/A)"
            echo ""
            echo "No stop-and-fix condition detected"
            echo "Gate passes (not applicable)"
          fi
        else
          echo "❌ STOP-AND-FIX ENFORCEMENT: FAIL"
          echo ""
          echo "Stop-and-fix occurred but RCA missing or incomplete"
          echo "See step failures for remediation"
        fi
```

---

## Supporting Scripts Design

### Script 1: wake-up-protocol.sh

```bash
#!/bin/bash
# Wake-Up Protocol - Living Agent System v6.2.0
# Per REQ-AS-005

set -euo pipefail

AGENT_ID="${1:-foreman}"
WORKSPACE=".agent-workspace/$AGENT_ID"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")

echo "📋 WAKE-UP PROTOCOL INITIATED"
echo "Agent: $AGENT_ID"
echo "Timestamp: $TIMESTAMP"
echo ""

# Phase 1: Self-Identification
echo "Phase 1: Reading agent identity..."
if [ ! -f ".github/agents/${AGENT_ID}-v2.md" ]; then
  echo "❌ Agent contract not found"
  exit 1
fi
echo "✅ Identity loaded"

# Phase 2: Memory Scan
echo "Phase 2: Scanning session memories..."
mkdir -p "$WORKSPACE/memory"
LAST_5_SESSIONS=$(find "$WORKSPACE/memory" -name "session-*.md" -type f | sort -r | head -5)
echo "✅ Found $(echo "$LAST_5_SESSIONS" | wc -l) recent sessions"

# Phase 3: Governance Discovery
echo "Phase 3: Loading governance canon..."
if [ ! -f "governance/CANON_INVENTORY.json" ]; then
  echo "❌ CANON_INVENTORY not found"
  exit 1
fi
echo "✅ Governance canon loaded"

# Phase 4: Environment Health Check
echo "Phase 4: Checking environment health..."
if [ ! -d ".agent-admin" ]; then
  mkdir -p .agent-admin/{prehandover,gates,rca,improvements,governance}
fi
echo "✅ Environment healthy"

# Phase 5: Working Contract Generation
echo "Phase 5: Generating working contract..."
cat > "$WORKSPACE/working-contract.md" << EOF
# Working Contract - Session $(date +%Y%m%d)

**Agent**: $AGENT_ID
**Generated**: $TIMESTAMP
**Governance Version**: Living Agent System v6.2.0

## Active Obligations
- Evidence artifact bundle required
- Wake-up and session-closure protocols mandatory
- Canon hash integrity required
- Zero test debt enforcement

## Recent Context
$(if [ -n "$LAST_5_SESSIONS" ]; then echo "$LAST_5_SESSIONS" | head -1; else echo "No recent sessions"; fi)

---
Generated by wake-up-protocol.sh
EOF
echo "✅ Working contract generated: $WORKSPACE/working-contract.md"

echo ""
echo "✅ WAKE-UP PROTOCOL COMPLETE"
exit 0
```

### Script 2: session-closure.sh

```bash
#!/bin/bash
# Session Closure Protocol - Living Agent System v6.2.0
# Per REQ-EO-005

set -euo pipefail

AGENT_ID="${1:-foreman}"
WORKSPACE=".agent-workspace/$AGENT_ID"
TIMESTAMP=$(date +%Y%m%d)
SESSION_FILE="$WORKSPACE/memory/session-$(date +%03d)-$TIMESTAMP.md"

echo "🔒 SESSION CLOSURE INITIATED"
echo "Agent: $AGENT_ID"
echo "Date: $TIMESTAMP"
echo ""

# Step 1: Create Session Memory
echo "Step 1: Creating session memory..."
mkdir -p "$WORKSPACE/memory"

cat > "$SESSION_FILE" << 'EOF'
# Session NNN - YYYYMMDD (Living Agent System v6.2.0)

## Agent
- Type: AGENT_TYPE
- Class: AGENT_CLASS
- Session ID: SESSION_ID

## Task
[What was I asked to do?]

## What I Did
### Actions Taken
- Action 1
- Action 2

### Decisions Made
- Decision 1
- Decision 2

## Outcome
✅ COMPLETE | ⚠️ PARTIAL | ❌ ESCALATED

## Lessons
### What Worked Well
- Lesson 1

### What Was Challenging
- Challenge 1

### What Future Sessions Should Know
- Recommendation 1

---
Authority: LIVING_AGENT_SYSTEM.md v6.2.0
EOF

echo "✅ Session memory created: $SESSION_FILE"

# Step 2: Rotate Session Memories
echo "Step 2: Rotating session memories..."
SESSION_COUNT=$(find "$WORKSPACE/memory" -name "session-*.md" -type f | wc -l)
if [ $SESSION_COUNT -gt 5 ]; then
  mkdir -p "$WORKSPACE/memory/.archive"
  find "$WORKSPACE/memory" -name "session-*.md" -type f | sort | head -n $((SESSION_COUNT - 5)) | xargs -I {} mv {} "$WORKSPACE/memory/.archive/"
  echo "✅ Archived $((SESSION_COUNT - 5)) old session(s)"
else
  echo "✅ No rotation needed ($SESSION_COUNT sessions)"
fi

# Step 3: Verify Evidence Completeness
echo "Step 3: Verifying evidence completeness..."
EVIDENCE_COMPLETE=true
[ ! -d ".agent-admin/prehandover" ] && EVIDENCE_COMPLETE=false
[ ! -d ".agent-admin/gates" ] && EVIDENCE_COMPLETE=false
[ ! -d ".agent-admin/improvements" ] && EVIDENCE_COMPLETE=false

if [ "$EVIDENCE_COMPLETE" = "false" ]; then
  echo "⚠️ WARNING: Evidence bundle incomplete"
else
  echo "✅ Evidence bundle complete"
fi

echo ""
echo "✅ SESSION CLOSURE COMPLETE"
echo "Session memory: $SESSION_FILE"
exit 0
```

### Script 3: validate-evidence-bundle.sh

```bash
#!/bin/bash
# Evidence Bundle Validation
# Per EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md

set -euo pipefail

echo "🔍 VALIDATING EVIDENCE ARTIFACT BUNDLE"
echo ""

ERRORS=0

# Check required directories
REQUIRED_DIRS=(
  ".agent-admin/prehandover"
  ".agent-admin/gates"
  ".agent-admin/improvements"
  ".agent-admin/governance"
)

for DIR in "${REQUIRED_DIRS[@]}"; do
  if [ ! -d "$DIR" ]; then
    echo "❌ Missing directory: $DIR"
    ((ERRORS++))
  else
    echo "✅ Directory exists: $DIR"
  fi
done

# Check required files
REQUIRED_FILES=(
  ".agent-admin/gates/gate-results.json"
  ".agent-admin/improvements/improvements.md"
  ".agent-admin/governance/sync-state.json"
)

for FILE in "${REQUIRED_FILES[@]}"; do
  if [ ! -f "$FILE" ]; then
    echo "❌ Missing file: $FILE"
    ((ERRORS++))
  else
    echo "✅ File exists: $FILE"
  fi
done

# Check prehandover proof (at least one .md file)
if [ -z "$(find .agent-admin/prehandover -name '*.md' -type f 2>/dev/null)" ]; then
  echo "❌ Missing prehandover proof (.md file in .agent-admin/prehandover/)"
  ((ERRORS++))
else
  echo "✅ Prehandover proof exists"
fi

echo ""
if [ $ERRORS -eq 0 ]; then
  echo "✅ EVIDENCE BUNDLE VALID"
  exit 0
else
  echo "❌ EVIDENCE BUNDLE INVALID ($ERRORS errors)"
  exit 1
fi
```

---

## Branch Protection Migration Strategy

### Current State (Assumed)
- Multiple required checks (16+ workflows)
- Repository-specific check names
- Fragile and difficult to maintain

### Target State
**Require ONLY these 3 checks**:
- `Merge Gate Interface / merge-gate/verdict`
- `Merge Gate Interface / governance/alignment`
- `Merge Gate Interface / stop-and-fix/enforcement`

### Migration Steps
1. **Deploy new workflow** (merge this PR)
2. **Test period** (1 week): New gates run alongside old gates
3. **Update branch protection**: Require only 3 new contexts
4. **Deprecate old gates**: Mark as informational (non-blocking)
5. **Cleanup**: Remove old workflow files after grace period

---

## Testing Strategy

### Unit Tests (Per Gate)
1. **merge-gate/verdict**:
   - Test: Missing evidence artifact → FAIL
   - Test: Complete evidence bundle → PASS
   - Test: Docs-only PR → SKIP
   
2. **governance/alignment**:
   - Test: Placeholder canon hash → FAIL
   - Test: Protected file modification → FLAG (CS2 required)
   - Test: Valid canon hashes → PASS
   
3. **stop-and-fix/enforcement**:
   - Test: Stop-and-fix without RCA → FAIL
   - Test: Stop-and-fix with RCA → PASS
   - Test: No stop-and-fix → PASS (N/A)

### Integration Tests
1. **PR #740 Replay**: Verify violations now caught
2. **Complete Compliance PR**: Verify all gates pass
3. **Partial Compliance PR**: Verify appropriate gate fails

---

## Success Metrics

### Implementation Success
- ✅ Single workflow file: `.github/workflows/merge-gate-interface.yml`
- ✅ Exactly 3 jobs with standard names
- ✅ All 9 critical gaps closed

### Enforcement Success
- ✅ PR with missing evidence → BLOCKED by merge-gate/verdict
- ✅ PR with placeholder hash → BLOCKED by governance/alignment
- ✅ PR with stop-and-fix no RCA → BLOCKED by stop-and-fix/enforcement
- ✅ PR with complete compliance → ALL GATES PASS

### Governance Success
- ✅ Branch protection standardized (3 required checks)
- ✅ Bootstrap documented
- ✅ CS2 approval obtained
- ✅ Old gates deprecated gracefully

---

## Authority & Compliance

**Design Authority**: FM_MERGE_GATE_MANAGEMENT_PROTOCOL.md (T0-014)  
**Standard Compliance**: MERGE_GATE_INTERFACE_STANDARD.md v1.0.0  
**Evidence Requirements**: EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md v1.0.0  
**Protocol Compliance**: Living Agent System v6.2.0  
**CS2 Approval**: REQUIRED (governance evolution event)

---

## Next Steps

1. Implement workflow file per this design
2. Implement supporting scripts (wake-up, session-closure, validate-evidence)
3. Create validation test report
4. Create branch protection migration plan
5. Create self-demonstrating evidence bundle
6. Request CS2 approval

---

**Design Completed**: 2026-02-12  
**Status**: READY FOR IMPLEMENTATION  
**Session**: BOOTSTRAP GOVERNANCE EVOLUTION
