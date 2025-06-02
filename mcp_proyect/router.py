from fastapi import APIRouter,status
from pydantic import BaseModel
from models import chat_con_tools


router = APIRouter()

class New_content(BaseModel):
    consulta: str

@router.post("/chat_model", status_code=status.HTTP_202_ACCEPTED)
async def chat_ia(consulta: New_content):
    print("inicio api...")
    response = await chat_con_tools(consulta.consulta)
    return {"response":response}


