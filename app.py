import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Drug Classifier", page_icon="💊")

st.title("Drug Classifier")
st.write("Predict the appropriate drug based on patient information.")

# ==========================
# MODEL SELECTION
# ==========================

model_choice = st.selectbox(
    "Select Model",
    ["KNN", "Logistic Regression"]
)

if model_choice == "KNN":
    model = joblib.load("knn_model.pkl")

    # Replace with actual notebook result
    accuracy = "Your KNN Accuracy"
    precision = "Your KNN Precision"

else:
    model = joblib.load("logistic_model.pkl")

    # Replace with actual notebook result
    accuracy = "Your LR Accuracy"
    precision = "Your LR Precision"

st.subheader("Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric("Accuracy", accuracy)

with col2:
    st.metric("Precision", precision)

st.divider()

# ==========================
# USER INPUTS
# ==========================

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=30
)

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

# ==========================
# PREDICTION
# ==========================

if st.button("Predict Drug"):

    try:

        # Encoding
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

        prediction = model.predict(input_data)[0]

        # Drug label mapping
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

        st.write("### Patient Information")
        st.write(f"Age: {age}")
        st.write(f"Sex: {sex}")
        st.write(f"Blood Pressure: {bp}")
        st.write(f"Cholesterol: {cholesterol}")
        st.write(f"Na_to_K Ratio: {na_to_k}")

    except Exception as e:

        st.error(
            f"Prediction Error: {e}"
        )
