import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import Paginas.pagina_inicial as pi
import Paginas.unicornio as u
import Paginas.magalu as m
import Paginas.ps4 as ps4


import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Luciano Borba - Portifólio", page_icon="🖥", layout="centered")

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
   u.Uni()

elif SideBar == 'Projeto Mercado Financeiro':
    m.magalu()

elif SideBar == 'Projeto PS4':
    ps4.ps4()
elif SideBar == 'Outros':
    st.title("Logo logo teremos mais")
