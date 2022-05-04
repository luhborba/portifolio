import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def nba():
    #Lendo e Tratando Dados
    df = pd.read_csv('Projeto 5/Players.csv')
    df.head()
    df = df.dropna()
    df = df.rename(columns={
        'Unnamed: 0'	: 'ID',
        'Player' : 'Jogador',
        'height' : 'Altura(cm)',
        'weight' : 'Peso(kg)',
        'collage' : 'Escola',
        'born' : 'Nascido',
        'birth_city' : 'Cidade Natal',
        'birth_state' : 'Estado'
    })
    df['IMC'] = df['Peso(kg)'] / (df['Altura(cm)']/100)**2
    Menor_Altura = df['Altura(cm)'].min()
    Menor_Peso = df['Peso(kg)'].min()
    Maior_Altura = df['Altura(cm)'].max()
    Maior_Peso = df['Peso(kg)'].max()
    #Streamlit
    st.subheader('Projeto Análise da NBA Disponibilizado pela Kaggle')
    st.subheader('Kaggle : https://www.kaggle.com/datasets/drgilermo/nba-players-stats')

    st.write('Tabela de Dados dos Jogadores da NBA desde 1950')
    st.dataframe(df)
    #Gráfico 1
    st.write()
    st.write('Gráfico 1 - Análise TOP 10 Escolas Reveladoras')
    plt.figure(figsize=(15,6))
    plt.title('Analisando TOP 10 Escolas dos Atletas NBA')
    plt.style.use('seaborn-darkgrid')
    plt.bar(df['Escola'].value_counts().head(10).index,df['Escola'].value_counts().head(10));
    plt.xticks(rotation=45, ha='right');
    plt.ylabel('Quantidade de Atletas');
    st.pyplot(plt)
    plt.clf()



    #Gráfico 2 
    st.write('Gráfico 2 - Análise TOP 10 Estados Reveladoras')
    plt.figure(figsize=(15,6))
    plt.style.use('seaborn-darkgrid')
    plt.title('Analisando TOP 10 Estados dos Atletas NBA')
    plt.bar(df['Estado'].value_counts().head(10).index,df['Estado'].value_counts().head(10));
    plt.xlabel('Estados');
    plt.ylabel('Quantidade de Atletas');
    st.pyplot(plt)

    st.subheader("Informações Adicionais")
    st.write(f'A maior altura entre os atletas é de : {Maior_Altura} cm')
    st.write(f'A menor altura entre os atletas é de : {Menor_Altura} cm')
    st.write(f'O maior peso entre os atletas é de : {Maior_Peso} kg')
    st.write(f'O menor peso entre os atletas é de : {Menor_Peso} kg')
    st.write(f'A média de altura entre os atletas é de : {round(df["Altura(cm)"].mean(),2)} cm')
    st.write(f'A média de peso entre os atletas é de : {round(df["Peso(kg)"].mean(),2)} kg')
