from fastapi import FastAPI
from langgraph.prebuilt import create_react_agent
from llms_agents.models import llm
from prompts.views import open_prompt


app = FastAPI()


math_agent_ = create_react_agent(
    model=llm,
    tools=[],
    prompt=(
        open_prompt("agents_indv/math_prompt.md")
    ),
    name="math_agent",
)



