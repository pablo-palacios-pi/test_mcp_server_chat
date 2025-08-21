from ast import Await
from http import client
from fastapi import FastAPI
from ai_realtime import MCP_Client
import uvicorn
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    mcp_client = MCP_Client()
    await mcp_client.conexion_sse()
    
@app.get("/get_mcp")
async def look_mcp_updates():
    mcp_client = MCP_Client()
    async def token_generator():
        async for token in mcp_client.mcp_process():
            yield f"{token}\n"

    return StreamingResponse(token_generator(), media_type="text/plain")


if __name__=="__main__":
    uvicorn.run(app=app, port=8002)