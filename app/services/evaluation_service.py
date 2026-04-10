from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def evaluate_answer(question: str, answer: str):
    prompt = f"""
You are a professional technical interviewer.

Evaluate the candidate’s answer.

Question:
{question}

Answer:
{answer}

Return STRICT format:

Score: X/10
Feedback: (2-3 lines)
Improvement: (1 suggestion)
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("Evaluation error:", e)
        return "Evaluation failed"