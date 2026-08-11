#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const repoRoot = process.cwd();
const manifestPath = path.join(repoRoot, '.agent-admin/control/merge-gate-required-checks.json');
function fail(message) {
  console.error(`::error::${message}`);
  process.exitCode = 1;
}
function listFiles(dir, results = []) {
  if (!fs.existsSync(dir)) return results;
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, item.name);
    if (item.isDirectory()) listFiles(full, results);
    else results.push(full);
  }
  return results;
}
function workflowJobNames() {
  const workflowDir = path.join(repoRoot, '.github/workflows');
  const files = listFiles(workflowDir).filter((file) => file.endsWith('.yml') || file.endsWith('.yaml'));
  const names = new Set();
  for (const file of files) {
    const lines = fs.readFileSync(file, 'utf8').split(/\r?\n/);
    for (const line of lines) {
      const match = line.match(/^\s{4,}name:\s*["']?([^"'#]+)["']?/);
      if (match && match[1]) names.add(match[1].trim());
    }
  }
  return names;
}
function checkMCPAvailability() {
  // Probe MCP bootstrap availability for diagnostic logging (non-blocking)
  try {
    const detectionModulePath = path.join(repoRoot, '.github/scripts/detect-mcp-bootstrap-availability.js');
    if (!fs.existsSync(detectionModulePath)) {
      console.log('::notice::MCP detection module not found (expected in Phase 1 implementation)');
      return { available: null, reason: 'detection_module_missing' };
    }

    const mcpConfigPath = path.join(repoRoot, '.mcp.json');
    if (!fs.existsSync(mcpConfigPath)) {
      console.log('::warning::MCP config (.mcp.json) not found — agents will use fallback path');
      return { available: false, reason: 'mcp_config_missing' };
    }

    let mcpConfig;
    try {
      mcpConfig = JSON.parse(fs.readFileSync(mcpConfigPath, 'utf8'));
    } catch (err) {
      console.log('::warning::MCP config is invalid JSON — agents will use fallback path');
      return { available: false, reason: 'mcp_config_invalid' };
    }

    if (!mcpConfig.mcpServers || !mcpConfig.mcpServers['agent-bootstrap']) {
      console.log('::warning::agent-bootstrap MCP server not registered — agents will use fallback path');
      return { available: false, reason: 'bootstrap_server_not_registered' };
    }

    const agentsDir = path.join(repoRoot, '.github', 'agents');
    if (!fs.existsSync(agentsDir)) {
      console.log('::warning::.github/agents directory not found — MCP server cannot function');
      return { available: false, reason: 'agents_dir_missing' };
    }

    const contracts = fs.readdirSync(agentsDir).filter((f) => f.endsWith('.md') && !f.startsWith('_'));
    if (contracts.length === 0) {
      console.log('::warning::No agent contracts found — MCP server has no data');
      return { available: false, reason: 'no_agent_contracts' };
    }

    console.log(`::notice::MCP bootstrap server is available (${contracts.length} agent contracts)`);
    return { available: true, reason: 'mcp_server_ready', contract_count: contracts.length };
  } catch (err) {
    console.log(`::warning::Could not probe MCP availability: ${err.message}`);
    return { available: null, reason: 'probe_error', error: err.message };
  }
}
console.log('=== AMC Merge Gate Required Checks Alignment (Issue #1228 Phase 1) ===');

// Diagnostic: Check MCP availability (non-blocking)
console.log('');
console.log('Checking MCP bootstrap availability...');
const mcpStatus = checkMCPAvailability();
console.log(`MCP Status: ${mcpStatus.available === true ? 'AVAILABLE' : mcpStatus.available === false ? 'UNAVAILABLE' : 'UNKNOWN'} (${mcpStatus.reason})`);
console.log('');

if (!fs.existsSync(manifestPath)) {
  fail('Missing .agent-admin/control/merge-gate-required-checks.json');
  process.exit(1);
}
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
const required = manifest.required_checks || [];
const workflowBacked = manifest.workflow_backed_required_checks || [];
if (required.length === 0) fail('required_checks must not be empty');
for (const check of new Set(required)) {
  if (required.filter((candidate) => candidate === check).length > 1) fail(`Duplicate required check: ${check}`);
}
for (const check of workflowBacked) {
  if (!required.includes(check)) fail(`workflow-backed check is not listed in required_checks: ${check}`);
}
const liveJobs = workflowJobNames();
for (const check of workflowBacked) {
  if (!liveJobs.has(check)) fail(`Workflow-backed required check has no matching live workflow job name: ${check}`);
}
console.log(`Required checks: ${required.length}`);
console.log(`Workflow-backed checks: ${workflowBacked.length}`);
console.log(`Live workflow job names: ${liveJobs.size}`);

// Additional diagnostic context for fallback path
if (mcpStatus.available === false) {
  console.log('');
  console.log('::notice::MCP unavailable — agents will receive fallback instruction comments');
  console.log('::notice::Merge gate will log fallback attestations for CS2 post-facto review');
}

if (process.exitCode) process.exit(1);
console.log('');
console.log('Merge gate required checks alignment passed.');

