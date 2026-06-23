#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const repoRoot = process.cwd();

const outputPatterns = [/^\.agent-admin\/ecap\//, /^\.agent-admin\/prehandover\/ecap-/i, /ecap.*\.(md|json)$/i];
const guidancePatterns = [/^\.github\/agents\/execution-ceremony-admin-agent\.md$/, /^\.agent-admin\/control\//, /^governance\//];
const forbidden = /(merge[- ]ready|ready[- ]for[- ]review|build[- ]ready|production[- ]ready|assurance[- ]pass|approved for merge|substantive readiness|quality pass)/i;
const requiredFalse = ['substantive_readiness_judgment_made','iaa_invoked_by_ecap','foreman_qp_judgment_rewritten'];
function fail(m){ console.error(`::error::${m}`); process.exitCode = 1; }
function read(file){ try { return fs.readFileSync(path.join(repoRoot, file), 'utf8'); } catch { return ''; } }
function changedFiles(){ return (process.env.CHANGED_FILES || '').split(/\r?\n/).map(s=>s.trim()).filter(Boolean); }
function filesFromGit(){
  const { execFileSync } = require('child_process');
  try { return execFileSync('git',['diff','--name-only','HEAD~1','HEAD'],{encoding:'utf8'}).trim().split(/\r?\n/).filter(Boolean); } catch { return []; }
}
const files = changedFiles().length ? changedFiles() : filesFromGit();
const outputs = files.filter(f => outputPatterns.some(p => p.test(f)));
const guidance = files.filter(f => guidancePatterns.some(p => p.test(f)));
console.log('=== AMC ECAP Admin Boundary Gate ===');
console.log(`ECAP output files changed: ${outputs.length}`);
console.log(`ECAP guidance files changed: ${guidance.length}`);
for (const file of outputs) {
  const content = read(file);
  if (forbidden.test(content)) fail(`${file} contains readiness/assurance language reserved for Foreman/IAA/CS2.`);
  if (/\.json$/i.test(file)) {
    try {
      const parsed = JSON.parse(content);
      for (const key of requiredFalse) if (parsed[key] !== false) fail(`${file}: ${key} must be false for ECAP admin validation.`);
    } catch (e) { fail(`${file} is invalid JSON: ${e.message}`); }
  }
}
for (const file of guidance) {
  const content = read(file);
  if (/execution-ceremony-admin-agent\.md$/.test(file) && !/NEVER issue.*verdict|Administrator only|admin/i.test(content)) {
    fail(`${file} must preserve ECAP admin-only / no-verdict boundary language.`);
  }
}
if (process.exitCode) process.exit(1);
console.log('ECAP admin boundary gate passed.');
