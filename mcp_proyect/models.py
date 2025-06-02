from dotenv import load_dotenv
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai.chat_models import AzureChatOpenAI

load_dotenv()

server_params = StdioServerParameters(
    command="python",
    args=["utils_mcp.py"]
)

llm = AzureChatOpenAI(
    api_key=os.getenv("API_KEY"),
    api_version=os.getenv("API_VERSION"),
    azure_endpoint=os.getenv("ENDPOINT"),
    azure_deployment=os.getenv("DEPLOYMENT")
)

class MCP_Server:
    def __init__(self):
        self.session: ClientSession = None

    async def connect(self, consulta: str):
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                self.session = session
                await self.session.initialize()
                tools = await load_mcp_tools(self.session)
                agent = create_react_agent(llm, tools)
                message = {"messages":[{"role":"user","content":consulta}]}
                return await agent.ainvoke(message)



async def chat_con_tools(consulta: str):
    print("inicio: chat_con_tools")
    session = MCP_Server()
    response = await session.connect(consulta=consulta)
    print(F"RESPONSE: {response}")    
    return response["messages"][-1].content