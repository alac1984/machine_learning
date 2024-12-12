"""
Nesse script trabalhamos com o dataset de diabetes "diabetes_data.csv", mantendo
sua coluna risk_score como contínua, e usamos então algumas técnicas para treinar
um modelo para dados contínuos (RandomForestRegressor) e avaliar a eficiência do
mesmo (mean_absolute_error, mean_squared_error, cross_val_score). Exploramos também
como "afinar" um modelo para conseguir um melhor desempenho. Com Seaborn fizemos
um heatmap pra ver quais features eram mais relevantes em relação a target.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


###########################
#### Carregar os dados ####
###########################

df = pd.read_csv('diabetes_data.csv')

#######################################################
#### Ver se a data é relevante em relação ao target ###
#######################################################

# # Criar os dados para o heatmap
# heat_data = df.drop(columns=['user_id'])
s
# # Preprocessar os dados de data (para evitar erros com datas em formato string)
# heat_data['year'] = pd.to_datetime(heat_data['date']).dt.year
# heat_data['month'] = pd.to_datetime(heat_data['date']).dt.month
# heat_data['day'] = pd.to_datetime(heat_data['date']).dt.day
# heat_data = heat_data.drop(columns=['date'])
# new_order = [
#     'year', 'month', 'day', 'weight', 'height', 'blood_glucose',
#     'physical_activity', 'diet', 'medication_adherence', 'stress_level',
#     'sleep_hours', 'hydration_level', 'bmi', 'risk_score'
# ]
# heat_data = heat_data[new_order]

# # Montar o heatmap
# plt.figure(figsize=(12,10))
# sns.heatmap(heat_data.corr(), annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
# plt.xticks(rotation=45, ha='right')
# plt.yticks(rotation=0)
# plt.title('Heatmap de Correlação das Features')
# plt.tight_layout()
# plt.savefig('heatmap.png')

#########################
#### Treinar o modelo ###
#########################

# Separar os dados
X = df.drop(columns=['user_id', 'date', 'risk_score'])
y = df['risk_score']

# Definir treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir o modelo
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42,
    min_samples_split=10,
    min_samples_leaf=2,
    max_features='sqrt',
    oob_score=True,
    n_jobs=-1
)

# Treinar
model.fit(X_train, y_train)

# Predizer teste
y_pred = model.predict(X_test)

# Caucular MAE
mae = mean_absolute_error(y_test, y_pred)
print(f"mae: {mae:.2f}")

# Caucular MSE
mse = mean_squared_error(y_test, y_pred)
print(f"mse: {mse:.2f}")

# Como o MAE deu 3.38 e o MSE deu 19.51 (6x maior que o MAE), devemos
# ter casos com grandes erros. Vamos plota-los.


########################################
#### Calculando e plotando residuals ###
#######################################

# Calculando os residuals
residuals = y_test - y_pred

# Plotando
plt.scatter(y_test, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Valores reais')
plt.xlabel('Resíduos')
plt.title('Gráfico de Resíduos')
plt.savefig('residuos.png')
