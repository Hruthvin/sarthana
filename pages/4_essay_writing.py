import random
import streamlit as st

def score_essay(essay):
    """Simple scoring function based on word count and basic structure."""
    word_count = len(essay.split())
    if word_count < 50:
        return "Score: 2/10 (Too short, needs more content)"
    elif 50 <= word_count < 150:
        return "Score: 5/10 (Average, try to elaborate more)"
    elif 150 <= word_count < 300:
        return "Score: 8/10 (Good effort, well-detailed)"
    else:
        return "Score: 10/10 (Excellent, comprehensive essay)"

def essay_writing():
    st.title("Essay Writing Practice")

    # Define subjects and corresponding essay topics with difficulty levels
    subjects = {
        "Literacy": {
            "easy": [
                "Why is literacy important for personal development?",
                "How can schools contribute to improving literacy rates in India?",
                "What are the benefits of literacy for children?"
            ],
            "medium": [
                "Challenges faced in promoting literacy in India.",
                "The impact of digital literacy on employment opportunities.",
                "How can India reduce the gender gap in literacy?"
            ],
            "advanced": [
                "How does literacy in a digital age influence social and political participation?",
                "What are the long-term economic consequences of low literacy rates in India?",
                "Can literacy alone contribute to the development of a knowledge-based economy?"
            ]
        },
        "Environment": {
            "easy": [
                "Why is it important to protect endangered species?",
                "What are the environmental impacts of deforestation?",
                "How can urbanization be made sustainable?"
            ],
            "medium": [
                "What challenges do cities face in becoming environmentally sustainable?",
                "How does urban sprawl contribute to environmental degradation?",
                "What role does technology play in creating sustainable cities?"
            ],
            "advanced": [
                "Smart cities and their role in sustainable development.",
                "How can India balance economic growth with environmental conservation?",
                "What are the implications of rapid urbanization on India’s natural resources?"
            ]
        }
    }

    # Subject selection
    selected_subject = st.selectbox("Select a subject:", list(subjects.keys()))

    # Difficulty level selection
    difficulty_level = st.selectbox("Select a difficulty level:", ["easy", "medium", "advanced"])

    # Generate random essay topic
    topics = subjects[selected_subject][difficulty_level]
    random_topic = random.choice(topics)

    st.write(f"**Random Topic:** {random_topic}")

    # Text area for essay writing
    essay = st.text_area("Write your essay below:")

    # Submit button to evaluate
    if st.button("Submit and Evaluate"):
        if essay.strip():
            score = score_essay(essay)
            st.write(f"### Your Essay Score: {score}")
        else:
            st.write("Please write your essay before submitting.")

# Run the app
if __name__ == "__main__":
    essay_writing()
