from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

def get_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not set")

    return OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )


def generate_questions(role: str, level: str):
    client = get_client()  # ✅ moved here

    prompt = f""" Generate exactly 5 interview questions for a {role} at {level} level. Return ONLY this JSON format: [ "Question 1", "Question 2", "Question 3", "Question 4", "Question 5" ] Rules: - No explanations - No markdown - No extra text """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        text = response.choices[0].message.content.strip()

        questions = json.loads(text)
        return questions

    except Exception as e:
        print("AI error:", e)
        return ["Error generating questions"]