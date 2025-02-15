"""
Step: Model Training and Evaluation (Using Intermediate Data)
-----------------------------------------------------------------
Trains a sentiment analysis model (Logistic Regression with TF-IDF features) on the cleaned data,
evaluates the model, and saves the trained pipeline as 'sentiment_model.pkl' in the 'data' folder.
Usage:
    python model_training.py
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import joblib

DATA_DIR = "data"
CLEANED_CSV = os.path.join(DATA_DIR, "imdb_reviews_cleaned.csv")
MODEL_FILE = os.path.join(DATA_DIR, "sentiment_model.pkl")

def load_data():
    df = pd.read_csv(CLEANED_CSV)
    return df['cleaned_review'], df['sentiment']

def main():
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                        random_state=42, stratify=y)
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression(max_iter=1000))
    ])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    print("Evaluation Metrics on Test Set:")
    print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred, pos_label='positive'):.4f}")
    print(f"Recall   : {recall_score(y_test, y_pred, pos_label='positive'):.4f}")
    print(f"F1 Score : {f1_score(y_test, y_pred, pos_label='positive'):.4f}\n")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    joblib.dump(pipeline, MODEL_FILE)
    print(f"Trained model saved as '{MODEL_FILE}'.")

if __name__ == "__main__":
    main()
