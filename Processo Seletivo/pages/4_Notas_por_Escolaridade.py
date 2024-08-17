import streamlit as st
from main import constroiGraficoLinhas

def criar_dicionario_nota(microdados, categorias, materias, questionario):
    dicionario = {}
    for categoria in categorias:
        dadosFiltrados = microdados[microdados[questionario] == categoria]
        medias_notas = dadosFiltrados[materias].mean()
        dicionario[categoria] = medias_notas.to_dict()
    return dicionario

materias = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']

microdadosEnem = st.session_state['data']


dicionario_pai = criar_dicionario_nota(microdadosEnem,["A", "B", "C", "D", "E", "F", "G", "H"], materias, "Q001")
dicionario_mae = criar_dicionario_nota(microdadosEnem,["A", "B", "C", "D", "E", "F", "G", "H"], materias, "Q002")

fig_nota_escolaridade_pai, ax_pai = constroiGraficoLinhas(dicionario_pai)
fig_nota_escolaridade_mae, ax_mae = constroiGraficoLinhas(dicionario_mae)



dicionario_escolaridade = {
    "A": "Nunca estudou.",
    "B": "Não completou a 4ª série/5º ano do Ensino Fundamental.",
    "C": "Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.",
    "D": "Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.",
    "E": "Completou o Ensino Médio, mas não completou a Faculdade.",
    "F": "Completou a Faculdade, mas não completou a Pós-graduação.",
    "G": "Completou a Pós-graduação.",
    "H": "Não sei."
}

st.write("### Escolaridade dos Pais X Notas - Pai")
i = 0
categorias = ["A","B", "C", "D", "E", "F", "G", "H"]
for descricao in dicionario_escolaridade.values():
    st.write(f"{categorias[i]}: {descricao}")
    i+=1
st.pyplot(fig_nota_escolaridade_pai)
st.write("### Escolaridade dos Pais X Notas - Mãe")
i = 0
categorias = ["A","B", "C", "D", "E", "F", "G", "H"]
for descricao in dicionario_escolaridade.values():
    st.write(f"{categorias[i]}: {descricao}")
    i+=1
st.pyplot(fig_nota_escolaridade_mae)