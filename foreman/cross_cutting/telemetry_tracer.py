"""
Telemetry Tracer for Wave 3.1 - Runtime Telemetry & Audit Trail Hardening
QA Coverage: Extended support for QA-171 to QA-176 (audit trail with trace correlation)

Provides end-to-end tracing across UI→API→Backend→Governance flows with:
- Tenant isolation (organisation_id in all traces)
- Span/trace correlation
- P95/P99 latency tracking
- Integration with audit logger
"""

from datetime import datetime, UTC
from typing import Any
import uuid
import time

# In-memory storage for traces (tenant-isolated)
_traces = {}
_spans = {}
_active_traces = {}


def clear_all():
    """Clear all telemetry state for testing."""
    global _traces, _spans, _active_traces
    _traces = {}
    _spans = {}
    _active_traces = {}


class TelemetrySpan:
    """
    Represents a single span in a distributed trace.
    Each span tracks a specific operation with timing and context.
    """
    
    def __init__(
        self,
        span_id: str,
        trace_id: str,
        organisation_id: str,
        operation_name: str,
        parent_span_id: str | None = None,
        metadata: dict[str, Any] | None = None
    ):
        self.span_id = span_id
        self.trace_id = trace_id
        self.organisation_id = organisation_id
        self.operation_name = operation_name
        self.parent_span_id = parent_span_id
        self.metadata = metadata or {}
        self.start_time = datetime.now(UTC)
        self.end_time = None
        self.duration_ms = None
        self.status = "IN_PROGRESS"
        self.events = []
    
    def add_event(self, event_name: str, attributes: dict | None = None):
        """Add an event to the span."""
        self.events.append({
            "timestamp": datetime.now(UTC),
            "name": event_name,
            "attributes": attributes or {}
        })
    
    def finish(self, status: str = "SUCCESS"):
        """Finish the span and calculate duration."""
        self.end_time = datetime.now(UTC)
        self.duration_ms = (self.end_time - self.start_time).total_seconds() * 1000
        self.status = status
    
    def to_dict(self) -> dict[str, Any]:
        """Convert span to dictionary for storage/serialization."""
        return {
            "span_id": self.span_id,
            "trace_id": self.trace_id,
            "organisation_id": self.organisation_id,
            "operation_name": self.operation_name,
            "parent_span_id": self.parent_span_id,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "duration_ms": self.duration_ms,
            "status": self.status,
            "metadata": self.metadata,
            "events": self.events
        }


class TelemetryTracer:
    """
    End-to-end telemetry tracer with tenant isolation.
    
    Provides:
    - Distributed tracing across system components
    - Tenant-isolated traces (organisation_id)
    - Trace correlation for audit logging
    - Performance metrics (P95, P99 latency)
    """
    
    def __init__(self, organisation_id: str):
        """Initialize tracer for specific organisation."""
        self.organisation_id = organisation_id
        
        # Initialize org-specific storage
        if organisation_id not in _traces:
            _traces[organisation_id] = []
        if organisation_id not in _spans:
            _spans[organisation_id] = {}
        if organisation_id not in _active_traces:
            _active_traces[organisation_id] = {}
    
    def start_trace(
        self,
        operation_name: str,
        metadata: dict[str, Any] | None = None
    ) -> str:
        """
        Start a new distributed trace.
        
        Returns:
            trace_id: Unique identifier for the trace
        """
        trace_id = f"trace-{uuid.uuid4().hex[:16]}"
        
        trace_record = {
            "trace_id": trace_id,
            "organisation_id": self.organisation_id,
            "operation_name": operation_name,
            "start_time": datetime.now(UTC),
            "end_time": None,
            "total_duration_ms": None,
            "span_count": 0,
            "status": "IN_PROGRESS",
            "metadata": metadata or {}
        }
        
        _traces[self.organisation_id].append(trace_record)
        _active_traces[self.organisation_id][trace_id] = trace_record
        
        return trace_id
    
    def start_span(
        self,
        trace_id: str,
        operation_name: str,
        parent_span_id: str | None = None,
        metadata: dict[str, Any] | None = None
    ) -> TelemetrySpan:
        """
        Start a new span within a trace.
        
        Args:
            trace_id: ID of the parent trace
            operation_name: Name of the operation being traced
            parent_span_id: Optional parent span ID for nested spans
            metadata: Additional context/metadata
        
        Returns:
            TelemetrySpan: Active span object
        """
        span_id = f"span-{uuid.uuid4().hex[:12]}"
        
        span = TelemetrySpan(
            span_id=span_id,
            trace_id=trace_id,
            organisation_id=self.organisation_id,
            operation_name=operation_name,
            parent_span_id=parent_span_id,
            metadata=metadata
        )
        
        _spans[self.organisation_id][span_id] = span
        
        # Update trace span count
        if trace_id in _active_traces[self.organisation_id]:
            _active_traces[self.organisation_id][trace_id]["span_count"] += 1
        
        return span
    
    def finish_span(self, span: TelemetrySpan, status: str = "SUCCESS"):
        """Finish a span and record its completion."""
        span.finish(status)
    
    def finish_trace(self, trace_id: str, status: str = "SUCCESS"):
        """
        Finish a trace and calculate total duration.
        
        Args:
            trace_id: ID of the trace to finish
            status: Final status (SUCCESS, FAILURE, ERROR)
        """
        if trace_id in _active_traces[self.organisation_id]:
            trace = _active_traces[self.organisation_id][trace_id]
            trace["end_time"] = datetime.now(UTC)
            trace["total_duration_ms"] = (
                trace["end_time"] - trace["start_time"]
            ).total_seconds() * 1000
            trace["status"] = status
            
            # Remove from active traces
            del _active_traces[self.organisation_id][trace_id]
    
    def get_trace(self, trace_id: str) -> dict[str, Any] | None:
        """Retrieve a specific trace by ID."""
        for trace in _traces.get(self.organisation_id, []):
            if trace["trace_id"] == trace_id:
                return trace
        return None
    
    def get_spans_for_trace(self, trace_id: str) -> list[dict[str, Any]]:
        """Get all spans associated with a trace."""
        spans = []
        for span in _spans.get(self.organisation_id, {}).values():
            if span.trace_id == trace_id:
                spans.append(span.to_dict())
        return spans
    
    def get_all_traces(self) -> list[dict[str, Any]]:
        """Get all traces for this organisation."""
        return _traces.get(self.organisation_id, [])
    
    def calculate_percentile_latency(
        self,
        operation_name: str | None = None,
        percentile: float = 95.0
    ) -> float | None:
        """
        Calculate percentile latency (P50, P95, P99) for operations.
        
        Args:
            operation_name: Optional filter by operation name
            percentile: Percentile to calculate (default: 95.0)
        
        Returns:
            Latency in milliseconds at the specified percentile
        """
        durations = []
        
        # Collect durations from completed traces
        for trace in _traces.get(self.organisation_id, []):
            if trace.get("total_duration_ms") is not None:
                if operation_name is None or trace.get("operation_name") == operation_name:
                    durations.append(trace["total_duration_ms"])
        
        if not durations:
            return None
        
        # Sort durations
        durations.sort()
        
        # Calculate percentile index
        index = int(len(durations) * (percentile / 100.0))
        if index >= len(durations):
            index = len(durations) - 1
        
        return durations[index]
    
    def get_latency_metrics(
        self,
        operation_name: str | None = None
    ) -> dict[str, Any]:
        """
        Get comprehensive latency metrics for operations.
        
        Returns:
            Dictionary with P50, P95, P99, min, max, avg latencies
        """
        p50 = self.calculate_percentile_latency(operation_name, 50.0)
        p95 = self.calculate_percentile_latency(operation_name, 95.0)
        p99 = self.calculate_percentile_latency(operation_name, 99.0)
        
        # Calculate min, max, avg
        durations = []
        for trace in _traces.get(self.organisation_id, []):
            if trace.get("total_duration_ms") is not None:
                if operation_name is None or trace.get("operation_name") == operation_name:
                    durations.append(trace["total_duration_ms"])
        
        return {
            "operation_name": operation_name or "ALL",
            "p50_ms": p50,
            "p95_ms": p95,
            "p99_ms": p99,
            "min_ms": min(durations) if durations else None,
            "max_ms": max(durations) if durations else None,
            "avg_ms": sum(durations) / len(durations) if durations else None,
            "sample_count": len(durations)
        }
    
    def create_audit_context(self, trace_id: str, span_id: str) -> dict[str, Any]:
        """
        Create audit context with trace correlation.
        
        Links audit log entries to specific traces/spans for full observability.
        
        Returns:
            Dictionary with trace_id, span_id, organisation_id for audit logging
        """
        return {
            "trace_id": trace_id,
            "span_id": span_id,
            "organisation_id": self.organisation_id,
            "timestamp": datetime.now(UTC).isoformat()
        }
    
    def get_active_traces(self) -> list[dict[str, Any]]:
        """Get all currently active (not finished) traces."""
        return list(_active_traces.get(self.organisation_id, {}).values())
