from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def generate_questions(role: str, level: str):
    prompt = f"""
Generate exactly 5 interview questions for a {role} at {level} level.

Return ONLY this JSON format:
[
  "Question 1",
  "Question 2",
  "Question 3",
  "Question 4",
  "Question 5"
]

Rules:
- No explanations
- No markdown
- No extra text
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        text = response.choices[0].message.content.strip()

        # ✅ Clean parsing
        questions = json.loads(text)

        return questions

    except Exception as e:
        print("AI error:", e)
        return ["Error generating questions"]