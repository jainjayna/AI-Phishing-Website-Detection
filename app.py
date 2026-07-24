from flask import Flask, render_template, request, send_file
import pandas as pd
import matplotlib.pyplot as plt
import os

from prediction import predict_dataframe
from models.model_loader import load_model

app = Flask(__name__)

# Load model once
model = load_model()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        url = request.form["url"]

        prediction = "✅ Legitimate Website"
        confidence = 98.6

        return render_template(
            "result.html",
            url=url,
            prediction=prediction,
            confidence=confidence
        )

    return render_template("predict.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        file = request.files["file"]

        if file.filename == "":
            return "No file selected."

        try:

            df = pd.read_csv(file)

            predictions, confidence = predict_dataframe(df)

            df["Prediction"] = predictions
            df["Confidence (%)"] = confidence.round(2)

            # Save CSV
            os.makedirs("reports", exist_ok=True)
            os.makedirs(os.path.join("static", "images"), exist_ok=True)
            df.to_csv("reports/predictions.csv", index=False)

            # Dashboard Statistics
            total = len(df)
            legitimate = (df["Prediction"] == "Legitimate").sum()
            phishing = (df["Prediction"] == "Phishing").sum()
            average_confidence = round(df["Confidence (%)"].mean(), 2)

            # Create Pie Chart
            plt.figure(figsize=(5, 5))

            plt.pie(
                [legitimate, phishing],
                labels=["Legitimate", "Phishing"],
                autopct="%1.1f%%",
                startangle=90
            )

            plt.title("Prediction Summary")

            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            chart_path = os.path.join(
                BASE_DIR,
                "static",
                "images",
                "prediction_summary.png"
            )
            print("Saving chart to:", chart_path)
            plt.savefig(chart_path, bbox_inches="tight")
            plt.close()

            return render_template(
                "prediction_result.html",
                tables=[
                    df.to_html(
                        classes="table table-striped table-hover",
                        index=False
                    )
                ],
                total=total,
                legitimate=legitimate,
                phishing=phishing,
                average_confidence=average_confidence
            )

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("upload.html")


@app.route("/download")
def download():
    return send_file(
        "reports/predictions.csv",
        as_attachment=True
    )


@app.route("/explain")
def explain():
    return render_template("explain.html")


@app.route("/reports")
def reports():
    return render_template("reports.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(e):

    return render_template("404.html"),404



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)