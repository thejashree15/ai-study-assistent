import streamlit as st
from openai import OpenAI
from pdf_utils import extract_text
from quiz import generate_quiz
from flashcards import generate_flashcards
from database import create_table, save_quiz, get_quizzes

# ------------------- SAFE API KEY -------------------
if "OPENAI_API_KEY" not in st.secrets:
    st.error("❌ API key missing. Please add it in Streamlit secrets.")
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ------------------- PAGE CONFIG -------------------
st.set_page_config(page_title="AI Study Assistant", layout="wide")

# ------------------- DATABASE INIT -------------------
create_table()

# ------------------- TITLE -------------------
st.title("📚 AI Study Assistant")

# ------------------- SIDEBAR -------------------
st.sidebar.title("Options")
option = st.sidebar.radio(
    "Choose Feature",
    ["Quiz", "Flashcards", "History"]
)

# ------------------- FILE UPLOAD -------------------
uploaded_file = st.file_uploader("📄 Upload PDF (optional)", type=["pdf"])

text = ""

if uploaded_file:
    text = extract_text(uploaded_file)
else:
    text = st.text_area("✍️ Or paste your study content here")

# ------------------- QUIZ SECTION -------------------
if option == "Quiz":
    st.header("📝 Generate Quiz")

    if st.button("Generate Quiz"):
        if text.strip() == "":
            st.warning("⚠️ Please enter some text")
        else:
            with st.spinner("Generating quiz..."):
                quiz = generate_quiz(client, text)

            st.success("✅ Quiz Generated!")

            for i, q in enumerate(quiz):
                st.write(f"**Q{i+1}: {q['question']}**")
                st.write("A.", q["options"][0])
                st.write("B.", q["options"][1])
                st.write("C.", q["options"][2])
                st.write("D.", q["options"][3])
                st.write(f"✅ Answer: {q['answer']}")
                st.markdown("---")

            save_quiz(str(quiz))

# ------------------- FLASHCARDS SECTION -------------------
elif option == "Flashcards":
    st.header("📌 Generate Flashcards")

    if st.button("Generate Flashcards"):
        if text.strip() == "":
            st.warning("⚠️ Please enter some text")
        else:
            with st.spinner("Generating flashcards..."):
                cards = generate_flashcards(client, text)

            st.success("✅ Flashcards Ready!")

            for card in cards:
                st.write(f"**Q:** {card['question']}")
                st.write(f"**A:** {card['answer']}")
                st.markdown("---")

# ------------------- HISTORY SECTION -------------------
elif option == "History":
    st.header("📜 Previous Quizzes")

    quizzes = get_quizzes()

    if quizzes:
        for q in quizzes:
            st.write(q)
            st.markdown("---")
    else:
        st.info("No quizzes saved yet.")