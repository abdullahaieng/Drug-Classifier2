import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Drug Classifier", page_icon="💊")

st.title("💊 Drug Classifier")
st.write("Predict the appropriate drug based on patient information.")

# Load model
model = joblib.load("knn_model.pkl")  # Change to logistic_model.pkl if needed

# User Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", ["F", "M"])
bp = st.selectbox("Blood Pressure", ["LOW", "NORMAL", "HIGH"])
cholesterol = st.selectbox("Cholesterol", ["NORMAL", "HIGH"])
na_to_k = st.number_input("Na_to_K Ratio", min_value=0.0, value=15.0)

if st.button("Predict Drug"):
    # The code below is now properly indented under the 'if' statement
    input_data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex],
        "BP": [bp],
        "Cholesterol": [cholesterol],
        "Na_to_K": [na_to_k]
    })
    
    prediction = model.predict(input_data)
    st.success(f"Predicted Drug: {prediction[0]}")
