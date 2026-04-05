# =============================================================================
# Fix agent-bootstrap setup in AMC:
#   1. Create .github/workflows/agent-bootstrap-inject.yml (correct location)
#   2. Update mcp-servers/agent-bootstrap/agent-ids.js (AMC agent list)
#   3. Delete mcp-servers/agent-bootstrap/agent-bootstrap-inject.yml (wrong location)
# =============================================================================

param(
    [string]$Pat        = $env:GH_PAT,
    [string]$TargetRepo = "APGI-cmy/app_management_centre"
)

if (-not $Pat) {
    Write-Error "GH_PAT environment variable not set."
    exit 1
}

$headers = @{
    Authorization          = "Bearer $Pat"
    Accept                 = "application/vnd.github+json"
    "X-GitHub-Api-Version" = "2022-11-28"
}

function Get-FileShaIfExists($repo, $path) {
    try {
        $url = "https://api.github.com/repos/$repo/contents/$($path -replace ' ','%20')"
        $r   = Invoke-RestMethod -Uri $url -Headers $headers -Method Get
        return $r.sha
    } catch { return $null }
}

function Push-File($repo, $path, $content, $message, $existingSha) {
    $url     = "https://api.github.com/repos/$repo/contents/$($path -replace ' ','%20')"
    $encoded = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($content))
    $body    = @{ message = $message; content = $encoded }
    if ($existingSha) { $body.sha = $existingSha }
    Invoke-RestMethod -Uri $url -Headers $headers -Method Put -Body ($body | ConvertTo-Json -Depth 5) -ContentType "application/json"
}

function Delete-File($repo, $path, $sha, $message) {
    $url  = "https://api.github.com/repos/$repo/contents/$($path -replace ' ','%20')"
    $body = @{ message = $message; sha = $sha } | ConvertTo-Json
    Invoke-RestMethod -Uri $url -Headers $headers -Method Delete -Body $body -ContentType "application/json"
}

# =============================================================================
# FILE CONTENTS
# =============================================================================

$workflowContent = @'
name: Agent Bootstrap Inject

# Fires on every new issue or PR opened in AMC.
# Posts a mandatory agent_bootstrap preflight instruction as the first comment.
# Skipping agent_bootstrap is a GOV-BREACH-AIMC-W5-002 POLC violation.

on:
  issues:
    types: [opened]
  pull_request:
    types: [opened]

permissions:
  issues: write
  pull-requests: write

jobs:
  inject-bootstrap-instruction:
    runs-on: ubuntu-latest
    steps:
      - name: Determine agent ID from assignees or title
        id: detect
        env:
          ASSIGNEES: ${{ toJson(github.event.issue.assignees || github.event.pull_request.assignees) }}
          TITLE: ${{ github.event.issue.title || github.event.pull_request.title }}
        run: |
          AGENT_IDS=(
            "CodexAdvisor-agent"
            "foreman-v2-agent"
            "governance-liaison-amc-agent"
            "independent-assurance-agent"
            "api-builder"
            "qa-builder"
            "schema-builder"
            "ui-builder"
            "integration-builder"
          )

          DETECTED_ID=""
          for id in "${AGENT_IDS[@]}"; do
            if echo "$ASSIGNEES $TITLE" | grep -qi "$id"; then
              DETECTED_ID="$id"
              break
            fi
          done

          if [ -z "$DETECTED_ID" ]; then
            DETECTED_ID="<your-agent-id>"
          fi

          echo "agent_id=$DETECTED_ID" >> "$GITHUB_OUTPUT"

      - name: Post agent_bootstrap instruction comment
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.MATURION_BOT_TOKEN }}
          script: |
            const agentId = '${{ steps.detect.outputs.agent_id }}';
            const body = [
              '## ⚠️ AGENT PREFLIGHT REQUIRED — CALL `agent_bootstrap` FIRST',
              '',
              '**Before reading this issue/PR body, before reading any repository file, call:**',
              '',
              '```',
              `agent_bootstrap(agent_id: "${agentId}")`,
              '```',
              '',
              'This is your **required first tool call** in every session. Skipping is a **GOV-BREACH-AIMC-W5-002 POLC violation** and will cause your PR to be blocked by the CI preflight gate.',
              '',
              'The `agent_bootstrap` tool is provided by the `agent-bootstrap` MCP server registered in `.mcp.json`. It returns your full agent contract file. Read it in full and complete **Phase 1 (Identity & Preflight)** before doing anything else.',
              '',
              '---',
              '',
              '**Authority**: CS2 (@APGI-cmy) — agent contract Phase 1, `agent-bootstrap` MCP server.',
            ].join('\n');

            const isIssue = context.eventName === 'issues';
            if (isIssue) {
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: context.issue.number,
                body,
              });
            } else {
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: context.payload.pull_request.number,
                body,
              });
            }
'@

$agentIdsContent = @'
"use strict";

/**
 * Required governed agent IDs — AMC consumer repo.
 *
 * These are the agent contracts that MUST exist in .github/agents/
 * for the agent-bootstrap server to start without warnings.
 * The npm test suite (test-bootstrap.js) asserts all of these are present.
 *
 * Update this list when a new mandatory agent contract is added to AMC.
 */
const REQUIRED_AGENT_IDS = [
  "CodexAdvisor-agent",
  "foreman-v2-agent",
  "governance-liaison-amc-agent",
  "independent-assurance-agent",
  "api-builder",
  "qa-builder",
  "schema-builder",
  "ui-builder",
  "integration-builder",
];

module.exports = { REQUIRED_AGENT_IDS };
'@

# =============================================================================
# EXECUTE
# =============================================================================

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Fix agent-bootstrap setup — AMC" -ForegroundColor Cyan
Write-Host "  Repo: $TargetRepo" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

$commitMsg = "CS2 Direct: Fix agent-bootstrap setup — correct workflow location + AMC agent-ids"

# ── 1. Create workflow in correct location ────────────────────────────────────
Write-Host "[1/3] Creating .github/workflows/agent-bootstrap-inject.yml" -ForegroundColor Yellow
try {
    $existingSha = Get-FileShaIfExists -repo $TargetRepo -path ".github/workflows/agent-bootstrap-inject.yml"
    $action      = if ($existingSha) { "UPDATE" } else { "CREATE" }
    Push-File -repo $TargetRepo -path ".github/workflows/agent-bootstrap-inject.yml" `
              -content $workflowContent -message $commitMsg -existingSha $existingSha
    Write-Host "      ✅ $action — .github/workflows/agent-bootstrap-inject.yml" -ForegroundColor Green
} catch {
    Write-Host "      ❌ FAILED: $($_.Exception.Message)" -ForegroundColor Red
}

Start-Sleep -Milliseconds 500

# ── 2. Update agent-ids.js with full AMC agent list ───────────────────────────
Write-Host "[2/3] Updating mcp-servers/agent-bootstrap/agent-ids.js" -ForegroundColor Yellow
try {
    $existingSha = Get-FileShaIfExists -repo $TargetRepo -path "mcp-servers/agent-bootstrap/agent-ids.js"
    Push-File -repo $TargetRepo -path "mcp-servers/agent-bootstrap/agent-ids.js" `
              -content $agentIdsContent -message $commitMsg -existingSha $existingSha
    Write-Host "      ✅ UPDATE — mcp-servers/agent-bootstrap/agent-ids.js" -ForegroundColor Green
} catch {
    Write-Host "      ❌ FAILED: $($_.Exception.Message)" -ForegroundColor Red
}

Start-Sleep -Milliseconds 500

# ── 3. Delete misplaced workflow file ─────────────────────────────────────────
Write-Host "[3/3] Deleting mcp-servers/agent-bootstrap/agent-bootstrap-inject.yml (wrong location)" -ForegroundColor Yellow
try {
    $sha = Get-FileShaIfExists -repo $TargetRepo -path "mcp-servers/agent-bootstrap/agent-bootstrap-inject.yml"
    if ($sha) {
        Delete-File -repo $TargetRepo -path "mcp-servers/agent-bootstrap/agent-bootstrap-inject.yml" `
                    -sha $sha -message "CS2 Direct: Remove misplaced workflow file from mcp-servers/ (moved to .github/workflows/)"
        Write-Host "      ✅ DELETED — mcp-servers/agent-bootstrap/agent-bootstrap-inject.yml" -ForegroundColor Green
    } else {
        Write-Host "      ℹ️  File not found — already deleted or never existed" -ForegroundColor Gray
    }
} catch {
    Write-Host "      ❌ FAILED: $($_.Exception.Message)" -ForegroundColor Red
}

# =============================================================================
# SUMMARY
# =============================================================================

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  DONE" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "After this runs:" -ForegroundColor White
Write-Host "  ✅ .github/workflows/agent-bootstrap-inject.yml — ACTIVE (fires on every new issue/PR)" -ForegroundColor Green
Write-Host "  ✅ mcp-servers/agent-bootstrap/agent-ids.js — all 9 AMC agents listed" -ForegroundColor Green
Write-Host "  ✅ mcp-servers/agent-bootstrap/agent-bootstrap-inject.yml — removed (was inert)" -ForegroundColor Green
Write-Host ""
Write-Host "You are now ready to open the first governed issue in AMC." -ForegroundColor Cyan
Write-Host ""
