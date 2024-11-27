import streamlit as st
import streamlit_authenticator as stauth
from time import sleep

# REGISTRO / LOGIN DO ALUNO para verificação

def ver_preenchidos(campos):  # funcao que ve se cada entrada foi preenchida
    return all(campos.values())


# informações sobre o aluno

foto = st.file_uploader("Foto do aluno:", type=["jpg", "jpeg", "png"])
nome = st.text_input("Nome do aluno:", value="", placeholder="Digite aqui...")
cpf = st.text_input("CPF do aluno:", value="", placeholder="Digite aqui...")
responsavel = st.text_input("Responsável do aluno:", value="", placeholder="Digite aqui...")
id_es = st.text_input("Número ID da escola:", value="", placeholder="Digite aqui...")

if foto is not None:
    st.image(foto, caption="Foto do aluno", width=100)

# id's de quais escolas participam do site

ids_escolas = [
    
    "123",
    "12",
    "1"

]

# Nome ficticio para cada "Aluno" presente nas 3 escolas cadastradas 🤓👍

nomes_alunos_1 = [

    "Luana Almeida",
    "Ruan Gonsalvez",
    "Deftoneron Scrobblers da silva"
    "Maria Raimunda"

]

nomes_alunos_12 = [

    "Sávio Cunha",
    "Bill Amostradinho do Lá Ele",
    "Mulch Lover",
    "Sister of the loam"

]

nomes_alunos_123 = [

    "Kiko Loureiro",
    "Alexi Laiho",
    "Dave Mustaine",
    "Alex Mikhail"

]

# dicionario de cada informação do aluno

campos_aluno = {
    'Nome': nome,
    'CPF': cpf,
    'Responsável': responsavel,
    'Foto': foto,
    'Id da ecola': id_es
}

# com base nas informações do aluno, ele é redirecionado para as paginas corresnondentes das escolas

if st.button("Concluir"):

    if ver_preenchidos(campos_aluno) and id_es in ids_escolas and id_es == "1" and nome in nomes_alunos_1:
        st.success("Concluído com sucesso!")
        sleep(0.5)
        st.switch_page("pages/room1.py")
        if nome not in nomes_alunos_1:
            st.error("Este aluno não pertence a escola cujo ID foi fornecido.") 
    
    elif ver_preenchidos(campos_aluno) and id_es in ids_escolas and id_es == "12" and nome in nomes_alunos_12:
        st.success("Concluído com sucesso!")
        sleep(0.5)
        st.switch_page("pages/room12.py")
        if nome not in nomes_alunos_12:
            st.error("Este aluno não pertence a escola cujo ID foi fornecido.") 

    elif ver_preenchidos(campos_aluno) and id_es in ids_escolas and id_es == "123" and nome in nomes_alunos_123:
        st.success("Concluído com sucesso!")
        sleep(0.5)
        st.switch_page("pages/room123.py")
        if nome not in nomes_alunos_123:
            st.error("Este aluno não pertence a escola cujo ID foi fornecido.") 

    elif id_es not in ids_escolas:
        st.error("Este ID não está cadastrado.")

    else:
        st.error("Por favor, preencha todos os campos.")
