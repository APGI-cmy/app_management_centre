#!/usr/bin/env python3
"""
Validation script for evidence-based gate validation (BL-027/028).

This script validates that a PREHANDOVER_PROOF document contains complete
evidence for evidence-based validation mode as defined in the Evidence-Based
Validation Schema.

Usage:
    python3 governance/scripts/validate_evidence_based.py <path-to-proof-file> [gate-name]
    
Exit Codes:
    0 - Evidence-based validation complete and valid
    1 - Evidence-based validation incomplete or invalid
    2 - File not found or invalid
    3 - Not evidence-based validation (automated mode detected)
"""

import sys
import re
from pathlib import Path
from typing import Tuple, List


def check_evidence_based_mode(content: str) -> Tuple[bool, List[str]]:
    """Check if evidence-based validation mode is declared."""
    errors = []
    warnings = []
    
    # Look for explicit evidence-based mode declaration
    mode_patterns = [
        r"Validation Mode.*Evidence-Based",
        r"Validation Mode.*Manual",
        r"Mode.*Evidence-Based",
    ]
    
    found_mode = False
    for pattern in mode_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            found_mode = True
            break
    
    if not found_mode:
        warnings.append(
            "No explicit Evidence-Based validation mode declaration found. "
            "This may be automated validation mode."
        )
        return False, warnings
    
    return True, []


def check_reason(content: str, gate_section: str = None) -> Tuple[bool, List[str]]:
    """Check if reason for evidence-based validation is documented."""
    errors = []
    
    # Look for reason documentation
    reason_patterns = [
        r"\*\*Reason\*\*:",
        r"Reason:",
        r"Why evidence-based",
    ]
    
    section_to_check = gate_section if gate_section else content
    
    found_reason = False
    for pattern in reason_patterns:
        if re.search(pattern, section_to_check, re.IGNORECASE):
            found_reason = True
            break
    
    if not found_reason:
        errors.append(
            "Missing reason for evidence-based validation. "
            "MUST document why automated validation was not used."
        )
    
    return len(errors) == 0, errors


def check_method(content: str, gate_section: str = None) -> Tuple[bool, List[str]]:
    """Check if verification method is documented."""
    errors = []
    
    # Look for method documentation
    method_patterns = [
        r"\*\*Method\*\*:",
        r"Method:",
        r"Verification Method:",
        r"How verification was performed",
    ]
    
    section_to_check = gate_section if gate_section else content
    
    found_method = False
    for pattern in method_patterns:
        if re.search(pattern, section_to_check, re.IGNORECASE):
            found_method = True
            break
    
    if not found_method:
        errors.append(
            "Missing verification method. "
            "MUST document how manual verification was performed."
        )
    
    return len(errors) == 0, errors


def check_verification_steps(content: str, gate_section: str = None) -> Tuple[bool, List[str]]:
    """Check if verification steps are documented (minimum 3 steps)."""
    errors = []
    
    section_to_check = gate_section if gate_section else content
    
    # Look for verification steps section
    if not re.search(r"\*\*Verification Steps\*\*:", section_to_check, re.IGNORECASE):
        errors.append(
            "Missing 'Verification Steps' section. "
            "MUST document step-by-step verification process."
        )
        return False, errors
    
    # Extract verification steps section
    steps_match = re.search(
        r"\*\*Verification Steps\*\*:(.*?)(?:\*\*[A-Z]|\n\n|\Z)",
        section_to_check,
        re.IGNORECASE | re.DOTALL
    )
    
    if not steps_match:
        errors.append("Could not parse Verification Steps section")
        return False, errors
    
    steps_content = steps_match.group(1)
    
    # Count numbered steps
    step_matches = re.findall(r"^\s*\d+\.", steps_content, re.MULTILINE)
    
    if len(step_matches) < 3:
        errors.append(
            f"Insufficient verification steps documented. "
            f"Found {len(step_matches)}, minimum 3 required."
        )
    
    return len(errors) == 0, errors


def check_evidence_artifacts(content: str, gate_section: str = None) -> Tuple[bool, List[str]]:
    """Check if evidence artifacts are provided."""
    errors = []
    
    section_to_check = gate_section if gate_section else content
    
    # Look for evidence section
    if not re.search(r"\*\*Evidence\*\*:", section_to_check, re.IGNORECASE):
        errors.append(
            "Missing 'Evidence' section. "
            "MUST provide concrete evidence artifacts (logs, screenshots, outputs, etc.)."
        )
        return False, errors
    
    # Check for evidence markers
    evidence_markers = [
        r"Screenshot:",
        r"Log output:",
        r"File contents:",
        r"Git diff:",
        r"Command output:",
        r"API response:",
        r"```",  # Code block indicates evidence
    ]
    
    found_evidence = False
    for marker in evidence_markers:
        if re.search(marker, section_to_check, re.IGNORECASE):
            found_evidence = True
            break
    
    if not found_evidence:
        errors.append(
            "No evidence artifacts found. "
            "MUST include at least one concrete evidence artifact."
        )
    
    return len(errors) == 0, errors


def check_findings(content: str, gate_section: str = None) -> Tuple[bool, List[str]]:
    """Check if findings are documented with compliance status."""
    errors = []
    
    section_to_check = gate_section if gate_section else content
    
    # Look for findings section
    if not re.search(r"\*\*Findings\*\*:", section_to_check, re.IGNORECASE):
        errors.append(
            "Missing 'Findings' section. "
            "MUST document verification findings with compliance status."
        )
        return False, errors
    
    # Look for compliance markers
    compliance_markers = [
        r"✅.*COMPLIANT",
        r"PASS",
        r"✅.*PASS",
        r"Status.*✅",
    ]
    
    found_compliance = False
    for marker in compliance_markers:
        if re.search(marker, section_to_check, re.IGNORECASE):
            found_compliance = True
            break
    
    if not found_compliance:
        errors.append(
            "No compliance status markers found in Findings. "
            "MUST mark requirements as COMPLIANT/NON-COMPLIANT."
        )
    
    return len(errors) == 0, errors


def check_attestation(content: str, gate_section: str = None) -> Tuple[bool, List[str]]:
    """Check if agent attestation is present."""
    errors = []
    
    section_to_check = gate_section if gate_section else content
    
    # Look for attestation section
    if not re.search(r"\*\*Attestation\*\*:", section_to_check, re.IGNORECASE):
        errors.append(
            "Missing 'Attestation' section. "
            "Agent MUST attest to verification accuracy and completeness."
        )
        return False, errors
    
    # Look for attestation statement
    attestation_keywords = [
        r"I.*attest",
        r"I.*certify",
        r"I.*confirm",
    ]
    
    found_attestation = False
    for keyword in attestation_keywords:
        if re.search(keyword, section_to_check, re.IGNORECASE):
            found_attestation = True
            break
    
    if not found_attestation:
        errors.append(
            "Attestation statement not found. "
            "MUST include personal attestation statement (e.g., 'I attest that...')."
        )
    
    # Look for date
    if not re.search(r"\*\*Date\*\*:", section_to_check, re.IGNORECASE):
        errors.append("Attestation missing date timestamp")
    
    # Look for confidence level
    if not re.search(r"Verification Confidence", section_to_check, re.IGNORECASE):
        errors.append("Attestation missing verification confidence level")
    
    return len(errors) == 0, errors


def extract_gate_sections(content: str) -> List[Tuple[str, str]]:
    """Extract individual gate sections from PREHANDOVER_PROOF."""
    # Look for gate sections (### Gate: ...)
    gate_pattern = r"###\s+(?:Gate:?\s+)?([^\n]+)"
    
    gates = []
    matches = list(re.finditer(gate_pattern, content))
    
    for i, match in enumerate(matches):
        gate_name = match.group(1).strip()
        start_pos = match.end()
        
        # Find end of this section (next ### or end of document)
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(content)
        
        section_content = content[start_pos:end_pos]
        gates.append((gate_name, section_content))
    
    return gates


def validate_evidence_based(file_path: Path, specific_gate: str = None) -> Tuple[bool, List[str]]:
    """
    Validate evidence-based validation in PREHANDOVER_PROOF.
    
    Args:
        file_path: Path to PREHANDOVER_PROOF file
        specific_gate: Optional specific gate name to validate
    
    Returns:
        Tuple of (is_valid, list_of_errors_or_warnings)
    """
    if not file_path.exists():
        return False, [f"File not found: {file_path}"]
    
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return False, [f"Error reading file: {e}"]
    
    all_errors = []
    all_warnings = []
    
    # Check if this is evidence-based validation
    is_evidence_based, mode_messages = check_evidence_based_mode(content)
    
    if not is_evidence_based:
        # Not evidence-based mode - this is OK, just not applicable
        return True, ["Not evidence-based validation mode (automated validation detected)"]
    
    # Extract gate sections
    gate_sections = extract_gate_sections(content)
    
    if not gate_sections:
        # No gate sections found - check entire document
        gate_sections = [("General", content)]
    
    # If specific gate requested, filter
    if specific_gate:
        gate_sections = [(name, section) for name, section in gate_sections 
                        if specific_gate.lower() in name.lower()]
        
        if not gate_sections:
            return False, [f"Gate '{specific_gate}' not found in PREHANDOVER_PROOF"]
    
    # Validate each gate section that uses evidence-based validation
    evidence_based_gates = []
    
    for gate_name, gate_section in gate_sections:
        # Check if this gate section uses evidence-based validation
        if not re.search(r"Validation Mode.*Evidence-Based", gate_section, re.IGNORECASE):
            continue
        
        evidence_based_gates.append(gate_name)
        
        print(f"\n📋 Validating evidence-based validation for gate: {gate_name}")
        print("=" * 70)
        
        gate_errors = []
        
        # Check all required components
        checks = [
            ("Reason", check_reason),
            ("Method", check_method),
            ("Verification Steps", check_verification_steps),
            ("Evidence Artifacts", check_evidence_artifacts),
            ("Findings", check_findings),
            ("Attestation", check_attestation),
        ]
        
        for check_name, check_func in checks:
            valid, messages = check_func(content, gate_section)
            if not valid:
                gate_errors.extend([f"[{gate_name}] {msg}" for msg in messages])
                print(f"  ❌ {check_name}: INCOMPLETE")
                for msg in messages:
                    print(f"     - {msg}")
            else:
                print(f"  ✅ {check_name}: COMPLETE")
        
        if gate_errors:
            all_errors.extend(gate_errors)
    
    if not evidence_based_gates:
        return True, ["No evidence-based validation gates found (all gates use automated validation)"]
    
    print("\n" + "=" * 70)
    if all_errors:
        print(f"❌ Evidence-based validation INCOMPLETE ({len(all_errors)} errors)")
        return False, all_errors
    else:
        print(f"✅ Evidence-based validation COMPLETE for {len(evidence_based_gates)} gate(s)")
        return True, []


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python3 validate_evidence_based.py <path-to-proof-file> [gate-name]")
        sys.exit(2)
    
    file_path = Path(sys.argv[1])
    specific_gate = sys.argv[2] if len(sys.argv) > 2 else None
    
    print("🔍 Evidence-Based Validation Checker (BL-027/028)")
    print("=" * 70)
    print(f"File: {file_path}")
    if specific_gate:
        print(f"Gate: {specific_gate}")
    print("=" * 70)
    
    is_valid, messages = validate_evidence_based(file_path, specific_gate)
    
    if messages:
        print("\nMessages:")
        for msg in messages:
            print(f"  - {msg}")
    
    if is_valid:
        print("\n✅ Evidence-based validation requirements MET")
        sys.exit(0)
    else:
        print("\n❌ Evidence-based validation requirements NOT MET")
        sys.exit(1)


if __name__ == "__main__":
    main()
