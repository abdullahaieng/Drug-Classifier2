import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score

st.set_page_config(page_title="Drug Classifier", page_icon="💊")

st.title("💊 Drug Classifier")
st.write("Predict the appropriate drug based on patient information.")

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv("drug200.csv")

# ==========================
# PREPROCESSING
# ==========================

X = df.drop("Drug", axis=1)
y = df["Drug"]

le_sex = LabelEncoder()
le_bp = LabelEncoder()
le_chol = LabelEncoder()
le_drug = LabelEncoder()

X["Sex"] = le_sex.fit_transform(X["Sex"])
X["BP"] = le_bp.fit_transform(X["BP"])
X["Cholesterol"] = le_chol.fit_transform(X["Cholesterol"])

y = le_drug.fit_transform(y)

# ==========================
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# SCALING
# ==========================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================
# TRAIN MODELS
# ==========================

log_reg_model = LogisticRegression(
    random_state=42,
    solver="liblinear"
)

log_reg_model.fit(
    X_train_scaled,
    y_train
)

knn_model = KNeighborsClassifier()

knn_model.fit(
    X_train_scaled,
    y_train
)

# ==========================
# MODEL METRICS
# ==========================

y_pred_lr = log_reg_model.predict(X_test_scaled)
y_pred_knn = knn_model.predict(X_test_scaled)

lr_accuracy = accuracy_score(
    y_test,
    y_pred_lr
) * 100

lr_precision = precision_score(
    y_test,
    y_pred_lr,
    average="weighted"
) * 100

knn_accuracy = accuracy_score(
    y_test,
    y_pred_knn
) * 100

knn_precision = precision_score(
    y_test,
    y_pred_knn,
    average="weighted"
) * 100

# ==========================
# MODEL SELECTION
# ==========================

model_choice = st.selectbox(
    "Select Model",
    [
        "Logistic Regression",
        "KNN"
    ]
)

if model_choice == "Logistic Regression":
    model = log_reg_model
    accuracy = lr_accuracy
    precision = lr_precision
else:
    model = knn_model
    accuracy = knn_accuracy
    precision = knn_precision

st.subheader("Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Accuracy",
        f"{accuracy:.2f}%"
    )

with col2:
    st.metric(
        "Precision",
        f"{precision:.2f}%"
    )

st.divider()

# ==========================
# USER INPUT
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

    input_df = pd.DataFrame({
        "Age": [age],
        "Sex": [sex],
        "BP": [bp],
        "Cholesterol": [cholesterol],
        "Na_to_K": [na_to_k]
    })

    input_df["Sex"] = le_sex.transform(
        input_df["Sex"]
    )

    input_df["BP"] = le_bp.transform(
        input_df["BP"]
    )

    input_df["Cholesterol"] = le_chol.transform(
        input_df["Cholesterol"]
    )

    input_scaled = scaler.transform(
        input_df
    )

    prediction = model.predict(
        input_scaled
    )[0]

    predicted_drug = le_drug.inverse_transform(
        [prediction]
    )[0]

    st.success(
        f"Predicted Drug: {predicted_drug}"
    )
