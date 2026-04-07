#!/bin/bash
# generate-evidence-bundle.sh — Evidence Bundle Generator
# Authority: EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md, MERGE_GATE_PHILOSOPHY.md v2.0
# Living Agent System: v6.2.0
#
# Purpose: Generates a structured evidence bundle for a wave/session handover.
#          Collects gate results, test results, and proof artifacts into a
#          dated bundle under .agent-admin/.
#
# Usage: bash generate-evidence-bundle.sh [--session <ID>] [--wave <N>] [--agent <id>]
#
# Exit code 0: bundle generated successfully
# Exit code 1: bundle generation failed

set -euo pipefail

# Default parameters
SESSION_ID="unknown"
WAVE_ID="unknown"
AGENT_ID="unknown"
TIMESTAMP=$(date -u +%Y%m%dT%H%M%SZ)
DATE_SLUG=$(date -u +%Y%m%d)

# Parse arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --session)
      SESSION_ID="$2"
      shift 2
      ;;
    --wave)
      WAVE_ID="$2"
      shift 2
      ;;
    --agent)
      AGENT_ID="$2"
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done

BUNDLE_DIR=".agent-admin/evidence-bundles"
BUNDLE_NAME="evidence-bundle-${SESSION_ID}-wave${WAVE_ID}-${DATE_SLUG}"
BUNDLE_PATH="$BUNDLE_DIR/$BUNDLE_NAME"
BUNDLE_MANIFEST="$BUNDLE_PATH/manifest.json"

echo "======================================================================"
echo "📦 EVIDENCE BUNDLE GENERATOR"
echo "======================================================================"
echo ""
echo "Authority: EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md"
echo "Session:   $SESSION_ID"
echo "Wave:      $WAVE_ID"
echo "Agent:     $AGENT_ID"
echo "Timestamp: $TIMESTAMP"
echo "Bundle:    $BUNDLE_PATH"
echo ""

ERRORS=0

# Step 1: Create bundle directory structure
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 1: Create bundle directory"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

mkdir -p "$BUNDLE_PATH/gates"
mkdir -p "$BUNDLE_PATH/proofs"
mkdir -p "$BUNDLE_PATH/tests"
echo "✅ Bundle directory created: $BUNDLE_PATH"
echo ""

# Step 2: Collect PREHANDOVER_PROOF artifacts
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 2: Collect PREHANDOVER_PROOF artifacts"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

PROOF_FILES=()
if [ -f "PREHANDOVER_PROOF.md" ]; then
  cp "PREHANDOVER_PROOF.md" "$BUNDLE_PATH/proofs/"
  PROOF_FILES+=("PREHANDOVER_PROOF.md")
  echo "✅ Collected: PREHANDOVER_PROOF.md"
fi

for PROOF in PREHANDOVER_PROOF_*.md; do
  if [ -f "$PROOF" ]; then
    cp "$PROOF" "$BUNDLE_PATH/proofs/"
    PROOF_FILES+=("$PROOF")
    echo "✅ Collected: $PROOF"
  fi
done

for PROOF in .agent-workspace/foreman-v2/memory/PREHANDOVER-*.md; do
  if [ -f "$PROOF" ]; then
    cp "$PROOF" "$BUNDLE_PATH/proofs/"
    PROOF_FILES+=("$PROOF")
    echo "✅ Collected: $PROOF"
  fi
done

if [ ${#PROOF_FILES[@]} -eq 0 ]; then
  echo "⚠️  No PREHANDOVER_PROOF files found"
  ((ERRORS++))
fi
echo ""

# Step 3: Collect gate results
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 3: Collect gate results"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

GATE_FILES=()
if [ -f ".agent-admin/gates/gate-results.json" ]; then
  cp ".agent-admin/gates/gate-results.json" "$BUNDLE_PATH/gates/"
  GATE_FILES+=("gate-results.json")
  echo "✅ Collected: .agent-admin/gates/gate-results.json"
fi

for GATE_FILE in .agent-admin/gates/*.json; do
  if [ -f "$GATE_FILE" ] && [[ "$GATE_FILE" != *"gate-results.json" ]]; then
    cp "$GATE_FILE" "$BUNDLE_PATH/gates/"
    GATE_FILES+=("$(basename "$GATE_FILE")")
    echo "✅ Collected: $GATE_FILE"
  fi
done
echo ""

# Step 4: Collect IAA assurance artifacts
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 4: Collect IAA assurance artifacts"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

IAA_FILES=()
for IAA_FILE in .agent-admin/assurance/iaa-token-*.md .agent-admin/assurance/iaa-prebrief-*.md; do
  if [ -f "$IAA_FILE" ]; then
    mkdir -p "$BUNDLE_PATH/assurance"
    cp "$IAA_FILE" "$BUNDLE_PATH/assurance/"
    IAA_FILES+=("$(basename "$IAA_FILE")")
    echo "✅ Collected: $IAA_FILE"
  fi
done

if [ ${#IAA_FILES[@]} -eq 0 ]; then
  echo "ℹ️  No IAA assurance artifacts found"
fi
echo ""

# Step 5: Generate bundle manifest
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 5: Generate manifest"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")
GIT_COMMIT=$(git rev-parse HEAD 2>/dev/null || echo "unknown")

# Build JSON arrays for files (handle empty arrays correctly)
if [ ${#PROOF_FILES[@]} -gt 0 ]; then
  PROOF_JSON=$(printf '"%s",' "${PROOF_FILES[@]}" | sed 's/,$//')
else
  PROOF_JSON=""
fi
if [ ${#GATE_FILES[@]} -gt 0 ]; then
  GATE_JSON=$(printf '"%s",' "${GATE_FILES[@]}" | sed 's/,$//')
else
  GATE_JSON=""
fi
if [ ${#IAA_FILES[@]} -gt 0 ]; then
  IAA_JSON=$(printf '"%s",' "${IAA_FILES[@]}" | sed 's/,$//')
else
  IAA_JSON=""
fi

cat > "$BUNDLE_MANIFEST" <<EOF
{
  "bundle_name": "$BUNDLE_NAME",
  "generated_at": "$TIMESTAMP",
  "session_id": "$SESSION_ID",
  "wave_id": "$WAVE_ID",
  "agent_id": "$AGENT_ID",
  "git_branch": "$GIT_BRANCH",
  "git_commit": "$GIT_COMMIT",
  "artifacts": {
    "proofs": [${PROOF_JSON}],
    "gates": [${GATE_JSON}],
    "iaa": [${IAA_JSON}]
  },
  "errors": $ERRORS,
  "authority": "EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md"
}
EOF

if ! command -v jq &>/dev/null; then
  echo "❌ jq is not installed — cannot validate manifest JSON"
  ((ERRORS++))
elif jq empty "$BUNDLE_MANIFEST" 2>/dev/null; then
  echo "✅ Manifest generated and valid: $BUNDLE_MANIFEST"
else
  echo "❌ Manifest JSON is invalid"
  ((ERRORS++))
fi
echo ""

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  Proof files:    ${#PROOF_FILES[@]}"
echo "  Gate files:     ${#GATE_FILES[@]}"
echo "  IAA files:      ${#IAA_FILES[@]}"
echo "  Errors:         $ERRORS"
echo "  Bundle path:    $BUNDLE_PATH"
echo ""

if [ $ERRORS -eq 0 ]; then
  echo "======================================================================"
  echo "✅ EVIDENCE BUNDLE GENERATION: PASS"
  echo "======================================================================"
  exit 0
else
  echo "======================================================================"
  echo "❌ EVIDENCE BUNDLE GENERATION: FAIL ($ERRORS error(s))"
  echo "======================================================================"
  echo ""
  echo "🔧 Remediation:"
  echo "  1. Ensure PREHANDOVER_PROOF.md exists before generating bundle"
  echo "  2. Re-run this script after creating required artifacts"
  exit 1
fi
