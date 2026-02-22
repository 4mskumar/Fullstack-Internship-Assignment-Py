import json

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


import json
import re

def generate_flashcards(context: str):
    prompt = f"""
Return ONLY valid JSON. No explanation. No markdown.

Format:
[
  {{"question": "string", "answer": "string"}}
]

Generate 10-15 flashcards from this context:

{context}
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    raw = response.text.strip()
    print("RAW FLASHCARDS:", raw)

    # Remove markdown if Gemini adds ```json
    raw = raw.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(raw)
        return data
    except Exception as e:
        print("JSON PARSE FAILED:", e)
        print("RAW WAS:", raw)
        return []
