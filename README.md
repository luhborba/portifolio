# Bem vindo ao Meu Portifólio
]
Se você deseja ver a página deste portifólio [Clique Aqui](https://luhborba.github.io/portifolio/)

Para utilização desse projeto você de Possuir o `Pyenv` e `Poetry` instalado na sua maquina, caso não tenha segue links a seguir sobre instalação:

[Clique aqui para Guia Instalação no Linux/WSL](https://github.com/luhborba/Wsl-Pyenv-Poetry)

[Clique aqui para Guia Instalação no Windows](https://www.youtube.com/watch?v=9LYqtLuD7z4)

Após instalação das ferramentas anteriores você pode seguir o passo-a-passo:

1. Clone o repositório:
```bash
git clone https://github.com/luhborba/portifolio.git
cd portifolio
```

2. Configure a versão correta do Python com `pyenv`
```bash
pyenv install 3.11
pyenv local 3.11
```

3. Ativando Poetry
```bash
poetry shell
```

4. Instalando Dependências
```bash
poetry install
```

5. Executando MkDocs
```bash
mkdocs serve
```

