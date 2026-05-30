import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Drug Classifier", page_icon="💊")

st.title("💊 Drug Classifier")
st.write("Predict the appropriate drug based on patient information.")

# Load Models
knn_model = joblib.load("knn_model.pkl")
lr_model = joblib.load("logistic_model.pkl")

model_choice = st.selectbox(
    "Select Model",
    ["KNN", "Logistic Regression"]
)

model = knn_model if model_choice == "KNN" else lr_model

age = st.number_input("Age", 1, 120, 30)

sex = st.selectbox(
    "Sex",
    ["F", "M"]
)

bp = st.selectbox(
    "Blood Pressure",
    ["LOW", "NORMAL", "HIGH"]
)

cholesterol = st.selectbox(
    "Cholesterol",
    ["NORMAL", "HIGH"]
)

na_to_k = st.number_input(
    "Na_to_K Ratio",
    min_value=0.0,
    value=15.0
)

if st.button("Predict Drug"):

    sex_encoded = 0 if sex == "F" else 1

    bp_mapping = {
        "HIGH": 0,
        "LOW": 1,
        "NORMAL": 2
    }

    chol_mapping = {
        "HIGH": 0,
        "NORMAL": 1
    }

    input_data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex_encoded],
        "BP": [bp_mapping[bp]],
        "Cholesterol": [chol_mapping[cholesterol]],
        "Na_to_K": [na_to_k]
    })

    try:
        prediction = model.predict(input_data)[0]

        drug_mapping = {
            0: "DrugY",
            1: "drugA",
            2: "drugB",
            3: "drugC",
            4: "drugX"
        }

        predicted_drug = drug_mapping.get(
            prediction,
            str(prediction)
        )

        st.success(
            f"Predicted Drug: {predicted_drug}"
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")
