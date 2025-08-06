from fastapi import APIRouter,status
from httpx import HTTPError
from pydantic import BaseModel
#from test_mcp_server_chat.mcp_proyect.mcp_clients import chat_con_tools
from ai_realtime import MCP_Client

router = APIRouter()

class New_content(BaseModel):
    consulta: str

server = MCP_Client()

@router.on_event("startup")
async def startup():
    await server.conexion_sse()

    

@router.post("/chat_llm_tools", status_code=status.HTTP_202_ACCEPTED)
async def chat_ia(consulta: New_content):
    try:
        response = await server.mcp_process(consulta.consulta)
        return {"response":response}
    except Exception as e:
        raise HTTPError("FALLO chat_llm_tools")


