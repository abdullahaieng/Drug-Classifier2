import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Drug Classifier", page_icon="💊")

st.title("💊 Drug Classifier")
st.write("Predict the appropriate drug based on patient information.")

# Load model
model = joblib.load("knn_model.pkl")  

# User Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", ["F", "M"])
bp = st.selectbox("Blood Pressure", ["LOW", "NORMAL", "HIGH"])
cholesterol = st.selectbox("Cholesterol", ["NORMAL", "HIGH"])
na_to_k = st.number_input("Na_to_K Ratio", min_value=0.0, value=15.0)

if st.button("Predict Drug"):
    # 1. Convert Text Inputs to Numbers to match your model training
    sex_encoded = 0 if sex == "F" else 1
    
    # Blood Pressure Mapping
    if bp == "LOW":
        bp_encoded = 0
    elif bp == "NORMAL":
        bp_encoded = 1
    else:
        bp_encoded = 2  # HIGH
        
    # Cholesterol Mapping
    chol_encoded = 0 if cholesterol == "NORMAL" else 1

    # 2. Create the DataFrame using the EXACT column names from your Jupyter Notebook
    input_data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex_encoded],
        "BP": [bp_encoded],
        "Cholesterol": [chol_encoded],
        "Na_to_K": [na_to_k]
    })
    
    # 3. Predict and Display
    try:
        prediction = model.predict(input_data)
        st.success(f"Predicted Drug: {prediction[0]}")
    except Exception as e:
        st.error(f"Error making prediction: {e}")
