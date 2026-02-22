📚 AI Course Learning Platform (RAG Based)
🔹 Short Overview

An AI-powered learning platform where users can create courses from PDFs or YouTube videos and generate:

📝 Quizzes

📒 Flashcards

💬 AI Chat (RAG-based)

All content is organized using course_id, ensuring data from one course does not interfere with another.

⚠️ Currently, there is no user authentication, so all courses are visible to everyone.

🏗️ Architecture Diagram (Flow)
Frontend (Next.js)
     |
     |  Select Course / Upload PDF / YouTube URL
     v
Backend (FastAPI)
     |
     |-- Extract Text (PDF / YouTube Transcript)
     |-- Chunk Text
     |-- Generate Embeddings
     |-- Store in Supabase (pgvector) with course_id
     |
     v
Supabase (Postgres + pgvector)
     |
     |-- Vector Search (course-based)
     |
     v
Gemini AI API
     |
     |-- Generate Quiz
     |-- Generate Flashcards
     |-- RAG Chat Answer
     |
     v
Frontend displays results
📘 Full Project README
📌 Project Title

AI Course Learning Platform using RAG (Retrieval Augmented Generation)

🎯 Purpose

This project allows users to:

Create learning courses from uploaded PDFs or YouTube videos

Store and organize content per course

Generate quizzes and flashcards from that content

Ask questions using an AI chatbot that answers only from the stored course data

🧠 Core Features
✅ Course Management

Create a course with a unique course_id

Upload PDF or YouTube URL per course

Content stored with course separation

✅ Quiz Generator

Generates MCQ quizzes per selected course

Returns structured JSON data

Frontend renders interactive quiz UI

✅ Flashcards Generator

Generates question-answer flashcards per course

Click to flip (question → answer)

✅ AI Chat (RAG)

Uses vector similarity search

Answers only from course data

If answer not found → returns "I don't know"

🏗️ System Architecture
Frontend (Next.js)

UI for:

Selecting courses

Generating quizzes & flashcards

Chat with AI

Built using:

React

Tailwind CSS

shadcn/ui

Sonner (toast notifications)

Backend (FastAPI)

Responsible for:

PDF text extraction

YouTube transcript extraction

Chunking & embedding generation

Vector search from Supabase
Prompting Gemini API for:
Quiz generation
Flashcard generation
Chat answers
Database (Supabase + pgvector)

Stores:
courses table
documents table (content + embedding + course_id)

Ensures:
No redundancy and no mixing of course data.

🗂️ Data Flow (Course-Based)
User creates a course
Uploads PDF or YouTube link
Backend extracts text
Text is chunked
Embeddings are generated
Stored in Supabase with course_id
User selects course
Quiz / Flashcards / Chat uses only that course data

📝 Quiz Format (JSON)
[
  {
    "question": "What is thermodynamics?",
    "options": ["A", "B", "C", "D"],
    "answer": "B"
  }
]
📒 Flashcard Format (JSON)
[
  {
    "question": "Define entropy",
    "answer": "Measure of disorder in a system"
  }
]
💬 RAG Chat Logic
User query → embedding generated
Similar chunks retrieved from database
Context passed to Gemini
Answer generated strictly from context

🧰 Tech Stack
Frontend
Next.js
React
Tailwind CSS
shadcn/ui
Sonner
Backend
FastAPI
Uvicorn
Python-dotenv
Google Gemini API (google-genai)
Sentence-Transformers
python-multipart
Database
Supabase (PostgreSQL)
pgvector

⚠️ Current Limitations
❌ No user authentication
❌ Courses are global (shared between all users)
❌ No course deletion or ownership control
❌ No rate limitin
❌ No file size validation
❌ API keys stored only in backend environment

🔮 Future Improvements
User authentication (JWT / Supabase Auth / Clerk)
User-specific courses
Private course visibility
Course delete & update
Streaming AI responses
Pagination for large datasets
Admin dashboard
Caching embeddings
Better error handling

🚀 Local Setup
Backend Setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Create .env file:

GEMINI_API_KEY=your_api_key
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
Frontend Setup
cd frontend
npm install
npm run dev

Open:

http://localhost:3000
🌍 Deployment
Frontend → Vercel
Backend → Render
Database → Supabase
Environment variables must be configured on deployment platforms.

📌 Summary

This project demonstrates:
Retrieval Augmented Generation (RAG)
Vector database integration
Course-based AI learning system
Full stack development using modern technologies