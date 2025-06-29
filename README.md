# Personal-tutor
An agentic AI-powered Personalized Learning Tutor that answers questions and generates quizzes from your study notes using Gemini, embeddings, and multilingual translation. Built with Streamlit and optimized for Render deployment.

# 📚 Personalized Learning Tutor (AI)

An agentic AI-powered Streamlit application that helps students learn better from their notes by:
- Answering questions using context-aware retrieval (RAG)
- Generating short quizzes
- Translating output into multiple languages

✅ Lightweight design to run smoothly on Render's Free Tier (≤ 512MB RAM).

---

# Features

- RAG-based Q&A: Retrieves context from uploaded notes using embeddings + Gemini Pro
- Auto-quiz generation: Create quick quizzes from notes to test understanding
- Multilingual output: Supports English, French, Spanish, Hindi, and German
- Flexible input: Accepts `.txt` and `.pdf` notes (≤150KB)
- Memory efficient: Optimized for low-RAM cloud deployment

---

## 🛠️ Tech Stack

| Layer           | Tech                         |
|----------------|------------------------------|
| Frontend       | Streamlit                    |
| Backend Logic  | Python, LangChain-like RAG   |
| Embeddings     | SentenceTransformers (MiniLM)|
| LLM            | Gemini 1.5 Flash (Google)    |
| Translation    | Deep Translator              |
| File Parsing   | PyMuPDF (`fitz`)             |
| Memory Check   | `psutil`                     |

---

# Demo

![Demo Screenshot](https://your-demo-image-link-if-any)

Try it live: [https://your-render-app-url](https://your-render-app-url)

---

# Local Setup

# 1. Clone the repo

```bash
git clone https://github.com/your-username/personalized-learning-tutor.git
cd personalized-learning-tutor
