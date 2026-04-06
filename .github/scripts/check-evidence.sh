#!/bin/bash
# check-evidence.sh
# Checks that required evidence artifacts exist for the current PR/session.
# Inspects .agent-admin/ for prehandover proof, session memory, and IAA token.
# Usage: check-evidence.sh [session_id]
# Exit 0 = PASS (all required evidence present), Exit 1 = FAIL (evidence missing)

set -euo pipefail

SESSION_ID="${1:-}"
REPO_ROOT="$(git rev-parse --show-toplevel)"
ASSURANCE_DIR="$REPO_ROOT/.agent-admin/assurance"
SESSIONS_DIR="$REPO_ROOT/.agent-admin/sessions"
PREHANDOVER_DIR="$REPO_ROOT/.agent-admin/prehandover"
MISSING=()
FOUND=()

echo "🔍 Checking evidence artifacts..."
[[ -n "$SESSION_ID" ]] && echo "   Session: $SESSION_ID"

check_dir_has_files() {
  local DIR="$1"
  local LABEL="$2"
  local PATTERN="${3:-*}"
  if [[ -d "$DIR" ]] && compgen -G "$DIR"/$PATTERN > /dev/null 2>&1; then
    local COUNT
    COUNT="$(find "$DIR" -maxdepth 2 -name "$PATTERN" -type f | wc -l)"
    FOUND+=("$LABEL ($COUNT files in $DIR)")
    return 0
  else
    return 1
  fi
}

# 1. Check for session memory
if [[ -n "$SESSION_ID" ]]; then
  SESSION_MEMORY="$(find "$SESSIONS_DIR" -name "*${SESSION_ID}*" -type f 2>/dev/null | head -1 || true)"
  if [[ -z "$SESSION_MEMORY" ]]; then
    SESSION_MEMORY="$(find "$REPO_ROOT/.agent-workspace" -name "session-*" -type f 2>/dev/null | tail -1 || true)"
  fi
  if [[ -n "$SESSION_MEMORY" ]]; then
    FOUND+=("Session memory: $SESSION_MEMORY")
  else
    MISSING+=("Session memory (pattern: session-*${SESSION_ID}*)")
  fi
else
  # Without session ID, just check that at least one recent session memory exists
  LATEST_MEMORY="$(find "$REPO_ROOT/.agent-workspace" -name "session-*.md" -type f 2>/dev/null | sort | tail -1 || true)"
  if [[ -n "$LATEST_MEMORY" ]]; then
    FOUND+=("Latest session memory: $LATEST_MEMORY")
  else
    MISSING+=("Session memory (no session-*.md found in .agent-workspace)")
  fi
fi

# 2. Check for IAA token (assurance token)
IAA_TOKEN="$(find "$ASSURANCE_DIR" -name "iaa-token-*.md" -type f 2>/dev/null | sort | tail -1 || true)"
if [[ -n "$IAA_TOKEN" ]]; then
  FOUND+=("IAA assurance token: $IAA_TOKEN")
else
  MISSING+=("IAA assurance token (iaa-token-*.md in $ASSURANCE_DIR)")
fi

# 3. Check for prehandover proof
PREHANDOVER="$(find "$PREHANDOVER_DIR" -name "*.md" -type f 2>/dev/null | sort | tail -1 || true)"
if [[ -z "$PREHANDOVER" ]]; then
  PREHANDOVER="$(find "$REPO_ROOT/.agent-admin" -name "PREHANDOVER_PROOF*.md" -type f 2>/dev/null | sort | tail -1 || true)"
fi
if [[ -n "$PREHANDOVER" ]]; then
  FOUND+=("Prehandover proof: $PREHANDOVER")
else
  MISSING+=("Prehandover proof (PREHANDOVER_PROOF*.md in .agent-admin/prehandover/)")
fi

# 4. Check CANON_INVENTORY is present and non-stub
CANON_INVENTORY="$REPO_ROOT/.governance-pack/CANON_INVENTORY.json"
if [[ -f "$CANON_INVENTORY" ]]; then
  SIZE="$(wc -c < "$CANON_INVENTORY")"
  if [[ "$SIZE" -gt 1024 ]]; then
    FOUND+=("CANON_INVENTORY.json (${SIZE} bytes)")
  else
    MISSING+=("CANON_INVENTORY.json is stub/too small (${SIZE} bytes — expected >1KB)")
  fi
else
  MISSING+=("CANON_INVENTORY.json missing from .governance-pack/")
fi

# Report
echo ""
if [[ ${#FOUND[@]} -gt 0 ]]; then
  echo "✅ Evidence found:"
  for F in "${FOUND[@]}"; do echo "   ✓ $F"; done
fi

if [[ ${#MISSING[@]} -gt 0 ]]; then
  echo ""
  echo "❌ Missing evidence artifacts:"
  for M in "${MISSING[@]}"; do echo "   ✗ $M"; done
  echo ""
  echo "Evidence check FAILED — complete all required artifacts before opening PR"
  exit 1
fi

echo ""
echo "✅ Evidence check PASSED — all required artifacts present"
exit 0
