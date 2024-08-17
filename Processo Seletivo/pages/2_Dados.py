import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from main import constroiGraficoComparativo, constroiGraficoBarra, constroiGraficoPizza

def compartivoEscolas(df):
    escolas_publicas = df[df['TP_ESCOLA'] == 2]
    escolas_privadas = df[df['TP_ESCOLA'] == 3]

    desempenho_publico = escolas_publicas[materias].describe()
    desempenho_privado = escolas_privadas[materias].describe()
    return desempenho_publico, desempenho_privado
def mediaNotas(df):
    desempenho = df[materias].describe()
    return desempenho
def faixaEtaria(df):
    distribuicao = df['Faixa Etária'].value_counts().sort_index()
    return distribuicao
def proporacaoGenero(df):
    coluna_tp_sexo = df["TP_SEXO"]
    distTP_SEXO = coluna_tp_sexo.value_counts()
    percentSexo = [100 * x / distTP_SEXO.sum() for x in distTP_SEXO]
    return percentSexo


microdadosEnem = st.session_state['data']
dadosFiltrados = microdadosEnem[microdadosEnem.NO_MUNICIPIO_PROVA == "Feira de Santana"]
materias = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']

#Grafico comparativo entre as escolas privadas e publicas de todo o Brasil
desempenho_publico_brasil, desempenho_privado_brasil = compartivoEscolas(microdadosEnem)

fig_comparativo_brasil_escolas, ax_escolas_brasil = constroiGraficoComparativo(materias, desempenho_privado_brasil.loc['mean'], desempenho_publico_brasil.loc['mean'])

#Grafico comparativo entre as escolas privadas e publicas de Feira de Santana
desempenho_publico_fsa, desempenho_privado_fsa = compartivoEscolas(dadosFiltrados)

fig_comparativo_fsa_escolas, ax_escolas_fsa = constroiGraficoComparativo(materias, desempenho_privado_fsa.loc['mean'], desempenho_publico_fsa.loc['mean'])

#Grafico da média das notas em todo o Brasil
desempenho_nacional = mediaNotas(microdadosEnem)
fig_notas_nacional, ax_notas_nacional = constroiGraficoBarra(materias, desempenho_nacional.loc['mean'])
#Grafico da média das notas em Feira de Santana
desempenho_fsa = mediaNotas(dadosFiltrados)
fig_notas_fsa, ax_notas_fsa = constroiGraficoBarra(materias ,desempenho_fsa.loc['mean'])
#Grafico da distribuicao Etaria em todo o Brasil
distribuicao_Etaria_nacional = faixaEtaria(microdadosEnem)
fig_Etaria_Nacional, ax_Nacional_Etaria = constroiGraficoBarra(distribuicao_Etaria_nacional.index, distribuicao_Etaria_nacional.values)
#Grafico da distribuicao em Feira de SANTANA
distribuicao_Etaria_fsa = faixaEtaria(dadosFiltrados)
fig_Etaria_Feira, ax_Feira_Etaria = constroiGraficoBarra(distribuicao_Etaria_fsa.index, distribuicao_Etaria_fsa.values)
#Grafico da distribuicao de genero em todo o Brasil
percentual_nacional_genero = proporacaoGenero(microdadosEnem)
fig_Genero_Nacional, ax_Nacional_Genero = constroiGraficoPizza(["Masculino", "Feminino"], percentual_nacional_genero)
#Grafico da distribuicao de genero em Feira de Santana
percentual_fsa_genero = proporacaoGenero(dadosFiltrados)
fig_Genero_Feira, ax_FSA_Genero = constroiGraficoPizza(['Masculino', 'Feminino'], percentual_fsa_genero)

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

ax_escolas_brasil.set_title(
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
col5.pyplot(fig_comparativo_brasil_escolas)
col6.pyplot(fig_comparativo_fsa_escolas)
col7.pyplot(fig_notas_nacional)
col8.pyplot(fig_notas_fsa)
