from mcp import ClientSession
from mcp.client.sse import sse_client
import logging


class MCP_Client_SEE:
    def __init__(self):
        self.session = None

    async def connect(self, sse_url: str):
        try:
            async with sse_client(url=sse_url) as (in_stream, out_stream):
                async with ClientSession(in_stream, out_stream) as session:
                    self.session = session
                    await self.session.initialize()
                    logging.info("Initialize MPC Server")
        except Exception as e:
            logging.error(f"Error conection MPC Server: {e}")

    async def gets_tools(self):
        tools_aviables = await self.session.list_tools()
        return tools_aviables






