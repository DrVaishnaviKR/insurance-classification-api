# 🏥 Insurance Premium Classification System

An end to end Machine Learning application to predict insurance premium category using a trained classification model, FastAPI backend, Streamlit frontend, and Firebase cloud storage.

This project demonstrates a complete production style ML pipeline from training to deployment and logging.

---

## ✨ Key Features

• Machine learning based premium classification  
• FastAPI powered backend inference service  
• Interactive Streamlit web frontend  
• Firebase Firestore cloud logging  
• Automated API testing with Pytest  
• Modular and production ready code structure  

---
```
## 🖼️ System Architecture

User
↓
Streamlit Frontend
↓
FastAPI Backend
↓
ML Classification Model
↓
Firebase Firestore
```
---

## 🎯 Problem Statement

Given customer information:

• Age  
• Body Mass Index  
• Number of children  
• Smoker status  

Predict the **insurance premium category**:

| Class | Description |
|-----|------------|
| 0 | Low Premium |
| 1 | Medium Premium |
| 2 | High Premium |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Language | Python |
| Machine Learning | Scikit learn |
| Backend API | FastAPI |
| Frontend | Streamlit |
| Database | Firebase Firestore |
| Testing | Pytest |

---
```
## 📁 Project Structure

Classification_model/

│ main.py FastAPI entry point
│ schema.py Pydantic input and output schemas
│ predict.py Model loading and inference logic
│ training.py Model training script
│ streamlit_app.py Streamlit frontend
│ firebase_db.py Firebase connection module
│ requirements.txt Python dependencies
│ tests/ Pytest test cases
│ model/ Trained model directory
│ .gitignore Ignore secrets and virtual environment

```
---

☁️ Firebase Integration
Each prediction is stored in Firebase Firestore with:

• Input features
• Predicted class
• Timestamp

This enables:

• Prediction history
• Monitoring
• Future analytics dashboards

🧪 Testing
Ran automated API tests using:

• Root endpoint
• Prediction endpoint

📈 Future Enhancements
Planned improvements:

• Predict actual premium amount using regression
• Display prediction confidence in UI
• Add user authentication
• Add dashboard for historical analysis
• Add Docker based deployment

👩‍💻 Author
Vaishnavi K R

Ayurvedic Doctor transitioning into
AI and Data Science in Healthcare

Why This Project Matters -

This project demonstrates:

• Complete ML lifecycle
• Clean backend API design
• Frontend and backend integration
• Cloud database logging
• Testing discipline
• Production ready architecture

---
