import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
Unicórnio é o termo usado na indústria de capital de risco para descrever uma startup de capital fechado com valor duperior a US$1 bilhão. 

'''

# Define o backend para TkAgg
plt.switch_backend('TkAgg')

# Ler os dados
base_dados = pd.read_csv('Startups+in+2021+end.csv')

# Visualizar uma visão gráfica dos dados, como um mapa de calor para verificar valores nulos
sns.heatmap(base_dados.isnull())
plt.show()

print(base_dados)

plt.figure(figsize=(15, 6))
plt.title('Análise de setores')
base_dados['Industry'].value_counts().plot.bar()
plt.show()

#Análise geral de países: 

analise = round(base_dados['Country'].value_counts(normalize=True) * 100, 1)

plt.figure(figsize=(6, 6))
plt.title('Distribuição por país')
plt.pie(analise, labels=analise.index, startangle=90, autopct='%1.1f%%')
plt.show()

# Selecionar apenas os 10 primeiros países
top_10_paises = analise.head(10)

plt.figure(figsize=(6, 6))
plt.title('Top 10 países')
plt.pie(top_10_paises, labels=top_10_paises.index, startangle=90, autopct='%1.1f%%')
plt.show()

