# Wave Current Tasks — wave-opojd-delivery — Uninterrupted OPOJD Delivery (Issue #1024)

wave: wave-opojd-delivery
agent: foreman-v2-agent
session: session-020
date: 20260408
iaa_prebrief_path: .agent-admin/assurance/iaa-prebrief-wave-opojd-delivery.md
iaa_prebrief_status: COMMITTED — SHA 45eda17

## Wave Description

Align the repository to a strict comment-only Copilot model so that push errors cannot
derail a Copilot session and OPOJD delivery is uninterrupted. Required changes per
CS2 directive (Issue #1024):

1. Modify `.github/workflows/copilot-setup-steps.yml`:
   - Remove write-back assumptions from comments/instructions
   - Remove fallback token logic (`MATURION_BOT_TOKEN || github.token`) from checkout
   - Add preflight step declaring COMMENT_ONLY session mode before MCP startup

2. Add preflight environment declarations:
   - `COPILOT_SESSION_MODE=COMMENT_ONLY`
   - `PUSH_DISABLED_INTENTIONAL=true`
   - `OUTPUT_MODE=PR_COMMENT_OR_ARTIFACT`

3. Keep `.github/workflows/copilot-push-intercept.yml` unchanged (safety net)

4. Create new bot automation workflow for future full automation:
   - Explicit write permissions
   - No `github.token` fallback
   - Fail-fast if required secret unavailable
   - Proper artifact/failure logging

## Tasks (pending IAA Pre-Brief)

- [ ] TASK-OPOJD-01: Modify `.github/workflows/copilot-setup-steps.yml` — remove write-back, add COMMENT_ONLY preflight
- [ ] TASK-OPOJD-02: Create `.github/workflows/copilot-bot-automation.yml` — separate bot workflow for future automation

## Delegated To

- integration-builder: TASK-OPOJD-01, TASK-OPOJD-02 (pending IAA Pre-Brief response)

## Status: IN PROGRESS — IAA Pre-Brief pending
