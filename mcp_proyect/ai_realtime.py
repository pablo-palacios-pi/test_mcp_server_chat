from services.client_mcp import MCP_Client_SEE
from services.service_openai import OpenAiService

class Server_realtime():
    def __init__(self):
        self.openai = OpenAiService()
        self.mcp = MCP_Client_SEE()

    async def mcp_process(self):
        client = await self.mcp.connect(sse_url="http://0.0.0.0:8000/sse")
        tools = await self.mcp.gets_tools()
        print(f"TOOLS: {tools}")