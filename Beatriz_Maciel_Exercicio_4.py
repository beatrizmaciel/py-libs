# Escreva um programa que leia uma série de dados temporais diários de um arquivo (sobre qualquer assunto – livre escolha) 
# e plote um gráfico contendo a quantidade de ocorrências diárias e a sua média móvel nos últimos cinco dias

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./database/dados_cronicas_ses_2023.csv', sep=';', parse_dates=['dt_obito'], dayfirst=True)

df['dt_obito'] = pd.to_datetime(df['dt_obito']) # converter para o formato certo de data

ocorrencias_por_dia = df.groupby(df['dt_obito'].dt.date).size() # conta ocorrências por dia

media_movel = ocorrencias_por_dia.rolling(window=5).mean()

ultimos_cinco_dias = ocorrencias_por_dia.tail(5)
media_movel_ultimos_cinco_dias = media_movel.tail(5)

print("» Número de ocorrências por dia:")
print(ocorrencias_por_dia)
print(type(ocorrencias_por_dia))
print("» Média móvel dos últimos 5 dias:")
print(media_movel_ultimos_cinco_dias)
print(type(media_movel_ultimos_cinco_dias))

plt.bar(ultimos_cinco_dias.index, ultimos_cinco_dias.values, color='blue', label='Ocorrências de Mortes Diárias')
plt.plot(media_movel_ultimos_cinco_dias.index, media_movel_ultimos_cinco_dias.values, color='red', label='Média Móvel')

plt.show()