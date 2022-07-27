#!/usr/bin/env python
# coding: utf-8

# # Importando Bibliotecas
# ---

# In[2]:


import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ##  Gráficos de Dispersão
# ---

# In[3]:


dados = pd.read_csv('iris.csv')
dados.head()


# In[5]:


fig = plt.figure(figsize=(15,8))                             #Grafico basico com apenas a dispersão 
eixo = fig.add_axes([0,0,1,1])

eixo.scatter(dados ['comprimento_sépala'], dados ['largura_sépala'])
eixo.set_title('Gráfico de dispersão', fontsize=25, pad=15)
eixo.set_xlabel('Comprimento da sépala', fontsize=15)
eixo.set_ylabel('Largura da sépala', fontsize=15)
eixo.tick_params(labelsize=15)


# In[8]:


fig = plt.figure(figsize=(15,8))                                    #Inclui um dicionario de cores para ficar mais facil a visualização
eixo = fig.add_axes([0,0,1,1])

cores = {'Iris-setosa': 'r', 'Iris-versicolor': 'b', 'Iris-virginica': 'g'}

for especie in dados['espécie'].unique():
    tmp = dados[dados['espécie'] == especie]
    eixo.scatter(tmp['comprimento_sépala'], tmp['largura_sépala'],
                 color=cores[especie])

eixo.set_title('Gráfico de dispersão', fontsize=25, pad=15)
eixo.set_xlabel('Comprimento da sépala', fontsize=15)
eixo.set_ylabel('Largura da sépala', fontsize=15)
eixo.tick_params(labelsize=15)


# In[13]:


fig = plt.figure(figsize=(15,8))                                     #Inclui um marcado no grafico e legendas para melhorar a leitura
eixo = fig.add_axes([0,0,1,1])

cores = {'Iris-setosa': 'r', 'Iris-versicolor': 'b', 'Iris-virginica': 'g'}
marcadores = {'Iris-setosa': 'x', 'Iris-versicolor': 'o', 'Iris-virginica': 'v'}

for especie in dados['espécie'].unique():
    tmp = dados[dados['espécie'] == especie]
    eixo.scatter(tmp['comprimento_sépala'], tmp['largura_sépala'],
                 color=cores[especie], marker=marcadores[especie],
                 s=100)

eixo.set_title('Gráfico de dispersão', fontsize=25, pad=15)
eixo.set_xlabel('Comprimento da sépala', fontsize=15)
eixo.set_ylabel('Largura da sépala', fontsize=15)
eixo.tick_params(labelsize=15)

eixo.legend(cores, fontsize=20)


# ### Distribuição dos dados com box-plot
# ---

# In[15]:


fig = plt.figure(figsize=(5,4))                      #boxplot representando os quartis desse conjunto
eixo = fig.add_axes([0,0,1,1])

eixo.boxplot(dados['largura_pétala'])
eixo.set_title('Gráfico de caixa', fontsize=15, pad=10)
eixo.set_xticklabels(['largura_pétala'])


# In[17]:


fig = plt.figure(figsize=(5,4))            #Plotei mais variaveis e ajudei comprimento de sépala e largura de sépala
eixo = fig.add_axes([0,0,1,1])

eixo.boxplot(dados.drop('espécie', axis=1))
eixo.set_title('Gráfico de caixa', fontsize=15, pad=10)
eixo.set_xticklabels(dados.drop('espécie', axis=1).columns)


# In[18]:


fig = plt.figure(figsize=(8,5))                       #Inclui cores nas caixas para melhor visualização
eixo = fig.add_axes([0,0,1,1])

cores = ['red', 'blue', 'orange', 'green']

caixas = eixo.boxplot(dados.drop('espécie', axis=1).values, patch_artist=True)
eixo.set_title('Gráfico de caixa', fontsize=15, pad=10)
eixo.set_xticklabels(dados.drop('espécie', axis=1).columns)

for caixa, cor in zip(caixas['boxes'], cores):
    caixa.set(color=cor)

for outlier in caixas['fliers']:
    outlier.set(marker='x', markersize=8)


# ### Mais formas de visualizar a distribuição de dados
# ---

# In[19]:


fig = plt.figure(figsize=(5,4))                         #Histograma com comprimento da pétala
eixo = fig.add_axes([0,0,1,1]) 

eixo.hist(dados['comprimento_pétala'])
eixo.set_title('Histograma', fontsize=15, pad=10)
eixo.set_xlabel('Comprimento da pétala', fontsize=15)
eixo.grid(True)


# In[20]:


fig = plt.figure(figsize=(5,4))                             #Normalizei a distribuicao
eixo = fig.add_axes([0,0,1,1])

eixo.hist(dados['comprimento_pétala'], bins=20, density=True)
eixo.set_title('Histograma', fontsize=15, pad=10)
eixo.set_xlabel('Comprimento da pétala', fontsize=15)
eixo.grid(True)


# In[22]:


fig = plt.figure(figsize=(5,4))                   #Inclui media, media no grafico de histograma
eixo = fig.add_axes([0,0,1,1])

mu, sigma = dados['comprimento_pétala'].mean(), dados['comprimento_pétala'].std()

eixo.hist(dados['comprimento_pétala'], bins=20)
eixo.set_title('Histograma', fontsize=15, pad=10)
eixo.set_xlabel('Comprimento da pétala', fontsize=15)
eixo.grid(True)

eixo.annotate('$\mu = {0:.2f}$\n$\sigma = {1:.2f}$'.format(mu, sigma),
               xy=(4.5, 20), fontsize=20)

eixo.axvline(mu, color = 'k', linestyle='--')
eixo.annotate('média', xy=(mu-1.3, 28), fontsize=20)

eixo.axvline(dados['comprimento_pétala'].median(), color='g', linestyle='--')
eixo.annotate('mediana', xy=(dados['comprimento_pétala'].median(), 31), fontsize=20)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




