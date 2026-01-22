# streamlit_app.py

import streamlit as st
import requests

st.set_page_config(page_title="Insurance Premium Predictor", layout="centered")

st.title("Insurance Premium Classification")
st.write("Enter customer details to predict premium class")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=1)
smoker = st.selectbox("Smoker", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

# Predict button
if st.button("Predict Premium Class"):
    payload = {
        "age": int(age),
        "bmi": float(bmi),
        "children": int(children),
        "smoker": int(smoker)
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)

        if response.status_code == 200:
            result = response.json()
            premium_class = result["premium_class"]

            if premium_class == 0:
                label = "Low Premium"
            elif premium_class == 1:
                label = "Medium Premium"
            else:
                label = "High Premium"

            st.success(f"Predicted Premium Class: {label}")

        else:
            st.error("API returned an error")

    except Exception as e:
        st.error("Could not connect to FastAPI server")
        st.write(str(e))
