
import os
import sys
import shutil
print("NPX",shutil.which("npx"))
print("NODE",shutil.which("node"))
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import asyncio
sys.path.insert(0,ROOT_DIR)
from Agents.PlannerAgent import PlannerAgent
from Agents.ResearcherAgent import ResearcherAgent
from Agents.ReviewAgent import ReviewAgent
from Agents.WriterAgent import WriterAgent
from typing import TypedDict
from langgraph.graph import StateGraph, END
from Tools.github_mcp import connect_to_github_mcp
from Tools.websearcher import extract_github_url
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client,StdioServerParameters

planner = PlannerAgent()
researcher = ResearcherAgent()
Reviewer = ReviewAgent()
writer = WriterAgent()

DEFAULT_AUDIENCES = ["LinkedIn", "developers", "non-developers"]
class AiContentTeam(TypedDict):
    query: str
    plan: str
    research: dict
    draft: str
    review: str
    mcp_session: ClientSession
    audiences: list[str]

def planner_node(state:AiContentTeam) -> AiContentTeam:
    print(f"Analyzing query: {state['query']}")
    agent_planner = planner.run(state['query'], state.get('audiences', DEFAULT_AUDIENCES))
    result = agent_planner['planner']
    state['plan'] = result.content

    return state

async def researcher_node(state:AiContentTeam) -> AiContentTeam:

    print(f"researching about: {state['query']}")
    query = extract_github_url(state['query'])
    agent_research = await researcher.research_agent(state['mcp_session'],query)
    result = {
         "readme":agent_research['readme'],
         "tree":agent_research['tree']
    }
    state['research'] = result
    
    return state

def writer_node(state:AiContentTeam) -> AiContentTeam:
    print(f"Writing for audiences: {state['audiences']}")
    agent_writer = writer.run(state['research'], state['plan'], state.get('audiences', DEFAULT_AUDIENCES))
    result = agent_writer['written']
    state['draft'] = result.content
    print(f"Draft generated")

    return state

def review_node(state:AiContentTeam) -> AiContentTeam:
    print(f"Comparing the source and the written content ....")
    agent_reviewer = Reviewer.reviewer(state['research'], state['draft'], state.get('audiences', DEFAULT_AUDIENCES))
    result = agent_reviewer['reviewer']
    state['review'] = result.content
    print(f"Review feedback: {result}")

    return state


def run_graph() -> StateGraph:

    workflow = StateGraph(AiContentTeam)

    workflow.add_node('plan',planner_node)
    workflow.add_node('research',researcher_node)
    workflow.add_node('draft',writer_node)
    workflow.add_node('review',review_node)

    workflow.set_entry_point('plan')

    workflow.add_edge('plan','research')
    workflow.add_edge('research','draft')
    workflow.add_edge('draft','review')
    workflow.add_edge('review',END)

    return workflow.compile()

mcp_env = os.environ.copy()

# 2. Add your token to the copy
mcp_env["GITHUB_PERSONAL_ACCESS_TOKEN"] = os.getenv("ACCESS_TOKEN", "")
async def run_pipeline(query: str, audiences: list[str] | None = None) -> dict:
     """Execute the complete pipeline"""
     audiences = audiences or DEFAULT_AUDIENCES
     print(f"\n{'='*60}")
     print(f"Starting Pipeline for: {query}")
     print(f"Audience targets: {audiences}")
     print(f"{'='*60}\n")
     print("Starting MCP connection...")
     server_params = StdioServerParameters(
       command="npx",
            args=["-y", "@modelcontextprotocol/server-github"],
            env=mcp_env
    )


     async with stdio_client(server_params) as (read,write):
         print("Transport (stdio) connected")
         async with ClientSession(read,write) as session:
                 print("Session created")
                 await session.initialize()
                 print("MCP initialized successfully")

                 tools = await session.list_tools()
                 print("TOOLS",tools)
               
                 
                 graph = run_graph()
                 result = await graph.ainvoke({
                    'query':query,
                    'plan': '',
                    'research':{},
                    'draft' : '',
                    'review': '',
                    'mcp_session': session,
                    'audiences': audiences
                })
                 print(f"\n{'='*60}")
                 print(f"Pipeline Complete")
                 print(f"{'='*60}\n")
                
                 return result
         

# if __name__ == '__main__':
#       # Test the pipeline
#     response = asyncio.run(run_pipeline(
#         "Explain this project and create audience-aware content for the provided link: https://github.com/Its-Brayan/Research_Assistant.git?",
#         ["developers", "non-developers"]
#     ))
#     print(response)
    
 