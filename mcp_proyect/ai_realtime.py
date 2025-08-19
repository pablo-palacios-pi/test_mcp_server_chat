
from mcp import ClientSession
from mcp.client.sse import sse_client
import logging
import aiohttp
from services.service_openai import OpenAiService
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
import traceback 
import os


from core.config import (
    URL_LOCAL_MCP_SERVER_STREAM
)


class MCP_Client():
    def __init__(self):
        self.openai = OpenAiService()

    async def conexion_sse(self):
        try:
            async with aiohttp.ClientSession() as client:
                async with client.get(url=URL_LOCAL_MCP_SERVER_STREAM,headers={"Accept": "text/event-stream"},allow_redirects=True) as client_sse: 
                    if client_sse.status == 200:
                            print(f"MCP_SSE_CONEXION OK: {client_sse.status}")
                    else:
                        raise Exception(f"MCP_SSE_STATUS: {client_sse.status}")
        except Exception as e:
            raise Exception(f"MCP SERVER NOT UP: {e}")  
        
    async def mcp_process(self, consulta: str):
        
        try:
            async with sse_client(url=URL_LOCAL_MCP_SERVER_STREAM) as (in_stream, out_stream):
                async with ClientSession(in_stream, out_stream) as session:
                    await session.initialize()

                    tools = await load_mcp_tools(session)

                    print(F"TOOLS: {tools}")
                    
                    if not tools:
                        logging.error("Tools not charge!!")

                    llm = self.openai.get_llm()

                    prompt = self.openai.load_promptSystem()

                    agent = create_react_agent(llm, tools, prompt=prompt)

                    message = {
                            "messages": [
                                {"role": "user", "content": consulta}
                            ]
                    }
                    return await agent.ainvoke(message)
                    
        except Exception as e:
            logging.error(f"Error conection MPC Server: {e}")
            traceback.print_exc()