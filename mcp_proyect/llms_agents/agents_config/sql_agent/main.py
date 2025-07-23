from fastapi import FastAPI
from langgraph.prebuilt import create_react_agent
from models import llm
from prompts.views import open_prompt


app = FastAPI()


sql_agent_= create_react_agent(
    model=llm,
    tools=[],
    prompt=(
        open_prompt("agents_indv/sql_prompt.md")
    ),
    name="sql_agent",
)


@app.post("/agent_sql")
async def run_sql_agent():
    result = await sql_agent_.astream(input.prompt)
    return {"response": result}





