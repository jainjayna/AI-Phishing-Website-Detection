# 🛡️ AI-Powered Phishing Website Detection System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![SHAP](https://img.shields.io/badge/Explainability-SHAP-red)
![LIME](https://img.shields.io/badge/Explainability-LIME-green)
![Render](https://img.shields.io/badge/Deployment-Render-purple)

</p>

<p align="center">

A Flask-based Machine Learning web application that detects phishing websites using a trained Random Forest Classifier and provides Explainable AI using SHAP and LIME.

</p>

---

# 🌐 Live Demo

### 🚀 https://ai-phishing-website-detection-hms9.onrender.com

---

# 📑 Table of Contents

- Project Overview
- Features
- Technologies Used
- Machine Learning Workflow
- Dataset
- Model Performance
- Explainable AI
- Important Features
- Application Screenshot
- Installation
- Project Structure
- Future Improvements
- Author

---

# 📌 Project Overview

Phishing attacks are among the most common cybersecurity threats affecting individuals and organizations worldwide.

This project uses Machine Learning to classify websites as **Legitimate** or **Phishing** based on engineered website features extracted from URLs and webpage characteristics.

The application provides an intuitive web interface for uploading datasets, viewing predictions, downloading results, and understanding model decisions through Explainable AI techniques.

---

# ✨ Features

- Upload CSV Dataset
- Predict Phishing Websites
- Confidence Score
- Random Forest Classifier
- SHAP Explainability
- LIME Explainability
- Feature Importance Visualization
- Confusion Matrix
- ROC Curve
- Prediction Summary Dashboard
- Download Prediction Results
- Professional Flask UI
- Responsive Design

---

# 🛠️ Technologies Used

## Frontend

- HTML5
- CSS3
- Jinja2

## Backend

- Flask
- Python

## Machine Learning

- Scikit-Learn
- Random Forest Classifier
- SHAP
- LIME

## Data Analysis

- Pandas
- NumPy

## Visualization

- Matplotlib

## Deployment

- Render

---

# 🧠 Machine Learning Workflow

```text
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Selection
      │
      ▼
Train-Test Split
      │
      ▼
Feature Scaling
      │
      ▼
Random Forest Training
      │
      ▼
Model Evaluation
      │
      ▼
Predictions
      │
      ▼
SHAP + LIME Explainability
      │
      ▼
Flask Deployment
```

---

# 📊 Dataset

The model is trained on a phishing website dataset containing engineered website features such as:

- Google Index
- Page Rank
- Number of Hyperlinks
- Domain Age
- Safe Anchor Ratio
- External Hyperlink Ratio
- URL Features
- HTML Features
- Domain Properties

### Target Classes

- Legitimate Website
- Phishing Website

---

# 🤖 Machine Learning Model

| Model | Random Forest Classifier |
|--------|--------------------------|
| Accuracy | **96.02%** |
| Explainability | SHAP + LIME |
| Output | Legitimate / Phishing |

---

# 📈 Explainable AI

This project incorporates Explainable Artificial Intelligence (XAI) techniques to improve transparency and interpretability.

## SHAP

- Global feature importance
- Feature contribution analysis
- Summary Plot

## LIME

- Local prediction explanations
- Instance-level interpretation
- Positive and negative feature contributions

---

# 📊 Most Important Features

| Rank | Feature |
|------|---------|
| 1 | Google Index |
| 2 | Page Rank |
| 3 | Number of Hyperlinks |
| 4 | Web Traffic |
| 5 | Number of WWW |
| 6 | External Hyperlink Ratio |
| 7 | Domain Age |
| 8 | Phish Hints |
| 9 | Safe Anchor |
| 10 | Internal Hyperlink Ratio |

---

# 📸 Application Screenshot

## 🏠 Home Page

<p align="center">
    <img src="./static/images/home_page.png" alt="Home Page" width="900">
</p>

The Home Page serves as the landing page of the AI-Powered Phishing Website Detection System. It provides users with a clean and modern interface, introduces the project, and allows easy navigation to the prediction, explainability, reports, and about pages.

---

# 📂 Project Structure

```text
AI-Phishing-Website-Detection
│
├── app.py
├── prediction.py
├── requirements.txt
├── runtime.txt
├── Procfile
│
├── models/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── feature_names.pkl
│
├── feature_extraction/
│
├── explainability/
│
├── static/
│   ├── css/
│   └── images/
│       └── home_page.png
│
└── templates/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/jainjayna/AI-Phishing-Website-Detection.git
```

Navigate to the project

```bash
cd AI-Phishing-Website-Detection
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it (Windows)

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```text
http://127.0.0.1:5000
```

---

# 🚀 Future Improvements

- Real-time URL Feature Extraction
- URL Prediction without CSV Upload
- Deep Learning Models
- Browser Extension
- REST API
- User Authentication
- Interactive Plotly Dashboard
- Docker Support

---

# 👩‍💻 Author

## Jayna Jain

Commerce Student | Data Science & AI Enthusiast

**GitHub:**  
https://github.com/jainjayna

---

# ⭐ If you found this project useful, consider giving it a Star!

It helps others discover the project and supports my work.

---

# 📄 License

This project is intended for educational and portfolio purposes.
