import streamlit as st
import requests
from PyPDF2 import PdfReader
import sqlite3
from googletrans import Translator
from gtts import gTTS
import openai
import os
import tempfile
import random

# Set OpenAI API Key
openai.api_key = 'your_openai_api_key_here'  # Replace with your OpenAI API key

# News API Key
API_KEY = "pub_60208bd691345e57519b7d614bf21139f26f7"
BASE_URL = "https://newsdata.io/api/1/news"

# Database Setup
conn = sqlite3.connect("upsc_app.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS notes (topic TEXT, content TEXT)")
conn.commit()

# Initialize Translator for multilingual support
translator = Translator()

# Prelims Questions
def get_mock_test_questions():
    """Fetch UPSC Prelims questions for Mock Test"""
    prelims_questions = [
        {
            "question": "Which Article of the Indian Constitution guarantees the Right to Equality?",
            "options": ["Article 14", "Article 19", "Article 21", "Article 25"],
            "answer": "Article 14"
        },
        {
            "question": "The concept of 'Carbon Credit' originated from which protocol?",
            "options": ["Kyoto Protocol", "Montreal Protocol", "Geneva Protocol", "Nagoya Protocol"],
            "answer": "Kyoto Protocol"
        },
        {
            "question": "Which Indian river is also known as the 'Sorrow of Bihar'?",
            "options": ["Ganga", "Kosi", "Yamuna", "Brahmaputra"],
            "answer": "Kosi"
        },
        {
            "question": "What is the primary objective of the Green Revolution?",
            "options": ["Increase food grain production", "Afforestation", "Soil conservation", "Irrigation development"],
            "answer": "Increase food grain production"
        },
        # Add more questions here...
    ]
    return random.sample(prelims_questions, k=min(len(prelims_questions), 100))  # Ensure a max of 100 questions

# Helper Functions
def fetch_news(category):
    """Fetch news based on category using News API"""
    params = {
        "apikey": API_KEY,
        "country": "in",
        "language": "en",
        "category": category,
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching news: {e}")
        return {}

# Streamlit App
st.title("UPSC Preparation Hub")

# Tabbed Interface
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📢 Current Affairs", "📚 Topic Summarization", "📝 Mock Tests", "💡 Saved Notes", "📝 Essay Feedback"])

# 1. Current Affairs
with tab1:
    st.header("Daily Current Affairs")
    CATEGORIES = ["politics", "economy", "environment", "science", "world"]
    category = st.selectbox("Select News Category", CATEGORIES)

    if st.button("Fetch News"):
        news_data = fetch_news(category)
        if "results" in news_data:
            st.subheader(f"News for {category.capitalize()}:")
            for article in news_data["results"][:5]:  # Display top 5 articles
                st.write(f"**{article['title']}**")
                st.write(article.get("description", "No description available."))
                st.write(f"[Read more]({article['link']})")
                st.write("---")
        else:
            st.error("No news available for this category. Please try again later.")

# 2. Topic Summarization
with tab2:
    st.header("Topic Summarizer")
    uploaded_file = st.file_uploader("Upload a PDF/Text file", type=["pdf", "txt"])
    lang = st.selectbox("Select Language for Summary and Explanation", ["English", "Telugu", "Hindi", "Tamil", "Marathi"])

    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            pdf = PdfReader(uploaded_file)
            text = " ".join(page.extract_text() for page in pdf.pages)
        else:
            text = uploaded_file.read().decode("utf-8")

        st.write("**Extracted Text:**")
        st.write(text)

# 3. Mock Test
with tab3:
    st.header("Mock Test")

    questions = get_mock_test_questions()
    score = 0
    answers = []
    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}: {q['question']}")
        user_answer = st.radio("Options", q["options"], key=f"q{i}")
        answers.append({"question": q['question'], "user_answer": user_answer, "correct_answer": q['answer']})
        if user_answer == q["answer"]:
            score += 1

    if st.button("Submit Quiz"):
        st.write(f"Your score: {score}/{len(questions)}")
        
        # Feedback on the score
        if score >= 90:
            st.success("Excellent performance! Keep it up.")
        elif score >= 70:
            st.info("Good job! You’re doing well, but there’s room for improvement.")
        else:
            st.warning("Don't worry, keep practicing! Focus on weak areas.")

        # Displaying answers and feedback
        for ans in answers:
            st.write(f"Question: {ans['question']}")
            st.write(f"Your answer: {ans['user_answer']}")
            st.write(f"Correct answer: {ans['correct_answer']}")
            st.write("---")

# 4. Saved Notes
with tab4:
    st.header("Saved Notes")
    cur.execute("SELECT * FROM notes")
    notes = cur.fetchall()
    if notes:
        for note in notes:
            st.write(f"**{note[0]}**")
            st.write(note[1])
            st.write("---")
    else:
        st.write("No saved notes yet.")

# 5. Essay Feedback
with tab5:
    st.header("Essay Feedback")
    essay_text = st.text_area("Write your essay here...", height=200)

    if st.button("Evaluate Essay"):
        st.write("Essay evaluation feature will be added soon.")
