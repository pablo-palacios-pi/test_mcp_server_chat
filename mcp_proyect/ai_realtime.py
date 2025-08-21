
from tabnanny import verbose
from mcp import ClientSession
from mcp.client.sse import sse_client
from mcp.client.streamable_http import streamablehttp_client

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
        
    async def mcp_process(self):
        consulta = "necesito que me brindes los nombres que estan almacenados en la lista"
        
        try:
            # Connect to a streamable HTTP server
            async with streamablehttp_client(URL_LOCAL_MCP_SERVER_STREAM) as (
                read_stream,
                write_stream,
                _,
            ):
                # Create a session using the client streams
                async with ClientSession(read_stream, write_stream) as session:
                    await session.initialize()
                    # List available tools
                    tools = await session.list_tools()
                    tools_list = await load_mcp_tools(session)

            
                    if not tools:
                        logging.error("Tools not charge!!")

                    llm = self.openai.get_llm()

                    prompt = self.openai.load_promptSystem()

                    agent = create_react_agent(llm, tools_list, prompt=prompt)

                    message = {
                            "messages": [
                                {"role": "user", "content": consulta}
                            ]
                    }
                    

                    async for token in agent.astream(
                        input=message,
                        stream_mode="messages"
                    ):  
                        yield token[0].content
                        # print(f"token: {chunk[0].content}")
                        # print("\n")

                        
                    
        except Exception as e:
            logging.error(f"Error conection MPC Server: {e}")
            traceback.print_exc()