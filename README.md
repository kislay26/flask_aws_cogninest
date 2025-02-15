# Flask AWS Cogninest - Sentiment Analysis

**Flask AWS Cogninest** is a Flask-based sentiment analysis application that classifies IMDB movie reviews as positive or negative. It follows a complete end-to-end machine learning pipeline, including data collection, database management, data cleaning, exploratory data analysis (EDA), model training, and deployment. The model is deployed using Flask with an interactive UI and can be hosted on an AWS EC2 instance.

## 📌 Features

✅ **End-to-End Machine Learning Pipeline:** From raw data to deployed model.  
✅ **Database Integration:** SQLite database for structured storage of reviews.  
✅ **Web Interface:** Interactive Bootstrap-based HTML UI for easy sentiment prediction.  
✅ **REST API:** Provides a `/predict` endpoint for automated sentiment analysis.  
✅ **AWS EC2 Deployment:** Configured for cloud hosting.  

## 🗂 Directory Structure

```
.
├── 01_data_collections.py      # Downloads IMDB dataset & saves as CSV
├── 02_database_setup.py        # Creates & loads SQLite database
├── 03_data_cleaning.py         # Cleans review text & generates cleaned CSV
├── 04_model_training.py        # Trains Logistic Regression model & saves it
├── app.py                      # Flask web app with API & UI
├── templates/
│   ├── index.html              # User-friendly web UI
├── requirements.txt            # Python dependencies
├── .gitignore                  # Ignores unnecessary files in Git
└── README.md                   # Project documentation
```

## 🛠 Prerequisites

Ensure you have the following installed:

- **Python 3.7+**
- **Git**
- **AWS EC2 instance (Ubuntu 20.04)**
- **VS Code** or any preferred code editor

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/kislay26/flask_aws_cogninest.git
cd flask_aws_cogninest
```

### 2️⃣ Create & Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # For macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔧 Running the Project Locally

### 📌 Step 1: Data Collection

```bash
python 01_data_collections.py
```

### 📌 Step 2: Database Setup

```bash
python 02_database_setup.py
```

### 📌 Step 3: Data Cleaning

```bash
python 03_data_cleaning.py
```

### 📌 Step 4: Model Training

```bash
python 04_model_training.py
```

### 📌 Step 5: Run the Flask App

```bash
python app.py
```

### 📌 Step 6: Open the Application

Navigate to **`http://127.0.0.1:5000/`** in your web browser.

## ☁️ Deploying on AWS EC2



## 🛠 Technologies Used

- **Flask** - Backend API
- **Scikit-learn** - Machine Learning Model
- **Pandas & Matplotlib** - Data Processing & Visualization
- **Bootstrap & Font Awesome** - Front-end UI
- **AWS EC2** - Cloud Deployment

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 📩 Contact

For queries or further details, reach out:

**Name**  
📧 Kislay Krishna  

