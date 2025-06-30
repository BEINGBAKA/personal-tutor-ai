# agents/quiz_agent.py
from google.generativeai import GenerativeModel

model = GenerativeModel("models/gemini-1.5-flash")  # Assumes api key set in env

def generate_quiz(context: str, num_questions: int = 10) -> str:
    prompt = f"""
You are an academic quiz generator.

Based on the following course content, generate {num_questions} multiple-choice questions. 
Each question should have 4 options and indicate the correct one clearly.

Content:
\"\"\"
{context}
\"\"\"
"""
    response = model.generate_content(prompt)
    return response.text

