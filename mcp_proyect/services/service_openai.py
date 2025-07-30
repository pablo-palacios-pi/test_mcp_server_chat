from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

ROOT_DIR_PROMPT = os.getenv("ROOT_DIR_PROMPT")
PROMPT_FILE = os.getenv("PROMPT_FILE")
AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")

class OpenAiService:
    def __init__(self):
        try:
            self.client = AzureOpenAI(
                api_version=os.getenv("API_VERSION"),
                azure_endpoint=os.getenv("ENDPOINT"),
                api_key=os.getenv("API_KEY")
            )
        except Exception as ex:
            raise Exception(f"Error al inicializar AzureOpenAI: {str(ex)}", 'OAI-001', 500)
        
    def load_promptSystem(self, prompt_file_name: str) ->  str:
        try:
            prompt_path = os.path.join(ROOT_DIR_PROMPT, prompt_file_name)
            with open(prompt_path, mode="r", encoding="utf-8") as file:
                prompt = file.read()
                return prompt
        except FileNotFoundError:
            raise FileNotFoundError(f"Archivo de prompt no encontrado en la ruta: {prompt_path}", 'LPS-001', 500)
        except Exception as e:
            raise Exception(f'Error inesperado leer archivo prompt {str(e)}', 'LPS-002', 500)
        
    def chat_model_gpt_4o(self,consulta: str):
        try:
            messages =[{"role":"system", "content":self.load_promptSystem(PROMPT_FILE)},
                       {"role":"system", "content":consulta}]

            response = self.client.chat.completions.create(
                model=AZURE_OPENAI_MODEL,
                messages=messages,
                temperature=0.5
            )

            respuesta = response.choices[0].message.content

            return respuesta
        except Exception as e:
            raise Exception(f'Error inesperado al cargar archivos {str(e)}', 'MRP-000', 500)