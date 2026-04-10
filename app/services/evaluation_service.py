from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# ❌ REMOVE this top-level client initialization:
# client = OpenAI(...)  <-- This crashes at import if key is missing

def get_client():
    """Initialize client lazily, only when needed."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set")
    return OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

def evaluate_answer(question: str, answer: str):
    client = get_client()  # ✅ Created here, not at import time
    
    prompt = f"""..."""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Evaluation error:", e)
        return "Evaluation failed"