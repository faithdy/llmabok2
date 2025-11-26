import dotenv
dotenv.load_dotenv()

from agent import root_agent

import asyncio
from google.adk.runners import InMemoryRunner
from google.genai.types import UserContent, Part

async def main():
    runner = InMemoryRunner(agent=root_agent, app_name=root_agent.name)
    session = await runner.session_service.create_session(app_name=root_agent.name, user_id="user1")

    request = "회식 비용 $250을 환급해주세요."

    for event in runner.run(
        user_id=session.user_id, session_id=session.id,
        new_message=UserContent(request)
    ):
        if event.content.parts:
            for part in event.content.parts:
                if part.function_response:
                    approval_request = part.function_response
                elif part.text:
                    response = part.text

    print(f"Agent: {response}")
    
    approval_request.response['status'] = 'approved'

    for event in runner.run(user_id=session.user_id, session_id=session.id,
                            new_message=UserContent(parts=[Part(function_response=approval_request)])):
        response = event.content.parts[0].text if event.content.parts else ""

    print(f"Agent: {response}")


asyncio.run(main())