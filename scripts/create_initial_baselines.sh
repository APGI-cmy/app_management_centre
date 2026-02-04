#!/bin/bash
#
# Create Initial Agent File Baselines
#
# Purpose: Copy current agent contract files to baselines directory as CS2-approved starting point
# Authority: CS2 Directive (2026-02-04), CS2_AGENT_FILE_AUTHORITY_MODEL.md
# Usage: ./scripts/create_initial_baselines.sh
#
# This script should be run ONCE by CS2 to establish initial baselines.
# After this, all agent file changes require CS2 review and baseline update.

# Note: Using set -e with explicit error handling
# We disable it temporarily for some checks, then re-enable
set -e

echo "========================================"
echo "Agent File Baseline Creation"
echo "========================================"
echo ""
echo "Purpose: Create CS2-approved baselines from current agent files"
echo "Authority: CS2_AGENT_FILE_AUTHORITY_MODEL.md"
echo ""

# Ensure we're in repository root
if [ ! -d ".github/agents" ]; then
    echo "❌ ERROR: .github/agents directory not found"
    echo "   Please run this script from repository root"
    exit 1
fi

# Create baselines directory if it doesn't exist
BASELINE_DIR="governance/baselines/agent-files"
mkdir -p "$BASELINE_DIR"
echo "✅ Baseline directory: $BASELINE_DIR"
echo ""

# Track what we create
CREATED_COUNT=0
SKIPPED_COUNT=0
ERROR_COUNT=0

echo "Processing agent contract files..."
echo ""

# Process each agent file
# Disable set -e temporarily for the loop to handle errors gracefully
set +e
for file in .github/agents/*.md; do
    # Check if file exists (in case glob doesn't match anything)
    if [ ! -f "$file" ]; then
        echo "  ⚠️  Warning: No .md files found in .github/agents/"
        ERROR_COUNT=$((ERROR_COUNT + 1))
        break
    fi
    
    filename=$(basename "$file")
    
    # Skip SCHEMA files and README
    if [[ "$filename" == *"SCHEMA"* ]] || [[ "$filename" == "README.md" ]]; then
        echo "  ⏭️  Skipping: $filename (excluded)"
        SKIPPED_COUNT=$((SKIPPED_COUNT + 1))
        continue
    fi
    
    # Copy to baseline directory
    if cp "$file" "$BASELINE_DIR/$filename"; then
        echo "  ✅ Created baseline: $filename"
        CREATED_COUNT=$((CREATED_COUNT + 1))
    else
        echo "  ❌ Failed to create: $filename"
        ERROR_COUNT=$((ERROR_COUNT + 1))
    fi
done
set -e  # Re-enable set -e

echo ""
echo "========================================"
echo "Baseline Creation Summary"
echo "========================================"
echo ""
echo "✅ Created:  $CREATED_COUNT baseline(s)"
echo "⏭️  Skipped:  $SKIPPED_COUNT file(s) (excluded)"
echo "❌ Errors:   $ERROR_COUNT"
echo ""

if [ $CREATED_COUNT -gt 0 ]; then
    echo "Next Steps:"
    echo ""
    echo "1. Review created baselines:"
    echo "   ls -la $BASELINE_DIR/"
    echo ""
    echo "2. Commit baselines to repository:"
    echo "   git add $BASELINE_DIR/"
    echo "   git commit -m 'CS2: Establish initial agent file baselines (CS2 Directive 2026-02-04)'"
    echo "   git push"
    echo ""
    echo "3. After commit, Agent File Baseline Gate will enforce these baselines"
    echo ""
    echo "⚠️  IMPORTANT: Only CS2 should update baselines going forward"
    echo ""
fi

if [ $ERROR_COUNT -gt 0 ]; then
    echo "⚠️  Warning: $ERROR_COUNT error(s) occurred during baseline creation"
    echo "   Review output above for details"
    exit 1
fi

echo "✅ Baseline creation completed successfully"
exit 0
