#!/bin/bash
# update-governance-alignment-inventory.sh
# Authority: CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md, GOVERNANCE_ALIGNMENT_MONITORING_PROTOCOL.md
# Purpose: Automatically update governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json
#          after a governance layer-down to reflect new artifact versions and hashes.
#
# Usage: ./update-governance-alignment-inventory.sh [--canonical-commit <SHA>] [--dry-run]
#
# This script:
# 1. Reads governance/CANON_INVENTORY.json (the layered-down canonical inventory)
# 2. Reads the current GOVERNANCE_ALIGNMENT_INVENTORY.json
# 3. For each artifact present in CANON_INVENTORY and present locally:
#    - Computes SHA256 hash of the local file
#    - Updates the inventory entry (version, hash, layered_down_at, canonical_commit)
# 4. Writes the updated GOVERNANCE_ALIGNMENT_INVENTORY.json
# 5. Prints a diff summary

set -e

ALIGNMENT_INVENTORY="governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json"
CANON_INVENTORY="governance/CANON_INVENTORY.json"

# Parse arguments
CANONICAL_COMMIT=""
DRY_RUN=false
while [[ $# -gt 0 ]]; do
  case $1 in
    --canonical-commit) CANONICAL_COMMIT="$2"; shift 2 ;;
    --dry-run) DRY_RUN=true; shift ;;
    *) echo "[WARN] Unknown option: $1"; shift ;;
  esac
done

echo "[INFO] Governance Alignment Inventory Update"
echo "[INFO] Alignment inventory: $ALIGNMENT_INVENTORY"
echo "[INFO] Canon inventory: $CANON_INVENTORY"
[ "$DRY_RUN" = true ] && echo "[INFO] DRY RUN MODE — no files will be modified"

# Validate prerequisites
if ! command -v jq >/dev/null 2>&1; then
  echo "[ERROR] jq is required but not installed."
  exit 1
fi

if [ ! -f "$ALIGNMENT_INVENTORY" ]; then
  echo "[ERROR] GOVERNANCE_ALIGNMENT_INVENTORY.json not found at $ALIGNMENT_INVENTORY"
  exit 1
fi

if [ ! -f "$CANON_INVENTORY" ]; then
  echo "[WARN] CANON_INVENTORY.json not found at $CANON_INVENTORY — skipping version cross-reference"
fi

# Determine canonical commit (use from CANON_INVENTORY if not provided)
if [ -z "$CANONICAL_COMMIT" ] && [ -f "$CANON_INVENTORY" ]; then
  CANONICAL_COMMIT=$(jq -r '.provenance.commit_sha // "unknown"' "$CANON_INVENTORY" 2>/dev/null || echo "unknown")
fi
CANONICAL_COMMIT="${CANONICAL_COMMIT:-unknown}"

TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)

echo "[INFO] Canonical commit: $CANONICAL_COMMIT"
echo "[INFO] Update timestamp: $TIMESTAMP"

# Read current inventory
CURRENT_INVENTORY=$(cat "$ALIGNMENT_INVENTORY")

# Build a lookup of canonical artifact paths → versions/hashes from CANON_INVENTORY
CANON_LOOKUP="{}"
if [ -f "$CANON_INVENTORY" ]; then
  CANON_LOOKUP=$(jq -r '
    .artifacts // [] |
    map({
      key: .path,
      value: {
        version: (.version // "unknown"),
        layer_down_status: (.layer_down_status // "INTERNAL"),
        canonical_commit: (.provenance_commit // "unknown")
      }
    }) |
    from_entries
  ' "$CANON_INVENTORY" 2>/dev/null || echo "{}")
fi

# Process each artifact in the alignment inventory
UPDATED=0
SKIPPED=0
FAILED=0
RESULT=$(echo "$CURRENT_INVENTORY")

# Get artifact count
ARTIFACT_COUNT=$(echo "$CURRENT_INVENTORY" | jq '.artifacts | length' 2>/dev/null || echo 0)
echo "[INFO] Processing $ARTIFACT_COUNT artifact entries..."

for i in $(seq 0 $((ARTIFACT_COUNT - 1))); do
  ARTIFACT_PATH=$(echo "$CURRENT_INVENTORY" | jq -r ".artifacts[$i].path // \"\"")
  [ -z "$ARTIFACT_PATH" ] && continue

  if [ ! -f "$ARTIFACT_PATH" ]; then
    echo "  [SKIP] $ARTIFACT_PATH — file not present locally"
    SKIPPED=$((SKIPPED + 1))
    continue
  fi

  # Compute actual SHA256 of local file
  ACTUAL_HASH=$(sha256sum "$ARTIFACT_PATH" 2>/dev/null | awk '{print $1}' || echo "")
  if [ -z "$ACTUAL_HASH" ]; then
    echo "  [FAIL] $ARTIFACT_PATH — could not compute hash"
    FAILED=$((FAILED + 1))
    continue
  fi

  # Get version from file header (pattern: **Version**: X.Y.Z or Version: X.Y.Z)
  # Use explicit sequential checks to avoid pipeline exit-code semantics with ||
  FILE_VERSION=""
  if [ -z "$FILE_VERSION" ]; then
    _v=$(grep -m1 -oE "\*\*Version\*\*: [0-9]+\.[0-9]+\.[0-9]+" "$ARTIFACT_PATH" 2>/dev/null)
    FILE_VERSION="${_v#\*\*Version\*\*: }"
  fi
  if [ -z "$FILE_VERSION" ]; then
    _v=$(grep -m1 -oE "^Version: [0-9]+\.[0-9]+\.[0-9]+" "$ARTIFACT_PATH" 2>/dev/null)
    FILE_VERSION="${_v#Version: }"
  fi
  if [ -z "$FILE_VERSION" ]; then
    FILE_VERSION=$(grep -m1 -oE "Status.*Version: [0-9]+\.[0-9]+\.[0-9]+" "$ARTIFACT_PATH" 2>/dev/null | \
      grep -oE "[0-9]+\.[0-9]+\.[0-9]+")
  fi
  
  # Get current stored values
  STORED_HASH=$(echo "$CURRENT_INVENTORY" | jq -r ".artifacts[$i].file_hash_sha256 // \"\"")
  STORED_VERSION=$(echo "$CURRENT_INVENTORY" | jq -r ".artifacts[$i].version // \"\"")

  # Check if update is needed
  if [ "$ACTUAL_HASH" = "$STORED_HASH" ] && \
     [ -z "$FILE_VERSION" -o "$FILE_VERSION" = "$STORED_VERSION" ]; then
    echo "  [OK]   $ARTIFACT_PATH — hash/version unchanged"
    SKIPPED=$((SKIPPED + 1))
    continue
  fi

  # Build update object
  NEW_VERSION="${FILE_VERSION:-$STORED_VERSION}"
  UPDATE_REASON=""
  [ "$ACTUAL_HASH" != "$STORED_HASH" ] && UPDATE_REASON="${UPDATE_REASON}hash-changed "
  [ -n "$FILE_VERSION" ] && [ "$FILE_VERSION" != "$STORED_VERSION" ] && UPDATE_REASON="${UPDATE_REASON}version-changed "

  echo "  [UPDATE] $ARTIFACT_PATH — $UPDATE_REASON"
  if [ -n "$NEW_VERSION" ]; then
    echo "    version: $STORED_VERSION → $NEW_VERSION"
  fi

  if [ "$DRY_RUN" = false ]; then
    RESULT=$(echo "$RESULT" | jq \
      --arg idx "$i" \
      --arg hash "$ACTUAL_HASH" \
      --arg version "$NEW_VERSION" \
      --arg commit "$CANONICAL_COMMIT" \
      --arg ts "$TIMESTAMP" \
      --arg action "UPDATED" \
      '
      .artifacts[($idx | tonumber)] |= . +
        (if ($version != "") then {version: $version} else {} end) +
        {
          file_hash_sha256: $hash,
          canonical_commit: $commit,
          layered_down_at: $ts,
          action: $action
        }
      ')
  fi

  UPDATED=$((UPDATED + 1))
done

# Update top-level metadata
if [ "$DRY_RUN" = false ] && [ "$UPDATED" -gt 0 ]; then
  RESULT=$(echo "$RESULT" | jq \
    --arg commit "$CANONICAL_COMMIT" \
    --arg ts "$TIMESTAMP" \
    --arg status "ALIGNED" \
    '
    .last_layer_down_commit = $commit |
    .last_updated = $ts |
    .alignment_status = $status
    ')
fi

echo ""
echo "[INFO] Update summary:"
echo "  Updated : $UPDATED artifacts"
echo "  Skipped : $SKIPPED artifacts (unchanged or not present)"
echo "  Failed  : $FAILED artifacts"

if [ "$UPDATED" -gt 0 ]; then
  if [ "$DRY_RUN" = false ]; then
    echo "$RESULT" | jq . > "$ALIGNMENT_INVENTORY"
    echo "[SUCCESS] GOVERNANCE_ALIGNMENT_INVENTORY.json updated ($UPDATED changes)"
  else
    echo "[DRY RUN] Would have written $UPDATED updates to $ALIGNMENT_INVENTORY"
  fi
else
  echo "[INFO] No updates required — inventory is already current"
fi
