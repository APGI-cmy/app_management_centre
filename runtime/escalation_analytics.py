"""
Escalation Analytics Module

Purpose: Failure analytics with evidence generation and escalation hooks
Authority: Wave 3.4 - Resilience & Failure Mode Expansion
Tenant Isolation: All operations scoped by organisation_id

Capabilities:
- Failure evidence collection and generation
- Escalation hooks for failure scenarios
- Failure analytics and pattern analysis
- Evidence artifact creation
- Escalation context building
"""

from typing import Any
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, timedelta, UTC
from enum import Enum
import threading
import uuid
import json


class EscalationSeverity(Enum):
    """Escalation severity levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class EvidenceType(Enum):
    """Types of failure evidence"""
    SYSTEM_STATE = "system_state"
    ERROR_LOG = "error_log"
    STACK_TRACE = "stack_trace"
    PERFORMANCE_METRICS = "performance_metrics"
    CONFIGURATION_SNAPSHOT = "configuration_snapshot"
    OPERATION_TIMELINE = "operation_timeline"
    RESOURCE_UTILIZATION = "resource_utilization"


class FailureCategory(Enum):
    """Failure categorization"""
    TRANSIENT = "transient"  # Temporary, likely to recover
    PERSISTENT = "persistent"  # Ongoing, needs intervention
    CASCADING = "cascading"  # Spreading to other components
    CRITICAL = "critical"  # System-wide impact


@dataclass
class FailureEvidence:
    """Evidence artifact for failure"""
    evidence_id: str
    evidence_type: EvidenceType
    failure_id: str
    collected_at: datetime
    data: dict[str, Any]
    organisation_id: str
    immutable: bool = True  # Evidence must be immutable


@dataclass
class EscalationContext:
    """Context for failure escalation"""
    escalation_id: str
    failure_id: str
    severity: EscalationSeverity
    category: FailureCategory
    what: str  # What failed
    why: str  # Why it failed
    blocked: str  # What is blocked
    decision_needed: str  # What decision is required
    consequence: str  # Consequence of inaction
    evidence_ids: list[str]
    affected_operations: list[str]
    affected_resources: list[str]
    timestamp: datetime
    organisation_id: str
    escalated: bool = False
    escalation_handler: str | None = None


@dataclass
class FailureAnalytics:
    """Analytics for failure patterns"""
    analytics_id: str
    time_window_hours: int
    failure_count: int
    failure_rate: float  # Failures per hour
    mtbf: float  # Mean time between failures (hours)
    mttr: float  # Mean time to recovery (minutes)
    most_common_category: FailureCategory
    trend: str  # increasing, stable, decreasing
    organisation_id: str


@dataclass
class EscalationHook:
    """Hook for failure escalation"""
    hook_id: str
    name: str
    severity_threshold: EscalationSeverity
    handler: Callable[[EscalationContext], Any]
    active: bool = True


class EscalationAnalytics:
    """
    Manages failure analytics and escalation with evidence
    
    Provides:
    - Failure evidence collection
    - Evidence artifact generation
    - Escalation context building
    - Escalation hooks for automated response
    - Failure pattern analytics
    """
    
    def __init__(self, organisation_id: str):
        """
        Initialize escalation analytics
        
        Args:
            organisation_id: Organisation ID for tenant isolation
        """
        self.organisation_id = organisation_id
        self._evidence_store: dict[str, FailureEvidence] = {}
        self._escalations: dict[str, EscalationContext] = {}
        self._hooks: dict[str, EscalationHook] = {}
        self._failure_history: list[dict[str, Any]] = []
        self._lock = threading.Lock()
    
    def collect_failure_evidence(
        self,
        failure_id: str,
        evidence_type: EvidenceType,
        data: dict[str, Any]
    ) -> dict[str, Any]:
        """
        Collect and store failure evidence
        
        Args:
            failure_id: ID of failure
            evidence_type: Type of evidence
            data: Evidence data
        
        Returns:
            dict with evidence_id and confirmation
        """
        evidence_id = str(uuid.uuid4())
        
        evidence = FailureEvidence(
            evidence_id=evidence_id,
            evidence_type=evidence_type,
            failure_id=failure_id,
            collected_at=datetime.now(UTC),
            data=data,
            organisation_id=self.organisation_id
        )
        
        with self._lock:
            self._evidence_store[evidence_id] = evidence
        
        return {
            "evidence_id": evidence_id,
            "evidence_type": evidence_type.value,
            "collected_at": evidence.collected_at.isoformat(),
            "immutable": evidence.immutable
        }
    
    def generate_evidence_artifact(
        self,
        failure_id: str,
        system_state: dict[str, Any],
        error_details: dict[str, Any],
        performance_metrics: dict[str, float] | None = None,
        operation_timeline: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """
        Generate comprehensive evidence artifact for failure
        
        Args:
            failure_id: ID of failure
            system_state: Current system state snapshot
            error_details: Error information (message, stack trace, etc.)
            performance_metrics: Performance data at time of failure
            operation_timeline: Timeline of operations leading to failure
        
        Returns:
            dict with artifact_id and evidence_ids
        """
        artifact_id = str(uuid.uuid4())
        evidence_ids = []
        
        # Collect system state evidence
        if system_state:
            result = self.collect_failure_evidence(
                failure_id,
                EvidenceType.SYSTEM_STATE,
                system_state
            )
            evidence_ids.append(result["evidence_id"])
        
        # Collect error log evidence
        if error_details:
            result = self.collect_failure_evidence(
                failure_id,
                EvidenceType.ERROR_LOG,
                error_details
            )
            evidence_ids.append(result["evidence_id"])
        
        # Collect stack trace if present
        if error_details.get("stack_trace"):
            result = self.collect_failure_evidence(
                failure_id,
                EvidenceType.STACK_TRACE,
                {"stack_trace": error_details["stack_trace"]}
            )
            evidence_ids.append(result["evidence_id"])
        
        # Collect performance metrics
        if performance_metrics:
            result = self.collect_failure_evidence(
                failure_id,
                EvidenceType.PERFORMANCE_METRICS,
                performance_metrics
            )
            evidence_ids.append(result["evidence_id"])
        
        # Collect operation timeline
        if operation_timeline:
            result = self.collect_failure_evidence(
                failure_id,
                EvidenceType.OPERATION_TIMELINE,
                {"timeline": operation_timeline}
            )
            evidence_ids.append(result["evidence_id"])
        
        return {
            "artifact_id": artifact_id,
            "failure_id": failure_id,
            "evidence_count": len(evidence_ids),
            "evidence_ids": evidence_ids,
            "generated_at": datetime.now(UTC).isoformat()
        }
    
    def create_escalation_context(
        self,
        failure_id: str,
        severity: EscalationSeverity,
        category: FailureCategory,
        what: str,
        why: str,
        blocked: str,
        decision_needed: str,
        consequence: str,
        evidence_ids: list[str],
        affected_operations: list[str] | None = None,
        affected_resources: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Create escalation context for failure
        
        Args:
            failure_id: ID of failure
            severity: Escalation severity
            category: Failure category
            what: What failed
            why: Why it failed
            blocked: What is blocked
            decision_needed: What decision is required
            consequence: Consequence of inaction
            evidence_ids: List of evidence IDs
            affected_operations: Operations affected
            affected_resources: Resources affected
        
        Returns:
            dict with escalation_id and context
        """
        escalation_id = str(uuid.uuid4())
        
        context = EscalationContext(
            escalation_id=escalation_id,
            failure_id=failure_id,
            severity=severity,
            category=category,
            what=what,
            why=why,
            blocked=blocked,
            decision_needed=decision_needed,
            consequence=consequence,
            evidence_ids=evidence_ids,
            affected_operations=affected_operations or [],
            affected_resources=affected_resources or [],
            timestamp=datetime.now(UTC),
            organisation_id=self.organisation_id
        )
        
        with self._lock:
            self._escalations[escalation_id] = context
            
            # Record in failure history
            self._failure_history.append({
                "failure_id": failure_id,
                "escalation_id": escalation_id,
                "severity": severity.value,
                "category": category.value,
                "timestamp": context.timestamp,
                "evidence_count": len(evidence_ids)
            })
        
        # Trigger escalation hooks
        self._trigger_escalation_hooks(context)
        
        return {
            "escalation_id": escalation_id,
            "severity": severity.value,
            "category": category.value,
            "evidence_count": len(evidence_ids),
            "context": context
        }
    
    def _trigger_escalation_hooks(
        self,
        context: EscalationContext
    ) -> None:
        """Trigger escalation hooks that match severity"""
        with self._lock:
            # Get severity ordering
            severity_order = {
                EscalationSeverity.LOW: 1,
                EscalationSeverity.MEDIUM: 2,
                EscalationSeverity.HIGH: 3,
                EscalationSeverity.CRITICAL: 4
            }
            
            context_severity_level = severity_order[context.severity]
            
            # Trigger matching hooks
            for hook in self._hooks.values():
                if not hook.active:
                    continue
                
                hook_severity_level = severity_order[hook.severity_threshold]
                
                # Trigger if escalation severity >= hook threshold
                if context_severity_level >= hook_severity_level:
                    try:
                        hook.handler(context)
                        context.escalated = True
                        context.escalation_handler = hook.name
                    except Exception as e:
                        # Log hook failure but continue
                        pass
    
    def register_escalation_hook(
        self,
        name: str,
        severity_threshold: EscalationSeverity,
        handler: Callable[[EscalationContext], Any]
    ) -> dict[str, Any]:
        """
        Register hook for escalation
        
        Args:
            name: Hook name
            severity_threshold: Minimum severity to trigger
            handler: Callable to execute on escalation
        
        Returns:
            dict with hook_id
        """
        hook_id = str(uuid.uuid4())
        
        hook = EscalationHook(
            hook_id=hook_id,
            name=name,
            severity_threshold=severity_threshold,
            handler=handler
        )
        
        with self._lock:
            self._hooks[hook_id] = hook
        
        return {
            "hook_id": hook_id,
            "name": name,
            "severity_threshold": severity_threshold.value,
            "active": hook.active
        }
    
    def deactivate_hook(self, hook_id: str) -> dict[str, Any]:
        """Deactivate escalation hook"""
        with self._lock:
            hook = self._hooks.get(hook_id)
            if hook:
                hook.active = False
                return {
                    "hook_id": hook_id,
                    "active": False
                }
        
        return {
            "hook_id": hook_id,
            "error": "hook_not_found"
        }
    
    def analyze_failure_patterns(
        self,
        time_window_hours: int = 24
    ) -> dict[str, Any]:
        """
        Analyze failure patterns over time window
        
        Args:
            time_window_hours: Hours to analyze
        
        Returns:
            dict with analytics
        """
        analytics_id = str(uuid.uuid4())
        cutoff_time = datetime.now(UTC) - timedelta(hours=time_window_hours)
        
        with self._lock:
            # Filter failures in window
            recent_failures = [
                f for f in self._failure_history
                if f["timestamp"] >= cutoff_time
            ]
            
            if not recent_failures:
                return {
                    "analytics_id": analytics_id,
                    "time_window_hours": time_window_hours,
                    "failure_count": 0,
                    "message": "no_failures_in_window"
                }
            
            # Calculate metrics
            failure_count = len(recent_failures)
            failure_rate = failure_count / time_window_hours
            
            # Category distribution
            category_counts: dict[str, int] = {}
            for f in recent_failures:
                cat = f["category"]
                category_counts[cat] = category_counts.get(cat, 0) + 1
            
            most_common_category = FailureCategory(
                max(category_counts.items(), key=lambda x: x[1])[0]
            )
            
            # Calculate MTBF (Mean Time Between Failures)
            if failure_count > 1:
                time_range = (
                    recent_failures[-1]["timestamp"] - recent_failures[0]["timestamp"]
                ).total_seconds() / 3600  # Convert to hours
                mtbf = time_range / (failure_count - 1)
            else:
                mtbf = 0.0
            
            # Estimate MTTR (simplified - would need recovery timestamps in real impl)
            mttr = 15.0  # Placeholder: 15 minutes average
            
            # Detect trend (comparing first half vs second half)
            mid_point = len(recent_failures) // 2
            first_half_count = mid_point
            second_half_count = len(recent_failures) - mid_point
            
            if second_half_count > first_half_count * 1.2:
                trend = "increasing"
            elif second_half_count < first_half_count * 0.8:
                trend = "decreasing"
            else:
                trend = "stable"
            
            analytics = FailureAnalytics(
                analytics_id=analytics_id,
                time_window_hours=time_window_hours,
                failure_count=failure_count,
                failure_rate=failure_rate,
                mtbf=mtbf,
                mttr=mttr,
                most_common_category=most_common_category,
                trend=trend,
                organisation_id=self.organisation_id
            )
            
            return {
                "analytics_id": analytics_id,
                "time_window_hours": time_window_hours,
                "failure_count": failure_count,
                "failure_rate": round(failure_rate, 2),
                "mtbf_hours": round(mtbf, 2),
                "mttr_minutes": round(mttr, 2),
                "most_common_category": most_common_category.value,
                "trend": trend,
                "category_distribution": category_counts,
                "analytics": analytics
            }
    
    def get_evidence(self, evidence_id: str) -> FailureEvidence | None:
        """Retrieve evidence by ID"""
        with self._lock:
            return self._evidence_store.get(evidence_id)
    
    def get_escalation(self, escalation_id: str) -> EscalationContext | None:
        """Retrieve escalation context by ID"""
        with self._lock:
            return self._escalations.get(escalation_id)
    
    def get_failure_evidence(self, failure_id: str) -> list[FailureEvidence]:
        """Get all evidence for a failure"""
        with self._lock:
            return [
                evidence for evidence in self._evidence_store.values()
                if evidence.failure_id == failure_id
            ]
    
    def export_evidence_artifact(
        self,
        failure_id: str,
        format: str = "json"
    ) -> dict[str, Any]:
        """
        Export evidence artifact for failure
        
        Args:
            failure_id: Failure ID
            format: Export format (json, xml, etc.)
        
        Returns:
            dict with exported data
        """
        evidence_list = self.get_failure_evidence(failure_id)
        
        if not evidence_list:
            return {
                "failure_id": failure_id,
                "evidence_count": 0,
                "error": "no_evidence_found"
            }
        
        # Build artifact
        artifact = {
            "failure_id": failure_id,
            "organisation_id": self.organisation_id,
            "evidence_count": len(evidence_list),
            "exported_at": datetime.now(UTC).isoformat(),
            "evidence": []
        }
        
        for evidence in evidence_list:
            artifact["evidence"].append({
                "evidence_id": evidence.evidence_id,
                "evidence_type": evidence.evidence_type.value,
                "collected_at": evidence.collected_at.isoformat(),
                "data": evidence.data,
                "immutable": evidence.immutable
            })
        
        if format == "json":
            return {
                "format": "json",
                "artifact": artifact,
                "serialized": json.dumps(artifact, indent=2)
            }
        
        return {
            "format": format,
            "error": "unsupported_format"
        }
    
    def get_failure_history(
        self,
        hours: int = 24
    ) -> list[dict[str, Any]]:
        """Get failure history for time window"""
        cutoff = datetime.now(UTC) - timedelta(hours=hours)
        
        with self._lock:
            return [
                f for f in self._failure_history
                if f["timestamp"] >= cutoff
            ]
    
    def clear_old_evidence(
        self,
        retention_days: int = 30
    ) -> dict[str, Any]:
        """
        Clear evidence older than retention period
        
        Args:
            retention_days: Days to retain evidence
        
        Returns:
            dict with cleared count
        """
        cutoff = datetime.now(UTC) - timedelta(days=retention_days)
        cleared = 0
        
        with self._lock:
            for evidence_id in list(self._evidence_store.keys()):
                evidence = self._evidence_store[evidence_id]
                if evidence.collected_at < cutoff:
                    del self._evidence_store[evidence_id]
                    cleared += 1
        
        return {
            "retention_days": retention_days,
            "cleared_count": cleared,
            "remaining_count": len(self._evidence_store)
        }
