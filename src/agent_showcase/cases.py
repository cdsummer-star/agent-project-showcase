from __future__ import annotations

from .types import CaseStudy


CASES: list[CaseStudy] = [
    CaseStudy(
        key="nanobrowser",
        title="Nanobrowser Rewrite",
        source_repo="nanobrowser/nanobrowser",
        license_name="Apache-2.0",
        pain_point="浏览器任务容易卡在页面状态、权限确认、操作失败和回退重试。",
        logic_flow=[
            "任务理解",
            "子任务拆解",
            "浏览器执行",
            "页面校验",
            "失败回退",
        ],
        rewrite_points=[
            "把高风险操作单独抽成确认门",
            "把执行日志和页面状态分离",
            "把失败重试改成带上下文的回退策略",
        ],
        agent_roles=["planner", "executor", "validator"],
    ),
    CaseStudy(
        key="doc-research",
        title="Multi-Agent Doc Research Rewrite",
        source_repo="Azure/multi-agent-doc-research",
        license_name="MIT",
        pain_point="长文档研究容易漏证据、漏引用、结论泛化。",
        logic_flow=[
            "文档切块",
            "语义检索",
            "证据筛选",
            "多 agent 写作",
            "质量校验",
        ],
        rewrite_points=[
            "把答案拆成证据链和结论链",
            "把引用校验做成独立 validator",
            "把 query rewrite 和 report outline 前置",
        ],
        agent_roles=["planner", "researcher", "writer", "validator"],
    ),
    CaseStudy(
        key="deep-research",
        title="Deep Research Agent Rewrite",
        source_repo="tarun7r/deep-research-agent",
        license_name="MIT",
        pain_point="研究任务需要可追溯、可复核、可评分，不能只有结果文本。",
        logic_flow=[
            "Planner",
            "Searcher",
            "Synthesizer",
            "Writer",
            "Validator",
        ],
        rewrite_points=[
            "把研究过程显式化",
            "加入可信度评分",
            "把 section-level retry 作为质量门",
        ],
        agent_roles=["planner", "executor", "validator", "reviewer"],
    ),
    CaseStudy(
        key="agentmesh",
        title="AgentMesh Rewrite",
        source_repo="hupe1980/agentmesh",
        license_name="Apache-2.0",
        pain_point="多 agent 并发时，调度、状态、checkpoint、观测最难。",
        logic_flow=[
            "图调度",
            "并行执行",
            "状态聚合",
            "checkpoint",
            "观测",
        ],
        rewrite_points=[
            "把 orchestration 层单独抽出来",
            "把状态和执行解耦",
            "把观测指标作为一等公民",
        ],
        agent_roles=["orchestrator", "planner", "executor", "validator"],
    ),
]
