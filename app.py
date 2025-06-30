# app.py
import streamlit as st

st.set_page_config(page_title="Personal Tutor", layout="wide")
from rag_pipeline import load_and_split_text, embed_chunks, retrieve_similar_chunks
from agents.quiz_agent import generate_quiz
from agents.translator import translate
from google.generativeai import configure, GenerativeModel
from config import gemini_api_key
from utils.memory_check import print_memory_usage, get_memory_usage
import os
import tempfile

# Gemini configuration
configure(api_key=gemini_api_key)

# Page config and sidebar
mem = get_memory_usage()
st.sidebar.markdown(f"💾 RAM usage: **{mem:.2f} MB**")

# Hide Streamlit's default upload size note
st.markdown("""
    <style>
    .uploadedFileDetails {display: none;}
    </style>
""", unsafe_allow_html=True)

st.title("📚 Personalized Learning Tutor (AI)")

# Session history
if "history" not in st.session_state:
    st.session_state.history = []

# Language selector BEFORE file upload
language_names = {
    "en": "English 🇺🇸",
    "fr": "French 🇫🇷",
    "es": "Spanish 🇪🇸",
    "hi": "Hindi 🇮🇳",
    "de": "German 🇩🇪"
}

target_lang = st.selectbox(
    "🌐 Select language for answers and quiz:",
    options=list(language_names.keys()),
    format_func=lambda code: language_names[code],
    index=0
)

# File upload (supports both .txt and .pdf)
st.markdown("⚠️ Please upload files smaller than **500KB**.")
uploaded_file = st.file_uploader("Upload notes", type=["txt", "pdf"])


if uploaded_file and uploaded_file.size > 2000000:
    st.warning("Please upload a smaller file (<2MB).")
    st.stop()

if uploaded_file:
    suffix = ".pdf" if uploaded_file.name.endswith(".pdf") else ".txt"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        filepath = tmp.name

    chunks = load_and_split_text(filepath)
    chunk_vectors = embed_chunks(chunks)

    st.success("✅ Document processed successfully!")
    #print("Loaded API Key:", gemini_api_key[:5] + "..." if gemini_api_key else "❌ None")

    # Functional mode selector
    option = st.radio("Choose a function:", ["Ask a Question", "Generate a Quiz"], horizontal=True)

    if option == "Ask a Question":
        query = st.text_input("Ask a question from the notes:")
        if query:
            top_chunks = retrieve_similar_chunks(query, chunks, chunk_vectors)
            context = "\n".join(top_chunks)

            # Send to Gemini
            model = GenerativeModel("models/gemini-1.5-flash")
            response = model.generate_content(f"""Use the following notes to answer:\n{context}\n\nQuestion: {query}""")

            answer = response.text
            if target_lang != "en":
                answer = translate(answer, target=target_lang)

            st.session_state.history.append(("You", query))
            st.session_state.history.append(("Tutor", answer))

        # Display chat history
        print_memory_usage("After response generation")
        for role, msg in st.session_state.history:
            st.chat_message(role).markdown(msg)

    elif option == "Generate a Quiz":
        print_memory_usage("Before quiz generation")
        if st.button("📝 Generate Quiz"):
            quiz = generate_quiz("\n".join(chunks[:5]))
            if target_lang != "en":
                translated_quiz = translate(quiz, target=target_lang)
                if "❌" not in translated_quiz:
                    quiz = translated_quiz
                else:
                    st.warning("Translation failed. Showing original quiz in English.")
            st.subheader("Quiz:")
            st.markdown(quiz)
