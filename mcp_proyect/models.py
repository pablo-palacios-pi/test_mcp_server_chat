from dotenv import load_dotenv
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai.chat_models import AzureChatOpenAI

load_dotenv()


# instanciamos el server y le pasamos donde estan alojadas las tools 
server_params = StdioServerParameters(
    command="python",
    args=["utils_mcp.py"]
)

# instanciamos un llm 
llm = AzureChatOpenAI(
    api_key=os.getenv("API_KEY"),
    api_version=os.getenv("API_VERSION"),
    azure_endpoint=os.getenv("ENDPOINT"),
    azure_deployment=os.getenv("DEPLOYMENT")
)

# genere una clase que pueda generar solamente una vez el la coneccion con ClientSession.
class MCP_Server:
    def __init__(self):
        self.session: ClientSession = None

    async def connect(self, consulta: str):
        async with stdio_client(server_params) as (read, write):  # linea que reccorre el file de las tools del server.
            async with ClientSession(read, write) as session:    # Iniciamos la session del cliente de mcp para poder comunicarse con las tools.
                self.session = session
                await self.session.initialize()
                tools = await load_mcp_tools(self.session)  # funcion que carga todas las tools disponibles 
                agent = create_react_agent(llm, tools)   # Aca, mediante esta funcion, instanciamos una suerte de agente (puede ser otro agente sin drama) donde concete el llm con las tools
                                                        # Para tener en cuenta, el server de MCP, solo organiza y ofrece las tools disponibles, luego puede ser un agente o un llm directo que las instancie y sepa que hacer con cada una
                message = {"messages":[{"role":"user","content":consulta}]}
                return await agent.ainvoke(message)  # aca invoca la respuesta del llm 


# funcion que conecta la consulta del cliente con el server
async def chat_con_tools(consulta: str):
    print("inicio: chat_con_tools")
    session = MCP_Server()
    response = await session.connect(consulta=consulta)
    print(F"RESPONSE: {response}")    
    return response["messages"][-1].content