# main.py

from fastapi import FastAPI
from schema import InsuranceRequest, InsuranceResponse
from predict import predict_premium

from firebase_db import db
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Insurance API running with Firebase"}

@app.post("/predict", response_model=InsuranceResponse)
def predict(request: InsuranceRequest):
    # 1. Predict
    result = predict_premium(
        age=request.age,
        bmi=request.bmi,
        children=request.children,
        smoker=request.smoker
    )

    # 2. Save to Firebase Firestore
    data = {
        "age": request.age,
        "bmi": request.bmi,
        "children": request.children,
        "smoker": request.smoker,
        "premium_class": result,
        "created_at": datetime.utcnow()
    }

    db.collection("insurance_predictions").add(data)

    # 3. Return response
    return InsuranceResponse(premium_class=result)

@app.get("/history")
def get_history(limit: int = 10):
    docs = db.collection("insurance_predictions").order_by(
        "created_at", direction="DESCENDING"
    ).limit(limit).stream()

    results = []
    for doc in docs:
        results.append(doc.to_dict())

    return results
