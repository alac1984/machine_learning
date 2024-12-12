"""
Nosso primeiro projeto em Machine Learning. Pegamos o dataset de iris, treinamos um
modelo RandomForestClassifier e medimos seu desempenho. Aplicamos técnicas como
cross_value_score (para medir se havia overfitting) e confusion_matrix pra estudar
os erros do modelo. Também exploramos os dados do classification_report.
"""


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
import pandas as pd

iris = load_iris()

# data = pd.DataFrame(iris.data, columns=iris.feature_names)
# data['target'] = iris.target

X = iris.data
y = iris.target

model = RandomForestClassifier(random_state=42)

# Treinando o modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Precisão do modelo: {accuracy:.2f}")

# Testando o quanto os dados tendem ao overfitting
scores = cross_val_score(model, X, y, cv=5)
print(f"Acurracy média: {scores.mean():.2f}")

# Gerando uma confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Classification report
report = classification_report(y_test, y_pred)
print(report)
