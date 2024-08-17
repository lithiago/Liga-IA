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

colunas = [
        'TP_FAIXA_ETARIA', 'TP_SEXO', 'TP_ESCOLA',
        'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT','NU_NOTA_REDACAO',
        'NO_MUNICIPIO_PROVA', 'Q001', 'Q002', 'Q006',
    ]

if "data" not in st.session_state:
    print("Entrou")
    microdadosEnem = pd.read_csv(
        "MICRODADOS_ENEM_2019.csv",
        sep=";", 
        encoding='ISO-8859-1',
        usecols=colunas
    )
    st.session_state['data'] = microdadosEnem
    microdadosEnem['Grau_Escolaridade_Pai'] = [dicionario_escolaridade[X] for X in microdadosEnem.Q001]
    microdadosEnem['Grau_Escolaridade_Mae'] = [dicionario_escolaridade[X] for X in microdadosEnem.Q002]
    microdadosEnem['Renda Familiar'] = [faixas_de_renda[X] for X in microdadosEnem.Q006]
    
    # Adicionar a coluna de faixa etária
    microdadosEnem['Faixa Etária'] = microdadosEnem['TP_FAIXA_ETARIA'].map(faixas_etarias)

def constroiGraficoBarra(lista, dados):
    fig, ax1 = plt.subplots(figsize=(16, 8))
    bars = ax1.bar(lista, dados)
    ax1.set_xticks(range(len(lista)))
    ax1.set_xticklabels(lista, rotation=90, fontsize=16)
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), ha='center', va='bottom', fontsize=12)
    return fig, ax1

def constroiGraficoBarraHorizontal(dicionario):
    fig, ax1 = plt.subplots(figsize=(16, 8))
    bars = ax1.barh(list(dicionario.keys()), list(dicionario.values()))
    ax1.set_yticks(range(len(dicionario.keys())))
    ax1.set_yticklabels(dicionario.keys(), rotation=0, fontsize=16)
    ax1.ticklabel_format(useOffset=False, style='plain', axis='x')    
    for bar in bars:
        yval = bar.get_width()
        ax1.text(yval, bar.get_y() + bar.get_height()/2.0, round(yval, 2), ha='left', va='center', fontsize=10)
    

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
