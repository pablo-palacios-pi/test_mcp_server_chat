
import logging
from mcp.server.fastmcp import FastMCP
#from mcp.server.streaming_asgi_transport import StreamingASGITransport

class MCP_Server_SEE:
    def __init__(self, name_server: str):
        self.mcp = FastMCP(name=name_server, host="0.0.0.0", port=8000, streamable_http_path="/mcp",stateless_http=True)
       
        
    
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



    def run(self):
        self.mcp.run(transport="streamable-http")


if __name__=="__main__":
    server = MCP_Server_SEE("streamable-http")
    logging.info("MCP SERVER UP!!")
    server.run()
    

































# from mcp.server import MCPServer  
# from mcp.transport.streaming import StreamingServerTransport  
  
# # Tus herramientas (tools)  
# async def sumar(a: int, b: int) -> int:  
#     return a + b  
  
# async def multiplicar(a: int, b: int) -> int:  
#     return a * b  
  
# async def dividir(a: int, b: int) -> float:  
#     return a / b  
  
# async def traer_nombres() -> list:  
#     return ["pablo", "juan", "martin"]  
  
# # Creás el server y le pasás las tools y el transport streaming SSE  
# server = MCPServer(  
#     tools=[  
#         MCPServer.tool("sumar", sumar, description="Suma dos enteros"),  
#         MCPServer.tool("multiplicar", multiplicar, description="Multiplica dos enteros"),  
#         MCPServer.tool("dividir", dividir, description="Divide dos enteros"),  
#         MCPServer.tool("traer_nombres", traer_nombres, description="Trae todos los nombres de la lista"),  
#     ],  
#     transport=StreamingServerTransport(path="/stream"), # esto expone el SSE en /stream  
# )  
  
# if __name__ == "__main__":  
#     import logging  
#     logging.info("MCP SERVER UP!!")  
#     server.run()  