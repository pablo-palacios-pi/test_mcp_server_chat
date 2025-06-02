# import asyncio
# import sys

# if sys.platform == "win32":
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi import FastAPI
from router import router

# Creamos la app antes de ejecutar uvicorn
app = FastAPI()
app.include_router(router, prefix="/api", tags=["Endpoints"])

# Solo se ejecuta si se corre este archivo directamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



# uvicorn main:app --reload 
