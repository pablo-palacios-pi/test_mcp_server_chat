import os
from dotenv import load_dotenv

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
ENV_FILE = os.path.join(ROOT_DIR, ".env")

load_dotenv(dotenv_path=ENV_FILE)

# Settings global
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_MODEL_VERSION = os.getenv("AZURE_OPENAI_MODEL_VERSION")
AZURE_OPENAI_MODEL_4o_MINI = os.getenv("AZURE_OPENAI_MODEL_4o_MINI")
PROMPT_FILE_TOOLS = os.getenv("PROMPT_FILE_TOOLS")
ROOT_DIR_PROMPT = os.path.join(ROOT_DIR, 'mcp_proyect', 'prompts')
AZURE_OPENAI_DEPLOYMENT_NAME= os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
URL_LOCAL_MCP_SERVER_STREAM = os.getenv("URL_LOCAL_MCP_SERVER_STREAM")