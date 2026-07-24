import joblib
import pandas as pd

# ==========================================
# Load Model, Scaler and Feature Names
# ==========================================

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_names = joblib.load("models/feature_names.pkl")


def predict_dataframe(df):
    """
    Predict phishing status for a DataFrame.
    """

    # Keep only required features in correct order
    X = df[feature_names]

    # Scale data
    X_scaled = scaler.transform(X)

    # Predict
    predictions = model.predict(X_scaled)

    # Confidence
    probabilities = model.predict_proba(X_scaled)
    confidence = probabilities.max(axis=1) * 100

    # Convert labels
    prediction_labels = [
        "Legitimate" if p == 0 else "Phishing"
        for p in predictions
    ]

    return prediction_labels, confidence