import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import warnings
from sklearn.preprocessing import LabelEncoder

warnings.filterwarnings('ignore')

def ps4():
    
    #LENDO DADOS
    df = pd.read_csv('Projeto 4/PS4_GamesSales.csv', encoding='latin-1')
    #Tratando Dados
    df = df.dropna()
    df = df.loc[ (df['Year'] != 2019) &  (df['Year'] != 2020)]
    Analise = df.groupby( by=['Year'] ).sum().reset_index()
    America = [ America / Total * 100 for America, Total in zip(Analise['North America'] , Analise['Global'])]
    Europa = [ Europa / Total * 100 for Europa, Total in zip(Analise['Europe'] , Analise['Global'])]
    Japao = [ Japao / Total * 100 for Japao, Total in zip(Analise['Japan'] , Analise['Global'])]
    Mundo = [ Mundo / Total * 100 for Mundo, Total in zip(Analise['Rest of World'] , Analise['Global'])]
    Funcao_Label = LabelEncoder()   
    df['Produtora'] = Funcao_Label.fit_transform (df.Publisher)
    df['Genero'] = Funcao_Label.fit_transform (df.Genre)
    df['Jogo'] = Funcao_Label.fit_transform (df.Game)
    Paleta_Cores = sns.color_palette('husl',8)
    large_b = 0.5
    rotulos = Analise['Year']
    Grupos = [ 0,1,2,3,4,5]

    
#Gráfico 1-
    st.write('Gráfico 1 - Nesta visualização mostraremos uma analise de Estatistica de Distribuição de Vendas dos Generos')
    plt.figure(figsize=(15,8))

    #Gráfico
    plt.title('Análise de Distribuição Global por Genero (mi)')
    sns.barplot(data=df,x='Genre',y='Global', ci=None,  estimator=sum);
    plt.xlabel('Genero');
    plt.ylabel('Vendas Globais (mi)')
    plt.xticks(rotation=45,ha='right');
    st.pyplot(plt)
    plt.clf()

    #Esqueleto do subplot

    #Tamanho da Imagem
    fig, ax = plt.subplots(figsize=(18,15))

    #Cor de Fundo
    Cor_Fundo = '#f5f5f5'
    ax.set_facecolor(Cor_Fundo)
    fig.set_facecolor(Cor_Fundo)

    #Paramentros para o Grid
    Linhas = 3
    Colunas = 2

    #Estilo do Grafico
    plt.style.use('seaborn')
    #Título Geral
    plt.suptitle('Python para Análise de Dados \n Projeto Prático 5 - Análise Mercado de Games PS4', fontsize=22, color='#404040', fontweight=600)

    #Acessando Gráfico 1
    plt.subplot( Linhas, Colunas, 1)
        #Título
    plt.title('Vendas Globais Por Ano (Mi)', loc='left', fontsize=14)
        #Gráfico
    plt.bar(df['Year'],df['Global'], color='#69b3a2');
        #Label
    plt.ylabel('Quantidade de Vendas (mi)');


    #Acessando Gráfico 2
    plt.subplot( Linhas, Colunas, 2)
    #Gráfico
    plt.title('Análise de Distribuição Global (mi)', loc='left', fontsize=14)
    sns.boxplot(data=df,x='Year',y='Global');



    #Acessando Gráfico 3
    plt.subplot( Linhas, Colunas, 3)
    plt.title('Análise da Distribuição por Continentes', loc='left', fontsize=14)
        #Plot America
    plt.bar(Grupos, America, width=large_b, color='#b5ffb9', edgecolor='white');
        #Plot Europa
    plt.bar(Grupos, Europa,bottom=America, width=large_b, color='#f9bc86', edgecolor='white');
        #Plot Japão
    plt.bar(Grupos, Japao, bottom=[A+B for A,B in zip(America, Europa)] , width=large_b,color='#a3acff',edgecolor='white');
        #Plot Resto do Mundo
    plt.bar(Grupos, Mundo, bottom=[A+B+C for A,B,C in zip(America, Europa, Japao)] , width=large_b,color='#d3dcfe',edgecolor='white');
        #Label
    plt.xticks(Grupos, rotulos);
    plt.xlabel('Grupo')
    plt.ylabel('Distribuição')
    plt.legend(['America do Norte', 'Europa', 'Japão','Mundo' ], loc='upper left', bbox_to_anchor=(0.15,-0.1), ncol=4);




    #Acessando Gráfico 4
    plt.subplot( Linhas, Colunas, 4)
    plt.title("Analise de Produtores de Game (mi)")
    sns.scatterplot(data=df, x='Produtora',y='Global', color=Paleta_Cores[0]);

    #Acessando Gráfico 5
    plt.subplot( Linhas, Colunas, 5)
    plt.title("Analise dos Generos de Game (mi)", loc='left', fontsize=14)
    sns.scatterplot(data=df, x='Genero',y='Global', color=Paleta_Cores[0]);

    #Acessando Gráfico 6
    plt.subplot( Linhas, Colunas, 6);
    plt.title("Analise dos Games (mi)", loc='left', fontsize=14)
    sns.scatterplot(data=df, x='Jogo',y='Global', color=Paleta_Cores[0]);

    #Ajustar Layout
    plt.subplots_adjust(hspace=0.35, wspace=0.15)

    #Rodapé
    Rodape = '''
    Este relatório foi elaborado no treinamento "Python para Análise de Dados"
    Está dispónivel no Canal do Youtube @Data Viking
    by: @Luciano Borba'''


    fig.text(0.5,-0.05,Rodape,ha='center',va='bottom', size=12, color='#938ca1');
    st.write("Gráfico 2 - Aqui mostraremos uma cadeia de gráfico gerenciais para facilitar as tomadas de decisões futuras como também a vizualização do panorama atual")
    st.pyplot(fig)
