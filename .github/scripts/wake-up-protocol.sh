#!/bin/bash
# Wake-Up Protocol - Living Agent System v6.2.0
# Per REQ-AS-005
# Authority: LIVING_AGENT_SYSTEM.md, FOREMAN_MEMORY_PROTOCOL.md

set -euo pipefail

AGENT_ID="${1:-foreman}"
WORKSPACE=".agent-workspace/$AGENT_ID"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")

echo "======================================================================"
echo "📋 WAKE-UP PROTOCOL - Living Agent System v6.2.0"
echo "======================================================================"
echo ""
echo "Agent: $AGENT_ID"
echo "Timestamp: $TIMESTAMP"
echo ""

# Phase 1: Self-Identification
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Phase 1: Self-Identification"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔍 Reading agent identity..."

# Try versioned contract first, then fall back to unversioned
if [ -f ".github/agents/${AGENT_ID}-v2.md" ]; then
  CONTRACT_FILE=".github/agents/${AGENT_ID}-v2.md"
elif [ -f ".github/agents/${AGENT_ID}.md" ]; then
  CONTRACT_FILE=".github/agents/${AGENT_ID}.md"
else
  echo "❌ ERROR: Agent contract not found"
  echo "Expected: .github/agents/${AGENT_ID}-v2.md or .github/agents/${AGENT_ID}.md"
  exit 1
fi

echo "✅ Identity loaded: $CONTRACT_FILE"
echo ""

# Phase 2: Memory Scan
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Phase 2: Memory Scan"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🧠 Scanning session memories..."

mkdir -p "$WORKSPACE/memory"

# Find last 5 session memories
LAST_5_SESSIONS=$(find "$WORKSPACE/memory" -name "session-*.md" -type f 2>/dev/null | sort -r | head -5 || echo "")
SESSION_COUNT=$(echo "$LAST_5_SESSIONS" | grep -c . || echo "0")

if [ "$SESSION_COUNT" -gt 0 ]; then
  echo "✅ Found $SESSION_COUNT recent session(s)"
  echo ""
  echo "Most recent sessions:"
  echo "$LAST_5_SESSIONS" | head -3 | xargs -n1 basename 2>/dev/null || true
else
  echo "ℹ️  No previous sessions found (first session)"
fi
echo ""

# Phase 3: Governance Discovery
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Phase 3: Governance Discovery"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📚 Loading governance canon..."

if [ -f "governance/CANON_INVENTORY.json" ]; then
  CANON_COUNT=$(jq -r '. | length' governance/CANON_INVENTORY.json 2>/dev/null || echo "0")
  echo "✅ Governance canon loaded ($CANON_COUNT entries)"
else
  echo "⚠️  WARNING: CANON_INVENTORY.json not found"
  echo "Continuing in degraded mode..."
fi
echo ""

# Phase 4: Environment Health Check
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Phase 4: Environment Health Check"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔧 Checking environment health..."

# Ensure evidence directories exist
if [ ! -d ".agent-admin" ]; then
  echo "Creating evidence directories..."
  mkdir -p .agent-admin/{prehandover,gates,rca,improvements,governance}
  echo "✅ Evidence directories created"
else
  echo "✅ Evidence directories exist"
fi

# Ensure personal learning directories exist
mkdir -p "$WORKSPACE/personal"
if [ ! -f "$WORKSPACE/personal/lessons-learned.md" ]; then
  cat > "$WORKSPACE/personal/lessons-learned.md" << 'EOFLESSONS'
# Lessons Learned

## Session YYYYMMDD

### Lesson: [Title]
- Context: [when this applies]
- Pattern: [what to watch for]
- Action: [what to do]
EOFLESSONS
  echo "✅ Created lessons-learned.md template"
else
  echo "✅ lessons-learned.md exists"
fi

if [ ! -f "$WORKSPACE/personal/patterns.md" ]; then
  cat > "$WORKSPACE/personal/patterns.md" << 'EOFPATTERNS'
# Patterns Observed

## Pattern: [Name]
- Observed: YYYY-MM-DD (Session NNN)
- Context: [when this occurs]
- Response: [how to handle]
EOFPATTERNS
  echo "✅ Created patterns.md template"
else
  echo "✅ patterns.md exists"
fi

echo ""

# Phase 5: Working Contract Generation
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Phase 5: Working Contract Generation"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 Generating working contract..."

# Get recent session summary if available
RECENT_CONTEXT="No recent sessions"
if [ -n "$LAST_5_SESSIONS" ]; then
  LATEST_SESSION=$(echo "$LAST_5_SESSIONS" | head -1)
  if [ -f "$LATEST_SESSION" ]; then
    RECENT_CONTEXT="Latest: $(basename $LATEST_SESSION)"
  fi
fi

# Generate working contract
cat > "$WORKSPACE/working-contract.md" << EOFCONTRACT
# Working Contract - Session $(date +%Y%m%d-%H%M%S)

**Agent**: $AGENT_ID
**Generated**: $TIMESTAMP
**Governance Version**: Living Agent System v6.2.0
**Contract Version**: 2.0.0

---

## Mission & Identity

Per agent contract: $CONTRACT_FILE

**Primary Responsibilities**:
- Architecture-first execution
- Zero-test-debt enforcement
- Evidence-based governance
- Merge gate ownership (if FM)

---

## Active Obligations

### Evidence Artifacts (REQ-EO-006)
- ✅ Evidence artifact bundle required under .agent-admin/
- ✅ Prehandover proof mandatory
- ✅ Gate results JSON (machine-readable)
- ✅ Improvements capture (may be PARKED)
- ✅ RCA (if stop-and-fix occurred)

### Protocol Execution (REQ-AS-005, REQ-EO-005)
- ✅ Wake-up protocol: EXECUTED (this session)
- ⏳ Session closure: REQUIRED at session end
- ✅ Canon hash integrity: MANDATORY validation
- ✅ Zero test debt: ENFORCED

### Learning & Memory (FOREMAN_MEMORY_PROTOCOL.md)
- ✅ Session memory creation required
- ✅ Lessons learned documentation
- ✅ Patterns observation
- ✅ Memory rotation (keep 5 most recent)

---

## Governance Context

### Canon Integrity
- CANON_INVENTORY validation: MANDATORY
- Placeholder hashes: FORBIDDEN (degraded mode)
- Protected files: CS2 approval required
- Constitutional canon: Amendment process required

### Merge Gate Interface
- Standard workflow: "Merge Gate Interface"
- Required jobs: merge-gate/verdict, governance/alignment, stop-and-fix/enforcement
- All gates must PASS for merge eligibility
- Branch protection: 3 required contexts

---

## Recent Context

$RECENT_CONTEXT

---

## Critical Invariants

1. **One-Time Build Law**: Build correctly first time, every time
2. **Zero Regression**: Never break existing functionality
3. **Zero Test Debt**: 100% GREEN required, no failing/skipped/TODO tests
4. **Evidence-First**: All claims backed by machine-readable evidence
5. **Protocol Compliance**: Wake-up and session-closure mandatory

---

## Session Closure Requirements

Before ending this session:
1. ✅ Run session-closure.sh
2. ✅ Create session memory file
3. ✅ Update lessons-learned.md
4. ✅ Update patterns.md
5. ✅ Rotate old session memories (>5)
6. ✅ Verify evidence bundle complete

---

**Generated by**: wake-up-protocol.sh v1.0.0
**Authority**: LIVING_AGENT_SYSTEM.md v6.2.0
**Status**: ACTIVE (ephemeral, not committed to git)

EOFCONTRACT

echo "✅ Working contract generated"
echo "   Location: $WORKSPACE/working-contract.md"
echo "   Status: ACTIVE (ephemeral)"
echo ""

# Phase 6: Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Wake-Up Protocol Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ Phase 1: Self-Identification COMPLETE"
echo "✅ Phase 2: Memory Scan COMPLETE ($SESSION_COUNT sessions)"
echo "✅ Phase 3: Governance Discovery COMPLETE"
echo "✅ Phase 4: Environment Health Check COMPLETE"
echo "✅ Phase 5: Working Contract Generation COMPLETE"
echo ""
echo "======================================================================"
echo "✅ WAKE-UP PROTOCOL COMPLETE"
echo "======================================================================"
echo ""
echo "Agent $AGENT_ID is ready for execution."
echo "Working contract: $WORKSPACE/working-contract.md"
echo ""
echo "Next: Execute task, then run session-closure.sh at session end"
echo ""

exit 0
