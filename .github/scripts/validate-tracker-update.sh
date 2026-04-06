#!/bin/bash
# validate-tracker-update.sh
# Validates that a tracker update (e.g. GOVERNANCE_ALIGNMENT_INVENTORY.json or session memory)
# has been committed as part of the PR changes. Required by merge-gate-interface.yml.
# Usage: validate-tracker-update.sh <base_sha> <head_sha>
# Exit 0 = PASS, Exit 1 = FAIL

set -euo pipefail

BASE_SHA="${1:-HEAD~1}"
HEAD_SHA="${2:-HEAD}"
REPO_ROOT="$(git rev-parse --show-toplevel)"

echo "📋 Validating tracker update: $BASE_SHA..$HEAD_SHA"

# Get changed files
CHANGED_FILES="$(git diff --name-only "$BASE_SHA" "$HEAD_SHA" 2>/dev/null || true)"

if [[ -z "$CHANGED_FILES" ]]; then
  echo "⚠️  No changed files detected — tracker validation skipped"
  exit 0
fi

# Tracker patterns that satisfy the requirement
TRACKER_PATTERNS=(
  "GOVERNANCE_ALIGNMENT_INVENTORY.json"
  ".agent-workspace/.*/memory/session-"
  ".agent-workspace/.*/knowledge/"
  ".agent-admin/completion-reports/"
  ".agent-admin/sessions/"
  ".agent-admin/assurance/iaa-token-"
  ".agent-admin/governance/layerdown-alignment-state.json"
  ".agent-admin/governance/sync-state.json"
)

FOUND_TRACKER=false
MATCHED_TRACKER=""

while IFS= read -r FILE; do
  [[ -z "$FILE" ]] && continue
  for PATTERN in "${TRACKER_PATTERNS[@]}"; do
    if echo "$FILE" | grep -qE "$PATTERN"; then
      FOUND_TRACKER=true
      MATCHED_TRACKER="$FILE (matches: $PATTERN)"
      break 2
    fi
  done
done <<< "$CHANGED_FILES"

if [[ "$FOUND_TRACKER" == "true" ]]; then
  echo "✅ Tracker update found: $MATCHED_TRACKER"
  exit 0
fi

echo "❌ TRACKER VALIDATION FAILED — no session memory, alignment inventory, or evidence tracker update found in diff"
echo ""
echo "Required: at least one of the following must be updated:"
for P in "${TRACKER_PATTERNS[@]}"; do
  echo "   - $P"
done
echo ""
echo "Changed files in diff:"
while IFS= read -r FILE; do echo "   - $FILE"; done <<< "$CHANGED_FILES"
exit 1
