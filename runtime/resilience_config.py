"""
Resilience Configuration Module

Purpose: Circuit breaker and backoff policy tuning for production scenarios
Authority: Wave 3.4 - Resilience & Failure Mode Expansion
Tenant Isolation: All operations scoped by organisation_id

Capabilities:
- Circuit breaker parameter calibration
- Backoff policy configuration with validation
- Production scenario tuning
- Performance envelope management
"""

from typing import Any
from dataclasses import dataclass, field
from datetime import datetime, UTC
from enum import Enum
import threading
import uuid


class ScenarioType(Enum):
    """Production scenario types for tuning"""
    LOW_TRAFFIC = "low_traffic"
    NORMAL_TRAFFIC = "normal_traffic"
    HIGH_TRAFFIC = "high_traffic"
    PEAK_TRAFFIC = "peak_traffic"
    DEGRADED_PERFORMANCE = "degraded_performance"
    RECOVERY_MODE = "recovery_mode"


class ValidationResult(Enum):
    """Configuration validation outcomes"""
    VALID = "valid"
    INVALID = "invalid"
    WARNING = "warning"


@dataclass
class CircuitBreakerConfig:
    """Circuit breaker configuration parameters"""
    config_id: str
    name: str
    failure_threshold: int  # Number of failures before opening
    timeout_seconds: int  # Time before attempting half-open
    half_open_max_calls: int  # Max calls to test in half-open
    success_threshold: int  # Successes needed to close from half-open
    scenario: ScenarioType
    organisation_id: str
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    validated: bool = False
    validation_errors: list[str] = field(default_factory=list)


@dataclass
class BackoffPolicyConfig:
    """Backoff policy configuration parameters"""
    config_id: str
    name: str
    initial_delay_ms: int  # Starting delay
    max_retries: int  # Maximum retry attempts
    backoff_multiplier: float  # Exponential growth factor
    max_delay_ms: int  # Cap on delay
    jitter_enabled: bool  # Add randomization
    jitter_factor: float  # Jitter magnitude (0.0 to 1.0)
    scenario: ScenarioType
    organisation_id: str
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    validated: bool = False
    validation_errors: list[str] = field(default_factory=list)


@dataclass
class PerformanceEnvelope:
    """Performance envelope constraints"""
    envelope_id: str
    scenario: ScenarioType
    max_latency_p95_ms: int  # 95th percentile latency target
    max_latency_p99_ms: int  # 99th percentile latency target
    max_throughput_rps: int  # Requests per second
    max_concurrent_operations: int  # Concurrency limit
    max_memory_mb: int  # Memory constraint
    organisation_id: str


@dataclass
class TuningRecommendation:
    """Tuning recommendation from calibration"""
    recommendation_id: str
    parameter_name: str
    current_value: Any
    recommended_value: Any
    reason: str
    confidence: float  # 0.0 to 1.0
    impact_estimate: str  # low, medium, high


class ResilienceConfigManager:
    """
    Manages resilience configuration tuning and calibration
    
    Provides:
    - Circuit breaker parameter calibration for production
    - Backoff policy configuration with validation
    - Scenario-specific tuning profiles
    - Performance envelope management
    """
    
    def __init__(self, organisation_id: str):
        """
        Initialize configuration manager
        
        Args:
            organisation_id: Organisation ID for tenant isolation
        """
        self.organisation_id = organisation_id
        self._circuit_breaker_configs: dict[str, CircuitBreakerConfig] = {}
        self._backoff_configs: dict[str, BackoffPolicyConfig] = {}
        self._performance_envelopes: dict[ScenarioType, PerformanceEnvelope] = {}
        self._tuning_history: dict[str, list[dict[str, Any]]] = {}
        self._lock = threading.Lock()
        
        # Initialize default production scenarios
        self._init_default_scenarios()
    
    def _init_default_scenarios(self) -> None:
        """Initialize default performance envelopes for scenarios"""
        defaults = {
            ScenarioType.LOW_TRAFFIC: PerformanceEnvelope(
                envelope_id=str(uuid.uuid4()),
                scenario=ScenarioType.LOW_TRAFFIC,
                max_latency_p95_ms=100,
                max_latency_p99_ms=150,
                max_throughput_rps=100,
                max_concurrent_operations=50,
                max_memory_mb=512,
                organisation_id=self.organisation_id
            ),
            ScenarioType.NORMAL_TRAFFIC: PerformanceEnvelope(
                envelope_id=str(uuid.uuid4()),
                scenario=ScenarioType.NORMAL_TRAFFIC,
                max_latency_p95_ms=180,
                max_latency_p99_ms=230,
                max_throughput_rps=500,
                max_concurrent_operations=200,
                max_memory_mb=1024,
                organisation_id=self.organisation_id
            ),
            ScenarioType.HIGH_TRAFFIC: PerformanceEnvelope(
                envelope_id=str(uuid.uuid4()),
                scenario=ScenarioType.HIGH_TRAFFIC,
                max_latency_p95_ms=250,
                max_latency_p99_ms=350,
                max_throughput_rps=1000,
                max_concurrent_operations=500,
                max_memory_mb=2048,
                organisation_id=self.organisation_id
            ),
            ScenarioType.PEAK_TRAFFIC: PerformanceEnvelope(
                envelope_id=str(uuid.uuid4()),
                scenario=ScenarioType.PEAK_TRAFFIC,
                max_latency_p95_ms=400,
                max_latency_p99_ms=600,
                max_throughput_rps=2000,
                max_concurrent_operations=1000,
                max_memory_mb=4096,
                organisation_id=self.organisation_id
            ),
            ScenarioType.DEGRADED_PERFORMANCE: PerformanceEnvelope(
                envelope_id=str(uuid.uuid4()),
                scenario=ScenarioType.DEGRADED_PERFORMANCE,
                max_latency_p95_ms=500,
                max_latency_p99_ms=800,
                max_throughput_rps=200,
                max_concurrent_operations=100,
                max_memory_mb=1024,
                organisation_id=self.organisation_id
            ),
            ScenarioType.RECOVERY_MODE: PerformanceEnvelope(
                envelope_id=str(uuid.uuid4()),
                scenario=ScenarioType.RECOVERY_MODE,
                max_latency_p95_ms=300,
                max_latency_p99_ms=450,
                max_throughput_rps=300,
                max_concurrent_operations=150,
                max_memory_mb=1024,
                organisation_id=self.organisation_id
            ),
        }
        
        with self._lock:
            self._performance_envelopes.update(defaults)
    
    def create_circuit_breaker_config(
        self,
        name: str,
        scenario: ScenarioType,
        failure_threshold: int | None = None,
        timeout_seconds: int | None = None,
        half_open_max_calls: int | None = None,
        success_threshold: int | None = None
    ) -> dict[str, Any]:
        """
        Create circuit breaker configuration for scenario
        
        Args:
            name: Configuration name
            scenario: Production scenario type
            failure_threshold: Failures before opening (default: scenario-based)
            timeout_seconds: Timeout before half-open (default: scenario-based)
            half_open_max_calls: Calls in half-open state (default: scenario-based)
            success_threshold: Successes to close (default: scenario-based)
        
        Returns:
            dict with config_id and validation_result
        """
        config_id = str(uuid.uuid4())
        
        # Apply scenario-based defaults if not specified
        defaults = self._get_circuit_breaker_defaults(scenario)
        
        config = CircuitBreakerConfig(
            config_id=config_id,
            name=name,
            failure_threshold=failure_threshold if failure_threshold is not None else defaults["failure_threshold"],
            timeout_seconds=timeout_seconds if timeout_seconds is not None else defaults["timeout_seconds"],
            half_open_max_calls=half_open_max_calls if half_open_max_calls is not None else defaults["half_open_max_calls"],
            success_threshold=success_threshold if success_threshold is not None else defaults["success_threshold"],
            scenario=scenario,
            organisation_id=self.organisation_id
        )
        
        # Validate configuration
        validation_result = self._validate_circuit_breaker_config(config)
        config.validated = validation_result["result"] == ValidationResult.VALID
        config.validation_errors = validation_result.get("errors", [])
        
        with self._lock:
            self._circuit_breaker_configs[config_id] = config
            
            # Record tuning history
            if name not in self._tuning_history:
                self._tuning_history[name] = []
            self._tuning_history[name].append({
                "timestamp": datetime.now(UTC),
                "config_id": config_id,
                "action": "created",
                "scenario": scenario.value,
                "validated": config.validated
            })
        
        return {
            "config_id": config_id,
            "validation_result": validation_result["result"].value,
            "errors": config.validation_errors,
            "config": config
        }
    
    def _get_circuit_breaker_defaults(self, scenario: ScenarioType) -> dict[str, int]:
        """Get default circuit breaker parameters for scenario"""
        defaults = {
            ScenarioType.LOW_TRAFFIC: {
                "failure_threshold": 3,
                "timeout_seconds": 30,
                "half_open_max_calls": 2,
                "success_threshold": 2
            },
            ScenarioType.NORMAL_TRAFFIC: {
                "failure_threshold": 5,
                "timeout_seconds": 60,
                "half_open_max_calls": 3,
                "success_threshold": 3
            },
            ScenarioType.HIGH_TRAFFIC: {
                "failure_threshold": 10,
                "timeout_seconds": 90,
                "half_open_max_calls": 5,
                "success_threshold": 5
            },
            ScenarioType.PEAK_TRAFFIC: {
                "failure_threshold": 15,
                "timeout_seconds": 120,
                "half_open_max_calls": 8,
                "success_threshold": 7
            },
            ScenarioType.DEGRADED_PERFORMANCE: {
                "failure_threshold": 2,
                "timeout_seconds": 180,
                "half_open_max_calls": 1,
                "success_threshold": 3
            },
            ScenarioType.RECOVERY_MODE: {
                "failure_threshold": 3,
                "timeout_seconds": 240,
                "half_open_max_calls": 2,
                "success_threshold": 5
            }
        }
        return defaults.get(scenario, defaults[ScenarioType.NORMAL_TRAFFIC])
    
    def _validate_circuit_breaker_config(
        self,
        config: CircuitBreakerConfig
    ) -> dict[str, Any]:
        """
        Validate circuit breaker configuration
        
        Checks:
        - Threshold ranges
        - Timeout ranges
        - Success threshold consistency
        - Performance envelope alignment
        """
        errors: list[str] = []
        result = ValidationResult.VALID
        
        # Validate failure threshold
        if config.failure_threshold < 1:
            errors.append("failure_threshold must be >= 1")
            result = ValidationResult.INVALID
        if config.failure_threshold > 100:
            errors.append("failure_threshold > 100 may delay circuit opening")
            result = ValidationResult.WARNING if result == ValidationResult.VALID else result
        
        # Validate timeout
        if config.timeout_seconds < 1:
            errors.append("timeout_seconds must be >= 1")
            result = ValidationResult.INVALID
        if config.timeout_seconds > 600:
            errors.append("timeout_seconds > 600 (10 min) may be too long")
            result = ValidationResult.WARNING if result == ValidationResult.VALID else result
        
        # Validate half-open parameters
        if config.half_open_max_calls < 1:
            errors.append("half_open_max_calls must be >= 1")
            result = ValidationResult.INVALID
        if config.success_threshold < 1:
            errors.append("success_threshold must be >= 1")
            result = ValidationResult.INVALID
        if config.success_threshold > config.half_open_max_calls:
            errors.append("success_threshold cannot exceed half_open_max_calls")
            result = ValidationResult.INVALID
        
        # Check alignment with performance envelope
        envelope = self._performance_envelopes.get(config.scenario)
        if envelope and config.half_open_max_calls > envelope.max_concurrent_operations / 10:
            errors.append(
                f"half_open_max_calls too high for scenario {config.scenario.value} "
                f"(max_concurrent={envelope.max_concurrent_operations})"
            )
            result = ValidationResult.WARNING if result == ValidationResult.VALID else result
        
        return {
            "result": result,
            "errors": errors
        }
    
    def create_backoff_policy_config(
        self,
        name: str,
        scenario: ScenarioType,
        initial_delay_ms: int | None = None,
        max_retries: int | None = None,
        backoff_multiplier: float | None = None,
        max_delay_ms: int | None = None,
        jitter_enabled: bool = True,
        jitter_factor: float = 0.1
    ) -> dict[str, Any]:
        """
        Create backoff policy configuration for scenario
        
        Args:
            name: Configuration name
            scenario: Production scenario type
            initial_delay_ms: Starting delay (default: scenario-based)
            max_retries: Maximum retries (default: scenario-based)
            backoff_multiplier: Exponential factor (default: 2.0)
            max_delay_ms: Maximum delay cap (default: scenario-based)
            jitter_enabled: Enable jitter (default: True)
            jitter_factor: Jitter magnitude 0.0-1.0 (default: 0.1)
        
        Returns:
            dict with config_id and validation_result
        """
        config_id = str(uuid.uuid4())
        
        # Apply scenario-based defaults
        defaults = self._get_backoff_policy_defaults(scenario)
        
        config = BackoffPolicyConfig(
            config_id=config_id,
            name=name,
            initial_delay_ms=initial_delay_ms if initial_delay_ms is not None else defaults["initial_delay_ms"],
            max_retries=max_retries if max_retries is not None else defaults["max_retries"],
            backoff_multiplier=backoff_multiplier if backoff_multiplier is not None else defaults["backoff_multiplier"],
            max_delay_ms=max_delay_ms if max_delay_ms is not None else defaults["max_delay_ms"],
            jitter_enabled=jitter_enabled,
            jitter_factor=jitter_factor,
            scenario=scenario,
            organisation_id=self.organisation_id
        )
        
        # Validate configuration
        validation_result = self._validate_backoff_policy_config(config)
        config.validated = validation_result["result"] == ValidationResult.VALID
        config.validation_errors = validation_result.get("errors", [])
        
        with self._lock:
            self._backoff_configs[config_id] = config
            
            # Record tuning history
            if name not in self._tuning_history:
                self._tuning_history[name] = []
            self._tuning_history[name].append({
                "timestamp": datetime.now(UTC),
                "config_id": config_id,
                "action": "created",
                "scenario": scenario.value,
                "validated": config.validated
            })
        
        return {
            "config_id": config_id,
            "validation_result": validation_result["result"].value,
            "errors": config.validation_errors,
            "config": config
        }
    
    def _get_backoff_policy_defaults(self, scenario: ScenarioType) -> dict[str, Any]:
        """Get default backoff policy parameters for scenario"""
        defaults = {
            ScenarioType.LOW_TRAFFIC: {
                "initial_delay_ms": 100,
                "max_retries": 3,
                "backoff_multiplier": 2.0,
                "max_delay_ms": 5000
            },
            ScenarioType.NORMAL_TRAFFIC: {
                "initial_delay_ms": 200,
                "max_retries": 5,
                "backoff_multiplier": 2.0,
                "max_delay_ms": 10000
            },
            ScenarioType.HIGH_TRAFFIC: {
                "initial_delay_ms": 500,
                "max_retries": 4,
                "backoff_multiplier": 1.5,
                "max_delay_ms": 15000
            },
            ScenarioType.PEAK_TRAFFIC: {
                "initial_delay_ms": 1000,
                "max_retries": 3,
                "backoff_multiplier": 1.5,
                "max_delay_ms": 20000
            },
            ScenarioType.DEGRADED_PERFORMANCE: {
                "initial_delay_ms": 2000,
                "max_retries": 2,
                "backoff_multiplier": 3.0,
                "max_delay_ms": 30000
            },
            ScenarioType.RECOVERY_MODE: {
                "initial_delay_ms": 3000,
                "max_retries": 3,
                "backoff_multiplier": 2.0,
                "max_delay_ms": 60000
            }
        }
        return defaults.get(scenario, defaults[ScenarioType.NORMAL_TRAFFIC])
    
    def _validate_backoff_policy_config(
        self,
        config: BackoffPolicyConfig
    ) -> dict[str, Any]:
        """
        Validate backoff policy configuration
        
        Checks:
        - Delay ranges
        - Retry limits
        - Multiplier sanity
        - Jitter factor validity
        - Performance envelope alignment
        """
        errors: list[str] = []
        result = ValidationResult.VALID
        
        # Validate initial delay
        if config.initial_delay_ms < 1:
            errors.append("initial_delay_ms must be >= 1")
            result = ValidationResult.INVALID
        if config.initial_delay_ms > 10000:
            errors.append("initial_delay_ms > 10000 may cause long wait times")
            result = ValidationResult.WARNING if result == ValidationResult.VALID else result
        
        # Validate max retries
        if config.max_retries < 0:
            errors.append("max_retries must be >= 0")
            result = ValidationResult.INVALID
        if config.max_retries > 10:
            errors.append("max_retries > 10 may cause excessive delays")
            result = ValidationResult.WARNING if result == ValidationResult.VALID else result
        
        # Validate backoff multiplier
        if config.backoff_multiplier < 1.0:
            errors.append("backoff_multiplier must be >= 1.0")
            result = ValidationResult.INVALID
        if config.backoff_multiplier > 5.0:
            errors.append("backoff_multiplier > 5.0 causes very rapid growth")
            result = ValidationResult.WARNING if result == ValidationResult.VALID else result
        
        # Validate max delay
        if config.max_delay_ms < config.initial_delay_ms:
            errors.append("max_delay_ms must be >= initial_delay_ms")
            result = ValidationResult.INVALID
        if config.max_delay_ms > 120000:  # 2 minutes
            errors.append("max_delay_ms > 120000 (2 min) may be too long")
            result = ValidationResult.WARNING if result == ValidationResult.VALID else result
        
        # Validate jitter
        if config.jitter_factor < 0.0 or config.jitter_factor > 1.0:
            errors.append("jitter_factor must be between 0.0 and 1.0")
            result = ValidationResult.INVALID
        
        # Calculate total maximum delay
        total_max_delay = sum(
            min(config.initial_delay_ms * (config.backoff_multiplier ** i), config.max_delay_ms)
            for i in range(config.max_retries + 1)
        )
        
        # Check against performance envelope (only warn if extremely excessive)
        # Warn if total retry time exceeds 1 minute per retry attempt
        if total_max_delay > config.max_retries * 60000:
            errors.append(
                f"Total retry delay ({total_max_delay}ms) is extremely high (>1min per retry)"
            )
            result = ValidationResult.WARNING if result == ValidationResult.VALID else result
        
        return {
            "result": result,
            "errors": errors
        }
    
    def calibrate_for_scenario(
        self,
        scenario: ScenarioType,
        performance_metrics: dict[str, float]
    ) -> list[TuningRecommendation]:
        """
        Calibrate circuit breaker and backoff settings for scenario
        
        Args:
            scenario: Production scenario type
            performance_metrics: Current performance data (latency_p95, latency_p99, throughput, error_rate)
        
        Returns:
            List of tuning recommendations
        """
        recommendations: list[TuningRecommendation] = []
        envelope = self._performance_envelopes.get(scenario)
        
        if not envelope:
            return recommendations
        
        # Analyze circuit breaker tuning
        cb_recommendations = self._calibrate_circuit_breaker(
            scenario, performance_metrics, envelope
        )
        recommendations.extend(cb_recommendations)
        
        # Analyze backoff policy tuning
        backoff_recommendations = self._calibrate_backoff_policy(
            scenario, performance_metrics, envelope
        )
        recommendations.extend(backoff_recommendations)
        
        return recommendations
    
    def _calibrate_circuit_breaker(
        self,
        scenario: ScenarioType,
        metrics: dict[str, float],
        envelope: PerformanceEnvelope
    ) -> list[TuningRecommendation]:
        """Generate circuit breaker tuning recommendations"""
        recommendations: list[TuningRecommendation] = []
        defaults = self._get_circuit_breaker_defaults(scenario)
        
        # Check error rate
        error_rate = metrics.get("error_rate", 0.0)
        if error_rate > 0.05:  # > 5% errors
            recommendations.append(TuningRecommendation(
                recommendation_id=str(uuid.uuid4()),
                parameter_name="failure_threshold",
                current_value=defaults["failure_threshold"],
                recommended_value=max(2, defaults["failure_threshold"] - 2),
                reason="High error rate detected, lower threshold to open circuit faster",
                confidence=0.8,
                impact_estimate="high"
            ))
        
        # Check latency
        latency_p99 = metrics.get("latency_p99", 0.0)
        if latency_p99 > envelope.max_latency_p99_ms * 1.5:
            recommendations.append(TuningRecommendation(
                recommendation_id=str(uuid.uuid4()),
                parameter_name="timeout_seconds",
                current_value=defaults["timeout_seconds"],
                recommended_value=defaults["timeout_seconds"] + 30,
                reason="High latency detected, increase timeout before recovery attempt",
                confidence=0.7,
                impact_estimate="medium"
            ))
        
        return recommendations
    
    def _calibrate_backoff_policy(
        self,
        scenario: ScenarioType,
        metrics: dict[str, float],
        envelope: PerformanceEnvelope
    ) -> list[TuningRecommendation]:
        """Generate backoff policy tuning recommendations"""
        recommendations: list[TuningRecommendation] = []
        defaults = self._get_backoff_policy_defaults(scenario)
        
        # Check throughput
        throughput = metrics.get("throughput", 0.0)
        if throughput > envelope.max_throughput_rps * 0.8:
            recommendations.append(TuningRecommendation(
                recommendation_id=str(uuid.uuid4()),
                parameter_name="initial_delay_ms",
                current_value=defaults["initial_delay_ms"],
                recommended_value=int(defaults["initial_delay_ms"] * 1.5),
                reason="High throughput, increase backoff to reduce retry pressure",
                confidence=0.75,
                impact_estimate="medium"
            ))
        
        # Check retry success rate
        retry_success_rate = metrics.get("retry_success_rate", 0.0)
        if retry_success_rate < 0.3:  # < 30% retry success
            recommendations.append(TuningRecommendation(
                recommendation_id=str(uuid.uuid4()),
                parameter_name="max_retries",
                current_value=defaults["max_retries"],
                recommended_value=max(1, defaults["max_retries"] - 1),
                reason="Low retry success rate, reduce retries to fail faster",
                confidence=0.8,
                impact_estimate="high"
            ))
        
        return recommendations
    
    def get_config(self, config_id: str) -> CircuitBreakerConfig | BackoffPolicyConfig | None:
        """Retrieve configuration by ID"""
        with self._lock:
            return (
                self._circuit_breaker_configs.get(config_id) or
                self._backoff_configs.get(config_id)
            )
    
    def get_performance_envelope(self, scenario: ScenarioType) -> PerformanceEnvelope | None:
        """Retrieve performance envelope for scenario"""
        return self._performance_envelopes.get(scenario)
    
    def list_configs_for_scenario(
        self,
        scenario: ScenarioType
    ) -> dict[str, list[CircuitBreakerConfig | BackoffPolicyConfig]]:
        """List all configurations for a scenario"""
        with self._lock:
            circuit_breakers = [
                config for config in self._circuit_breaker_configs.values()
                if config.scenario == scenario
            ]
            backoff_policies = [
                config for config in self._backoff_configs.values()
                if config.scenario == scenario
            ]
            
            return {
                "circuit_breakers": circuit_breakers,
                "backoff_policies": backoff_policies
            }
