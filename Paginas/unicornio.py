import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   
import streamlit as st

def Uni():

    st.subheader('Projeto Empresas Unicórnios Disponíbilizado pela Data Viking')
    st.subheader('Segue Canal do Youtube deles : ')
    st.markdown('https://www.youtube.com/channel/UCZT-d8Q9d3obS6NxhyxnznQ?app=desktop')
    banco = pd.read_csv('Projeto 1/Startups in 2021 end.csv')
    banco.rename(columns={
        'Unnamed: 0' : 'ID',
        'Company' : 'Empresa',
        'Valuation ($B)' : 'Valor $',
        'Date Joined' : 'Data de Adesão',
        'Country' : 'Pais',
        'City' : 'Cidade',
        'Industry' : 'Industria',
        'Select Investors' : 'Investidores'},
        inplace=True

        )
#Grafico 1 - Analise das Industrias
    st.write('Gráfico 1 - Nesta visualização mostraremos uma analise das Industrias mais Presentes')
    plt.figure(figsize=(15,6))
    plt.title('Analise das Industrias')
    plt.bar(banco['Industria'].value_counts().index,banco['Industria'].value_counts());
    plt.xticks(rotation=45, ha='right');

    st.pyplot(plt)
    plt.clf()

#Tratamento de Dados
    Analise = round(banco['Pais'].value_counts(normalize=True) * 100, 1)

#Grafico 2 - Pais Unicórnios Top 5
    st.write("Gráfico 2 - Nesta visualização mostraremos uma analise dos Tops 5 - Geradores de Unicórnios")
    plt.figure(figsize=(15,6))
    plt.title('Analise dos Paises Top 5 - Geradores e Unicórnios')
    plt.pie(
        Analise.head(5),
        labels = Analise.index[0:5],
        autopct='%1.1f%%'
    );


    st.pyplot(plt)
    plt.clf()

#Tratamento de Dados
    banco['Mes'] = pd.DatetimeIndex(banco['Data de Adesão']).month
    banco['Ano'] = pd.DatetimeIndex(banco['Data de Adesão']).year
    banco['Valor $'] = pd.to_numeric(banco['Valor $'].apply( lambda Linha: Linha.replace('$','')))
    Analise_Pais = banco.groupby(by=['Pais']).sum()['Valor $'].reset_index()
    Analise_Valor = Analise_Pais.sort_values('Valor $',ascending=False)

#Gráfico 3 - 
    st.write('Gráfico 3 - Nesta visualização mostraremos o TOP 8 Valores por Pais')
    plt.figure(figsize=(15,6))
    plt.title('Analise de Valor por Pais Top 8')
    plt.plot(Analise_Valor['Pais'].head(8),Analise_Valor['Valor $'].head(8));
    plt.xticks(rotation=45,ha='right');
    plt.ylabel('Valor $ (Bilhões)')

    st.pyplot(plt)
    plt.clf()
