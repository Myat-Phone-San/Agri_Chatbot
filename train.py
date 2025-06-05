# train.py

import mysql.connector
from db_config import db_settings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

def load_data():
    conn = mysql.connector.connect(**db_settings)
    cursor = conn.cursor()
    # Join keywords, questions, answers
    cursor.execute("""
        SELECT q.question_text, a.answer_text
        FROM questions q
        JOIN answers a ON q.id = a.question_id
    """)
    data = cursor.fetchall()
    conn.close()
    if not data:
        raise ValueError("No training data found in DB")
    questions, answers = zip(*data)
    return questions, answers

def train_and_save():
    questions, answers = load_data()
    vectorizer = TfidfVectorizer(token_pattern=r'\b\w+\b', max_features=1000)
    X = vectorizer.fit_transform(questions)
    model = LogisticRegression(max_iter=200)
    model.fit(X, answers)
    joblib.dump(model, "model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")
    print("✅ Model trained and saved.")

if __name__ == "__main__":
    train_and_save()
