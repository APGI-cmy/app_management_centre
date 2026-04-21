# CodexAdvisor-agent — Agent File Non-Negotiables Checklist

**Agent**: CodexAdvisor-agent
**Version**: 1.0.0
**Last Updated**: 2026-04-21
**Authority**: CS2 (@APGI-cmy)
**Governance Ref**: AMC Issue #1068, CodexAdvisor contract Phase 3 Step 3.1
**QP Gate**: S4 — No unresolved draft markers, stub text, or non-final instructional text

---

## Purpose

This checklist defines all conditions that constitute a stub, placeholder, or TODO
for QP gate S4 enforcement.

CodexAdvisor loads and acknowledges all gates in this file during Phase 3 Step 3.1
before drafting any artifact. A single S4 failure blocks file write.

---

## S4 Gate — Prohibited Conditions

The following conditions are PROHIBITED in any final agent contract artifact.
If any condition is found: S4 FAIL — do not write the file.

### Category 1 — Literal Stub Strings

Search the draft for these exact strings (case-insensitive):

| String | Condition | S4 Result |
|--------|-----------|-----------|
| `TODO` | Present anywhere in file | FAIL |
| `PLACEHOLDER` | Present anywhere in file | FAIL |
| `TBD` | Present anywhere in file | FAIL |
| `[FILL IN]` | Present anywhere in file | FAIL |
| `[INSERT]` | Present anywhere in file | FAIL |
| `[ADD]` | Present anywhere in file | FAIL |
| `[DESCRIBE]` | Present anywhere in file | FAIL |
| `[PENDING]` | Present anywhere in file | FAIL |
| `[TO BE DETERMINED]` | Present anywhere in file | FAIL |
| `[TO BE ADDED]` | Present anywhere in file | FAIL |
| `[STUB]` | Present anywhere in file | FAIL |
| `<...>` | Unresolved angle-bracket placeholder | FAIL |
| `[NNN]` | Unresolved session number placeholder | FAIL |
| `[YYYY-MM-DD]` | Unresolved date placeholder | FAIL |
| `[wave-slug]` | Unresolved wave slug placeholder | FAIL |

**Exception**: Literal strings in template files (like this one) that demonstrate
placeholder format are permitted. The S4 check applies to agent contract artifacts
being composed for production use, not to template documents.

---

### Category 2 — Structural Stub Conditions

| Condition | Description | S4 Result |
|-----------|-------------|-----------|
| Empty PHASE body | A PHASE heading (1, 2, 3, or 4) exists but has no steps or content | FAIL |
| Empty YAML key | A required YAML key is present but has an empty or null value | FAIL |
| Null value in required field | Any required field set to `null`, `~`, or left blank | FAIL |
| Empty string in required field | Any required field set to `""` or `''` | FAIL |
| Missing required YAML key | A mandatory top-level YAML key is absent from frontmatter | FAIL |
| Empty phase step | A step heading exists but has no instruction content | FAIL |
| Incomplete prohibition block | A prohibition entry missing `id`, `rule`, or `enforcement` | FAIL |
| Incomplete halt condition | A halt entry missing `id`, `trigger`, or `action` | FAIL |
| Forward-reference without resolution | Text says "will be defined" or "see below" but target section is absent | FAIL |

---

### Category 3 — Non-Final Instructional Text

| Condition | Description | S4 Result |
|-----------|-------------|-----------|
| Assembly instructions retained | Phase body still contains template assembly instructions not replaced with actual content | FAIL |
| "Draft" or "WIP" in content | Body text includes "DRAFT", "WIP", "work in progress", or "draft phase" | FAIL |
| Pre-final completion markers | Text includes "pending IAA", "pending CS2", "to be completed" in a non-log context | FAIL |
| Stale pending-phase wording | Final artifact still reads as if in a mid-session state | FAIL |
| Instructional commentary | Comments from template like "Replace this with..." retained in final output | FAIL |

---

### Category 4 — Tier 2 Bulk in Tier 1 (S5 overlap)

| Condition | Description | S4 Result |
|-----------|-------------|-----------|
| Extended examples embedded | Full worked examples, case studies, or sample outputs in contract body | FAIL (S5) |
| Large tables embedded | Reference tables exceeding 20 rows that belong in Tier 2 knowledge | FAIL (S5) |
| Knowledge content embedded | Domain knowledge, tutorials, or explanatory text not needed for execution | FAIL (S5) |

---

## S4 Check Procedure

Before every file write, execute:

1. **String scan**: Search full draft for all Category 1 strings.
2. **Structure scan**: Verify all Phase bodies have content; all YAML keys are non-empty.
3. **Text review**: Confirm no instructional or draft-state text remains.
4. **Bulk review**: Confirm no Tier 2 bulk content is embedded in Tier 1.

If ANY check finds a prohibited condition:
- Record the specific finding
- Fix before re-running S4
- Do not write the file until S4 PASS

**S4 PASS** = Zero prohibited conditions found across all four categories.

---

## Gate Count

| Category | Condition Count |
|----------|----------------|
| 1 — Literal stub strings | 15 |
| 2 — Structural stubs | 9 |
| 3 — Non-final text | 5 |
| 4 — Tier 2 bulk (S5 overlap) | 3 |
| **Total** | **32** |

---

*Authority: CS2 (@APGI-cmy) | CodexAdvisor-agent Tier 2 Knowledge*
