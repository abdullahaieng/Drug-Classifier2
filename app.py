import streamlit as st
import pandas as pd
import joblib

# Page Config
st.set_page_config(
    page_title="DrugIQ",
    layout="wide"
)

st.title("💊 DrugIQ - Drug Classifier")

# Load Models
try:
    knn_model = joblib.load("knn_model.pkl")
    lr_model = joblib.load("logistic_model.pkl")

except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

# User Inputs
age = st.slider("Age", 1, 120, 35)

sex = st.selectbox(
    "Sex",
    ["Female", "Male"]
)

bp = st.selectbox(
    "Blood Pressure",
    ["HIGH", "NORMAL", "LOW"]
)

cholesterol = st.selectbox(
    "Cholesterol",
    ["HIGH", "NORMAL"]
)

na_to_k = st.slider(
    "Na/K Ratio",
    0.0,
    50.0,
    15.0
)

model_choice = st.selectbox(
    "Select Model",
    ["KNN", "Logistic Regression"]
)

# Predict Button
if st.button("Predict Drug"):

    # Encoding
    sex_encoded = 0 if sex == "Female" else 1

    bp_mapping = {
        "HIGH": 0,
        "LOW": 1,
        "NORMAL": 2
    }

    chol_mapping = {
        "HIGH": 0,
        "NORMAL": 1
    }

    # Input Data
    input_data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex_encoded],
        "BP": [bp_mapping[bp]],
        "Cholesterol": [chol_mapping[cholesterol]],
        "Na_to_K": [na_to_k]
    })

    # Select Model
    model = knn_model if model_choice == "KNN" else lr_model

    try:

        # Prediction
        prediction = model.predict(input_data)[0]

        # Convert numpy type to int if possible
        try:
            prediction = int(prediction)
        except:
            pass

        # Drug Mapping
        drug_mapping = {
            0: "DrugA",
            1: "DrugB",
            2: "DrugC",
            3: "DrugX",
            4: "DrugY"
        }

        # Get Drug Name
        if prediction in drug_mapping:
            predicted_drug = drug_mapping[prediction]
        else:
            predicted_drug = str(prediction)

        # Result
        st.success(f"💊 Recommended Drug: {predicted_drug}")

        # Confidence
        try:
            probability = model.predict_proba(input_data)[0]

            confidence = max(probability) * 100

            st.info(
                f"Confidence: {confidence:.2f}%"
            )

        except:
            pass

        # Debug Section
        with st.expander("Debug Info"):

            st.write("Prediction Value:", prediction)
            st.write("Prediction Type:", type(prediction))

            try:
                st.write("Model Classes:", model.classes_)
            except:
                st.write("Classes not available")

    except Exception as e:
        st.error(f"Prediction error: {e}")
