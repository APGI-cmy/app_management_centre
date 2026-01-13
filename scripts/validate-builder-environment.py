#!/usr/bin/env python3
"""
Builder Environment Validation Script

Purpose: Validates that builder environment has all required tools for BL-026 enforcement
Authority: BL-026 Automated Deprecation Detection Gate, Wave 3.2
Usage: python3 scripts/validate-builder-environment.py

Exit Codes:
    0 - Environment valid
    1 - Environment invalid (missing requirements)
    2 - Script error
"""

import sys
import subprocess
import shutil
from pathlib import Path
from typing import List, Tuple


class Color:
    """ANSI color codes for terminal output"""
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'  # No Color


def check_command_exists(command: str) -> Tuple[bool, str]:
    """Check if a command exists in PATH"""
    path = shutil.which(command)
    if path:
        return True, path
    return False, ""


def check_python_version() -> Tuple[bool, str]:
    """Check Python version (requires 3.9+)"""
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    
    if version.major >= 3 and version.minor >= 9:
        return True, version_str
    return False, version_str


def check_ruff_installed() -> Tuple[bool, str]:
    """Check if ruff is installed and get version"""
    try:
        result = subprocess.run(
            ["ruff", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            return True, version
        return False, ""
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False, ""


def check_git_hooks_configured() -> Tuple[bool, str]:
    """Check if Git hooks are properly configured"""
    try:
        # Check if core.hooksPath is set
        result = subprocess.run(
            ["git", "config", "core.hooksPath"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0 and result.stdout.strip():
            hooks_path = result.stdout.strip()
            return True, hooks_path
        
        # Check if hooks exist in .git/hooks
        git_root = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if git_root.returncode == 0:
            git_hooks_dir = Path(git_root.stdout.strip()) / ".git" / "hooks"
            if (git_hooks_dir / "pre-commit").exists() or \
               (git_hooks_dir / "pre-push").exists():
                return True, str(git_hooks_dir)
        
        return False, ""
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False, ""


def check_hook_files_exist() -> Tuple[bool, List[str]]:
    """Check if required hook files exist in .githooks"""
    try:
        git_root = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if git_root.returncode != 0:
            return False, []
        
        githooks_dir = Path(git_root.stdout.strip()) / ".githooks"
        
        required_hooks = [
            "pre-commit-deprecation",
            "pre-push"
        ]
        
        missing_hooks = []
        for hook in required_hooks:
            hook_path = githooks_dir / hook
            if not hook_path.exists():
                missing_hooks.append(hook)
        
        return len(missing_hooks) == 0, missing_hooks
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False, required_hooks


def print_header():
    """Print validation header"""
    print()
    print(f"{Color.BLUE}╔════════════════════════════════════════════════════════════╗{Color.NC}")
    print(f"{Color.BLUE}║      Builder Environment Validation - BL-026 & Wave 3.2   ║{Color.NC}")
    print(f"{Color.BLUE}╚════════════════════════════════════════════════════════════╝{Color.NC}")
    print()


def print_check(name: str, passed: bool, details: str = ""):
    """Print a check result"""
    status = f"{Color.GREEN}✅{Color.NC}" if passed else f"{Color.RED}❌{Color.NC}"
    print(f"  {status} {name}")
    if details:
        print(f"     {details}")


def print_summary(all_passed: bool):
    """Print validation summary"""
    print()
    print(f"{Color.BLUE}╔════════════════════════════════════════════════════════════╗{Color.NC}")
    print(f"{Color.BLUE}║                  Validation Summary                        ║{Color.NC}")
    print(f"{Color.BLUE}╚════════════════════════════════════════════════════════════╝{Color.NC}")
    print()
    
    if all_passed:
        print(f"{Color.GREEN}✅ Environment is ready for BL-026 enforcement{Color.NC}")
        print()
        print("All requirements satisfied:")
        print("  • Python 3.9+ installed")
        print("  • ruff deprecation scanner available")
        print("  • Git hooks configured")
        print("  • Hook files present")
        print()
    else:
        print(f"{Color.RED}❌ Environment validation failed{Color.NC}")
        print()
        print("Please fix the issues above before continuing.")
        print()
        print("To install missing requirements:")
        print("  • Python: https://www.python.org/downloads/")
        print("  • ruff: pip install ruff")
        print("  • Git hooks: ./scripts/install-git-hooks.sh")
        print()


def main():
    """Main validation function"""
    print_header()
    
    checks_passed = []
    
    # Check 1: Python version
    python_ok, python_version = check_python_version()
    print_check(
        "Python 3.9+",
        python_ok,
        f"Version: {python_version}" + ("" if python_ok else " (Requires 3.9+)")
    )
    checks_passed.append(python_ok)
    
    # Check 2: Git command
    git_ok, git_path = check_command_exists("git")
    print_check(
        "Git",
        git_ok,
        f"Path: {git_path}" if git_ok else "Not found in PATH"
    )
    checks_passed.append(git_ok)
    
    # Check 3: ruff
    ruff_ok, ruff_version = check_ruff_installed()
    print_check(
        "ruff (BL-026 scanner)",
        ruff_ok,
        ruff_version if ruff_ok else "Not installed - run: pip install ruff"
    )
    checks_passed.append(ruff_ok)
    
    # Check 4: Git hooks configured
    hooks_ok, hooks_path = check_git_hooks_configured()
    print_check(
        "Git hooks configured",
        hooks_ok,
        f"Path: {hooks_path}" if hooks_ok else "Run: ./scripts/install-git-hooks.sh"
    )
    checks_passed.append(hooks_ok)
    
    # Check 5: Hook files exist
    hookfiles_ok, missing_hooks = check_hook_files_exist()
    print_check(
        "BL-026 hook files present",
        hookfiles_ok,
        "" if hookfiles_ok else f"Missing: {', '.join(missing_hooks)}"
    )
    checks_passed.append(hookfiles_ok)
    
    print()
    
    # Summary
    all_passed = all(checks_passed)
    print_summary(all_passed)
    
    if all_passed:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nValidation cancelled by user.")
        sys.exit(2)
    except Exception as e:
        print(f"\n{Color.RED}❌ Validation error: {e}{Color.NC}\n")
        sys.exit(2)
