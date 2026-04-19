#!/bin/bash
# check-deprecated-assurance-paths.sh
# Non-regression check: surfaces ACTIVE deprecated standalone assurance-path references
# in active governance instructions (contracts, templates, checklists, knowledge files).
# Authority: AMC 90/10 Admin Protocol v1.0.0 — wave-record-only assurance model.
# Usage: bash .github/scripts/check-deprecated-assurance-paths.sh
#
# WHAT IS FLAGGED: lines that indicate an active instruction to CREATE or USE a standalone
# iaa-prebrief-*.md or iaa-token-*.md file (as a destination path, write target, or live storage).
#
# WHAT IS NOT FLAGGED:
#  - Deprecation notices (lines containing "deprecated", "DEPRECATED", "NEVER", "NOT", "MUST NOT")
#  - Historical canon documentation in governance/canon/ (requires separate canon-change wave)
#  - Memory files (.agent-workspace/*/memory/)
#  - Archive / assurance artifact directories (.agent-admin/assurance/, .agent-admin/archive/)
#  - FAIL-ONLY-ONCE.md files (operational knowledge explaining OLD patterns for recognition)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
FAILS=()

echo "=== Deprecated Assurance Path Check ==="
echo "Scanning active instruction paths for ACTIVE use of deprecated standalone assurance-path references..."
echo ""

# Active instruction paths to scan (excludes historical canon docs)
SCAN_PATHS=(
  ".github/agents"
  ".agent-workspace/foreman-v2/knowledge"
  ".agent-workspace/independent-assurance-agent/knowledge"
  ".agent-workspace/execution-ceremony-admin-agent/knowledge"
  "governance/checklists"
  "governance/templates"
  ".agent-admin/templates"
)

# Patterns that indicate ACTIVE use of the deprecated standalone paths
# (not mere mentions or deprecation notices)
ACTIVE_USE_PATTERNS=(
  'stored_at:.*iaa-prebrief-wave'
  'token_file_pattern:.*iaa-token-'
  'write.*iaa-prebrief.*\.md.*commit'
  'Token file path:.*iaa-token-'
  'MUST be written to.*iaa-token-'
)

for scan_path in "${SCAN_PATHS[@]}"; do
  full_path="$REPO_ROOT/$scan_path"
  [ -d "$full_path" ] || continue

  for pattern in "${ACTIVE_USE_PATTERNS[@]}"; do
    while IFS= read -r match_file; do
      [ -f "$match_file" ] || continue
      rel_path="${match_file#$REPO_ROOT/}"

      # Skip known exclusion categories
      [[ "$rel_path" == *.agent-workspace/*/memory/* ]] && continue
      [[ "$rel_path" == .agent-admin/assurance/* ]] && continue
      [[ "$rel_path" == .agent-admin/archive/* ]] && continue
      [[ "$(basename "$rel_path")" == "FAIL-ONLY-ONCE.md" ]] && continue

      # Check if the match line is a deprecation/prohibition notice (not an active instruction)
      matching_lines=$(grep -in "$pattern" "$match_file" 2>/dev/null || true)
      while IFS= read -r line; do
        # Skip lines that are deprecation/prohibition notices
        if echo "$line" | grep -qiE "deprecated|DEPRECATED|NEVER|MUST NOT|no longer|CI-blocked|DO NOT|not accepted"; then
          continue
        fi
        FAILS+=("ACTIVE DEPRECATED PATH: pattern='$pattern' line='$(echo "$line" | tr -d '\r' | cut -c1-100)' file=$rel_path")
      done <<< "$matching_lines"
    done < <(grep -rl --include="*.md" --include="*.yml" --include="*.sh" "$pattern" "$full_path" 2>/dev/null || true)
  done
done

if [ ${#FAILS[@]} -gt 0 ]; then
  echo "❌ DEPRECATED ASSURANCE PATH CHECK FAILED"
  echo "   ACTIVE instructions using deprecated standalone assurance-path model detected."
  echo "   Normalize to wave-record-only model (pre-brief in section 2, token in section 5)."
  echo ""
  for f in "${FAILS[@]}"; do
    echo "  - $f"
  done
  exit 1
fi

echo "✅ DEPRECATED ASSURANCE PATH CHECK PASSED"
echo "   No active instructions using deprecated standalone assurance-path model."
exit 0
