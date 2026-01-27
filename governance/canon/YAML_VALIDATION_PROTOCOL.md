# YAML VALIDATION PROTOCOL

## Status
**Type**: Tier-1 Canonical Governance — Mandatory Enforcement
**Authority**: Supreme - Constitutional
**Version**: 1.0.0
**Effective Date**: 2026-01-27
**Owner**: Maturion Engineering Leadership (Johan Ras)
**Layer-Down Status**: PUBLIC_API
**Applies To**: All Agents, All Repositories, All YAML Files, All Agent Contracts
**Immutability**: LOCKED - Cannot be overridden or bypassed

---

## 1. Purpose

This protocol establishes **immutable YAML validation methodology and enforcement** to prevent catastrophic failures from YAML syntax errors and validation drift.

**Problem Addressed**: Systemic failure where invalid YAML validation methodology (validating entire .md files instead of frontmatter only) allowed test debt and governance gaps to accumulate, resulting in complete repo halt in PR #679.

**Solution**: Lock YAML validation methodology immutably, provide copy-paste validation commands, enforce zero-warning handovers.

**Constitutional Basis**:
- **STOP_AND_FIX_DOCTRINE.md** - Zero tolerance for validation errors, immediate remediation
- **EXECUTION_BOOTSTRAP_PROTOCOL.md** - Mandatory local validation before handover
- **CI_CONFIRMATORY_NOT_DIAGNOSTIC.md** - CI confirms preflight success, does not discover failures
- **BUILD_PHILOSOPHY.md** - Zero test debt, 100% GREEN handovers

**Incident Reference**: PR #679 - Catastrophic YAML validation failure requiring >6,800 line fix across 7 agent files

---

## 2. YAML Validation Methodology (IMMUTABLE)

### 2.1 Frontmatter Extraction Standard

**MANDATORY**: Agent contract YAML validation MUST extract frontmatter only, not validate entire .md files.

**Frontmatter Definition**: Content between opening `---` and first closing `---` or `...` marker at start of file.

**Industry Standard Pattern** (Jekyll, Hugo, GitHub Pages):
```markdown
---
key: value
multiline: >
  This is a
  multiline value
---

# Markdown content starts here
```

**Extraction Algorithm** (IMMUTABLE):
```bash
# Extract YAML frontmatter from agent contract .md file
# Between first --- and second --- (or first ...)
awk '/^---$/{if(++count==2) exit; if(count==1) next} count==1; /^\.\.\.$/{ if(count==1) exit}' "$FILE"
```

**Rationale**: Agent contract files contain:
1. YAML frontmatter (governance bindings, metadata)
2. Markdown content (instructions, LOCKED sections)

Only the YAML frontmatter should be validated as YAML. Markdown sections must NOT be validated as YAML.

### 2.2 Validation Scope

**Pure YAML Files** (`.yml`, `.yaml`):
- ✅ Validate entire file as YAML
- ✅ GitHub Actions workflows: Lenient validation (GitHub parser more permissive than standard YAML)
- ✅ Configuration files: Strict validation

**Agent Contract Files** (`.github/agents/*.md`):
- ✅ Extract frontmatter only (see 2.1)
- ✅ Validate extracted frontmatter as YAML
- ❌ Do NOT validate entire .md file as YAML
- ⚠️ Skip files without frontmatter (documentation files like SCHEMA.md)

**Documentation Files** (other `.md` files):
- ❌ Do NOT validate as YAML (unless they have frontmatter and are explicitly included)

### 2.3 Validation Strictness

**Syntax Errors** → BLOCKING (exit code 1):
- Invalid YAML syntax
- Key duplicates
- Malformed structures

**Style Warnings** → NON-BLOCKING (informational only):
- Line length
- Trailing spaces
- Indentation style
- Comments formatting

**Configuration** (relaxed yamllint for gates):
```yaml
extends: default
rules:
  line-length: disable
  trailing-spaces: disable
  empty-lines: disable
  truthy: disable
  comments: disable
  indentation: disable
  document-start: disable
  colons: disable
  key-duplicates: enable  # ONLY syntax errors block
  new-line-at-end-of-file: disable
  new-lines: disable
  quoted-strings: disable
```

---

## 3. Local Validation Commands (COPY-PASTE READY)

### 3.1 Standalone Validation Script

**Location**: `.github/scripts/validate-yaml-frontmatter.sh`

**Usage**:
```bash
# Validate all YAML files and agent contract frontmatter
./.github/scripts/validate-yaml-frontmatter.sh

# Exit code 0 = success (required for handover)
# Exit code 1 = failures detected (STOP-AND-FIX immediately)
```

**What it validates**:
- All `.yml` and `.yaml` files in repository
- YAML frontmatter in all `.github/agents/*.md` files (excludes documentation)
- Reports syntax errors only (warnings are informational)

### 3.2 Manual Validation Commands

**For agents without access to script**:

```bash
# Step 1: Install yamllint
pip install yamllint

# Step 2: Create relaxed config
cat > /tmp/yamllint-relaxed.yml << 'EOF'
extends: default
rules:
  line-length: disable
  trailing-spaces: disable
  empty-lines: disable
  truthy: disable
  comments: disable
  indentation: disable
  document-start: disable
  colons: disable
  key-duplicates: enable
  new-line-at-end-of-file: disable
  new-lines: disable
  quoted-strings: disable
EOF

# Step 3: Validate pure YAML files
echo "=== Validating .yml/.yaml files ==="
git ls-files '*.yml' '*.yaml' | while read f; do
  echo "Checking: $f"
  yamllint -c /tmp/yamllint-relaxed.yml -f parsable "$f" || echo "FAILED: $f"
done

# Step 4: Validate agent contract frontmatter
echo "=== Validating agent contract frontmatter ==="
git ls-files '.github/agents/*.md' | grep -v 'SCHEMA\|README\|_archive' | while read f; do
  echo "Checking: $f"
  # Extract frontmatter (between --- markers)
  FRONTMATTER=$(awk '/^---$/{if(++count==2) exit; if(count==1) next} count==1; /^\.\.\.$/{ if(count==1) exit}' "$f")
  if [ -z "$FRONTMATTER" ]; then
    echo "  No frontmatter (skipping)"
    continue
  fi
  # Write to temp file and validate
  TMPFILE=$(mktemp)
  echo "$FRONTMATTER" > "$TMPFILE"
  yamllint -c /tmp/yamllint-relaxed.yml -f parsable "$TMPFILE" || echo "FAILED: $f"
  rm "$TMPFILE"
done

# Step 5: Check exit codes
echo ""
echo "=== Validation Complete ==="
echo "✅ If no 'FAILED' lines above, validation PASSED (exit 0)"
echo "❌ If any 'FAILED' lines, validation FAILED (exit 1) - STOP-AND-FIX immediately"
```

---

## 4. Agent Pre-Handover Requirements (MANDATORY)

### 4.1 Before Creating PR

**MANDATORY for ALL agents before creating ANY PR**:

1. ✅ Run YAML validation locally (script or manual commands)
2. ✅ Achieve exit code 0 (zero errors)
3. ✅ Fix any syntax errors immediately (STOP-AND-FIX)
4. ✅ Document validation in PREHANDOVER_PROOF

**Prohibited**:
- ❌ Creating PR without running YAML validation locally
- ❌ Documenting validation errors and proceeding ("will fix in CI")
- ❌ Tolerating ANY YAML syntax errors
- ❌ Deferring fixes to next PR

### 4.2 PREHANDOVER_PROOF Evidence

**Required in every PREHANDOVER_PROOF.md**:

```markdown
### YAML Validation ✅

**Method**: [Script | Manual commands]
**Timestamp**: 2026-01-27T[HH:MM:SS]Z
**Exit Code**: 0

**Files Validated**:
- Pure YAML files: X files
- Agent contract frontmatter: Y files

**Command Executed**:
```bash
./.github/scripts/validate-yaml-frontmatter.sh
# OR manual commands from YAML_VALIDATION_PROTOCOL.md Section 3.2
```

**Output**:
```
=== Validating .yml/.yaml files ===
✅ All .yml/.yaml files valid

=== Validating agent contract frontmatter ===
✅ All agent contracts valid

✅ YAML validation PASSED (exit 0)
```

**Syntax Errors**: NONE
**Style Warnings**: [count] (non-blocking, informational only)
```

### 4.3 Zero-Warning Handover

Per **EXECUTION_BOOTSTRAP_PROTOCOL.md** Section 5.1:

- ✅ ZERO YAML syntax errors permitted
- ✅ Exit code MUST be 0
- ❌ NO handover with ANY validation errors
- ❌ NO "will validate in CI" statements

**Authority**: `EXECUTION_BOOTSTRAP_PROTOCOL.md` v1.1.0 Section 5.1, `STOP_AND_FIX_DOCTRINE.md`

---

## 5. CI Workflow Integration

### 5.1 Gate Behavior

**CI Workflow**: `.github/workflows/yaml-validation.yml`

**Classification**: Hard Gate (blocking)

**Behavior**:
- ✅ CI executes SAME validation logic as local script
- ✅ CI is CONFIRMATORY (confirms preflight success)
- ❌ CI is NOT diagnostic (should not discover new failures)
- ✅ If CI fails, indicates agent violated protocol (skipped local validation)

**Two-Path Validation**:
1. **Evidence-Based** (BL-027/028): Accept if PREHANDOVER_PROOF documents validation
2. **Script-Based**: Execute validation if no evidence found

**Exit Codes**:
- Exit 0 → Gate PASSES, merge allowed
- Exit 1 → Gate BLOCKS, merge prevented

### 5.2 Workflow Maintenance

**Immutability**: The yaml-validation.yml workflow MUST:
- ✅ Extract frontmatter using IDENTICAL algorithm (Section 2.1)
- ✅ Use IDENTICAL yamllint configuration (Section 2.3)
- ✅ Report IDENTICAL error categories (syntax vs style)
- ❌ NOT introduce stricter validation than local script
- ❌ NOT validate entire .md files as YAML

**Drift Prevention**: Any workflow modification MUST update this canon and vice versa.

---

## 6. Agent Contract YAML Structure Standard

### 6.1 Correct Structure

**Pattern** (IMMUTABLE):
```markdown
---
id: agent-name
description: >-
  Multi-line description
  of the agent's purpose

agent:
  id: agent-name
  class: builder

governance:
  bindings:
    - id: binding-1
      path: path/to/canon.md
      role: binding-role

metadata:
  version: 1.0.0
  last_updated: 2026-01-27
---

# Agent Contract Content Starts Here

## 🔒 Section (LOCKED)
<!-- LOCKED sections are Markdown, not YAML -->
<!-- They MUST appear AFTER the closing --- -->
```

**Critical Rule**: The closing `---` MUST appear BEFORE any Markdown content (including LOCKED sections).

### 6.2 Common Errors (FORBIDDEN)

**Error 1: LOCKED sections inside YAML**:
```markdown
---
id: agent-name
description: Agent description

## 🔒 LOCKED Section  ← ❌ WRONG - Markdown inside YAML
<!-- This breaks YAML parsing -->
---
```

**Fix**:
```markdown
---
id: agent-name
description: Agent description
---

## 🔒 LOCKED Section  ← ✅ CORRECT - After closing ---
```

**Error 2: Missing closing ---**:
```markdown
---
id: agent-name
description: Agent description

# Content starts  ← ❌ WRONG - No closing ---
```

**Fix**:
```markdown
---
id: agent-name
description: Agent description
---

# Content starts  ← ✅ CORRECT - Closing --- added
```

**Error 3: Multiple opening --- without closing**:
```markdown
---
id: agent-name
---  ← First closing (correct)

---  ← ❌ WRONG - Second opening --- without purpose
Something
---
```

**Fix**: Remove extra `---` markers in Markdown content, or use different delimiter.

---

## 7. Catastrophic Failure Prevention

### 7.1 What This Protocol Prevents

**Prevents**:
- ✅ Silent accumulation of YAML syntax errors
- ✅ Validation methodology drift (entire .md file validation)
- ✅ Handovers with YAML errors ("will fix in CI")
- ✅ CI discovering validation failures (should be found locally)
- ✅ Agent contract structure drift
- ✅ Test debt from broken validation gates

**Detection Points**:
- ✅ Agent local validation (MANDATORY before PR)
- ✅ PREHANDOVER_PROOF review (CS2 verification)
- ✅ CI gate (confirmatory only)

### 7.2 STOP-AND-FIX Triggers

**STOP immediately and FIX if**:
- ❌ YAML validation script exits with code 1
- ❌ Any YAML syntax errors detected
- ❌ Agent contract frontmatter malformed
- ❌ CI yaml-validation gate fails

**Fix Process**:
1. STOP all forward progress
2. Review validation output (errors highlighted)
3. Fix ALL syntax errors (not just one)
4. Re-run validation locally
5. Achieve exit code 0
6. Document in PREHANDOVER_PROOF
7. Proceed with handover

**No Deferral**: YAML validation errors CANNOT be deferred to "next PR" or "future work".

### 7.3 Escalation Path

**If unable to fix YAML errors** (rare):
1. Document specific error and attempted fixes
2. Escalate to CS2 with full context
3. HALT handover until CS2 resolves
4. Do NOT proceed with broken YAML

**Escalation should be rare**: YAML syntax errors are typically straightforward to fix.

---

## 8. Enforcement and Compliance

### 8.1 Agent Responsibility

**Every agent MUST**:
- ✅ Run YAML validation before EVERY PR
- ✅ Include validation evidence in PREHANDOVER_PROOF
- ✅ Achieve exit code 0 before handover
- ✅ Follow STOP-AND-FIX if errors detected

**Violation Consequences**:
- PR blocked by CI gate
- RCA required for process violation
- Learning promotion to prevent recurrence

### 8.2 CS2 Audit Points

**CS2 MUST verify**:
- ✅ PREHANDOVER_PROOF includes YAML validation evidence
- ✅ Exit code is 0
- ✅ Timestamp is recent (within PR creation window)
- ✅ All required file types validated

**If evidence missing or inadequate**:
- ❌ Request agent re-run validation
- ❌ Block merge until evidence provided

### 8.3 Immutability Enforcement

**This protocol is IMMUTABLE**. Changes require:
1. CS2 approval
2. RCA if change requested due to failure
3. Update to this canon and all dependent artifacts
4. Ecosystem-wide ripple

**No agent, FM, or builder may**:
- ❌ Override YAML validation requirements
- ❌ Skip local validation
- ❌ Use different validation methodology
- ❌ Tolerate YAML syntax errors

---

## 9. Integration with Other Protocols

### 9.1 Related Governance

**This protocol integrates with**:
- **STOP_AND_FIX_DOCTRINE.md** - Immediate remediation of validation errors
- **EXECUTION_BOOTSTRAP_PROTOCOL.md** - Local validation mandatory before handover
- **CI_CONFIRMATORY_NOT_DIAGNOSTIC.md** - CI confirms, not discovers, validation success
- **AGENT_CONTRACT_PROTECTION_PROTOCOL.md** - Agent contract structure standards
- **BUILD_PHILOSOPHY.md** - Zero test debt, 100% GREEN handovers

### 9.2 Precedence

**This protocol is subordinate to**:
- GOVERNANCE_PURPOSE_AND_SCOPE.md (supreme governance authority)
- BUILD_PHILOSOPHY.md (constitutional principles)

**This protocol has precedence over**:
- Individual agent preferences
- "Convenience" arguments for skipping validation
- CI-only validation strategies

---

## 10. Version History

**v1.0.0** (2026-01-27): Initial creation in response to catastrophic YAML validation failure (PR #679, Issue #681). Established immutable validation methodology, copy-paste commands, agent requirements, and permanent prevention measures. Locked frontmatter extraction algorithm, validation strictness, and enforcement requirements. Authority: STOP_AND_FIX_DOCTRINE.md, EXECUTION_BOOTSTRAP_PROTOCOL.md v1.1.0, BUILD_PHILOSOPHY.md, Incident PR#679.

---

## 11. Cross-Repository Layer-Down

This canon MUST be layered down to:
- ✅ All consumer repositories
- ✅ All ISMS module repositories
- ✅ All repositories with agent contracts
- ✅ All repositories with CI gates

**Layer-Down Requirements**:
1. Copy this canon to `governance/canon/YAML_VALIDATION_PROTOCOL.md`
2. Create `.github/scripts/validate-yaml-frontmatter.sh` (see Section 12)
3. Update `GOVERNANCE_ARTIFACT_INVENTORY.md`
4. Add YAML validation commands to all agent contracts
5. Update yaml-validation.yml workflow to reference this protocol

---

## 12. Reference Implementation

**Validation Script**: `.github/scripts/validate-yaml-frontmatter.sh`

See canonical implementation at: `APGI-cmy/maturion-foreman-governance/.github/scripts/validate-yaml-frontmatter.sh`

**Script Requirements**:
- ✅ Extract frontmatter using algorithm from Section 2.1
- ✅ Use yamllint configuration from Section 2.3
- ✅ Exit 0 on success, exit 1 on syntax errors
- ✅ Report errors clearly with file names and line numbers
- ✅ Distinguish syntax errors (blocking) from style warnings (informational)

---

**END OF YAML VALIDATION PROTOCOL**
