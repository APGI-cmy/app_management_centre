#!/bin/bash
# validate-scope-to-diff.sh
# Validates that all files changed in the PR diff are within the declared scope of the agent contract.
# Required by merge-gate-interface.yml
# Usage: validate-scope-to-diff.sh <agent_id> <base_sha> <head_sha>
# Exit 0 = PASS, Exit 1 = FAIL (files outside declared scope)

set -euo pipefail

AGENT_ID="${1:-}"
BASE_SHA="${2:-HEAD~1}"
HEAD_SHA="${3:-HEAD}"
REPO_ROOT="$(git rev-parse --show-toplevel)"
AGENTS_DIR="$REPO_ROOT/.github/agents"
AGENT_CONTRACT=""

if [[ -z "$AGENT_ID" ]]; then
  echo "Usage: $0 <agent_id> [base_sha] [head_sha]"
  exit 1
fi

# Locate agent contract file
for f in "$AGENTS_DIR"/*.md "$AGENTS_DIR"/*.agent.md; do
  [[ -f "$f" ]] || continue
  if grep -q "^id: ${AGENT_ID}$" "$f" 2>/dev/null || grep -q "^  id: ${AGENT_ID}$" "$f" 2>/dev/null; then
    AGENT_CONTRACT="$f"
    break
  fi
done

if [[ -z "$AGENT_CONTRACT" ]]; then
  echo "⚠️  Agent contract not found for ID: $AGENT_ID — skipping scope-to-diff validation"
  exit 0
fi

echo "📋 Validating scope-to-diff for agent: $AGENT_ID"
echo "   Contract: $AGENT_CONTRACT"
echo "   Diff: $BASE_SHA..$HEAD_SHA"

# Get changed files
CHANGED_FILES="$(git diff --name-only "$BASE_SHA" "$HEAD_SHA" 2>/dev/null || true)"

if [[ -z "$CHANGED_FILES" ]]; then
  echo "✅ No changed files detected — scope-to-diff check passes vacuously"
  exit 0
fi

# Extract declared write_paths from agent contract (lines after write_paths: until next top-level key or blank)
WRITE_PATHS="$(awk '/write_paths:/{found=1; next} found && /^ *- /{gsub(/^ *- *"?/, ""); gsub(/"$/, ""); print} found && !/^ /{found=0}' "$AGENT_CONTRACT" 2>/dev/null || true)"

if [[ -z "$WRITE_PATHS" ]]; then
  echo "⚠️  No write_paths declared in agent contract — scope-to-diff validation skipped (permissive)"
  exit 0
fi

VIOLATIONS=()
while IFS= read -r FILE; do
  [[ -z "$FILE" ]] && continue
  MATCHED=false
  while IFS= read -r ALLOWED_PATH; do
    [[ -z "$ALLOWED_PATH" ]] && continue
    # Strip trailing ** glob for prefix match
    ALLOWED_PREFIX="${ALLOWED_PATH%%\*\*}"
    if [[ "$FILE" == "$ALLOWED_PREFIX"* ]] || [[ "$FILE" == "$ALLOWED_PATH" ]]; then
      MATCHED=true
      break
    fi
  done <<< "$WRITE_PATHS"
  if [[ "$MATCHED" == "false" ]]; then
    VIOLATIONS+=("$FILE")
  fi
done <<< "$CHANGED_FILES"

if [[ ${#VIOLATIONS[@]} -gt 0 ]]; then
  echo "❌ SCOPE VIOLATION — files changed outside declared write_paths:"
  for V in "${VIOLATIONS[@]}"; do
    echo "   - $V"
  done
  echo ""
  echo "Declared write_paths:"
  while IFS= read -r P; do echo "   - $P"; done <<< "$WRITE_PATHS"
  exit 1
fi

echo "✅ Scope-to-diff validation PASSED — all ${#CHANGED_FILES[@]} changed files within declared scope"
exit 0
