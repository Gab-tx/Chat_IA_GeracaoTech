from google import genai
from google.genai import types
from PIL import Image
import time
from dotenv import load_dotenv
import os
import json

load_dotenv()
api_key = os.getenv("API_KEY")

with open('config.json','r',encoding='utf-8') as f:
    dados_instrucao = json.load(f)

system_instruction = json.dumps(dados_instrucao,indent=2,ensure_ascii=False)

client = genai.Client(api_key=api_key)
chat_session = client.chats.create(
    model='gemini-2.5-flash-lite',
    config={
        "system_instruction": system_instruction,
        "temperature": 0.5,
        "top_p": 0.5,
        "top_k": 20,
        "max_output_tokens": 300
    }
)




def enviar_pergunta(texto):
    response = chat_session.send_message(texto)
    print(response.text)

menu = """
=================================================
        SHERLOCK • ASSISTENTE PESSOAL
=================================================
 Precisão, lógica e respostas confiáveis
-------------------------------------------------
"""

def main():
    print(menu)

    while True:
        prompt = input("Digite seu prompt: ")
        enviar_pergunta(prompt)
        time.sleep(2)
        if prompt == "sair":
            break

if __name__ == "__main__":
    main()