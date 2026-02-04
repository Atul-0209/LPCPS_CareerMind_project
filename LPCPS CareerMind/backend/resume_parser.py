import re
import pdfplumber
from docx import Document

# Known skills list (simple NLP)
SKILLS_DB = [
    "python", "java", "sql", "html", "css", "javascript",
    "data analysis", "machine learning", "statistics",
    "excel", "flask"
]

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + " "
    return text.lower()

def extract_skills(resume_text_or_path):
    """
    Input:
    - resume text (string)
    - OR file path (pdf/docx)
    """

    text = ""

    # Case 1: PDF
    if isinstance(resume_text_or_path, str) and resume_text_or_path.endswith(".pdf"):
        text = extract_text_from_pdf(resume_text_or_path)

    # Case 2: DOCX
    elif isinstance(resume_text_or_path, str) and resume_text_or_path.endswith(".docx"):
        text = extract_text_from_docx(resume_text_or_path)

    # Case 3: Plain text
    else:
        text = resume_text_or_path.lower()

    found_skills = []
    for skill in SKILLS_DB:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.append(skill)

    return list(set(found_skills))
