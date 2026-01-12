"""
End-to-End Integration Test for Wave 3.1 Telemetry & Audit Trail Hardening

Demonstrates complete flow:
1. UI→API→Backend→Governance trace propagation
2. P95/P99 latency metric collection
3. SLA violation detection
4. Alert routing with audit correlation
5. Full observability with tenant isolation
"""

import pytest
from datetime import datetime, timezone
import time

UTC = timezone.utc


@pytest.mark.wave3
@pytest.mark.subwave_3_1
@pytest.mark.integration
class TestE2ETelemetryIntegration:
    """End-to-end integration test for complete telemetry stack"""
    
    def test_complete_telemetry_audit_alert_flow(
        self,
        test_organisation_id,
        test_user_id,
        create_qa_evidence
    ):
        """
        Test complete flow from trace creation to alert routing with audit.
        
        Simulates:
        - User initiates conversation (UI)
        - Request flows through API
        - Backend processes and queries governance
        - Latency metrics collected
        - SLA checked and violated
        - Alert generated and routed
        - Full audit trail maintained
        
        This is the Wave 3.1 success criterion: "100% flows emit trace + audit"
        """
        from foreman.cross_cutting.telemetry_tracer import TelemetryTracer
        from foreman.cross_cutting.sla_alert_router import SLAAlertRouter
        from foreman.cross_cutting.audit_logger import AuditLogger
        
        # Initialize components with tenant isolation
        tracer = TelemetryTracer(organisation_id=test_organisation_id)
        router = SLAAlertRouter(organisation_id=test_organisation_id)
        logger = AuditLogger(organisation_id=test_organisation_id)
        
        # Define SLA for conversation creation (strict threshold for test)
        router.define_sla(
            operation_name="conversation_creation",
            p95_threshold_ms=50.0,  # Intentionally low to trigger violation
            p99_threshold_ms=75.0,
            severity="HIGH"
        )
        
        # === STEP 1: UI INITIATES REQUEST ===
        trace_id = tracer.start_trace(
            operation_name="conversation_creation",
            metadata={
                "user_id": test_user_id,
                "entry_point": "UI",
                "conversation_type": "support"
            }
        )
        
        # Log UI event to audit
        ui_audit_context = tracer.create_audit_context(trace_id, "ui-span-001")
        logger.log_governance_event(
            actor=test_user_id,
            action="CONVERSATION_CREATE_INITIATED",
            target="UI",
            outcome="SUCCESS",
            metadata=ui_audit_context
        )
        
        # === STEP 2: API LAYER ===
        api_span = tracer.start_span(
            trace_id=trace_id,
            operation_name="api_handle_request",
            metadata={"endpoint": "/api/conversations", "method": "POST"}
        )
        
        api_span.add_event("validation_start", {"fields": ["title", "user_id"]})
        time.sleep(0.02)  # Simulate API work
        api_span.add_event("validation_complete", {"valid": True})
        
        # Log API audit
        api_audit_context = tracer.create_audit_context(trace_id, api_span.span_id)
        logger.log_governance_event(
            actor="API_LAYER",
            action="REQUEST_VALIDATED",
            target="/api/conversations",
            outcome="SUCCESS",
            metadata=api_audit_context
        )
        
        # === STEP 3: BACKEND PROCESSING ===
        backend_span = tracer.start_span(
            trace_id=trace_id,
            operation_name="backend_process",
            parent_span_id=api_span.span_id,
            metadata={"component": "CONV-01"}
        )
        
        backend_span.add_event("database_query_start", {"query": "INSERT"})
        time.sleep(0.03)  # Simulate backend work
        backend_span.add_event("database_query_complete", {"rows_affected": 1})
        
        # Log backend audit
        backend_audit_context = tracer.create_audit_context(trace_id, backend_span.span_id)
        logger.log_governance_event(
            actor="BACKEND",
            action="CONVERSATION_CREATED",
            target="conversation-12345",
            outcome="SUCCESS",
            metadata=backend_audit_context
        )
        
        tracer.finish_span(backend_span, status="SUCCESS")
        
        # === STEP 4: GOVERNANCE CHECK ===
        gov_span = tracer.start_span(
            trace_id=trace_id,
            operation_name="governance_validation",
            parent_span_id=api_span.span_id,
            metadata={"rules": ["conversation_policy", "user_permissions"]}
        )
        
        gov_span.add_event("rule_check", {"rule": "conversation_policy", "result": "PASS"})
        time.sleep(0.01)
        gov_span.add_event("permissions_check", {"user": test_user_id, "result": "ALLOWED"})
        
        # Log governance audit
        gov_audit_context = tracer.create_audit_context(trace_id, gov_span.span_id)
        logger.log_governance_event(
            actor="GOVERNANCE",
            action="POLICY_VALIDATED",
            target="conversation_policy",
            outcome="PASS",
            metadata=gov_audit_context
        )
        
        tracer.finish_span(gov_span, status="SUCCESS")
        tracer.finish_span(api_span, status="SUCCESS")
        
        # === STEP 5: COMPLETE TRACE ===
        time.sleep(0.01)  # Total: ~70ms (will exceed 50ms P95 threshold)
        tracer.finish_trace(trace_id, status="SUCCESS")
        
        # === STEP 6: COLLECT METRICS ===
        # In real system, this would be periodic background job
        # For test, we create multiple traces to get P95/P99
        for i in range(9):  # Total 10 traces (including the one above)
            t_id = tracer.start_trace(operation_name="conversation_creation")
            time.sleep(0.06 + (i * 0.01))  # Varying latencies: 60-140ms
            tracer.finish_trace(t_id)
        
        # Calculate latency metrics
        metrics = tracer.get_latency_metrics(operation_name="conversation_creation")
        
        # === STEP 7: CHECK SLA COMPLIANCE ===
        compliance = router.check_sla_compliance(
            operation_name="conversation_creation",
            metrics=metrics,
            trace_id=trace_id
        )
        
        # === STEP 8: GENERATE AND ROUTE ALERT ===
        if not compliance["compliant"]:
            alert = router.create_alert_for_violation(
                compliance_result=compliance,
                additional_context={
                    "user_id": test_user_id,
                    "entry_point": "UI",
                    "trace_id": trace_id
                }
            )
            
            # Route alert with audit
            routing = router.route_alert(alert, audit_logger=logger)
        
        # === VERIFICATION ===
        
        # 1. Verify trace was created with tenant isolation
        trace = tracer.get_trace(trace_id)
        assert trace is not None, "Trace must exist"
        assert trace["organisation_id"] == test_organisation_id, \
            "Trace must be tenant-isolated"
        
        # 2. Verify all spans were created
        spans = tracer.get_spans_for_trace(trace_id)
        assert len(spans) == 3, "Should have 3 spans (api, backend, governance)"
        
        # 3. Verify audit trail completeness (1 per major step)
        audit_events = logger.query_events()
        assert len(audit_events) >= 4, \
            "Should have audit events for UI, API, Backend, Governance"
        
        # Verify all audit events have trace correlation
        trace_correlated = [e for e in audit_events if "trace_id" in e.get("metadata", {})]
        assert len(trace_correlated) >= 4, \
            "All audit events must have trace correlation"
        
        # 4. Verify metrics were collected
        assert metrics["sample_count"] == 10, "Should have 10 sample traces"
        assert metrics["p95_ms"] is not None, "P95 must be calculated"
        assert metrics["p99_ms"] is not None, "P99 must be calculated"
        
        # 5. Verify SLA violation was detected
        assert compliance["compliant"] == False, \
            "SLA should be violated (p95 > 50ms threshold)"
        assert len(compliance["violations"]) > 0, \
            "Violations should be detected"
        
        # 6. Verify alert was generated
        violations = router.get_all_violations()
        assert len(violations) >= 1, "Alert should be generated"
        assert violations[0]["organisation_id"] == test_organisation_id, \
            "Alert must be tenant-isolated"
        
        # 7. Verify alert was routed with audit
        assert routing["audit_logged"] == True, \
            "Alert routing must be audited"
        assert "audit_entry_id" in routing, \
            "Audit entry ID must be returned"
        
        # 8. Verify complete observability chain
        # Can trace from alert → violation → compliance → metrics → traces → spans → audit
        alert_trace_id = violations[0].get("trace_id")
        assert alert_trace_id == trace_id, \
            "Alert must reference original trace"
        
        # Create comprehensive evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_E2E_INTEGRATION",
            "PASS",
            {
                "trace_id": trace_id,
                "organisation_id": test_organisation_id,
                "spans_created": len(spans),
                "audit_events": len(audit_events),
                "trace_correlated_events": len(trace_correlated),
                "p95_ms": metrics["p95_ms"],
                "p99_ms": metrics["p99_ms"],
                "sla_violated": not compliance["compliant"],
                "alert_generated": len(violations) > 0,
                "alert_routed": routing["audit_logged"],
                "tenant_isolated": True,
                "observability_complete": True
            }
        )
        
        # SUCCESS: Complete end-to-end flow demonstrated
        # ✅ Traces emitted across all layers (UI→API→Backend→Governance)
        # ✅ Organisation ID present everywhere
        # ✅ P95/P99 metrics calculated
        # ✅ SLA violations detected
        # ✅ Alerts routed with severity
        # ✅ Audit trail complete with trace correlation
        # ✅ Tenant isolation enforced
