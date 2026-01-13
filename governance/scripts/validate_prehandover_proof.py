#!/usr/bin/env python3
"""
Validation script for PREHANDOVER_PROOF documents.

This script validates that a PREHANDOVER_PROOF document contains all required
sections and evidence for the Execution Bootstrap Protocol (v2.0.0+).

Usage:
    python3 governance/scripts/validate_prehandover_proof.py <path-to-proof-file>
    
Exit Codes:
    0 - Validation passed
    1 - Validation failed
    2 - File not found or invalid
"""

import sys
import re
from pathlib import Path


def check_section_exists(content: str, section_name: str) -> bool:
    """Check if a section exists in the content."""
    pattern = rf"##\s+{re.escape(section_name)}"
    return bool(re.search(pattern, content, re.IGNORECASE))


def check_exit_codes(content: str) -> tuple[bool, list[str]]:
    """Check if exit codes are documented and all are 0."""
    errors = []
    warnings = []
    
    # Look for exit code patterns
    exit_code_patterns = [
        r"exit code[:\s]+(\d+)",
        r"Exit Code[:\s]+(\d+)",
        r"exitcode[:\s]+(\d+)",
        r"return code[:\s]+(\d+)",
    ]
    
    import re
    found_exit_codes = []
    
    for pattern in exit_code_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            code = int(match.group(1))
            found_exit_codes.append(code)
    
    if not found_exit_codes:
        warnings.append("No exit codes documented (Step 3 may be incomplete)")
    else:
        # Check if all exit codes are 0
        non_zero_codes = [code for code in found_exit_codes if code != 0]
        if non_zero_codes:
            errors.append(f"Non-zero exit codes found: {non_zero_codes} (All must be 0)")
    
    return len(errors) == 0, errors + warnings


def check_evidence_completeness(content: str) -> tuple[bool, list[str]]:
    """Check if evidence collection is complete (Step 4)."""
    errors = []
    
    # Required evidence elements
    evidence_markers = [
        ("execution logs", "Execution logs or command outputs"),
        ("timestamp", "Timestamps for execution"),
        ("output", "Command outputs or results"),
    ]
    
    missing_evidence = []
    for marker, description in evidence_markers:
        if marker not in content.lower():
            missing_evidence.append(description)
    
    if missing_evidence:
        errors.append(
            f"Evidence collection (Step 4) incomplete. Missing: {', '.join(missing_evidence)}"
        )
    
    return len(errors) == 0, errors


def check_category_0_complete(content: str) -> tuple[bool, list[str]]:
    """Check if Category 0 (7-step protocol) is complete."""
    errors = []
    
    # Check for Category 0 section
    if not check_section_exists(content, "Category 0: Execution Bootstrap Protocol"):
        errors.append("Missing 'Category 0: Execution Bootstrap Protocol' section")
        return False, errors
    
    # Check for all 7 steps
    steps = [
        "Step 1: Identify Execution Artifacts",
        "Step 2: Local Execution",
        "Step 3: Validate Exit Codes",
        "Step 4: Evidence Collection",
        "Step 5: Failure Remediation",
        "Step 6: Green Attestation",
        "Step 7: Handover Authorization",
    ]
    
    for step in steps:
        if not check_section_exists(content, step):
            errors.append(f"Missing '{step}' section")
    
    # Check for critical attestations
    if "All checks GREEN" not in content:
        errors.append("Missing 'All checks GREEN' attestation")
    
    if "Handover authorized" not in content:
        errors.append("Missing 'Handover authorized' statement")
    
    if "CI is confirmation, NOT diagnostic" not in content:
        errors.append("Missing hard rule acknowledgment: 'CI is confirmation, NOT diagnostic'")
    
    # Check exit codes (Step 3)
    exit_codes_valid, exit_code_errors = check_exit_codes(content)
    if not exit_codes_valid:
        errors.extend(exit_code_errors)
    
    # Check evidence completeness (Step 4)
    evidence_valid, evidence_errors = check_evidence_completeness(content)
    if not evidence_valid:
        errors.extend(evidence_errors)
    
    return len(errors) == 0, errors


def check_agent_attestation(content: str) -> tuple[bool, list[str]]:
    """Check if agent attestation section exists."""
    errors = []
    
    if not check_section_exists(content, "Agent Attestation"):
        errors.append("Missing 'Agent Attestation' section")
    
    return len(errors) == 0, errors


def check_metadata(content: str) -> tuple[bool, list[str]]:
    """Check if required metadata exists."""
    errors = []
    
    required_fields = [
        "Agent:",
        "PR:",
        "Branch:",
        "Date:",
        "Latest Commit:",
        "Protocol Version:",
    ]
    
    for field in required_fields:
        if field not in content:
            errors.append(f"Missing required field: {field}")
    
    # Check protocol version
    if "Protocol Version:" in content:
        if "2.0.0" not in content:
            errors.append("Protocol version must be 2.0.0 or higher")
    
    return len(errors) == 0, errors


def validate_prehandover_proof(file_path: Path) -> tuple[bool, list[str]]:
    """
    Validate a PREHANDOVER_PROOF document.
    
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    if not file_path.exists():
        return False, [f"File not found: {file_path}"]
    
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return False, [f"Error reading file: {e}"]
    
    all_errors = []
    
    # Check metadata
    metadata_valid, metadata_errors = check_metadata(content)
    if not metadata_valid:
        all_errors.extend(metadata_errors)
    
    # Check if this is an execution-related PR (Category 0 applicable)
    # If "N/A" is explicitly stated for Category 0, skip detailed validation
    if "Category 0:" in content and "N/A" in content.split("Category 0:")[1].split("\n")[0]:
        print("Category 0 marked as N/A - skipping 7-step validation")
    else:
        # Check Category 0 completeness
        category_0_valid, category_0_errors = check_category_0_complete(content)
        if not category_0_valid:
            all_errors.extend(category_0_errors)
    
    # Check agent attestation
    attestation_valid, attestation_errors = check_agent_attestation(content)
    if not attestation_valid:
        all_errors.extend(attestation_errors)
    
    return len(all_errors) == 0, all_errors


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate PREHANDOVER_PROOF documents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s PREHANDOVER_PROOF_PR_123.md
    %(prog)s --verbose PREHANDOVER_PROOF.md
    %(prog)s --json PREHANDOVER_PROOF.md

Exit Codes:
    0 - Validation passed
    1 - Validation failed
    2 - File not found or invalid
        """
    )
    
    parser.add_argument(
        "file",
        help="Path to PREHANDOVER_PROOF file to validate"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show detailed validation information"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format"
    )
    
    args = parser.parse_args()
    file_path = Path(args.file)
    
    if not args.json:
        print(f"Validating PREHANDOVER_PROOF: {file_path}")
        print("-" * 60)
    
    is_valid, errors = validate_prehandover_proof(file_path)
    
    if args.json:
        import json
        result = {
            "file": str(file_path),
            "valid": is_valid,
            "errors": errors,
            "error_count": len(errors)
        }
        print(json.dumps(result, indent=2))
    elif is_valid:
        print("✅ VALIDATION PASSED")
        print("\nPREHANDOVER_PROOF is complete and valid.")
        if args.verbose:
            print("\nAll required sections present:")
            print("  ✓ Metadata (Agent, PR, Branch, Date, Commit, Protocol Version)")
            print("  ✓ Category 0: Execution Bootstrap Protocol (7 steps)")
            print("  ✓ Agent Attestation")
            print("  ✓ Exit codes validated (all 0)")
            print("  ✓ Evidence collection complete")
    else:
        print("❌ VALIDATION FAILED")
        print(f"\nErrors found ({len(errors)}):")
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")
        print("\nPlease fix these issues before handover.")
        if args.verbose:
            print("\nValidation checklist:")
            print("  • Ensure all 7 steps of Category 0 are documented")
            print("  • All exit codes must be 0 (success)")
            print("  • Evidence must include: logs, timestamps, outputs")
            print("  • Required attestations: 'All checks GREEN', 'Handover authorized'")
            print("  • Hard rule: 'CI is confirmation, NOT diagnostic'")
    
    if not args.json:
        print()
    
    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
