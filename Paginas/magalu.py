import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import warnings
import streamlit as st
    
warnings.filterwarnings('ignore')

def magalu():
    #Tratando Dados
    st.subheader('Projeto Análise da MAGALU no Mercado Financeiro 2021 - Disponíbilizado pela Data Viking')
    st.subheader('Segue Canal do Youtube deles : ')
    st.markdown('https://www.youtube.com/channel/UCZT-d8Q9d3obS6NxhyxnznQ?app=desktop')
    
  

#TRATANDO DADOS
    Base_Dados = pd.read_excel('Projeto 3/Vase_004 - Magalu - Sem Resolução.xlsx')
    Dados = Base_Dados.set_index('Data')
    Media_Movel = Dados['Fechamento'].rolling(5).mean()
    Media_Tendencia = Dados['Fechamento'].rolling(30).mean()
    Base_Dados['Mes'] = Base_Dados['Data'].dt.month

#GRAFICO 1
    st.write('Gráfico 1 - Nesta visualização mostraremos uma analise de Fechamento')
    plt.style.use('seaborn-darkgrid')
    plt.figure(figsize=(16,5))
    plt.title('Análise das ações da MAGALU - Fechamento', fontsize=15, loc='left')
    plt.plot(Dados.index, Dados['Fechamento']);
    plt.xlabel('Período da Cotação', fontsize=13);
    plt.ylabel('Valor da Ação (R$)', fontsize=13);
    st.pyplot(plt)
    plt.clf()


#GRÁFICO 2
    st.write('Gráfico 2 - Nesta visualização mostraremos uma analise de Fechamento X Média Movel x Média Tendencia')
    plt.style.use('seaborn-darkgrid')
    plt.figure(figsize=(16,5))
    plt.title('Análise das ações da MAGALU - Fechamento', fontsize=15, loc='left')
    plt.xlabel('Período da Cotação', fontsize=13);
    plt.ylabel('Valor da Ação (R$)', fontsize=13);

    plt.plot(Dados.index, Dados['Fechamento']);
    plt.plot(Media_Movel.index,Media_Movel, color='red');
    plt.plot(Media_Tendencia.index, Media_Tendencia, color='green');
    st.pyplot(plt)
    plt.clf()
#GRÁFICO 3
    st.write('Gráfico 3 - Nesta visualização mostraremos uma BoxPlot(Estatistico) dos Meses')
    plt.style.use('seaborn-darkgrid')
    plt.figure(figsize=(16,8))
    plt.title('BoxPlot para Análise Mensal')
    sns.boxplot(data=Base_Dados, x='Mes',y='Fechamento');
    st.pyplot(plt)
    plt.clf()

#GRÁFICO 4
    st.write('Gráfico 4 - Gráfico Bovespa de Análise da MAGALU')

    Grafico = go.Figure(
    data=[
        go.Candlestick(
            x = Dados.index,
            open = Dados['Abertura'],
            high = Dados['Maior'],
            low = Dados['Menor'],
            close = Dados['Fechamento'],
        )
    ]
    )
    Grafico.update_layout(xaxis_rangeslider_visible=False)
    st.plotly_chart(Grafico)
