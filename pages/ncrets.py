import os
from PyPDF2 import PdfReader

# Path to NCERT textbooks
ncert_path = r"D:\Sarthana\training data\ncerts"

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        if not text.strip():  # Check if the extracted text is empty
            print(f"No extractable text found in {pdf_path}")
            return None
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

# Function to load specific subtopics
def load_subtopic_textbooks(folder_path, subtopic):
    subtopic_path = os.path.join(folder_path, subtopic)
    subtopic_text = {}
    
    if not os.path.exists(subtopic_path):
        print(f"Subtopic folder {subtopic} does not exist.")
        return subtopic_text

    print(f"Looking for PDFs in {subtopic_path}")
    for filename in os.listdir(subtopic_path):
        if filename.endswith('.pdf'):
            filepath = os.path.join(subtopic_path, filename)
            print(f"Loading: {filename}")
            content = extract_text_from_pdf(filepath)
            if content:
                subtopic_text[filename] = content
    return subtopic_text

# Load History and Indian Society NCERTs
history_data = load_subtopic_textbooks(ncert_path, "History")
indian_society_data = load_subtopic_textbooks(ncert_path, "Indian Society")

# Display a snippet of the content
if history_data:
    print("\nHistory Data Loaded:")
    for textbook, content in history_data.items():
        print(f"History Textbook: {textbook}, Content Snippet: {content[:500]}...\n")
else:
    print("No History data found.")

if indian_society_data:
    print("\nIndian Society Data Loaded:")
    for textbook, content in indian_society_data.items():
        print(f"Indian Society Textbook: {textbook}, Content Snippet: {content[:500]}...\n")
else:
    print("No Indian Society data found.")
