"""
diabetes_categorial.py

This script replicates the work done in iris.py, but transforms the continuous target 
'risk_score' into a categorical classification problem for the diabetes dataset.
It reads the data from 'diabetes_data.csv', splits the features and target, and trains 
an XGBoost Random Forest Classifier (XGBRFClassifier) to predict discrete risk categories. 
The script also calculates and displays the classification accuracy and the confusion matrix.

Usage:
  1. Place the 'diabetes_data.csv' file in the same directory as this script.
  2. Run the script. It will:
     - Load the dataset, removing irrelevant columns (such as 'user_id', 'date', etc.).
     - Convert 'risk_score' from continuous to categorical using predefined bins.
     - Split the data into training and testing sets.
     - Train the XGBRFClassifier with specified parameters.
     - Generate predictions on the test set.
     - Calculate and print out the model accuracy.
     - Display the confusion matrix.

Dependencies:
  - Python 3.x
  - pandas
  - scikit-learn
  - xgboost

Author:
  André Carvalho <alac1984@gmail.com>

License:
  [MIT]
"""

from sklearn.model_selection import train_test_split
from xgboost import XGBRFClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import pandas as pd

# Load data
df = pd.read_csv('diabetes_data.csv')

# Convert continuous classification into categorical
bins = [0.0, 33.33, 66.66, 100]
labels = [0, 1, 2]
df['risk_score'] = pd.cut(df['risk_score'], bins=bins, labels=labels, include_lowest=True)

# Separate the data
X = df.drop(columns=['user_id', 'date', 'risk_score', 'sleep_hours', 'blood_glucose'])
y = df['risk_score']

# Define training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
model = XGBRFClassifier(
    scale_pos_weight=1,
    use_label_encoder=False,
    eval_metrics='mlogloss',
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Prediction analysis
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Precision: {accuracy:.2f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
