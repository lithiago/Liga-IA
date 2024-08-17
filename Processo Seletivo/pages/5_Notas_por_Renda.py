import streamlit as st
from main import constroiGraficoLinhas

df_data = st.session_state['data']

materias = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
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

categorias_renda = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]
dicionario_renda = {}

for categoria in categorias_renda:
    dados_filtrados = df_data[df_data['Q006'] == categoria]
    medias_notas = dados_filtrados[materias].mean()
    dicionario_renda[categoria] = medias_notas.to_dict()

fig, ax = constroiGraficoLinhas(dicionario_renda)

st.write("### Renda Familiar X Notas")
i = 0
for descricao in faixas_de_renda.values():
    st.write(f"{categorias_renda[i]}: {descricao}")
    i+=1
st.pyplot(fig)