from google.adk.agents import Agent

from datetime import datetime
def get_today() -> str:
    """
    오늘의 날짜와 요일을 반환합니다.
    """
    return str(datetime.now())

root_agent = Agent(
    name="date_agent",
    model="gemini-2.5-flash",
    instruction=f"오늘은 {get_today()} 입니다. 사용자의 날짜와 요일에 관한 질문에 답하세요.",
)
