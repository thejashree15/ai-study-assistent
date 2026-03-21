import streamlit as st
from pdf_utils import extract_text
from quiz import generate_quiz
from flashcards import generate_flashcards

# Page config
st.set_page_config(page_title="AI Study Assistant", page_icon="📚", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📚 AI Study Assistant</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
st.sidebar.title("📌 Options")
feature = st.sidebar.radio("Choose Feature", ["Quiz", "Flashcards"])

# Upload section
st.subheader("📄 Upload your PDF")
uploaded_file = st.file_uploader("Choose a file", type="pdf")

if uploaded_file:
    text = extract_text(uploaded_file)

    st.subheader("📃 Extracted Text Preview")
    st.write(text[:300])

    st.markdown("---")

    # QUIZ SECTION
    if feature == "Quiz":
        if st.button("🎯 Generate Quiz"):
            quiz = generate_quiz(text)

            st.subheader("🧠 Quiz Questions")
            for i, q in enumerate(quiz, 1):
                st.write(f"{i}. {q}")

    # FLASHCARDS SECTION
    elif feature == "Flashcards":
        if st.button("🧾 Generate Flashcards"):
            cards = generate_flashcards(text)

            st.subheader("📚 Flashcards")

            for card in cards:
                with st.container():
                    st.markdown(f"""
                    <div style="background-color:#1e1e1e; padding:15px; border-radius:10px; margin-bottom:10px;">
                        <b>📌 Front:</b> {card['front']}<br>
                        <b>💡 Back:</b> {card['back']}
                    </div>
                    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)