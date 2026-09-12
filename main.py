import joblib 
from fastapi import FastAPI
model = joblib.load('Mental_Health_Model.pkl')

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Hello! Welcome to the Mental Health Prediction API."}