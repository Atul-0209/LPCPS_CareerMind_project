from tests_engine import TEST_QUESTIONS, evaluate_test

student_profiles = []

from flask import Flask, request, render_template
import os


# ==========================
# TEST RESULTS STORAGE (DEMO)
# ==========================
test_results = []

# ===== AI MODULES =====
from resume_parser import extract_skills
from career_engine import (
    recommend_career,
    find_skill_gap,
    generate_learning_roadmap,
    match_internships,
    calculate_readiness_score   # 🔥 NEW
)

# ===== FLASK APP =====
# templates folder backend ke bahar hai
# ===== UNIVERSITY ANALYTICS STORAGE (IN-MEMORY) =====
analytics_store = []

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# 🔥 TEMP STORAGE FOR UNIVERSITY ANALYTICS
student_profiles = []


# ==========================
# HOME ROUTE (UPLOAD PAGE)
# ==========================
@app.route("/")
def home():
    return render_template("upload.html", title="LPCPS CareerMind")


# ==========================
# ANALYZE RESUME ROUTE
# ==========================
@app.route("/analyze", methods=["POST"])
def analyze():

    # 1️⃣ Resume text (textarea)
    resume_text = request.form.get("resume", "")

    # 2️⃣ Resume file (PDF / DOCX / TXT)
    uploaded_file = request.files.get("resume_file")

    if uploaded_file and uploaded_file.filename != "":
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
        uploaded_file.save(file_path)
        resume_text = file_path  # path pass kar rahe (PDF/DOCX handled)

    # 3️⃣ Skill extraction
    skills = extract_skills(resume_text)

    # 4️⃣ Career recommendation
    career = recommend_career(skills)

    # 5️⃣ Skill gap
    missing_skills = find_skill_gap(career, skills)

    # 6️⃣ Learning roadmap
    roadmap = generate_learning_roadmap(missing_skills)

    # 7️⃣ Internship matching
    internships = match_internships(career, skills)

    # 🔥 8️⃣ Career Readiness Score
    readiness_score = calculate_readiness_score(career, skills)

    # 🔥 9️⃣ Save profile for University Analytics
    student_profiles.append({
        "career": career,
        "skills": skills,
        "readiness": readiness_score
    })

    # 10️⃣ Render dashboard
    return render_template(
        "dashboard.html",
        skills=skills,
        career=career,
        missing_skills=missing_skills,
        roadmap=roadmap,
        internships=internships,
        readiness_score=readiness_score
    )
@app.route("/test")
def test_page():
    return render_template(
        "test.html",
        questions=TEST_QUESTIONS,
        title="Skill Test"
    )
@app.route("/submit_test", methods=["POST"])
def submit_test():
    # 1️⃣ Student ka naam lena
    student_name = request.form.get("name")

    # 2️⃣ Saare answers lena
    answers = request.form.to_dict()
    answers.pop("name")  # name ko answers se hata diya

    # 3️⃣ Score calculate karna
    score = evaluate_test(answers)

    # 4️⃣ Result store karna
    test_results.append({
        "name": student_name,
        "score": score
    })

    # 5️⃣ Ranking generate karna
    ranked_students = sorted(
        test_results,
        key=lambda x: x["score"],
        reverse=True
    )

    # 6️⃣ Ranking page dikhana
    return render_template(
        "ranking.html",
        rankings=ranked_students,
        title="Student Ranking"
    )


# ==========================
# UNIVERSITY ANALYTICS DASHBOARD
# ==========================
@app.route("/analytics")
def university_analytics():

    total_students = len(student_profiles)
    career_count = {}
    avg_readiness = 0

    for profile in student_profiles:
        career = profile["career"]
        career_count[career] = career_count.get(career, 0) + 1
        avg_readiness += profile["readiness"]

    if total_students > 0:
        avg_readiness = avg_readiness // total_students

    return render_template(
        "analytics.html",
        total_students=total_students,
        career_count=career_count,
        avg_readiness=avg_readiness
    )


# ==========================
# RUN SERVER
# ==========================
if __name__ == "__main__":
    app.run(debug=True)
