# Issue #1233 — A2-R UTC Runtime Defect Inventory

## Authority

- Governing issue: #1233
- Parent QA issue: #1226
- Parent draft PR: #1232
- Upstream predecessor: A1 Optional import repair merged by PR #1239
- Lane: A2-R — runtime-side missing-`UTC` import repair

This record inventories the exact runtime-side files currently evidenced to call
`datetime.now(UTC)` without a corresponding `UTC` import and therefore suitable
for a bounded import-only repair lane.

## Exact runtime file inventory

The following files were identified by repository search as runtime/production
surfaces that reference `UTC`:

```text
fm/orchestration/build_authorization_gate.py
fm/runtime/watchdog/alert_reader.py
fm/runtime/watchdog/escalation_reporter.py
foreman/analytics/cost_tracker.py
foreman/analytics/metrics_engine.py
foreman/analytics/storage.py
foreman/analytics/usage_analyzer.py
foreman/domain/blocker.py
foreman/domain/program.py
foreman/domain/task.py
foreman/domain/wave.py
foreman/flows/flow_executor.py
foreman/intent/approval_manager.py
foreman/intent/intake_handler.py
python_agent/memory_proposal_client.py
```

## Deliberate exclusions

The following files also reference `UTC` but are outside A2-R authority and are
therefore excluded from the runtime builder write allowlist:

### Already-correct runtime files

These files already import `UTC` and require no repair:

```text
fm/runtime/integration_failure_handler.py
fm/runtime/security_failure_handler.py
fm/data/models/base.py
fm/data/models/clarification_session.py
fm/data/models/conversation.py
fm/data/models/message.py
fm/orchestration/build_intervention.py
fm/orchestration/build_node_inspector.py
foreman/cross_cutting/audit_logger.py
foreman/cross_cutting/evidence_store.py
foreman/cross_cutting/memory_manager.py
foreman/cross_cutting/memory_proposal.py
foreman/cross_cutting/notification_dispatcher.py
foreman/cross_cutting/system_health_watchdog.py
foreman/flows/e2e_flow_orchestrator.py
foreman/scripts/run-self-test.py
foreman/runtime/task_manager.py
```

### Test-side UTC references

These belong to the separately governed A2-T lane and may not be touched by the
A2-R runtime builder:

```text
tests/**
```

## Repair classification

- Change type: import-only
- Permitted semantic action: add the minimal missing `UTC` import to the exact
  files above
- Prohibited actions: refactor, behaviour change, test edits, marker changes,
  fixture changes, assertion changes, dependency/workflow/environment changes

## Required evidence for A2-R

1. Static file-by-file proof that each changed runtime file previously
   referenced `UTC` without importing it.
2. Import-only changed-file proof.
3. Focused execution proof for the affected owning surfaces.
4. Rerun proof for the frozen broad populations downstream of the lane.

## Foreman disposition

```text
A2-R runtime inventory: COMPLETE
Authority surface separation from A2-T: COMPLETE
Proposed builder role: api-builder
Builder write scope: runtime files above + dedicated evidence paths only
Integration builder: NOT APPOINTED
Merge authority: NOT GRANTED
```
