from google.adk.agents import Agent
from google.adk.tools import AgentTool

summarizer = Agent(
    name="summarizer",
    model="gemini-2.5-flash",
    description="Agent to summarize text",
    instruction="주어진 내용을 간결하게 요약하십시오. 끝에는 ㅇㅅㅇ를 붙일것",
)

# root_agent = Agent(
#     name="summary_agent",
#     model="gemini-2.5-flash",
#     instruction="요약이 요청되면, **summarizer** 에이전트를 사용하여 텍스트를 요약하십시오.",
#     sub_agents=[summarizer]
# )

root_agent = Agent(
    name="summary_agent",
    model="gemini-2.5-flash",
    instruction="요약이 요청되면, **summarizer** 툴을 사용하여 텍스트를 요약하십시오.",
    tools=[AgentTool(agent=summarizer)]
)
