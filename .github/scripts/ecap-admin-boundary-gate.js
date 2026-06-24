#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const repoRoot = process.cwd();
const prBaseSha = process.env.PR_BASE_SHA || '';
const prHeadSha = process.env.PR_HEAD_SHA || process.env.GITHUB_SHA || '';
const outputPatterns = [/^\.agent-admin\/ecap\//, /^\.agent-admin\/prehandover\/ecap-/i];
const contractPath = '.github/agents/execution-ceremony-admin-agent.md';
const claimWords = ['merge ready', 'ready for review', 'build ready', 'production ready', 'assurance pass', 'approved for merge', 'substantive readiness', 'quality pass'];
const safeWords = ['never', 'must not', 'cannot', 'not authorized', 'outside', 'invalid', 'admin-only', 'administrative only'];
const requiredFalse = ['substantive_readiness_judgment_made','iaa_invoked_by_ecap','foreman_qp_judgment_rewritten'];
function fail(message) { console.error(`::error::${message}`); process.exitCode = 1; }
function read(file) { try { return fs.readFileSync(path.join(repoRoot, file), 'utf8'); } catch { return ''; } }
function git(args) { return execFileSync('git', args, { cwd: repoRoot, encoding: 'utf8' }).trim(); }
function changedFiles() {
  if (process.env.CHANGED_FILES && process.env.CHANGED_FILES.trim()) return process.env.CHANGED_FILES.split(/\r?\n/).map((line) => line.trim()).filter(Boolean);
  if (prBaseSha && prHeadSha) {
    try { return git(['diff', '--name-only', `${prBaseSha}...${prHeadSha}`]).split(/\r?\n/).filter(Boolean); } catch (_error) {}
  }
  try { return git(['diff', '--name-only', 'HEAD~1', 'HEAD']).split(/\r?\n/).filter(Boolean); } catch { return []; }
}
function lineHasOperativeClaim(line) {
  const lower = line.toLowerCase();
  return claimWords.some((word) => lower.includes(word)) && !safeWords.some((word) => lower.includes(word));
}
const files = changedFiles();
const outputs = files.filter((file) => outputPatterns.some((pattern) => pattern.test(file)));
console.log('=== AMC ECAP Admin Boundary Gate ===');
console.log(`Changed files: ${files.length}`);
console.log(`ECAP output files changed: ${outputs.length}`);
for (const file of outputs) {
  const content = read(file);
  if (content.split(/\r?\n/).some(lineHasOperativeClaim)) fail(`${file} contains operative readiness or assurance language reserved for other roles.`);
  if (/\.json$/i.test(file)) {
    try {
      const parsed = JSON.parse(content);
      for (const key of requiredFalse) if (parsed[key] !== false) fail(`${file}: ${key} must be false for ECAP admin validation.`);
    } catch (error) { fail(`${file} is invalid JSON: ${error.message}`); }
  }
}
if (files.includes(contractPath)) {
  const contract = read(contractPath).toLowerCase();
  const requiredConcepts = [
    ['administrative'],
    ['never issues', 'never issue'],
    ['substantive quality'],
    ['appoints builders', 'appoint builders'],
    ['never invokes iaa', 'invoke iaa']
  ];
  for (const options of requiredConcepts) {
    if (!options.some((phrase) => contract.includes(phrase))) fail(`${contractPath} must preserve ECAP boundary concept: ${options.join(' or ')}`);
  }
}
if (process.exitCode) process.exit(1);
console.log('ECAP admin boundary gate passed.');
