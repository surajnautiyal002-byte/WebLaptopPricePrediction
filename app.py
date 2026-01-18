from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # enable CORS for frontend access

# Load trained ML model
model = joblib.load("laptop_price_model.pkl")


@app.route("/", methods=["GET"])
def home():
    return "Laptop Price Prediction API is running"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        # IMPORTANT:
        # Feature names MUST match training data exactly
        df = pd.DataFrame([{
            "Inches": data["inch"],
            "Ram": data["ram"],
            "Weight": data["weight"],
            "TotalMemory": data["total_memory"],
            "CpuTier": data["cpu_tier"],
            "GpuTier": data["gpu_tier"],
            "TotalPixels": data["total_pixels"]
        }])

        prediction = model.predict(df)[0]

        return jsonify({
            "predicted_price": float(prediction)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


# REQUIRED FOR RENDER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
