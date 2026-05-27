# SelfMend

**Self-Healing AI System**

SelfMend is an autonomous healing framework that monitors AI systems for failures, detects anomalies in real-time, automatically fixes issues, and prevents future failures by learning from patterns. When something goes wrong, SelfMend heals itself.

## Key Features

- **Failure Monitoring**: Continuous health checks on AI systems with real-time alerting
- **Anomaly Detection**: Identify unusual patterns in outputs before they become failures
- **Auto-Fix Engine**: Automatically diagnose and repair common failure modes
- **Pattern Learning**: Build a failure pattern library to prevent recurring issues
- **Preventive Maintenance**: Proactively reinforce systems prone to failure
- **Self-Quarantine**: Isolate compromised or degraded components until fixed

## Quick Start

```bash
# Install
pip install selfmend

# Basic usage
from selfmend import SelfMendSystem, Monitor

mend = SelfMendSystem(config={
    "health_check_interval": 60,
    "auto_fix_enabled": True,
    "quarantine_threshold": 0.7
})

# Monitor an AI service
monitor = mend.monitor(my_ai_service)

# SelfMend will:
# 1. Detect failures automatically
# 2. Diagnose root cause
# 3. Apply auto-fix if known
# 4. Quarantine if severe
# 5. Learn pattern for prevention
```

## Architecture

```
┌─────────────────────────────────────────────┐
│           Monitored AI System                │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│          SelfMend Controller                 │
│  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Health    │  │   Anomaly           │  │
│  │  Monitor   │  │   Detector          │  │
│  └─────────────┘  └─────────────────────┘  │
│  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Auto-Fix │  │   Pattern           │  │
│  │  Engine    │  │   Learner          │  │
│  └─────────────┘  └─────────────────────┘  │
└─────────────────────┬───────────────────────┘
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
     ┌─────────┐           ┌─────────────┐
     │ Healthy │           │ Quarantine  │
     │ (OK)    │           │ + Repair    │
     └─────────┘           └─────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│        Failure Pattern Library               │
│    (Preventive Reinforcement)               │
└─────────────────────────────────────────────┘
```

**Core Components:**

- **Health Monitor**: Continuous system health checks and metrics collection
- **Anomaly Detector**: Statistical and ML-based anomaly identification
- **Auto-Fix Engine**: Rule-based and learned repair strategies
- **Quarantine Manager**: Isolates degraded components to prevent cascade failures
- **Pattern Learner**: Builds and maintains failure pattern database
- **Preventive Reinforcer**: Proactively strengthens vulnerable components

## License

MIT License