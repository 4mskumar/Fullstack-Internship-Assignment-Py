from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))


def store_chunks(chunks, embeddings, course_id):
    for chunk, emb in zip(chunks, embeddings):
        supabase.table("documents").insert({
            "content": chunk,
            "embedding": emb,
            "course_id": course_id
        }).execute()


def get_all_chunks(course_id: str):
    res = supabase.table("documents") \
        .select("content") \
        .eq("course_id", course_id) \
        .execute()
    return res.data


def search_similar(query_embedding):
    result = supabase.rpc("match_documents", {
        "query_embedding": query_embedding,
        "match_count": 5
    }).execute()
    return result.data


# -------- COURSES --------

def create_course(name: str):
    return supabase.table("courses").insert({
        "name": name
    }).execute()


def get_courses():
    data = supabase.table("documents").select("course_id").execute()

    course_ids = list(set([row["course_id"] for row in data.data if row["course_id"]]))

    courses = [{"id": cid, "name": cid} for cid in course_ids]
    return {"courses": courses}
def get_all_courses():
    result = supabase.table("documents").select("course_id").execute()

    # unique course ids
    unique = list(set([row["course_id"] for row in result.data if row["course_id"]]))

    courses = []
    for cid in unique:
        courses.append({
            "id": cid,
            "name": cid
        })

    return courses