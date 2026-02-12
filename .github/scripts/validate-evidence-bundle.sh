#!/bin/bash
# Evidence Bundle Validation Script
# Per EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md
# Authority: Living Agent System v6.2.0

set -euo pipefail

echo "======================================================================"
echo "🔍 EVIDENCE ARTIFACT BUNDLE VALIDATION"
echo "======================================================================"
echo ""
echo "Per EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md v1.0.0"
echo ""

ERRORS=0
WARNINGS=0

# Check required root directory
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Checking Required Root Directory"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ ! -d ".agent-admin" ]; then
  echo "❌ CRITICAL: .agent-admin/ directory not found"
  ((ERRORS++))
else
  echo "✅ .agent-admin/ directory exists"
fi
echo ""

# Check required subdirectories
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Checking Required Subdirectories"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

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
echo ""

# Check required files
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Checking Required Files"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

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
    
    # Validate JSON files
    if [[ "$FILE" == *.json ]]; then
      if jq empty "$FILE" 2>/dev/null; then
        echo "   ✅ Valid JSON"
      else
        echo "   ❌ Invalid JSON syntax"
        ((ERRORS++))
      fi
    fi
  fi
done
echo ""

# Check prehandover proof (at least one .md file)
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Checking Prehandover Proof"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ ! -d ".agent-admin/prehandover" ]; then
  echo "❌ Prehandover directory missing (already reported)"
elif [ -z "$(find .agent-admin/prehandover -name '*.md' -type f 2>/dev/null)" ]; then
  echo "❌ Missing prehandover proof (.md file in .agent-admin/prehandover/)"
  ((ERRORS++))
else
  PROOF_COUNT=$(find .agent-admin/prehandover -name '*.md' -type f 2>/dev/null | wc -l)
  echo "✅ Prehandover proof exists ($PROOF_COUNT file(s))"
  
  # List proof files
  find .agent-admin/prehandover -name '*.md' -type f 2>/dev/null | while read -r PROOF; do
    echo "   - $(basename $PROOF)"
  done
fi
echo ""

# Check RCA directory (conditional)
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Checking RCA (Conditional)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if stop-and-fix indicators present
SAF_INDICATOR=false
if [ -f ".agent-admin/improvements/improvements.md" ]; then
  if grep -qi "stop.and.fix\|stop-and-fix" .agent-admin/improvements/improvements.md; then
    SAF_INDICATOR=true
  fi
fi

if [ "$SAF_INDICATOR" = "true" ]; then
  echo "ℹ️  Stop-and-fix indicator detected in improvements.md"
  echo "   RCA is REQUIRED per EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md § 4"
  echo ""
  
  if [ ! -d ".agent-admin/rca" ] || [ -z "$(find .agent-admin/rca -name '*.md' -type f 2>/dev/null)" ]; then
    echo "❌ RCA required but not found"
    ((ERRORS++))
  else
    RCA_COUNT=$(find .agent-admin/rca -name '*.md' -type f 2>/dev/null | wc -l)
    echo "✅ RCA exists ($RCA_COUNT file(s))"
  fi
else
  echo "ℹ️  No stop-and-fix indicators detected"
  echo "   RCA not required (unless gate failed and was repaired)"
  
  if [ -d ".agent-admin/rca" ] && [ -n "$(find .agent-admin/rca -name '*.md' -type f 2>/dev/null)" ]; then
    RCA_COUNT=$(find .agent-admin/rca -name '*.md' -type f 2>/dev/null | wc -l)
    echo "   ✅ RCA present anyway ($RCA_COUNT file(s)) - good practice"
  fi
fi
echo ""

# Validate gate-results.json schema
if [ -f ".agent-admin/gates/gate-results.json" ]; then
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Validating gate-results.json Schema"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
  
  # Check required fields per EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md § 5
  REQUIRED_FIELDS=(
    ".timestamp"
    ".pr_number"
    ".verdict"
    ".gates"
    ".test_results"
  )
  
  MISSING_FIELDS=()
  for FIELD in "${REQUIRED_FIELDS[@]}"; do
    if ! jq -e "$FIELD" .agent-admin/gates/gate-results.json >/dev/null 2>&1; then
      MISSING_FIELDS+=("$FIELD")
    fi
  done
  
  if [ ${#MISSING_FIELDS[@]} -gt 0 ]; then
    echo "❌ gate-results.json missing required fields:"
    for FIELD in "${MISSING_FIELDS[@]}"; do
      echo "   - $FIELD"
    done
    ((ERRORS++))
  else
    echo "✅ All required fields present"
    
    # Display summary
    VERDICT=$(jq -r '.verdict // "UNKNOWN"' .agent-admin/gates/gate-results.json)
    echo ""
    echo "Summary:"
    echo "  - Verdict: $VERDICT"
    
    if jq -e '.test_results' .agent-admin/gates/gate-results.json >/dev/null 2>&1; then
      TEST_DEBT=$(jq -r '.test_results.test_debt // "UNKNOWN"' .agent-admin/gates/gate-results.json)
      echo "  - Test Debt: $TEST_DEBT"
    fi
  fi
  echo ""
fi

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Validation Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
  echo "✅ EVIDENCE BUNDLE VALID"
  echo ""
  echo "All required artifacts present and valid."
  echo ""
  echo "======================================================================"
  echo "✅ VALIDATION PASSED"
  echo "======================================================================"
  exit 0
elif [ $ERRORS -eq 0 ] && [ $WARNINGS -gt 0 ]; then
  echo "⚠️  EVIDENCE BUNDLE VALID WITH WARNINGS"
  echo ""
  echo "Warnings: $WARNINGS"
  echo "Consider addressing warnings for completeness."
  echo ""
  echo "======================================================================"
  echo "✅ VALIDATION PASSED (with warnings)"
  echo "======================================================================"
  exit 0
else
  echo "❌ EVIDENCE BUNDLE INVALID"
  echo ""
  echo "Errors: $ERRORS"
  echo "Warnings: $WARNINGS"
  echo ""
  echo "🔧 Remediation:"
  echo "  1. Create missing directories/files"
  echo "  2. Fix JSON syntax errors"
  echo "  3. Ensure all required fields present in JSON files"
  echo "  4. Create RCA if stop-and-fix occurred"
  echo "  5. Re-run this validation script"
  echo ""
  echo "📚 Authority: EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md"
  echo ""
  echo "======================================================================"
  echo "❌ VALIDATION FAILED ($ERRORS errors)"
  echo "======================================================================"
  exit 1
fi
