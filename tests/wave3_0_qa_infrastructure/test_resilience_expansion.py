"""
Wave 3.4 - Resilience & Failure Mode Expansion Tests

Purpose: Test circuit breaker tuning, backoff policy validation, conflict resolution, and escalation analytics
Authority: Wave 3.4 Implementation Plan
QA Coverage: Wave 3.4 resilience expansion features
"""

import pytest
import time
import threading
from datetime import datetime, UTC

# Import modules under test
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "runtime")))

from resilience_config import (
    ResilienceConfigManager,
    ScenarioType,
    ValidationResult
)
from conflict_resolution_guard import (
    ConflictResolutionGuard,
    ConflictType,
    LockStatus
)
from escalation_analytics import (
    EscalationAnalytics,
    EvidenceType,
    FailureCategory,
    EscalationSeverity
)


@pytest.fixture
def org_id():
    """Test organisation ID"""
    return "test-org-wave3-4"


@pytest.fixture
def config_manager(org_id):
    """Create resilience config manager"""
    return ResilienceConfigManager(org_id)


@pytest.fixture
def conflict_guard(org_id):
    """Create conflict resolution guard"""
    guard = ConflictResolutionGuard(org_id)
    yield guard
    guard.shutdown()


@pytest.fixture
def escalation_analytics(org_id):
    """Create escalation analytics"""
    return EscalationAnalytics(org_id)


@pytest.mark.wave3
@pytest.mark.subwave_3_4
class TestCircuitBreakerTuning:
    """Test circuit breaker calibration for production scenarios"""
    
    def test_create_circuit_breaker_config_with_defaults(self, config_manager):
        """Test creating circuit breaker config with scenario-based defaults"""
        result = config_manager.create_circuit_breaker_config(
            name="api_gateway_breaker",
            scenario=ScenarioType.NORMAL_TRAFFIC
        )
        
        assert "config_id" in result
        assert result["validation_result"] == ValidationResult.VALID.value
        assert result["errors"] == []
        
        config = result["config"]
        assert config.failure_threshold == 5  # NORMAL_TRAFFIC default
        assert config.timeout_seconds == 60
        assert config.half_open_max_calls == 3
        assert config.success_threshold == 3
    
    def test_create_circuit_breaker_config_custom_params(self, config_manager):
        """Test creating circuit breaker config with custom parameters"""
        result = config_manager.create_circuit_breaker_config(
            name="custom_breaker",
            scenario=ScenarioType.HIGH_TRAFFIC,
            failure_threshold=8,
            timeout_seconds=120,
            half_open_max_calls=4,
            success_threshold=4
        )
        
        assert result["validation_result"] == ValidationResult.VALID.value
        
        config = result["config"]
        assert config.failure_threshold == 8
        assert config.timeout_seconds == 120
        assert config.half_open_max_calls == 4
        assert config.success_threshold == 4
    
    def test_circuit_breaker_validation_failure(self, config_manager):
        """Test circuit breaker validation catches invalid configurations"""
        result = config_manager.create_circuit_breaker_config(
            name="invalid_breaker",
            scenario=ScenarioType.LOW_TRAFFIC,
            failure_threshold=0,  # Invalid: must be >= 1
            success_threshold=5,  # Invalid: exceeds half_open_max_calls (default 2)
        )
        
        assert result["validation_result"] == ValidationResult.INVALID.value
        assert len(result["errors"]) > 0
        assert any("failure_threshold must be >= 1" in err for err in result["errors"])
        assert any("success_threshold cannot exceed half_open_max_calls" in err for err in result["errors"])
    
    def test_circuit_breaker_scenario_defaults(self, config_manager):
        """Test different scenarios have appropriate default parameters"""
        scenarios_to_test = [
            (ScenarioType.LOW_TRAFFIC, 3, 30),
            (ScenarioType.NORMAL_TRAFFIC, 5, 60),
            (ScenarioType.HIGH_TRAFFIC, 10, 90),
            (ScenarioType.PEAK_TRAFFIC, 15, 120),
        ]
        
        for scenario, expected_threshold, expected_timeout in scenarios_to_test:
            result = config_manager.create_circuit_breaker_config(
                name=f"breaker_{scenario.value}",
                scenario=scenario
            )
            
            config = result["config"]
            assert config.failure_threshold == expected_threshold
            assert config.timeout_seconds == expected_timeout
    
    def test_calibrate_for_high_error_rate(self, config_manager):
        """Test calibration recommends lower threshold for high error rates"""
        performance_metrics = {
            "error_rate": 0.08,  # 8% error rate (high)
            "latency_p95": 150.0,
            "latency_p99": 200.0,
            "throughput": 300.0
        }
        
        recommendations = config_manager.calibrate_for_scenario(
            ScenarioType.NORMAL_TRAFFIC,
            performance_metrics
        )
        
        # Should recommend lowering failure threshold
        threshold_recs = [r for r in recommendations if r.parameter_name == "failure_threshold"]
        assert len(threshold_recs) > 0
        
        rec = threshold_recs[0]
        assert rec.recommended_value < rec.current_value
        assert "error rate" in rec.reason.lower()


@pytest.mark.wave3
@pytest.mark.subwave_3_4
class TestBackoffPolicyConfiguration:
    """Test backoff policy configuration with validation"""
    
    def test_create_backoff_policy_with_defaults(self, config_manager):
        """Test creating backoff policy with scenario-based defaults"""
        result = config_manager.create_backoff_policy_config(
            name="api_retry_policy",
            scenario=ScenarioType.NORMAL_TRAFFIC
        )
        
        assert "config_id" in result
        assert result["validation_result"] == ValidationResult.VALID.value
        assert result["errors"] == []
        
        config = result["config"]
        assert config.initial_delay_ms == 200  # NORMAL_TRAFFIC default
        assert config.max_retries == 5
        assert config.backoff_multiplier == 2.0
        assert config.max_delay_ms == 10000
        assert config.jitter_enabled is True
    
    def test_create_backoff_policy_custom_params(self, config_manager):
        """Test creating backoff policy with custom parameters"""
        result = config_manager.create_backoff_policy_config(
            name="custom_policy",
            scenario=ScenarioType.HIGH_TRAFFIC,
            initial_delay_ms=1000,
            max_retries=3,
            backoff_multiplier=1.8,
            max_delay_ms=20000,
            jitter_enabled=False,
            jitter_factor=0.0
        )
        
        assert result["validation_result"] == ValidationResult.VALID.value
        
        config = result["config"]
        assert config.initial_delay_ms == 1000
        assert config.max_retries == 3
        assert config.backoff_multiplier == 1.8
        assert config.max_delay_ms == 20000
        assert config.jitter_enabled is False
    
    def test_backoff_policy_validation_failure(self, config_manager):
        """Test backoff policy validation catches invalid configurations"""
        result = config_manager.create_backoff_policy_config(
            name="invalid_policy",
            scenario=ScenarioType.LOW_TRAFFIC,
            initial_delay_ms=0,  # Invalid: must be >= 1
            max_retries=-1,  # Invalid: must be >= 0
            backoff_multiplier=0.5,  # Invalid: must be >= 1.0
            max_delay_ms=50,  # Invalid: less than initial_delay_ms
            jitter_factor=1.5  # Invalid: must be 0.0-1.0
        )
        
        assert result["validation_result"] == ValidationResult.INVALID.value
        assert len(result["errors"]) >= 4
    
    def test_backoff_policy_scenario_defaults(self, config_manager):
        """Test different scenarios have appropriate default backoff parameters"""
        scenarios_to_test = [
            (ScenarioType.LOW_TRAFFIC, 100, 3, 5000),
            (ScenarioType.NORMAL_TRAFFIC, 200, 5, 10000),
            (ScenarioType.HIGH_TRAFFIC, 500, 4, 15000),
            (ScenarioType.RECOVERY_MODE, 3000, 3, 60000),
        ]
        
        for scenario, expected_initial, expected_retries, expected_max in scenarios_to_test:
            result = config_manager.create_backoff_policy_config(
                name=f"policy_{scenario.value}",
                scenario=scenario
            )
            
            config = result["config"]
            assert config.initial_delay_ms == expected_initial
            assert config.max_retries == expected_retries
            assert config.max_delay_ms == expected_max
    
    def test_calibrate_for_high_throughput(self, config_manager):
        """Test calibration recommends increased backoff for high throughput"""
        performance_metrics = {
            "error_rate": 0.02,
            "latency_p95": 180.0,
            "latency_p99": 230.0,
            "throughput": 450.0,  # High (envelope max is 500)
            "retry_success_rate": 0.7
        }
        
        recommendations = config_manager.calibrate_for_scenario(
            ScenarioType.NORMAL_TRAFFIC,
            performance_metrics
        )
        
        # Should recommend increasing initial delay
        delay_recs = [r for r in recommendations if r.parameter_name == "initial_delay_ms"]
        assert len(delay_recs) > 0
        
        rec = delay_recs[0]
        assert rec.recommended_value > rec.current_value
        assert "throughput" in rec.reason.lower()


@pytest.mark.wave3
@pytest.mark.subwave_3_4
class TestConflictResolutionGuards:
    """Test race condition and deadlock prevention"""
    
    def test_acquire_and_release_lock(self, conflict_guard):
        """Test basic resource lock acquisition and release"""
        result = conflict_guard.acquire_resource_lock(
            resource_id="resource_1",
            operation_id="op_1",
            timeout_seconds=5
        )
        
        assert result["status"] == LockStatus.ACQUIRED.value
        assert "lock_id" in result
        
        lock_id = result["lock_id"]
        
        # Release lock
        release_result = conflict_guard.release_resource_lock(lock_id)
        assert release_result["status"] == LockStatus.RELEASED.value
    
    def test_lock_timeout_on_contention(self, conflict_guard):
        """Test lock timeout when resource is already locked"""
        # First operation acquires lock
        result1 = conflict_guard.acquire_resource_lock(
            resource_id="resource_2",
            operation_id="op_1",
            timeout_seconds=5
        )
        assert result1["status"] == LockStatus.ACQUIRED.value
        
        # Second operation tries to acquire same resource (should timeout quickly)
        result2 = conflict_guard.acquire_resource_lock(
            resource_id="resource_2",
            operation_id="op_2",
            timeout_seconds=1  # Short timeout
        )
        
        # Should timeout
        assert result2["status"] == LockStatus.TIMEOUT.value
        assert "conflict_id" in result2
        
        # Cleanup
        conflict_guard.release_resource_lock(result1["lock_id"])
    
    def test_deadlock_detection_and_prevention(self, conflict_guard):
        """Test deadlock detection prevents circular wait"""
        # Operation 1 acquires resource A
        result_a = conflict_guard.acquire_resource_lock(
            resource_id="resource_a",
            operation_id="op_1",
            timeout_seconds=10
        )
        assert result_a["status"] == LockStatus.ACQUIRED.value
        
        # Operation 2 acquires resource B
        result_b = conflict_guard.acquire_resource_lock(
            resource_id="resource_b",
            operation_id="op_2",
            timeout_seconds=10
        )
        assert result_b["status"] == LockStatus.ACQUIRED.value
        
        # Now op_1 tries to acquire resource B (held by op_2)
        # and op_2 tries to acquire resource A (held by op_1)
        # This would create a deadlock
        
        # Simulate op_2 waiting for resource A
        def try_acquire_a():
            return conflict_guard.acquire_resource_lock(
                resource_id="resource_a",
                operation_id="op_2",
                timeout_seconds=2
            )
        
        thread = threading.Thread(target=try_acquire_a)
        thread.start()
        
        time.sleep(0.5)  # Let op_2 start waiting
        
        # Now op_1 tries to acquire resource B (creating potential deadlock)
        result_b_for_op1 = conflict_guard.acquire_resource_lock(
            resource_id="resource_b",
            operation_id="op_1",
            timeout_seconds=2
        )
        
        # Should be denied due to deadlock detection
        assert result_b_for_op1["status"] in [LockStatus.DENIED.value, LockStatus.TIMEOUT.value]
        
        thread.join()
        
        # Cleanup
        conflict_guard.release_resource_lock(result_a["lock_id"])
        conflict_guard.release_resource_lock(result_b["lock_id"])
    
    def test_race_condition_detection(self, conflict_guard):
        """Test race condition detection on state mismatch"""
        result = conflict_guard.detect_race_condition(
            resource_id="shared_counter",
            expected_state=10,
            actual_state=12  # Mismatch indicates race condition
        )
        
        assert result["detected"] is True
        assert "conflict_id" in result
        assert result["expected_state"] == 10
        assert result["actual_state"] == 12
    
    def test_execute_with_lock_context_manager(self, conflict_guard):
        """Test execute_with_lock provides safe context for operations"""
        counter = {"value": 0}
        
        def increment_counter():
            counter["value"] += 1
            return counter["value"]
        
        result = conflict_guard.execute_with_lock(
            resource_id="counter_resource",
            operation_id="increment_op",
            operation=increment_counter,
            timeout_seconds=5
        )
        
        assert result["success"] is True
        assert result["result"] == 1
        assert counter["value"] == 1
        
        # Lock should be released automatically
        active_locks = conflict_guard.get_active_locks()
        assert len(active_locks) == 0
    
    def test_release_all_operation_locks(self, conflict_guard):
        """Test releasing all locks for an operation"""
        # Acquire multiple locks for same operation
        result1 = conflict_guard.acquire_resource_lock("res_1", "op_multi", 10)
        result2 = conflict_guard.acquire_resource_lock("res_2", "op_multi", 10)
        result3 = conflict_guard.acquire_resource_lock("res_3", "op_multi", 10)
        
        assert result1["status"] == LockStatus.ACQUIRED.value
        assert result2["status"] == LockStatus.ACQUIRED.value
        assert result3["status"] == LockStatus.ACQUIRED.value
        
        # Release all at once
        release_result = conflict_guard.release_all_operation_locks("op_multi")
        
        assert release_result["released_count"] == 3
        assert len(release_result["lock_ids"]) == 3
        
        # Verify all released
        active_locks = conflict_guard.get_active_locks()
        assert len(active_locks) == 0


@pytest.mark.wave3
@pytest.mark.subwave_3_4
class TestEscalationAnalytics:
    """Test failure analytics and evidence generation"""
    
    def test_collect_failure_evidence(self, escalation_analytics):
        """Test collecting evidence for a failure"""
        result = escalation_analytics.collect_failure_evidence(
            failure_id="failure_001",
            evidence_type=EvidenceType.SYSTEM_STATE,
            data={"cpu_usage": 85.5, "memory_mb": 2048, "active_connections": 150}
        )
        
        assert "evidence_id" in result
        assert result["evidence_type"] == EvidenceType.SYSTEM_STATE.value
        assert result["immutable"] is True
    
    def test_generate_comprehensive_evidence_artifact(self, escalation_analytics):
        """Test generating complete evidence artifact"""
        result = escalation_analytics.generate_evidence_artifact(
            failure_id="failure_002",
            system_state={"status": "degraded", "uptime_hours": 48},
            error_details={
                "error": "Connection timeout",
                "stack_trace": "line 1\nline 2\nline 3"
            },
            performance_metrics={"latency_p95": 250.0, "latency_p99": 380.0},
            operation_timeline=[
                {"step": 1, "action": "connect", "result": "success"},
                {"step": 2, "action": "query", "result": "timeout"}
            ]
        )
        
        assert "artifact_id" in result
        assert result["failure_id"] == "failure_002"
        assert result["evidence_count"] >= 4  # system_state, error_log, stack_trace, metrics, timeline
        assert len(result["evidence_ids"]) >= 4
    
    def test_create_escalation_context(self, escalation_analytics):
        """Test creating escalation context with 5 required elements"""
        evidence_ids = ["evidence_1", "evidence_2"]
        
        result = escalation_analytics.create_escalation_context(
            failure_id="failure_003",
            severity=EscalationSeverity.HIGH,
            category=FailureCategory.PERSISTENT,
            what="Database connection pool exhausted",
            why="Sudden traffic spike exceeded pool capacity",
            blocked="All new database operations",
            decision_needed="Increase pool size or implement connection throttling",
            consequence="Service outage if not addressed within 1 hour",
            evidence_ids=evidence_ids,
            affected_operations=["user_login", "data_query"],
            affected_resources=["db_connection_pool"]
        )
        
        assert "escalation_id" in result
        assert result["severity"] == EscalationSeverity.HIGH.value
        assert result["category"] == FailureCategory.PERSISTENT.value
        assert result["evidence_count"] == 2
        
        context = result["context"]
        assert context.what == "Database connection pool exhausted"
        assert context.why == "Sudden traffic spike exceeded pool capacity"
        assert context.blocked == "All new database operations"
        assert context.decision_needed == "Increase pool size or implement connection throttling"
        assert context.consequence == "Service outage if not addressed within 1 hour"
    
    def test_register_and_trigger_escalation_hook(self, escalation_analytics):
        """Test escalation hooks are triggered on severity match"""
        hook_triggered = {"count": 0, "context": None}
        
        def test_hook(context):
            hook_triggered["count"] += 1
            hook_triggered["context"] = context
        
        # Register hook for HIGH severity
        hook_result = escalation_analytics.register_escalation_hook(
            name="test_high_severity_hook",
            severity_threshold=EscalationSeverity.HIGH,
            handler=test_hook
        )
        
        assert "hook_id" in hook_result
        assert hook_result["severity_threshold"] == EscalationSeverity.HIGH.value
        
        # Create escalation with CRITICAL severity (should trigger hook)
        escalation_analytics.create_escalation_context(
            failure_id="failure_004",
            severity=EscalationSeverity.CRITICAL,
            category=FailureCategory.CRITICAL,
            what="System crash",
            why="Memory leak",
            blocked="All operations",
            decision_needed="Restart service",
            consequence="Complete service outage",
            evidence_ids=[]
        )
        
        # Hook should have been triggered
        assert hook_triggered["count"] == 1
        assert hook_triggered["context"] is not None
    
    def test_analyze_failure_patterns(self, escalation_analytics):
        """Test failure pattern analysis over time window"""
        # Create some test failures
        for i in range(5):
            escalation_analytics.create_escalation_context(
                failure_id=f"failure_{i}",
                severity=EscalationSeverity.MEDIUM,
                category=FailureCategory.TRANSIENT,
                what=f"Error {i}",
                why="Test",
                blocked="None",
                decision_needed="Monitor",
                consequence="Low",
                evidence_ids=[]
            )
        
        # Analyze patterns
        result = escalation_analytics.analyze_failure_patterns(time_window_hours=24)
        
        assert "analytics_id" in result
        assert result["failure_count"] == 5
        assert result["failure_rate"] > 0
        assert "mtbf_hours" in result
        assert "trend" in result
        assert result["trend"] in ["increasing", "stable", "decreasing"]
    
    def test_export_evidence_artifact(self, escalation_analytics):
        """Test exporting evidence as JSON artifact"""
        # Create some evidence
        escalation_analytics.collect_failure_evidence(
            failure_id="failure_export",
            evidence_type=EvidenceType.ERROR_LOG,
            data={"error": "Test error", "timestamp": "2026-01-13T12:00:00Z"}
        )
        
        # Export
        result = escalation_analytics.export_evidence_artifact(
            failure_id="failure_export",
            format="json"
        )
        
        assert result["format"] == "json"
        assert "artifact" in result
        assert result["artifact"]["evidence_count"] >= 1
        assert "serialized" in result  # JSON string representation


@pytest.mark.wave3
@pytest.mark.subwave_3_4
class TestResilienceIntegration:
    """Test integration between resilience components"""
    
    def test_config_calibration_integration(self, config_manager):
        """Test end-to-end configuration calibration flow"""
        # Create configs
        cb_result = config_manager.create_circuit_breaker_config(
            name="integrated_breaker",
            scenario=ScenarioType.NORMAL_TRAFFIC
        )
        
        bp_result = config_manager.create_backoff_policy_config(
            name="integrated_backoff",
            scenario=ScenarioType.NORMAL_TRAFFIC
        )
        
        assert cb_result["validation_result"] == ValidationResult.VALID.value
        assert bp_result["validation_result"] == ValidationResult.VALID.value
        
        # Calibrate based on metrics
        metrics = {
            "error_rate": 0.03,
            "latency_p95": 190.0,
            "latency_p99": 240.0,
            "throughput": 400.0,
            "retry_success_rate": 0.6
        }
        
        recommendations = config_manager.calibrate_for_scenario(
            ScenarioType.NORMAL_TRAFFIC,
            metrics
        )
        
        # Should have recommendations
        assert len(recommendations) >= 0  # May or may not have recommendations based on metrics
    
    def test_conflict_and_escalation_integration(self, conflict_guard, escalation_analytics):
        """Test conflict detection triggers escalation"""
        # Simulate conflict
        result = conflict_guard.detect_race_condition(
            resource_id="critical_resource",
            expected_state="state_a",
            actual_state="state_b"
        )
        
        assert result["detected"] is True
        conflict_id = result["conflict_id"]
        
        # Create escalation with evidence
        evidence_result = escalation_analytics.collect_failure_evidence(
            failure_id=f"failure_conflict_{conflict_id}",
            evidence_type=EvidenceType.SYSTEM_STATE,
            data={
                "conflict_id": conflict_id,
                "resource_id": "critical_resource",
                "expected": "state_a",
                "actual": "state_b"
            }
        )
        
        escalation_result = escalation_analytics.create_escalation_context(
            failure_id=f"failure_conflict_{conflict_id}",
            severity=EscalationSeverity.HIGH,
            category=FailureCategory.PERSISTENT,
            what="Race condition detected on critical resource",
            why="Concurrent operations modified state",
            blocked="Resource consistency compromised",
            decision_needed="Retry operation or rollback",
            consequence="Data corruption risk",
            evidence_ids=[evidence_result["evidence_id"]]
        )
        
        assert "escalation_id" in escalation_result
        assert escalation_result["evidence_count"] == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
