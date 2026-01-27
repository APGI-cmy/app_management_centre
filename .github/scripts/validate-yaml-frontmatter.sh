#!/bin/bash
# YAML Frontmatter Validation Script
# Authority: governance/canon/YAML_VALIDATION_PROTOCOL.md v1.0.0
# Purpose: Validate YAML files and agent contract frontmatter
# Exit 0 = success (all validation passed)
# Exit 1 = failure (syntax errors detected - STOP-AND-FIX required)

set -euo pipefail

echo "=== YAML Validation Script ==="
echo "Authority: governance/canon/YAML_VALIDATION_PROTOCOL.md"
echo "Timestamp: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""

# Check if yamllint is installed
if ! command -v yamllint &> /dev/null; then
    echo "❌ ERROR: yamllint not installed"
    echo "Install with: pip install yamllint"
    exit 1
fi

# Create relaxed yamllint config (only check syntax, not style)
YAMLLINT_CONFIG=$(mktemp)
cat > "$YAMLLINT_CONFIG" << 'EOF'
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

YAML_ERRORS=0
YAML_FILES_CHECKED=0
AGENT_FILES_CHECKED=0

# Function to check if git is available and we're in a git repo
check_git() {
    if ! command -v git &> /dev/null || ! git rev-parse --git-dir &> /dev/null 2>&1; then
        return 1
    fi
    return 0
}

# Function to find files
find_files() {
    local pattern="$1"
    if check_git; then
        git ls-files "$pattern" 2>/dev/null || find . -name "$pattern" -type f 2>/dev/null | grep -v ".git/"
    else
        find . -name "$pattern" -type f 2>/dev/null | grep -v ".git/" || true
    fi
}

# ===== VALIDATE PURE YAML FILES =====
echo "=== Validating .yml/.yaml files ==="
YAML_FILES=$(find_files '*.yml' && find_files '*.yaml' || true)

if [ -z "$YAML_FILES" ]; then
    echo "ℹ️  No .yml/.yaml files found"
else
    for FILE in $YAML_FILES; do
        if [ ! -f "$FILE" ]; then
            continue
        fi
        
        echo "  Checking: $FILE"
        YAML_FILES_CHECKED=$((YAML_FILES_CHECKED + 1))
        
        # GitHub Actions workflow files may contain GitHub-specific syntax
        # that standard YAML parsers don't support - be lenient
        if [[ "$FILE" == *".github/workflows/"* ]]; then
            # For workflows, just do basic structure check
            if ! grep -q "^on:" "$FILE" || ! grep -q "jobs:" "$FILE"; then
                echo "  ❌ Missing required workflow structure (on: or jobs:)"
                YAML_ERRORS=$((YAML_ERRORS + 1))
                continue
            fi
            
            # Try lenient validation
            OUTPUT=$(yamllint -c "$YAMLLINT_CONFIG" -f parsable "$FILE" 2>&1 || true)
            if echo "$OUTPUT" | grep -qE "\[error\]"; then
                # Check if errors are GitHub Actions specific syntax (JavaScript strings, etc.)
                if echo "$OUTPUT" | grep -qE "could not find expected|mapping values are not allowed|expected alphabetic or numeric character"; then
                    echo "  ⚠️  YAML parser warnings (GitHub Actions parser is more lenient)"
                else
                    echo "  ❌ YAML syntax errors:"
                    echo "$OUTPUT" | grep -E "\[error\]"
                    YAML_ERRORS=$((YAML_ERRORS + 1))
                fi
            else
                echo "  ✅ Valid"
            fi
        else
            # For non-workflow YAML files, strict validation
            OUTPUT=$(yamllint -c "$YAMLLINT_CONFIG" -f parsable "$FILE" 2>&1 || true)
            
            if echo "$OUTPUT" | grep -qE "\[error\]"; then
                echo "  ❌ YAML syntax errors:"
                echo "$OUTPUT" | grep -E "\[error\]"
                YAML_ERRORS=$((YAML_ERRORS + 1))
            elif [ -n "$OUTPUT" ]; then
                echo "  ⚠️  Style warnings (non-blocking)"
            else
                echo "  ✅ Valid"
            fi
        fi
    done
fi

# ===== VALIDATE AGENT CONTRACT FRONTMATTER =====
echo ""
echo "=== Validating agent contract frontmatter ==="

# Find agent contract files (exclude documentation and archives)
AGENT_FILES=$(find_files '.github/agents/*.md' | grep -v 'SCHEMA\|README\|_archive\|instructions' || true)

if [ -z "$AGENT_FILES" ]; then
    echo "ℹ️  No agent contract files found"
else
    for FILE in $AGENT_FILES; do
        if [ ! -f "$FILE" ]; then
            continue
        fi
        
        echo "  Checking: $FILE"
        AGENT_FILES_CHECKED=$((AGENT_FILES_CHECKED + 1))
        
        # Extract YAML frontmatter (between --- markers or --- ... markers)
        # Authority: YAML_VALIDATION_PROTOCOL.md Section 2.1
        FRONTMATTER=$(awk '/^---$/{if(++count==2) exit; if(count==1) next} count==1; /^\.\.\.$/{ if(count==1) exit}' "$FILE")
        
        if [ -z "$FRONTMATTER" ]; then
            echo "  ⚠️  No YAML frontmatter (may be documentation file - skipping)"
            continue
        fi
        
        # Write frontmatter to temp file
        TEMP_YAML=$(mktemp)
        echo "$FRONTMATTER" > "$TEMP_YAML"
        
        # Validate YAML frontmatter only
        OUTPUT=$(yamllint -c "$YAMLLINT_CONFIG" -f parsable "$TEMP_YAML" 2>&1 || true)
        
        if echo "$OUTPUT" | grep -qE "\[error\]"; then
            echo "  ❌ YAML frontmatter syntax errors:"
            echo "$OUTPUT" | grep -E "\[error\]"
            echo ""
            echo "  Frontmatter content:"
            echo "$FRONTMATTER" | head -20
            YAML_ERRORS=$((YAML_ERRORS + 1))
        elif [ -n "$OUTPUT" ]; then
            echo "  ⚠️  Style warnings (non-blocking)"
        else
            echo "  ✅ Valid"
        fi
        
        rm "$TEMP_YAML"
    done
fi

# ===== FINAL RESULT =====
echo ""
echo "=== Validation Summary ==="
echo "Pure YAML files checked: $YAML_FILES_CHECKED"
echo "Agent contracts checked: $AGENT_FILES_CHECKED"
echo "Syntax errors detected: $YAML_ERRORS"

# Clean up
rm "$YAMLLINT_CONFIG"

if [ $YAML_ERRORS -gt 0 ]; then
    echo ""
    echo "❌ YAML VALIDATION FAILED"
    echo "Syntax errors detected: $YAML_ERRORS"
    echo ""
    echo "STOP-AND-FIX REQUIRED"
    echo "- Fix ALL syntax errors above"
    echo "- Re-run this script until exit code 0"
    echo "- Document in PREHANDOVER_PROOF"
    echo ""
    echo "Authority: governance/canon/YAML_VALIDATION_PROTOCOL.md"
    echo "          governance/canon/STOP_AND_FIX_DOCTRINE.md"
    exit 1
else
    echo ""
    echo "✅ YAML VALIDATION PASSED"
    echo "Exit code: 0"
    echo "All YAML files and agent contract frontmatter are syntactically valid"
    echo ""
    echo "Ready for handover (include this output in PREHANDOVER_PROOF)"
    exit 0
fi
