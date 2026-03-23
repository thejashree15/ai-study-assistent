import streamlit as st
from pdf_utils import extract_text
from quiz import generate_quiz
from flashcards import generate_flashcards
from database import create_table, save_quiz, get_quizzes

# -------- INITIALIZE DATABASE --------
create_table()

# -------- PAGE CONFIG --------
st.set_page_config(page_title="AI Study Assistant", layout="wide")

# -------- TITLE --------
st.title("📚 AI Study Assistant")

# -------- SIDEBAR --------
st.sidebar.title("📌 Options")
option = st.sidebar.radio("Choose Feature", ["Quiz", "Flashcards", "History"])

# -------- FILE UPLOAD --------
uploaded_file = st.file_uploader("📄 Upload your PDF", type="pdf")

# -------- QUIZ & FLASHCARDS --------
if uploaded_file:
    text = extract_text(uploaded_file)

    st.subheader("📃 Extracted Text Preview")
    st.write(text[:500])

    # -------- QUIZ --------
    if option == "Quiz":
        if st.button("🎯 Generate Quiz"):
            quiz = generate_quiz(text)

            # Save to database
            save_quiz(quiz)

            st.subheader("🧠 Quiz Questions")
            for i, q in enumerate(quiz, 1):
                st.write(f"{i}. {q}")

    # -------- FLASHCARDS --------
    elif option == "Flashcards":
        if st.button("🧠 Generate Flashcards"):
            flashcards = generate_flashcards(text)

            st.subheader("📚 Flashcards")
            for card in flashcards:
                st.markdown(f"""
                **📌 Front:** {card['front']}  
                **💡 Back:** {card['back']}
                """)
                st.markdown("---")

# -------- HISTORY (FIXED ✅ ALWAYS WORKS) --------
if option == "History":
    st.subheader("📜 Quiz History")

    data = get_quizzes()

    if not data:
        st.write("No history found.")
    else:
        for row in data:
            st.write(f"{row[0]}. {row[1]} ({row[2]})")