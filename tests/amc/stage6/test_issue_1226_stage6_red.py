from pathlib import Path
import re

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[3]
WORKFLOW_DIR = PROJECT_ROOT / ".github" / "workflows"
CI_WORKFLOW = WORKFLOW_DIR / "ci.yml"
FRONTEND_WORKFLOW = WORKFLOW_DIR / "deploy-frontend.yml"
MIGRATION_WORKFLOW = WORKFLOW_DIR / "db-migrate.yml"
ENV_EXAMPLE = PROJECT_ROOT / ".env.example"
ISSUE_EVIDENCE_DIR = PROJECT_ROOT / "qa" / "evidence" / "issue-1226"

WAVE1_STARTUP_REQUIRED_VARS = {
    "AIMC_API_BASE_URL",
    "AIMCC_API_BASE_URL",
    "KUC_API_BASE_URL",
    "KNOWLEDGE_API_BASE_URL",
    "FOREMAN_API_BASE_URL",
    "SPECIALIST_AGENT_API_BASE_URL",
    "AIMC_SERVICE_TOKEN",
    "AIMCC_SERVICE_TOKEN",
    "KUC_SERVICE_TOKEN",
    "KNOWLEDGE_SERVICE_TOKEN",
    "FOREMAN_SERVICE_TOKEN",
    "SPECIALIST_AGENT_SERVICE_TOKEN",
}


def _workflow_payload(path: Path, test_id: str):
    assert path.exists(), (
        f"{test_id}: workflow '{path.name}' is missing, so the ownership/control "
        "requirement is unmet."
    )
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def _workflow_text(path: Path, test_id: str):
    assert path.exists(), (
        f"{test_id}: workflow '{path.name}' is missing, so the deployment control "
        "requirement is unmet."
    )
    return path.read_text(encoding="utf-8")


def _env_example_variables():
    content = ENV_EXAMPLE.read_text(encoding="utf-8")
    return {
        match.group(1)
        for match in re.finditer(r"^([A-Z0-9_]+)=", content, flags=re.MULTILINE)
    }


def _runtime_source_files():
    candidate_dirs = [PROJECT_ROOT / "lib", PROJECT_ROOT / "scripts"]
    extensions = {".py", ".ts", ".tsx", ".js", ".mjs", ".cjs"}
    files = []
    for directory in candidate_dirs:
        if not directory.exists():
            continue
        for file_path in directory.rglob("*"):
            if file_path.suffix in extensions and file_path.is_file():
                files.append(file_path)
    return files


def _runtime_sources_containing(token: str):
    matches = []
    for source_file in _runtime_source_files():
        if token in source_file.read_text(encoding="utf-8", errors="replace"):
            matches.append(source_file)
    return matches


def _is_workflow_dispatch_only(on_block):
    return (
        on_block == "workflow_dispatch"
        or on_block == {"workflow_dispatch": None}
        or (isinstance(on_block, dict) and set(on_block.keys()) == {"workflow_dispatch"})
    )


def test_qa_deploy_001_required_workflow_family_exists():
    missing = [
        wf.name
        for wf in (CI_WORKFLOW, FRONTEND_WORKFLOW, MIGRATION_WORKFLOW)
        if not wf.exists()
    ]
    assert not missing, (
        "QA-DEPLOY-001: required workflow family missing/renamed without disposition: "
        f"{', '.join(missing)}"
    )


def test_qa_deploy_002_production_jobs_use_protected_environment():
    frontend = _workflow_payload(FRONTEND_WORKFLOW, "QA-DEPLOY-002")
    migration = _workflow_payload(MIGRATION_WORKFLOW, "QA-DEPLOY-002")

    checked_jobs = 0
    for workflow in (frontend, migration):
        for job_name, job_payload in (workflow.get("jobs") or {}).items():
            if "prod" in job_name.lower() or "production" in job_name.lower():
                checked_jobs += 1
                assert job_payload.get("environment") == "production", (
                    "QA-DEPLOY-002: production job lacks protected 'production' "
                    f"environment: {job_name}"
                )

    assert checked_jobs > 0, "QA-DEPLOY-002: no production job was found to validate."


def test_qa_deploy_003_non_production_jobs_cannot_reference_production_secrets():
    workflow_text = (
        _workflow_text(CI_WORKFLOW, "QA-DEPLOY-003")
        + "\n"
        + _workflow_text(FRONTEND_WORKFLOW, "QA-DEPLOY-003")
    )
    assert "PRODUCTION_" not in workflow_text, (
        "QA-DEPLOY-003: PR/staging workflow content references production-scoped "
        "secret naming."
    )


def test_qa_deploy_004_migration_command_is_frozen():
    migration_text = _workflow_text(MIGRATION_WORKFLOW, "QA-DEPLOY-004")
    assert "supabase db push --project-ref $SUPABASE_PROJECT_REF" in migration_text, (
        "QA-DEPLOY-004: approved migration command is missing."
    )
    assert "supabase link" not in migration_text, (
        "QA-DEPLOY-004: migration workflow contains forbidden supabase link drift."
    )


def test_qa_deploy_006_required_runtime_and_workflow_variables_exist_in_env_example():
    expected = WAVE1_STARTUP_REQUIRED_VARS | {"SUPABASE_PROJECT_REF"}
    present = _env_example_variables()
    missing = sorted(expected - present)
    assert not missing, (
        "QA-DEPLOY-006: required variable(s) absent from .env.example: "
        + ", ".join(missing)
    )


def test_qa_deploy_007_health_and_smoke_evidence_exists():
    health_smoke_evidence = ISSUE_EVIDENCE_DIR / "DEPLOYMENT_HEALTH_SMOKE_EVIDENCE.md"
    assert health_smoke_evidence.exists(), (
        "QA-DEPLOY-007: deployment evidence lacks app/API/Supabase/realtime "
        "health-smoke validation artifact."
    )


def test_qa_deploy_010_placeholder_evidence_is_rejected():
    placeholder_disposition = ISSUE_EVIDENCE_DIR / "PLACEHOLDER_EVIDENCE_DISPOSITION.md"
    assert placeholder_disposition.exists(), (
        "QA-DEPLOY-010: placeholder evidence disposition record is missing."
    )
    disposition_text = placeholder_disposition.read_text(encoding="utf-8").lower()
    assert "rejected" in disposition_text, (
        "QA-DEPLOY-010: placeholder evidence rejection is not explicitly recorded."
    )


def test_qa_config_001_startup_fails_if_any_required_env_is_missing():
    missing_runtime_checks = [
        variable
        for variable in sorted(WAVE1_STARTUP_REQUIRED_VARS)
        if not _runtime_sources_containing(variable)
    ]
    assert not missing_runtime_checks, (
        "QA-CONFIG-001: startup runtime does not enforce required variable(s): "
        + ", ".join(missing_runtime_checks)
    )


def test_qa_config_002_startup_error_names_missing_variable_explicitly():
    explicit_error_paths = []
    for source_file in _runtime_source_files():
        source_text = source_file.read_text(encoding="utf-8", errors="ignore")
        if "NEXT_PUBLIC_SUPABASE_URL" in source_text and (
            "missing variable" in source_text.lower()
            or "missing environment variable" in source_text.lower()
        ):
            explicit_error_paths.append(source_file)

    assert explicit_error_paths, (
        "QA-CONFIG-002: startup runtime does not show explicit named missing-variable "
        "error handling."
    )


def test_qa_config_003_all_required_env_vars_are_individually_validated():
    sources_with_checks = {
        var for var in WAVE1_STARTUP_REQUIRED_VARS if _runtime_sources_containing(var)
    }
    assert sources_with_checks == WAVE1_STARTUP_REQUIRED_VARS, (
        "QA-CONFIG-003: full required startup-variable validation set is incomplete. "
        f"Validated={len(sources_with_checks)}/{len(WAVE1_STARTUP_REQUIRED_VARS)}"
    )


def test_qa_des001_001_frontend_deploy_ownership_is_exclusive():
    _workflow_payload(FRONTEND_WORKFLOW, "QA-DES001-001")
    owners = []
    for workflow_file in WORKFLOW_DIR.glob("*.yml"):
        text = workflow_file.read_text(encoding="utf-8", errors="ignore")
        if "vercel" in text.lower() or "deploy" in workflow_file.stem.lower():
            owners.append(workflow_file.name)

    assert owners == ["deploy-frontend.yml"], (
        "QA-DES001-001: workflow ownership drift detected for frontend deployment. "
        f"Owners seen={owners}"
    )


def test_qa_des001_002_db_migration_ownership_is_exclusive():
    _workflow_payload(MIGRATION_WORKFLOW, "QA-DES001-002")
    owners = []
    for workflow_file in WORKFLOW_DIR.glob("*.yml"):
        text = workflow_file.read_text(encoding="utf-8", errors="ignore")
        if "supabase db push" in text or "db-migrate" in workflow_file.name:
            owners.append(workflow_file.name)

    assert owners == ["db-migrate.yml"], (
        "QA-DES001-002: workflow ownership drift detected for DB migration. "
        f"Owners seen={owners}"
    )


def test_qa_des002_001_ci_runner_is_ubuntu_latest():
    ci_payload = _workflow_payload(CI_WORKFLOW, "QA-DES002-001")
    jobs = ci_payload.get("jobs") or {}
    assert jobs, "QA-DES002-001: ci.yml has no jobs block to validate runner policy."
    for job_name, job_payload in jobs.items():
        assert job_payload.get("runs-on") == "ubuntu-latest", (
            "QA-DES002-001: ci job does not use ubuntu-latest: "
            f"{job_name}"
        )


def test_qa_des003_001_no_workflow_uses_self_hosted_runner():
    required_workflows = [CI_WORKFLOW, FRONTEND_WORKFLOW, MIGRATION_WORKFLOW]
    missing = [workflow.name for workflow in required_workflows if not workflow.exists()]
    assert not missing, (
        "QA-DES003-001: required workflows missing, cannot satisfy repository-wide "
        f"runner validation: {', '.join(missing)}"
    )

    offenders = []
    for workflow_file in WORKFLOW_DIR.glob("*.yml"):
        workflow_text = workflow_file.read_text(encoding="utf-8", errors="ignore")
        if "self-hosted" in workflow_text or "runs-on: [" in workflow_text:
            offenders.append(workflow_file.name)

    assert not offenders, (
        "QA-DES003-001: self-hosted/custom runner usage found in workflow(s): "
        + ", ".join(offenders)
    )


def test_qa_des004_001_db_migrate_uses_exact_command():
    migration_text = _workflow_text(MIGRATION_WORKFLOW, "QA-DES004-001")
    assert "supabase db push --project-ref $SUPABASE_PROJECT_REF" in migration_text, (
        "QA-DES004-001: migration command does not match the exact approved command."
    )


def test_qa_des005_001_db_migrate_trigger_is_manual_only():
    migration_payload = _workflow_payload(MIGRATION_WORKFLOW, "QA-DES005-001")
    on_block = migration_payload.get("on")
    assert _is_workflow_dispatch_only(
        on_block
    ), "QA-DES005-001: db-migrate trigger is not workflow_dispatch only."


def test_qa_des006_001_frontend_workflow_has_no_db_mutation_step():
    frontend_text = _workflow_text(FRONTEND_WORKFLOW, "QA-DES006-001")
    assert "supabase db push" not in frontend_text, (
        "QA-DES006-001: deploy-frontend workflow contains database mutation command."
    )


def test_qa_des007_001_frontend_production_job_has_protected_environment():
    frontend_payload = _workflow_payload(FRONTEND_WORKFLOW, "QA-DES007-001")
    production_jobs = []
    for job_name, job_payload in (frontend_payload.get("jobs") or {}).items():
        if "prod" in job_name.lower() or "production" in job_name.lower():
            production_jobs.append((job_name, job_payload.get("environment")))

    assert production_jobs, "QA-DES007-001: no production frontend job found in workflow."
    assert all(environment == "production" for _, environment in production_jobs), (
        "QA-DES007-001: frontend production job lacks environment: production."
    )


def test_qa_des008_001_missing_next_public_supabase_url_fails_explicitly():
    matches = _runtime_sources_containing("NEXT_PUBLIC_SUPABASE_URL")
    assert matches, (
        "QA-DES008-001: startup runtime has no explicit NEXT_PUBLIC_SUPABASE_URL "
        "validation path."
    )
