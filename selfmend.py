# SelfMend - AI System Self-Healing Framework
# Auto-detect, auto-fix, auto-prevent

from typing import Callable, Optional
from enum import Enum

class HealthStatus(Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    CRITICAL = "critical"
    UNKNOWN = "unknown"

class HealthMonitor:
    """Monitor system health with multi-layer checks."""

    def __init__(self):
        self.checks = []
        self.last_results = {}

    def register_check(self, name: str, check_fn: Callable, weight: float = 1.0):
        self.checks.append({"name": name, "fn": check_fn, "weight": weight})

    def run_checks(self) -> dict:
        results = {}
        for check in self.checks:
            try:
                result = check["fn"]()
                results[check["name"]] = {"passed": result, "weight": check["weight"]}
            except Exception as e:
                results[check["name"]] = {"passed": False, "weight": check["weight"], "error": str(e)}
        
        total_weight = sum(r["weight"] for r in results.values())
        weighted_score = sum(
            (1.0 if r["passed"] else 0.0) * r["weight"] 
            for r in results.values()
        ) / max(total_weight, 1.0)
        
        status = HealthStatus.HEALTHY
        if weighted_score < 0.5:
            status = HealthStatus.CRITICAL
        elif weighted_score < 0.8:
            status = HealthStatus.DEGRADED
        
        self.last_results = results
        return {
            "status": status.value,
            "score": weighted_score,
            "checks": results
        }


class SelfHealer:
    """Automatically heal detected issues."""

    def __init__(self):
        self.remedy_map = {}
        self.healing_history = []

    def register_remedy(self, issue_type: str, remedy_fn: Callable):
        self.remedy_map[issue_type] = remedy_fn

    def heal(self, issue_type: str, context: dict) -> dict:
        if issue_type not in self.remedy_map:
            return {"success": False, "reason": "No remedy registered"}
        
        remedy_fn = self.remedy_map[issue_type]
        try:
            result = remedy_fn(context)
            self.healing_history.append({
                "issue": issue_type,
                "result": result,
                "success": True
            })
            return {"success": True, "result": result}
        except Exception as e:
            self.healing_history.append({
                "issue": issue_type,
                "error": str(e),
                "success": False
            })
            return {"success": False, "error": str(e)}


class PreventionEngine:
    """Predict and prevent issues before they occur."""

    def __init__(self):
        self.patterns = []

    def record(self, event: dict):
        self.patterns.append(event)

    def predict_risk(self, current_state: dict) -> list[dict]:
        """Predict potential issues based on past patterns."""
        risks = []
        # Simplified pattern matching
        if current_state.get("latency", 0) > 1000:
            risks.append({"type": "high_latency", "probability": 0.7})
        if current_state.get("error_rate", 0) > 0.05:
            risks.append({"type": "high_error_rate", "probability": 0.8})
        return risks


if __name__ == "__main__":
    monitor = HealthMonitor()
    monitor.register_check("api", lambda: True)
    monitor.register_check("memory", lambda: True)
    result = monitor.run_checks()
    print("Health:", result)