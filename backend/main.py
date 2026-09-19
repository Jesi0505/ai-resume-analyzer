from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import fitz

from analyzer import calculate_match


app = FastAPI(title="AI Resume Analyzer API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API is running!"
    }


@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    # Read uploaded PDF
    pdf_data = await resume.read()

    # Open PDF
    pdf = fitz.open(
        stream=pdf_data,
        filetype="pdf"
    )

    # Extract resume text
    resume_text = ""

    for page in pdf:
        resume_text += page.get_text()

    pdf.close()

    # Analyze skills
    analysis = calculate_match(
        resume_text,
        job_description
    )

    return {
        "filename": resume.filename,

        "match_score": analysis["match_score"],

        "resume_skills": analysis["resume_skills"],

        "job_skills": analysis["job_skills"],

        "matched_skills": analysis["matched_skills"],

        "missing_skills": analysis["missing_skills"]
    }
