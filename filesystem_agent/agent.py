import os
from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams
from mcp.client.stdio import StdioServerParameters

TARGET_FOLDER_PATH = ".."
filesystem_toolset = MCPToolset(
    connection_params = StdioConnectionParams(
        server_params = StdioServerParameters(
            command="npx",
            args=[
                "-y",  # Argument for npx to auto-confirm install
                "@modelcontextprotocol/server-filesystem",
                os.path.abspath(TARGET_FOLDER_PATH),
            ],
        ),
    ),
)

from google.adk.agents import Agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="filesystem_agent",
    tools=[filesystem_toolset],
    instruction="파일 시스템 도구를 사용하여 파일과 디렉토리를 관리하십시오.",
)
