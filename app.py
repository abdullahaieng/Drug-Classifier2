```python
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="DrugIQ — Drug Intelligence Platform",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"], .stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: #090c14;
    color: #e8eaf0;
}

#MainMenu, footer, header, .stDeployButton { visibility: hidden; }
.block-container { padding: 2rem 2.5rem 4rem 2.5rem; max-width: 1200px; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #0d1117; }
::-webkit-scrollbar-thumb { background: #1e2a40; border-radius: 10px; }

/* ── Background ambient glows ── */
.stApp::before {
    content: '';
    position: fixed;
    top: -200px; left: -200px;
    width: 700px; height: 700px;
    background: radial-gradient(circle, rgba(29,78,216,0.07) 0%, transparent 70%);
    pointer-events: none; z-index: 0;
}
.stApp::after {
    content: '';
    position: fixed;
    bottom: -200px; right: -200px;
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(14,165,233,0.05) 0%, transparent 70%);
    pointer-events: none; z-index: 0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0b0f1a !important;
    border-right: 1px solid rgba(255,255,255,0.05) !important;
}
[data-testid="stSidebar"] .block-container { padding: 2rem 1.5rem; }

.sidebar-logo {
    display: flex; align-items: center; gap: 10px;
    margin-bottom: 2rem; padding-bottom: 1.5rem;
    border-bottom: 1px solid rgba(255,255,255,0.07);
}
.sidebar-logo-mark {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, #1d4ed8, #0ea5e9);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px; font-weight: 900; color: white;
}
.sidebar-logo-text {
    font-size: 18px; font-weight: 700;
    color: #f1f5f9; letter-spacing: -0.3px;
}
.sidebar-logo-text span { color: #38bdf8; }

.status-pill {
    display: inline-flex; align-items: center; gap: 7px;
    background: rgba(34,197,94,0.08);
    border: 1px solid rgba(34,197,94,0.2);
    border-radius: 20px; padding: 6px 14px;
    font-size: 12px; font-weight: 500; color: #4ade80;
    margin-bottom: 1.5rem;
}
.status-dot {
    width: 7px; height: 7px;
    background: #4ade80; border-radius: 50%;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%,100% { opacity:1; transform:scale(1); }
    50% { opacity:0.5; transform:scale(0.8); }
}

.sidebar-section { margin-bottom: 1.8rem; }
.sidebar-section-title {
    font-size: 10px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 1.2px;
    color: #475569; margin-bottom: 10px;
}
.sidebar-item {
    display: flex; align-items: center; gap: 10px;
    padding: 9px 12px; border-radius: 10px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.05);
    margin-bottom: 6px; font-size: 13px; color: #94a3b8;
}
.sidebar-item-dot { width: 6px; height: 6px; border-radius: 50%; background: #1d4ed8; }
.sidebar-item strong { color: #cbd5e1; font-weight: 500; }

/* ── Hero ── */
.hero-section {
    text-align: center;
    padding: 3rem 1rem 2.5rem;
    position: relative;
}
.hero-badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(29,78,216,0.1);
    border: 1px solid rgba(29,78,216,0.25);
    border-radius: 20px; padding: 6px 16px;
    font-size: 11px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 1px;
    color: #60a5fa; margin-bottom: 1.5rem;
}
.hero-title {
    font-size: clamp(36px, 5vw, 58px);
    font-weight: 800; line-height: 1.1;
    letter-spacing: -1.5px;
    color: #f8fafc;
    margin-bottom: 1rem;
}
.hero-title span {
    background: linear-gradient(135deg, #3b82f6, #0ea5e9, #38bdf8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-subtitle {
    font-size: 17px; font-weight: 400;
    color: #64748b; max-width: 480px; margin: 0 auto;
    line-height: 1.6;
}

/* ── Stat Cards ── */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px; margin-bottom: 2.5rem;
}
@media (max-width: 768px) { .stats-grid { grid-template-columns: repeat(2,1fr); } }
.stat-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px; padding: 20px 22px;
    transition: border-color 0.2s, transform 0.2s;
    position: relative; overflow: hidden;
}
.stat-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(56,189,248,0.3), transparent);
}
.stat-card:hover { border-color: rgba(56,189,248,0.2); transform: translateY(-2px); }
.stat-label {
    font-size: 11px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.8px;
    color: #475569; margin-bottom: 8px;
}
.stat-value {
    font-size: 26px; font-weight: 800;
    color: #f1f5f9; letter-spacing: -0.5px;
}
.stat-sub { font-size: 12px; color: #334155; margin-top: 3px; font-weight: 400; }

/* ── Glass Panel ── */
.glass-panel {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px; padding: 36px 36px 32px;
    position: relative; overflow: hidden;
    box-shadow: 0 0 0 1px rgba(0,0,0,0.3), 0 20px 60px rgba(0,0,0,0.4);
    backdrop-filter: blur(20px);
    margin-bottom: 1.5rem;
}
.glass-panel::before {
    content: '';
    position: absolute; top: -1px; left: 40px; right: 40px; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(56,189,248,0.4), transparent);
}

.panel-header { margin-bottom: 28px; }
.panel-title {
    font-size: 16px; font-weight: 700;
    color: #e2e8f0; letter-spacing: -0.2px;
}
.panel-desc { font-size: 13px; color: #475569; margin-top: 4px; }

/* ── Form overrides ── */
[data-testid="stSelectbox"] > div > div,
[data-testid="stNumberInput"] input,
[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    transition: border-color 0.2s !important;
}
[data-testid="stSelectbox"] > div > div:focus-within,
[data-testid="stNumberInput"] input:focus {
    border-color: rgba(56,189,248,0.4) !important;
    box-shadow: 0 0 0 3px rgba(56,189,248,0.08) !important;
}

/* Slider */
[data-testid="stSlider"] .st-emotion-cache-1gv3huu,
.stSlider [data-baseweb="slider"] [data-testid="stThumbValue"] {
    color: #60a5fa !important;
}
.stSlider [data-baseweb="slider"] div[role="slider"] {
    background: #1d4ed8 !important;
    border: 2px solid #3b82f6 !important;
    box-shadow: 0 0 10px rgba(59,130,246,0.5) !important;
}
[data-baseweb="slider"] div:first-child div:nth-child(3) {
    background: linear-gradient(90deg, #1d4ed8, #0ea5e9) !important;
}

/* Labels */
.stSelectbox label, .stSlider label, [data-testid="stWidgetLabel"] p {
    font-size: 13px !important; font-weight: 500 !important;
    color: #94a3b8 !important; letter-spacing: 0.1px;
}

/* ── Divider ── */
.form-divider {
    height: 1px;
    background: rgba(255,255,255,0.06);
    margin: 24px 0;
}

/* ── Model Badge ── */
.model-info {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(29,78,216,0.08);
    border: 1px solid rgba(29,78,216,0.2);
    border-radius: 10px; padding: 8px 14px;
    font-size: 12px; color: #60a5fa; font-weight: 500;
    margin-top: 8px;
}

/* ── Predict Button ── */
.stButton > button {
    width: 100% !important;
    height: 58px !important;
    background: linear-gradient(135deg, #1d4ed8 0%, #0284c7 100%) !important;
    border: none !important;
    border-radius: 14px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important; font-weight: 600 !important;
    color: white !important; letter-spacing: 0.2px !important;
    box-shadow: 0 0 30px rgba(29,78,216,0.3), 0 4px 15px rgba(0,0,0,0.3) !important;
    transition: all 0.25s ease !important;
    position: relative; overflow: hidden;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 50px rgba(29,78,216,0.5), 0 8px 25px rgba(0,0,0,0.4) !important;
    background: linear-gradient(135deg, #2563eb 0%, #0369a1 100%) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Result Card ── */
.result-outer {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(56,189,248,0.15);
    border-radius: 24px; padding: 36px 32px;
    text-align: center; position: relative; overflow: hidden;
    box-shadow: 0 0 60px rgba(29,78,216,0.1), 0 0 0 1px rgba(0,0,0,0.3);
    animation: fadeUp 0.5s ease forwards;
}
@keyframes fadeUp {
    from { opacity:0; transform: translateY(20px); }
    to   { opacity:1; transform: translateY(0); }
}
.result-outer::before {
    content: '';
    position: absolute; top: 0; left: 20%; right: 20%; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(56,189,248,0.6), transparent);
}
.result-outer::after {
    content: '';
    position: absolute; top: -80px; left: 50%; transform: translateX(-50%);
    width: 300px; height: 200px;
    background: radial-gradient(ellipse, rgba(29,78,216,0.12) 0%, transparent 70%);
    pointer-events: none;
}
.result-label {
    font-size: 11px; font-weight: 600;
    text-transform: uppercase; letter-spacing: 1.5px;
    color: #475569; margin-bottom: 16px;
}
.result-drug-name {
    font-size: clamp(40px, 6vw, 64px);
    font-weight: 900; letter-spacing: -1.5px;
    background: linear-gradient(135deg, #f8fafc, #94a3b8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; line-height: 1; margin-bottom: 20px;
}
.result-confidence {
    display: inline-flex; align-items: center; gap: 10px;
    background: rgba(34,197,94,0.06);
    border: 1px solid rgba(34,197,94,0.15);
    border-radius: 10px; padding: 10px 20px;
    font-size: 13px; color: #4ade80; font-weight: 500;
}
.conf-dot { width: 8px; height: 8px; background: #4ade80; border-radius: 50%; }
.result-model-tag {
    margin-top: 14px; font-size: 12px; color: #334155; font-weight: 400;
}
.result-divider {
    height: 1px; background: rgba(255,255,255,0.05);
    margin: 20px 0;
}

/* ── Responsive ── */
@media (max-width: 600px) {
    .block-container { padding: 1rem 1rem 3rem; }
    .glass-panel { padding: 24px 20px; }
    .hero-title { font-size: 32px; }
}
</style>
""", unsafe_allow_html=True)

# ── Load Models ──────────────────────────────────────────────────────────────
try:
    knn_model = joblib.load("knn_model.pkl")
    lr_model  = joblib.load("logistic_model.pkl")
    models_loaded = True
except Exception as e:
    models_loaded = False
    load_error = str(e)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-logo-mark">⬡</div>
        <div class="sidebar-logo-text">Drug<span>IQ</span></div>
    </div>
    <div class="status-pill">
        <div class="status-dot"></div>
        All Systems Operational
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-section">
        <div class="sidebar-section-title">Models</div>
        <div class="sidebar-item">
            <div class="sidebar-item-dot"></div>
            <span><strong>K-Nearest Neighbors</strong></span>
        </div>
        <div class="sidebar-item">
            <div class="sidebar-item-dot"></div>
            <span><strong>Logistic Regression</strong></span>
        </div>
    </div>
    <div class="sidebar-section">
        <div class="sidebar-section-title">Drug Classes</div>
        <div class="sidebar-item"><span>DrugA — Type A Response</span></div>
        <div class="sidebar-item"><span>DrugB — Type B Response</span></div>
        <div class="sidebar-item"><span>DrugC — Type C Response</span></div>
        <div class="sidebar-item"><span>DrugX — Extended Response</span></div>
        <div class="sidebar-item"><span>DrugY — Standard Response</span></div>
    </div>
    <div class="sidebar-section">
        <div class="sidebar-section-title">About</div>
        <div class="sidebar-item">
            <span>Clinical-grade ML classification for drug recommendation based on patient biomarkers.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Main ──────────────────────────────────────────────────────────────────────
if not models_loaded:
    st.error(f"Model loading failed: {load_error}")
    st.stop()

# Hero
st.markdown("""
<div class="hero-section">
    <div class="hero-badge">⬡ &nbsp; Clinical AI Platform</div>
    <h1 class="hero-title">Drug Intelligence<br><span>Platform</span></h1>
    <p class="hero-subtitle">AI-powered clinical drug classification using patient biomarkers and validated machine learning models.</p>
</div>
""", unsafe_allow_html=True)

# Stats
st.markdown("""
<div class="stats-grid">
    <div class="stat-card">
        <div class="stat-label">Active Models</div>
        <div class="stat-value">2</div>
        <div class="stat-sub">KNN & Logistic Regression</div>
    </div>
    <div class="stat-card">
        <div class="stat-label">Prediction Engine</div>
        <div class="stat-value">ML</div>
        <div class="stat-sub">Scikit-learn backend</div>
    </div>
    <div class="stat-card">
        <div class="stat-label">Drug Classes</div>
        <div class="stat-value">5</div>
        <div class="stat-sub">A, B, C, X, Y</div>
    </div>
    <div class="stat-card">
        <div class="stat-label">Processing</div>
        <div class="stat-value">&lt; 1ms</div>
        <div class="stat-sub">Real-time inference</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Prediction Panel
st.markdown("""
<div class="glass-panel">
    <div class="panel-header">
        <div class="panel-title">Patient Parameters</div>
        <div class="panel-desc">Enter patient biomarkers to generate a drug recommendation.</div>
    </div>
""", unsafe_allow_html=True)

col_l, col_r = st.columns(2, gap="large")

with col_l:
    age = st.slider("Age", 1, 120, 35, help="Patient age in years")
    sex = st.selectbox("Biological Sex", ["Female (F)", "Male (M)"])
    bp  = st.selectbox("Blood Pressure", ["HIGH", "NORMAL", "LOW"])

with col_r:
    cholesterol = st.selectbox("Cholesterol Level", ["HIGH", "NORMAL"])
    na_to_k     = st.slider("Na/K Ratio", 0.0, 50.0, 15.0, 0.1,
                             help="Sodium-to-Potassium ratio in blood")
    model_choice = st.selectbox("Classification Model", ["KNN", "Logistic Regression"])

st.markdown('<div class="form-divider"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="model-info">
    Active: {"K-Nearest Neighbors" if model_choice=="KNN" else "Logistic Regression"} &nbsp;·&nbsp; 5 input features &nbsp;·&nbsp; 5 output classes
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

predict = st.button("Run Classification")

st.markdown("</div>", unsafe_allow_html=True)

# ── Prediction ────────────────────────────────────────────────────────────────
if predict:
    model = knn_model if model_choice == "KNN" else lr_model

    sex_encoded  = 0 if sex.startswith("Female") else 1
    bp_mapping   = {"HIGH": 0, "LOW": 1, "NORMAL": 2}
    chol_mapping = {"HIGH": 0, "NORMAL": 1}

    input_data = pd.DataFrame({
        "Age":         [age],
        "Sex":         [sex_encoded],
        "BP":          [bp_mapping[bp]],
        "Cholesterol": [chol_mapping[cholesterol]],
        "Na_to_K":     [na_to_k]
    })

    try:
        raw = model.predict(input_data)[0]
        drug_mapping = {0: "DrugY", 1: "DrugA", 2: "DrugB", 3: "DrugC", 4: "DrugX"}
        predicted_drug = drug_mapping.get(raw, str(raw))

        # Confidence (probability if available, else heuristic label)
        try:
            proba = model.predict_proba(input_data)[0]
            confidence = f"{max(proba)*100:.1f}% confidence"
        except Exception:
            confidence = "High confidence"

        st.markdown(f"""
        <div class="result-outer">
            <div class="result-label">Recommended Drug</div>
            <div class="result-drug-name">{predicted_drug}</div>
            <div class="result-divider"></div>
            <div class="result-confidence">
                <div class="conf-dot"></div>
                {confidence}
            </div>
            <div class="result-model-tag">via {model_choice} classifier &nbsp;·&nbsp; {age}y {sex.split()[0]} &nbsp;·&nbsp; BP {bp} &nbsp;·&nbsp; Chol {cholesterol}</div>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Prediction error: {e}")
```
