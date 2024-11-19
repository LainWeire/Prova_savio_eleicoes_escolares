import streamlit as st
import streamlit_authenticator as stauth
from time import sleep

# REGISTRO / LOGIN DO ALUNO para verificação

def ver_preenchidos(campos):  # funcao que ve se cada entrada foi preenchida
    return all(campos.values())




foto = st.file_uploader("Foto do aluno:", type=["jpg", "jpeg", "png"])
nome = st.text_input("Nome do aluno:", value="", placeholder="Digite aqui...")
cpf = st.text_input("CPF do aluno:", value="", placeholder="Digite aqui...")
responsavel = st.text_input("Responsável do aluno:", value="", placeholder="Digite aqui...")
id_es = st.text_input("Número ID da escola:", value="", placeholder="Digite aqui...")

if foto is not None:
    st.image(foto, caption="Foto do aluno", width=100)

ids_escolas = [
    "123456",
    "12345",
    "1234",
    "123",
    "12",
    "1"
]

campos_aluno = {
    'Nome': nome,
    'CPF': cpf,
    'Responsável': responsavel,
    'Foto': foto,
    'Id da ecola': id_es
}



if st.button("Concluir"):

    if ver_preenchidos(campos_aluno) and id_es in ids_escolas:
        st.success("Concluído com sucesso!")
        sleep(0.5)
        st.switch_page("pages/home_aluno.py")
    
    elif id_es not in ids_escolas:
        st.error("Este ID não está cadastrado.")


    else:
        st.error("Por favor, preencha todos os campos.")
    

