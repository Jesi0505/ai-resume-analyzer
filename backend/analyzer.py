# Skills that our analyzer can recognize

SKILLS = [
    "python",
    "java",
    "javascript",
    "typescript",
    "sql",
    "html",
    "css",
    "react",
    "node.js",
    "express",
    "mongodb",
    "mysql",
    "spring boot",
    "spring data jpa",
    "spring rest",
    "rest api",
    "git",
    "github",
    "docker",
    "aws",
    "power bi",
    "pandas",
    "numpy",
    "scikit-learn",
    "machine learning",
    "figma",
    "tailwind css",
    "fastapi",
    "flask"
]


def find_skills(text):
    """
    Find recognized skills in a given text.
    """

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills


def calculate_match(resume_text, job_description):
    """
    Compare resume skills with job description skills.
    """

    resume_skills = find_skills(resume_text)
    job_skills = find_skills(job_description)

    matched_skills = [
        skill for skill in job_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    if len(job_skills) > 0:
        match_score = round(
            (len(matched_skills) / len(job_skills)) * 100
        )
    else:
        match_score = 0

    return {
        "match_score": match_score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }
