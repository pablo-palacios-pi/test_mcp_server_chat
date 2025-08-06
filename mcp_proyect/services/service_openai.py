from openai import AzureOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
import os


from core.config import (
    ROOT_DIR_PROMPT,
    PROMPT_FILE_TOOLS,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_MODEL_VERSION,
    AZURE_OPENAI_DEPLOYMENT_NAME

)

class OpenAiService:
    def __init__(self):
        try:
            self.llm = AzureChatOpenAI(  
                openai_api_version=AZURE_OPENAI_MODEL_VERSION,  
                azure_endpoint=AZURE_OPENAI_ENDPOINT,  
                api_key=AZURE_OPENAI_API_KEY,  
                deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,  
                temperature=0.5,
                top_p=1.0
)  
        except Exception as ex:
            raise Exception(f"Error al inicializar AzureOpenAI: {str(ex)}", 'OAI-001', 500)
        
    def get_llm(self):
        return self.llm
        
    def load_promptSystem(self) ->  str:
        try:
            prompt_path = os.path.join(ROOT_DIR_PROMPT, PROMPT_FILE_TOOLS)
            with open(prompt_path, mode="r", encoding="utf-8") as file:
                prompt = file.read()
                return prompt
        except FileNotFoundError:
            raise FileNotFoundError(f"Archivo de prompt no encontrado en la ruta: {prompt_path}", 'LPS-001', 500)
        except Exception as e:
            raise Exception(f'Error inesperado leer archivo prompt {str(e)}', 'LPS-002', 500)
        







        
    # def chat_model_gpt_4o_mini(self,tools,consulta: str):
    #     try:
    #         prompt_template = PromptTemplate(
    #             input_variables=["tools"],
    #             template= self.load_promptSystem(prompt_file_name=PROMPT_FILE_TOOLS)
    #         )
            
    #         final_prompt = prompt_template.format(
    #             tools=tools
    #         )
        
    #         messages =[{"role":"system", "content":final_prompt},
    #                    {"role":"system", "content":consulta}]

    #         response = self.client.chat.completions.create(
    #             model=AZURE_OPENAI_MODEL_4o_MINI,
    #             messages=messages,
    #             temperature=0.5,
    #             top_p=1.0
    #         )
        
    #         return response.choices[0].message.content
    #     except Exception as e:
    #         raise Exception(f'Error inesperado al cargar archivos {str(e)}', 'MRP-000', 500)
        

