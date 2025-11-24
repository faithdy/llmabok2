from google.adk.agents import Agent

root_agent = Agent(
    name="test_agent",
    model="gemini-2.5-flash",
    instruction="모든 답변은 한국어로 작성하고, 각 문장의 끝에는 'ㅇㅅㅇ' 를 붙여",
)