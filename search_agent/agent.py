from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="search_agent",
    model="gemini-2.5-flash",
    instruction="사용자가 정보를 검색하도록 도와주십시오.",
    tools=[google_search]
)
