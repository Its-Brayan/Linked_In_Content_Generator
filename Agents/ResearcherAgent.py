from Tools.github_mcp import connect_to_github_mcp
from typing import Dict
class ResearcherAgent:

    async def research_agent(self,session,repo_info):
        owner = repo_info['owner']
        repo = repo_info['repo']

        print(f"Reading repo {owner}\n {repo}")

        readme = await session.call_tool(
            "get_file_contents",
            {
                "owner":owner,
                "repo":repo,
                "path":""
            }
        )
        print("Here is the readme file",readme)
        tree =await session.call_tool(
            "get_file_contents",
            {
                "owner":owner,
                "repo":repo,
                "path":""
            }
        )
        print("Here is the directory structure",tree)
        return {
            "readme":readme,
            "tree":tree
        }