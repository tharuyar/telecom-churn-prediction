import pandas as pd
import json

# Load the expected feature names from training
with open("feature_names.json", "r") as f:
    FEATURE_NAMES = json.load(f)

def preprocess_input(data: dict):
    """
    Transforms raw API input into a format that matches model training.
    """
    # Convert categorical Yes/No to 1/0
    binary_columns = ["SeniorCitizen", "Partner", "Dependents", "PhoneService", "PaperlessBilling"]
    for col in binary_columns:
        data[col] = 1 if data[col] == "Yes" else 0

    # One-hot encode categorical variables
    categorical_columns = ["gender", "MultipleLines", "InternetService", "OnlineSecurity",
                           "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV",
                           "StreamingMovies", "Contract", "PaymentMethod"]

    df = pd.DataFrame([data])
    df = pd.get_dummies(df, columns=categorical_columns)

    # Ensure all expected feature columns exist
    for col in FEATURE_NAMES:
        if col not in df.columns:
            df[col] = 0  # Add missing columns with default value 0

    # Reorder columns to match model training
    df = df[FEATURE_NAMES]

    return df
