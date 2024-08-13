import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("DashBoard Enem")
st.markdown('''A análise de dados educacionais desempenha um papel crucial na compreensão dos fatores que influenciam o desempenho acadêmico dos estudantes. Em um país com tamanha diversidade socioeconômica como o Brasil, entender como diferentes variáveis afetam o desempenho escolar pode fornecer insights valiosos para políticas públicas e estratégias educacionais.
Feira de Santana, uma das maiores cidades da Bahia, apresenta um cenário educacional com características diversas, refletindo a complexidade do sistema educacional brasileiro. Nesse sentido, o ENEM (Exame Nacional do Ensino Médio), além de uma das principais ferramentas para avaliar o desempenho dos estudantes, é também um indicador da eficácia do sistema educacional. Sendo assim, analisar os dados do ENEM para uma cidade específica como Feira de Santana permite uma abordagem mais focada e relevante, levando em conta as particularidades locais.''')

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

colunas_materias = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
sexos = ['Masculino', 'Feminino']
faixas_etarias = {
    1: 'Menor de 17 anos',
    2: '17 anos',
    3: '18 anos',
    4: '19 anos',
    5: '20 anos',
    6: '21 anos',
    7: '22 anos',
    8: '23 anos',
    9: '24 anos',
    10: '25 anos',
    11: 'Entre 26 e 30 anos',
    12: 'Entre 31 e 35 anos',
    13: 'Entre 36 e 40 anos',
    14: 'Entre 41 e 45 anos',
    15: 'Entre 46 e 50 anos',
    16: 'Entre 51 e 55 anos',
    17: 'Entre 56 e 60 anos',
    18: 'Entre 61 e 65 anos',
    19: 'Entre 66 e 70 anos',
    20: 'Maior de 70 anos'
}
faixas = ["Menor de 17 anos", "17 Anos", "18 Anos", "19 Anos", "20 Anos", "21 Anos", "22 Anos", "23 Anos", "24 Anos", "25 Anos", "Entre 26 e 30 Anos", "Entre 31 e 35 Anos", "Entre 36 e 40 anos", "Entre 41 e 45 Anos", "Entre 46 e 50 Anos", "Entre 51 e 55 Anos"]

@st.cache_data
def carregar_dados():
    colunas = [
        'TP_FAIXA_ETARIA', 'TP_SEXO', 'TP_ESCOLA',
        'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT','NU_NOTA_REDACAO',
        'CO_MUNICIPIO_ESC', 'NO_MUNICIPIO_ESC', 'CO_UF_ESC', 'SG_UF_ESC', 'Q001', 'Q002', 'Q006',
    ]
    
    microdadosEnem = pd.read_csv(
        "MICRODADOS_ENEM_2019.csv",
        sep=";", 
        encoding='ISO-8859-1',
        usecols=colunas
    )
    microdadosEnem = microdadosEnem.dropna()
    microdadosEnem['Grau_Escolaridade_Pai'] = [dicionario_escolaridade[X] for X in microdadosEnem.Q001]
    microdadosEnem['Grau_Escolaridade_Mae'] = [dicionario_escolaridade[X] for X in microdadosEnem.Q002]
    dadosFiltrados = microdadosEnem[microdadosEnem.NO_MUNICIPIO_ESC == "Feira de Santana"]
    return microdadosEnem, dadosFiltrados

microdadosEnem, dadosFiltrados = carregar_dados()


# Adicionar a coluna de faixa etária
microdadosEnem['Faixa Etária'] = microdadosEnem['TP_FAIXA_ETARIA'].map(faixas_etarias)
dadosFiltrados['Faixa Etária'] = dadosFiltrados['TP_FAIXA_ETARIA'].map(faixas_etarias)


questionario_01 = microdadosEnem["Grau_Escolaridade_Pai"]
dist_Q001 = questionario_01.value_counts().sort_index()

questionario_02 = microdadosEnem["Grau_Escolaridade_Mae"]
dist_Q002 = questionario_02.value_counts().sort_index()

questionario_06 = microdadosEnem["Q006"]
dist_Q006 = questionario_06.value_counts().sort_index()

dicionario_renda = {
"Nenhuma Renda": dist_Q006["A"],
"Até R$998,00": dist_Q006["B"],
"De R$998,01 até R$1.996,00": dist_Q006["C"] + dist_Q006["D"],
"De R$1.996,01 até R$2.994,00": dist_Q006["E"] +dist_Q006["F"],
"De R$ 2.994,01 até R$4.990,00": dist_Q006["G"] +dist_Q006["H"],
"De R$4.990,01 até R$6.986,00": dist_Q006["I"]+dist_Q006["J"],
"De R$6.986,01 até R$8.982,00": dist_Q006["K"]+dist_Q006["L"],
"De R$8.982,01 até R$11.976,00": dist_Q006["M"]+dist_Q006["N"],
"Superior a R$11.976,011": dist_Q006["O"]+dist_Q006["P"]+dist_Q006["Q"]
}
def criar_dicionario_nota_por_renda(microdados, materias):
    categorias_renda = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]
    dicionario_renda = {}

    for categoria in categorias_renda:
        dados_filtrados = microdados[microdados['Q006'] == categoria]
        medias_notas = dados_filtrados[materias].mean()
        dicionario_renda[categoria] = medias_notas.to_dict()
    return dicionario_renda
def criar_dicionario_nota(microdados, categorias, materias, questionario):
    dicionario = {}
    for categoria in categorias:
        dadosFiltrados = microdados[microdados[questionario] == categoria]
        medias_notas = dadosFiltrados[materias].mean()
        dicionario[categoria] = medias_notas.to_dict()
    return dicionario

def constroiGraficoBarra(lista, dados):
    fig, ax1 = plt.subplots(figsize=(16, 8))
    bars = ax1.bar(lista, dados)
    ax1.set_xticks(range(len(lista)))
    ax1.set_xticklabels(lista, rotation=90, fontsize=16)
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), ha='center', va='bottom', fontsize=14)
    return fig, ax1
def constroiGraficoBarraHorizontal(dicionario):
    fig, ax1= plt.subplots(figsize=(16, 8))
    ax1.barh(list(dicionario.keys()), list(dicionario.values()))
    ax1.set_yticks(range(len(dicionario.keys())))
    ax1.ticklabel_format(useOffset=False, style='plain', axis='x')
    ax1.set_yticklabels(dicionario.keys(), rotation=0, fontsize= 16)
    return fig, ax1
def constroiGraficoPizza(lista, percentual):
    fig, ax1 = plt.subplots(figsize=(16, 8))
    explode = (0.1, 0)
    ax1.pie(percentual, labels=lista, autopct="%.1f%%", shadow=True, explode=explode)
    return fig, ax1

def constroiGraficoComparativo(lista, dados_particular, dados_publico):
    fig, ax = plt.subplots(figsize=(16, 8))
    width = 0.35
    indices = range(len(lista))
    
    bars_publico = ax.bar(indices, dados_publico, width=width, label='Escolas Públicas', color='lightblue')
    bars_particular = ax.bar([i + width for i in indices], dados_particular, width=width, label='Escolas Privadas', color='lightcoral')
    
    ax.set_xticks([i + width / 2 for i in indices])
    ax.set_xticklabels(lista, rotation=90, fontsize=16)
    
    # Adiciona os valores reais das médias acima das barras (público)
    for bar in bars_publico:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), ha='center', va='bottom', fontsize=14)

    # Adiciona os valores reais das médias acima das barras (particular)
    for bar in bars_particular:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), ha='center', va='bottom', fontsize=14)
    
    ax.legend()
    return fig, ax
import matplotlib.pyplot as plt

def constroiGraficoLinhas(dicionario):
    fig, ax = plt.subplots(figsize=(16, 8))

    # Função para adicionar os valores no gráfico
    
    categorias = list(dicionario.keys())

    # Plotagem e anotação para cada disciplina
    notas_ch = [dicionario[categoria]["NU_NOTA_CH"] for categoria in categorias]
    ax.plot(categorias, notas_ch, label="Ciências Humanas (CH)", marker='o', markersize=8)
    

    notas_cn = [dicionario[categoria]["NU_NOTA_CN"] for categoria in categorias]
    ax.plot(categorias, notas_cn, label="Ciências da Natureza (CN)", marker='o', markersize=8)
    

    notas_mt = [dicionario[categoria]["NU_NOTA_MT"] for categoria in categorias]
    ax.plot(categorias, notas_mt, label="Matemática (MT)", marker='o', markersize=8)
    

    notas_lc = [dicionario[categoria]["NU_NOTA_LC"] for categoria in categorias]
    ax.plot(categorias, notas_lc, label="Linguagens e Códigos (LC)", marker='o', markersize=8)
    

    notas_redacao = [dicionario[categoria]["NU_NOTA_REDACAO"] for categoria in categorias]
    ax.plot(categorias, notas_redacao, label="Redação", marker='o', markersize=8)
    

    ax.legend()  # Adiciona uma legenda para o gráfico
    ax.grid(True)
    
    # Ajuste do espaçamento
    y_min = min(min(notas_ch), min(notas_cn), min(notas_mt), min(notas_lc), min(notas_redacao))
    y_max = max(max(notas_ch), max(notas_cn), max(notas_mt), max(notas_lc), max(notas_redacao))
    
    # Aumentar o intervalo no eixo y para dar mais espaço entre as linhas
    ax.set_ylim([y_min - 30, y_max + 30])

    return fig, ax


def graficoCompartivoNacional():
    escolas_publicas = microdadosEnem[microdadosEnem['TP_ESCOLA'] == 2]    
    escolas_privadas = microdadosEnem[microdadosEnem['TP_ESCOLA'] == 3]    

    desempenho_publico = escolas_publicas[colunas_materias].describe()
    desempenho_privado = escolas_privadas[colunas_materias].describe()

    fig, ax1 = constroiGraficoComparativo(colunas_materias, desempenho_privado.loc['mean'], desempenho_publico.loc['mean'])
    
    return fig, ax1

def graficoComparativoFsa():
    escolas_publicas = dadosFiltrados[dadosFiltrados['TP_ESCOLA'] == 2]
    escolas_privadas = dadosFiltrados[dadosFiltrados['TP_ESCOLA'] == 3]

    
    desempenho_publico = escolas_publicas[colunas_materias].describe()
    desempenho_privado = escolas_privadas[colunas_materias].describe()
    
    fig, ax1 = constroiGraficoComparativo(colunas_materias, desempenho_privado.loc['mean'], desempenho_publico.loc['mean'])

    return fig, ax1

def graficoMediasNotasNacional():
    
    desempenho_nacional = microdadosEnem[colunas_materias].describe()
    fig, ax = constroiGraficoBarra(colunas_materias, desempenho_nacional.loc['mean'])
    return fig, ax

def graficoMediasNotasFsa():
    
    desempenho_fsa = dadosFiltrados[colunas_materias].describe()
    fig, ax = constroiGraficoBarra(colunas_materias, desempenho_fsa.loc['mean'])
    return fig, ax

def graficoDistribuicaoEtariaNacional():
    distribuicao_nacional = microdadosEnem['Faixa Etária'].value_counts().sort_index()
    fig, ax = constroiGraficoBarra(distribuicao_nacional.index, distribuicao_nacional.values)
    return fig, ax

def graficoDistribuicaoEtariaFsa():
    distribuicao_feira = dadosFiltrados['Faixa Etária'].value_counts().sort_index()
    fig, ax = constroiGraficoBarra(faixas, distribuicao_feira.values)
    return fig, ax

def graficoProporcaoGeneroNacional():
    coluna_tp_sexo = microdadosEnem["TP_SEXO"]
    distTP_SEXO = coluna_tp_sexo.value_counts()
    percentSexo_Nacional = [100 * x / distTP_SEXO.sum() for x in distTP_SEXO]
    fig, ax = constroiGraficoPizza(sexos, percentSexo_Nacional)
    return fig, ax
def graficoProporcaoGeneroFsa():
    coluna_tp_sexo_FSA = dadosFiltrados["TP_SEXO"]
    distTP_SEXO_FSA = coluna_tp_sexo_FSA.value_counts()
    percentSexo_FSA = [100 * x / distTP_SEXO_FSA.sum() for x in distTP_SEXO_FSA]
    fig, ax = constroiGraficoPizza(sexos, percentSexo_FSA)
    return fig, ax
    
def criar_dicionario_escolaridade(distribuicao):
    return {categoria: distribuicao[categoria] for categoria in dicionario_escolaridade.values()}
def graficoEscolaridadePai():
    questionario_01 = microdadosEnem["Grau_Escolaridade_Pai"]
    dist_Q001 = questionario_01.value_counts().sort_index()
    dicionario = criar_dicionario_escolaridade(dist_Q001)
    fig, ax = constroiGraficoBarraHorizontal(dicionario)
    return fig, ax
def graficoEscolaridadeMae():
    dicionario = criar_dicionario_escolaridade(dist_Q002)
    fig, ax = constroiGraficoBarraHorizontal(dicionario)
    return fig, ax

def graficoRendaFamiliar():
    
    fig, ax = constroiGraficoBarraHorizontal(dicionario_renda)
    return fig, ax

def graficoNotasPorRenda():
    dicionario_renda = criar_dicionario_nota_por_renda(microdadosEnem, colunas_materias)
    fig, ax = constroiGraficoLinhas(dicionario_renda)
    return fig, ax

def graficoNotasPorEscolaridadePai():
    dicionario = criar_dicionario_nota(microdadosEnem,["A", "B", "C", "D", "E", "F", "G", "H"], colunas_materias, "Q001")
    fig, ax = constroiGraficoLinhas(dicionario)
    return fig, ax
def graficoNotasPorEscolaridadeMae():
    dicionario = criar_dicionario_nota(microdadosEnem,["A", "B", "C", "D", "E", "F", "G", "H"], colunas_materias, "Q002")
    fig, ax = constroiGraficoLinhas(dicionario)
    return fig, ax