import streamlit as st

def Porti():
    st.write('Olá! Muito Prazer me chamo Luciano de Andrade Borba, sou casado, tenho 3 filhos, sou uma pessoa apaixonada pela área de Tecnologia, em especial área de Dados, amo agregar valor através das minhas análises, assim impactando no dia a dia das pessoas!')
    st.write('')
    st.write('Trabalho na **Secretaria Municipal de Saúde de João Pessoa**, sou _Data Analytics_, atuo analisando dados organizacionais para auxiliar no planejamento financeiro da Secretaria.')
    st.write('')
    st.write('**-Tecnologia Utilizada: (Lista em Ordem de Experiência, Utilização e Habilidade)**')
    st.write('''
    -Linguagem Python<br>
    -PowerBI<br>
    -Excel/Google Sheets<br>
    -SQL Server<br>
    -MySQL<br>
    -Oracle Database<br>
    -Oracle Apex (Low Code)<br>
    -Tableau Public<br>
    -Linguagem R<br><br>    
    ''',unsafe_allow_html= True)
    FAcad = st.expander('Formação Acadêmica')
    with FAcad:
        st.write('''
        **-Formado em Gestão da Tecnologia da Informação - Nível Tecnologo - FPB - 2012.1 a 2014.1**<br>
        **-Em Andamento - Pós-Graduação em Analise de Dados - Descomplica - 03/2022**<BR>
        **-Em Andamento - MBA em Business Intelligence - Descomplica - 04/2022**<BR><BR>
        ''',unsafe_allow_html= True)
    Exp = st.expander('Experiência')
    with Exp:
        st.write('**-Analista de Dados - Secretaria Municipal de Saúde de João Pessoa - 01/04/2022 [Emprego Atual]**')
        st.write('Atuando com Dados em grande volume, com foco para planejamento organizacional para planejamentos, mas mediante ao projeto analisando dados dos cidadões para melhor planejamento de ações de Saúde na cidade')
        st.write('**-Técnico de Suporte a Sistemas - Secretaria Municipal de Saúde de João Pessoa - 01/01/2021 a 31/03/2022** ')
        st.write('Atuando com Treinamento, Suporte HelpDesk, Suporte Remoto, geração de relatório e dashboards')
        st.write('**-Técnico de Informática - Secretaria Municipal de Saúde de João Pessoa - 04/04/2018 a 31/12/2020**')
        st.write('Atuando com HelpDesk, Suporte de Software, Elaboração de Material para Suporte, Elaboração Termos para Contratação/Aquisição de Equipamentos e Suprimento de informática ')
    Curso = st.expander('Cursos Complementares')
    with Curso:
        st.write('''
        -Python para Engenheiros e Cientistas - 19,5 Horas - Udemy[05/2022]<BR>
        -Introdução ao Tableau - 5 Horas - EIA[04/2022]<BR>
        -Machine Learning com Python - 3 Horas - Regressão Linear - DataViking[04/2022]<BR>
        -SQL com Python - 3 Horas - DataViking[04/2022]<BR>
        -Microsoft PowerBI para DataScience - 72 Horas - DataScience Academy[04/2022]<BR>
        -Visualização de Dados(DataViz) - 10 Horas - Estidados[04/2022]<BR>
        -Python para Iniciantes - 5 Horas - EIA[04/2022]<BR>
        -Pyhton para Análise de Dados - 12 Horas - Udemy[04/2022]<BR>
        -Dashboards Matadores: Domine a Arte de Aprensentação de Dados - 3 Horas - EIA[03/2022]<BR>
        -Data Science para Iniciantes - 3 Horas - EIA[03/2022]<BR>
        -Python Fundamentos para Análise de Dados - 60 Horas - DataScience Academy[03/2022]<BR>
        -LGDP: Registro das Operações de tratamento de Dados Pessoais - 3 Horas - Udemy[03/2022]<BR>
        -LGDP Zero: Conceitos fundamentais de Proteção Dados Pessoais  - 1,5 Horas - EIA[03/2022]<BR>
        -Python - Mundo 1 - 40 Horas - Cruso em Vídeo[03/2022]<BR>
        -Técnicas Avançadas de Python - 2Horas - LinkedinLearning[02/2022]<BR>
        -Fundamentos do Big Data: Técnicas e Conceitos - 2Horas - LinkedinLearning[02/2022]<BR>
        -Big Data Fundamentos 3.0 - 12 Horas - DataScience Academy[02/2022]<BR>
        -Python para Ciência de Dados: Formação Básica - 4 Horas - LinkedinLearning[02/2022]<BR>
        -Data Science: Visualização de dados com Python - 2 Horas - DiegoMariano[02/2022]<BR>
        -Conformidade com a LGPD: O Impacto em Empresas Brasileiras - 1 Hora - LinkedinLearning[02/2022]<BR>
        -LGPD Política de Privacidade e Proteção de Dados Pessoais - 4 Horas - Udemy[02/2022]<BR>
        -Fundamentos da Ciência de Dados - 3 Horas - LinkedinLearning[01/2022]<BR>
        -Introducao a Ciência de Dados - 12 Horas - DataScience Academy[01/2022]<BR>
        -Descubra o Pythons - 2 Horas - LinkedinLearning[01/2022]<BR>
        -Introdução ao Python - 2 Horas - DiegoMariano[01/2022]<BR>
        -Oracle Apllication Express - APEX - Básico - 4 Horas - Udemy[03/2021]<BR>
        -Power BI - Do Básico ao Avançado - 9,5 Horas - Udemy[02/2021]<BR>
        -Fundamentos Scrum - 1,5 Horas - Udemy[01/2021]<BR>
        -Introdução ao Sistema Operacional Linux - 2 Horas - DiegoMariano[01/2021]<BR>
        -Introdução ao banco de dados MySQL - 0,5 Horas - DiegoMariano[01/2021]<BR><BR>    
        ''',unsafe_allow_html= True)
    Certifi = st.expander('Certificações')
    with Certifi:
        st.write("""
        -Fundamento da Informatica - IBSEC[03/2022]<br>
        -Exame Python Básico - Logikraft[03/2022]<br>
        -Scrum Fundamentals Certified - ScrumStudy[01/2021]
        <br><br>""",unsafe_allow_html= True)
    st.subheader('Todos os certificados estão na Pasta do GitHub do Portifólio')
    st.markdown('https://github.com/luhborba/portifolio/tree/main/Certificados')
    st.title('Navegue pelo menu a direita para visualizar meus projetos realizados')
    st.markdown('Me siga no Linkedin: www.linkedin.com/in/luhborba')
    st.markdown('Entra lá no meu Canal do Youtube: https://www.youtube.com/channel/UCN16u-GFjdNmVWlxBZvRqsQ')
    
