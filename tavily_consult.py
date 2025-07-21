from tavily import TavilyClient
import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", st.secrets.get("TAVILY_API_KEY"))
client = TavilyClient(api_key=TAVILY_API_KEY)


def buscar_destinos(clima, preferencias):

    prompt = f"Quais são os melhores destinos no Brasil com clima {clima} para quem gosta de {', '.join(preferencias)}?"
    resposta = client.search(query=prompt, include_answer=True)
    return resposta['answer']


