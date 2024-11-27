import streamlit as st
import sqlite3

def saved_notes():
    st.header("Saved Notes")
    
    conn = sqlite3.connect("upsc_app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes")  # Assuming there's a table named 'notes'
    notes = cur.fetchall()

    if notes:
        for note in notes:
            st.write(f"**{note[0]}**")  # Display the note title
            st.write(note[1])  # Display the note content
            st.write("---")
    else:
        st.write("No saved notes yet.")

if __name__ == "__main__":
    saved_notes()
