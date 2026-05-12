#!/bin/bash
# validate-simple-pr-admin.sh
#
# Purpose: Validate the .admin/pr.json PR admin manifest for AMC
# Authority: governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md v1.2.0
#            governance/canon/POLC_EXECUTION_MODEL_CANON.md v1.0.0
#            APGI-cmy/app_management_centre#1172 — Layer-down POLC execution model
#
# Exit Codes:
#   0 = PASS — manifest is valid and all checks pass
#   1 = FAIL — one or more checks failed
#   2 = ERROR — usage error or missing dependency
#
# Usage:
#   ./validate-simple-pr-admin.sh [--manifest <path>] [--changed-files <file>] [--base-ref <ref>] [--skip-diff]
#
# Options:
#   --manifest <path>        Path to the PR admin manifest (default: .admin/pr.json)
#   --changed-files <file>   File containing newline-separated list of changed files.
#                            If omitted, changed files are derived from git diff.
#   --base-ref <ref>         Git base ref for diff (default: origin/main)
#   --skip-diff              Skip execution-model changed-files detection (useful for template checks)
#
# Governance-control file patterns (triggers requires_iaa/requires_ecap enforcement):
#   .github/workflows/
#   .github/scripts/
#   .github/agents/
#   governance/           (all sub-paths: canon/, templates/, policies/, checklists/, etc.)
#   .agent-admin/
#   *.agent.md files (agent contracts)
#
# Implementation file patterns (triggers execution_model enforcement — Check 13):
#   apps/
#   src/
#   modules/
#   lib/
#   packages/
#
# Authority: governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md v1.2.0
#            governance/canon/POLC_EXECUTION_MODEL_CANON.md v1.0.0

set -euo pipefail

# ── Color helpers ─────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

pass()  { echo -e "${GREEN}✅ $*${NC}"; }
fail()  { echo -e "${RED}❌ $*${NC}"; }
warn()  { echo -e "${YELLOW}⚠️  $*${NC}"; }
info()  { echo "   $*"; }

# ── Defaults ──────────────────────────────────────────────────────────────────
MANIFEST=".admin/pr.json"
CHANGED_FILES_INPUT=""
BASE_REF="origin/main"
SKIP_DIFF=false
FAILURES=0

# ── Argument parsing ──────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
    case "$1" in
        --manifest)
            MANIFEST="$2"
            shift 2
            ;;
        --changed-files)
            CHANGED_FILES_INPUT="$2"
            shift 2
            ;;
        --base-ref)
            BASE_REF="$2"
            shift 2
            ;;
        --skip-diff)
            SKIP_DIFF=true
            shift
            ;;
        -h|--help)
            sed -n '/^# Usage:/,/^$/p' "$0"
            exit 0
            ;;
        *)
            echo "Unknown option: $1" >&2
            exit 2
            ;;
    esac
done

# ── Dependency check ──────────────────────────────────────────────────────────
if ! command -v jq &>/dev/null; then
    fail "jq is required but not installed"
    exit 2
fi

# ── Header ────────────────────────────────────────────────────────────────────
echo "======================================================="
echo "  AMC PR Admin Manifest Validator"
echo "  Authority: governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md v1.2.0"
echo "             governance/canon/POLC_EXECUTION_MODEL_CANON.md v1.0.0"
echo "======================================================="
echo ""
echo "Manifest: ${MANIFEST}"
echo ""

# ── Check 1: Manifest exists ──────────────────────────────────────────────────
echo "--- Check 1: Manifest exists ---"
if [[ ! -f "${MANIFEST}" ]]; then
    fail "Manifest not found: ${MANIFEST}"
    info "Every governed AMC PR must have .admin/pr.json"
    info "Reference: governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md §3.1"
    echo ""
    exit 1
fi
pass "Manifest found: ${MANIFEST}"
echo ""

# ── Check 2: Valid JSON ───────────────────────────────────────────────────────
echo "--- Check 2: Valid JSON ---"
if ! jq empty "${MANIFEST}" 2>/dev/null; then
    fail "Manifest is not valid JSON: ${MANIFEST}"
    echo ""
    exit 1
fi
pass "Valid JSON"
echo ""

# ── Check 3: Required fields present ─────────────────────────────────────────
echo "--- Check 3: Required fields ---"
REQUIRED_FIELDS=("type" "requires_iaa" "requires_ecap" "governing_issue" "scope_summary")
MISSING_FIELDS=()

for field in "${REQUIRED_FIELDS[@]}"; do
    value=$(jq -r --arg f "$field" '.[$f]' "${MANIFEST}" 2>/dev/null)
    if [[ "$value" == "null" ]]; then
        MISSING_FIELDS+=("$field")
    fi
done

if [[ ${#MISSING_FIELDS[@]} -gt 0 ]]; then
    fail "Missing required fields:"
    for f in "${MISSING_FIELDS[@]}"; do
        info "  - $f"
    done
    FAILURES=$((FAILURES + 1))
else
    pass "All required fields present"
fi
echo ""

# ── If fields are missing, stop here since subsequent checks will be unreliable
if [[ $FAILURES -gt 0 ]]; then
    fail "Validation failed with ${FAILURES} error(s) — required fields missing"
    echo ""
    exit 1
fi

# ── Check 4: type is accepted ─────────────────────────────────────────────────
echo "--- Check 4: type is accepted ---"
TYPE=$(jq -r '.type' "${MANIFEST}")
ACCEPTED_TYPES=("product-fix" "docs-only" "governance-control" "agent-contract" "migration" "deployment" "high-risk")
TYPE_VALID=false
for t in "${ACCEPTED_TYPES[@]}"; do
    if [[ "$TYPE" == "$t" ]]; then
        TYPE_VALID=true
        break
    fi
done
if [[ "$TYPE_VALID" == "false" ]]; then
    fail "type '${TYPE}' is not accepted"
    info "Accepted values: ${ACCEPTED_TYPES[*]}"
    FAILURES=$((FAILURES + 1))
else
    pass "type: ${TYPE}"
fi
echo ""

# ── Check 5: requires_iaa and requires_ecap are boolean ──────────────────────
echo "--- Check 5: requires_iaa and requires_ecap are boolean ---"
REQ_IAA_TYPE=$(jq -r '.requires_iaa | type' "${MANIFEST}" 2>/dev/null || echo "unknown")
REQ_ECAP_TYPE=$(jq -r '.requires_ecap | type' "${MANIFEST}" 2>/dev/null || echo "unknown")
BOOL_FAIL=false
if [[ "$REQ_IAA_TYPE" != "boolean" ]]; then
    fail "requires_iaa must be a boolean (true/false), got type: ${REQ_IAA_TYPE}"
    BOOL_FAIL=true
    FAILURES=$((FAILURES + 1))
fi
if [[ "$REQ_ECAP_TYPE" != "boolean" ]]; then
    fail "requires_ecap must be a boolean (true/false), got type: ${REQ_ECAP_TYPE}"
    BOOL_FAIL=true
    FAILURES=$((FAILURES + 1))
fi
if [[ "$BOOL_FAIL" == "false" ]]; then
    pass "requires_iaa: $(jq -r '.requires_iaa' "${MANIFEST}"), requires_ecap: $(jq -r '.requires_ecap' "${MANIFEST}")"
fi
echo ""

# ── Check 6: governing_issue pattern ─────────────────────────────────────────
echo "--- Check 6: governing_issue pattern ---"
GOVERNING_ISSUE=$(jq -r '.governing_issue' "${MANIFEST}")
if ! [[ "$GOVERNING_ISSUE" =~ ^#[0-9]+$ ]]; then
    fail "governing_issue must match pattern ^#[0-9]+\$ (e.g. '#1163'), got: '${GOVERNING_ISSUE}'"
    FAILURES=$((FAILURES + 1))
else
    pass "governing_issue: ${GOVERNING_ISSUE}"
fi
echo ""

# ── Check 7: scope_summary length ────────────────────────────────────────────
echo "--- Check 7: scope_summary length (10–500 chars) ---"
SCOPE_SUMMARY=$(jq -r '.scope_summary' "${MANIFEST}")
SCOPE_LEN=${#SCOPE_SUMMARY}
if [[ "$SCOPE_LEN" -lt 10 ]]; then
    fail "scope_summary is too short (${SCOPE_LEN} chars, minimum 10)"
    FAILURES=$((FAILURES + 1))
elif [[ "$SCOPE_LEN" -gt 500 ]]; then
    fail "scope_summary is too long (${SCOPE_LEN} chars, maximum 500)"
    FAILURES=$((FAILURES + 1))
else
    pass "scope_summary: ${SCOPE_LEN} chars"
fi
echo ""

# ── Check 8: Full-ceremony types require requires_iaa=true and requires_ecap=true ─────
echo "--- Check 8: Full-ceremony types require requires_iaa=true and requires_ecap=true ---"
FULL_CEREMONY_TYPES=("governance-control" "agent-contract" "migration" "deployment" "high-risk")
IS_FULL_CEREMONY=false
for ft in "${FULL_CEREMONY_TYPES[@]}"; do
    if [[ "$TYPE" == "$ft" ]]; then
        IS_FULL_CEREMONY=true
        break
    fi
done

if [[ "$IS_FULL_CEREMONY" == "true" ]]; then
    REQUIRES_IAA=$(jq -r '.requires_iaa' "${MANIFEST}" 2>/dev/null || echo "false")
    REQUIRES_ECAP=$(jq -r '.requires_ecap' "${MANIFEST}" 2>/dev/null || echo "false")
    CEREMONY_FAIL=false
    if [[ "$REQUIRES_IAA" != "true" ]]; then
        fail "type '${TYPE}' requires requires_iaa=true (BR-01)"
        CEREMONY_FAIL=true
        FAILURES=$((FAILURES + 1))
    fi
    if [[ "$REQUIRES_ECAP" != "true" ]]; then
        fail "type '${TYPE}' requires requires_ecap=true (BR-02)"
        CEREMONY_FAIL=true
        FAILURES=$((FAILURES + 1))
    fi
    if [[ "$CEREMONY_FAIL" == "false" ]]; then
        pass "type '${TYPE}': requires_iaa=true and requires_ecap=true (full ceremony)"
    fi
else
    pass "type '${TYPE}' does not require full ceremony by type alone"
fi
echo ""

# ── Check 9: governance-control files in diff require IAA and ECAP ────────────
# Governance-control file patterns — changes to these trigger IAA/ECAP enforcement
GOVERNANCE_CONTROL_PATTERNS=(
    "^\.github/workflows/"
    "^\.github/scripts/"
    "^\.github/agents/"
    "^governance/"
    "^\.agent-admin/"
    "\.agent\.md$"
)

echo "--- Check 9: governance-control files in diff require requires_iaa=true and requires_ecap=true ---"

DIFF_CHANGED_FILES=""
DIFF_AVAILABLE=false

if [[ "$SKIP_DIFF" == "true" ]]; then
    warn "Skipping diff-based governance-control check (--skip-diff)"
    DIFF_AVAILABLE=false
elif [[ -n "$CHANGED_FILES_INPUT" ]]; then
    if [[ ! -f "$CHANGED_FILES_INPUT" ]]; then
        warn "Changed files input file not found: ${CHANGED_FILES_INPUT} — skipping diff check"
    else
        DIFF_CHANGED_FILES=$(cat "$CHANGED_FILES_INPUT")
        if [[ "$DIFF_CHANGED_FILES" =~ [^[:space:]] ]]; then
            DIFF_AVAILABLE=true
        else
            warn "Changed files input file is empty: ${CHANGED_FILES_INPUT} — skipping diff check"
            DIFF_AVAILABLE=false
        fi
    fi
else
    # Derive from git diff
    if git rev-parse --git-dir &>/dev/null 2>&1; then
        if git rev-parse "${BASE_REF}" &>/dev/null 2>&1; then
            if DIFF_CHANGED_FILES=$(git diff --name-only "${BASE_REF}...HEAD" 2>/dev/null); then
                DIFF_AVAILABLE=true
            else
                warn "git diff failed — skipping diff-based governance-control check"
            fi
        else
            warn "Base ref '${BASE_REF}' not found — skipping diff-based governance-control check"
        fi
    else
        warn "Not in a git repository — skipping diff-based governance-control check"
    fi
fi

if [[ "$DIFF_AVAILABLE" == "true" ]]; then
    GOV_CONTROL_FOUND=false
    GOV_CONTROL_FILE=""
    while IFS= read -r fpath; do
        [[ -z "$fpath" ]] && continue
        for pattern in "${GOVERNANCE_CONTROL_PATTERNS[@]}"; do
            if [[ "$fpath" =~ $pattern ]]; then
                GOV_CONTROL_FOUND=true
                GOV_CONTROL_FILE="$fpath"
                break
            fi
        done
        [[ "$GOV_CONTROL_FOUND" == "true" ]] && break
    done <<< "$DIFF_CHANGED_FILES"

    REQUIRES_IAA=$(jq -r '.requires_iaa' "${MANIFEST}" 2>/dev/null || echo "false")
    REQUIRES_ECAP=$(jq -r '.requires_ecap' "${MANIFEST}" 2>/dev/null || echo "false")

    if [[ "$GOV_CONTROL_FOUND" == "true" ]]; then
        info "Governance-control file in diff: ${GOV_CONTROL_FILE}"
        GOV_FAIL=false
        if [[ "$REQUIRES_IAA" != "true" ]]; then
            fail "Governance-control file in diff but requires_iaa is not true"
            GOV_FAIL=true
            FAILURES=$((FAILURES + 1))
        fi
        if [[ "$REQUIRES_ECAP" != "true" ]]; then
            fail "Governance-control file in diff but requires_ecap is not true"
            GOV_FAIL=true
            FAILURES=$((FAILURES + 1))
        fi
        if [[ "$GOV_FAIL" == "false" ]]; then
            pass "requires_iaa=true and requires_ecap=true (governance-control file in diff)"
        fi
    else
        pass "No governance-control files detected in diff"
        info "  requires_iaa: ${REQUIRES_IAA}, requires_ecap: ${REQUIRES_ECAP}"
    fi
else
    warn "Diff not available — governance-control file check skipped"
fi
echo ""

# ── Check 10: No additional properties ───────────────────────────────────────
echo "--- Check 10: No unexpected properties ---"
ALLOWED_PROPERTIES=("type" "requires_iaa" "requires_ecap" "governing_issue" "scope_summary"
                    "created_by" "created_at"
                    "execution_model" "implementing_agent" "orchestrating_agent" "cs2_justification")

EXTRA_PROPS=()
while IFS= read -r key; do
    FOUND=false
    for allowed in "${ALLOWED_PROPERTIES[@]}"; do
        if [[ "$key" == "$allowed" ]]; then
            FOUND=true
            break
        fi
    done
    if [[ "$FOUND" == "false" ]]; then
        EXTRA_PROPS+=("$key")
    fi
done < <(jq -r 'keys[]' "${MANIFEST}" 2>/dev/null || true)

if [[ ${#EXTRA_PROPS[@]} -gt 0 ]]; then
    fail "Unexpected properties found (additionalProperties: false):"
    for p in "${EXTRA_PROPS[@]}"; do
        info "  - $p"
    done
    FAILURES=$((FAILURES + 1))
else
    pass "No unexpected properties"
fi
echo ""

# ── Check 11: execution_model value is accepted (if present) ─────────────────
echo "--- Check 11: execution_model value (if present) ---"
EXECUTION_MODEL=$(jq -r '.execution_model // empty' "${MANIFEST}" 2>/dev/null || true)
if [[ -n "$EXECUTION_MODEL" ]]; then
    ACCEPTED_MODELS=("builder-governed" "foreman-orchestrated" "cs2-hotfix-override")
    MODEL_VALID=false
    for m in "${ACCEPTED_MODELS[@]}"; do
        if [[ "$EXECUTION_MODEL" == "$m" ]]; then
            MODEL_VALID=true
            break
        fi
    done
    if [[ "$MODEL_VALID" == "false" ]]; then
        fail "execution_model '${EXECUTION_MODEL}' is not accepted"
        info "  Accepted values: ${ACCEPTED_MODELS[*]}"
        info "  Authority: governance/canon/POLC_EXECUTION_MODEL_CANON.md"
        FAILURES=$((FAILURES + 1))
    else
        pass "execution_model: ${EXECUTION_MODEL}"
    fi
else
    pass "execution_model not declared (will be checked in Check 13 if implementation files present)"
fi
echo ""

# ── Check 12: execution_model companion fields ────────────────────────────────
echo "--- Check 12: execution_model companion fields ---"
EXECUTION_MODEL=$(jq -r '.execution_model // empty' "${MANIFEST}" 2>/dev/null || true)
if [[ -n "$EXECUTION_MODEL" ]]; then
    case "$EXECUTION_MODEL" in
        builder-governed)
            IMPLEMENTING_AGENT=$(jq -r '.implementing_agent // empty' "${MANIFEST}" 2>/dev/null || true)
            if [[ -z "$IMPLEMENTING_AGENT" ]]; then
                fail "execution_model=builder-governed requires implementing_agent"
                info "  Authority: governance/canon/POLC_EXECUTION_MODEL_CANON.md §3.1"
                FAILURES=$((FAILURES + 1))
            else
                pass "implementing_agent: ${IMPLEMENTING_AGENT}"
            fi
            ;;
        foreman-orchestrated)
            ORCHESTRATING_AGENT=$(jq -r '.orchestrating_agent // empty' "${MANIFEST}" 2>/dev/null || true)
            IMPLEMENTING_AGENT=$(jq -r '.implementing_agent // empty' "${MANIFEST}" 2>/dev/null || true)
            COMPANION_FAIL=false
            if [[ -z "$ORCHESTRATING_AGENT" ]]; then
                fail "execution_model=foreman-orchestrated requires orchestrating_agent"
                info "  Authority: governance/canon/POLC_EXECUTION_MODEL_CANON.md §3.2"
                COMPANION_FAIL=true
                FAILURES=$((FAILURES + 1))
            else
                pass "orchestrating_agent: ${ORCHESTRATING_AGENT}"
            fi
            if [[ -z "$IMPLEMENTING_AGENT" ]]; then
                fail "execution_model=foreman-orchestrated requires implementing_agent"
                info "  Authority: governance/canon/POLC_EXECUTION_MODEL_CANON.md §3.2"
                COMPANION_FAIL=true
                FAILURES=$((FAILURES + 1))
            else
                pass "implementing_agent: ${IMPLEMENTING_AGENT}"
            fi
            ;;
        cs2-hotfix-override)
            CS2_JUSTIFICATION=$(jq -r '.cs2_justification // empty' "${MANIFEST}" 2>/dev/null || true)
            if [[ -z "$CS2_JUSTIFICATION" ]]; then
                fail "execution_model=cs2-hotfix-override requires cs2_justification"
                info "  Authority: governance/canon/POLC_EXECUTION_MODEL_CANON.md §3.3"
                FAILURES=$((FAILURES + 1))
            else
                pass "cs2_justification: present"
            fi
            ;;
        *)
            # Already caught in Check 11
            ;;
    esac
else
    pass "No execution_model declared — companion field check skipped"
fi
echo ""

# ── Check 13: execution_model required for implementation PRs (POLC_EXECUTION_MODEL_CANON.md) ──
#
# Implementation file patterns — changes to these trigger execution_model enforcement
# Authority: governance/canon/POLC_EXECUTION_MODEL_CANON.md §2.1
IMPLEMENTATION_PATTERNS=(
    "^apps/"
    "^src/"
    "^modules/"
    "^lib/"
    "^packages/"
)

echo "--- Check 13: execution_model required for implementation PRs ---"
echo "    (Authority: governance/canon/POLC_EXECUTION_MODEL_CANON.md)"

EXECUTION_MODEL=$(jq -r '.execution_model // empty' "${MANIFEST}" 2>/dev/null || true)

if [[ "$SKIP_DIFF" == "true" ]]; then
    warn "Skipping implementation-file detection (--skip-diff)"
    pass "execution_model check skipped (--skip-diff)"
elif [[ "$DIFF_AVAILABLE" == "true" ]]; then
    IMPL_FILE_FOUND=false
    IMPL_FILE_EXAMPLE=""
    while IFS= read -r fpath; do
        [[ -z "$fpath" ]] && continue
        for pattern in "${IMPLEMENTATION_PATTERNS[@]}"; do
            if [[ "$fpath" =~ $pattern ]]; then
                IMPL_FILE_FOUND=true
                IMPL_FILE_EXAMPLE="$fpath"
                break
            fi
        done
        [[ "$IMPL_FILE_FOUND" == "true" ]] && break
    done <<< "$DIFF_CHANGED_FILES"

    if [[ "$IMPL_FILE_FOUND" == "true" ]]; then
        info "Implementation file in diff: ${IMPL_FILE_EXAMPLE}"
        if [[ -z "$EXECUTION_MODEL" ]]; then
            fail "Implementation files changed, but execution_model is missing."
            info "  Declare one of: builder-governed, foreman-orchestrated, cs2-hotfix-override"
            info "  Authority: governance/canon/POLC_EXECUTION_MODEL_CANON.md §4"
            FAILURES=$((FAILURES + 1))
        else
            pass "execution_model declared for implementation PR: ${EXECUTION_MODEL}"
        fi
    elif [[ -n "$EXECUTION_MODEL" ]]; then
        # execution_model present even though no implementation files detected — accepted
        pass "execution_model declared (no implementation file pattern matched in diff): ${EXECUTION_MODEL}"
    else
        pass "No implementation files in diff — execution_model not required"
    fi
else
    warn "Diff not available — implementation-file check skipped"
    if [[ -n "$EXECUTION_MODEL" ]]; then
        pass "execution_model declared: ${EXECUTION_MODEL}"
    else
        warn "execution_model not declared (cannot verify if required without diff)"
    fi
fi
echo ""

# ── Summary ───────────────────────────────────────────────────────────────────
echo "======================================================="
if [[ $FAILURES -eq 0 ]]; then
    pass "PR admin manifest validation PASSED"
    echo ""
    echo "Manifest: ${MANIFEST}"
    echo "PR type:  $(jq -r '.type' "${MANIFEST}")"
    echo "IAA:      $(jq -r '.requires_iaa' "${MANIFEST}")"
    echo "ECAP:     $(jq -r '.requires_ecap' "${MANIFEST}")"
    EXEC_MODEL=$(jq -r '.execution_model // "not declared"' "${MANIFEST}" 2>/dev/null || echo "not declared")
    echo "Exec:     ${EXEC_MODEL}"
    echo "Authority: CS2 | SPAM-001 v1.2.0 | POLC_EXECUTION_MODEL_CANON.md v1.0.0"
    echo "======================================================="
    exit 0
else
    fail "PR admin manifest validation FAILED with ${FAILURES} error(s)"
    echo ""
    echo "Reference: governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md v1.2.0"
    echo "           governance/canon/POLC_EXECUTION_MODEL_CANON.md v1.0.0"
    echo "======================================================="
    exit 1
fi
