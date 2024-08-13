import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import main


microdadosEnem, dadosFiltrados = main.carregar_dados()

fig_notas_nacional, ax_notas_nacional = main.graficoMediasNotasNacional()
fig_notas_fsa, ax_notas_fsa = main.graficoMediasNotasFsa()
fig_comparativo_nacional_escolas, ax_escolas_nacional = main.graficoCompartivoNacional()
fig_comparativo_fsa_escolas, ax_escolas_fsa = main.graficoComparativoFsa()
fig_Etaria_Nacional, ax_Nacional_Etaria = main.graficoDistribuicaoEtariaNacional()
fig_Etaria_Feira, ax_Feira_Etaria = main.graficoDistribuicaoEtariaFsa()
fig_Genero_Nacional, ax_Nacional_Genero = main.graficoProporcaoGeneroNacional()
fig_Genero_Feira, ax_FSA_Genero = main.graficoProporcaoGeneroFsa()

ax_Nacional_Etaria.set_title(
    "Distribuição Etária Nacional", fontdict={'fontsize': 16, 'fontweight': 'bold', 'family': 'serif'}
)
ax_Feira_Etaria.set_title(
    "Distribuição Etária de Feira de Santana", 
    fontdict={'fontsize': 16, 'fontweight': 'bold', 'family': 'serif'}
)
ax_notas_fsa.set_title(
    "Médias das Notas de Feira de Santana np Enem de 2019", 
    fontdict={'fontsize': 16, 'fontweight': 'bold', 'family': 'serif'}
)
ax_notas_nacional.set_title(
    "Médias das Notas em todo Brasil no Enem de 2019", 
    fontdict={'fontsize': 16, 'fontweight': 'bold', 'family': 'serif'}
)


fig_Etaria_Nacional.tight_layout()
fig_Etaria_Feira.tight_layout()


ax_Nacional_Genero.set_title(
    "Homens e Mulheres no Enem 2019 em todo Brasil", 
    fontdict={'fontsize': 16, 'fontweight': 'bold', 'family': 'serif'}
)

ax_FSA_Genero.set_title(
    "Homens e Mulheres no Enem 2019 em Feira de Santana", 
    fontdict={'fontsize': 16, 'fontweight': 'bold', 'family': 'serif'}
)

ax_escolas_nacional.set_title(
    "Escolas Públicas e Particulares no Enem 2019 em todo Brasil", 
    fontdict={'fontsize': 16, 'fontweight': 'bold', 'family': 'serif'}
)

ax_escolas_fsa.set_title(
    "Escolas Públicas e Particulares no Enem 2019 em Feira de Santana", 
    fontdict={'fontsize': 16, 'fontweight': 'bold', 'family': 'serif'}
)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)
col1.pyplot(fig_Etaria_Nacional)
col2.pyplot(fig_Etaria_Feira)
col3.pyplot(fig_Genero_Nacional)
col4.pyplot(fig_Genero_Feira)
col5.pyplot(fig_comparativo_nacional_escolas)
col6.pyplot(fig_comparativo_fsa_escolas)
col7.pyplot(fig_notas_nacional)
col8.pyplot(fig_notas_fsa)
