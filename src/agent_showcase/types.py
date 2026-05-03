from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


AgentRole = Literal["planner", "executor", "validator", "orchestrator", "reviewer"]


@dataclass(frozen=True)
class AgentStep:
    role: AgentRole
    action: str
    output: str


@dataclass(frozen=True)
class CaseStudy:
    key: str
    title: str
    source_repo: str
    license_name: str
    pain_point: str
    logic_flow: list[str] = field(default_factory=list)
    rewrite_points: list[str] = field(default_factory=list)
    agent_roles: list[str] = field(default_factory=list)
