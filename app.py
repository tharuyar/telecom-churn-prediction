from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from preprocess import preprocess_input  # Import preprocessing function

# Load trained model
try:
    model = joblib.load("xgboost_churn_model.pkl")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

# Define request format
class CustomerData(BaseModel):
    SeniorCitizen: str
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    PaperlessBilling: str
    MonthlyCharges: float
    TotalCharges: float
    gender: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaymentMethod: str

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API"}

@app.post("/predict/")
def predict_churn(data: CustomerData):
    try:
        print("Received raw data:", data.dict())  # Debugging log

        # Preprocess input
        processed_data = preprocess_input(data.dict())

        # Make prediction
        prediction = model.predict(processed_data)

        # Convert output to readable format
        result = "Churn" if prediction[0] == 1 else "No Churn"

        return {"prediction": result}

    except Exception as e:
        print(f"Error: {e}")  # Print the actual error
        raise HTTPException(status_code=500, detail=str(e))
