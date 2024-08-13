import streamlit as st
import main


microdadosEnem, dadosFiltrados = main.carregar_dados()

fig_nota_renda, ax_nota_renda = main.graficoNotasPorRenda()

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
i = 0
categorias= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]
for descricao in faixas_de_renda.values():
    st.write(f"{categorias[i]}: {descricao}")
    i+=1
st.pyplot(fig_nota_renda)