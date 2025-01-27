from pydantic_ai import Agent, RunContext
from dotenv import load_dotenv
from tavily import TavilyClient, AsyncTavilyClient
import logfire
import os
import asyncio

logfire.configure()

load_dotenv()

search_agent = Agent(  
    'openai:gpt-4',
    #deps_type=int,
    result_type=str,
    system_prompt=(
        'Use the talivy_tool function to find the latest information'
    ),
)
@search_agent.tool
async def talivy_tool(ctx: RunContext, query:str):  
    """useful to find the latest information from internet"""
    tavily_client = AsyncTavilyClient(api_key=os.environ["TAVILY_API_KEY"])
    response = await tavily_client.search(query, max_results=3)
    return response['results']

# user_prompt = input("Provide your query: ") # <-- Uncomment this line to run this app directly
## Run Asynchronous - 
# result = search_agent.run_sync(user_prompt)

## standard way of running it:
async def run_agent():
    result = await search_agent.run(user_prompt)
    # print("Agent Result:", result)
    return result

# Execute the async function directly
# result=asyncio.run(run_agent()) # <-- Uncomment this line to run this app directly

# print(result.data) # <-- Uncomment this line to run this app directly
