from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
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
X = df.drop(columns=['user_id', 'date', 'risk_score'])
y = df['risk_score']

# Definir treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir modelo
model = RandomForestClassifier(class_weight='balanced', random_state=42)

# Treinar
model.fit(X_train, y_train)

# Predição
y_pred = model.predict(X_test)

# Análise da predição
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisão do modelo: {accuracy:.2f}")
