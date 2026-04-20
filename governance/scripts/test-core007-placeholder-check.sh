#!/usr/bin/env bash
# CORE-007 Proof-of-Operation Test Script
# Authority: AGENT_CONTRACT_PLACEHOLDER_CHECK_CANON.md v1.0.0
# Issue: #1094 (APGI-cmy/app_management_centre) — layer-down activation 2026-04-20
#
# Verifies:
#   - True-positive preservation: genuine unresolved content still fails CORE-007 (canon §8.1)
#   - False-positive reduction: governed meta-language now passes CORE-007 (canon §8.2)
set -euo pipefail

PASS=0
FAIL=0

# Apply the CORE-007 filter chain to a single line.
# Returns the number of violations (0 = passes, >0 = flagged).
check_line() {
  local line="$1"
  local tmpfile
  tmpfile=$(mktemp)
  echo "$line" > "$tmpfile"
  local violations=0
  while IFS= read -r l; do
    # EXC-001: governance condition descriptions
    if echo "$l" | grep -qiE "(placeholder|stub|TBD).*(hash|detect|trigger|mode|state|escalat|condition|gate)"; then continue; fi
    if echo "$l" | grep -qiE "(hash|detect|trigger|mode|state|escalat|condition|gate).*(placeholder|stub|TBD)"; then continue; fi
    # EXC-002: checker or output template strings / iaa_audit_token
    if echo "$l" | grep -qiE "(echo|print|output|message|report|template).*['\"].*((no )?(placeholder|stub|TBD|TODO)|iaa_audit_token)"; then continue; fi
    if echo "$l" | grep -qiE "iaa_audit_token"; then continue; fi
    # EXC-003: negative assertions
    if echo "$l" | grep -qiE "no (placeholder|stub|TBD|TODO)(.*content|[^a-zA-Z]|$)"; then continue; fi
    # EXC-004: checklist / gate labels
    if echo "$l" | grep -qiE "(gate|check|checklist|step)[^a-zA-Z]+(placeholder|stub|TBD)"; then continue; fi
    if echo "$l" | grep -qiE "(placeholder|stub|TBD)[^a-zA-Z]+(gate|check|checklist|step)"; then continue; fi
    # EXC-005: canon hash-validation terminology
    if echo "$l" | grep -qiE "placeholder.*(hash|api)"; then continue; fi
    if echo "$l" | grep -qiE "(hash|api).*placeholder"; then continue; fi
    violations=$((violations + 1))
  done < <(grep -niE "(^|[^[:alnum:]_])(placeholder|stub|TBD|TODO:|FIXME:)([^[:alnum:]_]|$)" "$tmpfile" || true)
  rm -f "$tmpfile"
  echo "$violations"
}

assert_fail() {
  local id="$1" line="$2"
  local v; v=$(check_line "$line")
  if [ "$v" -gt 0 ]; then
    echo "PASS [$id] (violations=$v) — correctly blocked: $line"
    PASS=$((PASS + 1))
  else
    echo "FAIL [$id] — expected block, got none: $line"
    FAIL=$((FAIL + 1))
  fi
}

assert_pass() {
  local id="$1" line="$2"
  local v; v=$(check_line "$line")
  if [ "$v" -eq 0 ]; then
    echo "PASS [$id] (violations=0) — correctly exempted: $line"
    PASS=$((PASS + 1))
  else
    echo "FAIL [$id] — expected exemption, got violations=$v: $line"
    FAIL=$((FAIL + 1))
  fi
}

echo "=== CORE-007 Proof-of-Operation — AGENT_CONTRACT_PLACEHOLDER_CHECK_CANON.md v1.0.0 ==="
echo ""

echo "--- Section A: True-Positive Preservation (canon §8.1 — must remain blocked) ---"
assert_fail A1 "Phase 3 Build Script: TBD — complete before activation"
assert_fail A2 "authority: placeholder — will bind to canon when determined"
assert_fail A3 "enforcement rule: [stub] — not yet defined"
assert_fail A4 "agent_version: placeholder"
assert_fail A5 "FIXME: this section is incomplete"

echo ""
echo "--- Section B: False-Positive Reduction (canon §8.2 — must now pass) ---"
assert_pass B1 "CANON_INVENTORY placeholder hashes detected → DEGRADED MODE"    # EXC-001
assert_pass B2 "No placeholder/stub/TODO content: ✅"                            # EXC-003
assert_pass B3 "Detect placeholder or TBD values in hash fields"                 # EXC-005
assert_pass B4 "Gate: placeholder-check-enforcement"                             # EXC-004
assert_pass B5 "echo 'No stub content detected in contract body'"                # EXC-002

echo ""
echo "--- Section C: AMC Continuity (iaa_audit_token must still pass via EXC-002) ---"
assert_pass C1 "iaa_audit_token: IAA-session-049-20260420-PASS"

echo ""
echo "--- Section D: Boundary Cases (canon §8.3) ---"
assert_pass D1 "Detect placeholder hashes and escalate"   # EXC-001
assert_pass D3 "No TBD content present ✅"                # EXC-003
assert_fail D4 "TBD: resolve before PR merge"
assert_pass D5 "Gate name: placeholder-scan"              # EXC-004

echo ""
TOTAL=$((PASS + FAIL))
echo "=== Summary: ${PASS}/${TOTAL} tests passed ==="
if [ "$FAIL" -gt 0 ]; then
  echo "❌ $FAIL test(s) failed"
  exit 1
fi
echo "✅ All tests passed"
exit 0
