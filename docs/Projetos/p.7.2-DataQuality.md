# Projeto Data Quality

Este projeto de Data Quality foi desenvolvido após Workshop do [Luciano Vasconcelos Filho](https://www.linkedin.com/in/lucianovasconcelosf/)

**GitHub do Projeto:** [Deputados-LuhBorba](https://github.com/luhborba/projeto_camara_deputados)<br>
**Documentação do Projeto:**  [Documentacao](https://luhborba.github.io/workshop-free-lgalvao/)<br>

## Stack do Projeto

- python
- streamlit
- selenium
- pytest
- taskipy
- pydantic
- openpyxl
- mkdocs
- mkdocstrings
- mkdocs-material

## Proposta do Projeto

O projeto tem como objetivo realizar um processo de validação de estrutura de uma planilha no Excel, considerando que hoje no mundo corporativo esta é uma ferramenta amplamente usada, assim buscando definições padrões para envios de dados considerando um estrutura de contrato pre-definida.

A abordagem utilizada é criar um App no Streamlit que realize todo processo de validação, ferramenta com criação de testes, buscando assim um qualidade no dado enviado.

## Estrutura do Projeto

O projeto está basicamente dividido em 4 (quatro) arquivos, todos eles dentro da pasta `src`.

- app.py
- backend.py
- contrato.py
- frontend.py

### App.py

Aqui é particularmente faço a união entre o frontend e backend, carregando assim todas as validações propostas no backend e trazendo todos os visuais carregados no frontend.

