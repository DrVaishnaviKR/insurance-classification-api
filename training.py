# training.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Create sample insurance dataset
data = {
    "age": [22, 25, 47, 52, 46, 56, 30, 40, 28, 60],
    "bmi": [18.5, 22.0, 30.1, 31.5, 29.0, 35.2, 24.5, 27.8, 23.0, 34.0],
    "children": [0, 1, 2, 3, 2, 4, 0, 1, 0, 3],
    "smoker": [0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    "premium_class": [0, 0, 2, 2, 1, 2, 0, 1, 0, 2]
}

df = pd.DataFrame(data)

X = df[["age", "bmi", "children", "smoker"]]
y = df["premium_class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/insurance_classifier.pkl")

print("Insurance model trained and saved")
