from langgraph_supervisor import create_supervisor
#from langchain.chat_models import init_chat_model
from models import llm
#from agents_mini import summary_agent,sql_agent,math_agent,userList_manager_agent
from prompts.views import open_prompt
from models import HttpAgent


math_agent = HttpAgent(name="math_agent", endpoint="http://localhost:8001/agent_math")
sql_agent = HttpAgent(name="sql_agent", endpoint="http://localhost:8001/agent_sql")

supervisor = create_supervisor(
        model=llm,
        agents=[sql_agent,math_agent],
        prompt=(
            open_prompt("agents_indv/supervisor_prompt.md")
        ),
        add_handoff_back_messages=True,
        output_mode="full_history",
    ).compile()