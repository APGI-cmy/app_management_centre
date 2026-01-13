# Wave 3.2 Tools - Usage Guide

**Authority**: Wave 3.2 - Deprecation Gate + Bootstrap Enforcement  
**Date**: 2026-01-13  
**Status**: Active

---

## Overview

Wave 3.2 introduces automated tools for BL-026 deprecation enforcement and Execution Bootstrap Protocol validation. This guide explains how to use each tool.

---

## Tool 1: Git Hooks Installation

**Script**: `scripts/install-git-hooks.sh`  
**Purpose**: Install pre-commit and pre-push hooks for BL-026 enforcement  
**Authority**: BL-026 Automated Deprecation Detection Gate

### Usage

```bash
# From repository root
./scripts/install-git-hooks.sh
```

### What It Does

1. Configures Git to use `.githooks/` directory (preferred method)
2. Falls back to manual hook copying if needed
3. Validates environment (Python, ruff)
4. Offers to install ruff if missing

### Installed Hooks

- **pre-commit**: Test debt detection, file validation
- **pre-commit-deprecation**: BL-026 scan on staged files
- **pre-commit-tier0-consistency**: Constitutional file checks
- **pre-push**: Full BL-026 scan on all Python files

### Exit Codes

- `0` - Installation successful
- `1` - Installation failed

---

## Tool 2: Builder Environment Validation

**Script**: `scripts/validate-builder-environment.py`  
**Purpose**: Validate builder environment has all required tools  
**Authority**: BL-026, Wave 3.2

### Usage

```bash
python3 scripts/validate-builder-environment.py
```

### What It Checks

1. Python 3.9+ installed
2. Git available
3. ruff installed (BL-026 scanner)
4. Git hooks configured
5. Hook files present

### Exit Codes

- `0` - Environment valid
- `1` - Environment invalid (missing requirements)
- `2` - Script error

### Sample Output

```
╔════════════════════════════════════════════════════════════╗
║      Builder Environment Validation - BL-026 & Wave 3.2   ║
╚════════════════════════════════════════════════════════════╝

  ✅ Python 3.9+
     Version: 3.12.3
  ✅ Git
     Path: /usr/bin/git
  ✅ ruff (BL-026 scanner)
     ruff 0.14.11
  ✅ Git hooks configured
     Path: .githooks
  ✅ BL-026 hook files present

╔════════════════════════════════════════════════════════════╗
║                  Validation Summary                        ║
╚════════════════════════════════════════════════════════════╝

✅ Environment is ready for BL-026 enforcement
```

---

## Tool 3: PREHANDOVER_PROOF Template Generator

**Script**: `scripts/generate-prehandover-proof-template.py`  
**Purpose**: Generate skeleton PREHANDOVER_PROOF with all required sections  
**Authority**: Execution Bootstrap Protocol v2.0.0+

### Basic Usage

```bash
# Default template
python3 scripts/generate-prehandover-proof-template.py

# Customized template
python3 scripts/generate-prehandover-proof-template.py \
  --agent "API Builder" \
  --pr 123 \
  --wave "Wave 3.2" \
  --branch "feature/my-changes"

# Documentation-only changes (no Category 0)
python3 scripts/generate-prehandover-proof-template.py \
  --no-category-0 \
  --output PREHANDOVER_PROOF_DOC_ONLY.md
```

### Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--agent NAME` | Agent name | "Builder Name" |
| `--pr NUMBER` | PR number | "PR_NUMBER" |
| `--branch NAME` | Branch name | "feature/your-branch" |
| `--wave ID` | Wave identifier | "Wave X.Y" |
| `--no-category-0` | Mark Category 0 as N/A | False (Category 0 included) |
| `-o, --output FILE` | Output file path | "PREHANDOVER_PROOF_TEMPLATE.md" |

### Output

Generates a complete PREHANDOVER_PROOF template with:
- Metadata section
- Category 0: Execution Bootstrap Protocol (7 steps)
- Agent Attestation
- Appendices for test results, logs, artifacts

### Next Steps After Generation

1. Fill in all `[PLACEHOLDERS]`
2. Execute artifacts locally and capture evidence
3. Document exit codes (must all be 0)
4. Validate with `validate_prehandover_proof.py`

---

## Tool 4: PREHANDOVER_PROOF Validator

**Script**: `governance/scripts/validate_prehandover_proof.py`  
**Purpose**: Validate PREHANDOVER_PROOF completeness and correctness  
**Authority**: Execution Bootstrap Protocol v2.0.0+, Wave 3.2

### Basic Usage

```bash
# Standard validation
python3 governance/scripts/validate_prehandover_proof.py PREHANDOVER_PROOF.md

# Verbose output
python3 governance/scripts/validate_prehandover_proof.py PREHANDOVER_PROOF.md --verbose

# JSON output (for CI integration)
python3 governance/scripts/validate_prehandover_proof.py PREHANDOVER_PROOF.md --json
```

### What It Validates

1. **Metadata Completeness**
   - Agent, PR, Branch, Date, Latest Commit, Protocol Version

2. **Category 0 (if applicable)**
   - All 7 steps present
   - Exit codes documented (all must be 0)
   - Evidence collection complete (logs, timestamps, outputs)
   - Critical attestations present

3. **Agent Attestation**
   - Attestation section exists

### Exit Codes

- `0` - Validation passed
- `1` - Validation failed
- `2` - File not found or invalid

### Sample Output (Verbose)

```
Validating PREHANDOVER_PROOF: PREHANDOVER_PROOF_PR_123.md
------------------------------------------------------------
✅ VALIDATION PASSED

PREHANDOVER_PROOF is complete and valid.

All required sections present:
  ✓ Metadata (Agent, PR, Branch, Date, Commit, Protocol Version)
  ✓ Category 0: Execution Bootstrap Protocol (7 steps)
  ✓ Agent Attestation
  ✓ Exit codes validated (all 0)
  ✓ Evidence collection complete
```

---

## Tool 5: Evidence Capture Automation

**Script**: `scripts/prehandover-capture.sh`  
**Purpose**: Automatically execute artifacts and capture evidence  
**Authority**: Execution Bootstrap Protocol v2.0.0+, Wave 3.2

### Basic Usage

```bash
# Capture single artifact
./scripts/prehandover-capture.sh -- "python3 scripts/validate-builder-environment.py"

# Capture multiple artifacts
./scripts/prehandover-capture.sh -- \
  "ruff check --select UP ." \
  "pytest tests/" \
  "python3 governance/scripts/validate_prehandover_proof.py PROOF.md"

# Custom output location
./scripts/prehandover-capture.sh \
  -o PREHANDOVER_PROOF_PR_123.md \
  -- "command1" "command2"

# Dry run (test without executing)
./scripts/prehandover-capture.sh --dry-run -- "command1" "command2"
```

### Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `-d, --evidence-dir DIR` | Evidence output directory | "evidence/prehandover" |
| `-o, --output FILE` | PREHANDOVER_PROOF output file | "PREHANDOVER_PROOF_{timestamp}.md" |
| `-n, --dry-run` | Show what would execute without running | False |
| `-h, --help` | Show help message | - |

### What It Captures

For each artifact:
1. **Execution logs** - Full stdout/stderr to `.log` files
2. **Exit codes** - Saved to `.exitcode` files
3. **Timestamps** - Start and end times (UTC)
4. **Metadata** - JSON file with all execution details

### Output Structure

```
evidence/prehandover/capture_TIMESTAMP/
├── artifact_001.log       # Execution output
├── artifact_001.exitcode  # Exit code (0 or error)
├── artifact_001.meta      # JSON metadata
├── artifact_002.log
├── artifact_002.exitcode
├── artifact_002.meta
└── ...
```

### Generated PREHANDOVER_PROOF

The script auto-generates a partial PREHANDOVER_PROOF with:
- Evidence Capture ID
- Step 3: Exit code table (auto-populated)
- Step 4: Evidence collection (with logs embedded)

### Next Steps After Capture

1. Review evidence in `evidence/prehandover/{capture_id}/`
2. Complete remaining PREHANDOVER_PROOF sections (Steps 1, 2, 5, 6, 7)
3. Fill in metadata placeholders
4. Add Agent Attestation
5. Validate with `validate_prehandover_proof.py`

---

## Complete Workflow Example

### Scenario: Wave 3.2 Builder Handover

```bash
# Step 1: Validate environment
python3 scripts/validate-builder-environment.py

# Step 2: Install hooks (if not already done)
./scripts/install-git-hooks.sh

# Step 3: Generate PREHANDOVER_PROOF template
python3 scripts/generate-prehandover-proof-template.py \
  --agent "API Builder" \
  --pr 543 \
  --wave "Wave 3.2" \
  --branch "feature/wave-3.2-implementation"

# Step 4: Capture evidence for execution artifacts
./scripts/prehandover-capture.sh \
  -o PREHANDOVER_PROOF_PR_543.md \
  -- \
  "bash .githooks/pre-push" \
  "python3 scripts/validate-builder-environment.py" \
  "ruff check --select UP ."

# Step 5: Complete manual sections in PREHANDOVER_PROOF_PR_543.md
# (Edit file to fill in Steps 1, 2, 5, 6, 7, attestation)

# Step 6: Validate PREHANDOVER_PROOF
python3 governance/scripts/validate_prehandover_proof.py \
  PREHANDOVER_PROOF_PR_543.md \
  --verbose

# Step 7: Commit and push
git add PREHANDOVER_PROOF_PR_543.md evidence/
git commit -m "Wave 3.2: Add PREHANDOVER_PROOF with evidence"
git push origin feature/wave-3.2-implementation
```

---

## CI/CD Integration

### GitHub Actions Workflow

The PREHANDOVER_PROOF validation runs automatically on PRs via:
- Workflow: `.github/workflows/prehandover-proof-validation.yml`
- Triggers: When PREHANDOVER_PROOF files are modified
- Gate Type: SOFT (informational, does not block merge)

### What CI Validates

1. PREHANDOVER_PROOF file exists (if execution artifacts modified)
2. All required sections present
3. Exit codes documented and all 0
4. Evidence complete
5. Agent attestation present

### CI Outcomes

- ✅ **PASS**: PREHANDOVER_PROOF valid and complete
- ⚠️ **INCOMPLETE**: Issues found (informational warning)
- ℹ️ **SKIP**: No PREHANDOVER_PROOF files in PR

---

## Troubleshooting

### Issue: ruff not found

```bash
# Install ruff
pip install ruff

# Or use the hook installer
./scripts/install-git-hooks.sh
# (It will offer to install ruff)
```

### Issue: Git hooks not running

```bash
# Check hooks path
git config core.hooksPath

# Should return: .githooks

# If not set, run installer
./scripts/install-git-hooks.sh
```

### Issue: PREHANDOVER_PROOF validation fails

```bash
# Run validator in verbose mode to see details
python3 governance/scripts/validate_prehandover_proof.py PROOF.md --verbose

# Check specific issues:
# - All metadata fields filled? (Agent, PR, Branch, Date, Commit, Protocol Version)
# - All 7 steps of Category 0 present?
# - All exit codes are 0?
# - Evidence includes logs, timestamps, outputs?
# - Agent Attestation section exists?
# - Hard rules acknowledged? ("CI is confirmation, NOT diagnostic")
```

### Issue: Evidence capture fails

```bash
# Use dry-run to test without executing
./scripts/prehandover-capture.sh --dry-run -- "command"

# Check command syntax
# Each command must be quoted if it contains spaces
# Example: "./scripts/prehandover-capture.sh -- \"pytest tests/\" \"ruff check .\""
```

---

## References

- **BL-026**: `governance/policies/AUTOMATED_DEPRECATION_DETECTION_GATE.md`
- **Execution Bootstrap Protocol**: `governance/canon/EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md`
- **Git Hooks**: `.githooks/README.md`
- **Wave 3.2 Spec**: (See PR description)

---

## Support

For issues or questions:
- Run validation scripts with `--help` flag
- Check script documentation headers
- Review error messages (they include remediation guidance)
- Escalate to FM if blocked

---

**Last Updated**: 2026-01-13  
**Version**: 1.0.0  
**Authority**: Wave 3.2 - Deprecation Gate + Bootstrap Enforcement
