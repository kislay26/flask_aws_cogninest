"""
Step 1: Data Collection (Raw Data)
----------------------------------
Downloads the IMDB movie reviews dataset from Hugging Face,
converts numeric labels to sentiment strings ("positive"/"negative"),
and saves the raw data as CSV files in the 'data' folder.
Usage:
    python data_collection.py
"""

import os
from datasets import load_dataset
import pandas as pd

# Create the data directory if it doesn't exist
DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def main():
    # Load the IMDB dataset from Hugging Face.
    dataset = load_dataset("imdb")
    
    # Convert the 'train' and 'test' splits to Pandas DataFrames.
    train_df = pd.DataFrame(dataset["train"])
    test_df = pd.DataFrame(dataset["test"])
    
    # Convert numeric labels: 0 -> negative, 1 -> positive.
    train_df['sentiment'] = train_df['label'].apply(lambda x: 'negative' if x == 0 else 'positive')
    test_df['sentiment'] = test_df['label'].apply(lambda x: 'negative' if x == 0 else 'positive')
    
    # Rename "text" column to "review_text".
    train_df = train_df.rename(columns={'text': 'review_text'})
    test_df = test_df.rename(columns={'text': 'review_text'})
    
    # Drop redundant "label" column.
    train_df = train_df.drop(columns=['label'])
    test_df = test_df.drop(columns=['label'])
    
    # Save DataFrames to CSV files in the data directory.
    train_csv = os.path.join(DATA_DIR, "imdb_train.csv")
    test_csv = os.path.join(DATA_DIR, "imdb_test.csv")
    train_df.to_csv(train_csv, index=False)
    test_df.to_csv(test_csv, index=False)
    
    print(f"Raw data collection complete. Files saved as '{train_csv}' and '{test_csv}'.")

if __name__ == "__main__":
    main()
