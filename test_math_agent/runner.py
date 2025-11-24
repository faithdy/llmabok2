import dotenv
dotenv.load_dotenv()

from agent import root_agent

import asyncio
from google.adk.runners import InMemoryRunner
from google.genai.types import UserContent

async def main():
    runner = InMemoryRunner(agent=root_agent, app_name=root_agent.name)
    session = await runner.session_service.create_session(app_name=runner.app_name, user_id="user_123")

    while True:
        user_input = input("질문을 입력하세요: ")
        if user_input.lower() == "exit":
            break

        for event in runner.run(user_id="user_123", session_id=session.id, new_message=UserContent(user_input)):
            response = event.content.parts[0].text

        print(f"에이전트 응답: {response}")

        if runner.session_service.get_session(app_name=session.app_name, user_id=session.user_id, session_id=session.id):
            session = await runner.session_service.get_session(app_name=session.app_name, user_id=session.user_id, session_id=session.id)
            print(session.events)            
asyncio.run(main())