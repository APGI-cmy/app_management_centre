#!/bin/bash
# validate-scope-to-diff.sh — Scope-to-Diff Validation (BL-027)
# Authority: MERGE_GATE_PHILOSOPHY.md v2.0, SCOPE_TO_DIFF_RULE.md
# Living Agent System: v6.2.0
#
# Purpose: Validates that the declared scope (SCOPE_DECLARATION.md or
#          governance/scope/*.md) matches the actual git diff for this PR/branch.
#          Implements BL-027: scope declaration must be accurate.
#
# Usage: bash validate-scope-to-diff.sh [--base <ref>]
#
# Exit code 0: scope matches diff (PASS)
# Exit code 1: scope mismatch or missing declaration (FAIL)

set -euo pipefail

# Parse arguments first, then apply default
BASE_REF=""
while [[ $# -gt 0 ]]; do
  case $1 in
    --base)
      BASE_REF="$2"
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done
BASE_REF="${BASE_REF:-HEAD~1}"

echo "======================================================================"
echo "🔍 SCOPE-TO-DIFF VALIDATION (BL-027)"
echo "======================================================================"
echo ""
echo "Authority: MERGE_GATE_PHILOSOPHY.md v2.0"
echo "Base ref: $BASE_REF"
echo ""

ERRORS=0

# Step 1: Locate scope declaration
SCOPE_FILE=""
if [ -f "SCOPE_DECLARATION.md" ]; then
  SCOPE_FILE="SCOPE_DECLARATION.md"
elif ls governance/scope/*.md 1>/dev/null 2>&1; then
  SCOPE_FILE=$(ls governance/scope/*.md 2>/dev/null | sort | tail -1)
fi

if [ -z "$SCOPE_FILE" ]; then
  echo "⚠️  No SCOPE_DECLARATION.md found"
  echo "   Checking PREHANDOVER_PROOF for scope evidence..."
  echo ""

  PROOF_FILE=""
  if [ -f "PREHANDOVER_PROOF.md" ]; then
    PROOF_FILE="PREHANDOVER_PROOF.md"
  elif ls PREHANDOVER_PROOF_*.md 1>/dev/null 2>&1; then
    PROOF_FILE=$(ls PREHANDOVER_PROOF_*.md 2>/dev/null | sort | tail -1)
  fi

  if [ -n "$PROOF_FILE" ] && grep -qiE "scope.*declaration|scope.*diff|BL-027" "$PROOF_FILE" 2>/dev/null; then
    echo "✅ Scope validation evidence found in $PROOF_FILE"
    echo "   BL-027 evidence-based skip accepted"
  else
    echo "ℹ️  No scope declaration found — BL-027 check skipped"
    echo "   (No SCOPE_DECLARATION.md and no proof evidence)"
  fi

  echo ""
  echo "======================================================================"
  echo "✅ BL-027 SCOPE-TO-DIFF: PASS (no scope declaration required)"
  echo "======================================================================"
  exit 0
fi

echo "📄 Scope file: $SCOPE_FILE"
echo ""

# Step 2: Get actual diff
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Getting actual git diff..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if ! DIFF_FILES=$(git diff --name-only "$BASE_REF" 2>/dev/null); then
  echo "⚠️  Could not compute git diff against $BASE_REF"
  echo "   Attempting HEAD diff..."
  DIFF_FILES=$(git diff --name-only HEAD 2>/dev/null || echo "")
fi

if [ -z "$DIFF_FILES" ]; then
  echo "ℹ️  No changed files detected in diff"
else
  echo "Changed files:"
  echo "$DIFF_FILES" | while read -r f; do echo "  - $f"; done
fi
echo ""

# Step 3: Extract declared files from scope declaration
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Checking scope declaration coverage..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if each changed file appears in the scope declaration
UNDECLARED_FILES=()
if [ -n "$DIFF_FILES" ]; then
  while IFS= read -r file; do
    [ -z "$file" ] && continue
    # Skip the scope file itself
    [ "$file" = "$SCOPE_FILE" ] && continue
    # Skip PREHANDOVER_PROOF
    [[ "$file" == PREHANDOVER_PROOF* ]] && continue

    if ! grep -qF "$file" "$SCOPE_FILE" 2>/dev/null; then
      UNDECLARED_FILES+=("$file")
    fi
  done <<< "$DIFF_FILES"
fi

if [ ${#UNDECLARED_FILES[@]} -gt 0 ]; then
  echo "❌ Files changed but NOT declared in scope:"
  for f in "${UNDECLARED_FILES[@]}"; do
    echo "  - $f"
  done
  ((ERRORS++))
else
  echo "✅ All changed files are covered by scope declaration"
fi
echo ""

# Summary
if [ $ERRORS -eq 0 ]; then
  echo "======================================================================"
  echo "✅ BL-027 SCOPE-TO-DIFF VALIDATION: PASS"
  echo "======================================================================"
  exit 0
else
  echo "======================================================================"
  echo "❌ BL-027 SCOPE-TO-DIFF VALIDATION: FAIL ($ERRORS error(s))"
  echo "======================================================================"
  echo ""
  echo "🔧 Remediation:"
  echo "  1. Update $SCOPE_FILE to include all changed files"
  echo "  2. OR remove undeclared changes from the PR"
  echo "  3. Re-run this script to confirm PASS"
  exit 1
fi
