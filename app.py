import streamlit as st
import pandas as pd
import joblib

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="AI Drug Classifier",
    page_icon="💊",
    layout="wide"
)

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp {
    background:
    linear-gradient(
    135deg,
    #050816 0%,
    #0B1023 30%,
    #111827 60%,
    #1E1B4B 100%);
}

/* Hide Streamlit Branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
.main-title{
    font-size:64px;
    font-weight:800;
    text-align:center;
    background:linear-gradient(
    90deg,
    #ff6b6b,
    #ffd93d,
    #6bcb77,
    #4d96ff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:0;
}

.subtitle{
    text-align:center;
    color:#b8c1ec;
    font-size:18px;
    margin-bottom:40px;
}

/* Glass Card */
.glass{
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(18px);
    padding:30px;
    border-radius:25px;
    border:1px solid rgba(255,255,255,0.1);
    box-shadow:0 8px 32px rgba(0,0,0,0.4);
}

/* Metric Card */
.metric-card{
    background:rgba(255,255,255,0.05);
    border-radius:20px;
    padding:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.08);
    margin-bottom:15px;
}

/* Result Card */
.result-card{
    background:linear-gradient(
    135deg,
    #00c9a7,
    #00b4d8);
    border-radius:20px;
    padding:30px;
    text-align:center;
    font-size:32px;
    font-weight:700;
    color:white;
    margin-top:25px;
    box-shadow:0 0 25px rgba(0,255,200,0.5);
}

/* Button */
.stButton > button{
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;
    font-size:20px;
    font-weight:700;
    color:white;
    background:linear-gradient(
    90deg,
    #7f5af0,
    #2cb67d);
    transition:0.3s;
}

.stButton > button:hover{
    transform:translateY(-3px);
    box-shadow:0 10px 25px rgba(0,255,200,0.4);
}

/* Labels */
label{
    font-weight:600 !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# LOAD MODELS
# ==========================

try:
    knn_model = joblib.load("knn_model.pkl")
    lr_model = joblib.load("logistic_model.pkl")
except Exception as e:
    st.error(f"Model Loading Error: {e}")
    st.stop()

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.title("💊 AI Dashboard")

    st.markdown("---")

    st.markdown("""
    ### Features

    ✅ KNN Model

    ✅ Logistic Regression

    ✅ Real-Time Prediction

    ✅ ML Powered

    ✅ Luxury UI

    ✅ Fast Processing
    """)

    st.markdown("---")

    st.success("System Online")

# ==========================
# HEADER
# ==========================

st.markdown("""
<h1 class='main-title'>
💊 AI Drug Classifier
</h1>

<p class='subtitle'>
Next Generation Machine Learning Powered Drug Recommendation System
</p>
""", unsafe_allow_html=True)

# ==========================
# TOP CARDS
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='metric-card'>
    <h2>🤖</h2>
    <h3>2 AI Models</h3>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-card'>
    <h2>⚡</h2>
    <h3>Instant Prediction</h3>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-card'>
    <h2>🎯</h2>
    <h3>High Accuracy</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================
# MAIN FORM
# ==========================

st.markdown("<div class='glass'>", unsafe_allow_html=True)

left, right = st.columns(2)

with left:

    model_choice = st.selectbox(
        "🧠 Select Model",
        ["KNN", "Logistic Regression"]
    )

    age = st.slider(
        "🎂 Age",
        1,
        120,
        30
    )

    sex = st.selectbox(
        "👤 Gender",
        ["F", "M"]
    )

with right:

    bp = st.selectbox(
        "🩸 Blood Pressure",
        ["LOW", "NORMAL", "HIGH"]
    )

    cholesterol = st.selectbox(
        "🧪 Cholesterol",
        ["NORMAL", "HIGH"]
    )

    na_to_k = st.slider(
        "⚗️ Na_to_K Ratio",
        0.0,
        50.0,
        15.0
    )

predict = st.button("🚀 Predict Drug")

st.markdown("</div>", unsafe_allow_html=True)

# ==========================
# MODEL SELECTION
# ==========================

model = (
    knn_model
    if model_choice == "KNN"
    else lr_model
)

# ==========================
# PREDICTION
# ==========================

if predict:

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
            1: "DrugA",
            2: "DrugB",
            3: "DrugC",
            4: "DrugX"
        }

        predicted_drug = drug_mapping.get(
            prediction,
            str(prediction)
        )

        st.markdown(
            f"""
            <div class="result-card">
                🏆 Recommended Drug
                <br><br>
                {predicted_drug}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

    except Exception as e:
        st.error(f"Prediction Error: {e}")
