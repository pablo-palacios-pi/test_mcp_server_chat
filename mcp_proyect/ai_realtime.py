# from services.client_mcp import MCP_Client_SEE
from httpx import get, request
from mcp import ClientSession
from mcp.client.sse import sse_client
import logging
import json
import aiohttp
import requests
from services.service_openai import OpenAiService
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
import traceback 

from langchain_openai import AzureChatOpenAI
import os


from core.config import (
    ROOT_DIR_PROMPT,
    PROMPT_FILE_TOOLS,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_MODEL_VERSION,
    AZURE_OPENAI_MODEL_4o_MINI,
    AZURE_OPENAI_DEPLOYMENT_NAME,
    URL_LOCAL_MCP_SERVER_SSE
)


# llm = AzureChatOpenAI(  
#                 openai_api_version=AZURE_OPENAI_MODEL_VERSION,  
#                 azure_endpoint=AZURE_OPENAI_ENDPOINT,  
#                 api_key=AZURE_OPENAI_API_KEY,  
#                 deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,  
#                 temperature=0.5,
#                 top_p=1.0
# )

class MCP_Client():
    def __init__(self):
        self.openai = OpenAiService()
        # self.mcp = MCP_Client_SEE()

    async def conexion_sse(self):
        try:
            async with aiohttp.ClientSession() as client:
                async with client.get(url=URL_LOCAL_MCP_SERVER_SSE) as client_sse: 
                    if client_sse.status == 200:
                            print(f"MCP_SSE_CONEXION OK: {client_sse.status}")
                    else:
                        raise Exception(f"MCP_SSE_STATUS: {client_sse.status}")
        except Exception as e:
            raise Exception(f"MCP SERVER NOT UP: {e}")  
        
    async def mcp_process(self, consulta: str):
        
        try:
            async with sse_client(url=URL_LOCAL_MCP_SERVER_SSE) as (in_stream, out_stream):
                async with ClientSession(in_stream, out_stream) as session:
                    await session.initialize()
                    tools = await load_mcp_tools(session)

                    print(F"TOOLS: {tools}")
                    
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
    













# llm_response = self.openai.chat_model_gpt_4o_mini(tools=tools,consulta=consulta)
                    
                    # tool_call = json.loads(llm_response)
                                
                    # result = await session.call_tool(tool_call["tool"], arguments=tool_call["arguments"])

                    #logging.info("Initialize MPC Server")