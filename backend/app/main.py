from fastapi import FastAPI, UploadFile, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.services.pdf_services import extract_text_from_pdf
from app.services.yt_service import get_transcript
from app.services.embedding_services import chunk_text, embed_text
from app.db.vector_store import store_chunks, search_similar, get_all_chunks, create_course, get_all_courses, get_courses
from app.services.rag_service import rag_chat
from app.services.flashcard import generate_flashcards
from app.services.quiz import generate_quiz

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "https://python-fs-next.vercel.app/", "https://python-fs-next.vercel.app/*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"status": "ok"}


# -------- PDF --------
@app.post("/process-pdf")
async def process_pdf(file: UploadFile, course_id: str = Form(...)):
    text = extract_text_from_pdf(file.file)
    chunks = chunk_text(text)

    embeddings = []
    for c in chunks:
        embeddings.append(embed_text(c))

    store_chunks(chunks, embeddings, course_id)
    return {"message": "PDF processed", "course_id": course_id}


# -------- VIDEO --------
class VideoRequest(BaseModel):
    youtube_url: str
    course_id: str


@app.post("/process-video")
def process_video(req: VideoRequest):
    text = get_transcript(req.youtube_url)
    chunks = chunk_text(text)

    embeddings = []
    for c in chunks:
        embeddings.append(embed_text(c))

    store_chunks(chunks, embeddings, req.course_id)
    return {"message": "Video processed", "course_id": req.course_id}


# -------- CHAT --------
class ChatRequest(BaseModel):
    query: str


@app.post("/chat")
def chat(req: ChatRequest):
    answer = rag_chat(req.query)
    return {"answer": answer}


# -------- FLASHCARDS --------
class CourseRequest(BaseModel):
    course_id: str

@app.post("/generate-flashcards")
def flashcards(req: CourseRequest):
    docs = get_all_chunks(req.course_id)

    if not docs:
        return {"flashcards": []}

    context = " ".join([d["content"] for d in docs])

    cards = generate_flashcards(context)

    return {"flashcards": cards}

# -------- QUIZ --------
@app.post("/generate-quiz")
def quiz(req: CourseRequest):
    docs = get_all_chunks(req.course_id)
    context = " ".join([d["content"] for d in docs])
    # print("Main data: " + context)
    return {"quiz": generate_quiz(context)}

class CreateCourseRequest(BaseModel):
    name: str


@app.post("/courses")
def create_new_course(req: CreateCourseRequest):
    create_course(req.name)
    return {"message": "Course created"}


@app.get("/courses")
def list_courses():
    courses = get_all_courses()
    print("Courses: " + str(courses))
    return {"courses": courses}