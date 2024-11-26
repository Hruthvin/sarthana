import streamlit as st
import requests
from PyPDF2 import PdfReader
import sqlite3
from googletrans import Translator
from gtts import gTTS
from transformers import pipeline
import tempfile
import random

# Database Setup
conn = sqlite3.connect("upsc_app.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS notes (topic TEXT, content TEXT)")
conn.commit()

# Initialize Translator for multilingual support
translator = Translator()

# Helper Functions
def fetch_news(category):
    """Fetch news based on category using News API"""
    NEWS_API_KEY = "pub_60208bd691345e57519b7d614bf21139f26f7"
    NEWS_API_URL = "https://newsdata.io/api/1/news"
    params = {
        "apikey": NEWS_API_KEY,
        "country": "in",
        "language": "en",
        "category": category,
    }
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching news: {e}")
        return {}

def text_to_speech(text, lang_code="en"):
    """Convert text to speech and play it"""
    tts = gTTS(text=text, lang=lang_code)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        tts.save(temp_audio.name)
        st.audio(temp_audio.name, format="audio/mp3")

def generate_mock_questions_from_text(text):
    """Generate random questions from text using Transformers"""
    question_generator = pipeline("text2text-generation", model="valhalla/t5-small-qg-prepend")
    try:
        questions = question_generator(
            f"generate questions: {text}", max_length=512, num_return_sequences=10
        )
        mock_test = []
        for q in questions:
            question_text = q['generated_text']
            options = [
                "Option A",
                "Option B",
                "Option C",
                "Correct Answer"
            ]
            random.shuffle(options)
            mock_test.append((question_text, options, options[-1]))
        return mock_test
    except Exception as e:
        return f"Error during question generation: {e}"

# Streamlit App
st.title("UPSC Preparation Hub")

# Tabbed Interface
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📢 Current Affairs", "📚 Topic Summarization", "📝 Mock Tests", "💡 Saved Notes", "📝 Essay Writing"])

# 1. Current Affairs
with tab1:
    st.header("Daily Current Affairs")
    CATEGORIES = ["politics", "economy", "environment", "science", "world"]
    category = st.selectbox("Select News Category", CATEGORIES)

    if st.button("Fetch News"):
        news_data = fetch_news(category)
        if "results" in news_data:
            st.subheader(f"News for {category.capitalize()}:")
            for article in news_data["results"][:5]:
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

        if st.button("Summarize"):
            try:
                summary_pipeline = pipeline("summarization")
                summary = summary_pipeline(text, max_length=150, min_length=30, do_sample=False)
                summarized_text = summary[0]['summary_text']
                st.write("**Summary:**")
                st.write(summarized_text)
                lang_code = {"English": "en", "Telugu": "te", "Hindi": "hi", "Tamil": "ta", "Marathi": "mr"}.get(lang, "en")
                if st.button("Play Summary"):
                    text_to_speech(summarized_text, lang_code)
            except Exception as e:
                st.error(f"Error summarizing the text: {e}")

# 3. Mock Test
with tab3:
    st.header("Mock Test")
    uploaded_file = st.file_uploader("Upload a PDF for Mock Test", type=["pdf"])
    if uploaded_file:
        pdf = PdfReader(uploaded_file)
        text = " ".join(page.extract_text() for page in pdf.pages)

        st.write("**Extracted Text for Questions:**")
        st.write(text)

        if st.button("Generate Mock Test"):
            mock_questions = generate_mock_questions_from_text(text)
            if isinstance(mock_questions, str):
                st.error(mock_questions)
            else:
                st.write("### Mock Test")
                for idx, (question, options, correct_answer) in enumerate(mock_questions, 1):
                    st.write(f"**Q{idx}. {question}**")
                    for option in options:
                        st.write(f"- {option}")
                    st.write(f"*Answer:* {correct_answer}")
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

# 5. Essay Writing
with tab5:
    st.header("Essay Writing (UPSC Mains Preparation)")
    essay_text = st.text_area("Write your essay here...", height=200, max_chars=1500)
    if st.button("Submit Essay"):
        if len(essay_text.split()) < 1000:
            st.warning("Your essay is too short! Please aim for at least 1000 words.")
        elif len(essay_text.split()) > 1200:
            st.warning("Your essay is too long! Please limit it to 1200 words.")
        else:
            st.success("Essay submitted successfully!")
