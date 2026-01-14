# QIW Builder Quickstart Guide

**Version**: 1.0.0  
**Date**: 2026-01-14  
**Authority**: WATCHDOG_QUALITY_INTEGRITY_CHANNEL.md v1.0.0  
**Audience**: All Builder Agents (api-builder, qa-builder, ui-builder, schema-builder, integration-builder)

---

## What is QIW?

**QIW (Quality Integrity Watchdog)** is an observational channel within the Independent Watchdog system that monitors **5 quality channels** to ensure log integrity before QA is allowed to pass.

**Purpose**: Prevent false positives in QA by detecting silent warnings, failures, and anomalies in build artifacts.

**Authority**: Canonical governance (WATCHDOG_QUALITY_INTEGRITY_CHANNEL.md v1.0.0, effective 2026-01-13)

---

## The 5 QIW Channels

### 1. Build Log Monitoring (QIW-1)
**Watches**: Build command execution logs, compiler output, build system warnings

**Detection Patterns**:
- **Critical**: `Build failed`, `Compilation error`, `Fatal error`
- **Error**: `ERROR`, `TypeError`, `Failed to compile`, `Cannot find module`
- **Warning**: `WARNING`, `Deprecated`, `Module not found` (non-fatal)

**Builder Action**: Verify build logs are clean (no errors/warnings) before handover

### 2. Lint Log Monitoring (QIW-2)
**Watches**: Lint command execution logs, ESLint/TSLint/ruff output

**Detection Patterns**:
- **Critical**: Linter crash, configuration error
- **Error**: `error` (lint severity), `✖` marker, rule violations
- **Warning**: `warning` (lint severity), `⚠` marker, deprecated API usage

**Builder Action**: Verify lint logs are clean (no violations) before handover

### 3. Test Log Monitoring (QIW-3)
**Watches**: Test runner execution logs, test results, runtime errors

**Detection Patterns**:
- **Critical**: Test runner crash, all tests failing
- **Error**: `FAIL`, `✖`, `Error:`, assertion failures
- **Warning**: `SKIP`, `⊘`, `.only`/`.skip` markers, coverage below threshold

**Builder Action**: Verify test logs are clean (no skipped tests, no runtime errors) before handover

### 4. Deployment Simulation Monitoring (QIW-4)
**Watches**: `next build`, `next start`, deployment build logs

**Detection Patterns**:
- **Critical**: Deployment build failure, server start failure
- **Error**: `Build error`, `Failed to start`, route errors, API failures
- **Warning**: Environment variable warnings, performance warnings

**Builder Action**: Verify deployment simulation logs clean (if applicable) before handover

### 5. Runtime Initialization Monitoring (QIW-5)
**Watches**: Application initialization logs, service startup sequences

**Detection Patterns**:
- **Critical**: Application crash during initialization, fatal errors
- **Error**: `Initialization error`, `Failed to connect`, component failures
- **Warning**: Slow initialization, retry attempts, fallback modes

**Builder Action**: Verify runtime initialization logs clean (if applicable) before handover

---

## QIW Blocking Conditions

### Automatic QA Blocking

QA is **automatically blocked** when ANY of the following conditions are detected:

**Critical Severity** (Always Blocks):
- Build failure, test runner crash, deployment failure, server start failure, linter crash

**Error Severity** (Always Blocks):
- Build succeeds but errors logged (silent failures)
- Lint errors present
- Test failures or runtime errors during tests
- Deployment errors (route errors, API failures)
- Runtime initialization errors (component failures)

**Warning Severity** (Blocks per Zero-Warning Discipline):
- Build warnings present
- Lint warnings present (unless whitelisted)
- Skipped tests or suppressed tests (`.skip`, `.only`)
- Deployment warnings
- Runtime initialization warnings

**Info Severity** (Does Not Block):
- Informational messages, performance metrics, health check successes

---

## How to Verify QIW Status

### Before Handover Checklist

**In Pre-Handover Execution Protocol (Step 2), verify:**

```bash
# 1. Build logs clean
npm run build  # or relevant build command
# Check output: No ERROR, WARNING, or FAIL messages

# 2. Lint logs clean
npm run lint   # or ruff check .
# Check output: No errors or warnings

# 3. Test logs clean
pytest tests/ -v
# Check output: All tests pass, no skipped, no runtime errors

# 4. Deployment simulation (if applicable)
next build && next start
# Check output: Build succeeds, server starts, no errors

# 5. Runtime initialization (if applicable)
# Check application startup logs for errors
```

### Pre-Handover Checklist Items

**QIW Channel Verification (v1.0.0):**
- [ ] Build logs verified clean (no errors/warnings)
- [ ] Lint logs verified clean (no violations)
- [ ] Test logs verified clean (no skipped tests, no runtime errors)
- [ ] Deployment simulation logs clean (if applicable)
- [ ] Runtime initialization logs clean (if applicable)
- [ ] No QA blocking conditions detected
- [ ] All anomalies recorded to governance memory (if any)

---

## How to Whitelist Warnings

**Scenario**: QIW detects a warning, but it's benign and cannot be fixed immediately.

**Process**:
1. **Document the warning** in your Pre-Handover Proof
2. **Justify why it's benign** (e.g., third-party library, known issue with workaround)
3. **Request whitelisting** via governance liaison
4. **Governance liaison reviews** and approves/rejects
5. **If approved**, warning is whitelisted in project QIW configuration

**Whitelisting Criteria**:
- Warning cannot be resolved immediately (external dependency)
- Warning has no functional impact
- Workaround is documented and tested
- Removal plan exists (target date for fix)

**Prohibited**: Blanket whitelisting, permanent whitelisting without plan

---

## Common Patterns and Fixes

### Pattern 1: Silent Build Warnings

**Symptom**: Build succeeds (exit code 0) but warnings logged

**Fix**:
1. Identify warning source (deprecation, unused variable, etc.)
2. Fix warning at source (upgrade API, remove unused code)
3. Re-run build, verify clean output
4. Document fix in Pre-Handover Proof

**QIW Role**: QIW detects silent warnings that exit code misses

### Pattern 2: Skipped Tests

**Symptom**: Tests pass but some marked `.skip` or `.only`

**Fix**:
1. Remove `.skip` or `.only` markers
2. Fix failing tests (update assertions, mock data)
3. Re-run tests, verify all pass
4. Document fix in Pre-Handover Proof

**QIW Role**: QIW detects test debt (skipped tests = incomplete QA)

### Pattern 3: Runtime Errors in Tests

**Symptom**: Tests pass but runtime errors logged during execution

**Fix**:
1. Identify error source (unhandled exception, missing cleanup)
2. Add error handling or cleanup logic
3. Re-run tests, verify no runtime errors
4. Document fix in Pre-Handover Proof

**QIW Role**: QIW detects runtime errors that test framework ignores

### Pattern 4: Deployment Warnings

**Symptom**: Deployment succeeds but environment variable warnings logged

**Fix**:
1. Identify missing environment variables
2. Add to `.env` or configuration
3. Re-run deployment simulation, verify clean
4. Document fix in Pre-Handover Proof

**QIW Role**: QIW detects deployment issues before production

---

## Governance Memory Integration

### When to Record Anomalies

**Record to governance memory when**:
- Critical or error anomalies detected (always)
- Warning anomalies detected (if not whitelisted)
- Anomaly represents systemic issue (not one-off)

**Do NOT record**:
- Info-level messages (not anomalies)
- Already-whitelisted warnings (no governance gap)

### What to Record

**Incident Structure** (QualityIntegrityIncident schema):
```json
{
  "whatFailed": "Description of what failed",
  "where": "File/line or component location",
  "why": "Root cause analysis",
  "recommendedFix": "Actionable fix suggestion",
  "missingArchitectureRule": "Governance gap identified",
  "channel": "build | lint | test | deployment_simulation | runtime_initialization",
  "severity": "critical | error | warning | info",
  "timestamp": "ISO8601",
  "buildSequenceId": "Build/PR identifier",
  "projectId": "Project/repo identifier",
  "metadata": {
    "commitSha": "...",
    "branch": "...",
    "environment": "...",
    "anomalyContext": ["Surrounding log lines"]
  }
}
```

**Memory Location**: `memory/{projectId}/qiw-events.json` (or global)

**Builder Responsibility**: Document anomalies in Pre-Handover Proof (governance memory write is automatic)

---

## Dashboard Visibility (When Available)

**QIW Dashboard** (when implemented) will show:
- **Real-time Status**: GREEN (no anomalies) / AMBER (warnings) / RED (errors/critical)
- **Per-channel Status**: Build, Lint, Test, Deployment, Runtime
- **Recent Anomalies**: Last 10 anomalies with severity and message
- **Trends**: 7-day anomaly count, quality improvement trend

**Dashboard API**: Programmatic access for FM/builders to check QIW status

**Until dashboard ready**: Builders verify QIW manually (check logs per channel)

---

## FAQ

### Q1: Do I need to verify all 5 channels for every PR?

**A**: Verify all **applicable** channels. Not all PRs touch deployment or runtime initialization. Use judgment:
- **Always**: Build, Lint, Test (mandatory for all PRs)
- **If applicable**: Deployment simulation (if code affects deployment)
- **If applicable**: Runtime initialization (if code affects startup)

### Q2: What if QIW blocks me but I can't fix it?

**A**: Escalate to governance liaison with justification. Options:
1. Fix the issue (preferred)
2. Request whitelisting (with plan to fix later)
3. Escalate to FM (if governance gap identified)

### Q3: Does QIW replace existing checks?

**A**: No, QIW **extends** existing checks. You still run:
- BL-026 deprecation check (`ruff check --select UP`)
- Test execution protocol (pytest, coverage)
- Lint checks (ruff, ESLint)

QIW adds **log verification** to ensure those checks didn't produce silent warnings.

### Q4: What if exit code is 0 but QIW detects errors?

**A**: Exit code success is insufficient. QIW enforces **log integrity**:
- Exit code 0 + clean logs = TRUE success
- Exit code 0 + errors in logs = SILENT FAILURE (QIW blocks)

This is QIW's core value: catching what exit codes miss.

### Q5: How do I know if QIW is blocking?

**A**: Until dashboard is ready, check manually:
1. Review build/lint/test logs for ERROR/WARNING/FAIL patterns
2. If detected, QIW would block (treat as blocked)
3. Fix anomalies before handover
4. Document verification in Pre-Handover Proof

### Q6: Does QIW apply to documentation-only PRs?

**A**: No. QIW applies to code changes (build/lint/test affected). Documentation-only PRs can skip QIW verification (state "Documentation-only PR - QIW not applicable" in Pre-Handover Proof).

---

## Quick Reference Card

**QIW = 5 Channels**:
1. Build logs → Clean (no errors/warnings)
2. Lint logs → Clean (no violations)
3. Test logs → Clean (no skipped/runtime errors)
4. Deployment logs → Clean (if applicable)
5. Runtime logs → Clean (if applicable)

**QIW Blocking**: Critical/Error/Warning anomalies block QA (zero-warning discipline)

**Builder Action**: Verify all channels clean before handover, document in Pre-Handover Proof

**Escalation**: Governance liaison → FM → Johan (if governance gap)

**Authority**: WATCHDOG_QUALITY_INTEGRITY_CHANNEL.md v1.0.0 (canonical)

---

**END OF QIW BUILDER QUICKSTART GUIDE**

For full specification, see: https://github.com/APGI-cmy/maturion-foreman-governance/blob/main/governance/canon/WATCHDOG_QUALITY_INTEGRITY_CHANNEL.md
