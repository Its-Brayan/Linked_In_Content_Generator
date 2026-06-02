import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client,StdioServerParameters
import os
from dotenv import load_dotenv
load_dotenv()
async def connect_to_github_mcp():
    print("Starting MCP connection...")
    server_params = StdioServerParameters(
       command="npx",
            args=["-y", "@modelcontextprotocol/server-github"],
            env={
                "GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("ACCESS_TOKEN")
            }
    )


    async with stdio_client(server_params) as (read,write):
         print("Transport (stdio) connected")
         async with ClientSession(read,write) as session:
                 print("Session created")
                 await session.initialize()
                 print("MCP initialized successfully")

                 tools = await session.list_tools()
                 for tool in tools.tools:
                       print(tool.name)
               
                 
