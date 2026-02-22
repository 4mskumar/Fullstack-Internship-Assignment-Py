from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def chunk_text(text: str, size: int = 500):
    words = text.split()
    return [" ".join(words[i:i + size]) for i in range(0, len(words), size)]


def embed_text(text: str) -> list[float]:
    response = client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=text
    )

    # Gemini returns a list of embeddings
    embedding_obj = response.embeddings[0]

    embedding = embedding_obj.values

    # Debug safety check
    if len(embedding) != 3072:
        raise ValueError(f"Embedding dimension mismatch: {len(embedding)}")

    return embedding


# Test locally
if __name__ == "__main__":
    emb = embed_text("test")
    print("Embedding length:", len(emb))  # must print 3072