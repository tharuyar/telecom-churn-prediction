import streamlit as st
import requests

# Streamlit UI Title
st.title("📊 Customer Churn Prediction")

# User Inputs
tenure = st.number_input("Customer Tenure (months)", min_value=0, max_value=100, value=12)
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=70.5)
total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=845.5)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

# Submit Button
if st.button("Predict Churn"):
    # Prepare input data
    input_data = {
        "tenure": tenure,
        "monthly_charges": monthly_charges,
        "total_charges": total_charges,
        "contract": contract,
        "internet_service": internet_service,
        "payment_method": payment_method
    }

    # Call FastAPI
    api_url = "https://telechurn.duckdns.org/predict/"
    response = requests.post(api_url, json=input_data)

    # Display Results
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        if prediction == "Churn":
            st.error("⚠️ This customer is likely to churn!")
        else:
            st.success("✅ This customer is NOT likely to churn.")
    else:
        st.warning("Error: Unable to get a prediction. Check API.")


