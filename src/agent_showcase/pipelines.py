from __future__ import annotations

from .cases import CASES
from .types import CaseStudy, AgentStep


def build_overview() -> list[dict[str, object]]:
    return [
        {
            "key": case.key,
            "title": case.title,
            "source_repo": case.source_repo,
            "license": case.license_name,
            "pain_point": case.pain_point,
            "logic_flow": case.logic_flow,
            "rewrite_points": case.rewrite_points,
            "agent_roles": case.agent_roles,
        }
        for case in CASES
    ]


def build_case_report(case: CaseStudy) -> dict[str, object]:
    steps = [
        AgentStep(role="planner", action=case.logic_flow[0], output=case.pain_point),
        AgentStep(
            role="executor",
            action=case.logic_flow[1] if len(case.logic_flow) > 1 else "执行",
            output="执行分流和上下文收集。",
        ),
        AgentStep(
            role="validator",
            action=case.logic_flow[-1],
            output="输出校验、引用校验或回退结论。",
        ),
    ]
    return {
        "title": case.title,
        "source_repo": case.source_repo,
        "license": case.license_name,
        "pain_point": case.pain_point,
        "logic_flow": case.logic_flow,
        "rewrite_points": case.rewrite_points,
        "agent_roles": case.agent_roles,
        "sample_steps": [step.__dict__ for step in steps],
    }
