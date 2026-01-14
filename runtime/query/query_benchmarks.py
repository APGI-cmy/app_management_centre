"""
Query Performance Benchmarking

Provides performance benchmarking and validation for Wave 3.5 performance targets.
Implements P95/P99 latency tracking, throughput measurement, and performance envelope validation.

Authority: WAVE_3.5_ARCHITECTURE_FROZEN.md
Tenant Isolation: All operations scoped by organisation_id
"""

import time
import statistics
from typing import Any
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, UTC


@dataclass
class PerformanceBenchmark:
    """Performance benchmark result"""
    operation_name: str
    organisation_id: str
    execution_times: list[float] = field(default_factory=list)
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))
    
    def add_execution(self, exec_time: float) -> None:
        """Add execution time to benchmark"""
        self.execution_times.append(exec_time)
    
    def get_p50(self) -> float:
        """Get P50 (median) latency"""
        if not self.execution_times:
            return 0.0
        sorted_times = sorted(self.execution_times)
        return statistics.median(sorted_times)
    
    def get_p95(self) -> float:
        """Get P95 latency"""
        if not self.execution_times:
            return 0.0
        sorted_times = sorted(self.execution_times)
        index = int(len(sorted_times) * 0.95)
        if index >= len(sorted_times):
            index = len(sorted_times) - 1
        return sorted_times[index]
    
    def get_p99(self) -> float:
        """Get P99 latency"""
        if not self.execution_times:
            return 0.0
        sorted_times = sorted(self.execution_times)
        index = int(len(sorted_times) * 0.99)
        if index >= len(sorted_times):
            index = len(sorted_times) - 1
        return sorted_times[index]
    
    def get_average(self) -> float:
        """Get average latency"""
        if not self.execution_times:
            return 0.0
        return statistics.mean(self.execution_times)
    
    def get_min(self) -> float:
        """Get minimum latency"""
        if not self.execution_times:
            return 0.0
        return min(self.execution_times)
    
    def get_max(self) -> float:
        """Get maximum latency"""
        if not self.execution_times:
            return 0.0
        return max(self.execution_times)
    
    def meets_p95_target(self, target: float = 0.180) -> bool:
        """Check if P95 meets target (default 180ms)"""
        return self.get_p95() < target
    
    def meets_p99_target(self, target: float = 0.230) -> bool:
        """Check if P99 meets target (default 230ms)"""
        return self.get_p99() < target
    
    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for reporting"""
        return {
            'operation_name': self.operation_name,
            'organisation_id': self.organisation_id,
            'sample_size': len(self.execution_times),
            'p50': self.get_p50(),
            'p95': self.get_p95(),
            'p99': self.get_p99(),
            'average': self.get_average(),
            'min': self.get_min(),
            'max': self.get_max(),
            'meets_p95_target': self.meets_p95_target(),
            'meets_p99_target': self.meets_p99_target(),
            'timestamp': self.timestamp.isoformat()
        }


class QueryBenchmarkRunner:
    """
    Query Benchmark Runner
    
    Provides:
    - Query performance benchmarking
    - P95/P99 latency tracking
    - Performance target validation
    - Tenant-isolated benchmarking
    """
    
    def __init__(self):
        """Initialize benchmark runner"""
        self._benchmarks: dict[str, PerformanceBenchmark] = {}
        self._active = True
    
    def benchmark_query(self, 
                        operation_name: str,
                        organisation_id: str,
                        query_func: Callable[[], Any],
                        iterations: int = 100) -> PerformanceBenchmark:
        """
        Benchmark a query operation
        
        Args:
            operation_name: Name of operation being benchmarked
            organisation_id: Organisation ID for tenant isolation
            query_func: Function to execute for benchmarking
            iterations: Number of iterations to run
        
        Returns:
            PerformanceBenchmark with results
        """
        benchmark = PerformanceBenchmark(
            operation_name=operation_name,
            organisation_id=organisation_id
        )
        
        # Run iterations
        for _ in range(iterations):
            start = time.time()
            try:
                query_func()
            except Exception as e:
                # Record failed execution with high time
                benchmark.add_execution(999.0)  # 999 seconds = obvious failure
                continue
            end = time.time()
            
            exec_time = end - start
            benchmark.add_execution(exec_time)
        
        # Store benchmark
        key = f"{organisation_id}:{operation_name}"
        self._benchmarks[key] = benchmark
        
        return benchmark
    
    def get_benchmark(self, operation_name: str, organisation_id: str) -> PerformanceBenchmark | None:
        """Get stored benchmark"""
        key = f"{organisation_id}:{operation_name}"
        return self._benchmarks.get(key)
    
    def get_all_benchmarks(self) -> dict[str, PerformanceBenchmark]:
        """Get all stored benchmarks"""
        return self._benchmarks.copy()
    
    def generate_report(self, organisation_id: str | None = None) -> dict[str, Any]:
        """
        Generate performance report
        
        Args:
            organisation_id: Optional filter by organisation ID
        
        Returns:
            Performance report with all benchmarks
        """
        benchmarks_to_report = []
        
        for key, benchmark in self._benchmarks.items():
            if organisation_id is None or benchmark.organisation_id == organisation_id:
                benchmarks_to_report.append(benchmark.to_dict())
        
        # Calculate aggregate metrics
        all_p95 = [b.get_p95() for b in self._benchmarks.values()]
        all_p99 = [b.get_p99() for b in self._benchmarks.values()]
        
        return {
            'total_benchmarks': len(benchmarks_to_report),
            'aggregate_p95': statistics.mean(all_p95) if all_p95 else 0.0,
            'aggregate_p99': statistics.mean(all_p99) if all_p99 else 0.0,
            'all_meet_p95_target': all(b.meets_p95_target() for b in self._benchmarks.values()),
            'all_meet_p99_target': all(b.meets_p99_target() for b in self._benchmarks.values()),
            'benchmarks': benchmarks_to_report
        }
    
    def clear_benchmarks(self) -> None:
        """Clear all stored benchmarks"""
        self._benchmarks.clear()


class PerformanceValidator:
    """
    Performance Target Validator
    
    Validates performance against Wave 3.5 targets:
    - P95 latency < 180ms
    - P99 latency < 230ms
    - Query execution < 100ms (P95)
    - Cache hit rate ≥ 80%
    """
    
    # Performance targets
    P95_TARGET = 0.180  # 180ms
    P99_TARGET = 0.230  # 230ms
    QUERY_P95_TARGET = 0.100  # 100ms for queries
    CACHE_HIT_RATE_TARGET = 0.80  # 80%
    
    @staticmethod
    def validate_p95_latency(latency: float) -> dict[str, Any]:
        """Validate P95 latency"""
        meets_target = latency < PerformanceValidator.P95_TARGET
        
        return {
            'metric': 'p95_latency',
            'value': latency,
            'target': PerformanceValidator.P95_TARGET,
            'meets_target': meets_target,
            'margin': PerformanceValidator.P95_TARGET - latency,
            'status': 'PASS' if meets_target else 'FAIL'
        }
    
    @staticmethod
    def validate_p99_latency(latency: float) -> dict[str, Any]:
        """Validate P99 latency"""
        meets_target = latency < PerformanceValidator.P99_TARGET
        
        return {
            'metric': 'p99_latency',
            'value': latency,
            'target': PerformanceValidator.P99_TARGET,
            'meets_target': meets_target,
            'margin': PerformanceValidator.P99_TARGET - latency,
            'status': 'PASS' if meets_target else 'FAIL'
        }
    
    @staticmethod
    def validate_query_execution(latency: float) -> dict[str, Any]:
        """Validate query execution time"""
        meets_target = latency < PerformanceValidator.QUERY_P95_TARGET
        
        return {
            'metric': 'query_p95_execution',
            'value': latency,
            'target': PerformanceValidator.QUERY_P95_TARGET,
            'meets_target': meets_target,
            'margin': PerformanceValidator.QUERY_P95_TARGET - latency,
            'status': 'PASS' if meets_target else 'FAIL'
        }
    
    @staticmethod
    def validate_cache_hit_rate(hit_rate: float) -> dict[str, Any]:
        """Validate cache hit rate"""
        meets_target = hit_rate >= PerformanceValidator.CACHE_HIT_RATE_TARGET
        
        return {
            'metric': 'cache_hit_rate',
            'value': hit_rate,
            'target': PerformanceValidator.CACHE_HIT_RATE_TARGET,
            'meets_target': meets_target,
            'margin': hit_rate - PerformanceValidator.CACHE_HIT_RATE_TARGET,
            'status': 'PASS' if meets_target else 'FAIL'
        }
    
    @staticmethod
    def validate_all(benchmark: PerformanceBenchmark, cache_hit_rate: float | None = None) -> dict[str, Any]:
        """
        Validate all performance targets
        
        Args:
            benchmark: Performance benchmark to validate
            cache_hit_rate: Optional cache hit rate
        
        Returns:
            Complete validation report
        """
        validations = {
            'p95_latency': PerformanceValidator.validate_p95_latency(benchmark.get_p95()),
            'p99_latency': PerformanceValidator.validate_p99_latency(benchmark.get_p99()),
            'query_execution': PerformanceValidator.validate_query_execution(benchmark.get_p95())
        }
        
        if cache_hit_rate is not None:
            validations['cache_hit_rate'] = PerformanceValidator.validate_cache_hit_rate(cache_hit_rate)
        
        # Overall status
        all_pass = all(v['meets_target'] for v in validations.values())
        
        return {
            'operation': benchmark.operation_name,
            'organisation_id': benchmark.organisation_id,
            'validations': validations,
            'overall_status': 'PASS' if all_pass else 'FAIL',
            'timestamp': benchmark.timestamp.isoformat()
        }
