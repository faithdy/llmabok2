import dotenv
dotenv.load_dotenv()

from agent import root_agent

import asyncio
from google.adk.runners import InMemoryRunner
from google.genai.types import UserContent

async def main():
    runner = InMemoryRunner(agent=root_agent, app_name=root_agent.name)
    session = await runner.session_service.create_session(app_name=runner.app_name, user_id="user1")
    
    print('new session created')

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        elif user_input.lower() == "new":
            session = await runner.session_service.get_session(session_id=session.id, app_name=runner.app_name, user_id=session.user_id)
            await runner.memory_service.add_session_to_memory(session)
            session = await runner.session_service.create_session(app_name=runner.app_name, user_id="user1")
        else:
            for event in runner.run(user_id=session.user_id, session_id=session.id, new_message=UserContent(user_input)):
                response = event.content.parts[0].text

            print(f"AI: {response}")

asyncio.run(main())