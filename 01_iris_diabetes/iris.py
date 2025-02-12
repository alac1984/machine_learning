"""
iris.py

This script represents our first Machine Learning project. We load the Iris dataset, 
train a RandomForestClassifier, and measure its performance by computing accuracy, 
cross-validation scores, a confusion matrix, and a classification report.

Usage:
  1. The script uses the Iris dataset from scikit-learn.
  2. It trains a RandomForestClassifier with a predefined random_state for reproducibility.
  3. The script splits the data into training and testing sets (80% / 20%).
  4. It evaluates model performance by:
     - Calculating the accuracy on the test set.
     - Applying cross_val_score to assess potential overfitting.
     - Generating and displaying a confusion matrix.
     - Printing a classification report.

Dependencies:
  - Python 3.x
  - scikit-learn
  - pandas (optional: shown for demonstration if needed for data manipulation)

Author:
  [Your Name or Organization]

License:
  [Optional: Specify License]
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

# Uncomment the following lines to convert the dataset into a pandas DataFrame.
# data = pd.DataFrame(iris.data, columns=iris.feature_names)
# data['target'] = iris.target

X = iris.data
y = iris.target

model = RandomForestClassifier(random_state=42)

# Training the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")

# Testing potential overfitting using cross-validation
scores = cross_val_score(model, X, y, cv=5)
print(f"Mean accuracy via cross-validation: {scores.mean():.2f}")

# Generating a confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Displaying a classification report
report = classification_report(y_test, y_pred)
print(report)
