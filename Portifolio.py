import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import Paginas.pagina_inicial as pi
import streamlit.components.v1 as c


import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Luciano Borba - Portifólio", page_icon="🖥", layout="centered")

page_bg_img = '''
<style>
body {
background-image: url("https://img.freepik.com/fotos-gratis/fundo-preto-antigo-textura-do-grunge-papel-de-parede-escuro-quadro-negro-quadro-negro-parede-da-sala_1258-28312.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
#Titulo

st.title('Luciano Borba - Projetos')
st.sidebar.title('Menu')
SideBar = st.sidebar.selectbox('Escolha o Projeto: ', ['Página Incial','Projeto SMS(Power BI)','Projeto Unicórnios','Projeto Mercado Financeiro','Projeto PS4','Outros'])
if SideBar == 'Página Incial':
    pi.Porti()
    
elif SideBar == 'Projeto SMS(Power BI)':
    st.subheader('Projeto de Análise Salaria da Secretaria Municipal de João Pessoa no Ano de 2021 feito em Power BI')
    st.markdown('<iframe title="LabSMS" width="800" height="636" src="https://app.powerbi.com/view?r=eyJrIjoiMjExYzI4MDAtMTg2Zi00MzU0LWFiMzMtOTg1Y2YzNjliNTc1IiwidCI6IjM2ZjUxZmFhLThiYTItNDcxNy1iMmFlLTEwNTIxNzFjNjM0YiJ9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
elif SideBar == 'Projeto Unicórnios':
#Tratando Dados
    st.subheader('Projeto Empresas Unicórnios Disponíbilizado pela Data Viking')
    st.subheader('Segue Canal do Youtube deles : https://www.youtube.com/channel/UCZT-d8Q9d3obS6NxhyxnznQ?app=desktop')
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

elif SideBar == 'Projeto Mercado Financeiro':
    #Tratando Dados
    st.subheader('Projeto Análise da MAGALU no Mercado Financeiro 2021 - Disponíbilizado pela Data Viking')
    st.subheader('Segue Canal do Youtube deles : https://www.youtube.com/channel/UCZT-d8Q9d3obS6NxhyxnznQ?app=desktop')
    #imports
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.graph_objects as go
    import warnings

    warnings.filterwarnings('ignore')

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


elif SideBar == 'Projeto PS4':
    #LENDO DADOS
    df = pd.read_csv('Projeto 4/PS4_GamesSales.csv', encoding='latin-1')
    #Tratando Dados
    df = df.dropna()
    df = df.loc[ (df['Year'] != 2019) &  (df['Year'] != 2020)]

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
elif SideBar == 'Outros':
    st.title("Logo logo teremos mais")
