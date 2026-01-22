# app/predict.py

import joblib
import numpy as np

model = joblib.load("model/insurance_classifier.pkl")


def predict_premium(age: int, bmi: float, children: int, smoker: int) -> int:
    X = np.array([[age, bmi, children, smoker]])
    prediction = model.predict(X)
    return int(prediction[0])
