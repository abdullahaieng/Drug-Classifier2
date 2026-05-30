# 💊 Patient Medication Predictor

An end-to-end predictive healthcare application designed to assist medical practitioners in selecting the most effective drug class for patients. By analyzing fundamental physiological metrics (Age, Gender, Blood Pressure intensity, Cholesterol levels, and Sodium-to-Potassium ratio), this system applies machine learning to generate real-time therapeutic recommendations.

The underlying model leverages **Python** and **K-Nearest Neighbors (KNN)**, while the front-end graphical user interface is deployed on the web via the **Streamlit Cloud** platform.

---

## 🌐 Live Application
🔗 **[Launch the Medical Dashboard](https://share.streamlit.io/)** *(Apna Streamlit link yahan paste karein)*

---

## 🎯 Key Capabilities
* **Dynamic Feature Input:** Intuitive numeric fields and dropdown menus for rapid patient data entry.
* **Instantaneous Inference:** High-speed algorithmic execution providing immediate drug category outputs.
* **Responsive Architecture:** Clean, streamlined web interface built for cross-device accessibility.

---

## 📊 Analytical Dimensions (Dataset Features)
The predictive engine evaluates the following clinical variables:
* **Age:** Numerical lifespan representation of the patient (1 to 120 years).
* **Sex:** Categorical biological classification (Female / Male).
* **Blood Pressure (BP):** Stratified cardiovascular pressure mapping (LOW, NORMAL, HIGH).
* **Cholesterol:** Lipid profile categorization (NORMAL, HIGH).
* **Na_to_K:** Electrolyte balance metric indicating the Sodium-to-Potassium ratio in blood serum.

---

## 📁 Repository Blueprint
```text
├── .venv/                 # Isolated local development space
├── DRUG_CLASSIFER.ipynb   # Exploratory Data Analysis, Preprocessing & Model Evaluation
├── app.py                 # Core Streamlit application architecture
├── drug200.csv            # Structured historical patient records
├── knn_model.pkl          # Serialized predictive weights (Trained Model)
└── requirements.txt       # Environment tracking and cloud dependency declarations
