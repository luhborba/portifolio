# Projeto 5DataGlowUP nº 25

**GitHub do Projeto:** [DataGlowUp5-LuhBorba](https://github.com/luhborba/dataglowup25)<br>
**Vídeo Explicativo** :video_camera: [Apresentando o Projeto - Youtube](https://www.youtube.com/watch?v=lRpkS6tVPAc&ab_channel=LucianoBorba)

## Stack do Projeto

- Python
- Pandas
- Matplotlib
- Numpy
- Jupyter Notebook
- Power Point

## Proposta do Projeto

O projeto tem como objetivo fazer uma análise exploratória dos dados de partidas de League of Legends, dados estes disponíveis no [Kaggle](https://www.kaggle.com/datasets/bobbyscience/league-of-legends-soloq-ranked-games/data) buscando focar não apenas nas tecnologias e funções utilizadas, mas também na apresentação simples e linguagem compatível com gestores, para fácil entendimento.

## Sumário do Código

1. Explorando Dados
2. Transformação de Dados
3. Analisando Dados

### 1- Explorando Dados

Antes de explorar os dados, utilizei uma célula exclusiva para importação de bibliotecas.
```
# Importando Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
```
Após importação das bibliotecas, fiz o carregamento dos dados, como também alguns opções para obter melhores informações:
```
# Carregando dados
df = pd.read_csv('lol_ranked_games.csv')
# Verificando 5 primeiras linhas
df.head()
# Verificando Schema
df.info()
# Verificando contagem de valores do gameId
contagem_gameId = df['gameId'].value_counts()
print(contagem_gameId)
```

### 2- Transformando Dados

Nesta etapa, primeiramente criei um campo de KDA, verificando a quantidade de assassinatos (Kills), assistências e mortes por jogo, considerando que caso a quantidade de mortes seja 0 não de nenhum error.
```
# Criando campo de KDA, Verificando se o número de mortes é igual a 0 para não criar valores com erro
df['kda'] = np.where(df['deaths'] == 0, (df['kills'] + df['assists']), (df['kills'] + df['assists']) /( df['deaths'] ))
```
Após criação, ajustei as casas decimais do novo campo criado
```
df['kda']  = df['kda'].round(2)
```
Posteriormente criei um novo DataFrame utilizando apenas as colunas que irei utilizar para retirar insights.
```
# Criando novo DF com dados que serão apenas utilizados
df_final = df[[
    'gameId',
    'hasWon',
    'goldDiff',
    'champLevelDiff',
    'isFirstTower',
    'isFirstBlood',
    'killedElderDrake',
    'killedBaronNashor',
    'kills',
    'deaths',
    'assists',
    'wardsPlaced',
    'wardsDestroyed',
    'wardsLost',
    'kda'
]]
```
### 3- Realizando Análises

#### 3.1 - Análises comparativas

Primeiramente criei um DataFrame para vitórias e outro para derrotas. Para fazer comparações de alguns dados.

```
# Filtrando o DataFrame para quando o time venceu (hasWon == 1)
vitorias = df_final[df_final['hasWon'] == 1]

# Filtrando o DataFrame para quando o time perdeu (hasWon == 0)
derrotas = df_final[df_final['hasWon'] == 0]
```

- Calculando comparativo de KDA:
```
media_kda_vitorias = vitorias['kda'].mean()
media_kda_derrotas = derrotas['kda'].mean()


# Exibindo os resultados
print("Média do KDA para vitórias:", media_kda_vitorias.round(2))
print("Média do KDA para derrotas:", media_kda_derrotas.round(2))
```
- Calculando comparativo de Wards Colocadas:

```
# Calculando a média de wardsPlaced para vitórias e derrotas
media_wardsPlaced_vitorias = vitorias['wardsPlaced'].mean()
media_wardsPlaced_derrotas = derrotas['wardsPlaced'].mean()

# Exibindo os resultados
print("Média de wardsPlaced para vitórias:", media_wardsPlaced_vitorias.round(2))
print("Média de wardsPlaced para derrotas:", media_wardsPlaced_derrotas.round(2))
```

- Calculando comparativo de Wards Destruídas:

```
# Calculando a média de wardsDestroyed para vitórias e derrotas
media_wardsDestroyed_vitorias = vitorias['wardsDestroyed'].mean()
media_wardsDestroyed_derrotas = derrotas['wardsDestroyed'].mean()

# Exibindo os resultados
print("Média de wardsDestroyed para vitórias:", media_wardsDestroyed_vitorias.round(2))
print("Média de wardsDestroyed para derrotas:", media_wardsDestroyed_derrotas.round(2))
```

- Calculando comparativo de Diferença de Gold:

```
# Calculando a média de goldDiff para vitórias e derrotas
media_goldDiff_vitorias = vitorias['goldDiff'].mean()
media_goldDiff_derrotas = derrotas['goldDiff'].mean()

# Exibindo os resultados
print("Média de goldDiff para vitórias:", media_goldDiff_vitorias.round(2))
print("Média de goldDiff para derrotas:", media_goldDiff_derrotas.round(2))
```

#### 3.2 - Análises Gerais

- **Calculando Chance de Vitória através do campo KDA:**<br><br>
Basicamente nesta etapa criei um variável de valor médio de kda, para assim calcular a probabilidade de vitória quando se esta acima do KDA médio.
```
# Calculando o valor médio do KDA
valor_medio_kda = df_final['kda'].mean()

# Filtrando as partidas que o KDA está acima da média
partidas_kda_maior_media = df_final[df_final['kda'] > valor_medio_kda]

# Contando o número de vitórias e derrotas nas partidas em que o KDA é acima da média
vitorias_kda_maior_media = partidas_kda_maior_media[partidas_kda_maior_media['hasWon'] == 1]
derrotas_kda_maior_media = partidas_kda_maior_media[partidas_kda_maior_media['hasWon'] == 0]

# Calculando a chance de vitória
chance_vitoria_kda_maior_media = len(vitorias_kda_maior_media) / len(partidas_kda_maior_media)

# Exibindo os resultados

print("Valor médio do KDA:", valor_medio_kda.round(2))
print('-----------------')
print("Número de partidas com KDA acima da média:", len(partidas_kda_maior_media))
print('-----------------')
print("Número de vitórias com KDA acima da média:", len(vitorias_kda_maior_media))
print('-----------------')
print("Número de derrotas com KDA acima da média:", len(derrotas_kda_maior_media))
print('-----------------')
print("Chance de vitória com KDA acima da média: {:.2f}".format(chance_vitoria_kda_maior_media))
```

- **Calculando Chance de Vitória através do campo WardsPlaced (Visões Colocadas)**:<br><br>
Basicamente nesta etapa criei um variável de valor médio de WardsPlaced, para assim calcular a probabilidade de vitória quando se esta acima do WardsPlaced médio.
```
# Calculando o valor médio de wardsPlaced
valor_medio_wardsPlaced = df_final['wardsPlaced'].mean()

# Filtrando as partidas em que wardsPlaced é acima da média
partidas_wardsPlaced_maior_media = df[df['wardsPlaced'] > valor_medio_wardsPlaced]

# Contando o número de vitórias e derrotas nas partidas em que wardsPlaced é acima da média
vitorias_wardsPlaced_maior_media = partidas_wardsPlaced_maior_media[partidas_wardsPlaced_maior_media['hasWon'] == 1]
derrotas_wardsPlaced_maior_media = partidas_wardsPlaced_maior_media[partidas_wardsPlaced_maior_media['hasWon'] == 0]

# Calculando a chance de vitória
chance_vitoria_wardsPlaced_maior_media = len(vitorias_wardsPlaced_maior_media) / len(partidas_wardsPlaced_maior_media)

# Exibindo valores
print("Valor médio de wardsPlaced:", valor_medio_wardsPlaced.round(2))
print('-----------------')
print("Número de partidas com wardsPlaced maior que a média:", len(partidas_wardsPlaced_maior_media))
print('-----------------')
print("Número de vitórias com wardsPlaced maior que a média:", len(vitorias_wardsPlaced_maior_media))
print('-----------------')
print("Número de derrotas com wardsPlaced maior que a média:", len(derrotas_wardsPlaced_maior_media))
print('-----------------')
print(f"Chance de vitória com wardsPlaced maior que a média: {chance_vitoria_wardsPlaced_maior_media:.2f}")
```

- **Calculando Chance de Vitória através do campo GoldDiff (Diferença de Ouro)**:<br><br>
Basicamente nesta etapa criei um variável de valor médio de GoldDiff, para assim calcular a probabilidade de vitória quando se esta acima do GoldDiff médio.
```
# Calculando o valor médio de goldDiff
valor_medio_goldDiff = df_final['goldDiff'].mean()

# Filtrando as partidas em que goldDiff é acima da média
partidas_goldDiff_maior_media = df[df['goldDiff'] > valor_medio_goldDiff]

# Contando o número de vitórias e derrotas nas partidas em que goldDiff é acima da média
vitorias_goldDiff_maior_media = partidas_goldDiff_maior_media[partidas_goldDiff_maior_media['hasWon'] == 1]
derrotas_goldDiff_maior_media = partidas_goldDiff_maior_media[partidas_goldDiff_maior_media['hasWon'] == 0]

# Calculando a chance de vitória
chance_vitoria_goldDiff_maior_media = len(vitorias_goldDiff_maior_media) / len(partidas_goldDiff_maior_media)

# Exibindo Valores
print("Valor médio de goldDiff:", valor_medio_goldDiff.round(2))
print('-----------------')
print("Número de partidas com goldDiff maior que a média:", len(partidas_goldDiff_maior_media))
print('-----------------')
print("Número de vitórias com goldDiff maior que a média:", len(vitorias_goldDiff_maior_media))
print('-----------------')
print("Número de derrotas com goldDiff maior que a média:", len(derrotas_goldDiff_maior_media))
print('-----------------')
print(f"Chance de vitória com goldDiff maior que a média: {chance_vitoria_goldDiff_maior_media:.2f}")
```

- **Calculando Chance de Vitória através do campo ChampLevelDiff (Diferença de Level)**:<br><br>
Basicamente nesta etapa criei um variável de valor médio de ChampLevelDiff, para assim calcular a probabilidade de vitória quando se esta acima do ChampLevelDiff médio.
```
# Calculando o valor médio de champLevelDiff
valor_medio_champLevelDiff = df_final['champLevelDiff'].mean()

# Filtrando as partidas em que champLevelDiff é acima da média
partidas_champLevelDiff_maior_media = df_final[df_final['champLevelDiff'] > valor_medio_champLevelDiff]

# Contando o número de vitórias e derrotas nas partidas em que champLevelDiff é acima da média
vitorias_champLevelDiff_maior_media = partidas_champLevelDiff_maior_media[partidas_champLevelDiff_maior_media['hasWon'] == 1]
derrotas_champLevelDiff_maior_media = partidas_champLevelDiff_maior_media[partidas_champLevelDiff_maior_media['hasWon'] == 0]

# Calculando a chance de vitória
chance_vitoria_champLevelDiff_maior_media = len(vitorias_champLevelDiff_maior_media) / len(partidas_champLevelDiff_maior_media)

# Exibindo Valores
print("Valor médio de champLevelDiff:", valor_medio_champLevelDiff.round(2))
print('-----------------')
print("Número de partidas com champLevelDiff maior que a média:", len(partidas_champLevelDiff_maior_media))
print('-----------------')
print("Número de vitórias com champLevelDiff maior que a média:", len(vitorias_champLevelDiff_maior_media))
print('-----------------')
print("Número de derrotas com champLevelDiff maior que a média:", len(derrotas_champLevelDiff_maior_media))
print('-----------------')
print(f"Chance de vitória com champLevelDiff maior que a média: {chance_vitoria_champLevelDiff_maior_media:.2f}")
```

- **Calculando Chance de Vitória através do campo isFirstTower (Primeira Torre)**:<br><br>
Basicamente nesta etapa criei um variável de verificando se o time vencedor obteve isFirstTower, para assim calcular a probabilidade de vitória esta condição é verdadeira.
```
# Filtrando as partidas em que isFirstTower foi derrubada
partidas_firstTower = df[df['isFirstTower'] == 1]

# Contando o número de vitórias e derrotas nas partidas em que isFirstTower foi derrubada
vitorias_firstTower = partidas_firstTower[partidas_firstTower['hasWon'] == 1]
derrotas_firstTower = partidas_firstTower[partidas_firstTower['hasWon'] == 0]

# Calculando a chance de vitória quando isFirstTower foi derrubada
chance_vitoria_firstTower = len(vitorias_firstTower) / len(partidas_firstTower)

print("Número de partidas em que isFirstTower é igual a 1:", len(partidas_firstTower))
print('-----------------')
print("Número de vitórias quando isFirstTower é igual a 1:", len(vitorias_firstTower))
print('-----------------')
print("Número de derrotas quando isFirstTower é igual a 1:", len(derrotas_firstTower))
print('-----------------')
print(f"Chance de vitória quando isFirstTower é igual a 1: {chance_vitoria_firstTower:.2f}")
```

- **Calculando Chance de Vitória através do campo isFirstBlood (Primeira Assassinato)**:<br><br>
Basicamente nesta etapa criei um variável de verificando se o time vencedor obteve isFirstBlood, para assim calcular a probabilidade de vitória esta condição é verdadeira.
```
# Filtrando as partidas em que isFirstBlood foi realizado
partidas_firstBlood = df[df['isFirstBlood'] == 1]

# Contar o número de vitórias e derrotas nas partidas em que isFirstBlood foi realizado
vitorias_firstBlood = partidas_firstBlood[partidas_firstBlood['hasWon'] == 1]
derrotas_firstBlood = partidas_firstBlood[partidas_firstBlood['hasWon'] == 0]

# Calcular a chance de vitória quando isFirstBlood foi realizado
chance_vitoria_firstBlood = len(vitorias_firstBlood) / len(partidas_firstBlood)

# Exibindo Resultados
print("Número de partidas em que isFirstBlood é igual a 1:", len(partidas_firstBlood))
print('-----------------')
print("Número de vitórias quando isFirstBlood é igual a 1:", len(vitorias_firstBlood))
print('-----------------')
print("Número de derrotas quando isFirstBlood é igual a 1:", len(derrotas_firstBlood))
print('-----------------')
print(f"Chance de vitória quando isFirstBlood é igual a 1: {chance_vitoria_firstBlood:.2f}")
```

- **Calculando Chance de Vitória através do campo killedElderDrake (Matou Dragão Ancião)**:<br><br>
Basicamente nesta etapa criei um variável de verificando se o time vencedor obteve killedElderDrake, para assim calcular a probabilidade de vitória esta condição é verdadeira.
```
# Filtrando as partidas em que Dragão Ancião foi Derrotado
partidas_elder_true = df_final[df_final['killedElderDrake'] == 1]

# Contando o número de vitórias e derrotas nas partidas em que Dragão Ancião foi Derrotado
vitorias_elder_true = partidas_elder_true[partidas_elder_true['hasWon'] == 1]
derrotas_elder_true = partidas_elder_true[partidas_elder_true['hasWon'] == 0]

# Calculando a chance de vitória quando Dragão Ancião foi Derrotado
chance_vitoria_elder_true = len(vitorias_elder_true) / len(partidas_elder_true)

# Exibindo Resultados
print("Número de partidas em que o Dragão Ancião foi Derrotado:", len(partidas_elder_true))
print('-----------------')
print("Número de vitórias quando o Dragão Ancião foi Derrotado:", len(vitorias_elder_true))
print('-----------------')
print("Número de derrotas quando o Dragão Ancião foi Derrotado:", len(derrotas_elder_true))
print('-----------------')
print(f"Chance de vitória quando o Dragão Ancião foi Derrotado: {chance_vitoria_elder_true:.2f}")
```

- **Calculando Chance de Vitória através do campo killedBaronNashor (Matou Baron Nashor)**:<br><br>
Basicamente nesta etapa criei um variável de verificando se o time vencedor obteve killedBaronNashor, para assim calcular a probabilidade de vitória esta condição é verdadeira.
```
# Filtrar as partidas em que Barão Nashor foi Derrotado
partidas_baron_true = df_final[df_final['killedBaronNashor'] == 1]

# Contando o número de vitórias e derrotas nas partidas em que Barão Nashor foi Derrotado
vitorias_baron_true = partidas_baron_true[partidas_baron_true['hasWon'] == 1]
derrotas_baron_true = partidas_baron_true[partidas_baron_true['hasWon'] == 0]

# Calculando a chance de vitória quando o Barão Nashor foi Derrotado
chance_vitoria_baron_true = len(vitorias_baron_true) / len(partidas_baron_true)

# Exibindo resultados
print("Número de partidas em que killedBaronNashor é True:", len(partidas_baron_true))
print('-----------------')
print("Número de vitórias quando killedBaronNashor é True:", len(vitorias_baron_true))
print('-----------------')
print("Número de derrotas quando killedBaronNashor é True:", len(derrotas_baron_true))
print('-----------------')
print(f"Chance de vitória quando killedBaronNashor é True: {chance_vitoria_baron_true:.2f}")
```

## Conclusão

Se você deseja avaliar melhor o código [clique aqui](https://github.com/luhborba/dataglowup25/blob/main/DadosLolzin.ipynb), se desejar assistir o vídeo de explicação dos resultados [clique aqui](https://www.youtube.com/watch?v=lRpkS6tVPAc). Ao ir para o vídeo me da uma moralzinha, curte, comenta o que você achou, se inscreve no canal e compartilha. Obrigado

![Vídeo](../assets/img/dgu25.png)