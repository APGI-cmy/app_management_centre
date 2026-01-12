"""
Tests for Wave 3.1 Telemetry Tracer

Tests telemetry infrastructure including:
- End-to-end tracing with tenant isolation
- Span/trace correlation
- P95/P99 latency calculation
- Audit trail integration
"""

import pytest
from datetime import datetime, timezone
import time

UTC = timezone.utc


@pytest.mark.wave3
@pytest.mark.subwave_3_1
class TestTelemetryTracer:
    """Test suite for TelemetryTracer (Wave 3.1)"""
    
    def test_start_trace_with_organisation_id(
        self,
        test_organisation_id,
        create_qa_evidence
    ):
        """
        Test that traces are created with organisation_id for tenant isolation.
        
        Verifies:
        - Trace ID generation
        - Organisation ID capture
        - Trace metadata storage
        """
        from foreman.cross_cutting.telemetry_tracer import TelemetryTracer
        
        tracer = TelemetryTracer(organisation_id=test_organisation_id)
        
        # Start a trace
        trace_id = tracer.start_trace(
            operation_name="conversation_creation",
            metadata={"user_id": "user-123", "conversation_type": "support"}
        )
        
        # Verify trace ID generated
        assert trace_id is not None, "Trace ID must be generated"
        assert trace_id.startswith("trace-"), "Trace ID must have correct prefix"
        
        # Retrieve trace
        trace = tracer.get_trace(trace_id)
        
        # Verify organisation ID isolation
        assert trace is not None, "Trace must be retrievable"
        assert trace["organisation_id"] == test_organisation_id, \
            "Trace must be isolated by organisation_id"
        
        # Verify metadata captured
        assert trace["operation_name"] == "conversation_creation", \
            "Operation name must be captured"
        assert trace["metadata"]["user_id"] == "user-123", \
            "Metadata must be preserved"
        
        # Verify trace is active
        active_traces = tracer.get_active_traces()
        assert len(active_traces) == 1, "Trace should be active"
        assert active_traces[0]["trace_id"] == trace_id, \
            "Active trace should match created trace"
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_TRACE_CREATION",
            "PASS",
            {
                "trace_id": trace_id,
                "organisation_id": test_organisation_id,
                "tenant_isolated": True
            }
        )
    
    def test_span_creation_and_hierarchy(
        self,
        test_organisation_id,
        create_qa_evidence
    ):
        """
        Test span creation with parent-child relationships.
        
        Verifies:
        - Span ID generation
        - Parent span relationships
        - Nested span support
        """
        from foreman.cross_cutting.telemetry_tracer import TelemetryTracer
        
        tracer = TelemetryTracer(organisation_id=test_organisation_id)
        
        # Start trace
        trace_id = tracer.start_trace(operation_name="api_request")
        
        # Start root span
        root_span = tracer.start_span(
            trace_id=trace_id,
            operation_name="handle_request",
            metadata={"endpoint": "/api/conversations"}
        )
        
        assert root_span is not None, "Root span must be created"
        assert root_span.trace_id == trace_id, "Span must reference trace"
        assert root_span.parent_span_id is None, "Root span has no parent"
        
        # Start child span
        child_span = tracer.start_span(
            trace_id=trace_id,
            operation_name="database_query",
            parent_span_id=root_span.span_id,
            metadata={"query_type": "SELECT"}
        )
        
        assert child_span.parent_span_id == root_span.span_id, \
            "Child span must reference parent"
        
        # Finish spans
        tracer.finish_span(child_span, status="SUCCESS")
        tracer.finish_span(root_span, status="SUCCESS")
        
        # Verify span completion
        assert child_span.end_time is not None, "Child span must have end time"
        assert child_span.duration_ms is not None, "Child span must have duration"
        assert child_span.duration_ms > 0, "Duration must be positive"
        
        # Get all spans for trace
        spans = tracer.get_spans_for_trace(trace_id)
        assert len(spans) == 2, "Both spans should be retrievable"
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_SPAN_HIERARCHY",
            "PASS",
            {
                "root_span_id": root_span.span_id,
                "child_span_id": child_span.span_id,
                "hierarchy_preserved": True
            }
        )
    
    def test_trace_correlation_with_audit(
        self,
        test_organisation_id,
        test_user_id,
        create_qa_evidence
    ):
        """
        Test trace correlation with audit logging (QA-171 integration).
        
        Verifies:
        - Audit context generation
        - Trace/span correlation IDs
        - Organisation ID propagation
        """
        from foreman.cross_cutting.telemetry_tracer import TelemetryTracer
        from foreman.cross_cutting.audit_logger import AuditLogger
        
        tracer = TelemetryTracer(organisation_id=test_organisation_id)
        logger = AuditLogger(organisation_id=test_organisation_id)
        
        # Start trace and span
        trace_id = tracer.start_trace(operation_name="governance_validation")
        span = tracer.start_span(
            trace_id=trace_id,
            operation_name="rule_check"
        )
        
        # Create audit context
        audit_context = tracer.create_audit_context(
            trace_id=trace_id,
            span_id=span.span_id
        )
        
        # Verify audit context
        assert audit_context["trace_id"] == trace_id, \
            "Audit context must include trace_id"
        assert audit_context["span_id"] == span.span_id, \
            "Audit context must include span_id"
        assert audit_context["organisation_id"] == test_organisation_id, \
            "Audit context must include organisation_id"
        
        # Log governance event with trace correlation
        log_entry = logger.log_governance_event(
            actor=test_user_id,
            action="RULE_VALIDATED",
            target="BUILD_PHILOSOPHY.md",
            outcome="PASS",
            metadata=audit_context  # Include trace correlation
        )
        
        # Verify correlation
        assert log_entry["metadata"]["trace_id"] == trace_id, \
            "Audit log must correlate with trace"
        assert log_entry["metadata"]["span_id"] == span.span_id, \
            "Audit log must correlate with span"
        
        # Finish span and trace
        tracer.finish_span(span)
        tracer.finish_trace(trace_id)
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_AUDIT_CORRELATION",
            "PASS",
            {
                "trace_id": trace_id,
                "span_id": span.span_id,
                "audit_entry_id": log_entry.get("entry_id"),
                "correlation_verified": True
            }
        )
    
    def test_tenant_isolation_enforcement(
        self,
        create_qa_evidence
    ):
        """
        Test that traces from different organisations are completely isolated.
        
        Verifies:
        - Tenant isolation boundary
        - No cross-organisation leakage
        - Organisation-specific trace retrieval
        """
        from foreman.cross_cutting.telemetry_tracer import TelemetryTracer
        
        org_1_id = "org-001"
        org_2_id = "org-002"
        
        tracer_1 = TelemetryTracer(organisation_id=org_1_id)
        tracer_2 = TelemetryTracer(organisation_id=org_2_id)
        
        # Create traces for both orgs
        trace_1 = tracer_1.start_trace(operation_name="org1_operation")
        trace_2 = tracer_2.start_trace(operation_name="org2_operation")
        
        # Verify org 1 can only see its trace
        org_1_traces = tracer_1.get_all_traces()
        assert len(org_1_traces) >= 1, "Org 1 should see at least its trace"
        org_1_trace_ids = [t["trace_id"] for t in org_1_traces]
        assert trace_1 in org_1_trace_ids, "Org 1 should see its own trace"
        
        # Verify org 2 can only see its trace
        org_2_traces = tracer_2.get_all_traces()
        assert len(org_2_traces) >= 1, "Org 2 should see at least its trace"
        org_2_trace_ids = [t["trace_id"] for t in org_2_traces]
        assert trace_2 in org_2_trace_ids, "Org 2 should see its own trace"
        
        # Verify cross-organisation isolation
        org_1_cannot_see_trace_2 = tracer_1.get_trace(trace_2)
        assert org_1_cannot_see_trace_2 is None, \
            "Org 1 must not see Org 2's trace"
        
        org_2_cannot_see_trace_1 = tracer_2.get_trace(trace_1)
        assert org_2_cannot_see_trace_1 is None, \
            "Org 2 must not see Org 1's trace"
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_TENANT_ISOLATION",
            "PASS",
            {
                "org_1_trace_count": len(org_1_traces),
                "org_2_trace_count": len(org_2_traces),
                "isolation_verified": True
            }
        )
    
    def test_p95_p99_latency_calculation(
        self,
        test_organisation_id,
        create_qa_evidence
    ):
        """
        Test P95 and P99 latency percentile calculations.
        
        Verifies:
        - Latency metric collection
        - Percentile calculation accuracy
        - Operation-specific metrics
        """
        from foreman.cross_cutting.telemetry_tracer import TelemetryTracer
        import time
        
        tracer = TelemetryTracer(organisation_id=test_organisation_id)
        
        # Create multiple traces with varying durations
        durations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # ms
        
        for i, duration_ms in enumerate(durations):
            trace_id = tracer.start_trace(
                operation_name="api_call",
                metadata={"iteration": i}
            )
            
            # Simulate work (convert ms to seconds)
            time.sleep(duration_ms / 1000.0)
            
            tracer.finish_trace(trace_id, status="SUCCESS")
        
        # Calculate latency metrics
        metrics = tracer.get_latency_metrics(operation_name="api_call")
        
        # Verify metrics structure
        assert metrics is not None, "Metrics must be calculated"
        assert "p50_ms" in metrics, "P50 must be calculated"
        assert "p95_ms" in metrics, "P95 must be calculated"
        assert "p99_ms" in metrics, "P99 must be calculated"
        assert "sample_count" in metrics, "Sample count must be included"
        
        # Verify sample count
        assert metrics["sample_count"] == 10, \
            "All 10 traces should be counted"
        
        # Verify percentile calculations are reasonable
        # P50 should be around 50-60ms (median of 10-100)
        assert 40 <= metrics["p50_ms"] <= 70, \
            f"P50 should be around 50-60ms, got {metrics['p50_ms']}"
        
        # P95 should be around 95ms (95th percentile of 10-100)
        assert metrics["p95_ms"] >= metrics["p50_ms"], \
            "P95 should be >= P50"
        assert 85 <= metrics["p95_ms"] <= 105, \
            f"P95 should be around 95ms, got {metrics['p95_ms']}"
        
        # P99 should be highest value
        assert metrics["p99_ms"] >= metrics["p95_ms"], \
            "P99 should be >= P95"
        
        # Verify min/max/avg
        assert metrics["min_ms"] is not None, "Min latency must be calculated"
        assert metrics["max_ms"] is not None, "Max latency must be calculated"
        assert metrics["avg_ms"] is not None, "Avg latency must be calculated"
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_LATENCY_METRICS",
            "PASS",
            {
                "p50_ms": metrics["p50_ms"],
                "p95_ms": metrics["p95_ms"],
                "p99_ms": metrics["p99_ms"],
                "sample_count": metrics["sample_count"]
            }
        )
    
    def test_span_events_and_metadata(
        self,
        test_organisation_id,
        create_qa_evidence
    ):
        """
        Test span event tracking and metadata enrichment.
        
        Verifies:
        - Event recording within spans
        - Event timestamps
        - Event attributes
        """
        from foreman.cross_cutting.telemetry_tracer import TelemetryTracer
        
        tracer = TelemetryTracer(organisation_id=test_organisation_id)
        
        # Start trace and span
        trace_id = tracer.start_trace(operation_name="data_processing")
        span = tracer.start_span(
            trace_id=trace_id,
            operation_name="transform_data"
        )
        
        # Add events to span
        span.add_event("validation_start", {"record_count": 100})
        span.add_event("validation_complete", {"errors": 0})
        span.add_event("transformation_start", {"output_format": "JSON"})
        span.add_event("transformation_complete", {"bytes_written": 1024})
        
        # Verify events
        assert len(span.events) == 4, "All events should be recorded"
        
        # Verify first event
        event_1 = span.events[0]
        assert event_1["name"] == "validation_start", \
            "Event name must be recorded"
        assert event_1["attributes"]["record_count"] == 100, \
            "Event attributes must be preserved"
        assert "timestamp" in event_1, \
            "Event must have timestamp"
        
        # Finish span
        tracer.finish_span(span)
        
        # Verify span dict includes events
        span_dict = span.to_dict()
        assert "events" in span_dict, "Span dict must include events"
        assert len(span_dict["events"]) == 4, \
            "All events must be in span dict"
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_SPAN_EVENTS",
            "PASS",
            {
                "span_id": span.span_id,
                "event_count": len(span.events),
                "events_captured": True
            }
        )
    
    def test_trace_completion_and_status(
        self,
        test_organisation_id,
        create_qa_evidence
    ):
        """
        Test trace lifecycle from start to finish.
        
        Verifies:
        - Trace status transitions
        - Duration calculation
        - Active vs completed traces
        """
        from foreman.cross_cutting.telemetry_tracer import TelemetryTracer
        import time
        
        tracer = TelemetryTracer(organisation_id=test_organisation_id)
        
        # Start trace
        trace_id = tracer.start_trace(operation_name="e2e_flow")
        
        # Verify trace is active
        active = tracer.get_active_traces()
        active_ids = [t["trace_id"] for t in active]
        assert trace_id in active_ids, "Trace should be active"
        
        # Find our trace
        our_trace = [t for t in active if t["trace_id"] == trace_id][0]
        assert our_trace["status"] == "IN_PROGRESS", \
            "Active trace should have IN_PROGRESS status"
        
        # Simulate work
        time.sleep(0.1)  # 100ms
        
        # Finish trace with success
        tracer.finish_trace(trace_id, status="SUCCESS")
        
        # Verify trace is no longer active
        active_after = tracer.get_active_traces()
        active_ids_after = [t["trace_id"] for t in active_after]
        assert trace_id not in active_ids_after, \
            "Trace should not be active after completion"
        
        # Retrieve completed trace
        trace = tracer.get_trace(trace_id)
        assert trace is not None, "Completed trace should be retrievable"
        assert trace["status"] == "SUCCESS", \
            "Trace should have SUCCESS status"
        assert trace["end_time"] is not None, \
            "Completed trace must have end_time"
        assert trace["total_duration_ms"] is not None, \
            "Completed trace must have duration"
        assert trace["total_duration_ms"] >= 100, \
            "Duration should reflect work time"
        
        # Create evidence
        evidence = create_qa_evidence(
            "WAVE_3.1_TRACE_LIFECYCLE",
            "PASS",
            {
                "trace_id": trace_id,
                "final_status": trace["status"],
                "duration_ms": trace["total_duration_ms"]
            }
        )
