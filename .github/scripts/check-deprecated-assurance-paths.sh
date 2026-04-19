#!/bin/bash
# check-deprecated-assurance-paths.sh
# Non-regression check: surfaces deprecated standalone assurance-path references
# in active governance instructions (contracts, templates, checklists, knowledge files).
# Authority: AMC 90/10 Admin Protocol v1.0.0 — wave-record-only assurance model.
# Usage: bash .github/scripts/check-deprecated-assurance-paths.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
FAILS=()

# Deprecated standalone path patterns to detect in active instructions
DEPRECATED_PATTERNS=(
  'iaa-prebrief-wave[0-9\<]'
  'iaa-prebrief-wave<N>'
  '\.agent-admin/assurance/iaa-prebrief-'
  '\.agent-admin/assurance/iaa-token-'
  'iaa-token-session-.*\.md.*active'
  'write.*iaa-prebrief.*\.md.*commit'
  'stored_at.*iaa-prebrief-wave'
)

# Active instruction paths to scan (excludes historical memory/archive/assurance artifacts)
SCAN_PATHS=(
  ".github/agents"
  ".agent-workspace/foreman-v2/knowledge"
  ".agent-workspace/independent-assurance-agent/knowledge"
  ".agent-workspace/execution-ceremony-admin-agent/knowledge"
  "governance/checklists"
  "governance/templates"
  "governance/canon"
  ".agent-admin/templates"
)

echo "=== Deprecated Assurance Path Check ==="
echo "Scanning active instruction paths for deprecated standalone assurance-path references..."
echo ""

for scan_path in "${SCAN_PATHS[@]}"; do
  full_path="$REPO_ROOT/$scan_path"
  [ -d "$full_path" ] || continue
  for pattern in "${DEPRECATED_PATTERNS[@]}"; do
    matches=$(grep -rl --include="*.md" --include="*.yml" --include="*.sh" "$pattern" "$full_path" 2>/dev/null || true)
    if [ -n "$matches" ]; then
      while IFS= read -r match_file; do
        rel_path="${match_file#$REPO_ROOT/}"
        # Skip historical archive and memory files
        [[ "$rel_path" == .agent-workspace/*/memory/* ]] && continue
        [[ "$rel_path" == .agent-admin/assurance/* ]] && continue
        [[ "$rel_path" == .agent-admin/archive/* ]] && continue
        FAILS+=("DEPRECATED PATH: pattern='$pattern' found in: $rel_path")
      done <<< "$matches"
    fi
  done
done

if [ ${#FAILS[@]} -gt 0 ]; then
  echo "❌ DEPRECATED ASSURANCE PATH CHECK FAILED"
  echo "   Standalone assurance-path references detected in active instructions."
  echo "   These must be normalized to the wave-record-only model before merge."
  echo ""
  for f in "${FAILS[@]}"; do
    echo "  - $f"
  done
  exit 1
fi

echo "✅ DEPRECATED ASSURANCE PATH CHECK PASSED"
echo "   No deprecated standalone assurance-path references in active instructions."
exit 0
