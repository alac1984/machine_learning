"""
Nesse script eu produzi heatmaps para dados
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from pathlib import Path
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Carregar os dados
pt = Path('02_palas/PALAS_OPERACOES_2021_01.csv')
df = pd.read_csv(pt)

# Categorizando Tipo de Operação
# print(df["Tipo de Operacao"].nunique()) # Número de unique values
# print(df["Tipo de Operacao"].unique()) # Unique values themselves

tipo_operacao = {
    "Operacao Simples": 0,
    "Operacao Comum": 1,
    "Operacao de Apoio": 2,
    "Operacao Especial": 3
}

df['Tipo de Operacao'] = df['Tipo de Operacao'].map(tipo_operacao)

# Categorizando a Área
# print(df["Area"].unique()) # Número de unique values

area = {
    'Tráfico de Drogas': 0,
    'Crimes Fazendários': 1,
    'Crimes Ambientais e Contra o Patrimônio Cultural': 2,
    'Crimes Contra o Patrimônio': 3,
    'Crimes de Corrupção': 4,
    'Crimes Eleitorais': 5,
    'Crimes Previdenciários': 6,
    'Crimes Contra Direitos Humanos': 7,
    'Crimes de Ódio e Pornografia Infantil': 8,
    'Crimes Financeiros': 9,
    'Assuntos Internos': 10
}
df['Area'] = df['Area'].map(area)

# Categorizando Unidades Federativas
# print(df['Sigla Unidade Federativa'].unique())

uf = {
    'AC': 0,
    'AL': 1,
    'AM': 2,
    'AP': 3,
    'BA': 4,
    'CE': 5,
    'DF': 6,
    'ES': 7,
    'GO': 8,
    'MA': 9,
    'MG': 10,
    'MS': 11,
    'MT': 12,
    'PA': 13,
    'PB': 14,
    'PE': 15,
    'PI': 16,
    'PR': 17,
    'RJ': 18,
    'RN': 19,
    'RO': 20,
    'RR': 21,
    'RS': 22,
    'SC': 23,
    'SE': 24,
    'SP': 25,
    'TO': 26
}
df['Sigla Unidade Federativa'] = df['Sigla Unidade Federativa'].map(uf)

# Categorizando paises (Atuacao em Territorio de Fronteira)
# print(df['Atuacao em Territorio de Fronteira'].unique())

front = {
    np.nan : 0,
    'Argentina': 1,
    'Bolívia': 2,
    'Colômbia': 3,
    'Guiana': 4,
    'Guiana Francesa': 5,
    'Paraguai': 6,
    'Peru': 7,
    'Uruguai': 8,
    'Venezuela': 9
}
df['Atuacao em Territorio de Fronteira'] = df['Atuacao em Territorio de Fronteira'].map(front)
print(df['Atuacao em Territorio de Fronteira'])

# Datas para timestamp
df['Data Inicio'] = pd.to_datetime(df['Data do Inicio'], format='mixed')
df['Data Inicio'] = df['Data Inicio'].astype('int64') // 10**9
df['Data Deflagracao'] = pd.to_datetime(df['Data da Deflagracao'], format='mixed')
df['Data Deflagracao'] = df['Data Deflagracao'].astype('int64') // 10**9

# Criar os dados para o heatmap
heat_data = df.drop(columns=[
    'Checksum Id Operacao',
    'Data do Inicio',
    'Data da Deflagracao',
    'Sigla Unidade Institucional'
])

# Montar o heatmap
plt.figure(figsize=(12,10))
sns.heatmap(heat_data.corr(), annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.title('Heatmap de Correlação das Features')
plt.tight_layout()
plt.savefig('02_palas/heatmap.png')
