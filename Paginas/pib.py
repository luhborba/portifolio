#IMPORTAÇÕES
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


def pib():
    Base = pd.read_excel('Projeto 6/Dados_Pib.xlsx')
    #Sistema de Grids

    #Cor de Fundo
    CorF = '#f5f5f5'

    #Criar Sistema de Grids
    Grid = sns.FacetGrid(Base, col='Territorialidades',hue='Territorialidades',col_wrap=4)

    Grid = Grid.map(plt.plot, 'Ano', 'PIB per capita')

    #Sombra + Ajuste do Titulo
    Grid = Grid.map(plt.fill_between, 'Ano', 'PIB per capita', alpha=0.2).set_titles('{col_name} Territorialidades');

    #Filtrando Titulo
    Grid = Grid.set_titles('{col_name}')

    #Titulo Geral

    Grid = Grid.fig.suptitle('Evolução de Rendar per capita por Estado \n Relatório elaborado no treina,ento Python para Análise de Dados \n Dispónivel no Youtude da @Data Viking e reproduzido por @Luciano Borba',
    fontsize=18)
    #Ajustando Titulo
    plt.subplots_adjust( top=0.92)
    st.write('GRID 1 - Neste GRID mostraremos a a evolução de PIB per Capita dos Anos 2013 a 2016')
    st.pyplot(plt)
