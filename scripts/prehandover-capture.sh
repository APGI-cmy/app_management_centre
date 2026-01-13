#!/bin/bash
#
# Prehandover Evidence Capture Script
#
# Purpose: Automatically capture execution evidence for PREHANDOVER_PROOF
# Authority: Execution Bootstrap Protocol v2.0.0+, Wave 3.2
# Usage: ./scripts/prehandover-capture.sh [OPTIONS]
#
# This script executes and captures evidence for execution artifacts
# (workflows, scripts, gates, validation tools) required for Category 0
# of the Execution Bootstrap Protocol.
#

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
EVIDENCE_DIR="evidence/prehandover"
TIMESTAMP=$(date -u +%Y%m%d_%H%M%S)
CAPTURE_ID="capture_${TIMESTAMP}"
OUTPUT_FILE=""
ARTIFACTS=()
DRY_RUN=false

# Usage function
usage() {
    cat << EOF
Usage: $0 [OPTIONS] -- ARTIFACT_COMMANDS...

Automatically capture execution evidence for PREHANDOVER_PROOF documentation.

OPTIONS:
    -d, --evidence-dir DIR    Evidence output directory (default: evidence/prehandover)
    -o, --output FILE         PREHANDOVER_PROOF output file (default: PREHANDOVER_PROOF_${CAPTURE_ID}.md)
    -n, --dry-run             Show what would be executed without running
    -h, --help                Show this help message

ARTIFACT_COMMANDS:
    Space-separated list of commands to execute and capture evidence for.
    Each command should be quoted if it contains spaces.

EXAMPLES:
    # Capture single artifact
    $0 -- "python3 scripts/validate-builder-environment.py"
    
    # Capture multiple artifacts
    $0 -- "ruff check --select UP ." "pytest tests/" "python3 governance/scripts/validate_prehandover_proof.py PROOF.md"
    
    # Custom output location
    $0 -o PREHANDOVER_PROOF_PR_123.md -- "bash .githooks/pre-push"
    
    # Dry run to see what would execute
    $0 --dry-run -- "command1" "command2"

OUTPUT:
    - Evidence logs saved to: \${EVIDENCE_DIR}/\${CAPTURE_ID}/
    - PREHANDOVER_PROOF markdown generated with captured evidence
    - Exit codes, timestamps, and outputs automatically documented

EOF
    exit 0
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -d|--evidence-dir)
            EVIDENCE_DIR="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_FILE="$2"
            shift 2
            ;;
        -n|--dry-run)
            DRY_RUN=true
            shift
            ;;
        -h|--help)
            usage
            ;;
        --)
            shift
            ARTIFACTS=("$@")
            break
            ;;
        *)
            echo -e "${RED}Error: Unknown option: $1${NC}"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Check if artifacts provided
if [ ${#ARTIFACTS[@]} -eq 0 ]; then
    echo -e "${RED}Error: No artifacts specified${NC}"
    echo "Use --help for usage information"
    exit 1
fi

# Set default output file if not specified
if [ -z "$OUTPUT_FILE" ]; then
    OUTPUT_FILE="PREHANDOVER_PROOF_${CAPTURE_ID}.md"
fi

# Print header
echo ""
echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║         Prehandover Evidence Capture - Wave 3.2           ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}[DRY RUN MODE - No actual execution]${NC}"
    echo ""
fi

echo "Capture ID: $CAPTURE_ID"
echo "Evidence Directory: $EVIDENCE_DIR/$CAPTURE_ID"
echo "Output File: $OUTPUT_FILE"
echo "Artifacts to Execute: ${#ARTIFACTS[@]}"
echo ""

# Create evidence directory
CAPTURE_DIR="$EVIDENCE_DIR/$CAPTURE_ID"
if [ "$DRY_RUN" = false ]; then
    mkdir -p "$CAPTURE_DIR"
    echo -e "${GREEN}✅ Created evidence directory${NC}"
else
    echo -e "${YELLOW}Would create: $CAPTURE_DIR${NC}"
fi

echo ""

# Initialize results array
declare -a RESULTS

# Execute each artifact and capture evidence
for i in "${!ARTIFACTS[@]}"; do
    ARTIFACT="${ARTIFACTS[$i]}"
    ARTIFACT_NUM=$((i + 1))
    ARTIFACT_ID="artifact_$(printf "%03d" $ARTIFACT_NUM)"
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Artifact $ARTIFACT_NUM/${#ARTIFACTS[@]}: $ARTIFACT${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    ARTIFACT_START=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    
    if [ "$DRY_RUN" = true ]; then
        echo -e "${YELLOW}Would execute: $ARTIFACT${NC}"
        echo -e "${YELLOW}Would capture output to: $CAPTURE_DIR/${ARTIFACT_ID}.log${NC}"
        echo ""
        
        # Mock result for dry run
        RESULTS+=("$ARTIFACT|0|$ARTIFACT_START|$ARTIFACT_START|DRY_RUN")
        continue
    fi
    
    # Execute artifact and capture output
    LOG_FILE="$CAPTURE_DIR/${ARTIFACT_ID}.log"
    EXIT_CODE_FILE="$CAPTURE_DIR/${ARTIFACT_ID}.exitcode"
    
    echo "Executing..."
    echo ""
    
    # Run command and capture output
    set +e
    eval "$ARTIFACT" 2>&1 | tee "$LOG_FILE"
    EXIT_CODE=${PIPESTATUS[0]}
    set -e
    
    ARTIFACT_END=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    
    # Save exit code
    echo "$EXIT_CODE" > "$EXIT_CODE_FILE"
    
    # Save metadata
    cat > "$CAPTURE_DIR/${ARTIFACT_ID}.meta" << EOF
{
  "artifact_id": "$ARTIFACT_ID",
  "artifact_number": $ARTIFACT_NUM,
  "command": "$ARTIFACT",
  "start_time": "$ARTIFACT_START",
  "end_time": "$ARTIFACT_END",
  "exit_code": $EXIT_CODE,
  "log_file": "${ARTIFACT_ID}.log",
  "exit_code_file": "${ARTIFACT_ID}.exitcode"
}
EOF
    
    # Store result
    RESULTS+=("$ARTIFACT|$EXIT_CODE|$ARTIFACT_START|$ARTIFACT_END|$LOG_FILE")
    
    echo ""
    if [ $EXIT_CODE -eq 0 ]; then
        echo -e "${GREEN}✅ EXIT CODE: 0 (SUCCESS)${NC}"
    else
        echo -e "${RED}❌ EXIT CODE: $EXIT_CODE (FAILURE)${NC}"
    fi
    echo -e "   Start: $ARTIFACT_START"
    echo -e "   End:   $ARTIFACT_END"
    echo -e "   Log:   $LOG_FILE"
    echo ""
done

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Generate summary
SUCCESS_COUNT=0
FAILURE_COUNT=0

for result in "${RESULTS[@]}"; do
    IFS='|' read -r cmd exit_code start end log <<< "$result"
    if [ "$exit_code" -eq 0 ]; then
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
    else
        FAILURE_COUNT=$((FAILURE_COUNT + 1))
    fi
done

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                   Execution Summary                        ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo "Total Artifacts: ${#ARTIFACTS[@]}"
echo -e "${GREEN}Successful: $SUCCESS_COUNT${NC}"
if [ $FAILURE_COUNT -gt 0 ]; then
    echo -e "${RED}Failed: $FAILURE_COUNT${NC}"
else
    echo "Failed: $FAILURE_COUNT"
fi
echo ""

if [ "$DRY_RUN" = false ]; then
    # Generate PREHANDOVER_PROOF document
    echo "Generating PREHANDOVER_PROOF document..."
    
    cat > "$OUTPUT_FILE" << 'PROOF_HEADER'
# PREHANDOVER_PROOF - Evidence Capture

**Agent**: [AGENT_NAME]  
**PR**: #[PR_NUMBER]  
**Branch**: [BRANCH_NAME]  
**Date**: DATEPLACEHOLDER  
**Latest Commit**: [COMMIT_SHA]  
**Protocol Version**: 2.0.0+  
**Execution Protocol**: Execution Bootstrap Protocol v2.0.0+

**Evidence Capture ID**: CAPTUREIDPLACEHOLDER

---

## Category 0: Execution Bootstrap Protocol

### Step 3: Validate Exit Codes

| Artifact | Command | Exit Code | Status |
|----------|---------|-----------|--------|
PROOF_HEADER

    # Replace placeholders
    sed -i "s/DATEPLACEHOLDER/$(date -u +%Y-%m-%d)/" "$OUTPUT_FILE"
    sed -i "s/CAPTUREIDPLACEHOLDER/$CAPTURE_ID/" "$OUTPUT_FILE"
    
    # Add artifact results
    for i in "${!RESULTS[@]}"; do
        result="${RESULTS[$i]}"
        IFS='|' read -r cmd exit_code start end log <<< "$result"
        
        artifact_num=$((i + 1))
        if [ "$exit_code" -eq 0 ]; then
            status="✅ PASS"
        else
            status="❌ FAIL"
        fi
        
        echo "| Artifact $artifact_num | \`$cmd\` | $exit_code | $status |" >> "$OUTPUT_FILE"
    done
    
    # Add evidence section
    cat >> "$OUTPUT_FILE" << EOF

**All exit codes are 0**: $([ $FAILURE_COUNT -eq 0 ] && echo "✅ YES" || echo "❌ NO")

---

### Step 4: Evidence Collection

**Evidence Location**: \`$CAPTURE_DIR\`

**Captured Evidence**:

EOF

    for i in "${!RESULTS[@]}"; do
        result="${RESULTS[$i]}"
        IFS='|' read -r cmd exit_code start end log <<< "$result"
        
        artifact_num=$((i + 1))
        artifact_id="artifact_$(printf "%03d" $artifact_num)"
        
        cat >> "$OUTPUT_FILE" << EOF
#### Artifact $artifact_num: \`$cmd\`

- **Start Time**: $start
- **End Time**: $end
- **Exit Code**: $exit_code
- **Log File**: \`$CAPTURE_DIR/${artifact_id}.log\`
- **Metadata**: \`$CAPTURE_DIR/${artifact_id}.meta\`

<details>
<summary>View Execution Log</summary>

\`\`\`
$(cat "$log" 2>/dev/null || echo "[Log content not available]")
\`\`\`

</details>

---

EOF
    done
    
    cat >> "$OUTPUT_FILE" << EOF

**Evidence Completeness**: $([ $FAILURE_COUNT -eq 0 ] && echo "✅ COMPLETE" || echo "⚠️ INCOMPLETE (failures detected)")

---

**Note**: This document was auto-generated. Complete remaining sections:
- Fill in metadata placeholders [AGENT_NAME], [PR_NUMBER], [BRANCH_NAME], [COMMIT_SHA]
- Complete Step 1, Step 2, Step 5, Step 6, Step 7
- Add Agent Attestation section

Validate with:
\`\`\`bash
python3 governance/scripts/validate_prehandover_proof.py $OUTPUT_FILE
\`\`\`

---

**END OF AUTO-GENERATED SECTION**
EOF

    echo -e "${GREEN}✅ PREHANDOVER_PROOF generated: $OUTPUT_FILE${NC}"
    echo ""
fi

# Final status
if [ $FAILURE_COUNT -eq 0 ]; then
    echo -e "${GREEN}✅ All artifacts executed successfully${NC}"
    echo ""
    if [ "$DRY_RUN" = false ]; then
        echo "Next steps:"
        echo "  1. Review evidence in: $CAPTURE_DIR"
        echo "  2. Complete PREHANDOVER_PROOF: $OUTPUT_FILE"
        echo "  3. Validate: python3 governance/scripts/validate_prehandover_proof.py $OUTPUT_FILE"
    fi
    echo ""
    exit 0
else
    echo -e "${RED}❌ Some artifacts failed execution${NC}"
    echo ""
    echo "Failures must be remediated before handover (Step 5)."
    echo ""
    exit 1
fi
