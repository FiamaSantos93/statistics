# -*- coding: utf-8 -*-
"""aulao grande - aula 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10b9mvFFD4eLjV74Tts8vMswGpk0iEbcI

**Bibliotecas**
"""

import numpy as np
import pandas as pd



"""Carregar Dados"""

dados = pd.read_csv('dados_1997_2011_paises_csv.csv',encoding = 'latin1', sep = ';',decimal = ',')

dados

type(dados)

dados.dtypes



"""# comandos básicos para dataframe"""

dados.head(2) #para ver as primeiras linhas

dados.tail(3) #para ver as 3 últimas

"""# Colunas"""

# somente nome das colunas
dados.columns

# trocar nome coluna

dados2 = dados.rename(columns= {'populacao':'pop'})

dados2  # não use a mesma tabela caso vá utilizar os mesmos dados, então neste caso foi criado a dados2 e renomeado as colunas

dados2.columns

#filtrar coluna 1

dados2['pais']

#filtrar mais de uma coluna - forma 1

dados2[['ano','pais','idh']].head(2)

#filtrar mais de uma coluna - forma 2

cols = ['ano', 'pais', 'idh']
dados2[cols].head(2)

#ver as linhas de qualquer posição

dados.iloc[3:7]

#ver as linhas de qualquer posição

dados.iloc[3:7] ['ano'] #caso de achar a coluna

#como criar uma coluna

dados2['idh_perc'] = dados2['idh'] * 100
dados2.columns

dados2.head(2)

#como criar uma coluna nova - forma2

dados2['log_pop'] = dados2['pop'].apply(lambda x: np.log(x))
dados2.head(2)

#como aplicar a mesma função em mais de uma coluna nova

dados2[['log_pop', 'log_pib']] = dados2[['pop', 'pib']].apply(lambda x: np.log(x))
dados2.head(2)

"""# **Filtros**"""

dados2['pais'].unique() #ver como está escrito nas colunas // VAI CAIR NA ATIVIDADEEEEEE //

#Contagem // VAI CAIR NO CHECKPOINT TAMBÉM

len(dados['pais'].unique())

#filtrar textos - formas 1

dados2[dados2['pais'] == 'Brasil']

# Filtrar texto - forma2

dados2[dados2['pais'].str.contains('Br')]

# Filtragem de números

dados2[dados2['idh'] > 0.8]   # podendo usar > < == >= <=

# Filtrar lista de valores
lista_paises = ['Brasil', 'Alemanha', 'China']
dados2[dados2['pais'].isin(lista_paises)]

# Filtrar excluindo da lista de valores
lista_paises = ['Brasil', 'Alemanha', 'China']
dados2[~dados2['pais'].isin(lista_paises)]

#Filtrar maais de uma coluna

dados2[(dados2['pais'] == 'Brasil') & (dados2['ano'] == 2011)]

"""# Ordenar Valores"""

dados2.sort_values('idh', ascending = False)  #ascending False sendo que coloca em ordem crescente e True para descrecente

"""# Agregar Valores"""

#forma direta

dados2['pop'].sum()

#forma direta com agrupamento de columa

dados2.groupby('pais')['idh'].mean()   #mean é a média

# agregar colunas diferentes

dados2.groupby('pais') \
    .agg(total_pop = pd.NamedAgg('pop', 'sum'),
        media_idh = pd.NamedAgg('idh', 'mean'))



"""# Graficos"""

import matplotlib.pyplot as plt

# grafico de linhas

dados_brasil = dados2[dados2['pais'] == 'Brasil']

plt.plot(dados_brasil['ano'], dados_brasil['idh'])

plt.bar(dados_brasil['ano'], dados_brasil['idh'])