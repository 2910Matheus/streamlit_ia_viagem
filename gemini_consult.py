import google.generativeai as genai
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_KEY_GEMINI = os.getenv("API_KEY_GEMINI", st.secrets.get("API_KEY_GEMINI"))
genai.configure(api_key=API_KEY_GEMINI)

def recomendar_destino(dados_cliente, resumo_tavily):
    prompt = f"""
Usuário deseja viajar em {dados_cliente['data']} com clima {dados_cliente['clima']}, e gosta de {', '.join(dados_cliente['preferencias'])}.

Com base nas informações da web:
{resumo_tavily}

Sugira 3 cidades no Brasil que se alinhem com esse perfil.
Para cada uma:
- Descreva os atrativos principais
- Justifique por que se encaixa com o perfil

Depois:
- Compare as 3 opções
- Escolha a melhor cidade e explique os critérios da escolha.
"""
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt)
    return response.candidates[0].content.parts[0].text
