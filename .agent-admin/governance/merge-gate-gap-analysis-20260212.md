# Merge Gate Gap Analysis - Living Agent System v6.2.0

**Date**: 2026-02-12  
**Agent**: Foreman (Living Agent System v6.2.0)  
**Authority**: FM_MERGE_GATE_MANAGEMENT_PROTOCOL.md (T0-014)  
**Purpose**: Identify gaps between current gates and Living Agent System v6.2.0 requirements

---

## Executive Summary

**Total Gaps Identified**: 23  
**Critical Gaps**: 9  
**High Priority Gaps**: 8  
**Medium Priority Gaps**: 6  

**Primary Gap Categories**:
1. Living Agent System protocol enforcement (7 critical gaps)
2. Standard interface compliance (3 critical gaps)
3. Evidence artifact enforcement (5 high priority gaps)
4. Canon governance alignment (4 high priority gaps)

**Risk**: Current merge gates allow non-compliant PRs to merge, undermining governance integrity.

---

## Gap Category 1: Living Agent System Protocol Enforcement

### GAP-001: Wake-Up Protocol Execution Not Validated
**Severity**: CRITICAL  
**Requirement**: REQ-AS-005  
**Expected**: Every session must execute `.github/scripts/wake-up-protocol.sh`  
**Current**: No gate validates wake-up protocol execution  
**Impact**: Sessions may start without loading identity, memory, governance state, or generating working contract  
**Evidence**: PR #740 merged without wake-up validation  

**Required Implementation**:
```yaml
- name: Validate Wake-Up Protocol Execution
  run: |
    # Check for wake-up execution evidence
    if [ ! -f ".agent-workspace/foreman/working-contract.md" ]; then
      echo "❌ FAIL: Working contract not found"
      echo "Wake-up protocol must generate working-contract.md"
      exit 1
    fi
    
    # Validate working contract is fresh (current session)
    CONTRACT_AGE=$(( $(date +%s) - $(stat -c %Y .agent-workspace/foreman/working-contract.md) ))
    if [ $CONTRACT_AGE -gt 3600 ]; then
      echo "❌ FAIL: Working contract stale (age: ${CONTRACT_AGE}s)"
      exit 1
    fi
    
    echo "✅ PASS: Wake-up protocol executed (working contract exists and fresh)"
```

### GAP-002: Session Closure Not Validated
**Severity**: CRITICAL  
**Requirement**: REQ-EO-005  
**Expected**: Every session must execute `.github/scripts/session-closure.sh`  
**Current**: No gate validates session closure execution  
**Impact**: Sessions may end without capturing evidence, rotating memories, or recording lessons  
**Evidence**: PR #740 merged without session closure validation  

**Required Implementation**:
```yaml
- name: Validate Session Closure Execution
  run: |
    # Check for session memory file
    LATEST_SESSION=$(ls -t .agent-workspace/foreman/memory/session-*.md 2>/dev/null | head -1)
    if [ -z "$LATEST_SESSION" ]; then
      echo "❌ FAIL: No session memory found"
      echo "Session closure must create session memory file"
      exit 1
    fi
    
    # Validate session memory is fresh
    SESSION_AGE=$(( $(date +%s) - $(stat -c %Y "$LATEST_SESSION") ))
    if [ $SESSION_AGE -gt 7200 ]; then
      echo "❌ FAIL: Session memory stale (age: ${SESSION_AGE}s)"
      exit 1
    fi
    
    echo "✅ PASS: Session closure executed (session memory exists and fresh)"
```

### GAP-003: Canon Hash Integrity Not Checked
**Severity**: CRITICAL  
**Requirement**: REQ-CM-001, REQ-CM-002  
**Expected**: Validate CANON_INVENTORY hashes are not placeholder/truncated  
**Current**: No gate validates canon hash integrity  
**Impact**: Degraded alignment mode may go undetected, allowing misaligned PRs to merge  
**Evidence**: PR #740 merged without canon hash validation  

**Required Implementation**:
```yaml
- name: Validate Canon Hash Integrity
  run: |
    # Check CANON_INVENTORY exists
    if [ ! -f "governance/CANON_INVENTORY.json" ]; then
      echo "❌ FAIL: CANON_INVENTORY.json not found"
      exit 1
    fi
    
    # Check for placeholder hashes (e.g., "PLACEHOLDER", "TBD", or suspiciously short)
    PLACEHOLDER_COUNT=$(jq -r '.. | select(type == "string" and (. == "PLACEHOLDER" or . == "TBD" or (length > 0 and length < 20)))' governance/CANON_INVENTORY.json | wc -l)
    
    if [ $PLACEHOLDER_COUNT -gt 0 ]; then
      echo "❌ FAIL: Found $PLACEHOLDER_COUNT placeholder/truncated hashes"
      echo "DEGRADED ALIGNMENT MODE - escalate per REQ-SS-004"
      exit 1
    fi
    
    echo "✅ PASS: Canon hash integrity validated (no placeholders)"
```

### GAP-004: Learning Artifacts Not Validated
**Severity**: HIGH  
**Requirement**: FOREMAN_MEMORY_PROTOCOL.md § 4.4  
**Expected**: Session closure must update lessons-learned.md and patterns.md  
**Current**: No gate validates learning artifact updates  
**Impact**: Learning not captured, repeated mistakes, governance insights lost  

**Required Implementation**:
```yaml
- name: Validate Learning Artifacts Updated
  run: |
    # Check lessons-learned.md modified in this PR
    if git diff --name-only origin/main...HEAD | grep -q "lessons-learned.md"; then
      echo "✅ lessons-learned.md updated"
    else
      echo "⚠️ WARNING: lessons-learned.md not updated"
    fi
    
    # Check patterns.md modified in this PR
    if git diff --name-only origin/main...HEAD | grep -q "patterns.md"; then
      echo "✅ patterns.md updated"
    else
      echo "⚠️ WARNING: patterns.md not updated"
    fi
```

### GAP-005: Working Contract Generation Not Validated
**Severity**: HIGH  
**Requirement**: REQ-EO-006  
**Expected**: Wake-up must generate ephemeral working contract  
**Current**: No gate validates working contract existence (excluded from git)  
**Impact**: Agent may operate without current governance context  

**Note**: Working contract is ephemeral (`.gitignore`), so validation must occur during PR build, not via commit.

### GAP-006: Memory Rotation Not Validated
**Severity**: MEDIUM  
**Requirement**: FOREMAN_MEMORY_PROTOCOL.md § 4.4.3  
**Expected**: Keep only 5 most recent session memories, archive older ones  
**Current**: No gate validates memory rotation  
**Impact**: Memory directory may grow unbounded  

### GAP-007: Escalation Creation Not Validated
**Severity**: MEDIUM  
**Requirement**: FOREMAN_MEMORY_PROTOCOL.md § 4.4.4  
**Expected**: Create escalation files when blockers/gaps encountered  
**Current**: No gate checks for required escalations  
**Impact**: Blockers may go unescalated  

---

## Gap Category 2: Standard Interface Compliance

### GAP-008: No Standard Workflow Name
**Severity**: CRITICAL  
**Requirement**: MERGE_GATE_INTERFACE_STANDARD.md § 2  
**Expected**: Workflow named exactly "Merge Gate Interface"  
**Current**: 16 workflows with various names  
**Impact**: Branch protection cannot be standardized across repos  

**Required Implementation**:
```yaml
name: Merge Gate Interface
```

### GAP-009: No Standard Job Names
**Severity**: CRITICAL  
**Requirement**: MERGE_GATE_INTERFACE_STANDARD.md § 2  
**Expected**: Jobs named `merge-gate/verdict`, `governance/alignment`, `stop-and-fix/enforcement`  
**Current**: Each workflow has different job names  
**Impact**: Branch protection rules are repo-specific and fragile  

**Required Implementation**:
```yaml
jobs:
  merge-gate/verdict:
    name: Merge Gate Verdict
    # ...
  
  governance/alignment:
    name: Governance Alignment
    # ...
  
  stop-and-fix/enforcement:
    name: Stop-and-Fix Enforcement
    # ...
```

### GAP-010: No Deterministic PR Classification
**Severity**: HIGH  
**Requirement**: MERGE_GATE_INTERFACE_STANDARD.md § 4  
**Expected**: Deterministic classification based on paths, labels, branches  
**Current**: Various ad-hoc detection logic scattered across workflows  
**Impact**: Inconsistent gate applicability decisions  

**Required Implementation**:
```yaml
- name: Classify PR
  id: classify
  run: |
    # Label override (highest precedence)
    if [[ "$LABELS" =~ governance-only ]]; then
      echo "type=governance" >> $GITHUB_OUTPUT
    elif [[ "$LABELS" =~ docs-only ]]; then
      echo "type=docs" >> $GITHUB_OUTPUT
    # Path-based detection
    elif git diff --name-only origin/main...HEAD | grep -qE '^governance/|^\.agent|^\.agent-admin/'; then
      echo "type=governance" >> $GITHUB_OUTPUT
    elif git diff --name-only origin/main...HEAD | grep -qE '^docs/|\.md$' && ! git diff --name-only origin/main...HEAD | grep -qvE '^docs/|\.md$'; then
      echo "type=docs" >> $GITHUB_OUTPUT
    else
      echo "type=code" >> $GITHUB_OUTPUT
    fi
```

---

## Gap Category 3: Evidence Artifact Bundle Enforcement

### GAP-011: Evidence Artifact Bundle Not Required
**Severity**: HIGH  
**Requirement**: EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md § 3, § 4  
**Expected**: All PRs must have complete evidence bundle under `.agent-admin/`  
**Current**: PREHANDOVER_PROOF validation is soft gate (informational only)  
**Impact**: PRs may merge without evidence  

**Required Structure**:
```
.agent-admin/
├── prehandover/           # REQUIRED
│   └── proof-YYYYMMDD.md
├── gates/                 # REQUIRED
│   └── gate-results.json
├── rca/                   # REQUIRED (if stop-and-fix occurred)
│   └── rca-YYYYMMDD.md
├── improvements/          # REQUIRED
│   └── improvements.md
└── governance/            # REQUIRED
    └── sync-state.json
```

### GAP-012: Gate Results JSON Not Required
**Severity**: HIGH  
**Requirement**: EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md § 5  
**Expected**: Machine-readable gate-results.json under `.agent-admin/gates/`  
**Current**: No gate enforces gate results JSON presence  
**Impact**: Gate outcomes not machine-readable, audit trail incomplete  

**Required Schema**:
```json
{
  "timestamp": "ISO8601",
  "pr_number": "PR_NUMBER",
  "verdict": "PASS|FAIL",
  "gates": {
    "merge-gate/verdict": { "status": "PASS|FAIL", "evidence_artifacts": {...}, "issues": [] },
    "governance/alignment": { "status": "PASS|FAIL", "drift_detected": false, "issues": [] },
    "stop-and-fix/enforcement": { "status": "PASS|FAIL", "rca_required": false, "issues": [] }
  },
  "test_results": { "total_tests": 0, "passed": 0, "failed": 0, "skipped": 0, "test_debt": "ZERO|DETECTED" }
}
```

### GAP-013: RCA Not Required When Stop-and-Fix Occurs
**Severity**: HIGH  
**Requirement**: EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md § 4  
**Expected**: RCA required when stop-and-fix occurred OR gate failed and was repaired  
**Current**: No gate enforces RCA presence  
**Impact**: Root causes not documented, learning lost  

### GAP-014: Continuous Improvement Capture Not Required
**Severity**: MEDIUM  
**Requirement**: EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md § 4  
**Expected**: Improvements capture mandatory (may be "PARKED")  
**Current**: No gate enforces improvements capture  
**Impact**: Improvement opportunities lost  

### GAP-015: Governance Sync State Not Required
**Severity**: MEDIUM  
**Requirement**: EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md § 3  
**Expected**: `.agent-admin/governance/sync-state.json` documents alignment  
**Current**: No gate enforces sync state presence  
**Impact**: Governance alignment state not tracked  

---

## Gap Category 4: Canon Governance Alignment

### GAP-016: No Drift Detection
**Severity**: HIGH  
**Requirement**: MERGE_GATE_INTERFACE_STANDARD.md § 6  
**Expected**: `governance/alignment` gate must detect drift via sha256 comparison  
**Current**: No gate performs drift detection  
**Impact**: Governance drift may go undetected  

### GAP-017: No Constitutional Canon Protection
**Severity**: HIGH  
**Requirement**: REQ-CM-003  
**Expected**: Changes to constitutional canon must escalate to CS2  
**Current**: No gate escalates constitutional changes  
**Impact**: Constitutional canon may be modified without CS2 approval  

### GAP-018: No Protected File Detection
**Severity**: HIGH  
**Requirement**: REQ-CM-005  
**Expected**: Changes to protected files must escalate to CS2  
**Current**: No gate escalates protected file changes  
**Impact**: Critical files may be modified without approval  

### GAP-019: No Agent Contract Modification Detection
**Severity**: MEDIUM  
**Requirement**: AGENT_CONTRACT_PROTECTION_PROTOCOL.md  
**Expected**: Agent contract modifications must escalate  
**Current**: `agent-contract-governance.yml` exists but doesn't integrate with standard interface  
**Impact**: Agent contract changes not consistently enforced  

---

## Gap Category 5: Stop-and-Fix Enforcement

### GAP-020: No Stop-and-Fix Detection
**Severity**: HIGH  
**Requirement**: MERGE_GATE_INTERFACE_STANDARD.md § 7  
**Expected**: `stop-and-fix/enforcement` gate must fail if condition unresolved  
**Current**: No gate detects stop-and-fix conditions  
**Impact**: Stop-and-fix conditions may be ignored  

### GAP-021: No RCA Requirement When Stop-and-Fix Occurred
**Severity**: HIGH  
**Requirement**: MERGE_GATE_INTERFACE_STANDARD.md § 7  
**Expected**: RCA required when stop-and-fix occurred  
**Current**: No gate enforces RCA after stop-and-fix  
**Impact**: Root causes not analyzed  

---

## Gap Category 6: Error Messaging & Evidence-First Standard

### GAP-022: No Evidence-First Error Messages
**Severity**: MEDIUM  
**Requirement**: EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md § 7  
**Expected**: All failures must report missing artifact path, required schema, remediation action  
**Current**: Error messages vary, some require log archaeology  
**Impact**: Agents spend time debugging instead of fixing  

**Required Format**:
```
❌ GATE FAILURE: [Classification]

Missing Artifact: `.agent-admin/prehandover/proof.md`
Required Schema: See EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md § 4
Action: Create prehandover proof using template at `governance/templates/prehandover-proof.md`

Evidence Location: [exact path]
Validation Command: [exact command to run locally]
```

### GAP-023: No Log Archaeology Prohibition Enforcement
**Severity**: MEDIUM  
**Requirement**: MERGE_GATE_INTERFACE_STANDARD.md § 5  
**Expected**: Gates must fail fast with clear, actionable errors  
**Current**: Some gates produce verbose logs requiring archaeology  
**Impact**: Developer friction, time waste  

---

## Priority Matrix

### Critical (Merge-Blocking Implementation Required)
1. GAP-001: Wake-up protocol execution validation
2. GAP-002: Session closure validation
3. GAP-003: Canon hash integrity check
4. GAP-008: Standard workflow name
5. GAP-009: Standard job names
6. GAP-011: Evidence artifact bundle enforcement
7. GAP-012: Gate results JSON requirement
8. GAP-016: Drift detection
9. GAP-020: Stop-and-fix detection

### High Priority (Should Implement)
1. GAP-004: Learning artifacts validation
2. GAP-005: Working contract generation
3. GAP-010: Deterministic PR classification
4. GAP-013: RCA requirement
5. GAP-017: Constitutional canon protection
6. GAP-018: Protected file detection
7. GAP-021: RCA after stop-and-fix

### Medium Priority (Nice to Have)
1. GAP-006: Memory rotation validation
2. GAP-007: Escalation creation validation
3. GAP-014: Continuous improvement capture
4. GAP-015: Governance sync state
5. GAP-019: Agent contract modification detection
6. GAP-022: Evidence-first error messages
7. GAP-023: Log archaeology prohibition

---

## Implementation Strategy

### Phase 1: Foundation (This PR)
**Target**: Close all 9 CRITICAL gaps

1. Create `.github/workflows/merge-gate-interface.yml` with standard interface
2. Implement `merge-gate/verdict` job:
   - Evidence artifact bundle validation (GAP-011, GAP-012)
   - Wake-up protocol check (GAP-001)
   - Session closure check (GAP-002)
3. Implement `governance/alignment` job:
   - Canon hash integrity (GAP-003)
   - Drift detection (GAP-016)
4. Implement `stop-and-fix/enforcement` job:
   - Stop-and-fix condition detection (GAP-020)

### Phase 2: High Priority (Next PR)
**Target**: Close all 7 HIGH priority gaps

1. Enhance `merge-gate/verdict`:
   - Learning artifacts check (GAP-004)
   - Working contract validation (GAP-005)
   - RCA requirement enforcement (GAP-013)
2. Enhance `governance/alignment`:
   - Constitutional canon protection (GAP-017)
   - Protected file detection (GAP-018)
   - RCA after stop-and-fix (GAP-021)
3. Implement deterministic PR classification (GAP-010)

### Phase 3: Polish (Future PR)
**Target**: Close remaining MEDIUM priority gaps

1. Memory rotation validation
2. Escalation creation checks
3. Evidence-first error messages
4. Comprehensive documentation

---

## Test Cases for New Gates

### Test Case 1: Complete Compliance
**Setup**: PR with all evidence artifacts, valid canon hashes, no stop-and-fix  
**Expected**:
- `merge-gate/verdict` → PASS
- `governance/alignment` → PASS
- `stop-and-fix/enforcement` → PASS

### Test Case 2: Missing Evidence Bundle
**Setup**: PR without `.agent-admin/gates/gate-results.json`  
**Expected**:
- `merge-gate/verdict` → FAIL (missing artifact)
- Error message shows exact path and remediation

### Test Case 3: Placeholder Canon Hash
**Setup**: PR with "PLACEHOLDER" in CANON_INVENTORY.json  
**Expected**:
- `governance/alignment` → FAIL (degraded mode)
- Escalation to CS2 triggered

### Test Case 4: No Wake-Up Protocol
**Setup**: PR without working-contract.md  
**Expected**:
- `merge-gate/verdict` → FAIL (protocol not executed)

### Test Case 5: Stop-and-Fix Without RCA
**Setup**: PR with stop-and-fix condition but no RCA  
**Expected**:
- `stop-and-fix/enforcement` → FAIL (RCA required)

### Test Case 6: PR #740 Replay
**Setup**: Simulate PR #740 conditions  
**Expected**: All gates that missed violations should now FAIL

---

## Migration Risk Assessment

### Risk 1: Bootstrap Evaluation
**Risk**: This PR will be evaluated by OLD gates  
**Mitigation**: Document bootstrap explicitly, demonstrate self-compliance, obtain CS2 approval

### Risk 2: Existing PR Disruption
**Risk**: Open PRs may fail new gates retroactively  
**Mitigation**: Grandfather open PRs (apply new gates only to PRs opened after merge)

### Risk 3: Agent Adjustment Period
**Risk**: Agents not yet trained on new requirements  
**Mitigation**: Provide clear error messages, training documentation, grace period (warnings before errors)

### Risk 4: Branch Protection Update Window
**Risk**: Time gap between workflow merge and protection update  
**Mitigation**: Deploy new workflow first, test with voluntary enforcement, then update protection

---

## Success Criteria

### Deployment Success
- ✅ New workflow deployed without breaking existing CI
- ✅ All 3 standard contexts appear in PR checks
- ✅ Branch protection updated to require only 3 contexts
- ✅ Old gates deprecated gracefully

### Enforcement Success
- ✅ Test PR with missing evidence → BLOCKED
- ✅ Test PR with placeholder canon hash → BLOCKED
- ✅ Test PR with complete compliance → PASSED
- ✅ PR #740 conditions → BLOCKED

### Governance Success
- ✅ CS2 approval obtained
- ✅ Bootstrap documented
- ✅ Evidence artifact bundle complete
- ✅ Learning artifacts updated

---

## Conclusion

Current merge gates have **23 significant gaps** relative to Living Agent System v6.2.0 requirements. The most critical gaps involve protocol enforcement (wake-up, session closure, canon validation) and standard interface compliance.

**Immediate Action Required**: Implement new 3-gate standard interface with critical gap closures.

**Authority**: FM owns merge gate readiness per FM_MERGE_GATE_MANAGEMENT_PROTOCOL.md  
**CS2 Role**: Explicit approval required for this governance evolution  
**Bootstrap Status**: Recognized - old law applies, new law demonstrated

---

**Analysis Completed**: 2026-02-12  
**Next Step**: Design new gate interface implementation  
**Session**: BOOTSTRAP GOVERNANCE EVOLUTION
