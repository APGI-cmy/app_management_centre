"""
Tests for Runtime Telemetry and Audit Trail (Wave 3.1)

Purpose: Validate end-to-end telemetry and audit functionality
Authority: Wave 3.1 - Runtime Telemetry & Audit Trail Hardening
QA Coverage: QA-171 to QA-176 (Audit Logger requirements)

Test Categories:
- Telemetry span tracking
- Metrics collection
- Audit trail logging
- Tenant isolation enforcement
- Trace correlation
- SLA breach detection
"""

import pytest
from datetime import datetime, UTC, timedelta
from runtime.audit import (
    get_telemetry_collector,
    get_runtime_audit_trail,
    clear_telemetry,
    clear_audit_trail,
    SpanStatus,
    TelemetryLevel,
    AuditSeverity,
    AuditCategory
)


@pytest.fixture
def telemetry_collector():
    """Provide a fresh telemetry collector for each test"""
    clear_telemetry()
    collector = get_telemetry_collector()
    yield collector
    clear_telemetry()


@pytest.fixture
def audit_trail():
    """Provide a fresh audit trail for each test"""
    clear_audit_trail()
    trail = get_runtime_audit_trail()
    yield trail
    clear_audit_trail()


@pytest.fixture
def test_org_id():
    """Test organisation ID"""
    return "test-org-001"


@pytest.fixture
def test_actor():
    """Test actor/user ID"""
    return "test-user-001"


class TestTelemetrySpans:
    """Tests for telemetry span tracking"""
    
    def test_start_and_complete_span(self, telemetry_collector, test_org_id):
        """Test basic span lifecycle"""
        # Start a span
        span = telemetry_collector.start_span(
            operation="test_operation",
            organisation_id=test_org_id,
            metadata={"key": "value"}
        )
        
        assert span is not None
        assert span.operation == "test_operation"
        assert span.organisation_id == test_org_id
        assert span.status is None  # Not yet completed
        assert span.metadata == {"key": "value"}
        
        # Complete the span
        completed = telemetry_collector.complete_span(
            span_id=span.span_id,
            status=SpanStatus.SUCCESS,
            metadata={"result": "success"}
        )
        
        assert completed is not None
        assert completed.status == SpanStatus.SUCCESS
        assert completed.end_time is not None
        assert completed.metadata["result"] == "success"
        assert completed.duration_ms() is not None
        assert completed.duration_ms() > 0
    
    def test_span_with_errors(self, telemetry_collector, test_org_id):
        """Test span with error tracking"""
        span = telemetry_collector.start_span(
            operation="failing_operation",
            organisation_id=test_org_id
        )
        
        # Add errors to the span
        span.add_error(
            error_type="ValueError",
            error_message="Invalid input",
            details={"input": "bad_value"}
        )
        
        # Complete with failure status
        completed = telemetry_collector.complete_span(
            span_id=span.span_id,
            status=SpanStatus.FAILURE
        )
        
        assert completed.status == SpanStatus.FAILURE
        assert len(completed.errors) == 1
        assert completed.errors[0]["type"] == "ValueError"
    
    def test_nested_spans_with_trace_id(self, telemetry_collector, test_org_id):
        """Test nested spans with parent-child relationship"""
        # Parent span
        parent_span = telemetry_collector.start_span(
            operation="parent_operation",
            organisation_id=test_org_id
        )
        
        # Child span with parent reference
        child_span = telemetry_collector.start_span(
            operation="child_operation",
            organisation_id=test_org_id,
            parent_span_id=parent_span.span_id,
            trace_id=parent_span.trace_id
        )
        
        assert child_span.parent_span_id == parent_span.span_id
        assert child_span.trace_id == parent_span.trace_id
        
        # Complete both spans
        telemetry_collector.complete_span(child_span.span_id, SpanStatus.SUCCESS)
        telemetry_collector.complete_span(parent_span.span_id, SpanStatus.SUCCESS)
        
        # Query trace
        trace_summary = telemetry_collector.get_trace_summary(
            test_org_id,
            parent_span.trace_id
        )
        
        assert trace_summary["found"] is True
        assert trace_summary["span_count"] == 2
        assert "parent_operation" in trace_summary["operations"]
        assert "child_operation" in trace_summary["operations"]
    
    def test_tenant_isolation_in_spans(self, telemetry_collector):
        """Test that spans are properly isolated by organisation_id"""
        org1 = "org-001"
        org2 = "org-002"
        
        # Create spans for different organisations
        span1 = telemetry_collector.start_span("op1", org1)
        span2 = telemetry_collector.start_span("op2", org2)
        
        telemetry_collector.complete_span(span1.span_id, SpanStatus.SUCCESS)
        telemetry_collector.complete_span(span2.span_id, SpanStatus.SUCCESS)
        
        # Verify isolation
        org1_spans = telemetry_collector.get_spans(org1)
        org2_spans = telemetry_collector.get_spans(org2)
        
        assert len(org1_spans) == 1
        assert len(org2_spans) == 1
        assert org1_spans[0].organisation_id == org1
        assert org2_spans[0].organisation_id == org2


class TestTelemetryMetrics:
    """Tests for metrics collection"""
    
    def test_record_metric(self, telemetry_collector, test_org_id):
        """Test recording a simple metric"""
        metric = telemetry_collector.record_metric(
            metric_name="response_time",
            metric_value=125.5,
            metric_unit="ms",
            organisation_id=test_org_id,
            tags={"endpoint": "/api/users"},
            metadata={"method": "GET"}
        )
        
        assert metric.metric_name == "response_time"
        assert metric.metric_value == 125.5
        assert metric.metric_unit == "ms"
        assert metric.tags["endpoint"] == "/api/users"
    
    def test_query_metrics_by_name(self, telemetry_collector, test_org_id):
        """Test querying metrics by name"""
        # Record multiple metrics
        telemetry_collector.record_metric("cpu_usage", 45.0, "%", test_org_id)
        telemetry_collector.record_metric("memory_usage", 60.0, "%", test_org_id)
        telemetry_collector.record_metric("cpu_usage", 50.0, "%", test_org_id)
        
        # Query CPU metrics only
        cpu_metrics = telemetry_collector.get_metrics(
            test_org_id,
            metric_name="cpu_usage"
        )
        
        assert len(cpu_metrics) == 2
        assert all(m.metric_name == "cpu_usage" for m in cpu_metrics)
    
    def test_tenant_isolation_in_metrics(self, telemetry_collector):
        """Test metric isolation between organisations"""
        org1 = "org-001"
        org2 = "org-002"
        
        telemetry_collector.record_metric("metric1", 100.0, "units", org1)
        telemetry_collector.record_metric("metric2", 200.0, "units", org2)
        
        org1_metrics = telemetry_collector.get_metrics(org1)
        org2_metrics = telemetry_collector.get_metrics(org2)
        
        assert len(org1_metrics) == 1
        assert len(org2_metrics) == 1
        assert org1_metrics[0].organisation_id == org1
        assert org2_metrics[0].organisation_id == org2


class TestAuditTrail:
    """Tests for audit trail functionality (QA-171 to QA-176)"""
    
    def test_log_governance_event(self, audit_trail, test_org_id, test_actor):
        """
        QA-171: Log governance event
        
        Verify:
        - Timestamp capture (UTC)
        - Actor recording
        - Action and outcome logging
        - Immutability flag
        """
        entry = audit_trail.log_governance_event(
            organisation_id=test_org_id,
            actor=test_actor,
            action="VALIDATE_BUILD_PHILOSOPHY",
            outcome="PASS",
            resource="BUILD_PHILOSOPHY.md",
            metadata={"violations": 0, "warnings": 0}
        )
        
        assert entry.entry_id is not None
        assert entry.timestamp is not None
        assert entry.actor == test_actor
        assert entry.action == "VALIDATE_BUILD_PHILOSOPHY"
        assert entry.outcome == "PASS"
        assert entry.immutable is True
        assert entry.category == AuditCategory.GOVERNANCE
        assert entry.severity == AuditSeverity.COMPLIANCE
    
    def test_log_authority_event(self, audit_trail, test_org_id, test_actor):
        """
        QA-172: Log authority event
        
        Verify:
        - Permission check logging
        - Override detection
        - Complete audit trail
        """
        entry = audit_trail.log_authority_event(
            organisation_id=test_org_id,
            actor=test_actor,
            action="OVERRIDE_POLICY",
            outcome="SUCCESS",
            permission_check=True,
            override_used=True,
            resource="GOVERNANCE_RULE_X",
            metadata={"reason": "Emergency fix required"}
        )
        
        assert entry.category == AuditCategory.AUTHORITY
        assert entry.metadata["permission_check"] is True
        assert entry.metadata["override_used"] is True
        assert entry.severity == AuditSeverity.CRITICAL  # Because override was used
    
    def test_query_audit_log(self, audit_trail, test_org_id, test_actor):
        """
        QA-173: Query audit log
        
        Verify:
        - Time range queries
        - Actor filtering
        - Event type filtering
        """
        # Create multiple audit entries
        audit_trail.log_governance_event(
            test_org_id, test_actor, "ACTION_1", "SUCCESS"
        )
        audit_trail.log_governance_event(
            test_org_id, "another-actor", "ACTION_2", "SUCCESS"
        )
        audit_trail.log_authority_event(
            test_org_id, test_actor, "ACTION_3", "SUCCESS",
            permission_check=True, override_used=False
        )
        
        # Query by actor
        actor_entries = audit_trail.query_audit_log(
            test_org_id,
            actor=test_actor
        )
        assert len(actor_entries) == 2
        assert all(e.actor == test_actor for e in actor_entries)
        
        # Query by category
        gov_entries = audit_trail.query_audit_log(
            test_org_id,
            category=AuditCategory.GOVERNANCE
        )
        assert len(gov_entries) == 2
        assert all(e.category == AuditCategory.GOVERNANCE for e in gov_entries)
    
    def test_audit_log_immutability(self, audit_trail, test_org_id):
        """
        QA-174: Audit log immutability
        
        Verify:
        - Append-only structure
        - All entries marked immutable
        - No modifications possible
        """
        # Create audit entries
        entry = audit_trail.log_governance_event(
            test_org_id, "actor-1", "ACTION_1", "SUCCESS"
        )
        
        # Verify entry is immutable
        assert entry.immutable is True
        
        # Verify all entries in log are immutable
        assert audit_trail.verify_immutability(test_org_id) is True
    
    def test_tenant_isolation_in_audit(self, audit_trail):
        """Test audit log tenant isolation"""
        org1 = "org-001"
        org2 = "org-002"
        
        # Create entries for different organisations
        audit_trail.log_governance_event(org1, "actor-1", "ACTION_1", "SUCCESS")
        audit_trail.log_governance_event(org2, "actor-2", "ACTION_2", "SUCCESS")
        
        # Verify isolation
        org1_entries = audit_trail.query_audit_log(org1)
        org2_entries = audit_trail.query_audit_log(org2)
        
        assert len(org1_entries) == 1
        assert len(org2_entries) == 1
        assert org1_entries[0].organisation_id == org1
        assert org2_entries[0].organisation_id == org2
    
    def test_audit_statistics(self, audit_trail, test_org_id):
        """Test audit log statistics generation"""
        # Create various entries
        audit_trail.log_governance_event(test_org_id, "actor", "A1", "SUCCESS")
        audit_trail.log_authority_event(
            test_org_id, "actor", "A2", "SUCCESS",
            permission_check=True, override_used=False
        )
        audit_trail.log_sla_breach(
            test_org_id, "operation", 250.0, 200.0
        )
        
        stats = audit_trail.get_audit_statistics(test_org_id)
        
        assert stats["total_entries"] == 3
        assert "governance" in stats["by_category"]
        assert "authority" in stats["by_category"]
        assert "sla" in stats["by_category"]


class TestSLABreachDetection:
    """Tests for SLA breach detection and alerting"""
    
    def test_log_sla_breach(self, audit_trail, test_org_id):
        """Test SLA breach logging"""
        entry = audit_trail.log_sla_breach(
            organisation_id=test_org_id,
            operation="api_request",
            duration_ms=250.0,
            threshold_ms=200.0,
            metadata={"endpoint": "/api/users"}
        )
        
        assert entry.category == AuditCategory.SLA
        assert entry.severity == AuditSeverity.WARNING
        assert entry.metadata["duration_ms"] == 250.0
        assert entry.metadata["threshold_ms"] == 200.0
        assert entry.metadata["breach_amount_ms"] == 50.0


class TestTenantIsolationEnforcement:
    """Tests for tenant isolation tracking"""
    
    def test_log_isolation_success(self, audit_trail, test_org_id):
        """Test successful tenant isolation enforcement"""
        entry = audit_trail.log_tenant_isolation_event(
            organisation_id=test_org_id,
            actor="SYSTEM",
            action="DATA_ACCESS",
            outcome="SUCCESS",
            isolation_verified=True,
            resource="user_data",
            metadata={"accessed_org": test_org_id}
        )
        
        assert entry.category == AuditCategory.TENANT_ISOLATION
        assert entry.severity == AuditSeverity.INFO
        assert entry.metadata["isolation_verified"] is True
    
    def test_log_isolation_violation(self, audit_trail, test_org_id):
        """Test detection of tenant isolation violation"""
        entry = audit_trail.log_tenant_isolation_event(
            organisation_id=test_org_id,
            actor="SYSTEM",
            action="DATA_ACCESS",
            outcome="BLOCKED",
            isolation_verified=False,
            resource="other_org_data",
            metadata={"attempted_access": "org-002"}
        )
        
        assert entry.category == AuditCategory.TENANT_ISOLATION
        assert entry.severity == AuditSeverity.CRITICAL
        assert entry.outcome == "ISOLATION_VIOLATION"


class TestTraceCorrelation:
    """Tests for trace correlation between telemetry and audit"""
    
    def test_audit_event_with_trace_correlation(
        self, telemetry_collector, audit_trail, test_org_id
    ):
        """Test that audit events can be correlated with telemetry spans"""
        # Start a telemetry span
        span = telemetry_collector.start_span(
            operation="governance_validation",
            organisation_id=test_org_id
        )
        
        # Log audit event with trace correlation
        audit_entry = audit_trail.log_governance_event(
            organisation_id=test_org_id,
            actor="system",
            action="VALIDATE",
            outcome="PASS",
            trace_id=span.trace_id
        )
        
        # Complete the span
        telemetry_collector.complete_span(span.span_id, SpanStatus.SUCCESS)
        
        # Verify correlation
        assert audit_entry.trace_id == span.trace_id
        
        # Verify we can query telemetry for this trace
        trace_summary = telemetry_collector.get_trace_summary(
            test_org_id,
            span.trace_id
        )
        assert trace_summary["found"] is True
        
        # Verify we can find the audit entry
        audit_entries = audit_trail.query_audit_log(test_org_id)
        correlated = [e for e in audit_entries if e.trace_id == span.trace_id]
        assert len(correlated) == 1
