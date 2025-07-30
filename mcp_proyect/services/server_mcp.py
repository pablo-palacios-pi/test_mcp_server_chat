from mcp import ClientSession
from mcp.client.sse import sse_client
import logging
from mcp.server.fastmcp import FastMCP
from mcp.server.sse import SseServerTransport


class MCP_Server_SEE:
    def __init__(self, name_server: str):
        self.mcp = FastMCP(name=name_server)
        self.transport = SseServerTransport("/see")
        self.register_tools()

    def register_tools(self):
        @self.mcp.tool(name="sumar", description="Sirve para sumar dos enteros entre si")
        async def sumar(a: int, b: int): 
            return a + b

        @self.mcp.tool(name="multiplicar", description="Sirve para multiplicar dos enteros entre si")
        async def multiplicar(a: int, b: int):
            return a*b

        @self.mcp.tool(name="dividir", description="Sirve para dividir dos enteros entre si")
        async def dividir(a: int, b: int):
            return a/b

        @self.mcp.tool(name="traer_nombres", description="Trae todos los nombres que estan almacenados en la lista")
        async def traer_nombres():
            return ["pablo","juan","martin"]

    async def handle_sse(self, request):
    # Prepare bidirectional streams over SSE
        async with self.transport.connect_sse(
            request.scope,
            request.receive,
            request._send
        ) as (in_stream, out_stream):
            # Run the MCP server: read JSON-RPC from in_stream, write replies to out_stream
            await self.mcp._mcp_server.run(
                in_stream,
                out_stream,
                self.mcp._mcp_server.create_initialization_options()
            )

    def run(self):
        self.mcp.run(transport="sse")


if __name__=="__main__":
    server = MCP_Server_SEE("server_sse")
    logging.info("MCP SERVER UP!!")
    server.run()
    