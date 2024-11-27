import streamlit as st

def display_image(image_path):
    """
    Displays the image in the center of the app with a reduced size.
    """
    st.image(image_path, width=400, caption="Sarthana UPSC Preparation Hub")  # Reduce image size to 400px width

def main():
    # Display the image first
    image_path = r"C:\Users\saihr\Downloads\Sarthana  (2).png"  # Ensure the correct path to the image
    display_image(image_path)

    # App title and description
    st.title("UPSC Preparation Hub")
    
    st.write("""
        Welcome to the **UPSC Preparation Hub**! This platform is designed to assist you in preparing for the UPSC exams.
        You can stay updated with **Current Affairs**, summarize important topics, practice **Mock Tests**, save and manage **Notes**, and even work on **Essay Writing** to boost your performance in the UPSC Mains.
    """)

if __name__ == "__main__":
    main()
