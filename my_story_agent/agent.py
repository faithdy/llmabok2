from google.adk.agents import SequentialAgent, LoopAgent
from .sub_agents import initial_writer_agent, critic_agent, reviser_agent

# Loop agent: 반복적으로 비평->수정 과정을 돌려 시놉시스를 개선합니다.
loop_agent = LoopAgent(
    name="synopsis_loop_agent",
    description=(
        "An agent that loops through critiquing and revising a short synopsis until it meets the defined quality guidelines."
    ),
    sub_agents=[critic_agent, reviser_agent],
    max_iterations=3,
)

# Root agent: 1줄 로그라인을 받아 초기 시놉시스를 만들고,
# 그 후 루프 에이전트로 비평과 수정을 반복하여 완성도 높은 시놉시스를 산출합니다.
root_agent = SequentialAgent(
    name="synopsis_root_agent",
    description=(
        "Orchestrates the flow: accept a single-line logline input, generate an initial synopsis, "
        "then iteratively critique and revise to produce a polished synopsis."
    ),
    sub_agents=[initial_writer_agent, loop_agent],
)