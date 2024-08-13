import streamlit as st
import main

microdadosEnem, dadosFiltrados = main.carregar_dados()

fig_Escolaridade_Pai, ax_Escolaridade_Pai = main.graficoEscolaridadePai()
fig_Escolaridade_Mae, ax_Escolaridade_Mae = main.graficoEscolaridadeMae()
fig_Renda_Familiar, ax_Renda = main.graficoRendaFamiliar()

# Exibir gráficos no Streamlit
st.write("### Nível de Escolaridade dos Pais - Pai")
st.pyplot(fig_Escolaridade_Pai)

st.write("### Nível de Escolaridade dos Pais - Mãe")
st.pyplot(fig_Escolaridade_Mae)

st.write("### Renda Familiar")
st.pyplot(fig_Renda_Familiar)
