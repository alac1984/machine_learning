"""
diabetes_continuous.py

This script demonstrates a basic workflow for training a Random Forest Regressor on a diabetes dataset.
It reads the data from 'diabetes_data.csv', splits the features and target, and trains the model to
predict the 'risk_score'. Various regression metrics (MAE and MSE) are computed to evaluate the
model performance, and a residual plot is generated to visualize prediction errors.

Usage:
  1. Place the 'diabetes_data.csv' file in the same directory as this script.
  2. Run the script. It will:
     - Load and preprocess the data (dropping irrelevant columns: 'user_id' and 'date').
     - Split the data into training and testing sets.
     - Train a Random Forest Regressor with predefined hyperparameters.
     - Generate predictions on the test set.
     - Calculate and print out the Mean Absolute Error (MAE) and Mean Squared Error (MSE).
     - Produce and save a residuals plot ('residuos.png').

Dependencies:
  - Python 3.x
  - pandas
  - scikit-learn
  - seaborn
  - matplotlib

Author:
    André Carvalho <alac1984@gmail.com>

License:
  [MIT]

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


# Loading data
df = pd.read_csv('diabetes_data.csv')


# # Creating a heatmap
# heat_data = df.drop(columns=['user_id'])
# # Preprocessing data 
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

# # Plotting the heatmap
# plt.figure(figsize=(12,10))
# sns.heatmap(heat_data.corr(), annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
# plt.xticks(rotation=45, ha='right')
# plt.yticks(rotation=0)
# plt.title('Heatmap de Correlação das Features')
# plt.tight_layout()
# plt.savefig('heatmap.png')

# Putting data apart
X = df.drop(columns=['user_id', 'date', 'risk_score'])
y = df['risk_score']

# Defining train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Defining the model
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

# Training
model.fit(X_train, y_train)

# Predict test
y_pred = model.predict(X_test)

# Calculating MAE
mae = mean_absolute_error(y_test, y_pred)
print(f"mae: {mae:.2f}")

# Calculating MSE
mse = mean_squared_error(y_test, y_pred)
print(f"mse: {mse:.2f}")

# As the MAE gave 3.38 and the MSE gave 19.51 (6x greater than the MAE), we must
# have cases with big errors. Let's plot them.

# Calculating residuals
residuals = y_test - y_pred

# Plotting
plt.scatter(y_test, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Valores reais')
plt.xlabel('Resíduos')
plt.title('Gráfico de Resíduos')
plt.savefig('residuos.png')


