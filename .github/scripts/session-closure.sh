#!/bin/bash
# Session Closure Protocol - Living Agent System v6.2.0
# Per REQ-EO-005
# Authority: LIVING_AGENT_SYSTEM.md, FOREMAN_MEMORY_PROTOCOL.md

set -euo pipefail

AGENT_ID="${1:-foreman}"
WORKSPACE=".agent-workspace/$AGENT_ID"
TIMESTAMP=$(date +%Y%m%d)
SESSION_NUM=$(printf "%03d" $(($(find "$WORKSPACE/memory" -name "session-*.md" 2>/dev/null | wc -l) + 1)))
SESSION_FILE="$WORKSPACE/memory/session-$SESSION_NUM-$TIMESTAMP.md"

echo "======================================================================"
echo "🔒 SESSION CLOSURE PROTOCOL - Living Agent System v6.2.0"
echo "======================================================================"
echo ""
echo "Agent: $AGENT_ID"
echo "Date: $TIMESTAMP"
echo "Session: $SESSION_NUM"
echo ""

# Step 1: Create Session Memory
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 1: Create Session Memory"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 Creating session memory file..."

mkdir -p "$WORKSPACE/memory"

# Detect session ID from git context
GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")
GIT_COMMIT=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")

cat > "$SESSION_FILE" << EOFMEMORY
# Session $SESSION_NUM - $TIMESTAMP (Living Agent System v6.2.0)

## Agent
- Type: $AGENT_ID
- Class: $(if [ "$AGENT_ID" = "foreman" ]; then echo "supervisor"; else echo "executor"; fi)
- Session ID: session-$SESSION_NUM-$TIMESTAMP
- Branch: $GIT_BRANCH
- Commit: $GIT_COMMIT

## Task
[Document what you were asked to do in this session]

Example:
- Implement merge gate alignment with Living Agent System v6.2.0
- Create 3-gate standard interface
- Close 9 critical governance gaps

## What I Did

### Files Modified
[List key files modified with brief description]

Example:
- .github/workflows/merge-gate-interface.yml - New 3-gate interface
- .github/scripts/wake-up-protocol.sh - Wake-up protocol implementation
- .agent-admin/governance/merge-gate-design-v2-20260212.md - Design document

### Actions Taken
[List major actions taken during this session]

Example:
- Action 1: Audited current 16 workflow gates
- Action 2: Identified 23 gaps (9 critical, 8 high, 6 medium)
- Action 3: Designed 3-gate standard interface
- Action 4: Implemented merge-gate-interface.yml workflow
- Action 5: Created wake-up and session-closure scripts

### Decisions Made
[Document key decisions and rationale]

Example:
- Decision 1: Consolidate 16 gates into 3 standard jobs
  - Rationale: Branch protection standardization, simpler mental model
- Decision 2: Enforce wake-up/session-closure protocols in gates
  - Rationale: Close critical gaps in protocol enforcement

## Living Agent System Evidence

### Evidence Collection
- Evidence log: .agent-admin/gates/gate-results.json
- Status: [COMPLETE | PARTIAL | INCOMPLETE]

### Ripple Status
- Status: [NO_RIPPLE | RIPPLE_PLANNED | RIPPLE_EXECUTED]
- Ripple required: [YES/NO]
- Downstream impacts: [if applicable]

### Governance Gap Progress
- Gaps addressed: [list gaps closed]
- Gaps remaining: [list open gaps]

### Governance Hygiene
- Status: [CLEAN | ISSUES_DETECTED]
- Issues: [if any]

## Outcome
[Choose one and expand]
✅ COMPLETE
⚠️ PARTIAL
❌ ESCALATED

Details:
[Explain outcome status]

## Lessons

### What Worked Well
[Document positive patterns for future sessions]

Example:
- Lesson 1: Evidence-first error messages reduce agent debugging time
- Lesson 2: Deterministic PR classification eliminates ambiguity

### What Was Challenging
[Document difficulties encountered]

Example:
- Challenge 1: Balancing comprehensiveness with gate execution time
- Challenge 2: Ensuring bootstrap paradox handled correctly

### What Future Sessions Should Know
[Provide guidance for future work]

Example:
- Recommendation 1: Test new gates with trial PRs before enforcing
- Recommendation 2: Document CS2 escalation triggers clearly
- Recommendation 3: Keep gate error messages evidence-first (no log archaeology)

### Governance Insights
[Document governance-related learnings]

Example:
- Insight 1: Standard interface enables cross-repo governance consistency
- Insight 2: Wake-up/session-closure protocols critical for evidence chain

## Escalations
[If blockers or governance gaps require CS2 attention]

- Escalation 1: [if any]
- Resolution: [if resolved]

---
**Authority**: LIVING_AGENT_SYSTEM.md v6.2.0 | Session: $SESSION_NUM
**Created**: $TIMESTAMP | Agent: $AGENT_ID

EOFMEMORY

echo "✅ Session memory created: $(basename $SESSION_FILE)"
echo ""

# Step 2: Rotate Session Memories
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 2: Rotate Session Memories"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔄 Checking session memory count..."

SESSION_COUNT=$(find "$WORKSPACE/memory" -name "session-*.md" -type f 2>/dev/null | wc -l)
echo "Current session count: $SESSION_COUNT"

if [ "$SESSION_COUNT" -gt 5 ]; then
  echo "Rotating old sessions (keeping 5 most recent)..."
  mkdir -p "$WORKSPACE/memory/.archive"
  
  # Move oldest sessions to archive
  SESSIONS_TO_ARCHIVE=$((SESSION_COUNT - 5))
  find "$WORKSPACE/memory" -name "session-*.md" -type f | sort | head -n "$SESSIONS_TO_ARCHIVE" | while read -r OLD_SESSION; do
    mv "$OLD_SESSION" "$WORKSPACE/memory/.archive/"
    echo "  Archived: $(basename $OLD_SESSION)"
  done
  
  echo "✅ Archived $SESSIONS_TO_ARCHIVE old session(s)"
else
  echo "✅ No rotation needed ($SESSION_COUNT sessions ≤ 5)"
fi
echo ""

# Step 3: Verify Evidence Completeness
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 3: Verify Evidence Completeness"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔍 Checking evidence artifact bundle..."

EVIDENCE_WARNINGS=0

# Check required directories
REQUIRED_DIRS=(
  ".agent-admin/prehandover"
  ".agent-admin/gates"
  ".agent-admin/improvements"
  ".agent-admin/governance"
)

for DIR in "${REQUIRED_DIRS[@]}"; do
  if [ ! -d "$DIR" ]; then
    echo "⚠️  Missing: $DIR"
    ((EVIDENCE_WARNINGS++))
  else
    echo "✅ Exists: $DIR"
  fi
done

# Check required files
if [ ! -f ".agent-admin/gates/gate-results.json" ]; then
  echo "⚠️  Missing: .agent-admin/gates/gate-results.json"
  ((EVIDENCE_WARNINGS++))
else
  echo "✅ Exists: gate-results.json"
fi

if [ ! -f ".agent-admin/improvements/improvements.md" ]; then
  echo "⚠️  Missing: .agent-admin/improvements/improvements.md"
  ((EVIDENCE_WARNINGS++))
else
  echo "✅ Exists: improvements.md"
fi

# Check prehandover proof
if [ -z "$(find .agent-admin/prehandover -name '*.md' -type f 2>/dev/null)" ]; then
  echo "⚠️  Missing: Prehandover proof (.md file)"
  ((EVIDENCE_WARNINGS++))
else
  echo "✅ Exists: Prehandover proof"
fi

echo ""
if [ "$EVIDENCE_WARNINGS" -eq 0 ]; then
  echo "✅ Evidence bundle COMPLETE"
else
  echo "⚠️  Evidence bundle INCOMPLETE ($EVIDENCE_WARNINGS warnings)"
  echo ""
  echo "Recommendation: Create missing evidence artifacts before finalizing PR"
  echo "Use templates in governance/templates/ if available"
fi
echo ""

# Step 4: Remind about Learning Artifacts
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 4: Learning Artifact Reminder"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📚 Checking personal learning artifacts..."

if [ -f "$WORKSPACE/personal/lessons-learned.md" ]; then
  echo "✅ lessons-learned.md exists"
  echo "   Reminder: Update with lessons from this session"
else
  echo "⚠️  lessons-learned.md not found"
fi

if [ -f "$WORKSPACE/personal/patterns.md" ]; then
  echo "✅ patterns.md exists"
  echo "   Reminder: Update with patterns observed in this session"
else
  echo "⚠️  patterns.md not found"
fi

echo ""
echo "💡 TIP: Add session learnings to:"
echo "   - $WORKSPACE/personal/lessons-learned.md"
echo "   - $WORKSPACE/personal/patterns.md"
echo ""

# Step 5: Archive Working Contract
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 5: Archive Working Contract"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ -f "$WORKSPACE/working-contract.md" ]; then
  echo "ℹ️  Working contract is ephemeral (excluded from git)"
  echo "   Location: $WORKSPACE/working-contract.md"
  echo "   Status: Will be regenerated on next wake-up"
else
  echo "ℹ️  No working contract found (expected if not generated)"
fi
echo ""

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Session Closure Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ Step 1: Session Memory Created"
echo "✅ Step 2: Memory Rotation Complete"
echo "✅ Step 3: Evidence Verification Complete ($EVIDENCE_WARNINGS warnings)"
echo "✅ Step 4: Learning Artifact Reminder Issued"
echo "✅ Step 5: Working Contract Status Checked"
echo ""
echo "======================================================================"
echo "✅ SESSION CLOSURE COMPLETE"
echo "======================================================================"
echo ""
echo "Session memory: $SESSION_FILE"
echo "Session ID: session-$SESSION_NUM-$TIMESTAMP"
echo ""
echo "📝 TODO BEFORE FINALIZING PR:"
echo "   1. Edit $SESSION_FILE with session details"
echo "   2. Update $WORKSPACE/personal/lessons-learned.md"
echo "   3. Update $WORKSPACE/personal/patterns.md"
if [ "$EVIDENCE_WARNINGS" -gt 0 ]; then
  echo "   4. Complete missing evidence artifacts ($EVIDENCE_WARNINGS warnings)"
fi
echo "   5. Commit all changes to git"
echo ""
echo "Next session: Run wake-up-protocol.sh to begin"
echo ""

exit 0
