"""
Tests for Wave 3.1 SLA Alert Router

Tests SLA-based alerting with telemetry integration including:
- SLA definition and threshold management
- Compliance checking against metrics
- Alert generation and routing
- Audit trail correlation
"""

import pytest
from datetime import datetime, UTC, UTC

UTC = UTC


@pytest.mark.wave3
@pytest.mark.subwave_3_1
class TestSLAAlertRouter:
    """Test suite for SLAAlertRouter (Wave 3.1)"""
    
    def test_define_sla_thresholds(
        self,
        test_organisation_id,
        create_qa_evidence
    ):
        """
        Test SLA threshold definition for operations.
        
        Verifies:
        - SLA creation with P95/P99 thresholds
        - Organisation isolation
        - Threshold retrieval
        """
        from foreman.cross_cutting.sla_alert_router import SLAAlertRouter
        
        router = SLAAlertRouter(organisation_id=test_organisation_id)
        
        # Define SLA for API calls
        router.define_sla(
            operation_name="api_request",
            p95_threshold_ms=180.0,
            p99_threshold_ms=230.0,
            avg_threshold_ms=100.0,
            severity="HIGH"
        )
        
        # Retrieve SLA
        sla = router.get_sla_definition("api_request")
        
        assert sla is not None, "SLA must be retrievable"
        assert sla["operation_name"] == "api_request"
        assert sla["p95_threshold_ms"] == 180.0
        assert sla["p99_threshold_ms"] == 230.0
        assert sla["avg_threshold_ms"] == 100.0
        assert sla["severity"] == "HIGH"
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_SLA_DEFINITION",
            "PASS",
            {
                "operation_name": "api_request",
                "p95_threshold": 180.0,
                "p99_threshold": 230.0,
                "sla_defined": True
            }
        )
    
    def test_sla_compliance_check_passing(
        self,
        test_organisation_id,
        create_qa_evidence
    ):
        """
        Test SLA compliance check when metrics are within thresholds.
        
        Verifies:
        - Compliant metrics pass check
        - No violations generated
        - Proper compliance reporting
        """
        from foreman.cross_cutting.sla_alert_router import SLAAlertRouter
        
        router = SLAAlertRouter(organisation_id=test_organisation_id)
        
        # Define SLA
        router.define_sla(
            operation_name="data_fetch",
            p95_threshold_ms=150.0,
            p99_threshold_ms=200.0,
            severity="MEDIUM"
        )
        
        # Check compliance with good metrics
        metrics = {
            "p50_ms": 50.0,
            "p95_ms": 120.0,  # Under threshold
            "p99_ms": 180.0,  # Under threshold
            "avg_ms": 75.0,
            "sample_count": 100
        }
        
        result = router.check_sla_compliance(
            operation_name="data_fetch",
            metrics=metrics,
            trace_id="trace-compliant-001"
        )
        
        assert result["compliant"] == True, "Metrics should be compliant"
        assert len(result["violations"]) == 0, "No violations should be found"
        assert result["operation_name"] == "data_fetch"
        assert result["trace_id"] == "trace-compliant-001"
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_SLA_COMPLIANCE_PASS",
            "PASS",
            {
                "operation_name": "data_fetch",
                "compliant": True,
                "violations": 0
            }
        )
    
    def test_sla_compliance_check_failing(
        self,
        test_organisation_id,
        create_qa_evidence
    ):
        """
        Test SLA compliance check when metrics violate thresholds.
        
        Verifies:
        - Violations detected correctly
        - Violation details captured
        - Multiple violations handled
        """
        from foreman.cross_cutting.sla_alert_router import SLAAlertRouter
        
        router = SLAAlertRouter(organisation_id=test_organisation_id)
        
        # Define SLA with strict thresholds
        router.define_sla(
            operation_name="database_query",
            p95_threshold_ms=100.0,
            p99_threshold_ms=150.0,
            avg_threshold_ms=50.0,
            severity="CRITICAL"
        )
        
        # Check compliance with bad metrics (violating all thresholds)
        metrics = {
            "p50_ms": 75.0,
            "p95_ms": 180.0,  # Exceeds threshold by 80ms
            "p99_ms": 250.0,  # Exceeds threshold by 100ms
            "avg_ms": 90.0,   # Exceeds threshold by 40ms
            "sample_count": 50
        }
        
        result = router.check_sla_compliance(
            operation_name="database_query",
            metrics=metrics,
            trace_id="trace-violation-001"
        )
        
        assert result["compliant"] == False, "Metrics should be non-compliant"
        assert len(result["violations"]) == 3, "Should detect 3 violations"
        
        # Verify violation details
        violations_by_metric = {v["metric"]: v for v in result["violations"]}
        
        assert "p95" in violations_by_metric
        assert violations_by_metric["p95"]["actual"] == 180.0
        assert violations_by_metric["p95"]["threshold"] == 100.0
        assert violations_by_metric["p95"]["exceeded_by"] == 80.0
        
        assert "p99" in violations_by_metric
        assert violations_by_metric["p99"]["actual"] == 250.0
        
        assert "avg" in violations_by_metric
        assert violations_by_metric["avg"]["actual"] == 90.0
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_SLA_COMPLIANCE_FAIL",
            "PASS",
            {
                "operation_name": "database_query",
                "compliant": False,
                "violations": len(result["violations"])
            }
        )
    
    def test_alert_generation_for_violation(
        self,
        test_organisation_id,
        create_qa_evidence
    ):
        """
        Test alert creation when SLA is violated.
        
        Verifies:
        - Alert generation from compliance result
        - Alert contains all necessary context
        - Organisation ID isolation
        """
        from foreman.cross_cutting.sla_alert_router import SLAAlertRouter
        
        router = SLAAlertRouter(organisation_id=test_organisation_id)
        
        # Define SLA
        router.define_sla(
            operation_name="api_endpoint",
            p95_threshold_ms=200.0,
            severity="HIGH"
        )
        
        # Check compliance (will fail)
        metrics = {"p95_ms": 350.0}
        compliance = router.check_sla_compliance(
            operation_name="api_endpoint",
            metrics=metrics,
            trace_id="trace-alert-001"
        )
        
        # Create alert
        alert = router.create_alert_for_violation(
            compliance_result=compliance,
            additional_context={"endpoint": "/api/conversations"}
        )
        
        assert "alert_id" in alert, "Alert should be created"
        assert "alert_id" in alert, "Alert must have ID"
        assert alert["organisation_id"] == test_organisation_id
        assert alert["alert_type"] == "SLA_VIOLATION"
        assert alert["operation_name"] == "api_endpoint"
        assert alert["severity"] == "HIGH"
        assert alert["trace_id"] == "trace-alert-001"
        assert alert["status"] == "OPEN"
        assert len(alert["violations"]) > 0
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_ALERT_GENERATION",
            "PASS",
            {
                "alert_id": alert["alert_id"],
                "severity": alert["severity"],
                "violations": len(alert["violations"])
            }
        )
    
    def test_alert_routing_by_severity(
        self,
        test_organisation_id,
        test_user_id,
        create_qa_evidence
    ):
        """
        Test alert routing based on severity with audit logging.
        
        Verifies:
        - Different channels for different severities
        - Audit trail integration
        - Trace correlation in audit
        """
        from foreman.cross_cutting.sla_alert_router import SLAAlertRouter
        from foreman.cross_cutting.audit_logger import AuditLogger
        
        router = SLAAlertRouter(organisation_id=test_organisation_id)
        logger = AuditLogger(organisation_id=test_organisation_id)
        
        # Test CRITICAL severity routing
        router.define_sla(
            operation_name="critical_op",
            p95_threshold_ms=50.0,
            severity="CRITICAL"
        )
        
        metrics = {"p95_ms": 100.0}
        compliance = router.check_sla_compliance("critical_op", metrics, "trace-001")
        alert = router.create_alert_for_violation(compliance)
        
        # Route alert with audit
        routing = router.route_alert(alert, audit_logger=logger)
        
        assert "escalation" in routing["channels"], \
            "CRITICAL alerts must route to escalation"
        assert routing["escalation_priority"] == "IMMEDIATE"
        assert routing["audit_logged"] == True, \
            "Alert must be logged to audit trail"
        assert "audit_entry_id" in routing
        
        # Test HIGH severity routing
        router.define_sla(
            operation_name="high_op",
            p95_threshold_ms=100.0,
            severity="HIGH"
        )
        
        metrics = {"p95_ms": 150.0}
        compliance = router.check_sla_compliance("high_op", metrics)
        alert = router.create_alert_for_violation(compliance)
        routing = router.route_alert(alert, audit_logger=logger)
        
        assert "notification" in routing["channels"]
        assert routing["escalation_priority"] == "HIGH"
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_ALERT_ROUTING",
            "PASS",
            {
                "critical_channels": 3,  # escalation, notification, dashboard
                "high_channels": 2,       # notification, dashboard
                "audit_logged": True
            }
        )
    
    def test_violation_lifecycle_management(
        self,
        test_organisation_id,
        test_user_id,
        create_qa_evidence
    ):
        """
        Test violation status transitions (OPEN → ACKNOWLEDGED → RESOLVED).
        
        Verifies:
        - Violation acknowledgment
        - Violation resolution
        - Status tracking
        """
        from foreman.cross_cutting.sla_alert_router import SLAAlertRouter
        
        router = SLAAlertRouter(organisation_id=test_organisation_id)
        
        # Create violation
        router.define_sla("test_op", p95_threshold_ms=100.0, severity="MEDIUM")
        metrics = {"p95_ms": 150.0}
        compliance = router.check_sla_compliance("test_op", metrics)
        alert = router.create_alert_for_violation(compliance)
        
        alert_id = alert["alert_id"]
        
        # Initially OPEN
        violations = router.get_all_violations(status="OPEN")
        assert len(violations) == 1
        assert violations[0]["alert_id"] == alert_id
        
        # Acknowledge violation
        ack_result = router.acknowledge_violation(
            alert_id=alert_id,
            acknowledged_by=test_user_id
        )
        assert ack_result == True, "Acknowledgment should succeed"
        
        # Verify status changed
        ack_violations = router.get_all_violations(status="ACKNOWLEDGED")
        assert len(ack_violations) == 1
        assert ack_violations[0]["acknowledged_by"] == test_user_id
        
        # Resolve violation
        resolve_result = router.resolve_violation(
            alert_id=alert_id,
            resolved_by=test_user_id,
            resolution_notes="Latency improved after cache optimization"
        )
        assert resolve_result == True, "Resolution should succeed"
        
        # Verify status changed
        resolved_violations = router.get_all_violations(status="RESOLVED")
        assert len(resolved_violations) == 1
        assert resolved_violations[0]["resolved_by"] == test_user_id
        assert "cache optimization" in resolved_violations[0]["resolution_notes"]
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_VIOLATION_LIFECYCLE",
            "PASS",
            {
                "alert_id": alert_id,
                "acknowledged": True,
                "resolved": True
            }
        )
    
    def test_violation_summary_statistics(
        self,
        test_organisation_id,
        test_user_id,
        create_qa_evidence
    ):
        """
        Test violation summary and statistics.
        
        Verifies:
        - Count by status
        - Count by severity
        - Operations affected list
        """
        from foreman.cross_cutting.sla_alert_router import SLAAlertRouter
        
        router = SLAAlertRouter(organisation_id=test_organisation_id)
        
        # Create multiple violations
        router.define_sla("op1", p95_threshold_ms=100.0, severity="CRITICAL")
        router.define_sla("op2", p95_threshold_ms=100.0, severity="HIGH")
        router.define_sla("op3", p95_threshold_ms=100.0, severity="MEDIUM")
        
        metrics = {"p95_ms": 200.0}
        
        # Create 3 violations
        for op_name in ["op1", "op2", "op3"]:
            compliance = router.check_sla_compliance(op_name, metrics)
            router.create_alert_for_violation(compliance)
        
        # Acknowledge one
        violations = router.get_all_violations()
        router.acknowledge_violation(violations[0]["alert_id"], test_user_id)
        
        # Get summary
        summary = router.get_violation_summary()
        
        assert summary["total_violations"] == 3
        assert summary["by_status"]["OPEN"] == 2
        assert summary["by_status"]["ACKNOWLEDGED"] == 1
        assert summary["by_severity"]["CRITICAL"] == 1
        assert summary["by_severity"]["HIGH"] == 1
        assert summary["by_severity"]["MEDIUM"] == 1
        assert len(summary["operations_affected"]) == 3
        assert "op1" in summary["operations_affected"]
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_VIOLATION_SUMMARY",
            "PASS",
            {
                "total_violations": summary["total_violations"],
                "operations_affected": len(summary["operations_affected"])
            }
        )
    
    def test_tenant_isolation_for_sla(
        self,
        create_qa_evidence
    ):
        """
        Test that SLA definitions and violations are tenant-isolated.
        
        Verifies:
        - Organisation isolation
        - No cross-tenant leakage
        """
        from foreman.cross_cutting.sla_alert_router import SLAAlertRouter
        
        org1_id = "org-sla-001"
        org2_id = "org-sla-002"
        
        router1 = SLAAlertRouter(organisation_id=org1_id)
        router2 = SLAAlertRouter(organisation_id=org2_id)
        
        # Define SLA for org1
        router1.define_sla("op1", p95_threshold_ms=100.0, severity="HIGH")
        
        # Verify org2 cannot see org1's SLA
        org2_sla = router2.get_sla_definition("op1")
        assert org2_sla is None, "Org2 must not see Org1's SLA"
        
        # Create violation in org1
        metrics = {"p95_ms": 200.0}
        compliance = router1.check_sla_compliance("op1", metrics)
        router1.create_alert_for_violation(compliance)
        
        # Verify org2 cannot see org1's violations
        org2_violations = router2.get_all_violations()
        assert len(org2_violations) == 0, "Org2 must not see Org1's violations"
        
        # Verify org1 can see its own violations
        org1_violations = router1.get_all_violations()
        assert len(org1_violations) >= 1, "Org1 should see its violations"
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_SLA_TENANT_ISOLATION",
            "PASS",
            {
                "org1_violations": len(org1_violations),
                "org2_violations": len(org2_violations),
                "isolation_verified": True
            }
        )
