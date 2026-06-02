from tavily import TavilyClient
from dotenv import load_dotenv
from groq import AsyncGroq
import os
import _asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from urllib.parse import urlparse
import re
load_dotenv()

client = TavilyClient(
    api_key=os.getenv('TAVILY_API_KEY')
)

def extract_github_url(text: str):
   match = re.search(r"github\.com/([\w\-]+)/([\w\-\.]+)", text.strip())
   if not match:
      return None, None
   
   owner = match.group(1)
   repo = match.group(2)
   if repo.endswith('.git'):
      repo = repo[:-4]
   return{
      "owner":owner,
      "repo":repo
   }
