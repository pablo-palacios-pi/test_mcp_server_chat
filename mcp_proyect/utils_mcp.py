from mcp.server.fastmcp import FastMCP

mcp = FastMCP("functions")

@mcp.tool(name="sumar", description="Sirve para sumar dos enteros entre si")
async def sumar(a: int, b: int): 
    return a + b

@mcp.tool(name="multiplicar", description="Sirve para multiplicar dos enteros entre si")
async def multiplicar(a: int, b: int):
    return a*b

@mcp.tool(name="dividir", description="Sirve para dividir dos enteros entre si")
async def dividir(a: int, b: int):
    return a/b

@mcp.tool(name="traer_nombres", description="Trae todos los nombres que estan almacenados en la lista")
async def traer_nombres():
    return ["pablo","juan","martin"]


# Esta línea ejecuta el servidor MCP en modo stdio, que es el transporte necesario para integrarlo con LangChain o LangGraph (por ejemplo, con create_react_agent()).


if __name__ =="__main__":
    mcp.run(transport="stdio")