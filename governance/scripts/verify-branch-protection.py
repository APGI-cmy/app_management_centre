#!/usr/bin/env python3
"""
Branch Protection Verification Script

Purpose: Programmatically verify branch protection status and produce evidence
         compatible with canonical governance schemas.

Constitutional Authority:
- Governance PR #818 - Branch protection constitutional requirement
- BUILD_PHILOSOPHY.md Section IX - PR Gate Requirements
- governance/build/BRANCH_PROTECTION_GOVERNANCE_CONSUMPTION_SPEC.md

Version: 1.0.0
Date: 2025-12-30
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Any, Optional

class BranchProtectionVerifier:
    """Verifies branch protection status using multiple methods."""
    
    def __init__(self, repo: str, branches: list[str] = None):
        self.repo = repo
        self.branches = branches or ["main"]
        self.results = {
            "verification_timestamp": datetime.now().isoformat().replace('+00:00', 'Z') if '+00:00' in datetime.now().isoformat() else datetime.now().isoformat() + 'Z',
            "verification_method": "UNKNOWN",
            "repository": repo,
            "branches_verified": [],
            "overall_status": "RED",
            "canonical_governance_reference": "maturion-foreman-governance#PR-818",
            "bootstrap_exception": False,
            "bootstrap_exception_details": None
        }
    
    def verify(self) -> dict[str, Any]:
        """Run verification using available methods."""
        print("🔍 Starting Branch Protection Verification...")
        print(f"   Repository: {self.repo}")
        print(f"   Branches: {', '.join(self.branches)}")
        print()
        
        # Try verification methods in priority order
        success = False
        
        # Method 1: GitHub CLI (preferred if available)
        if self._has_github_cli():
            print("📡 Using GitHub CLI (gh) for verification...")
            success = self._verify_with_cli()
            if success:
                self.results["verification_method"] = "CLI"
        
        # Method 2: GitHub API (if CLI not available, requires token)
        if not success and self._has_github_token():
            print("📡 Using GitHub API for verification...")
            success = self._verify_with_api()
            if success:
                self.results["verification_method"] = "API"
        
        # Method 3: Inspection fallback (not authoritative)
        if not success:
            print("⚠️  Using inspection fallback (NOT authoritative)...")
            self._verify_with_inspection()
            self.results["verification_method"] = "INSPECTION"
        
        # Determine overall status
        self._determine_overall_status()
        
        return self.results
    
    def _has_github_cli(self) -> bool:
        """Check if GitHub CLI is available."""
        try:
            result = subprocess.run(
                ["gh", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False
    
    def _has_github_token(self) -> bool:
        """Check if GitHub token is available."""
        return "GITHUB_TOKEN" in os.environ or "GH_TOKEN" in os.environ
    
    def _verify_with_cli(self) -> bool:
        """Verify using GitHub CLI."""
        try:
            for branch in self.branches:
                print(f"\n🔍 Verifying branch: {branch}")
                
                # Query branch protection using gh CLI
                cmd = [
                    "gh", "api",
                    f"/repos/{self.repo}/branches/{branch}/protection",
                    "--silent"
                ]
                
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                branch_result = {
                    "branch_name": branch,
                    "protection_enabled": False,
                    "compliance_status": "NON_COMPLIANT",
                    "deviations": []
                }
                
                if result.returncode == 0:
                    # Branch protection exists
                    protection_data = json.loads(result.stdout)
                    branch_result["protection_enabled"] = True
                    
                    # Extract protection details
                    self._extract_protection_details(branch_result, protection_data)
                    
                    print(f"   ✅ Protection enabled: YES")
                    print(f"   📋 Status checks: {len(branch_result.get('required_status_checks', []))}")
                    print(f"   👥 Required approvals: {branch_result.get('required_approvals', 0)}")
                    
                elif result.returncode == 404:
                    # Branch protection not configured
                    branch_result["protection_enabled"] = False
                    branch_result["deviations"].append({
                        "requirement": "branch_protection_enabled",
                        "expected": "true",
                        "actual": "false",
                        "severity": "CRITICAL"
                    })
                    print(f"   ❌ Protection enabled: NO")
                else:
                    # Error querying
                    print(f"   ⚠️  Error querying protection: {result.stderr}")
                    return False
                
                # Evaluate compliance
                branch_result["compliance_status"] = \
                    "COMPLIANT" if branch_result["protection_enabled"] and not branch_result["deviations"] \
                    else "NON_COMPLIANT"
                
                self.results["branches_verified"].append(branch_result)
            
            return True
            
        except subprocess.TimeoutExpired:
            print("   ⚠️  Timeout querying GitHub API")
            return False
        except Exception as e:
            print(f"   ⚠️  Error: {str(e)}")
            return False
    
    def _extract_protection_details(self, branch_result: dict[str, Any], protection_data: dict[str, Any]):
        """Extract protection details from API response."""
        # Required status checks
        if "required_status_checks" in protection_data and protection_data["required_status_checks"]:
            contexts = protection_data["required_status_checks"].get("contexts", [])
            branch_result["required_status_checks"] = contexts
        else:
            branch_result["required_status_checks"] = []
        
        # Required approvals
        if "required_pull_request_reviews" in protection_data and protection_data["required_pull_request_reviews"]:
            branch_result["required_approvals"] = \
                protection_data["required_pull_request_reviews"].get("required_approving_review_count", 0)
        else:
            branch_result["required_approvals"] = 0
        
        # Administrator enforcement
        branch_result["administrator_enforcement"] = \
            protection_data.get("enforce_admins", {}).get("enabled", False)
        
        # Restrictions (force push, deletion)
        branch_result["force_push_blocked"] = "restrictions" in protection_data
        branch_result["deletion_blocked"] = True  # Always true if protection enabled
        
        # Linear history
        branch_result["linear_history"] = \
            protection_data.get("required_linear_history", {}).get("enabled", False)
    
    def _verify_with_api(self) -> bool:
        """Verify using GitHub API directly (not implemented in this basic version)."""
        # This would use requests library to call GitHub API
        # For now, fall back to inspection
        print("   ℹ️  Direct API verification not implemented, using inspection")
        return False
    
    def _verify_with_inspection(self):
        """Fallback inspection method (not authoritative)."""
        print("\n⚠️  WARNING: Using inspection fallback")
        print("   This method is NOT authoritative and may not reflect actual GitHub settings")
        print()
        
        for branch in self.branches:
            branch_result = {
                "branch_name": branch,
                "protection_enabled": False,
                "compliance_status": "NON_COMPLIANT",
                "deviations": [{
                    "requirement": "authoritative_verification",
                    "expected": "API or CLI",
                    "actual": "inspection_fallback",
                    "severity": "CRITICAL"
                }]
            }
            
            print(f"   ⚠️  {branch}: Cannot verify authoritatively (API/CLI unavailable)")
            
            self.results["branches_verified"].append(branch_result)
    
    def _determine_overall_status(self):
        """Determine overall compliance status."""
        print("\n📊 Verification Summary:")
        
        if not self.results["branches_verified"]:
            self.results["overall_status"] = "RED"
            print("   ❌ Overall Status: RED (no branches verified)")
            return
        
        all_compliant = all(
            b["compliance_status"] == "COMPLIANT" 
            for b in self.results["branches_verified"]
        )
        
        any_critical = any(
            d.get("severity") == "CRITICAL"
            for b in self.results["branches_verified"]
            for d in b.get("deviations", [])
        )
        
        if all_compliant:
            self.results["overall_status"] = "GREEN"
            print("   ✅ Overall Status: GREEN (all branches compliant)")
        elif any_critical:
            self.results["overall_status"] = "RED"
            print("   ❌ Overall Status: RED (critical deviations detected)")
        else:
            self.results["overall_status"] = "AMBER"
            print("   ⚠️  Overall Status: AMBER (minor deviations)")
        
        # Show per-branch status
        for branch in self.results["branches_verified"]:
            status_icon = "✅" if branch["compliance_status"] == "COMPLIANT" else "❌"
            print(f"      {status_icon} {branch['branch_name']}: {branch['compliance_status']}")

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Verify branch protection status programmatically"
    )
    parser.add_argument(
        "--repo",
        default="MaturionISMS/maturion-foreman-office-app",
        help="Repository in owner/repo format"
    )
    parser.add_argument(
        "--branch",
        action="append",
        dest="branches",
        help="Branch to verify (can be specified multiple times)"
    )
    parser.add_argument(
        "--output",
        default="foreman/evidence/branch-protection-verification-report.json",
        help="Output path for evidence report"
    )
    
    args = parser.parse_args()
    
    # Default to main if no branches specified
    branches = args.branches if args.branches else ["main"]
    
    # Create verifier
    verifier = BranchProtectionVerifier(args.repo, branches)
    
    # Run verification
    results = verifier.verify()
    
    # Ensure output directory exists
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write results to evidence file
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📝 Evidence written to: {output_path}")
    
    # Exit with appropriate code
    if results["overall_status"] == "GREEN":
        print("\n✅ Branch protection verification: GREEN")
        sys.exit(0)
    elif results["overall_status"] == "AMBER":
        print("\n⚠️  Branch protection verification: AMBER")
        sys.exit(1)
    else:
        print("\n❌ Branch protection verification: RED")
        print("\n⚠️  ESCALATION REQUIRED: Bootstrap exception protocol may be needed")
        print("   See: governance/build/BRANCH_PROTECTION_GOVERNANCE_CONSUMPTION_SPEC.md Section VI")
        sys.exit(2)

if __name__ == "__main__":
    main()
