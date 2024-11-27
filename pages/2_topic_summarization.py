import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline
from googletrans import Translator
import tempfile
from gtts import gTTS

def text_to_speech(text, lang_code="en"):
    """Convert text to speech and play it"""
    tts = gTTS(text=text, lang=lang_code)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        tts.save(temp_audio.name)
        st.audio(temp_audio.name, format="audio/mp3")

def topic_summarization():
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

if __name__ == "__main__":
    topic_summarization()
