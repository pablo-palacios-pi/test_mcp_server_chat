# import asyncio
# import sys

# if sys.platform == "win32":
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi import FastAPI
from router import router

app = FastAPI()
app.include_router(router, prefix="/api", tags=["Endpoints"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8200, reload=True)


# uvicorn main:app --reload 
