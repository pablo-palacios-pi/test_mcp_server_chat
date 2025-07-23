# SERVER MCP -- ACA INSTANCIAMOS LAS TOOLS DISPONIBLES PARA NUESTRO AGENTE O LLM. 

from mcp.server.fastmcp import FastMCP
from surpervisor_agent.super_agent_mcp import supervisor

mcp = FastMCP("functions")

@mcp.tool(name="agente_primero", description="Grupo de agentes que resuleven consultas del usuario.")
async def agente_primero(consulta: str): 
    message = {"messages": [{"role": "user", "content": consulta}]}
    result = await supervisor.ainvoke(message)
    return result
    

# Esta línea ejecuta el servidor MCP en modo stdio, que es el transporte necesario para integrarlo con LangChain o LangGraph (por ejemplo, con create_react_agent()).
if __name__ =="__main__":
    mcp.run(transport="stdio")