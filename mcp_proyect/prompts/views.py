import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def open_prompt(file_path: str):
    doc_dir = os.path.normpath(os.path.join(current_dir,file_path))
    with open(file=doc_dir, mode="r", encoding="utf-8") as file:
        prompt = file.read()
        return prompt
    

