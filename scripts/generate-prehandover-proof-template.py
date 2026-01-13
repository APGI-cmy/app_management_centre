#!/usr/bin/env python3
"""
PREHANDOVER_PROOF Template Generator

Purpose: Generate a skeleton PREHANDOVER_PROOF document with all required sections
Authority: Execution Bootstrap Protocol v2.0.0+, Wave 3.2
Usage: python3 scripts/generate-prehandover-proof-template.py [OPTIONS]

Exit Codes:
    0 - Template generated successfully
    1 - Generation failed
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime


def generate_template(
    agent: str = "Builder Name",
    pr_number: str = "PR_NUMBER",
    branch: str = "feature/your-branch",
    wave: str = "Wave X.Y",
    category_0_applicable: bool = True
) -> str:
    """Generate PREHANDOVER_PROOF template content"""
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    template = f"""# PREHANDOVER_PROOF - {wave}

**Agent**: {agent}  
**PR**: #{pr_number}  
**Branch**: {branch}  
**Date**: {date_str}  
**Latest Commit**: [COMMIT_SHA]  
**Protocol Version**: 2.0.0+  
**Execution Protocol**: Execution Bootstrap Protocol v2.0.0+

---

## Executive Summary

[Provide a brief summary of the work completed, key achievements, and readiness for handover]

**Key Deliverables**:
- ✅ [Deliverable 1]
- ✅ [Deliverable 2]
- ✅ [Deliverable 3]

**Quality Metrics**:
- Tests: [N] tests, 100% passing
- Coverage: [Coverage metrics]
- Technical Debt: Zero
- Deprecations: Zero (BL-026 compliant)

---

"""

    if category_0_applicable:
        template += """## Category 0: Execution Bootstrap Protocol (v2.0.0+)

### Step 1: Identify Execution Artifacts

**Artifacts Created/Modified**:
1. **[Artifact Name]** - [Description]
   - Type: [workflow/script/config/gate]
   - Path: [path/to/artifact]
   - Purpose: [What it does]

2. **[Artifact Name]** - [Description]
   - Type: [workflow/script/config/gate]
   - Path: [path/to/artifact]
   - Purpose: [What it does]

**Total Artifacts**: [N]

---

### Step 2: Local Execution

**Execution Environment**:
- OS: [Linux/macOS/Windows]
- Python: [Version]
- Tools: [List relevant tools]

**Artifacts Executed Locally**:

#### Artifact 1: [Name]
```bash
# Command executed
[command]

# Execution date/time
[timestamp]

# Execution successful: YES
```

#### Artifact 2: [Name]
```bash
# Command executed
[command]

# Execution date/time
[timestamp]

# Execution successful: YES
```

**All artifacts executed successfully locally**: ✅ YES

---

### Step 3: Validate Exit Codes

| Artifact | Command | Exit Code | Status |
|----------|---------|-----------|--------|
| [Name 1] | `[command]` | 0 | ✅ PASS |
| [Name 2] | `[command]` | 0 | ✅ PASS |
| [Name 3] | `[command]` | 0 | ✅ PASS |

**All exit codes are 0**: ✅ YES

**Exit Code Validation**:
- Total artifacts: [N]
- Exit code 0: [N]
- Non-zero codes: 0

---

### Step 4: Evidence Collection

**Evidence Artifacts**:

1. **Execution Logs**
   - Location: [path or inline below]
   - Format: [text/json/artifact]
   - Timestamp: [timestamp]

2. **Exit Codes**
   - Documented in Step 3 table
   - All verified as 0

3. **Command Outputs**
   - [Include relevant outputs inline or reference artifacts]

**Evidence Package**:
```
[Paste relevant logs, outputs, or link to GitHub Actions artifacts]
```

**Evidence Completeness**: ✅ COMPLETE

---

### Step 5: Failure Remediation

**Initial Execution**:
- Failures detected: [YES/NO]
- Count: [N or 0]

**Remediation Actions** (if applicable):
[If no failures, state "No failures detected. No remediation required."]

1. **Issue**: [Description]
   - Root Cause: [Cause]
   - Fix Applied: [Fix description]
   - Re-execution Result: ✅ PASS

**All failures remediated**: ✅ YES  
**Re-execution after fixes**: ✅ ALL GREEN

---

### Step 6: Green Attestation

**Final Execution Status**:

✅ **All checks GREEN on latest commit**: `[COMMIT_SHA]`

**Checks Performed**:
- ✅ [Check 1: Description]
- ✅ [Check 2: Description]
- ✅ [Check 3: Description]
- ✅ [Check N: Description]

**Green Confirmation**:
- Execution artifacts: ✅ GREEN
- Exit codes: ✅ ALL 0
- Evidence: ✅ COMPLETE
- Remediation: ✅ COMPLETE (or N/A)

---

### Step 7: Handover Authorization

**Handover Status**: ✅ AUTHORIZED

**Authorization Statement**:
> All checks GREEN. All execution artifacts validated locally with exit code 0.
> Evidence collected and documented. No failures outstanding.
> **Handover authorized** for PR #{pr_number}.

**Hard Rule Acknowledgment**:
> ✅ **CI is confirmation, NOT diagnostic**.
> Local execution completed successfully. CI will confirm, not discover issues.

**Authorizing Agent**: {agent}  
**Date**: {date_str}  
**Commit**: `[COMMIT_SHA]`

---

"""
    else:
        template += """## Category 0: Execution Bootstrap Protocol

**Status**: N/A

**Rationale**: This PR does not involve execution artifacts (workflows, scripts, gates, configs).  
Changes are limited to: [Specify what changed - e.g., documentation, architecture specs, non-executable configs]

**No execution validation required**.

---

"""

    template += f"""## Agent Attestation

**Agent**: {agent}  
**Date**: {date_str}  
**Commit**: `[COMMIT_SHA]`

### Attestation Statement

I, {agent}, attest that:

1. ✅ **Scope Conformance**: All work completed aligns with frozen architecture and QA specifications
2. ✅ **Quality Standards**: All tests passing, zero technical debt, zero warnings
3. ✅ **Execution Protocol**: Category 0 requirements {"fully satisfied" if category_0_applicable else "N/A (non-executable changes)"}
4. ✅ **Exit Codes**: {"All execution artifacts validated with exit code 0" if category_0_applicable else "N/A"}
5. ✅ **Evidence**: {"Complete evidence collected and documented" if category_0_applicable else "N/A"}
6. ✅ **Local Validation**: {"All checks passed locally before handover" if category_0_applicable else "Changes reviewed and validated"}
7. ✅ **CI Semantics**: Understood - CI is confirmation, not diagnostic
8. ✅ **Handover Ready**: Work complete, validated, and ready for FM review

### Constitutional Compliance

- ✅ Zero Test Debt Constitutional Rule: Compliant
- ✅ One-Time Build Correctness: Achieved
- ✅ Build Philosophy: Followed
- ✅ BL-026 Deprecation Detection: Compliant (if Python changes)

### Signature

**Agent**: {agent}  
**Date**: {date_str}  
**Protocol Version**: 2.0.0+

---

## Appendices

### Appendix A: Test Results
[Include test execution summary or link to test reports]

### Appendix B: Execution Logs
[Include or reference full execution logs]

### Appendix C: Evidence Artifacts
[Include or reference GitHub Actions artifacts, screenshots, etc.]

---

**END OF PREHANDOVER_PROOF**
"""

    return template


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Generate PREHANDOVER_PROOF template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s
    %(prog)s --agent "API Builder" --pr 123 --wave "Wave 3.2"
    %(prog)s --no-category-0 --output PREHANDOVER_PROOF_DOC_ONLY.md
        """
    )
    
    parser.add_argument(
        "--agent",
        default="Builder Name",
        help="Agent name (default: Builder Name)"
    )
    parser.add_argument(
        "--pr",
        default="PR_NUMBER",
        help="PR number (default: PR_NUMBER)"
    )
    parser.add_argument(
        "--branch",
        default="feature/your-branch",
        help="Branch name (default: feature/your-branch)"
    )
    parser.add_argument(
        "--wave",
        default="Wave X.Y",
        help="Wave identifier (default: Wave X.Y)"
    )
    parser.add_argument(
        "--no-category-0",
        action="store_true",
        help="Mark Category 0 as N/A (for non-executable changes)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: PREHANDOVER_PROOF_TEMPLATE.md)"
    )
    
    args = parser.parse_args()
    
    # Generate template
    template_content = generate_template(
        agent=args.agent,
        pr_number=args.pr,
        branch=args.branch,
        wave=args.wave,
        category_0_applicable=not args.no_category_0
    )
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = Path("PREHANDOVER_PROOF_TEMPLATE.md")
    
    # Write template
    try:
        output_path.write_text(template_content, encoding='utf-8')
        print(f"✅ PREHANDOVER_PROOF template generated: {output_path}")
        print()
        print("Next steps:")
        print(f"  1. Edit {output_path} and fill in all [PLACEHOLDERS]")
        print("  2. Execute all artifacts locally and capture evidence")
        print("  3. Document exit codes (must all be 0)")
        print("  4. Validate with: python3 governance/scripts/validate_prehandover_proof.py {output_path}")
        print()
        sys.exit(0)
    except Exception as e:
        print(f"❌ Failed to generate template: {e}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGeneration cancelled by user.")
        sys.exit(1)
