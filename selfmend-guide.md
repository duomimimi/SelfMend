# SelfMend 使用指南

> 自我修复AI系统——监控健康、发现问题、自动修复、预防复发

---

## 核心概念

SelfMend 是一个**自我修复AI框架**，它的核心理念是：AI系统不应该在出错后依赖人工修复，而应该具备自我监控、自我诊断、自我修复的能力，实现真正的自主运维。

**为什么重要？**

生产环境中的AI系统面临的故障类型远超传统软件：
- **模型漂移**：模型性能随数据分布变化而下降
- **幻觉爆发**：特定触发条件下输出质量急剧下降
- **级联失败**：某个环节的问题扩散到整个系统
- **资源耗尽**：API限额、Token爆炸、内存泄漏

传统方案是人工监控+人工干预，但：
- 故障发现滞后（人工巡检慢）
- 故障定位困难（系统复杂）
- 修复速度慢（需要人工分析+执行）

SelfMend 将这个过程自动化：Monitor → Detect → Diagnose → Fix → Prevent

---

## 如何使用

### 第一步：初始化健康监控

```python
from selfmend import SelfMendSystem, HealthMonitor

# 创建自修复系统
system = SelfMendSystem(
    name="production-ai-assistant",
    check_interval=60  # 每60秒检查一次健康状态
)

# 定义健康指标
monitor = HealthMonitor(system)
monitor.track("response_latency", threshold=2000)  # 响应延迟>2秒告警
monitor.track("error_rate", threshold=0.05)        # 错误率>5%告警
monitor.track("hallucination_rate", threshold=0.1) # 幻觉率>10%告警
```

### 第二步：注册自动修复策略

```python
from selfmend import RepairStrategy

# 定义修复策略
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

### 第三步：启动监控

```python
# 启动自修复系统
system.start()

# 系统自动：
# 1. 持续监控各项健康指标
# 2. 异常时触发对应修复策略
# 3. 修复后验证是否恢复
# 4. 记录故障模式用于预防
```

---

## 代码示例

```python
import asyncio
from selfmend import SelfMendSystem

async def run_production_system():
    system = SelfMendSystem(name="ai-assistant")

    # 注册组件
    system.register_component("nexuscore", nexuscore_instance)
    system.register_component("truthmatrix", truthmatrix_instance)
    system.register_component("agenthive", agenthive_instance)

    # 设置自动恢复
    system.set_recovery_policy({
        "nexuscore": {
            "failure": "restart",
            "degradation": "reduce_load"
        },
        "truthmatrix": {
            "failure": "bypass",  # 旁路验证层，保证服务可用
            "degradation": "lower_threshold"
        }
    })

    # 启动监控
    await system.start()

    # 查看系统健康状态
    status = system.get_health_status()
    print(f"系统健康: {status.overall_score}")
    print(f"活跃告警: {len(status.alerts)}")

asyncio.run(run_production_system())
```

---

## 适用场景

### 场景1：24/7在线AI服务
电商网站的AI客服必须24小时可用。SelfMend监控响应延迟、错误率、API配额，一旦发现问题自动触发修复：限流→降级→切换模型→告警人工，用户无感知。

### 场景2：金融交易AI系统
交易系统对稳定性要求极高。SelfMend监控模型预测质量、延迟异常、数据异常，一旦检测到模型漂移自动切换备份模型并告警。

### 场景3：大规模API服务
面向开发者的AI API服务，需要保障SLA。SelfMend监控各租户的用量、延迟、错误，自动进行容量规划和故障隔离。

### 场景4：多模型生产环境
同时运行多个模型实例的生产环境。SelfMend监控每个模型的健康状态，自动进行负载均衡、故障转移、版本升级。

---

## 与其他模块的关系

| 模块 | 关系 | 说明 |
|:----:|:----:|:-----|
| NexusCore | 核心监控对象 | SelfMend监控NexusCore的路由质量和延迟 |
| TruthMatrix | 问题触发源 | TruthMatrix发现的质量问题触发SelfMend修复 |
| QualityForge | 长期健康分析 | QualityForge的质量评分帮助SelfMend预测问题 |
| AgentHive | 修复执行者 | AgentHive中的修复Agent执行SelfMend的修复指令 |

**架构定位**：SelfMend是保障层，负责整个系统的健康运行和故障恢复，是生产环境的守护者。

---

## 故障处理流程

```python
# SelfMend的自动处理流程示例

alert = system.get_active_alerts()[0]

print(f"""
故障: {alert.name}
严重度: {alert.severity}
触发时间: {alert.timestamp}

自动处理:
  1. 诊断: {alert.diagnosis}
  2. 原因: {alert.root_cause}
  3. 动作: {alert.action_taken}
  4. 结果: {alert.outcome}
  5. 预防: {alert.prevention_learned}

状态: {'✅ 已恢复' if alert.resolved else '🔄 处理中'}
""")
```

---

## 下一步

- 查看 [QualityForge 指南](./qualityforge-guide.md) — 如何预防质量问题
- 查看 [NexusCore 指南](./nexuscore-guide.md) — 如何实现高可用路由
- 开始集成：pip install selfmend

---

*SelfMend — 让AI系统从"坏了再修"升级为"永不宕机"*