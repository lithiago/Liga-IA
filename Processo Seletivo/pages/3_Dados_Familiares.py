import streamlit as st
from main import constroiGraficoBarraHorizontal

def criar_dicionario_escolaridade(distribuicao):
    return {categoria: distribuicao[categoria] for categoria in dicionario_escolaridade_descricao.values()}

dicionario_escolaridade_descricao = {
    "A": "Nunca estudou.",
    "B": "Não completou a 4ª série/5º ano do Ensino Fundamental.",
    "C": "Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.",
    "D": "Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.",
    "E": "Completou o Ensino Médio, mas não completou a Faculdade.",
    "F": "Completou a Faculdade, mas não completou a Pós-graduação.",
    "G": "Completou a Pós-graduação.",
    "H": "Não sei."
}
faixas_de_renda = {
    "A": "Nenhuma renda.",
    "B": "Até 998,00.",
    "C": "De 998,01 - 1.497,00.",
    "D": "De 1.497,01 - 1.996,00.",
    "E": "De 1.996,01 - 2.495,00.",
    "F": "De 2.495,01 - 2.994,00.",
    "G": "De 2.994,01 - 3.992,00.",
    "H": "De 3.992,01 - 4.990,00.",
    "I": "De 4.990,01 - 5.988,00.",
    "J": "De 5.988,01 - 6.986,00.",
    "K": "De 6.986,01 - 7.984,00.",
    "L": "De 7.984,01 - 8.982,00.",
    "M": "De 8.982,01 - 9.980,00.",
    "N": "De 9.980,01 - 11.976,00.",
    "O": "De 11.976,01 - 14.970,00.",
    "P": "De 14.970,01 - 19.960,00.",
    "Q": "Mais de  19.960,00."
}
microdadosEnem = st.session_state['data']


questionario_01 = microdadosEnem["Grau_Escolaridade_Pai"]
dist_Q001 = questionario_01.value_counts().sort_index()

questionario_02 = microdadosEnem["Grau_Escolaridade_Mae"]
dist_Q002 = questionario_02.value_counts().sort_index()

questionario_06 = microdadosEnem["Renda Familiar"]
dist_Q006 = questionario_06.value_counts().sort_index()

dicionario_pai = criar_dicionario_escolaridade(dist_Q001)
dicionario_mae = criar_dicionario_escolaridade(dist_Q002)
dicionario_renda = {categoria: dist_Q006[categoria] for categoria in faixas_de_renda.values()}

fig_Escolaridade_Pai, ax_Escolaridade_Pai = constroiGraficoBarraHorizontal(dicionario_pai)
fig_Escolaridade_Mae, ax_Escolaridade_Mae = constroiGraficoBarraHorizontal(dicionario_mae)
fig_Renda_Familiar, ax_Renda = constroiGraficoBarraHorizontal(dicionario_renda)

# Exibir gráficos no Streamlit
st.write("### Nível de Escolaridade dos Pais - Pai")
st.pyplot(fig_Escolaridade_Pai)

st.write("### Nível de Escolaridade dos Pais - Mãe")
st.pyplot(fig_Escolaridade_Mae)

st.write("### Renda Familiar")
st.pyplot(fig_Renda_Familiar)
