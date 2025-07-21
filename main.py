# ===========================================================================
# Importações
import streamlit as st

from tavily_consult import buscar_destinos
from gemini_consult import recomendar_destino

from datetime import datetime
# ===========================================================================

# Configuração do Streamlit

st.set_page_config(page_title="Consultor de Viagens IA", page_icon="🌍")

st.title("🌍 Consultor de Viagens Inteligente")
st.markdown("Receba recomendações personalizadas com base no clima, data e seus interesses!")

# Formulário

with st.form("form_viagem"):
    
    clima = st.selectbox("Qual clima você prefere?", ["Quente", "Frio", "Moderado"])

    data_viagem = st.date_input("Escolha a data da viagem", value=datetime.today())
    data = data_viagem.strftime("%B").lower()

    preferencias = st.text_input("Você se interessa por: cultura, natureza, gastronomia, praia, etc? (separe por vírgulas)")

    enviar = st.form_submit_button("🔍 Gerar recomendação")

# ===========================================================================

# Processa após clique

if enviar:
    preferencias_lista = [p.strip().lower() for p in preferencias.split(',')]
    cliente = {
        "clima": clima,
        "data": data,
        "preferencias": preferencias_lista
    }

    with st.spinner("🔍 Pesquisando destinos na web..."):
        resumo_tavily = buscar_destinos(clima, preferencias_lista)

    st.success("✅ Resumo encontrado!")

    with st.spinner("🧠 Gerando recomendação personalizada com IA..."):
        resposta = recomendar_destino(cliente, resumo_tavily)

    st.markdown("---")
    st.subheader("📋 Resultado da Recomendação:")
    st.markdown(resposta)
