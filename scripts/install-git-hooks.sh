#!/bin/bash
#
# Git Hooks Installation Script
#
# Purpose: Install all Git hooks for Build-to-Green and BL-026 enforcement
# Usage: ./scripts/install-git-hooks.sh
# Platform: Cross-platform (Linux, macOS, Windows/Git Bash)
#

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo ""
echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   Git Hooks Installation - Build-to-Green & BL-026        ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Detect repository root
if REPO_ROOT=$(git rev-parse --show-toplevel); then
    cd "$REPO_ROOT"
else
    echo "Warning: Not in a git repository, using current directory"
    REPO_ROOT=$(pwd)
fi

echo "Repository root: $REPO_ROOT"
echo ""

# Method 1: Configure Git to use .githooks directory (RECOMMENDED)
echo -e "${YELLOW}[Method 1]${NC} Configuring Git to use .githooks directory..."
echo ""

if git config core.hooksPath .githooks; then
    echo -e "${GREEN}✅ Git configured to use .githooks directory${NC}"
    echo "   This will automatically use all hooks in .githooks/"
    echo ""
    METHOD1_SUCCESS=true
else
    echo -e "${RED}❌ Failed to configure Git hooks path${NC}"
    echo ""
    METHOD1_SUCCESS=false
fi

# Method 2: Manual copying (FALLBACK)
echo -e "${YELLOW}[Method 2]${NC} Fallback: Manual hook installation..."
echo ""

# Ensure .git/hooks directory exists
if [ ! -d ".git/hooks" ]; then
    echo -e "${YELLOW}⚠️  .git/hooks directory not found${NC}"
    echo "   This might not be a Git repository or hooks are managed differently"
    echo ""
    METHOD2_SUCCESS=false
else
    # List of hooks to install
    HOOKS=(
        "pre-commit"
        "pre-commit-deprecation"
        "pre-commit-tier0-consistency"
        "pre-push"
    )
    
    INSTALLED_COUNT=0
    FAILED_COUNT=0
    
    for hook in "${HOOKS[@]}"; do
        if [ -f ".githooks/$hook" ]; then
            if cp ".githooks/$hook" ".git/hooks/$hook" && chmod +x ".git/hooks/$hook"; then
                echo -e "   ${GREEN}✅${NC} Installed: $hook"
                INSTALLED_COUNT=$((INSTALLED_COUNT + 1))
            else
                echo -e "   ${RED}❌${NC} Failed: $hook"
                FAILED_COUNT=$((FAILED_COUNT + 1))
            fi
        else
            echo -e "   ${YELLOW}⚠️${NC}  Not found: $hook"
        fi
    done
    
    echo ""
    
    if [ $FAILED_COUNT -eq 0 ]; then
        echo -e "${GREEN}✅ Manual hook installation complete ($INSTALLED_COUNT hooks)${NC}"
        METHOD2_SUCCESS=true
    else
        echo -e "${YELLOW}⚠️  Partial installation ($INSTALLED_COUNT installed, $FAILED_COUNT failed)${NC}"
        METHOD2_SUCCESS=false
    fi
    echo ""
fi

# Check Python and ruff availability
echo -e "${YELLOW}[Validation]${NC} Checking environment requirements..."
echo ""

# Check Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    echo -e "   ${GREEN}✅${NC} Python: $PYTHON_VERSION"
else
    echo -e "   ${RED}❌${NC} Python 3 not found"
    echo "      Install Python 3.9+ from https://www.python.org/"
    VALIDATION_FAILED=true
fi

# Check ruff (or offer to install)
if command -v ruff &> /dev/null; then
    RUFF_VERSION=$(ruff --version 2>&1 | head -1)
    echo -e "   ${GREEN}✅${NC} ruff: $RUFF_VERSION"
else
    echo -e "   ${YELLOW}⚠️${NC}  ruff not found"
    echo ""
    echo "   ruff is required for BL-026 deprecation detection."
    echo ""
    read -p "   Install ruff now? (y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        if pip install ruff; then
            echo -e "   ${GREEN}✅${NC} ruff installed successfully"
        else
            echo -e "   ${RED}❌${NC} Failed to install ruff"
            echo "      Try manually: pip install ruff"
            VALIDATION_FAILED=true
        fi
    else
        echo -e "   ${YELLOW}⚠️${NC}  Skipped ruff installation"
        echo "      Hooks will attempt to install ruff automatically when needed"
    fi
fi

echo ""

# Summary
echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                   Installation Summary                    ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

if [ "$METHOD1_SUCCESS" = true ]; then
    echo -e "${GREEN}✅ Primary Method: Git hooks path configured${NC}"
    echo "   All hooks in .githooks/ will run automatically"
    echo ""
    echo "   Configured hooks:"
    for hook in .githooks/pre-*; do
        if [ -f "$hook" ] && [ -x "$hook" ]; then
            echo "     • $(basename $hook)"
        fi
    done
    echo ""
elif [ "$METHOD2_SUCCESS" = true ]; then
    echo -e "${GREEN}✅ Fallback Method: Hooks manually copied${NC}"
    echo "   Installed $INSTALLED_COUNT hooks to .git/hooks/"
    echo ""
    echo -e "${YELLOW}⚠️  Note: Manual updates required if hooks change${NC}"
    echo "   Re-run this script after pulling hook updates"
    echo ""
else
    echo -e "${RED}❌ Installation Failed${NC}"
    echo ""
    echo "Possible causes:"
    echo "  • Not in a Git repository"
    echo "  • Insufficient permissions"
    echo "  • Git configuration issues"
    echo ""
    echo "Manual installation:"
    echo "  git config core.hooksPath .githooks"
    echo ""
    exit 1
fi

if [ "$VALIDATION_FAILED" = true ]; then
    echo -e "${YELLOW}⚠️  Environment Validation Issues${NC}"
    echo "   Some requirements are missing. Hooks may not work correctly."
    echo ""
fi

echo "What hooks enforce:"
echo "  • pre-commit: Test debt detection, file validation"
echo "  • pre-commit-deprecation: BL-026 deprecated API detection (staged files)"
echo "  • pre-commit-tier0-consistency: Constitutional file consistency"
echo "  • pre-push: Full BL-026 scan (all Python files)"
echo ""

echo -e "${GREEN}Next Steps:${NC}"
echo "  1. Make a commit to test the pre-commit hooks"
echo "  2. Try pushing to test the pre-push hook"
echo "  3. Verify hooks are blocking invalid code"
echo ""

echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo ""

exit 0
