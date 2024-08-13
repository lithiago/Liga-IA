import streamlit as st
import main

microdadosEnem, dadosFiltrados = main.carregar_dados()


fig_nota_escolaridade_pai, ax_pai = main.graficoNotasPorEscolaridadePai()
fig_nota_escolaridade_mae, ax_mae = main.graficoNotasPorEscolaridadeMae()

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