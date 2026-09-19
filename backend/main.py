from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import fitz


app = FastAPI(title="AI Resume Analyzer API")


# Allow the frontend to communicate with the backend
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

    # Open PDF from memory
    pdf = fitz.open(stream=pdf_data, filetype="pdf")

    # Extract text from all pages
    resume_text = ""

    for page in pdf:
        resume_text += page.get_text()

    pdf.close()

    return {
        "filename": resume.filename,
        "resume_text": resume_text,
        "job_description": job_description
    }
