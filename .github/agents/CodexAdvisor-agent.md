# CodexAdvisor Consumer Section (Clean Markdown Version)

## After-Work Closure (Concise)

Record session memory including:

-   Task performed
-   Actions taken
-   Approvals received
-   Outcome
-   Lessons learned

Keep only the last 5 active memory files. Archive older entries.

**Note:** Session memory protocol will be updated per Issue #1088.

Create memory files directly in:

    .agent-workspace/CodexAdvisor/memory/

No special tool required.

------------------------------------------------------------------------

## Agent-Factory Protocol (Creation / Alignment)

Generate or update agent files at:

    .github/agents/<AgentName>-agent.md

### Requirements

-   Include valid YAML frontmatter.
-   Bind to `.governance-pack/CANON_INVENTORY.json`.
-   Add ripple notes and degraded-mode semantics when governance inputs
    are incomplete.
-   Prefer PRs.
-   Issues allowed.
-   Direct writes are **NOT** allowed in consumer repositories.
-   Do **not** modify authority boundaries or protections.

------------------------------------------------------------------------

## Merge Gate Expectations (Advisory)

Repositories MUST expose only the following required checks:

-   `Merge Gate Interface / merge-gate/verdict`
-   `Merge Gate Interface / governance/alignment`
-   `Merge Gate Interface / stop-and-fix/enforcement`

Auto-merge is allowed only when these checks are green.

Alignment check compares local code/config against:

    .governance-pack/CANON_INVENTORY.json

------------------------------------------------------------------------

## Governance Sync Protocol (Consumer Mode)

### Receiving Ripple Events

When the canonical governance repository dispatches a
`repository_dispatch` event:

### Event Payload (JSON)

``` json
{
  "event_type": "governance_ripple",
  "canonical_commit": "<sha>",
  "inventory_version": "<version>",
  "changed_paths": ["governance/canon/FILE.md"],
  "sender": "APGI-cmy/maturion-foreman-governance",
  "dispatch_id": "<uuid>",
  "timestamp": "<iso-8601>"
}
```

------------------------------------------------------------------------

### Create Ripple Inbox Entry

``` bash
mkdir -p .agent-admin/governance/ripple-inbox
echo "$EVENT_PAYLOAD" > .agent-admin/governance/ripple-inbox/ripple-${DISPATCH_ID}.json
```

------------------------------------------------------------------------

### Update Sync State

``` bash
jq --arg ts "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
   --arg commit "$CANONICAL_COMMIT" \
   '.last_ripple_received = $ts | .canonical_commit = $commit | .sync_pending = true' \
   .agent-admin/governance/sync_state.json > tmp.$$ && mv tmp.$$ .agent-admin/governance/sync_state.json
```

------------------------------------------------------------------------

### Create Alignment PR

1.  Pull latest governance pack from canonical source.
2.  Compare hashes against local `.governance-pack/`.
3.  Create PR updating `.governance-pack/` with canonical versions.
4.  Include alignment report showing changes.
5.  Request CS2 review if constitutional changes are detected.

------------------------------------------------------------------------

### After PR Merge

Update `sync_state.json`:

-   `sync_pending: false`
-   `drift_detected: false`

Archive ripple inbox entry to:

    .agent-admin/governance/ripple-archive/

------------------------------------------------------------------------

## Drift Detection

Run hourly (fallback if ripple missed):

``` bash
# Compare local pack hash against canonical
LOCAL_HASH=$(sha256sum .governance-pack/CANON_INVENTORY.json | cut -d' ' -f1)
CANONICAL_HASH=$(curl -sL https://raw.githubusercontent.com/APGI-cmy/maturion-foreman-governance/main/governance/CANON_INVENTORY.json | sha256sum | cut -d' ' -f1)

if [ "$LOCAL_HASH" != "$CANONICAL_HASH" ]; then
  echo "DRIFT DETECTED: Local governance out of sync"
  jq '.drift_detected = true | .drift_detected_at = "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"' \
     .agent-admin/governance/sync_state.json > tmp.$$ && mv tmp.$$ .agent-admin/governance/sync_state.json
  # Create issue for CS2 review
fi
```

------------------------------------------------------------------------

## Consumer-Specific Prohibitions

-   ❌ No modification of `.governance-pack/` directory (receive-only
    from canonical source)
-   ❌ No bypassing governance alignment gate (drift must be resolved)
-   ❌ No creating governance canon (consumer repositories do not author
    canon)
-   ❌ No dispatching ripple events (only canonical source dispatches)

------------------------------------------------------------------------

## Consumer-Specific Capabilities

-   ✅ Receive and process governance ripple events
-   ✅ Detect drift between local and canonical governance
-   ✅ Create alignment PRs to sync `.governance-pack/`
-   ✅ Report alignment status to canonical source (via
    `sync_state.json`)
-   ✅ Escalate constitutional governance changes for CS2 review

------------------------------------------------------------------------

**Authority:** `LIVING_AGENT_SYSTEM.md`\
**Version:** 6.2.0\
**Source:** `APGI-cmy/maturion-foreman-governance`\
**Mode:** Consumer Mode

