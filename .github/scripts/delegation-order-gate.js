#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const repoRoot = process.cwd();
const workflowSha = process.env.GITHUB_SHA || '';
const prHeadSha = process.env.PR_HEAD_SHA || workflowSha;
const prBaseSha = process.env.PR_BASE_SHA || '';
const controlPath = path.join(repoRoot, '.agent-admin/control/delegation-order.json');
const implementationPathPattern = /^(modules\/amc\/src\/|apps\/[^/]+\/src\/|packages\/[^/]+\/src\/|supabase\/functions\/|api\/|lib\/)/;
const implementationTestPattern = /(^|\/)(__tests__|tests?)\/|\.(test|spec)\.(ts|tsx|js|jsx)$/;
const stopAndFixGuidance = [
  'STOP_AND_FIX: AMC delegation order could not be proven.',
  'Required order: canonical IAA pre-brief commit -> builder appointment commit -> first implementation commit.',
  'Same-commit proof is not accepted.',
  'Record/commit IAA pre-brief and builder appointment before implementation, or obtain explicit CS2 waiver.',
  'Do not proceed to handover.'
].join(' ');

function fail(message) { console.error(`::error::${message}`); process.exitCode = 1; }
function warn(message) { console.warn(`::warning::${message}`); }
function runGit(args) { return execFileSync('git', args, { cwd: repoRoot, encoding: 'utf8' }).trim(); }
function getChangedFiles() {
  if (process.env.CHANGED_FILES && process.env.CHANGED_FILES.trim()) return process.env.CHANGED_FILES.split(/\r?\n/).map(s => s.trim()).filter(Boolean);
  if (prBaseSha && prHeadSha) {
    try { return runGit(['diff', '--name-only', `${prBaseSha}...${prHeadSha}`]).split(/\r?\n/).map(s => s.trim()).filter(Boolean); }
    catch (e) { warn(`Could not diff PR base/head: ${e.message}`); }
  }
  try { return runGit(['diff', '--name-only', 'HEAD~1', 'HEAD']).split(/\r?\n/).map(s => s.trim()).filter(Boolean); }
  catch (e) { warn(`Could not determine changed files: ${e.message}`); return []; }
}
function readJson(filePath) { try { return JSON.parse(fs.readFileSync(filePath, 'utf8')); } catch (e) { fail(`Cannot read valid JSON from ${path.relative(repoRoot, filePath)}: ${e.message}`); return null; } }
function commitExists(sha) { try { runGit(['cat-file', '-e', `${sha}^{commit}`]); return true; } catch { return false; } }
function isAncestor(a, d) { try { execFileSync('git', ['merge-base', '--is-ancestor', a, d], { cwd: repoRoot }); return true; } catch { return false; } }
function isStrictAncestor(a, d) { return a !== d && isAncestor(a, d); }
function firstImplementationCommit(files) {
  if (!prBaseSha || !prHeadSha || files.length === 0) return '';
  try { return runGit(['log', '--reverse', '--format=%H', `${prBaseSha}..${prHeadSha}`, '--', ...files]).split(/\r?\n/).filter(Boolean)[0] || ''; }
  catch (e) { warn(`Could not determine first implementation commit: ${e.message}`); return ''; }
}
function validIso(value) { return typeof value === 'string' && value.trim() && Number.isFinite(Date.parse(value)); }
function validate(control, firstImpl) {
  const errors = [];
  const required = ['schema_version','wave_id','pr_number','prebrief_commit_sha','builder_appointment_timestamp','builder_appointment_commit_sha','builder_agent','builder_task_ref','first_implementation_commit_sha','qp_review_timestamp','result'];
  for (const key of required) if (!(key in control)) errors.push(`missing required key: ${key}`);
  if (control.schema_version !== '1.0.0') errors.push('schema_version must be 1.0.0');
  if (control.result !== 'DELEGATION_ORDER_VERIFIED') errors.push('result must be DELEGATION_ORDER_VERIFIED');
  if (!validIso(control.builder_appointment_timestamp)) errors.push('builder_appointment_timestamp must be ISO date-time');
  if (!validIso(control.qp_review_timestamp)) errors.push('qp_review_timestamp must be ISO date-time');
  for (const field of ['prebrief_commit_sha','builder_appointment_commit_sha','first_implementation_commit_sha']) {
    const value = control[field];
    if (typeof value !== 'string' || !/^[a-f0-9]{40}$/.test(value)) errors.push(`${field} must be a 40-character lowercase commit SHA`);
    else if (!commitExists(value)) errors.push(`${field} does not resolve to a commit: ${value}`);
  }
  if (control.prebrief_commit_sha === control.builder_appointment_commit_sha) errors.push('prebrief and builder appointment commits must differ');
  if (control.builder_appointment_commit_sha === control.first_implementation_commit_sha) errors.push('builder appointment and first implementation commits must differ');
  if (firstImpl && control.first_implementation_commit_sha !== firstImpl) errors.push(`first_implementation_commit_sha must equal detected first implementation commit ${firstImpl}`);
  if (control.prebrief_commit_sha && control.builder_appointment_commit_sha && !isStrictAncestor(control.prebrief_commit_sha, control.builder_appointment_commit_sha)) errors.push('prebrief_commit_sha must be a strict ancestor of builder_appointment_commit_sha');
  if (control.builder_appointment_commit_sha && control.first_implementation_commit_sha && !isStrictAncestor(control.builder_appointment_commit_sha, control.first_implementation_commit_sha)) errors.push('builder_appointment_commit_sha must be a strict ancestor of first_implementation_commit_sha');
  if (control.first_implementation_commit_sha && prHeadSha && !isAncestor(control.first_implementation_commit_sha, prHeadSha)) errors.push('first_implementation_commit_sha must be an ancestor of current PR head');
  return errors;
}
function stop(code=1){ console.error(`::error::${stopAndFixGuidance}`); process.exit(code); }

const changedFiles = getChangedFiles();
const implementationFiles = changedFiles.filter(f => implementationPathPattern.test(f) || implementationTestPattern.test(f));
console.log('=== AMC Builder Delegation Order Gate ===');
console.log(`PR head SHA: ${prHeadSha || 'unknown'}`);
console.log(`PR base SHA: ${prBaseSha || 'unknown'}`);
console.log(`Changed files: ${changedFiles.length}`);
console.log(`Implementation files changed: ${implementationFiles.length}`);
if (implementationFiles.length === 0) { console.log('No implementation-like files changed. Delegation order gate passes.'); process.exit(0); }
const firstImpl = firstImplementationCommit(implementationFiles);
if (!firstImpl) { fail('Implementation files changed but first implementation commit could not be determined.'); stop(process.exitCode || 1); }
if (!fs.existsSync(controlPath)) { fail('Missing .agent-admin/control/delegation-order.json while implementation files changed.'); warn(`implementation files changed: ${implementationFiles.slice(0,20).join(', ')}`); warn(`detected first implementation commit: ${firstImpl}`); stop(process.exitCode || 1); }
const control = readJson(controlPath); if (!control) stop(process.exitCode || 1);
const errors = validate(control, firstImpl);
if (errors.length) { console.error('Delegation order gate failed:'); errors.forEach(e => console.error(`- ${e}`)); warn(`implementation files changed: ${implementationFiles.slice(0,20).join(', ')}`); warn(`detected first implementation commit: ${firstImpl}`); stop(1); }
console.log('Delegation order gate passed.');
