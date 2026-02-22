import json

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_quiz(context: str):
    prompt = f"""
Generate 5-10 MCQs ONLY from the context in JSON:

Return ONLY valid JSON like this:

[
  {{
    "question": "string",
    "options": ["A","B","C","D"],
    "answer": "correct option"
  }}
]

No explanation. No markdown. No text outside JSON.

Context:
{context}
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )
    # print("Quiz service data: " + response.text)

    return json.loads(response.text)