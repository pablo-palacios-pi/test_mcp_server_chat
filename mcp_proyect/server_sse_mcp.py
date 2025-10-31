
import logging
from mcp.server.fastmcp import FastMCP

class MCP_SERVER_SEE:
    def __init__(self, name_server: str):
        self.mcp = FastMCP(name=name_server, sse_path="/mcp_sse", stateless_http=True)

        list_name = []
       
        @self.mcp.tool(name="subtract", description="It is used to subtract two integers together.")
        async def subtract(a: int, b: int): 
            return a - b
    
        @self.mcp.tool(name="add", description="It is used to add two integers together.")
        async def add(a: int, b: int): 
            return a + b

        @self.mcp.tool(name="multiply", description="It is used to multiply two integers together.")
        async def multiply(a: int, b: int):
            return a*b

        @self.mcp.tool(name="divide", description="It is used to divide two integers.")
        async def divide(a: int, b: int):
            return a/b

        @self.mcp.tool(name="get_names_list", description="It retrieves all the names that are stored in the list.")
        async def get_names_list():
            if not list_name:
                return "Lista de nombres completamente vacia. Agrega nombres."
            else:
                return list_name
            
        @self.mcp.tool(name="add_names_list", description="Add one or many names in list.")
        async def add_names_list(names: str):
            list_name.append(names)
            return f"Se agrego con exito el nombre: {names}"
        
        @self.mcp.tool(name="remove_name", description="Remove one name from the list if it exists.")
        async def remove_name(name: str):
                if name in list_name:
                    list_name.remove(name)
                    return f"Se eliminó el nombre: {name}"
                else:
                    return f"El nombre '{name}' no se encuentra en la lista."
                
        import random

        @self.mcp.tool(name="pick_random_name", description="Selects a random name from the list.")
        async def pick_random_name():
            if not list_name:
                return "La lista está vacía, agrega nombres primero."
            return f"El nombre elegido al azar es: {random.choice(list_name)}"
        

        @self.mcp.tool(name="write_text_file", description="Writes text content into a local file.")
        async def write_text_file(filename: str, content: str):
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            return f"Archivo '{filename}' creado y guardado exitosamente."
        
        @self.mcp.tool(name="read_text_file", description="Reads the content of a local text file.")
        async def read_text_file(filename: str):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()
                return content
            except FileNotFoundError:
                return f"El archivo '{filename}' no existe."

        
        @self.mcp.resource(uri="config://settings", name="application_settings", description="send infomation to specific settings in json")
        def get_settings() -> str:
            """Get application settings."""

            return """{
                "theme": "dark",
                "language": "en",
                "debug": false
                }"""



    def run(self):
        self.mcp.run(transport="sse")


if __name__=="__main__":
    server = MCP_SERVER_SEE("SERVER SSE")
    logging.info("MCP SERVER UP SSE!!")
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