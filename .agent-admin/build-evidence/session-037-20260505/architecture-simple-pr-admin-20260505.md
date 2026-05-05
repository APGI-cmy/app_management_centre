# Architecture Design — AMC Simple PR Admin Model
# Wave: wave-simple-pr-admin-20260505
# Session: session-037
# Date: 2026-05-05
# Authority: CS2 (@APGI-cmy) — Issue #1163
# Status: FROZEN — approved for builder delegation

---

## 1. Problem Statement

The AMC governance system currently applies the same full ceremony (IAA Final Audit + ECAP
ceremony + prehandover proof + wave record) to all PRs regardless of scope. This creates
significant overhead for simple product-fix PRs (e.g., a typo fix, a UI label correction,
a minor config update) that pose minimal governance risk.

The AMC Simple PR Admin Model (AMC equivalent of maturion-isms#1530) introduces a two-tier
ceremony model:

- **Tier 1 (Full Ceremony)**: Unchanged. All governance-control, agent-contract, migration,
  database, deployment, and high-risk PRs continue to require full IAA + ECAP ceremony.
- **Tier 2 (Simple Admin)**: New lightweight path for product-fix PRs. The PR author creates
  `.admin/pr.json` declaring the PR type and ceremony exemptions. CI gates read this manifest
  and downgrade ceremony requirements accordingly.

---

## 2. Architecture Components

### 2.1 New Canon: `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md`

**Purpose**: Defines the two-tier PR ceremony model, the `.admin/pr.json` schema, forced-ceremony
override rules, and the preservation requirements for full-ceremony PR types.

**Version**: 1.0.0
**Canon ID**: SPAM-001

**Key sections**:
1. Purpose and Scope
2. PR Type Classification Table
3. `.admin/pr.json` Schema (normative)
4. Simple Admin Mode: Conditions and Activation
5. Forced-Ceremony Override: Conditions that reinstate full ceremony regardless of manifest
6. Preserved Controls: Gates that are NEVER downgraded
7. Implementation Reference (CI gate hook points)

**PR Type Classification**:

| Type | Ceremony Level | `requires_iaa` | `requires_ecap` | Notes |
|------|---------------|-----------------|-----------------|-------|
| `product-fix` | Simple Admin | false | false | Small functional fixes, minor UI/config changes |
| `docs-only` | Simple Admin | false | false | Documentation-only changes |
| `governance-control` | Full | true | true | Changes to governance canon or control infrastructure |
| `agent-contract` | Full | true | true | Changes to `.github/agents/**` |
| `migration` | Full | true | true | Database schema changes |
| `deployment` | Full | true | true | Infrastructure / deployment configuration changes |
| `high-risk` | Full | true | true | Any PR that the author or Foreman classifies as high-risk |

**Forced-Ceremony Override** (these paths reinstate full ceremony regardless of `pr.json`):
- `.github/agents/**`
- `governance/**`
- `.governance-pack/**`
- `.agent-workspace/**/knowledge/**`
- `supabase/migrations/**`
- `schema/` and `migrations/` path prefixes
- `BUILD_PROGRESS_TRACKER*`

**Preserved Controls** (NEVER downgraded regardless of `pr.json`):
- POLC boundary validation (`polc-boundary-gate.yml` foreman-implementation-check)
- Build-to-green enforcement (`build-to-green-enforcement.yml`)
- Agent contract format gate (`agent-contract-format-gate.yml`)
- Agent boundary gate (`agent-boundary-gate.yml`)
- Agent bootstrap inject gate (`agent-bootstrap-inject.yml`)

### 2.2 `.admin/pr.json` Schema

**Location**: `.admin/pr.json` (per-PR file, created by the PR author)

**Schema** (`.admin/pr.json.schema.json`):

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AMC PR Admin Manifest",
  "description": "Single source of truth for PR ceremony level in AMC Simple PR Admin Model (SPAM-001)",
  "type": "object",
  "required": ["type", "requires_iaa", "requires_ecap", "governing_issue", "scope_summary"],
  "properties": {
    "type": {
      "type": "string",
      "enum": ["product-fix", "docs-only", "governance-control", "agent-contract", "migration", "deployment", "high-risk"],
      "description": "PR classification type"
    },
    "requires_iaa": {
      "type": "boolean",
      "description": "Whether IAA final assurance is required for this PR"
    },
    "requires_ecap": {
      "type": "boolean",
      "description": "Whether ECAP ceremony is required for this PR"
    },
    "governing_issue": {
      "type": "string",
      "pattern": "^#[0-9]+$",
      "description": "Reference to the governing issue (e.g., '#1163')"
    },
    "scope_summary": {
      "type": "string",
      "minLength": 10,
      "maxLength": 500,
      "description": "Brief human-readable description of what this PR does"
    },
    "created_by": {
      "type": "string",
      "description": "Agent or user ID that created this manifest"
    },
    "created_at": {
      "type": "string",
      "format": "date-time",
      "description": "ISO-8601 timestamp when this manifest was created"
    }
  },
  "additionalProperties": false
}
```

**Business rules**:
1. `requires_iaa` MUST be `true` if `type` is `governance-control`, `agent-contract`, `migration`, `deployment`, or `high-risk`
2. `requires_ecap` MUST be `true` if `type` is `governance-control`, `agent-contract`, `migration`, `deployment`, or `high-risk`
3. If `.admin/pr.json` is absent, gates behave as before (full ceremony required for agent/foreman PRs)
4. If `.admin/pr.json` exists but is invalid JSON or fails schema validation → full ceremony required (treat as absent)
5. If `.admin/pr.json` says `requires_iaa: false` but diff contains forced-ceremony paths → full ceremony reinstated; gate logs override warning

### 2.3 CI Gate Modifications

#### 2.3.1 `iaa-ecap-hard-gate.yml`

**Change**: Add Simple Admin bypass step to `classify-protected-paths` job.

After the existing `AUTO_BYPASS` check, add:
```bash
# ------------------------------------------------------------------
# Simple Admin Model bypass: .admin/pr.json with type=product-fix
# ------------------------------------------------------------------
SIMPLE_ADMIN=false
if [ -f ".admin/pr.json" ]; then
  PR_TYPE=$(python3 -c "import json,sys; d=json.load(open('.admin/pr.json')); print(d.get('type',''))" 2>/dev/null || echo "")
  PR_REQ_IAA=$(python3 -c "import json,sys; d=json.load(open('.admin/pr.json')); print(str(d.get('requires_iaa',True)).lower())" 2>/dev/null || echo "true")
  PR_REQ_ECAP=$(python3 -c "import json,sys; d=json.load(open('.admin/pr.json')); print(str(d.get('requires_ecap',True)).lower())" 2>/dev/null || echo "true")
  
  if [[ "$PR_TYPE" == "product-fix" || "$PR_TYPE" == "docs-only" ]] && \
     [[ "$PR_REQ_IAA" == "false" ]] && \
     [[ "$PR_REQ_ECAP" == "false" ]]; then
    # Check for forced-ceremony paths
    HAS_FORCED_PATHS=false
    FORCED_PATTERNS=("^\.github/agents/" "^governance/" "^\.governance-pack/" 
                     "^\.agent-workspace/.*/knowledge/" "supabase/migrations/" 
                     "^schema/" "^migrations/" "BUILD_PROGRESS_TRACKER")
    while IFS= read -r fpath; do
      [ -z "$fpath" ] && continue
      for pattern in "${FORCED_PATTERNS[@]}"; do
        if echo "$fpath" | grep -qE "$pattern"; then
          HAS_FORCED_PATHS=true
          break 2
        fi
      done
    done <<< "$CHANGED"
    
    if [ "$HAS_FORCED_PATHS" = "false" ]; then
      echo "✅ Simple Admin Model: .admin/pr.json type=$PR_TYPE, requires_iaa=false, requires_ecap=false"
      echo "   No forced-ceremony paths detected — SIMPLE_ADMIN bypass activated."
      SIMPLE_ADMIN=true
      # Set outputs to bypass IAA and ECAP gates
      echo "is_auto_bypass=true" >> $GITHUB_OUTPUT
      echo "is_protected_path_pr=false" >> $GITHUB_OUTPUT
      echo "requires_iaa=false" >> $GITHUB_OUTPUT
      exit 0
    else
      echo "⚠️  Simple Admin override: .admin/pr.json requests simple admin, but forced-ceremony paths detected."
      echo "   Full ceremony reinstated per SPAM-001 §5 Forced-Ceremony Override rule."
    fi
  fi
fi
```

#### 2.3.2 `preflight-evidence-gate.yml`

**Change**: After the layer-down/governance bypass check, add a Simple Admin bypass.

For product-fix PRs with valid `.admin/pr.json`:
- Session memory check → downgrade to informational (still runs, but does not block)
- Wave task list (IAA prebrief) check → downgrade to informational (still runs, but does not block)
- Agent bootstrap inject check → still runs and is still blocking

#### 2.3.3 `polc-boundary-gate.yml`

**Change**: Add `.admin/pr.json` check.

For product-fix PRs:
- `foreman-implementation-check`: Continues to run (POLC boundary preserved)
- `builder-involvement-check`: Continues to run
- `session-memory-check`: Downgraded to informational (not blocking)

#### 2.3.4 `merge-gate-interface.yml`

**Change**: Add `product-fix` as a recognized PR type in the `classify-pr` job.

Product-fix PRs with valid `.admin/pr.json` → `pr_type=product-fix`.

### 2.4 Tier 1 Canon Updates

#### 2.4.1 `AGENT_HANDOVER_AUTOMATION.md` (v1.7.3 → v1.7.4)

Add new section after §4.3e: **§4.3f Simple Admin Model Exception**

Content:
```
### 4.3f Simple Admin Model Exception (SPAM-001)

For product-fix PRs where `.admin/pr.json` declares `type: product-fix`,
`requires_iaa: false`, `requires_ecap: false`, AND no forced-ceremony paths are touched:

- §4.3c Pre-IAA Commit-State Gate → NOT REQUIRED
- §4.3d Scope-Declaration Parity Gate → NOT REQUIRED
- §4.3e Admin Ceremony Compliance Gate → NOT REQUIRED (ECAP not appointed)
- §4.4 IAA Invocation → NOT REQUIRED
- §4.5 Token Ceremony → NOT REQUIRED

Phase 4 for Simple Admin PRs consists of:
- §4.1 Evidence: `.admin/pr.json` serves as the evidence manifest
- §4.2 Session Memory: Optional (recommended for agent-authored PRs)
- Merge gate parity check: All preserved-control gates still apply

Forced-ceremony override: If the PR diff touches any forced-ceremony path (SPAM-001 §5),
full ceremony is reinstated regardless of `.admin/pr.json` declarations.

Authority: SPAM-001 (MMM_SIMPLE_PR_ADMIN_MODEL.md)
```

#### 2.4.2 `EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` (v1.3.0 → v1.3.1)

Add new section §2.4: **Product-Fix PR Exception**

Content:
```
### 2.4 Product-Fix PR Exception (SPAM-001)

ECAP appointment is NOT required for product-fix PRs where:
1. `.admin/pr.json` exists and is valid
2. `.admin/pr.json` declares `type: product-fix` AND `requires_ecap: false`
3. The PR diff does NOT touch any forced-ceremony path (SPAM-001 §5)

For such PRs, `.admin/pr.json` itself serves as the ceremony declaration.
The Foreman does NOT need to appoint `execution-ceremony-admin-agent`.

If any forced-ceremony path is present in the diff, ECAP appointment is reinstated
regardless of `.admin/pr.json` declarations. The Foreman MUST verify this before
proceeding without ECAP.
```

---

## 3. QA-to-Red Criteria

Since this is a governance/CI alignment wave (no production application code), the "Red" QA
criteria are CI gate behavior assertions. The red tests are verified by checking the before/after
gate behavior:

**RED-037-01**: CI gate `iaa-ecap-hard-gate.yml` currently has NO mechanism to read `.admin/pr.json`
→ After TASK-037-04: Gate reads `.admin/pr.json` and bypasses IAA/ECAP for product-fix PRs

**RED-037-02**: CI gate `preflight-evidence-gate.yml` currently has NO mechanism to bypass for product-fix
→ After TASK-037-05: Gate reads `.admin/pr.json` and downgraded session memory check for product-fix

**RED-037-03**: CI gate `polc-boundary-gate.yml` currently blocks all PRs without session memory for foreman PRs
→ After TASK-037-06: Gate downgraded for product-fix PRs with valid `.admin/pr.json`

**RED-037-04**: `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` does NOT exist
→ After TASK-037-01: File exists, valid, references committed at HEAD

**RED-037-05**: `.admin/` directory does NOT exist  
→ After TASK-037-08: Directory exists with README and schema

---

## 4. Implementation Guidance for Builders

### 4.1 For governance-liaison-amc-agent (TASKS 037-01, 037-02, 037-03)

Focus on creating well-structured governance canon documentation. The MMM_SIMPLE_PR_ADMIN_MODEL.md
must be authoritative, machine-parseable (clear field definitions), and include the full schema
specification as normative content. The AGENT_HANDOVER_AUTOMATION.md and ECAP amendments must
preserve all existing content and add the new exceptions as clearly labeled addendum sections.

### 4.2 For integration-builder (TASKS 037-04, 037-05, 037-06, 037-07, 037-08)

Focus on defensive programming in the `.admin/pr.json` reading logic:
- Always use `python3` or `jq` to parse JSON (never string matching)
- Handle malformed JSON gracefully (treat as absent → full ceremony)
- Handle missing `.admin/pr.json` gracefully (full ceremony as default)
- Always check for forced-ceremony paths AFTER reading `.admin/pr.json`
- Log clear messages explaining bypass/reinstatement decisions
- The schema validation should be a separate step with clear error messages

All CI gate changes must maintain full backward compatibility. The default behavior (no `.admin/pr.json`)
must be identical to the current behavior.

---

## 5. Acceptance Criteria

| AC | Criterion | Evidence Type |
|----|-----------|---------------|
| AC-01 | `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` exists at HEAD with version 1.0.0 | File exists check |
| AC-02 | `.admin/README.md` explains directory purpose and .admin/pr.json format | File exists + content check |
| AC-03 | `.admin/pr.json.schema.json` is valid JSON Schema | JSON Schema validation |
| AC-04 | `iaa-ecap-hard-gate.yml` reads `.admin/pr.json` and bypasses for product-fix/no-forced-paths | Workflow grep |
| AC-05 | `iaa-ecap-hard-gate.yml` preserves full ceremony if forced-ceremony paths detected | Logic check |
| AC-06 | `preflight-evidence-gate.yml` downgrades session-memory check for product-fix PRs | Workflow grep |
| AC-07 | `polc-boundary-gate.yml` preserves POLC checks; downgrades session-memory-check for product-fix | Workflow grep |
| AC-08 | `merge-gate-interface.yml` recognizes product-fix as PR type | Workflow grep |
| AC-09 | `AGENT_HANDOVER_AUTOMATION.md` amended with §4.3f Simple Admin Model Exception | File content check |
| AC-10 | `EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` amended with product-fix exception | File content check |
| AC-11 | All existing CI gate bypass conditions (layer-down, governance, automated) are preserved | YAML content check |
| AC-12 | No forced-ceremony-path bypass: governance/**, .github/agents/**, .governance-pack/**, migrations/ always force full ceremony | Logic check |

---

**Architecture Status**: FROZEN — approved for IAA Pre-Brief and builder delegation
**Foreman**: foreman-v2-agent — session-037-20260505
