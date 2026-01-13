# Git Hooks for Build-to-Green Enforcement

This directory contains Git hooks that enforce Build-to-Green semantics locally before code is committed.

## Constitutional Authority

These hooks implement:
- **Zero Test Debt Constitutional Rule**
- **Governance Supremacy Rule**
- **Build-to-Green Rule**

## Available Hooks

### pre-commit

Runs before every `git commit` to check for:

1. **Test Debt Detection**
   - Scans for test skip and focus patterns
   - Checks for TODO/FIXME markers in test files
   - Detects commented out tests
   - Identifies stub tests

2. **Staged File Validation**
   - Validates test files being committed
   - Prevents committing test debt

3. **Protected File Monitoring**
   - Warns when constitutional files are modified
   - Reminds about CS2 approval requirement

### pre-commit-deprecation (BL-026)

Runs on staged Python files to enforce modern Python patterns:

1. **Deprecated API Detection**
   - Scans staged Python files for deprecated APIs
   - Blocks commits with BL-026 violations
   - Provides auto-fix suggestions

2. **Common Violations Detected**
   - `datetime.utcnow()` → `datetime.now(timezone.utc)`
   - `datetime.utcfromtimestamp()` → `datetime.fromtimestamp(tz=timezone.utc)`
   - `typing.List[X]` → `list[X]` (Python 3.9+)
   - `typing.Dict[K,V]` → `dict[K,V]` (Python 3.9+)

**Authority**: BL-026 Automated Deprecation Detection Gate

### pre-push (BL-026 Full Scan)

Runs before `git push` to perform comprehensive validation:

1. **Full Repository Scan**
   - Scans ALL Python files (not just changed)
   - Ensures no deprecated APIs exist anywhere
   - Blocks push if violations found

2. **Comprehensive Coverage**
   - Validates entire Python codebase
   - Catches violations missed in commit-time checks
   - Final gate before code reaches remote

**Authority**: BL-026 Automated Deprecation Detection Gate, Wave 3.2

**Note**: This hook may take longer than pre-commit hooks as it scans all files.

## Installation

### Recommended: Use Installation Script (Wave 3.2)

```bash
# From repository root - Cross-platform automatic installation
./scripts/install-git-hooks.sh
```

This script will:
- Configure Git to use `.githooks/` directory (preferred method)
- Fallback to manual copying if needed
- Validate environment requirements (Python, ruff)
- Provide installation status and next steps

### Manual Installation Methods

#### Method 1: Configure Git Hooks Path (Recommended)

```bash
# Tell git to use .githooks as hooks directory
git config core.hooksPath .githooks
```

This will automatically use all hooks in `.githooks/` without manual copying.

#### Method 2: Manual Copy (Fallback)

```bash
# From repository root
cp .githooks/pre-commit .git/hooks/pre-commit
cp .githooks/pre-commit-deprecation .git/hooks/pre-commit-deprecation
cp .githooks/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit-deprecation
chmod +x .git/hooks/pre-push
```

### Validate Installation

```bash
# Check builder environment is ready
python3 scripts/validate-builder-environment.py
```

## Usage

Once installed, hooks run automatically:

```bash
# When you commit, hooks run automatically
git commit -m "Your commit message"

# Output will show enforcement checks:
🔍 Build-to-Green Enforcement: Pre-commit checks...

1. Checking for test debt...
✅ No test debt detected

2. Checking staged test files for violations...
✅ No violations in staged test files

3. Checking for protected file modifications...

✅ All pre-commit checks passed

# When you push, additional checks run:
git push origin your-branch

# Output will show:
🔍 Full BL-026 Deprecation Scan: Pre-push validation...

1. Scanning all Python files for BL-026 violations...
   Found 42 Python files to scan

2. Running full ruff deprecation detection...
✅ No deprecated APIs detected in 42 files

✅ All pre-push checks passed - Push authorized
```

## Bypass (NOT RECOMMENDED)

Bypassing hooks is **strongly discouraged** as it violates constitutional rules.

If absolutely necessary for emergency fixes:

```bash
git commit --no-verify -m "Emergency fix"
```

**WARNING**: Bypassing hooks may result in:
- CI/CD failures
- Merge blocks
- Governance violations
- Audit trail issues

**Only use in genuine emergencies with Owner approval.**

## Troubleshooting

### Hook not running

```bash
# Check hook is installed
ls -la .git/hooks/pre-commit

# Check hook is executable
chmod +x .git/hooks/pre-commit

# Verify git hooks path
git config core.hooksPath
```

### Python not found

Hooks require Python 3. Install Python 3 or update shebang in hook file.

### False positives

If hook incorrectly blocks commit:
1. Review the violation reported
2. Verify it's actually a false positive
3. Report issue if hook logic needs adjustment
4. DO NOT bypass without investigation

## Testing Hooks

Test hooks without committing:

```bash
# Run test debt detection manually
python3 foreman/scripts/detect-test-debt.py --test-dir tests

# Test pre-commit-deprecation hook (BL-026)
bash .githooks/pre-commit-deprecation

# Test pre-push hook (full scan)
bash .githooks/pre-push

# Validate builder environment
python3 scripts/validate-builder-environment.py

# Test BL-026 detection with ruff directly
ruff check --select UP path/to/file.py
```

## Maintenance

Hooks are maintained in `.githooks/` directory and version controlled.

Updates to enforcement logic should:
1. Update hook scripts in `.githooks/`
2. Update this README
3. Test thoroughly
4. Document changes

## Support

For issues or questions:
- See: `governance/policies/AUTOMATED_DEPRECATION_DETECTION_GATE.md` (BL-026)
- See: `foreman/governance/build-to-green-enforcement-spec.md`
- See: `foreman/governance/zero-test-debt-constitutional-rule.md`
- Run: `./scripts/install-git-hooks.sh` for installation help
- Run: `python3 scripts/validate-builder-environment.py` for environment validation
- Contact: Repository maintainers
