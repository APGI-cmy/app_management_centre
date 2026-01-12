"""Test fixtures for Wave 3.0 QA Infrastructure"""

import pytest
from datetime import datetime, UTC


@pytest.fixture
def test_organisation_id():
    """Provide a test organisation ID for tenant isolation."""
    return "test-org-wave3"


@pytest.fixture
def test_user_id():
    """Provide a test user ID."""
    return "user-johan-wave3"


@pytest.fixture
def create_qa_evidence():
    """Factory for creating QA evidence artifacts."""
    def _create_evidence(qa_id: str, status: str, details: dict):
        return {
            "qa_id": qa_id,
            "status": status,
            "details": details,
            "timestamp": datetime.now(UTC).isoformat()
        }
    return _create_evidence


@pytest.fixture(autouse=True)
def cleanup_telemetry():
    """Clean up telemetry state before and after each test."""
    from foreman.cross_cutting import telemetry_tracer
    from foreman.cross_cutting import audit_logger
    from foreman.cross_cutting import sla_alert_router
    
    # Clean before test
    telemetry_tracer.clear_all()
    audit_logger.clear_all()
    sla_alert_router.clear_all()
    
    yield
    
    # Clean after test
    telemetry_tracer.clear_all()
    audit_logger.clear_all()
    sla_alert_router.clear_all()
