"""
heatmaps.py

This script is part of the '03_palas' folder, initially intended to create a model
capable of predicting which type of Brazilian Federal Police operation would be triggered,
using public data from the PALAS (Investigation Information System). However, upon
analyzing the generated heatmaps, it became apparent that most features did not
vary significantly with the target variable, leading to a pause in the approach.
The script mainly demonstrates how to generate heatmaps to visualize feature
correlations. Future refinements may involve adding more relevant variables or
tuning feature engineering steps.

Usage:
  1. Adjust the paths in 'original_paths' to point to the correct CSV files.
  2. Run the script to:
     - Detect file encodings.
     - Optionally convert and combine CSV files for further processing.
     - Generate and save a heatmap (if uncommented).
  3. Customize the commented-out sections to suit data cleaning or feature encoding needs.

Dependencies:
  - Python 3.x
  - pandas
  - seaborn
  - matplotlib
  - scikit-learn
  - charset_normalizer

Author:
  [Your Name or Organization]

License:
  [Optional: Specify License]
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

# File header template
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

# Paths to the original spreadsheets
original_paths = [
    Path('02_palas/PALAS_OPERACOES_2021_01.csv'),
    Path('02_palas/PALAS_OPERACOES_2021_02.csv')
]

# Empty list to store the paths of the modified spreadsheets
new_paths = []

# For each original spreadsheet
for path in original_paths:
    new_path = Path(path.parent / f"{path.stem}_mod{path.suffix}")
    # Only create a file if it hasn't been created yet
    if not new_path.is_file():
        print(f"Creating file {new_path}")
        # Detect encoding
        with open(path, 'rb') as f:
            result = detect(f.read())
            detected_encoding = result['encoding']

        # Boolean deciding whether the file should be written
        should_save = True
        # Open the original file
        with open(path, mode='r', newline='', encoding=detected_encoding) as infile:
            # Read the file with its original delimiter
            csv_reader = csv.reader(infile, delimiter=';')
            # Create the path for the modified file
            # Create the modified file
            with open(new_path, mode='w', newline='', encoding='utf-8') as outfile:
                # Create the writer
                csv_writer = csv.writer(outfile, delimiter=',')
                # For each line in the original, write it to the modified one
                for index, row in enumerate(csv_reader):
                    # Removing trailing whitespace
                    cleaned_row = [cell.strip() for cell in row]
                    # Checking if all headers match
                    if index == 0:
                        file_header = row
                        for cell in row:
                            if not header.get(cell):
                                print(f"Column {cell} was not found in the file {new_path}. This file will be ignored.")
                            else:
                                csv_writer.writerow(cleaned_row)

                # Save the new path in the list of new paths
                new_paths.append(new_path)
    else:
        # If the file already exists, just notify
        print(f"File {new_path} already created")


# # Combine the spreadsheets
# with open('02_palas/combined_files.csv', mode='w', newline='', encoding='utf-8') as outfile:
#     linewriter = csv.writer(outfile, delimiter=',')
#     # Loop over all files and save the index
#     for index, file in enumerate(new_paths):
#         # Opening each CSV file
#         with open(file, mode='r', newline='', encoding='utf-8') as infile:
#             linereader = csv.reader(infile, delimiter=',')
#             if index == 0:
#                 linewriter.writerow(next(linereader))
#                 linewriter.writerows(linereader)
#             else:
#                 next(linereader)
#                 linewriter.writerows(linereader)

# # Load the data
# for path in new_paths:
#     df1 = pd.read_csv(pt1)
# df2 = pd.read_csv(pt2)
# df = pd.concat([df1, df2])
# print(df.head())

# # Categorizing Operation Type
# # print(df["Tipo de Operacao"].nunique())  # Number of unique values
# # print(df["Tipo de Operacao"].unique())   # Unique values themselves
# tipo_operacao = {
#     "Operacao Simples": 0,
#     "Operacao Comum": 1,
#     "Operacao de Apoio": 2,
#     "Operacao Especial": 3
# }
# df['Tipo de Operacao'] = df['Tipo de Operacao'].map(tipo_operacao)

# # Categorizing the Area
# # print(df["Area"].unique())
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

# # Categorizing Federative Units
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

# # Categorizing Indigenous Territory Activity
# terr_ind = {
#     "Nao": 0,
#     "Sim": 1
# }
# df['Atuacao em Territorio Indigena'] = df['Atuacao em Territorio Indigena'].map(terr_ind)

# # Categorizing countries (Frontier Territory Activity)
# # print(df['Atuacao em Territorio de Fronteira'].unique())
# front = {
#     np.nan: 0,
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

# # Fixing the 'Qtd Valores Apreendidos i11' field
# df['Qtd Valores Apreendidos i11'] = df['Qtd Valores Apreendidos i11'].replace(np.nan, '0.0')
# df['Qtd Valores Apreendidos i11'] = df['Qtd Valores Apreendidos i11'].str.replace('R$', '')
# df['Qtd Valores Apreendidos i11'] = df['Qtd Valores Apreendidos i11'].str.replace('.', '')
# df['Qtd Valores Apreendidos i11'] = df['Qtd Valores Apreendidos i11'].str.replace(',', '.')
# df['Qtd Valores Apreendidos i11'] = df['Qtd Valores Apreendidos i11'].astype('float')

# # Fixing the 'Qtd Prejuizos Causados a Uniao' field
# df['Qtd Prejuizos Causados a Uniao'] = df['Qtd Prejuizos Causados a Uniao'].replace(np.nan, '0.0')
# df['Qtd Prejuizos Causados a Uniao'] = df['Qtd Prejuizos Causados a Uniao'].str.replace('R$', '')
# df['Qtd Prejuizos Causados a Uniao'] = df['Qtd Prejuizos Causados a Uniao'].str.replace('.', '')
# df['Qtd Prejuizos Causados a Uniao'] = df['Qtd Prejuizos Causados a Uniao'].str.replace(',', '.')
# df['Qtd Prejuizos Causados a Uniao'] = df['Qtd Prejuizos Causados a Uniao'].astype('float')
# print(df['Qtd Prejuizos Causados a Uniao'])

# # Converting dates to timestamps
# df['Data Inicio'] = pd.to_datetime(df['Data do Inicio'], format='mixed')
# df['Data Inicio'] = df['Data Inicio'].astype('int64') // 10**9
# df['Data Deflagracao'] = pd.to_datetime(df['Data da Deflagracao'], format='mixed')
# df['Data Deflagracao'] = df['Data Deflagracao'].astype('int64') // 10**9

# # Create the data for the heatmap
# heat_data = df.drop(columns=[
#     'Checksum Id Operacao',
#     'Data do Inicio',
#     'Data da Deflagracao',
#     'Sigla Unidade Institucional'
# ])

# # Build the heatmap
# plt.figure(figsize=(16,12))
# sns.heatmap(heat_data.corr(), annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
# plt.xticks(rotation=45, ha='right')
# plt.yticks(rotation=0)
# plt.title('Heatmap of Feature Correlations')
# plt.tight_layout()
# plt.savefig('02_palas/heatmap.png')
