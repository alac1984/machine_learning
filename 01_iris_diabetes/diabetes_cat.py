"""
Aqui fizemos o mesmo trabalho que fizemos em iris.py, mas transformando o dataset
de diabetes, que possuia um target contínuo, em classificatório.
"""

from sklearn.model_selection import train_test_split
from xgboost import XGBRFClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import pandas as pd


###########################
#### Carregar os dados ####
###########################

df = pd.read_csv('diabetes_data.csv')

#######################################################
#### Converter classificação contínua em categórica ###
#######################################################

bins = [0.0, 33.33, 66.66, 100]
labels = [0, 1, 2]
df['risk_score'] = pd.cut(df['risk_score'], bins=bins, labels=labels, include_lowest=True)

###############################
#### Treinamento e predição ###
###############################

# Separar os dados
X = df.drop(columns=['user_id', 'date', 'risk_score', 'sleep_hours', 'blood_glucose'])
y = df['risk_score']

# Definir treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir modelo
model = XGBRFClassifier(
    scale_pos_weight=1,
    use_label_encoder=False,
    eval_metrics='mlogloss',
    random_state=42
)

# Treinar
model.fit(X_train, y_train)

# Predição
y_pred = model.predict(X_test)

# Análise da predição
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisão do modelo: {accuracy:.2f}")

# Confusion Matrix 
cm = confusion_matrix(y_test, y_pred)
print(cm)
