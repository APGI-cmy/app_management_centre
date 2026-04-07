---
id: test-modular-loading
name: test-modular-loading
version: 1.0.0

operational_guides:
  - path: test-modular-loading/test-procedures.md
  - path: test-modular-loading/test-data.md

metadata:
  purpose: Validate modular file loading capability
---

# Test Modular Loading Agent

**Purpose**: Test if GitHub Copilot can load files referenced in agent contracts.

## Quick Reference

**For operational procedures, see:**
- [Test Procedures](test-modular-loading/test-procedures.md)
- [Test Data](test-modular-loading/test-data.md)

## Test Instructions

This agent should be able to:
1. Read the test procedures file
2. Access the test data file
3. Report the secret code from test-data.md
