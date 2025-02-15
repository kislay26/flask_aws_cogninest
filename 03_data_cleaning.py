"""
Step: Data Cleaning (Intermediate Data)
-----------------------------------------
Connects to the SQLite database (imdb_reviews.db in 'data' folder), cleans the review text,
and saves an intermediate CSV file (imdb_reviews_cleaned.csv) in the 'data' folder.
The raw data remains unchanged.
Usage:
    python data_cleaning.py
"""

import os
import sqlite3
import pandas as pd
import re
import string

DATA_DIR = "data"
DB_FILE = os.path.join(DATA_DIR, "imdb_reviews.db")
OUTPUT_CSV = os.path.join(DATA_DIR, "imdb_reviews_cleaned.csv")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def load_data_from_db(db_file):
    conn = sqlite3.connect(db_file)
    query = "SELECT id, review_text, sentiment FROM imdb_reviews"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def main():
    df = load_data_from_db(DB_FILE)
    df['cleaned_review'] = df['review_text'].apply(clean_text)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Data cleaning complete. Cleaned data saved as '{OUTPUT_CSV}'.")

if __name__ == "__main__":
    main()
