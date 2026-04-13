#!/bin/bash
# check-evidence.sh — Evidence-Based Validation Skip Check
# Authority: MERGE_GATE_PHILOSOPHY.md v2.0, EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md
# Living Agent System: v6.2.0
#
# Purpose: Checks whether a PREHANDOVER_PROOF file contains evidence for a
#          specific gate check, allowing CI to accept agent-validated evidence
#          rather than re-executing the gate script.
#
# Usage: bash check-evidence.sh "<check_name>" "<pattern>"
#
# Outputs "skip_execution=true" (stdout) when evidence is found.
# Exit code 0 on success (evidence found or graceful not-found), 1 on error.

set -euo pipefail

CHECK_NAME="${1:-unknown}"
PATTERN="${2:-}"

if [ -z "$PATTERN" ]; then
  echo "Usage: $0 \"<check_name>\" \"<pattern>\"" >&2
  exit 1
fi

echo "======================================================================"
echo "🔍 EVIDENCE-BASED VALIDATION CHECK"
echo "======================================================================"
echo ""
echo "Check: $CHECK_NAME"
echo "Pattern: $PATTERN"
echo ""

# Locate PREHANDOVER_PROOF or wave record file
# Search order:
#   1. Repo root: PREHANDOVER_PROOF.md
#   2. Repo root: PREHANDOVER_PROOF_*.md (dated variants)
#   3. AMC agent-workspace: .agent-workspace/foreman-v2/memory/PREHANDOVER-*.md
#   4. Broader fallback: .agent-workspace/*/memory/PREHANDOVER-*.md
#   5. Wave records (90/10 model): .agent-admin/wave-records/amc-wave-record-*.md
PROOF_FILE=""
if [ -f "PREHANDOVER_PROOF.md" ]; then
  PROOF_FILE="PREHANDOVER_PROOF.md"
elif ls PREHANDOVER_PROOF_*.md 1>/dev/null 2>&1; then
  PROOF_FILE=$(ls PREHANDOVER_PROOF_*.md 2>/dev/null | sort | tail -1)
elif ls .agent-workspace/foreman-v2/memory/PREHANDOVER-*.md 1>/dev/null 2>&1; then
  PROOF_FILE=$(ls .agent-workspace/foreman-v2/memory/PREHANDOVER-*.md 2>/dev/null | sort | tail -1)
elif ls .agent-workspace/*/memory/PREHANDOVER-*.md 1>/dev/null 2>&1; then
  PROOF_FILE=$(ls .agent-workspace/*/memory/PREHANDOVER-*.md 2>/dev/null | sort | tail -1)
elif ls .agent-admin/wave-records/amc-wave-record-*.md 1>/dev/null 2>&1; then
  PROOF_FILE=$(ls .agent-admin/wave-records/amc-wave-record-*.md 2>/dev/null | sort | tail -1)
fi

if [ -z "$PROOF_FILE" ]; then
  echo "ℹ️  No PREHANDOVER_PROOF or wave record found — evidence-based skip not available"
  echo "   Searched paths:"
  echo "     - PREHANDOVER_PROOF.md"
  echo "     - PREHANDOVER_PROOF_*.md"
  echo "     - .agent-workspace/foreman-v2/memory/PREHANDOVER-*.md"
  echo "     - .agent-workspace/*/memory/PREHANDOVER-*.md"
  echo "     - .agent-admin/wave-records/amc-wave-record-*.md (90/10 model)"
  echo "   Proceeding with direct gate execution"
  echo ""
  echo "skip_execution=false"
  exit 0
fi

echo "📄 Proof file: $PROOF_FILE"
echo ""

# Search for the check pattern in the proof file
if grep -qiE "$PATTERN" "$PROOF_FILE" 2>/dev/null; then
  echo "✅ Evidence found for: $CHECK_NAME"
  echo "   Pattern '$PATTERN' matched in $PROOF_FILE"
  echo ""
  echo "skip_execution=true"
  exit 0
else
  echo "ℹ️  No evidence found for: $CHECK_NAME"
  echo "   Pattern '$PATTERN' not matched in $PROOF_FILE"
  echo "   Proceeding with direct gate execution"
  echo ""
  echo "skip_execution=false"
  exit 0
fi
