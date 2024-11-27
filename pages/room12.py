import streamlit as st
import matplotlib.pyplot as plt
import random
from io import BytesIO
import time
import webbrowser

# Configuração inicial da página

st.set_page_config(page_title="Sistema de Votação com Gráfico", layout="centered")

# Títulos e descrição
st.title("🗳️ Sistema de Votação")
st.write("Vote no seu candidato preferido! Cada usuário pode votar apenas uma vez.")

# Variáveis de estado para armazenar votos
if "votos_candidato1" not in st.session_state:
    st.session_state.votos_candidato1 = 0

if "votos_candidato2" not in st.session_state:
    st.session_state.votos_candidato2 = 0

if "ja_votou" not in st.session_state:
    st.session_state.ja_votou = False

# Verifica se o usuário já votou
if st.session_state.ja_votou:
    st.warning("Você já votou! Obrigado por participar.")
else:
    # Botões de votação
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Votar no Candidato 1"):  
            st.session_state.votos_candidato1 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 1!")
 
    with col2:
        if st.button("Votar no Candidato 2"):
            st.session_state.votos_candidato2 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 2!")


col3, col4 = st.columns(2)

with col3:
    if st.button("Discurso do candidato 1:"):
        webbrowser.open("https://drive.google.com/file/d/1kQLq79oVjbr01VncLILsOYeNoUbamg9Z/view")
with col4:
        if st.button("Discurso do candidato 2:"):
            webbrowser.open("https://drive.google.com/file/d/1qmZaOtp8vKijO7M4KoV5A4kBMBEaNaf4/view")


# Exibir os totais de votos
st.markdown("---")
st.markdown(f"""
### Totais de votos:
- **Candidato 1:** {st.session_state.votos_candidato1}
- **Candidato 2:** {st.session_state.votos_candidato2}
""")

# Gráfico de votação
st.markdown("---")
st.title("📊 Gráfico de Votação em Tempo Real")

# Dados iniciais
candidatos = ["Candidato 1", "Candidato 2"]
votos = [
    st.session_state.votos_candidato1,
    st.session_state.votos_candidato2,
]

# Gerar gráfico como imagem
def plotar_grafico():
    fig, ax = plt.subplots()
    ax.bar(candidatos, votos, color=['blue', 'green'])
    ax.set_title("Votação - Quem está ganhando")
    ax.set_xlabel("Candidatos")
    ax.set_ylabel("Número de votos")
    # Converter gráfico para imagem
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Botão para exibir gráfico
if st.button("Atualizar Gráfico"):
    # Atualizar votos no gráfico
    votos = [
        st.session_state.votos_candidato1,
        st.session_state.votos_candidato2,
    ]
    grafico = plotar_grafico()
    st.image(grafico, caption="Gráfico de Votação", use_column_width=True)
