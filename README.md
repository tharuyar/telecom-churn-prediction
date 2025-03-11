**📡 Telecom Customer Churn Prediction**

**🚀 Project Overview**

The Telecom Customer Churn Prediction project aims to identify customers who are likely to churn using machine learning. This project utilizes XGBoost for high-accuracy predictions and includes:



📡 FastAPI Backend - For API-based predictions.

🎨 Streamlit UI - User-friendly interface.

☁️ AWS EC2 Deployment - Hosted on a cloud instance.

🔄 Nginx Reverse Proxy - For secure API access.

🎯 Features




**🎯 Features**

✔️ Predicts customer churn based on telecom usage data.

✔️ Uses XGBoost for high-accuracy predictions.

✔️ Interactive UI built with Streamlit.

✔️ API backend developed using FastAPI.

✔️ Hosted on AWS EC2 with Nginx Reverse Proxy.



**📂 Project Structure**

📁 telecom-churn-prediction
│── 📂 fastapi-app

│   ├── 📜 app.py   # FastAPI application

│   ├── 📜 preprocess.py        # Preprocessing functions

│   ├── 📜 feature_names.json   # Feature names

│   ├── 📜 xgboost_churn_model.pkl  # Trained ML model

│   ├── 📜 requirements.txt     # Python dependencies

│   ├── 📜 streamlit_app.py     # Streamlit UI

│   ├── 📂 venv                # Virtual environment

│── 📂 screenshots              # UI & API screenshots

│── 📜 telecom_customers.csv    # Dataset file

│── 📜 README.md                # Project documentation


**🛠 Installation & Setup**

🔹 1. Clone the Repository

git clone git@github.com:tharuyar/telecom-churn-prediction.git

cd telecom-churn-prediction

🔹 2. Create Virtual Environment & Install Dependencies

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

 **3. Run FastAPI Backend**
 
    uvicorn app:app --host 0.0.0.0 --port 8000
    
API will be accessible at: http://<public-ip>:8000

Swagger UI: http://<public-ip>:8000/docs


 __4. Run Streamlit UI__
 
    streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
    
UI will be accessible at: http://<public-ip>:8501


__📡 API Endpoints__

Method     	Endpoint	     Description

POST    	/predict/	       Predicts churn probability

GET	        /docs	         API Documentation (Swagger UI)


**🔹 Example API Request**


curl -X POST "http://<public-ip>:8000/predict/" -H "Content-Type: application/json" -d '{

    "tenure": 12,
    
    "monthly_charges": 70.5,
    
    "total_charges": 845.5,
    
    "contract": "Month-to-month",
    
    "internet_service": "Fiber optic",
    
    "payment_method": "Credit card"
    
}'



__🏗 Deployment Details__


__✅ Backend: FastAPI__

__✅ Frontend: Streamlit__

__✅ Hosting: AWS EC2 Instance__

__✅ Reverse Proxy: Nginx__

__✅ Security: SSL with Let’s Encrypt__


__📊 Dataset__

The dataset used for training is the IBM Telco Customer Churn Dataset:


📜 Source: IBM Sample Data

📌 Total Records: 7,043 customers

🎯 Target Column: Churn


__📸 Screenshots__

Streamlit UI

FastAPI Swagger UI



__🤝 Contributing__

Contributions are welcome! 🎉

Fork the repo, make changes, and submit a Pull Request.

For major changes, open an issue first to discuss your proposal.

# __🚀 Developed by:__
## __📌 Tharun Yara__

