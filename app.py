import streamlit as st
from openai import OpenAI
from pdf_utils import extract_text
from quiz import generate_quiz
from flashcards import generate_flashcards
from database import create_table, save_quiz, get_quizzes

# -------------------- CONFIG --------------------
st.set_page_config(page_title="AI Study Assistant", layout="wide")

st.title("📚 AI Study Assistant")

# -------------------- OPENAI --------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# -------------------- DATABASE --------------------
create_table()

# -------------------- SIDEBAR --------------------
st.sidebar.title("📌 Options")
option = st.sidebar.radio("Choose Feature", ["Quiz", "Flashcards", "History"])

# -------------------- FILE UPLOAD --------------------
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

text = ""

if uploaded_file is not None:
    text = extract_text(uploaded_file)

    st.subheader("📄 Extracted Text Preview")
    st.write(text[:1000])  # show first 1000 chars


# -------------------- QUIZ --------------------
if option == "Quiz":
    if text:
        if st.button("🔥 Generate Quiz"):
            with st.spinner("Generating quiz..."):
                quiz = generate_quiz(text, client)

                st.subheader("🧠 Quiz Questions")
                st.write(quiz)

                # Save to database
                save_quiz(quiz)
    else:
        st.warning("Please upload a PDF first.")


# -------------------- FLASHCARDS --------------------
elif option == "Flashcards":
    if text:
        if st.button("📘 Generate Flashcards"):
            with st.spinner("Generating flashcards..."):
                flashcards = generate_flashcards(text, client)

                st.subheader("📚 Flashcards")
                st.write(flashcards)
    else:
        st.warning("Please upload a PDF first.")


# -------------------- HISTORY --------------------
elif option == "History":
    st.subheader("📜 Quiz History")

    quizzes = get_quizzes()

    if quizzes:
        for q in quizzes:
            st.write(q)
            st.markdown("---")
    else:
        st.info("No history found.")