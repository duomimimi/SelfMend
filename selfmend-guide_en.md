# SelfMend User Guide

> Self-Healing AI System — Monitor Health, Detect Problems, Auto-Repair, Prevent Recurrence

---

## Core Concept

SelfMend is a **self-healing AI framework** whose core philosophy is: AI systems should not rely on human repair after failures. Instead, they should have self-monitoring, self-diagnosis, and self-repair capabilities, achieving true autonomous operations.

**Why does it matter?**

Production AI systems face failure types far beyond traditional software:
- **Model Drift**: Model performance degrades as data distribution changes
- **Hallucination Outbreaks**: Output quality drops sharply under specific trigger conditions
- **Cascading Failures**: Problems in one component spread to the entire system
- **Resource Exhaustion**: API quotas, token explosions, memory leaks

Traditional solutions rely on human monitoring + human intervention:
- Delayed failure discovery (slow human inspection)
- Difficult failure localization (complex system)
- Slow repair speed (requires human analysis + execution)

SelfMend automates this: Monitor → Detect → Diagnose → Fix → Prevent

---

## How to Use

### Step 1: Initialize Health Monitoring

```python
from selfmend import SelfMendSystem, HealthMonitor

# Create self-healing system
system = SelfMendSystem(
    name="production-ai-assistant",
    check_interval=60  # Check health status every 60 seconds
)

# Define health metrics
monitor = HealthMonitor(system)
monitor.track("response_latency", threshold=2000)  # Alert if response latency > 2 seconds
monitor.track("error_rate", threshold=0.05)        # Alert if error rate > 5%
monitor.track("hallucination_rate", threshold=0.1) # Alert if hallucination rate > 10%
```

### Step 2: Register Auto-Repair Strategies

```python
from selfmend import RepairStrategy

# Define repair strategies
strategies = [
    RepairStrategy(
        trigger="response_latency_high",
        action="scale_up",
        params={"max_retry": 3}
    ),
    RepairStrategy(
        trigger="error_rate_high",
        action="circuit_break",
        params={"reset_timeout": 60}
    ),
    RepairStrategy(
        trigger="hallucination_rate_high",
        action="switch_model",
        params={"fallback_order": ["claude", "gpt"]}
    ),
    RepairStrategy(
        trigger="api_quota_exceeded",
        action="queue_requests",
        params={"max_queue": 1000}
    )
]

for strategy in strategies:
    system.register_strategy(strategy)
```

### Step 3: Start Monitoring

```python
# Start self-healing system
system.start()

# System automatically:
# 1. Continuously monitors health metrics
# 2. Triggers corresponding repair strategies when anomalies detected
# 3. Verifies recovery after repair
# 4. Records failure patterns for prevention
```

---

## Code Example

```python
import asyncio
from selfmend import SelfMendSystem

async def run_production_system():
    system = SelfMendSystem(name="ai-assistant")

    # Register components
    system.register_component("nexuscore", nexuscore_instance)
    system.register_component("truthmatrix", truthmatrix_instance)
    system.register_component("agenthive", agenthive_instance)

    # Set auto-recovery policies
    system.set_recovery_policy({
        "nexuscore": {
            "failure": "restart",
            "degradation": "reduce_load"
        },
        "truthmatrix": {
            "failure": "bypass",  # Bypass validation layer to ensure service availability
            "degradation": "lower_threshold"
        }
    })

    # Start monitoring
    await system.start()

    # View system health status
    status = system.get_health_status()
    print(f"System Health: {status.overall_score}")
    print(f"Active Alerts: {len(status.alerts)}")

asyncio.run(run_production_system())
```

---

## Use Cases

### Case 1: 24/7 Online AI Service
E-commerce website AI customer service must be available 24 hours. SelfMend monitors response latency, error rate, and API quotas — when issues are detected, automatically triggers: rate limiting → degraded service → model switching → human alert. User experiences no interruption.

### Case 2: Financial Trading AI System
Trading systems have extremely high stability requirements. SelfMend monitors model prediction quality, latency anomalies, and data anomalies. When model drift is detected, automatically switches to backup model and alerts.

### Case 3: Large-Scale API Services
AI API services for developers need SLA guarantees. SelfMend monitors each tenant's usage, latency, and errors, automatically performing capacity planning and fault isolation.

### Case 4: Multi-Model Production Environment
Production environments running multiple model instances. SelfMend monitors each model's health, automatically performing load balancing, failover, and version upgrades.

---

## Relationship with Other Modules

| Module | Relationship | Description |
|:----:|:----:|:-----|
| NexusCore | Core Monitored Object | SelfMend monitors NexusCore's routing quality and latency |
| TruthMatrix | Issue Trigger Source | Quality issues found by TruthMatrix trigger SelfMend repair |
| QualityForge | Long-Term Health Analysis | QualityForge quality scores help SelfMend predict issues |
| AgentHive | Repair Executor | Repair agents in AgentHive execute SelfMend repair directives |

**Architecture Position**: SelfMend is the guarantee layer, responsible for the healthy operation and fault recovery of the entire system — the guardian of production environments.

---

## Fault Handling Flow

```python
# Example of SelfMend's auto-handling flow

alert = system.get_active_alerts()[0]

print(f"""
Fault: {alert.name}
Severity: {alert.severity}
Trigger Time: {alert.timestamp}

Auto-Handling:
  1. Diagnosis: {alert.diagnosis}
  2. Cause: {alert.root_cause}
  3. Action: {alert.action_taken}
  4. Result: {alert.outcome}
  5. Prevention: {alert.prevention_learned}

Status: {'✅ Recovered' if alert.resolved else '🔄 Processing'}
""")
```

---

## Next Steps

- See the [QualityForge Guide](./qualityforge-guide_en.md) — How to prevent quality issues
- See the [NexusCore Guide](./nexuscore-guide_en.md) — How to achieve high-availability routing
- Get started: `pip install selfmend`

---

*SelfMend — Upgrade AI systems from "fix when broken" to "never down"*