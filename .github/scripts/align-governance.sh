#!/bin/bash
# Governance Alignment Script
# Authority: CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md
# Living Agent System: v6.2.0
#
# Purpose: Layer down canonical governance artifacts from maturion-foreman-governance
# Usage: ./align-governance.sh [--dry-run] [--verbose]
#
# This script:
# 1. Fetches canonical CANON_INVENTORY.json
# 2. Identifies PUBLIC_API artifacts
# 3. Downloads each artifact
# 4. Updates local sync state
# 5. Reports alignment status

set -e

# Configuration
CANONICAL_REPO="APGI-cmy/maturion-foreman-governance"
CANONICAL_REF="main"
BASE_URL="https://raw.githubusercontent.com"
CANONICAL_BASE_URL="$BASE_URL/$CANONICAL_REPO/$CANONICAL_REF"
INVENTORY_PATH="governance/CANON_INVENTORY.json"
SYNC_STATE_PATH=".agent-admin/governance/sync_state.json"

# Parse arguments
DRY_RUN=false
VERBOSE=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --verbose)
            VERBOSE=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [--dry-run] [--verbose]"
            exit 1
            ;;
    esac
done

# Logging functions
log_info() {
    echo "[INFO] $*"
}

log_verbose() {
    if [ "$VERBOSE" = true ]; then
        echo "[VERBOSE] $*"
    fi
}

log_error() {
    echo "[ERROR] $*" >&2
}

log_success() {
    echo "[SUCCESS] $*"
}

# Main execution
main() {
    log_info "Starting governance alignment..."
    log_info "Canonical source: $CANONICAL_REPO @ $CANONICAL_REF"
    
    if [ "$DRY_RUN" = true ]; then
        log_info "DRY RUN MODE - No files will be modified"
    fi
    
    # Ensure directories exist
    mkdir -p .agent-admin/governance
    mkdir -p .agent-admin/ripple
    mkdir -p governance
    
    # Step 1: Fetch canonical inventory
    log_info "Fetching canonical CANON_INVENTORY.json..."
    TEMP_INVENTORY="/tmp/canonical_inventory.json"
    
    if ! curl -f -s "$CANONICAL_BASE_URL/$INVENTORY_PATH" -o "$TEMP_INVENTORY"; then
        log_error "Failed to fetch canonical inventory"
        exit 1
    fi
    
    # Extract version and commit info
    CANONICAL_VERSION=$(jq -r '.version // "unknown"' "$TEMP_INVENTORY")
    CANONICAL_COMMIT=$(jq -r '.provenance.commit_sha // "unknown"' "$TEMP_INVENTORY")
    
    log_info "Canonical version: $CANONICAL_VERSION"
    log_info "Canonical commit: $CANONICAL_COMMIT"
    
    # Check local version
    if [ -f "$INVENTORY_PATH" ]; then
        LOCAL_VERSION=$(jq -r '.version // "unknown"' "$INVENTORY_PATH")
        LOCAL_COMMIT=$(jq -r '.provenance.commit_sha // "unknown"' "$INVENTORY_PATH")
        log_info "Local version: $LOCAL_VERSION"
        log_info "Local commit: $LOCAL_COMMIT"
        
        if [ "$CANONICAL_VERSION" = "$LOCAL_VERSION" ] && \
           [ "$CANONICAL_COMMIT" = "$LOCAL_COMMIT" ]; then
            log_success "Already aligned - no action needed"
            update_sync_state "false" "false"
            exit 0
        fi
    else
        log_info "No local inventory found - first-time alignment"
    fi
    
    # Step 2: Extract PUBLIC_API artifacts
    log_info "Identifying PUBLIC_API artifacts to layer down..."
    JQ_FILTER='.artifacts[] | select(.layer_down_status == "PUBLIC_API") | .path'
    PUBLIC_API_FILES=$(jq -r "$JQ_FILTER" "$TEMP_INVENTORY")
    
    if [ -z "$PUBLIC_API_FILES" ]; then
        log_error "No PUBLIC_API artifacts found in canonical inventory"
        exit 1
    fi
    
    FILE_COUNT=$(echo "$PUBLIC_API_FILES" | wc -l)
    log_info "Found $FILE_COUNT PUBLIC_API artifacts to layer down"
    
    # Step 3: Layer down artifacts
    DOWNLOADED=0
    FAILED=0
    
    echo "$PUBLIC_API_FILES" | while read -r file; do
        [ -z "$file" ] && continue
        
        log_verbose "Processing: $file"
        
        if [ "$DRY_RUN" = true ]; then
            log_verbose "  [DRY RUN] Would download: $file"
            continue
        fi
        
        # Ensure parent directory exists
        mkdir -p "$(dirname "$file")"
        
        # Download file
        if curl -f -s "$CANONICAL_BASE_URL/$file" -o "$file"; then
            log_verbose "  ✅ Downloaded: $file"
            DOWNLOADED=$((DOWNLOADED + 1))
        else
            log_error "  ❌ Failed: $file (may not exist in canonical repo)"
            FAILED=$((FAILED + 1))
        fi
    done
    
    # Step 4: Update local inventory
    if [ "$DRY_RUN" = false ]; then
        log_info "Updating local CANON_INVENTORY.json..."
        cp "$TEMP_INVENTORY" "$INVENTORY_PATH"
    fi
    
    # Step 5: Update sync state
    log_info "Updating sync state..."
    update_sync_state "true" "true"
    
    # Summary
    log_success "Governance alignment complete"
    log_info "Canonical version: $CANONICAL_VERSION"
    log_info "Canonical commit: $CANONICAL_COMMIT"
    
    if [ "$DRY_RUN" = false ]; then
        log_info "Files processed: $FILE_COUNT"
        log_success "✅ Alignment successful"
    else
        log_info "[DRY RUN] Would have processed $FILE_COUNT files"
    fi
}

# Update sync state JSON
update_sync_state() {
    local drift_detected=$1
    local needs_alignment=$2
    
    if [ "$DRY_RUN" = true ]; then
        log_verbose "  [DRY RUN] Would update sync_state.json"
        return
    fi
    
    # Get versions
    if [ -f "$INVENTORY_PATH" ]; then
        LOCAL_VERSION=$(jq -r '.version // "unknown"' "$INVENTORY_PATH")
        LOCAL_COMMIT=$(jq -r '.provenance.commit_sha // "unknown"' "$INVENTORY_PATH")
    else
        LOCAL_VERSION="none"
        LOCAL_COMMIT="none"
    fi
    
    CANONICAL_VERSION=$(jq -r '.version // "unknown"' "$TEMP_INVENTORY")
    CANONICAL_COMMIT=$(jq -r '.provenance.commit_sha // "unknown"' "$TEMP_INVENTORY")
    
    cat > "$SYNC_STATE_PATH" <<EOF
{
  "last_check": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "canonical_version": "$CANONICAL_VERSION",
  "canonical_commit": "$CANONICAL_COMMIT",
  "local_version": "$LOCAL_VERSION",
  "local_commit": "$LOCAL_COMMIT",
  "drift_detected": "$drift_detected",
  "needs_alignment": "$needs_alignment",
  "alignment_method": "align-governance.sh"
}
EOF
    
    log_verbose "Sync state updated"
}

# Run main
main "$@"
