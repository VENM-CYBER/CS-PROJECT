import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from datetime import datetime
from streamlit_option_menu import option_menu

# ==========================================================
# CONFIG
# ==========================================================

st.set_page_config(
    page_title="SpamShield AI",
    page_icon="🛡️",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "spam_model.pkl"
VECTORIZER_PATH = BASE_DIR / "vectorizer.pkl"
HISTORY_PATH = BASE_DIR / "history.csv"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
135deg,
#020617 0%,
#0f172a 50%,
#111827 100%
);
color:white;
}

.title{
font-size:60px;
font-weight:800;
text-align:center;
color:white;
}

.subtitle{
text-align:center;
font-size:18px;
color:#94a3b8;
margin-bottom:30px;
}

.metric-card{
background:rgba(255,255,255,0.05);
padding:20px;
border-radius:20px;
border:1px solid rgba(255,255,255,0.08);
text-align:center;
}

.result-safe{
background:#14532d;
padding:20px;
border-radius:15px;
font-size:24px;
font-weight:bold;
color:white;
}

.result-spam{
background:#7f1d1d;
padding:20px;
border-radius:15px;
font-size:24px;
font-weight:bold;
color:white;
}

.block{
background:rgba(255,255,255,0.04);
padding:20px;
border-radius:20px;
border:1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HISTORY FUNCTIONS
# ==========================================================

def save_prediction(message, prediction, spam_score):

    row = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Message": message,
        "Prediction": prediction,
        "Spam Score": round(spam_score, 2)
    }

    df = pd.DataFrame([row])

    if HISTORY_PATH.exists():
        df.to_csv(
            HISTORY_PATH,
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(
            HISTORY_PATH,
            index=False
        )

def load_history():

    if HISTORY_PATH.exists():
        return pd.read_csv(HISTORY_PATH)

    return pd.DataFrame(
        columns=[
            "Time",
            "Message",
            "Prediction",
            "Spam Score"
        ]
    )

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/shield.png",
        width=80
    )

    selected = option_menu(
        menu_title="SpamShield AI",
        options=[
            "Detector",
            "Analytics",
            "History",
            "Bulk Scanner",
            "About"
        ],
        icons=[
            "shield-check",
            "bar-chart",
            "clock-history",
            "file-earmark-arrow-up",
            "info-circle"
        ],
        default_index=0
    )

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    "<div class='title'>🛡️ SpamShield AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Advanced SMS Spam Detection & Fraud Analysis Platform</div>",
    unsafe_allow_html=True
)

# ==========================================================
# DETECTOR PAGE
# ==========================================================

if selected == "Detector":

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class='metric-card'>
        <h2>97.1%</h2>
        <p>Accuracy</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='metric-card'>
        <h2>100%</h2>
        <p>Precision</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='metric-card'>
        <h2>88.4%</h2>
        <p>F1 Score</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    message = st.text_area(
        "📨 Enter SMS Message",
        height=180,
        placeholder="Paste any SMS here..."
    )

    if st.button("🔍 Analyze Message", use_container_width=True):

        if message.strip():

            vector = vectorizer.transform([message])

            prediction = model.predict(vector)[0]

            probabilities = model.predict_proba(vector)[0]

            ham_score = float(probabilities[0] * 100)
            spam_score = float(probabilities[1] * 100)

            if prediction == 1:

                st.markdown(
                    f"""
                    <div class='result-spam'>
                    🚨 SPAM DETECTED<br><br>
                    Confidence: {spam_score:.2f}%
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                label = "Spam"

            else:

                st.markdown(
                    f"""
                    <div class='result-safe'>
                    ✅ LEGITIMATE MESSAGE<br><br>
                    Confidence: {ham_score:.2f}%
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                label = "Ham"

            save_prediction(
                message,
                label,
                spam_score
            )

            st.markdown("### Spam Risk Meter")

            gauge = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=spam_score,
                    title={"text":"Risk Score"},
                    gauge={
                        "axis":{"range":[0,100]},
                        "steps":[
                            {"range":[0,35],"color":"green"},
                            {"range":[35,70],"color":"orange"},
                            {"range":[70,100],"color":"red"}
                        ]
                    }
                )
            )

            st.plotly_chart(
                gauge,
                use_container_width=True
            )

            chart_df = pd.DataFrame({
                "Category":["Ham","Spam"],
                "Probability":[ham_score,spam_score]
            })

            fig = px.bar(
                chart_df,
                x="Category",
                y="Probability",
                title="Prediction Confidence"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

# ==========================================================
# ANALYTICS
# ==========================================================

elif selected == "Analytics":

    st.subheader("📊 Analytics Dashboard")

    hist = load_history()

    # Ensure required columns exist
    required_cols = [
        "Time",
        "Message",
        "Prediction",
        "Spam Score"
    ]

    if hist.empty:

        st.info("No prediction history available yet.")

    else:

        missing_cols = [
            col for col in required_cols
            if col not in hist.columns
        ]

        if missing_cols:

            st.error(
                f"History file is missing columns: {missing_cols}"
            )

            st.write("Current columns:")
            st.write(hist.columns.tolist())

        else:

            col1, col2, col3 = st.columns(3)

            spam_count = len(
                hist[hist["Prediction"] == "Spam"]
            )

            ham_count = len(
                hist[hist["Prediction"] == "Ham"]
            )

            col1.metric(
                "Total Predictions",
                len(hist)
            )

            col2.metric(
                "Spam Messages",
                spam_count
            )

            col3.metric(
                "Legitimate Messages",
                ham_count
            )

            import plotly.express as px

            pie = px.pie(
                hist,
                names="Prediction",
                title="Spam vs Ham Distribution"
            )

            st.plotly_chart(
                pie,
                use_container_width=True
            )
# ==========================================================
# HISTORY
# ==========================================================

elif selected == "History":

    st.subheader("🕒 Prediction History")

    hist = load_history()

    st.dataframe(
        hist,
        use_container_width=True
    )

    if len(hist) > 0:

        st.download_button(
            "⬇ Download History",
            hist.to_csv(index=False),
            "history.csv",
            "text/csv"
        )

# ==========================================================
# BULK SCANNER
# ==========================================================

elif selected == "Bulk Scanner":

    st.subheader("📂 Bulk SMS Scanner")

    uploaded = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if uploaded:

        data = pd.read_csv(uploaded)

        st.write("Preview")

        st.dataframe(
            data.head()
        )

        column = st.selectbox(
            "Select Message Column",
            data.columns
        )

        preds = model.predict(
            vectorizer.transform(
                data[column]
            )
        )

        data["Prediction"] = np.where(
            preds==1,
            "Spam",
            "Ham"
        )

        st.dataframe(
            data,
            use_container_width=True
        )

        st.download_button(
            "⬇ Download Results",
            data.to_csv(index=False),
            "bulk_results.csv",
            "text/csv"
        )

# ==========================================================
# ABOUT
# ==========================================================

elif selected == "About":

    st.subheader("ℹ About SpamShield AI")

    st.markdown("""
# 🛡️ SpamShield AI

SpamShield AI is an advanced Machine Learning-powered SMS Spam Detection platform designed to identify fraudulent and unwanted messages with high accuracy.

### 🚀 Key Features

- AI-Powered SMS Spam Detection
- TF-IDF Text Vectorization
- Multinomial Naive Bayes Classification
- Real-Time Spam Risk Analysis
- Interactive Analytics Dashboard
- Prediction History Tracking
- Bulk CSV Message Scanning
- Downloadable Reports
- Modern Cybersecurity-Themed Interface

### 📊 Model Performance

| Metric | Score |
|----------|----------|
| Accuracy | 97.1% |
| Precision | 100% |
| Recall | 79.3% |
| F1 Score | 88.4% |

### 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Plotly
- Joblib
- NLTK

### 👨‍💻 Developer

**Archit Deep**

Computer Science Student & AI/ML Enthusiast

Passionate about Machine Learning, Artificial Intelligence, Data Science, Cybersecurity, and Full-Stack Development. This project demonstrates the practical application of Natural Language Processing (NLP) and Machine Learning techniques for real-world spam detection systems.

### 🎯 Project Objective

To build a reliable and intelligent SMS filtering system capable of distinguishing legitimate messages from spam with high accuracy, helping users avoid scams, phishing attempts, and unwanted communications.

---

© 2026 Archit Deep | SpamShield AI
""")