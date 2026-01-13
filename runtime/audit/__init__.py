"""
Runtime Audit Module

Purpose: Telemetry and audit trail infrastructure with tenant isolation
Authority: Wave 3.1 - Runtime Telemetry & Audit Trail Hardening
"""

from runtime.audit.telemetry import (
    TelemetryCollector,
    TelemetrySpan,
    TelemetryMetric,
    TelemetryEvent,
    TelemetryLevel,
    SpanStatus,
    get_telemetry_collector,
    clear_telemetry
)

from runtime.audit.audit_trail import (
    RuntimeAuditTrail,
    AuditEntry,
    AuditSeverity,
    AuditCategory,
    get_runtime_audit_trail,
    clear_audit_trail
)

__all__ = [
    # Telemetry
    "TelemetryCollector",
    "TelemetrySpan",
    "TelemetryMetric",
    "TelemetryEvent",
    "TelemetryLevel",
    "SpanStatus",
    "get_telemetry_collector",
    "clear_telemetry",
    
    # Audit Trail
    "RuntimeAuditTrail",
    "AuditEntry",
    "AuditSeverity",
    "AuditCategory",
    "get_runtime_audit_trail",
    "clear_audit_trail",
]
