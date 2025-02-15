"""
Optimized Flask Application for Sentiment Analysis with HTML UI
----------------------------------------------------------------
This Flask app loads the pre-trained sentiment analysis model (from the 'data' folder)
and serves it via two endpoints:
  - GET /       -> renders an HTML form for user input.
  - POST /predict -> returns the sentiment prediction as JSON.
Usage:
    python app.py
"""

import os
from flask import Flask, request, jsonify, render_template
import joblib
import re
import string
import logging

app = Flask(__name__)

# Set up logging.
logging.basicConfig(level=logging.INFO)

# Precompile regex and translation table.
HTML_TAG_PATTERN = re.compile(r'<.*?>')
TRANSLATION_TABLE = str.maketrans('', '', string.punctuation)

def clean_text(text: str) -> str:
    text = text.lower()
    text = HTML_TAG_PATTERN.sub('', text)
    text = text.translate(TRANSLATION_TABLE)
    return text

# Define data directory and model file path.
DATA_DIR = "data"
MODEL_FILE = os.path.join(DATA_DIR, "sentiment_model.pkl")

# Load the trained model at startup.
try:
    model = joblib.load(MODEL_FILE)
    logging.info("Model loaded successfully from %s.", MODEL_FILE)
except Exception as e:
    logging.error("Error loading model: %s", e)
    model = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    data = request.get_json(force=True)
    review_text = data.get("review_text", None)
    
    if not review_text:
        return jsonify({"error": "No review_text provided"}), 400
    
    cleaned_text = clean_text(review_text)
    try:
        prediction = model.predict([cleaned_text])[0]
    except Exception as e:
        logging.error("Prediction error: %s", e)
        return jsonify({"error": "Prediction failed"}), 500
    
    return jsonify({"sentiment_prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
