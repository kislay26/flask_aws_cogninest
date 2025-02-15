"""
Step 2: Database Setup (Raw Data)
----------------------------------
Deletes any existing SQLite database, creates a new one (imdb_reviews.db) in the 'data' folder,
and loads raw data from the CSV files into the 'imdb_reviews' table.
Usage:
    python database_setup.py
"""

import os
import sqlite3
import pandas as pd

# Define the data directory and create it if necessary.
DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def create_connection(db_file):
    return sqlite3.connect(db_file)

def create_table(conn):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS imdb_reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        review_text TEXT NOT NULL,
        sentiment TEXT NOT NULL
    );
    """
    cur = conn.cursor()
    cur.execute(create_table_sql)
    conn.commit()

def insert_data(conn, csv_file):
    df = pd.read_csv(csv_file)
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute("INSERT INTO imdb_reviews (review_text, sentiment) VALUES (?, ?)",
                    (row['review_text'], row['sentiment']))
    conn.commit()

def main():
    db_file = os.path.join(DATA_DIR, "imdb_reviews.db")
    
    # Delete the existing database file if it exists.
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Existing database '{db_file}' deleted.")
        
    conn = create_connection(db_file)
    create_table(conn)
    
    # Insert data from both train and test CSV files.
    train_csv = os.path.join(DATA_DIR, "imdb_train.csv")
    test_csv = os.path.join(DATA_DIR, "imdb_test.csv")
    insert_data(conn, train_csv)
    insert_data(conn, test_csv)
    
    conn.close()
    print(f"Database setup complete. Raw data inserted into '{db_file}'.")

if __name__ == "__main__":
    main()
