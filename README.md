# 🛡️ SpamShield AI

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&weight=700&size=34&duration=3000&pause=1000&color=00E5FF&center=true&vCenter=true&width=1000&lines=SpamShield+AI;Advanced+SMS+Spam+Detection+System;Machine+Learning+Powered+Cyber+Security;Built+With+Python+%7C+Streamlit+%7C+Scikit-Learn" />

<br>

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red?style=for-the-badge\&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge\&logo=scikitlearn)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production-success?style=for-the-badge)

</div>

---

## 🚀 Overview

SpamShield AI is an advanced Machine Learning-powered SMS Spam Detection platform designed to identify spam, phishing attempts, fraudulent messages, and malicious SMS content in real-time.

The system leverages Natural Language Processing (NLP) and Machine Learning techniques to provide accurate classification of SMS messages as:

* ✅ Legitimate (Ham)
* 🚨 Spam
* 🔒 Potentially Fraudulent

---

## ✨ Features

### 🤖 AI Detection Engine

* Real-Time SMS Classification
* TF-IDF Text Vectorization
* Multinomial Naive Bayes Model
* Confidence Score Analysis
* Spam Risk Assessment

### 📊 Analytics Dashboard

* Total Messages Scanned
* Spam vs Ham Statistics
* Interactive Visualizations
* Prediction History Tracking
* Detection Trends

### 📂 Bulk Scanner

* Upload CSV Files
* Analyze Thousands of Messages
* Batch Processing
* Export Results

### ☁ NLP Insights

* Word Cloud Generation
* Keyword Analysis
* Message Pattern Discovery
* Text Distribution Insights

### 📈 Model Performance

* Accuracy Metrics
* Precision Analysis
* Recall Evaluation
* F1 Score Tracking

---

## 🏗️ System Architecture

```text
SMS Message
     │
     ▼
Text Preprocessing
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Machine Learning Model
     │
     ▼
Spam / Ham Prediction
     │
     ▼
Analytics Dashboard
```

---

## 📊 Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 97.1% |
| Precision | 100%  |
| Recall    | 79.3% |
| F1 Score  | 88.4% |

---

## 🛠️ Tech Stack

### Frontend

* Streamlit
* Plotly

### Backend

* Python

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorizer
* Multinomial Naive Bayes

### Data Processing

* Pandas
* NumPy
* NLTK

---

## 📂 Project Structure

```text
spam_sms_detection/
│
├── app.py
├── spam_model.pkl
├── vectorizer.pkl
├── history.csv
│
├── pages/
│   ├── 1_Detector.py
│   ├── 2_Analytics.py
│   ├── 3_Bulk_Scanner.py
│   ├── 4_NLP_Insights.py
│   ├── 5_Model_Performance.py
│   └── 6_About.py
│
├── data/
│   └── spam.csv
│
├── requirements.txt
└── README.md
```

---

## ⚡ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/spamshield-ai.git
cd spamshield-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m streamlit run app.py
```

---

## 🎯 Sample Spam Message

```text
Congratulations! You have won a FREE iPhone 16.
Click here now to claim your reward.
```

### Prediction

```text
🚨 SPAM DETECTED
Confidence: 98.7%
```

---

## 🔥 Future Enhancements

* Deep Learning Models
* BERT-Based Classification
* Real-Time API
* Email Spam Detection
* WhatsApp Spam Detection
* PDF Report Generation
* User Authentication
* Cloud Deployment

---

## 👨‍💻 Developer

# Archit Deep

### Computer Science Student

AI / ML Enthusiast • Full Stack Developer • Cyber Security Learner

Passionate about:

* Artificial Intelligence
* Machine Learning
* Natural Language Processing
* Data Science
* Cyber Security
* Modern Web Development

---

## 🌟 Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

📢 Share it with others

---

<div align="center">

### 🛡️ SpamShield AI

Intelligent SMS Security Powered by Machine Learning

Made with ❤️ by Archit Deep

</div>
