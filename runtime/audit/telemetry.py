"""
Runtime Telemetry Infrastructure

Purpose: End-to-end trace capture, metrics collection, and telemetry with tenant isolation
Authority: Wave 3.1 - Runtime Telemetry & Audit Trail Hardening
Tenant Isolation: All operations scoped by organisation_id
QA Coverage: Supports QA-171 to QA-176 (Audit Logger requirements)
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC
from enum import Enum
from typing import Any, Optional
from collections import deque
import threading
import uuid


class TelemetryLevel(Enum):
    """Telemetry event levels"""
    TRACE = "trace"
    METRIC = "metric"
    AUDIT = "audit"
    ALERT = "alert"


class SpanStatus(Enum):
    """Span completion status"""
    SUCCESS = "success"
    FAILURE = "failure"
    TIMEOUT = "timeout"
    CANCELLED = "cancelled"


@dataclass
class TelemetrySpan:
    """Represents a traced operation span"""
    span_id: str
    trace_id: str
    parent_span_id: str | None
    operation: str
    organisation_id: str
    start_time: datetime
    end_time: datetime | None = None
    status: SpanStatus | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    errors: list[dict[str, Any]] = field(default_factory=list)
    
    def complete(self, status: SpanStatus, metadata: dict[str, Any] = None) -> None:
        """Complete the span with status and optional metadata"""
        self.end_time = datetime.now(UTC)
        self.status = status
        if metadata:
            self.metadata.update(metadata)
    
    def add_error(self, error_type: str, error_message: str, details: dict[str, Any] = None) -> None:
        """Add an error to the span"""
        self.errors.append({
            "type": error_type,
            "message": error_message,
            "timestamp": datetime.now(UTC),
            "details": details or {}
        })
    
    def duration_ms(self) -> float | None:
        """Calculate span duration in milliseconds"""
        if self.end_time:
            delta = self.end_time - self.start_time
            return delta.total_seconds() * 1000
        return None


@dataclass
class TelemetryMetric:
    """Represents a collected metric"""
    metric_id: str
    metric_name: str
    metric_value: float
    metric_unit: str
    organisation_id: str
    timestamp: datetime
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class TelemetryEvent:
    """Represents a telemetry event"""
    event_id: str
    event_type: str
    level: TelemetryLevel
    organisation_id: str
    timestamp: datetime
    data: dict[str, Any] = field(default_factory=dict)
    correlation_id: str | None = None


class TelemetryCollector:
    """
    Centralized telemetry collection with tenant isolation
    
    Responsibilities:
    - Collect traces, metrics, and events
    - Enforce tenant isolation via organisation_id
    - Maintain in-memory buffer for recent telemetry
    - Support querying and analysis
    """
    
    def __init__(self, max_buffer_size: int = 10000):
        self.max_buffer_size = max_buffer_size
        
        # Separate buffers per organisation
        self._spans: dict[str, deque] = {}
        self._metrics: dict[str, deque] = {}
        self._events: dict[str, deque] = {}
        
        # Active spans (for completing spans later)
        self._active_spans: dict[str, TelemetrySpan] = {}
        
        self._lock = threading.RLock()
    
    def start_span(
        self,
        operation: str,
        organisation_id: str,
        parent_span_id: str | None = None,
        trace_id: str | None = None,
        metadata: dict[str, Any] = None
    ) -> TelemetrySpan:
        """Start a new telemetry span"""
        span_id = str(uuid.uuid4())
        trace_id = trace_id or str(uuid.uuid4())
        
        span = TelemetrySpan(
            span_id=span_id,
            trace_id=trace_id,
            parent_span_id=parent_span_id,
            operation=operation,
            organisation_id=organisation_id,
            start_time=datetime.now(UTC),
            metadata=metadata or {}
        )
        
        with self._lock:
            self._active_spans[span_id] = span
        
        return span
    
    def complete_span(
        self,
        span_id: str,
        status: SpanStatus,
        metadata: dict[str, Any] = None
    ) -> TelemetrySpan | None:
        """Complete an active span"""
        with self._lock:
            span = self._active_spans.pop(span_id, None)
            if not span:
                return None
            
            span.complete(status, metadata)
            
            # Add to organisation buffer
            if span.organisation_id not in self._spans:
                self._spans[span.organisation_id] = deque(maxlen=self.max_buffer_size)
            
            self._spans[span.organisation_id].append(span)
            
            return span
    
    def record_metric(
        self,
        metric_name: str,
        metric_value: float,
        metric_unit: str,
        organisation_id: str,
        tags: dict[str, str] = None,
        metadata: dict[str, Any] = None
    ) -> TelemetryMetric:
        """Record a metric"""
        metric = TelemetryMetric(
            metric_id=str(uuid.uuid4()),
            metric_name=metric_name,
            metric_value=metric_value,
            metric_unit=metric_unit,
            organisation_id=organisation_id,
            timestamp=datetime.now(UTC),
            tags=tags or {},
            metadata=metadata or {}
        )
        
        with self._lock:
            if organisation_id not in self._metrics:
                self._metrics[organisation_id] = deque(maxlen=self.max_buffer_size)
            
            self._metrics[organisation_id].append(metric)
        
        return metric
    
    def log_event(
        self,
        event_type: str,
        level: TelemetryLevel,
        organisation_id: str,
        data: dict[str, Any] = None,
        correlation_id: str | None = None
    ) -> TelemetryEvent:
        """Log a telemetry event"""
        event = TelemetryEvent(
            event_id=str(uuid.uuid4()),
            event_type=event_type,
            level=level,
            organisation_id=organisation_id,
            timestamp=datetime.now(UTC),
            data=data or {},
            correlation_id=correlation_id
        )
        
        with self._lock:
            if organisation_id not in self._events:
                self._events[organisation_id] = deque(maxlen=self.max_buffer_size)
            
            self._events[organisation_id].append(event)
        
        return event
    
    def get_spans(
        self,
        organisation_id: str,
        trace_id: str | None = None,
        operation: str | None = None,
        limit: int = 100
    ) -> list[TelemetrySpan]:
        """Query spans for an organisation"""
        with self._lock:
            spans = list(self._spans.get(organisation_id, []))
        
        # Apply filters
        if trace_id:
            spans = [s for s in spans if s.trace_id == trace_id]
        if operation:
            spans = [s for s in spans if s.operation == operation]
        
        # Return most recent first
        return list(reversed(spans))[:limit]
    
    def get_metrics(
        self,
        organisation_id: str,
        metric_name: str | None = None,
        limit: int = 100
    ) -> list[TelemetryMetric]:
        """Query metrics for an organisation"""
        with self._lock:
            metrics = list(self._metrics.get(organisation_id, []))
        
        if metric_name:
            metrics = [m for m in metrics if m.metric_name == metric_name]
        
        return list(reversed(metrics))[:limit]
    
    def get_events(
        self,
        organisation_id: str,
        event_type: str | None = None,
        level: TelemetryLevel | None = None,
        limit: int = 100
    ) -> list[TelemetryEvent]:
        """Query events for an organisation"""
        with self._lock:
            events = list(self._events.get(organisation_id, []))
        
        if event_type:
            events = [e for e in events if e.event_type == event_type]
        if level:
            events = [e for e in events if e.level == level]
        
        return list(reversed(events))[:limit]
    
    def get_trace_summary(self, organisation_id: str, trace_id: str) -> dict[str, Any]:
        """Get a summary of all spans in a trace"""
        spans = self.get_spans(organisation_id, trace_id=trace_id, limit=1000)
        
        if not spans:
            return {"trace_id": trace_id, "found": False}
        
        # Calculate trace statistics
        total_duration = 0
        span_count = len(spans)
        error_count = sum(1 for s in spans if s.status == SpanStatus.FAILURE)
        
        for span in spans:
            if span.duration_ms():
                total_duration += span.duration_ms()
        
        return {
            "trace_id": trace_id,
            "organisation_id": organisation_id,
            "found": True,
            "span_count": span_count,
            "error_count": error_count,
            "total_duration_ms": total_duration,
            "operations": list(set(s.operation for s in spans)),
            "start_time": min(s.start_time for s in spans),
            "end_time": max(s.end_time for s in spans if s.end_time)
        }
    
    def clear_organisation_data(self, organisation_id: str) -> None:
        """Clear all telemetry data for an organisation (for testing)"""
        with self._lock:
            self._spans.pop(organisation_id, None)
            self._metrics.pop(organisation_id, None)
            self._events.pop(organisation_id, None)
            
            # Remove active spans for this organisation
            to_remove = [
                span_id for span_id, span in self._active_spans.items()
                if span.organisation_id == organisation_id
            ]
            for span_id in to_remove:
                self._active_spans.pop(span_id, None)


# Global telemetry collector instance
_telemetry_collector: TelemetryCollector | None = None


def get_telemetry_collector() -> TelemetryCollector:
    """Get or create the global telemetry collector"""
    global _telemetry_collector
    if _telemetry_collector is None:
        _telemetry_collector = TelemetryCollector()
    return _telemetry_collector


def clear_telemetry() -> None:
    """Clear global telemetry collector (for testing)"""
    global _telemetry_collector
    _telemetry_collector = None
