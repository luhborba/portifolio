import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import Paginas.pagina_inicial as pi
import Paginas.unicornio as u
import Paginas.magalu as m
import Paginas.ps4 as ps4
import Paginas.nba as nba
import Paginas.pib as pib


import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Luciano Borba - Portifólio", page_icon="🖥", layout="centered")

#Titulo

st.title('Luciano Borba - Projetos')
st.sidebar.title('Menu')
SideBar = st.sidebar.selectbox('Escolha o Projeto: ', ['Página Incial','Projeto Análise Secretaria de Saúde de João Pessoas(Power BI)','Projeto Unicórnios','Projeto Mercado Financeiro (MAGALU)','Projeto PS4','Projeto NBA','Projeto Renda Per Capita','Outros'])
if SideBar == 'Página Incial':
    pi.Porti()
    
elif SideBar == 'Projeto Análise Secretaria de Saúde de João Pessoas(Power BI)':
    st.subheader('Projeto de Análise Salarial da Secretaria Municipal de João Pessoa no Ano de 2021 feito em Power BI')
    st.write('''
    Estes dados foram coletados atráves do Portal da Transparência deste Município.
    O arquivo foi importado em CSV, através do próprio portal, e foram analisados o tipo de vínculo dos funcionários mais presentes, como também responder algumas perguntas, são elas:<br>
    **1)** Qual foi o gasto salarial mensal?<br>
    **2)** Quais são os vínculos destes Servidores? e Existem quantos funcionários em cada um desses vínculos?<br>
    **3)** Qual a média salarial por mês?<br>
    **4)** Total salarial por tipo de salarial?<br>
    **5)** Qual a média salarial?
    ''', unsafe_allow_html=True)
    st.markdown('<iframe title="LabSMS" width="800" height="636" src="https://app.powerbi.com/view?r=eyJrIjoiMjExYzI4MDAtMTg2Zi00MzU0LWFiMzMtOTg1Y2YzNjliNTc1IiwidCI6IjM2ZjUxZmFhLThiYTItNDcxNy1iMmFlLTEwNTIxNzFjNjM0YiJ9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
elif SideBar == 'Projeto Unicórnios':
#Tratando Dados
   u.Uni()

elif SideBar == 'Projeto Mercado Financeiro (MAGALU)':
    m.magalu()

elif SideBar == 'Projeto PS4':
    ps4.ps4()
    
elif SideBar == 'Projeto NBA':
    nba.nba()
    
elif SideBar == 'Projeto Renda Per Capita':
    pib.pib()
    
elif SideBar == 'Outros':
    st.title("Logo logo teremos mais")
