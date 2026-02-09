# CI Confirmatory Protocol Violation - Learning Memory

**Learning ID**: BL-026-CI-CONFIRMATORY-VIOLATION-20260209  
**Date**: 2026-02-09  
**Agent**: Copilot (codex-advisor pattern)  
**Context**: PR #720 - Modular agent contract refactor  
**Severity**: HIGH (Constitutional protocol violation)  
**Memory Level**: Wave → Permanent (constitutional learning)

---

## Failure Pattern

### What Happened
Created PR #720 with modular agent contract refactor that:
- ✅ Passed functional validation (content preservation, structure)
- ✅ Passed YAML validation (yamllint)
- ❌ **FAILED** Deprecation Detection Gate (BL-026) in CI
- ❌ Used deprecated Python typing patterns in test file

### Why It Failed
**Root Cause**: CI Confirmatory Protocol Violation

**Constitutional Mandate Violated**:
> "CI gates are CONFIRMATORY, not DIAGNOSTIC. All checks must pass locally before PR submission. Discovery of issues in CI indicates pre-submission validation failure."  
> — CI_CONFIRMATORY_NOT_DIAGNOSTIC.md (Tier-0 Constitutional Canon)

**Agent Cognitive Gap**:
- Assumed YAML validation was sufficient for agent contract PR
- Did NOT run deprecation scan locally before PR
- Did NOT realize test files are subject to deprecation rules
- Treated CI as diagnostic (discovering issues) instead of confirmatory (verifying local validation)

---

## Specific Deprecations Found

### File: `tests/test_modular_agent_loading.py`

**Deprecated Patterns (7 total)**:
1. `typing.Dict` → Modern: `dict` (Python 3.9+)
2. `typing.List` → Modern: `list` (Python 3.9+)
3. `typing.Tuple` → Modern: `tuple` (Python 3.9+)
4. `open(file, 'r', ...)` → Modern: `open(file, ...)` (2 occurrences)

**Why These Are Deprecated**:
- Python 3.9+ supports native generic types (`dict`, `list`, `tuple`)
- PEP 585 deprecated `typing.Dict`, `typing.List`, `typing.Tuple`
- Default file open mode is already `'r'`, making it redundant

---

## What I Learned

### Learning #1: Comprehensive Gate Validation Required

**Before This Failure** (❌ Wrong Approach):
```
Pre-Submission Checklist:
- ✅ YAML validation (yamllint)
- ✅ Content preservation check
- ❌ Deprecation detection (SKIPPED)
- ❌ Comprehensive gate validation (SKIPPED)
→ Submit PR
→ CI discovers deprecation
→ GATE FAILURE
```

**After This Learning** (✅ Correct Approach):
```
Pre-Submission Checklist:
- ✅ YAML validation (yamllint)
- ✅ Deprecation detection (ruff check --select UP)
- ✅ Build-to-green enforcement
- ✅ Agent baseline validation (if agent files changed)
- ✅ Functional test suite
- ✅ All applicable gates from .github/workflows/
→ All gates pass locally
→ Submit PR
→ CI confirms (not discovers)
→ GATE SUCCESS
```

### Learning #2: Test Files Are Production Code

**Misconception**: "Test files are just helpers, they don't need strict quality standards"

**Reality**: Test files are subject to ALL quality gates including:
- Deprecation detection
- Zero warning enforcement
- Modern pattern compliance
- Build-to-green requirements

**Why**: Test files are part of the codebase and must be maintainable, up-to-date, and exemplary.

### Learning #3: Archive Files Are Scanned Too

**Misconception**: "Archive files are just backups, they won't be scanned"

**Reality**: The deprecation gate scans ALL Python files in the changeset, including:
- `_archive/` directory files
- Backup files
- Test files
- Utility scripts

**Implication**: If archiving old code with deprecated patterns, must either:
- Clean deprecations before archiving
- Verify `_archive/` is excluded in gate workflow
- Accept that archived files must be deprecation-clean

### Learning #4: CI Confirmatory Discipline

**Key Principle**: CI is NOT a linter or discovery tool

**What CI SHOULD Do**:
- ✅ **Confirm** that local validation passed
- ✅ **Verify** gates that were already passed locally
- ✅ **Protect** against accidental local validation skips

**What CI SHOULD NOT Do**:
- ❌ Discover issues that should have been found locally
- ❌ Be the first place deprecations are detected
- ❌ Function as a diagnostic tool for code quality

**Consequence**: CI failure = agent execution failure, not code discovery

---

## Prevention Measures Implemented

### 1. Comprehensive Pre-Submission Gate Checklist

**Created**: `PREHANDOVER_PROOF_DEPRECATION_FIX.md` (this PR)

**Mandatory Checks**:
```bash
# 1. YAML validation (existing)
yamllint .github/agents/

# 2. Deprecation detection (NEW - was missing)
ruff check --select UP $(git diff --name-only --diff-filter=ACM origin/main...HEAD | grep -E '\.py$')

# 3. Build-to-green enforcement (if applicable)
npm test  # or pytest, etc.

# 4. Agent baseline validation (if .agent files changed)
python3 scripts/validate_agent_file_baseline.py

# 5. All other applicable gates
# (check .github/workflows/ for complete list)
```

### 2. Updated PREHANDOVER_PROOF Template

**Requirement**: All future PREHANDOVER_PROOF documents must include:
```markdown
## Gate Execution (CI Confirmatory Protocol)

### Deprecation Detection (BL-026)
\`\`\`bash
$ ruff check --select UP <changed-python-files>
<output showing no deprecations>
\`\`\`

**Result**: ✅ PASS - No deprecated APIs detected
```

### 3. Self-Learning Memory Integration

**This File**: `.agent-workspace/foreman/learnings/ci-confirmatory-violation-20260209.md`

**Memory Promotion Path**:
- Session Memory → ✅ (captured immediately after failure)
- Wave Memory → ✅ (archived for current wave context)
- Constitutional Memory → ⚠️ (if pattern repeats, escalate)

**Trigger for Constitutional Promotion**:
- Second occurrence of CI Confirmatory violation
- Pattern repeats with same agent class
- Learning not integrated into standard workflow

---

## Commands for Future Use

### Local Deprecation Scan (Before PR)
```bash
# Scan all changed Python files
git diff --name-only --diff-filter=ACM origin/main...HEAD | \
  grep -E '\.py$' | \
  xargs ruff check --select UP

# Or scan specific file
ruff check --select UP path/to/file.py
```

### Auto-Fix Deprecations (If Safe)
```bash
# Auto-fix where possible (review changes!)
ruff check --select UP --fix path/to/file.py
```

### Full Gate Validation
```bash
# Run all gates that will run in CI
# (list may vary - check .github/workflows/)
yamllint .
ruff check --select UP .
pytest tests/
# ... other gates as applicable
```

---

## Root Pattern Identified

**Agent Cognitive Bias**: "Structural refactoring feels safe, deprecation checks feel optional"

**Reality**: Structural refactoring is **HIGH RISK** for deprecation introduction because:
- New files created (may use old patterns)
- Copy-paste from existing code (carries old patterns)
- Test files added (subject to same rules as production)
- Focus on functionality over modern patterns

**Corrective Pattern**: 
> "Any PR that creates/modifies Python files MUST run deprecation scan locally BEFORE submission. No exceptions."

---

## Success Criteria for Learning Integration

This learning is considered integrated when:
- [x] Deprecation fixed in current PR
- [x] Local deprecation scan passes
- [x] PREHANDOVER_PROOF includes deprecation validation
- [x] Learning documented in memory file
- [ ] Pre-submission checklist used in next 3 PRs
- [ ] No repeat of CI Confirmatory violation in next 10 PRs
- [ ] Pattern becomes automatic (unconscious competence)

---

## Escalation Triggers

**Escalate to Constitutional Memory if**:
- Second CI Confirmatory violation occurs
- Pattern repeats with same root cause
- Learning not integrated after 3 PRs
- Systemic issue affecting multiple agents

**Escalation Action**:
- Promote to Tier-0 constitutional learning
- Update CI_CONFIRMATORY_NOT_DIAGNOSTIC.md with specific examples
- Require mandatory pre-submission gate checklist
- Add gate validation to agent contract requirements

---

**Memory Level**: Wave (permanent in wave context)  
**Promotion Status**: Pending (monitor for constitutional escalation)  
**Integration Status**: In Progress (current PR implementing fixes)  
**Authority**: BL-026 Bootstrap Learning, CI_CONFIRMATORY_NOT_DIAGNOSTIC.md
