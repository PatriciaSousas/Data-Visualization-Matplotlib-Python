#!/usr/bin/env python
# coding: utf-8

# # Importando Bibliotecas
# ---

# In[14]:


import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ##  Primeiras visualizações dos dados 
# ---

# In[5]:


dados = pd.read_csv('monitoramento_tempo.csv')
dados.head


# In[33]:


dados['data'] = pd.to_datetime(dados['data'])  #Caregando do dataset e a tranformação da coluna data de str para data 


# In[9]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0, 0, 1, 1])
eixo.plot(dados['data'], dados['temperatura'])

eixo.set_title('Temperatura no momento')


# In[12]:


fig = plt.figure(figsize=(15,8))                                #inclui mais alguns detalhes no grafico
eixo = fig.add_axes([0, 0, 1, 1])
eixo.plot(dados['data'], dados['temperatura'], color= 'indigo')  

eixo.set_title('Temperatura no momento', fontsize=25)
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize=15)


# ## Espessura, estilo, foco, marcadores e grades
# ---

# In[16]:


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0, 0, 1, 1])
eixo.plot(dados['data'], dados['temperatura'], color = 'orange')

eixo.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1))
eixo.set_title('Temperatura no momento', fontsize=25)
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize=15)
eixo.grid(True)


# ## Visualização com foco no ano de 2014 no canto superior do grafico 
# ---

# In[22]:


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])
eixo2 = fig.add_axes([0.7, 0.65, 0.3, 0.3])

eixo.grid(True)
eixo.plot(dados['data'], dados['temperatura'], color = 'orange')
eixo.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1))
eixo.set_title('Temperatura em 2014', fontsize=25, pad=20)
eixo.legend(['temperatura'], loc='lower right', fontsize=15)
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)

eixo2.plot(dados['data'], dados['temperatura'], color = 'blue')
eixo2.set_title('Temperatura no momento', fontsize=15)
eixo2.legend(['temperatura'], loc='best', fontsize=8)
eixo2.set_ylabel('Temperatura', fontsize=10)
eixo2.set_xlabel('Data', fontsize=10)
eixo2.grid(True)


# ## Visualização com foco no ano de 20122- 2018 no canto superior do grafico 
# ---

# In[32]:


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0,0,1,1])
eixo2 = fig.add_axes([0.7,0.65,0.3,0.3])

eixo.grid(True)
eixo.plot(dados['data'], dados['temperatura'], color = 'g')
eixo.set_xlim(datetime.datetime(2014,1,1), datetime.datetime(2015,1,1))
eixo.set_title('Temperatura em 2014', fontsize=25, pad = 20)
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize= 15)

eixo2.plot(dados['data'], dados['temperatura'], color = 'b')
eixo2.legend(['Temperatura'], loc = 'lower right') 
eixo2.set_title('Temperatura 2012-2018', fontsize=15)


# ## Quero sinaliza no grafíco o maxímo e a minima que a temperatura pode chegar 
# ---

# In[40]:


fig = plt.figure(figsize = (15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(dados['data'], dados['temperatura'], color = 'pink')
eixo.set_title('Temperatura no momento', fontsize = 25, pad = 20)
eixo.set_xlabel('Data', fontsize=20)
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.legend(['Temperatura'], loc='lower right', fontsize=15)
eixo.grid(True)

eixo.axhline(max(dados['temperatura']), color = 'k', linestyle='--')
eixo.axhline(min(dados['temperatura']), color = 'k', linestyle='--')


x1 = dados['data'][dados['temperatura'].idxmax()]
y1 = max(dados['temperatura'])

x2 = dados['data'][dados['temperatura'].idxmax() - 7000]
y2 = max(dados['temperatura']) - 5

eixo.annotate('Máximo', xy=(x1,y1), fontsize=20, 
              xytext=(x2,y2), arrowprops=dict(facecolor='k'))

x1 = dados['data'][dados['temperatura'].idxmin()]
y1 = min(dados['temperatura'])

x2 = dados['data'][dados['temperatura'].idxmin() - 7000]
y2 = min(dados['temperatura']) + 5

eixo.annotate('Mínimo', xy=(x1,y1), fontsize=20, 
              xytext=(x2,y2), arrowprops=dict(facecolor='k'))


# ## Quero entender se tem dias da semana mais quentes ou mais frios e quais são?
# ----

# In[41]:


temperatura_por_dia_da_semana = dados.groupby('dia_da_semana')['temperatura'].mean() #media dos valores
temperatura_por_dia_da_semana 


# In[42]:


temperatura_por_dia_da_semana = dados.groupby('dia_da_semana')['temperatura'].mean()   #crio uma variavel contendo uma lista de dias
nome_dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
temperatura_por_dia_da_semana = temperatura_por_dia_da_semana[nome_dias]
temperatura_por_dia_da_semana


# In[49]:


fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])
indice = range(len(temperatura_por_dia_da_semana))

indice = range(len(temperatura_por_dia_da_semana))
cores = ['black', 'r', 'g', 'b', 'yellow', 'orange', 'magenta']

eixo.bar(indice, temperatura_por_dia_da_semana, color = cores, edgecolor= 'black')
eixo.set_title('Temperatura por dia da semana', fontsize=15, pad=10)
eixo.set_xlabel('Dia da semana', fontsize=15)
eixo.set_ylabel('Temperatura média', fontsize=15)
eixo.set_xticks(indice)
eixo.set_xticklabels(nome_dias)


# In[50]:


fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])

explodir = [1,0,0,0,0,1,1]

eixo.pie(temperatura_por_dia_da_semana, labels=temperatura_por_dia_da_semana.index,
         autopct='%.1f%%')
eixo.set_title('Temperatura por dia da semana', size=15, pad=10)


# In[51]:


fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])

explodir = [1,0,0,0,0,1,1]

eixo.pie(temperatura_por_dia_da_semana, labels=temperatura_por_dia_da_semana.index,
         autopct='%.1f%%', explode=explodir)
eixo.set_title('Temperatura por dia da semana', size=15, pad=10)


# In[53]:


fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])

explodir = [0.1,0,0,0,0,0.1,0.1]

eixo.pie(temperatura_por_dia_da_semana, labels=temperatura_por_dia_da_semana.index,
         autopct='%.1f%%', explode=explodir, shadow=True)
eixo.set_title('Temperatura por dia da semana', size=15, pad=10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




