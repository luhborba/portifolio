import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

def ps4():
    
    #LENDO DADOS
    df = pd.read_csv('Projeto 4/PS4_GamesSales.csv', encoding='latin-1')
    #Tratando Dados
    df = df.dropna()
    df = df.loc[ (df['Year'] != 2019) &  (df['Year'] != 2020)]
    st.subheader('Projeto Análise PS4 - Disponíbilizado pela Data Viking')
    st.subheader('Segue Canal do Youtube deles : https://www.youtube.com/channel/UCZT-d8Q9d3obS6NxhyxnznQ?app=desktop')
    #Gráfico 1 - 
    st.write('Gráfico 1 - Nesta visualização mostraremos uma analise de Vendas Globais por Ano')
    #Tamanho
    plt.figure(figsize=(10,5))

    #Titulo
    plt.title('Vendas Globais Por Ano (Mi)', loc='left', fontsize=14)

    #Gráfico
    sns.barplot(data=df,x='Year',y='Global', ci=None, color='#69b3a2', estimator=sum);
    plt.ylabel('Quantidade de Vendas (mi)');
    st.pyplot(plt)
    plt.clf()

#Gráfico 2 - 
    st.write('Gráfico 2 - Nesta visualização mostraremos uma analise de Distribuição de Vendas')
    # Tamanho
    plt.figure(figsize=(12,5))

    #Estilo
    plt.style.use('ggplot')

    #Titulo
    plt.title('Distribuição das vendas Globais', loc='left', fontsize=14)

    #Plot
    sns.kdeplot(df['Global'], shade=True, bw=1, color='#96a8a8', linewidth=2.5);
    st.pyplot(plt)
    plt.clf()

#Gráfico 3-
    st.write('Gráfico 3 - Nesta visualização mostraremos uma analise de Estatistica de Distribuição de Vendas')
    #Tamanho
    plt.figure(figsize=(15,8))

    #Gráfico
    plt.title('Análise de Distribuição Global (mi)')
    sns.boxplot(data=df,x='Year',y='Global');
    st.pyplot(plt)
    plt.clf()

#Gráfico 4-
    st.write('Gráfico 4 - Nesta visualização mostraremos uma analise de Estatistica de Distribuição de Vendas')
    plt.figure(figsize=(15,8))

    #Gráfico
    plt.title('Análise de Distribuição Global por Genero (mi)')
    sns.barplot(data=df,x='Genre',y='Global', ci=None,  estimator=sum);
    plt.xlabel('Genero');
    plt.ylabel('Vendas Globais (mi)')
    plt.xticks(rotation=45,ha='right');
    st.pyplot(plt)
    plt.clf()
