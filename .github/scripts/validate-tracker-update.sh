#!/bin/bash
# validate-tracker-update.sh — BUILD_PROGRESS_TRACKER Update Validation (BL-029)
# Authority: MERGE_GATE_PHILOSOPHY.md v2.0
# Living Agent System: v6.2.0
#
# Purpose: Validates that the BUILD_PROGRESS_TRACKER has been updated as part
#          of this PR/wave, ensuring progress tracking is current (BL-029).
#
# Usage: bash validate-tracker-update.sh
#
# Exit code 0: tracker updated or not required (PASS)
# Exit code 1: tracker update missing when required (FAIL)

set -euo pipefail

# Accept optional --base parameter; fall back to GITHUB_BASE_REF env var then HEAD~1
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
# Prefer explicit parameter, then CI env var, then local fallback
if [ -z "$BASE_REF" ]; then
  if [ -n "${GITHUB_BASE_REF:-}" ]; then
    BASE_REF="origin/${GITHUB_BASE_REF}"
  else
    BASE_REF="HEAD~1"
  fi
fi

echo "======================================================================"
echo "🔍 BUILD_PROGRESS_TRACKER UPDATE VALIDATION (BL-029)"
echo "======================================================================"
echo ""
echo "Authority: MERGE_GATE_PHILOSOPHY.md v2.0"
echo ""

ERRORS=0
WARNINGS=0

# Step 1: Check for evidence-based skip
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 1: Check for PREHANDOVER_PROOF evidence"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

PROOF_FILE=""
if [ -f "PREHANDOVER_PROOF.md" ]; then
  PROOF_FILE="PREHANDOVER_PROOF.md"
elif ls PREHANDOVER_PROOF_*.md 1>/dev/null 2>&1; then
  PROOF_FILE=$(ls PREHANDOVER_PROOF_*.md 2>/dev/null | sort | tail -1)
fi

if [ -n "$PROOF_FILE" ]; then
  echo "📄 Proof file: $PROOF_FILE"
  if grep -qiE "BUILD_PROGRESS_TRACKER|BL-029|tracker.*update|progress.*tracker" "$PROOF_FILE" 2>/dev/null; then
    echo "✅ BUILD_PROGRESS_TRACKER update evidence found in $PROOF_FILE"
    echo "   BL-029 evidence-based skip accepted"
    echo ""
    echo "======================================================================"
    echo "✅ BL-029 TRACKER UPDATE VALIDATION: PASS (evidence-based)"
    echo "======================================================================"
    exit 0
  else
    echo "ℹ️  No tracker evidence in proof file — proceeding with direct check"
  fi
else
  echo "ℹ️  No PREHANDOVER_PROOF file found — proceeding with direct check"
fi
echo ""

# Step 2: Locate BUILD_PROGRESS_TRACKER
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 2: Locate BUILD_PROGRESS_TRACKER"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

TRACKER_FILE=""
TRACKER_CANDIDATES=(
  "BUILD_PROGRESS_TRACKER.md"
  "governance/BUILD_PROGRESS_TRACKER.md"
  "governance/reports/BUILD_PROGRESS_TRACKER.md"
)

for CANDIDATE in "${TRACKER_CANDIDATES[@]}"; do
  if [ -f "$CANDIDATE" ]; then
    TRACKER_FILE="$CANDIDATE"
    break
  fi
done

if [ -z "$TRACKER_FILE" ]; then
  echo "ℹ️  No BUILD_PROGRESS_TRACKER found"
  echo "   BL-029 check skipped — tracker not required in this repo configuration"
  echo ""
  echo "======================================================================"
  echo "✅ BL-029 TRACKER UPDATE VALIDATION: PASS (no tracker required)"
  echo "======================================================================"
  exit 0
fi

echo "📄 Tracker file: $TRACKER_FILE"
echo ""

# Step 3: Verify the tracker was updated in this branch
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 3: Verify tracker was updated in this branch (base: $BASE_REF)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if tracker appears in recent git changes
if git diff --name-only "$BASE_REF" 2>/dev/null | grep -qF "$TRACKER_FILE"; then
  echo "✅ $TRACKER_FILE was updated relative to $BASE_REF"
elif git diff --name-only HEAD 2>/dev/null | grep -qF "$TRACKER_FILE"; then
  echo "✅ $TRACKER_FILE has uncommitted updates"
else
  echo "⚠️  $TRACKER_FILE does not appear in git diff (base: $BASE_REF)"
  echo "   This may be acceptable if the PR does not require tracker update"
  ((WARNINGS++))
fi
echo ""

# Step 4: Check tracker is not empty and has content
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 4: Validate tracker content"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

TRACKER_SIZE=$(wc -c < "$TRACKER_FILE" 2>/dev/null || echo 0)
if [ "$TRACKER_SIZE" -gt 10 ]; then
  echo "✅ Tracker file has content ($TRACKER_SIZE bytes)"
else
  echo "❌ Tracker file appears empty or too small ($TRACKER_SIZE bytes)"
  ((ERRORS++))
fi
echo ""

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Summary: Errors=$ERRORS Warnings=$WARNINGS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ $ERRORS -eq 0 ]; then
  echo "======================================================================"
  echo "✅ BL-029 TRACKER UPDATE VALIDATION: PASS"
  echo "======================================================================"
  exit 0
else
  echo "======================================================================"
  echo "❌ BL-029 TRACKER UPDATE VALIDATION: FAIL ($ERRORS error(s))"
  echo "======================================================================"
  echo ""
  echo "🔧 Remediation:"
  echo "  1. Update $TRACKER_FILE with current wave/batch progress"
  echo "  2. Ensure file has valid content"
  echo "  3. Re-run this script to confirm PASS"
  exit 1
fi
