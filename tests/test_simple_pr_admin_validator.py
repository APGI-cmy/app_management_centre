"""
tests/test_simple_pr_admin_validator.py

Regression tests for the AMC Simple PR Admin Model validator.

Authority: governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md v1.2.0
           governance/canon/POLC_EXECUTION_MODEL_CANON.md v1.0.0
Issue:     app_management_centre#1172 — Layer-down POLC execution model

Acceptance Criteria covered:
  AC1  — missing execution_model fails where implementation paths require it
  AC2  — invalid execution_model value fails
  AC3  — valid builder-governed passes with required companion fields
  AC4  — valid foreman-orchestrated passes with required companion fields
  AC5  — valid cs2-hotfix-override passes only with CS2 justification
  AC6  — docs-only / canon-only cases not incorrectly forced into execution_model
  AC7  — missing implementing_agent for builder-governed fails
  AC8  — missing orchestrating_agent for foreman-orchestrated fails
  AC9  — missing cs2_justification for cs2-hotfix-override fails
  AC10 — missing required fields (type, requires_iaa, etc.) fails
  AC11 — invalid type enum fails
  AC12 — full-ceremony types (governance-control) require requires_iaa/requires_ecap=true
  AC13 — governance-control files in diff require requires_iaa/requires_ecap=true
"""

import json
import os
import subprocess
import tempfile
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

SCRIPT_PATH = Path(__file__).parent.parent / ".github" / "scripts" / "validate-simple-pr-admin.sh"


def _run_validator(manifest_content: dict, changed_files: list[str] | None = None,
                   extra_args: list[str] | None = None) -> tuple[int, str, str]:
    """
    Write manifest_content to a temp file, run the validator against it,
    optionally with a changed-files list. Returns (returncode, stdout, stderr).
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        # Write manifest
        manifest_path = os.path.join(tmpdir, "pr.json")
        with open(manifest_path, "w") as f:
            json.dump(manifest_content, f, indent=2)

        # Write changed-files list if provided
        cmd = [str(SCRIPT_PATH), "--manifest", manifest_path, "--skip-diff"]

        if changed_files is not None:
            cf_path = os.path.join(tmpdir, "changed_files.txt")
            with open(cf_path, "w") as f:
                f.write("\n".join(changed_files))
            # Don't skip diff when changed_files provided — use the file
            cmd = [str(SCRIPT_PATH), "--manifest", manifest_path, "--changed-files", cf_path]

        if extra_args:
            cmd.extend(extra_args)

        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr


def _minimal_product_fix(overrides: dict | None = None) -> dict:
    """Return a minimal valid product-fix manifest."""
    base = {
        "type": "product-fix",
        "requires_iaa": False,
        "requires_ecap": False,
        "governing_issue": "#1172",
        "scope_summary": "Fix minor label typo in dashboard component.",
        "created_by": "api-builder",
        "created_at": "2026-05-12T10:00:00Z",
    }
    if overrides:
        base.update(overrides)
    return base


def _minimal_governance_control(overrides: dict | None = None) -> dict:
    """Return a minimal valid governance-control manifest."""
    base = {
        "type": "governance-control",
        "requires_iaa": True,
        "requires_ecap": True,
        "governing_issue": "#1172",
        "scope_summary": "Layer-down POLC execution model canon and update validator.",
        "created_by": "governance-liaison-amc-agent",
        "created_at": "2026-05-12T10:00:00Z",
    }
    if overrides:
        base.update(overrides)
    return base


# ---------------------------------------------------------------------------
# Check 1: Manifest exists (covered implicitly — validator exits 1 if missing)
# Check 2: Valid JSON (covered by writing valid dicts)
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# AC10 — Required fields
# ---------------------------------------------------------------------------

class TestRequiredFields:
    """AC10 — missing required fields cause FAIL."""

    @pytest.mark.parametrize("missing_field", [
        "type", "requires_iaa", "requires_ecap", "governing_issue", "scope_summary"
    ])
    def test_missing_required_field_fails(self, missing_field):
        manifest = _minimal_product_fix()
        del manifest[missing_field]
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1, f"Expected FAIL when '{missing_field}' is missing, got rc={rc}"
        assert "Missing required fields" in stdout or "required" in stdout.lower()

    def test_all_required_fields_pass(self):
        manifest = _minimal_product_fix()
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 0, f"Expected PASS for valid manifest, got rc={rc}\n{stdout}"


# ---------------------------------------------------------------------------
# AC11 — type enum validation
# ---------------------------------------------------------------------------

class TestTypeEnum:
    """AC11 — invalid type fails; valid types pass."""

    @pytest.mark.parametrize("invalid_type", [
        "bugfix", "hotfix", "feature", "test-only", "", "governance_control"
    ])
    def test_invalid_type_fails(self, invalid_type):
        manifest = _minimal_product_fix({"type": invalid_type})
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1, f"Expected FAIL for type='{invalid_type}', got rc={rc}"

    @pytest.mark.parametrize("valid_type", [
        "product-fix", "docs-only", "governance-control", "agent-contract",
        "migration", "deployment", "high-risk"
    ])
    def test_valid_type_passes(self, valid_type):
        manifest = _minimal_product_fix({"type": valid_type})
        # Full-ceremony types need requires_iaa/requires_ecap=true
        if valid_type in ("governance-control", "agent-contract", "migration", "deployment", "high-risk"):
            manifest["requires_iaa"] = True
            manifest["requires_ecap"] = True
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 0, f"Expected PASS for type='{valid_type}', got rc={rc}\n{stdout}"


# ---------------------------------------------------------------------------
# AC12 — Full-ceremony types require requires_iaa/requires_ecap=true
# ---------------------------------------------------------------------------

class TestFullCeremonyTypes:
    """AC12 — governance-control etc. require requires_iaa=true, requires_ecap=true."""

    @pytest.mark.parametrize("pr_type", [
        "governance-control", "agent-contract", "migration", "deployment", "high-risk"
    ])
    def test_full_ceremony_type_without_iaa_fails(self, pr_type):
        manifest = _minimal_product_fix({
            "type": pr_type,
            "requires_iaa": False,
            "requires_ecap": True,
        })
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1, f"Expected FAIL for {pr_type} with requires_iaa=false, got rc={rc}"

    @pytest.mark.parametrize("pr_type", [
        "governance-control", "agent-contract", "migration", "deployment", "high-risk"
    ])
    def test_full_ceremony_type_without_ecap_fails(self, pr_type):
        manifest = _minimal_product_fix({
            "type": pr_type,
            "requires_iaa": True,
            "requires_ecap": False,
        })
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1, f"Expected FAIL for {pr_type} with requires_ecap=false, got rc={rc}"

    @pytest.mark.parametrize("pr_type", [
        "governance-control", "agent-contract", "migration", "deployment", "high-risk"
    ])
    def test_full_ceremony_type_with_both_passes(self, pr_type):
        manifest = _minimal_product_fix({
            "type": pr_type,
            "requires_iaa": True,
            "requires_ecap": True,
        })
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 0, f"Expected PASS for {pr_type} with iaa=ecap=true, got rc={rc}\n{stdout}"


# ---------------------------------------------------------------------------
# AC13 — governance-control files in diff require requires_iaa/requires_ecap=true
# ---------------------------------------------------------------------------

class TestGovernanceControlDiff:
    """AC13 — governance-control files in diff require full ceremony flags."""

    @pytest.mark.parametrize("gov_file", [
        ".github/workflows/iaa-ecap-hard-gate.yml",
        ".github/scripts/validate-simple-pr-admin.sh",
        ".github/agents/foreman-v2-agent.md",
        "governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md",
        ".agent-admin/wave-records/amc-wave-record.md",
        "some-file.agent.md",
    ])
    def test_governance_file_in_diff_requires_iaa_ecap(self, gov_file):
        manifest = _minimal_product_fix()  # requires_iaa=false, requires_ecap=false
        rc, stdout, _ = _run_validator(manifest, changed_files=[gov_file])
        assert rc == 1, f"Expected FAIL for governance-control file {gov_file} with iaa=false, got rc={rc}"
        assert "requires_iaa" in stdout or "requires_ecap" in stdout or "governance-control" in stdout.lower()

    def test_non_governance_file_no_enforcement(self):
        """Files outside governance-control patterns don't trigger IAA/ECAP enforcement."""
        manifest = _minimal_product_fix()
        rc, stdout, _ = _run_validator(manifest, changed_files=["apps/dashboard/index.tsx"])
        # apps/ is an implementation file → triggers execution_model check, not iaa/ecap
        # Without execution_model it should fail Check 13
        assert rc == 1
        assert "execution_model" in stdout


# ---------------------------------------------------------------------------
# AC1 — missing execution_model fails where implementation paths require it
# ---------------------------------------------------------------------------

class TestExecutionModelRequired:
    """AC1 — implementation files require execution_model declaration."""

    @pytest.mark.parametrize("impl_file", [
        "apps/dashboard/index.tsx",
        "src/api/users.py",
        "modules/isms/controller.ts",
        "lib/utils/helpers.py",
        "packages/shared/Button.tsx",
    ])
    def test_implementation_file_without_execution_model_fails(self, impl_file):
        manifest = _minimal_product_fix()  # no execution_model
        rc, stdout, _ = _run_validator(manifest, changed_files=[impl_file])
        assert rc == 1, f"Expected FAIL for impl file {impl_file} without execution_model"
        assert "execution_model" in stdout

    @pytest.mark.parametrize("non_impl_file", [
        "governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md",
        ".admin/pr.json",
        "docs/README.md",
    ])
    def test_non_implementation_file_no_execution_model_enforcement(self, non_impl_file):
        """Non-implementation files don't trigger execution_model requirement."""
        manifest = _minimal_governance_control()
        rc, stdout, _ = _run_validator(manifest, changed_files=[non_impl_file])
        # governance files will trigger iaa/ecap but not execution_model for governance-control type
        # Just check execution_model is not the reason for failure here
        if rc != 0:
            assert "requires_iaa" in stdout or "requires_ecap" in stdout


# ---------------------------------------------------------------------------
# AC2 — invalid execution_model value fails
# ---------------------------------------------------------------------------

class TestInvalidExecutionModel:
    """AC2 — invalid execution_model value fails."""

    @pytest.mark.parametrize("invalid_model", [
        "copilot-governed", "agent-governed", "manual", "cs2-override"
    ])
    def test_invalid_execution_model_fails(self, invalid_model):
        manifest = _minimal_product_fix({
            "execution_model": invalid_model,
            "implementing_agent": "api-builder",
        })
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1, f"Expected FAIL for execution_model='{invalid_model}'"
        assert "execution_model" in stdout


# ---------------------------------------------------------------------------
# AC3 — valid builder-governed passes with required companion fields
# ---------------------------------------------------------------------------

class TestBuilderGoverned:
    """AC3 — builder-governed passes with implementing_agent; fails without."""

    def test_builder_governed_with_implementing_agent_passes(self):
        manifest = _minimal_product_fix({
            "execution_model": "builder-governed",
            "implementing_agent": "api-builder",
        })
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 0, f"Expected PASS for builder-governed with implementing_agent\n{stdout}"

    def test_builder_governed_without_implementing_agent_fails(self):
        """AC7 — missing implementing_agent for builder-governed fails."""
        manifest = _minimal_product_fix({
            "execution_model": "builder-governed",
        })
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1, "Expected FAIL for builder-governed without implementing_agent"
        assert "implementing_agent" in stdout

    def test_builder_governed_with_impl_files_passes(self):
        """Full builder-governed scenario with implementation file in diff."""
        manifest = _minimal_product_fix({
            "execution_model": "builder-governed",
            "implementing_agent": "api-builder",
        })
        rc, stdout, _ = _run_validator(manifest, changed_files=["src/api/users.py"])
        assert rc == 0, f"Expected PASS for builder-governed with impl file\n{stdout}"


# ---------------------------------------------------------------------------
# AC4 — valid foreman-orchestrated passes with required companion fields
# ---------------------------------------------------------------------------

class TestForemanOrchestrated:
    """AC4 — foreman-orchestrated passes with both orchestrating_agent and implementing_agent."""

    def test_foreman_orchestrated_with_all_fields_passes(self):
        manifest = _minimal_product_fix({
            "execution_model": "foreman-orchestrated",
            "orchestrating_agent": "foreman-v2-agent",
            "implementing_agent": "api-builder",
        })
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 0, f"Expected PASS for foreman-orchestrated with all fields\n{stdout}"

    def test_foreman_orchestrated_without_orchestrating_agent_fails(self):
        """AC8 — missing orchestrating_agent for foreman-orchestrated fails."""
        manifest = _minimal_product_fix({
            "execution_model": "foreman-orchestrated",
            "implementing_agent": "api-builder",
        })
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1, "Expected FAIL for foreman-orchestrated without orchestrating_agent"
        assert "orchestrating_agent" in stdout

    def test_foreman_orchestrated_without_implementing_agent_fails(self):
        """AC8 — missing implementing_agent for foreman-orchestrated fails."""
        manifest = _minimal_product_fix({
            "execution_model": "foreman-orchestrated",
            "orchestrating_agent": "foreman-v2-agent",
        })
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1, "Expected FAIL for foreman-orchestrated without implementing_agent"
        assert "implementing_agent" in stdout

    def test_foreman_orchestrated_with_impl_files_passes(self):
        """Foreman-orchestrated with implementation file in diff passes."""
        manifest = _minimal_product_fix({
            "execution_model": "foreman-orchestrated",
            "orchestrating_agent": "foreman-v2-agent",
            "implementing_agent": "ui-builder",
        })
        rc, stdout, _ = _run_validator(manifest, changed_files=["modules/isms/controller.ts"])
        assert rc == 0, f"Expected PASS for foreman-orchestrated with impl file\n{stdout}"


# ---------------------------------------------------------------------------
# AC5 — cs2-hotfix-override passes only with cs2_justification
# ---------------------------------------------------------------------------

class TestCS2HotfixOverride:
    """AC5 — cs2-hotfix-override passes with cs2_justification; fails without."""

    def test_cs2_hotfix_with_justification_passes(self):
        manifest = _minimal_product_fix({
            "execution_model": "cs2-hotfix-override",
            "cs2_justification": "CS2 approved emergency fix per issue #9999 — production down",
        })
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 0, f"Expected PASS for cs2-hotfix-override with justification\n{stdout}"

    def test_cs2_hotfix_without_justification_fails(self):
        """AC9 — missing cs2_justification for cs2-hotfix-override fails."""
        manifest = _minimal_product_fix({
            "execution_model": "cs2-hotfix-override",
        })
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1, "Expected FAIL for cs2-hotfix-override without cs2_justification"
        assert "cs2_justification" in stdout

    def test_cs2_hotfix_with_empty_justification_fails(self):
        """Empty cs2_justification is not acceptable."""
        manifest = _minimal_product_fix({
            "execution_model": "cs2-hotfix-override",
            "cs2_justification": "",
        })
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1, "Expected FAIL for cs2-hotfix-override with empty cs2_justification"


# ---------------------------------------------------------------------------
# AC6 — docs-only / canon-only cases not forced into execution_model
# ---------------------------------------------------------------------------

class TestDocsOnlyNoExecutionModelRequired:
    """AC6 — pure docs/governance-only changes do not require execution_model."""

    def test_docs_only_without_execution_model_passes(self):
        manifest = _minimal_product_fix({"type": "docs-only"})
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 0, f"Expected PASS for docs-only without execution_model\n{stdout}"

    def test_governance_control_without_execution_model_passes(self):
        """governance-control PRs touching only canon files don't need execution_model."""
        manifest = _minimal_governance_control()
        rc, stdout, _ = _run_validator(
            manifest,
            changed_files=["governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md"]
        )
        assert rc == 0, f"Expected PASS for governance-control without execution_model\n{stdout}"

    def test_no_impl_files_no_execution_model_required(self):
        """Product-fix with no implementation files doesn't require execution_model."""
        manifest = _minimal_product_fix()
        rc, stdout, _ = _run_validator(manifest, changed_files=[".admin/pr.json"])
        # .admin/ is a forced-ceremony path trigger, but product-fix with requires_iaa=false
        # will fail on governance-control enforcement if iaa/ecap checks trigger
        # The key check: no Check-13 execution_model failure
        if rc == 1:
            assert "execution_model" not in stdout or "No implementation files" in stdout


# ---------------------------------------------------------------------------
# Additional: governing_issue pattern validation
# ---------------------------------------------------------------------------

class TestGoverningIssue:
    """governing_issue must match ^#[0-9]+$."""

    @pytest.mark.parametrize("bad_issue", ["1172", "#abc", "issue-1172", "#", ""])
    def test_invalid_governing_issue_fails(self, bad_issue):
        manifest = _minimal_product_fix({"governing_issue": bad_issue})
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1, f"Expected FAIL for governing_issue='{bad_issue}'"

    @pytest.mark.parametrize("good_issue", ["#1172", "#1", "#99999"])
    def test_valid_governing_issue_passes(self, good_issue):
        manifest = _minimal_product_fix({"governing_issue": good_issue})
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 0, f"Expected PASS for governing_issue='{good_issue}'\n{stdout}"


# ---------------------------------------------------------------------------
# Additional: scope_summary length
# ---------------------------------------------------------------------------

class TestScopeSummaryLength:
    """scope_summary must be 10–500 characters."""

    def test_too_short_fails(self):
        manifest = _minimal_product_fix({"scope_summary": "Too short"})
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1

    def test_too_long_fails(self):
        manifest = _minimal_product_fix({"scope_summary": "x" * 501})
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1

    def test_exactly_10_chars_passes(self):
        manifest = _minimal_product_fix({"scope_summary": "1234567890"})
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 0, f"\n{stdout}"

    def test_exactly_500_chars_passes(self):
        manifest = _minimal_product_fix({"scope_summary": "x" * 500})
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 0, f"\n{stdout}"


# ---------------------------------------------------------------------------
# Additional: no extra properties allowed
# ---------------------------------------------------------------------------

class TestAdditionalProperties:
    """additionalProperties: false — unexpected keys cause FAIL."""

    def test_unknown_property_fails(self):
        manifest = _minimal_product_fix({"unknown_field": "value"})
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 1
        assert "unknown_field" in stdout or "Unexpected" in stdout

    def test_known_optional_fields_pass(self):
        manifest = _minimal_product_fix({
            "execution_model": "builder-governed",
            "implementing_agent": "api-builder",
        })
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 0, f"Expected PASS with known optional fields\n{stdout}"


# ---------------------------------------------------------------------------
# Integration: full governance-control PR for this layer-down
# ---------------------------------------------------------------------------

class TestIntegrationLayerDownManifest:
    """Integration test — validate the actual PR manifest shape for this layer-down."""

    def test_governance_control_layer_down_manifest_passes(self):
        """The governance-control manifest shape used for this PR passes validation."""
        manifest = {
            "type": "governance-control",
            "requires_iaa": True,
            "requires_ecap": True,
            "governing_issue": "#1172",
            "scope_summary": (
                "Layer-down POLC execution model canon and update AMC Simple PR Admin Model "
                "to v1.2.0 per upstream governance commit 77a8297b."
            ),
            "created_by": "governance-liaison-amc-agent",
            "created_at": "2026-05-12T10:00:00Z",
        }
        rc, stdout, _ = _run_validator(manifest)
        assert rc == 0, f"Expected PASS for governance-control layer-down manifest\n{stdout}"
