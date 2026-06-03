import streamlit as st
import pandas as pd
import joblib

# Page Settings
st.set_page_config(
    page_title="DrugIQ",
    layout="wide"
)

st.title("Drug Classifier")

# Load Models
try:
    knn_model = joblib.load("knn_model.pkl")
    lr_model = joblib.load("logistic_model.pkl")

except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

# User Input
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

# Model Selection
model_choice = st.selectbox(
    "Select Model",
    ["KNN", "Logistic Regression"]
)

# Prediction Button
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

    # Input DataFrame
    input_data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex_encoded],
        "BP": [bp_mapping[bp]],
        "Cholesterol": [chol_mapping[cholesterol]],
        "Na_to_K": [na_to_k]
    })

    # Select Model
    model = (
        knn_model
        if model_choice == "KNN"
        else lr_model
    )

    try:

        # Prediction
        prediction = model.predict(input_data)[0]

        # Debug Information
        st.subheader("Debug Info")

        try:
            st.write("Model Classes:", model.classes_)
        except:
            pass

        st.write("Raw Prediction:", prediction)

        # Show Result
        st.success(
            f"Recommended Drug: {prediction}"
        )

        # Confidence
        try:
            probability = model.predict_proba(input_data)[0]

            confidence = max(probability) * 100

            st.info(
                f"Confidence: {confidence:.2f}%"
            )

            st.subheader("Class Probabilities")

            for drug, prob in zip(
                model.classes_,
                probability
            ):
                st.write(
                    f"{drug}: {prob*100:.2f}%"
                )

        except:
            st.warning(
                "Probability not available for this model."
            )

    except Exception as e:
        st.error(
            f"Prediction error: {e}"
        )
