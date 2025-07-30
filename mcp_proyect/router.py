from fastapi import APIRouter,status
from pydantic import BaseModel
#from test_mcp_server_chat.mcp_proyect.mcp_clients import chat_con_tools
from ai_realtime import Server_realtime

router = APIRouter()

class New_content(BaseModel):
    consulta: str

@router.on_event("startup")
async def startup():
    server = Server_realtime()
    await server.mcp_process()


# @router.post("/chat_model", status_code=status.HTTP_202_ACCEPTED)
# async def chat_ia(consulta: New_content):
#     print("inicio api...")t   
#     response = await chat_con_tools(consulta.consulta)
#     return {"response":response}


