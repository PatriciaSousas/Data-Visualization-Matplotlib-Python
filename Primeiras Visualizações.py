

## Carregando Bibliotecas
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""## Primeiras Visualizações """

dados = pd.read_csv('monitoramento_tempo.csv')                  #Carrego meu dataset
dados

dados.info()                                                  #Aqui eu vejo os dados que eu estou trabalhando e vejo que data esta como objeto, preciso configurar para que fique com data

dados['data']= pd.to_datetime(dados['data'])                #transformo a coluna data

plt.figure(figsize=(15,8))
plt.plot(dados['data'], dados['temperatura'])  
plt.title('Temperatura do tempo')                       #Variação entre a data e a temperatura





















