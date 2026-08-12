#!/usr/bin/env node
/**
 * Bootstrap Diagnostic Tool
 * 
 * CLI tool for debugging MCP bootstrap availability and agent configuration.
 * Run this to probe your local setup and identify bootstrap issues.
 * 
 * Usage:
 *   node .github/scripts/bootstrap-diagnostic.js [--json]
 * 
 * Options:
 *   --json         Output as JSON (instead of human-readable text)
 *   --agent <id>   Check specific agent contract (e.g., --agent ui-builder)
 * 
 * Authority: Issue #1228 Phase 1 (agent-bootstrap diagnostics)
 */

"use strict";

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const REPO_ROOT = process.cwd();
const args = process.argv.slice(2);
const jsonOutput = args.includes("--json");
const agentFilter = args.includes("--agent")
  ? args[args.indexOf("--agent") + 1]
  : null;

// Color output helpers (disabled in JSON mode)
const colors = {
  reset: jsonOutput ? "" : "\x1b[0m",
  red: jsonOutput ? "" : "\x1b[31m",
  green: jsonOutput ? "" : "\x1b[32m",
  yellow: jsonOutput ? "" : "\x1b[33m",
  blue: jsonOutput ? "" : "\x1b[34m",
  dim: jsonOutput ? "" : "\x1b[2m",
};

/**
 * Main diagnostic routine
 */
async function runDiagnostics() {
  const diagnostics = {
    timestamp: new Date().toISOString(),
    repo_root: REPO_ROOT,
    checks: {},
    summary: {
      total_checks: 0,
      passed: 0,
      failed: 0,
      warnings: 0,
    },
  };

  const progress = jsonOutput
    ? (msg) => process.stderr.write(msg + "\n")
    : (msg) => console.log(msg);

  // Check 1: .mcp.json exists and is valid
  progress(`${colors.blue}[CHECK 1]${colors.reset} Verifying .mcp.json...`);
  const mcpCheck = checkMCPConfig();
  diagnostics.checks.mcp_config = mcpCheck;
  diagnostics.summary.total_checks++;
  if (mcpCheck.status === "pass") diagnostics.summary.passed++;
  else if (mcpCheck.status === "warn") diagnostics.summary.warnings++;
  else diagnostics.summary.failed++;

  // Check 2: agent-bootstrap server is registered
  progress(
    `${colors.blue}[CHECK 2]${colors.reset} Verifying agent-bootstrap server registration...`
  );
  const bootstrapCheck = checkBootstrapServer(mcpCheck.data?.config);
  diagnostics.checks.bootstrap_server = bootstrapCheck;
  diagnostics.summary.total_checks++;
  if (bootstrapCheck.status === "pass") diagnostics.summary.passed++;
  else if (bootstrapCheck.status === "warn") diagnostics.summary.warnings++;
  else diagnostics.summary.failed++;

  // Check 3: .github/agents directory and contracts
  progress(`${colors.blue}[CHECK 3]${colors.reset} Scanning agent contracts...`);
  const agentsCheck = checkAgentContracts(agentFilter);
  diagnostics.checks.agent_contracts = agentsCheck;
  diagnostics.summary.total_checks++;
  if (agentsCheck.status === "pass") diagnostics.summary.passed++;
  else if (agentsCheck.status === "warn") diagnostics.summary.warnings++;
  else diagnostics.summary.failed++;

  // Check 4: Required agent IDs from agent-ids.js
  progress(`${colors.blue}[CHECK 4]${colors.reset} Verifying required agents...`);
  const requiredCheck = checkRequiredAgents(agentsCheck.data?.contracts || [], agentFilter);
  diagnostics.checks.required_agents = requiredCheck;
  diagnostics.summary.total_checks++;
  if (requiredCheck.status === "pass") diagnostics.summary.passed++;
  else if (requiredCheck.status === "warn") diagnostics.summary.warnings++;
  else diagnostics.summary.failed++;

  // Check 5: MCP server startup test (non-blocking)
  progress(`${colors.blue}[CHECK 5]${colors.reset} Testing MCP server startup...`);
  const mcpStartupCheck = testMCPStartup();
  diagnostics.checks.mcp_startup = mcpStartupCheck;
  diagnostics.summary.total_checks++;
  if (mcpStartupCheck.status === "pass") diagnostics.summary.passed++;
  else if (mcpStartupCheck.status === "warn") diagnostics.summary.warnings++;
  else diagnostics.summary.failed++;

  // Check 6: Fallback instructions available
  progress(`${colors.blue}[CHECK 6]${colors.reset} Verifying fallback instructions...`);
  const fallbackCheck = checkFallbackInstructions();
  diagnostics.checks.fallback_instructions = fallbackCheck;
  diagnostics.summary.total_checks++;
  if (fallbackCheck.status === "pass") diagnostics.summary.passed++;
  else if (fallbackCheck.status === "warn") diagnostics.summary.warnings++;
  else diagnostics.summary.failed++;

  // Output results
  if (jsonOutput) {
    process.stdout.write(JSON.stringify(diagnostics, null, 2) + "\n");
  } else {
    console.log();
    printSummary(diagnostics);
  }

  process.exit(diagnostics.summary.failed > 0 ? 1 : 0);
}

/**
 * Check 1: Verify .mcp.json
 */
function checkMCPConfig() {
  const mcpPath = path.join(REPO_ROOT, ".mcp.json");
  try {
    if (!fs.existsSync(mcpPath)) {
      return {
        status: "fail",
        message: ".mcp.json not found",
        data: { path: mcpPath },
      };
    }
    const config = JSON.parse(fs.readFileSync(mcpPath, "utf8"));
    return {
      status: "pass",
      message: ".mcp.json valid",
      data: { path: mcpPath, config },
    };
  } catch (err) {
    return {
      status: "fail",
      message: `.mcp.json invalid: ${err.message}`,
      data: { path: mcpPath, error: err.message },
    };
  }
}

/**
 * Check 2: Verify agent-bootstrap server registration
 */
function checkBootstrapServer(mcpConfig) {
  if (!mcpConfig || !mcpConfig.mcpServers) {
    return {
      status: "fail",
      message: "MCP config missing mcpServers",
      data: {},
    };
  }
  const bootstrapServer = mcpConfig.mcpServers["agent-bootstrap"];
  if (!bootstrapServer) {
    return {
      status: "fail",
      message: "agent-bootstrap server not registered",
      data: { registered_servers: Object.keys(mcpConfig.mcpServers) },
    };
  }
  return {
    status: "pass",
    message: "agent-bootstrap server registered",
    data: { server: bootstrapServer },
  };
}

/**
 * Check 3: Scan .github/agents directory
 */
function checkAgentContracts(agentFilter) {
  const agentsDir = path.join(REPO_ROOT, ".github", "agents");
  try {
    if (!fs.existsSync(agentsDir)) {
      return {
        status: "fail",
        message: ".github/agents directory not found",
        data: { path: agentsDir },
      };
    }
    let contracts = fs
      .readdirSync(agentsDir)
      .filter((f) => f.endsWith(".md") && !f.startsWith("_"))
      .sort();
    if (agentFilter) {
      contracts = contracts.filter((f) => f === `${agentFilter}.md`);
    }
    if (contracts.length === 0) {
      return {
        status: "fail",
        message: agentFilter
          ? `No contract found for agent: ${agentFilter}`
          : "No agent contracts found in .github/agents",
        data: { path: agentsDir, count: 0 },
      };
    }
    return {
      status: "pass",
      message: `Found ${contracts.length} agent contract(s)`,
      data: { path: agentsDir, contracts, count: contracts.length },
    };
  } catch (err) {
    return {
      status: "fail",
      message: `Could not scan .github/agents: ${err.message}`,
      data: { path: agentsDir, error: err.message },
    };
  }
}

/**
 * Check 4: Verify required agents from agent-ids.js
 */
function checkRequiredAgents(discoveredContracts, agentFilter) {
  try {
    // Load required agents from mcp-servers/agent-bootstrap/agent-ids.js
    const agentIdsPath = path.join(
      REPO_ROOT,
      "mcp-servers/agent-bootstrap/agent-ids.js"
    );
    if (!fs.existsSync(agentIdsPath)) {
      return {
        status: "warn",
        message: "Cannot verify required agents (agent-ids.js not found)",
        data: {},
      };
    }

    // Simple parse of REQUIRED_AGENT_IDS array
    const content = fs.readFileSync(agentIdsPath, "utf8");
    const match = content.match(/REQUIRED_AGENT_IDS\s*=\s*\[([\s\S]*?)\]/);
    if (!match) {
      return {
        status: "warn",
        message: "Cannot parse REQUIRED_AGENT_IDS",
        data: {},
      };
    }

    const requiredIds = match[1]
      .split(",")
      .map((s) => s.trim().replace(/['"]/g, ""))
      .filter((s) => s.length > 0);

    const filteredRequired = agentFilter
      ? requiredIds.filter((id) => id === agentFilter)
      : requiredIds;

    const contractIds = discoveredContracts.map((f) => f.replace(/\.md$/, ""));
    const missing = filteredRequired.filter((id) => !contractIds.includes(id));

    if (missing.length > 0) {
      return {
        status: "warn",
        message: `Missing required agent contracts: ${missing.join(", ")}`,
        data: { required: filteredRequired, found: contractIds, missing },
      };
    }

    return {
      status: "pass",
      message: `All ${filteredRequired.length} required agents present`,
      data: { required: filteredRequired, found: contractIds },
    };
  } catch (err) {
    return {
      status: "warn",
      message: `Could not verify required agents: ${err.message}`,
      data: { error: err.message },
    };
  }
}

/**
 * Check 5: Test MCP server startup
 */
function testMCPStartup() {
  try {
    const bootstrapScript = path.join(
      REPO_ROOT,
      "mcp-servers/agent-bootstrap/index.js"
    );
    if (!fs.existsSync(bootstrapScript)) {
      return {
        status: "fail",
        message: "agent-bootstrap MCP server script not found",
        data: { path: bootstrapScript },
      };
    }

    // Try to load the script (Node.js syntax check)
    // Note: We don't actually run it (would hang waiting for stdin)
    try {
      execSync(`node --check "${bootstrapScript}"`, { stdio: "ignore" });
      return {
        status: "warn",
        message:
          "Bootstrap server file exists (full test requires MCP client context)",
        data: { path: bootstrapScript },
      };
    } catch (err) {
      // Script may have require errors; this is expected without full MCP context
      if (err.message.includes("McpServer")) {
        return {
          status: "warn",
          message:
            "Bootstrap server requires MCP SDK (expected in runtime context)",
          data: { path: bootstrapScript },
        };
      }
      return {
        status: "warn",
        message: `Bootstrap server has issue: ${err.message}`,
        data: { path: bootstrapScript, error: err.message },
      };
    }
  } catch (err) {
    return {
      status: "warn",
      message: `Could not test MCP startup: ${err.message}`,
      data: { error: err.message },
    };
  }
}

/**
 * Check 6: Fallback instructions available
 */
function checkFallbackInstructions() {
  const fallbackPath = path.join(
    REPO_ROOT,
    ".github/scripts/agent-bootstrap-fallback-instructions.md"
  );
  try {
    if (!fs.existsSync(fallbackPath)) {
      return {
        status: "fail",
        message: "Fallback instructions not found",
        data: { path: fallbackPath },
      };
    }
    const content = fs.readFileSync(fallbackPath, "utf8");
    if (content.length === 0) {
      return {
        status: "warn",
        message: "Fallback instructions file is empty",
        data: { path: fallbackPath },
      };
    }
    return {
      status: "pass",
      message: "Fallback instructions available",
      data: { path: fallbackPath, size: content.length },
    };
  } catch (err) {
    return {
      status: "fail",
      message: `Could not read fallback instructions: ${err.message}`,
      data: { path: fallbackPath, error: err.message },
    };
  }
}

/**
 * Print human-readable summary
 */
function printSummary(diagnostics) {
  console.log(`${colors.blue}=== Bootstrap Diagnostics Summary ===${colors.reset}`);
  console.log(
    `Repository: ${diagnostics.repo_root}`
  );
  console.log(
    `Timestamp: ${diagnostics.timestamp}\n`
  );

  const { total_checks, passed, failed, warnings } = diagnostics.summary;
  const statusColor = failed > 0 ? colors.red : warnings > 0 ? colors.yellow : colors.green;
  console.log(
    `${statusColor}Total: ${total_checks} | Pass: ${passed} | Fail: ${failed} | Warn: ${warnings}${colors.reset}\n`
  );

  for (const [checkName, check] of Object.entries(diagnostics.checks)) {
    const statusIcon =
      check.status === "pass"
        ? `${colors.green}✓${colors.reset}`
        : check.status === "warn"
        ? `${colors.yellow}⚠${colors.reset}`
        : `${colors.red}✗${colors.reset}`;
    console.log(`${statusIcon} ${checkName.toUpperCase()}`);
    console.log(`  ${check.message}`);
    if (check.data && Object.keys(check.data).length > 0) {
      console.log(`  ${colors.dim}${JSON.stringify(check.data)}${colors.reset}`);
    }
    console.log();
  }

  if (failed === 0 && warnings === 0) {
    console.log(
      `${colors.green}All checks passed. Bootstrap is ready.${colors.reset}`
    );
  } else if (failed === 0) {
    console.log(
      `${colors.yellow}Some warnings detected. Check the details above.${colors.reset}`
    );
  } else {
    console.log(
      `${colors.red}Bootstrap issues detected. See failures above.${colors.reset}`
    );
  }
}

// Main execution
runDiagnostics();
