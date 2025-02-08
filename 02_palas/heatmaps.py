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
from charset_normalizer import detect
import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Modelo de header dos arquivos
header = { 
    'Checksum Id Operacao': 0, 
    'Data do Inicio': 1, 
    'Data da Deflagracao': 2, 
    'Tipo de Operacao': 3, 
    'Area': 4, 
    'Sigla Unidade Federativa': 5, 
    'Sigla Unidade Institucional': 6, 
    'Atuacao em Territorio Indigena': 7, 
    'Atuacao em Territorio de Fronteira': 8, 
    'Qtd Prisao em Flagrante': 9, 
    'Qtd Prisao Preventiva': 10, 
    'Qtd Prisao Temporaria': 11, 
    'Qtd Mandado de Busca e Apreesao': 12, 
    'Qtd Valores Apreendidos': 13, 
    'Qtd Valores Apreendidos i11': 14, 
    'Qtd Valores Descapitalizados': 15, 
    'Qtd Prejuizos Causados a Uniao': 16, 
    'Proib Ausentar Comarca': 17, 
    'Proib Acesso ou Freq': 18, 
    'Comparecimento Juizo': 19, 
    'Qtd Fianca': 20, 
    'Qtd Internacao Prov': 21, 
    'Proib Contato': 22, 
    'Mand Jud Caut Assec': 23, 
    'Recol Domic Noturno': 24, 
    'Susp Ex Func Pub A E': 25, 
    'Monit Eletronica': 26
}

# Paths das planilhas originais
original_paths = [
    Path('02_palas/PALAS_OPERACOES_2021_01.csv'),
    Path('02_palas/PALAS_OPERACOES_2021_02.csv')
]

# List vazio para receber os paths das planilhas alteradas
new_paths = []

# Para cada planilha original
for path in original_paths:
    new_path = Path(path.parent / f"{path.stem}_mod{path.suffix}")
    # Só precisa criar arquivo se não já tiver sido criado
    if not new_path.is_file():
        print(f"Creating file {new_path}")
        # Detectar o encoding
        with open(path, 'rb') as f:
            result = detect(f.read())
            detected_encoding = result['encoding']

        # Booleana que decide se o arquivo deve ser escrito:
        should_save = True
        # Abra o arquivo original
        with open(path, mode='r', newline='', encoding=detected_encoding) as infile:
            # Leia o arquivo com seu delimitador original
            csv_reader = csv.reader(infile, delimiter=';')
            # Crie o path do arquivo alterado
            # Crie o arquivo alterado
            with open(new_path, mode='w', newline='', encoding='utf-8') as outfile:
                # Crie o writer
                csv_writer = csv.writer(outfile, delimiter=',')
                # Para cada linha do original, escreva-o no alterado
                for index, row in enumerate(csv_reader):
                    # Removendo o trailing whitespace
                    cleaned_row = [cell.strip() for cell in row]
                    # Vendo se as headers são todas iguais
                    if index == 0:
                        file_header = row
                        for cell in row:
                            if not header[cell]:
                                print(f"A coluna {cell} não foi encontrada no arquivo {new_path}. O mesmo será ignorado.")
                            else:
                                csv_writer.writerow(cleaned_row)

                # Salve o novo path na lista de novos paths
                new_paths.append(new_path)
    else:
        # Se já há arquivo, apenas avisa
        print(f"File {new_path} already created")


# # Juntar as planilhas
# with open('02_palas/combined_files.csv', mode='w', newline='', encoding='utf-8') as outfile:
#     linewriter = csv.writer(outfile, delimiter=',')

#     # Loopando por todos os arquivos e salvando o index
#     for index, file in enumerate(new_paths):
#         # Abrindo cada arquivo csv
#         with open(file, mode='r', newline='', encoding='utf-8') as infile:
#             linereader = csv.reader(infile, delimiter=',')

#             if index == 0:
#                 linewriter.writerow(next(linereader))
#                 linewriter.writerows(linereader)
#             else:
#                 next(linereader)
#                 linewriter.writerows(linereader)


# # Carregar os dados

# for path in new_paths:
#     df1 = pd.read_csv(pt1)
# df2 = pd.read_csv(pt2)
# df = pd.concat([df1, df2])
# print(df.head())

# # Categorizando Tipo de Operação
# # print(df["Tipo de Operacao"].nunique()) # Número de unique values
# # print(df["Tipo de Operacao"].unique()) # Unique values themselves

# tipo_operacao = {
#     "Operacao Simples": 0,
#     "Operacao Comum": 1,
#     "Operacao de Apoio": 2,
#     "Operacao Especial": 3
# }

# df['Tipo de Operacao'] = df['Tipo de Operacao'].map(tipo_operacao)

# # Categorizando a Área
# # print(df["Area"].unique()) # Número de unique values

# area = {
#     'Tráfico de Drogas': 0,
#     'Crimes Fazendários': 1,
#     'Crimes Ambientais e Contra o Patrimônio Cultural': 2,
#     'Crimes Contra o Patrimônio': 3,
#     'Crimes de Corrupção': 4,
#     'Crimes Eleitorais': 5,
#     'Crimes Previdenciários': 6,
#     'Crimes Contra Direitos Humanos': 7,
#     'Crimes de Ódio e Pornografia Infantil': 8,
#     'Crimes Financeiros': 9,
#     'Assuntos Internos': 10
# }
# df['Area'] = df['Area'].map(area)

# # Categorizando Unidades Federativas
# # print(df['Sigla Unidade Federativa'].unique())

# uf = {
#     'AC': 0,
#     'AL': 1,
#     'AM': 2,
#     'AP': 3,
#     'BA': 4,
#     'CE': 5,
#     'DF': 6,
#     'ES': 7,
#     'GO': 8,
#     'MA': 9,
#     'MG': 10,
#     'MS': 11,
#     'MT': 12,
#     'PA': 13,
#     'PB': 14,
#     'PE': 15,
#     'PI': 16,
#     'PR': 17,
#     'RJ': 18,
#     'RN': 19,
#     'RO': 20,
#     'RR': 21,
#     'RS': 22,
#     'SC': 23,
#     'SE': 24,
#     'SP': 25,
#     'TO': 26
# }
# df['Sigla Unidade Federativa'] = df['Sigla Unidade Federativa'].map(uf)

# # Categorizando Atuacao em Territorio Indigena

# terr_ind = {
#     "Nao": 0,
#     "Sim": 1
# }

# df['Atuacao em Territorio Indigena'] = df['Atuacao em Territorio Indigena'].map(terr_ind)
# # print(df['Atuacao em Territorio Indigena'])

# # Categorizando paises (Atuacao em Territorio de Fronteira)
# # print(df['Atuacao em Territorio de Fronteira'].unique())

# front = {
#     np.nan : 0,
#     'Argentina': 1,
#     'Bolívia': 2,
#     'Colômbia': 3,
#     'Guiana': 4,
#     'Guiana Francesa': 5,
#     'Paraguai': 6,
#     'Peru': 7,
#     'Uruguai': 8,
#     'Venezuela': 9
# }
# df['Atuacao em Territorio de Fronteira'] = df['Atuacao em Territorio de Fronteira'].map(front)
# # print(df['Atuacao em Territorio de Fronteira'])

# # Corrigindo o campo "Qtd Valores Apreendidos i11"
# df['Qtd Valores Apreendidos i11'] = df['Qtd Valores Apreendidos i11'].replace(np.nan, '0.0')
# df['Qtd Valores Apreendidos i11'] = df['Qtd Valores Apreendidos i11'].str.replace('R$', '')
# df['Qtd Valores Apreendidos i11'] = df['Qtd Valores Apreendidos i11'].str.replace('.', '')
# df['Qtd Valores Apreendidos i11'] = df['Qtd Valores Apreendidos i11'].str.replace(',', '.')
# df['Qtd Valores Apreendidos i11'] = df['Qtd Valores Apreendidos i11'].astype('float')
# # print(df['Qtd Valores Apreendidos i11'])

# # Corrigindo o campo "Qtd Prejuizos Causados a Uniao"
# df['Qtd Prejuizos Causados a Uniao'] = df['Qtd Prejuizos Causados a Uniao'].replace(np.nan, '0.0')
# df['Qtd Prejuizos Causados a Uniao'] = df['Qtd Prejuizos Causados a Uniao'].str.replace('R$', '')
# df['Qtd Prejuizos Causados a Uniao'] = df['Qtd Prejuizos Causados a Uniao'].str.replace('.', '')
# df['Qtd Prejuizos Causados a Uniao'] = df['Qtd Prejuizos Causados a Uniao'].str.replace(',', '.')
# df['Qtd Prejuizos Causados a Uniao'] = df['Qtd Prejuizos Causados a Uniao'].astype('float')
# print(df['Qtd Prejuizos Causados a Uniao'])

# # Datas para timestamp
# df['Data Inicio'] = pd.to_datetime(df['Data do Inicio'], format='mixed')
# df['Data Inicio'] = df['Data Inicio'].astype('int64') // 10**9
# df['Data Deflagracao'] = pd.to_datetime(df['Data da Deflagracao'], format='mixed')
# df['Data Deflagracao'] = df['Data Deflagracao'].astype('int64') // 10**9

# # Criar os dados para o heatmap
# heat_data = df.drop(columns=[
#     'Checksum Id Operacao',
#     'Data do Inicio',
#     'Data da Deflagracao',
#     'Sigla Unidade Institucional'
# ])

# # Montar o heatmap
# plt.figure(figsize=(16,12))
# sns.heatmap(heat_data.corr(), annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
# plt.xticks(rotation=45, ha='right')
# plt.yticks(rotation=0)
# plt.title('Heatmap de Correlação das Features')
# plt.tight_layout()
# plt.savefig('02_palas/heatmap.png')
