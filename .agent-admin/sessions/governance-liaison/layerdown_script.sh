#!/bin/bash
# Governance Canon Layer-Down Script
# Session: liaison-20260211-125102
# Authority: LIVING_AGENT_SYSTEM v5.0.0 | Self-Alignment Authorized

set -e

SESSION_ID="liaison-20260211-125102"
SESSION_DIR=".agent-admin/sessions/governance-liaison"
ALIGNMENT_LOG="$SESSION_DIR/${SESSION_ID}_alignment.log"
CANONICAL_REPO="APGI-cmy/maturion-foreman-governance"
CANONICAL_REF="main"

echo "=========================================="
echo "Governance Canon Layer-Down Execution"
echo "Session: $SESSION_ID"
echo "Canonical Source: $CANONICAL_REPO"
echo "=========================================="
echo ""

# Initialize alignment log
echo "ALIGNMENT START: $(date -Iseconds)" > "$ALIGNMENT_LOG"
echo "Source: $CANONICAL_REPO (ref: $CANONICAL_REF)" >> "$ALIGNMENT_LOG"
echo "" >> "$ALIGNMENT_LOG"

# Counter for tracking
LAYERED_DOWN=0
SKIPPED=0
FAILED=0

# Read the list of PUBLIC_API files
while IFS= read -r file_path; do
    echo "Processing: $file_path"
    
    # Create directory structure
    dir_path=$(dirname "$file_path")
    mkdir -p "$dir_path"
    
    # Fetch file using GitHub raw content URL
    file_url="https://raw.githubusercontent.com/$CANONICAL_REPO/$CANONICAL_REF/$file_path"
    
    if curl -sf "$file_url" -o "$file_path.new" 2>/dev/null; then
        if [ -s "$file_path.new" ]; then
            mv "$file_path.new" "$file_path"
            SHA256=$(sha256sum "$file_path" | cut -d' ' -f1)
            echo "$(date -Iseconds): $file_path layered down (SHA256: $SHA256)" >> "$ALIGNMENT_LOG"
            echo "  ✅ Layered down: $file_path (SHA256: ${SHA256:0:12}...)"
            ((LAYERED_DOWN++))
        else
            rm -f "$file_path.new"
            echo "  ⚠️  Skipped: $file_path (empty or not found)"
            echo "$(date -Iseconds): $file_path SKIPPED (empty)" >> "$ALIGNMENT_LOG"
            ((SKIPPED++))
        fi
    else
        rm -f "$file_path.new"
        echo "  ❌ Failed: $file_path"
        echo "$(date -Iseconds): $file_path FAILED (curl error)" >> "$ALIGNMENT_LOG"
        ((FAILED++))
    fi
    
    # Small delay to avoid rate limiting
    sleep 0.1
done < /tmp/public_api_files_to_layer_down.txt

echo ""
echo "=========================================="
echo "Layer-Down Summary"
echo "=========================================="
echo "Layered down: $LAYERED_DOWN files"
echo "Skipped: $SKIPPED files"
echo "Failed: $FAILED files"
echo ""
echo "ALIGNMENT COMPLETE: $(date -Iseconds)" >> "$ALIGNMENT_LOG"
echo "Status: SUCCESS (Layered down: $LAYERED_DOWN, Skipped: $SKIPPED, Failed: $FAILED)" >> "$ALIGNMENT_LOG"
echo "✅ Alignment log: $ALIGNMENT_LOG"
