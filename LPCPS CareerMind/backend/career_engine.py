# Career ke liye required skills
career_required_skills = {
    "Data Analyst": [
        "python",
        "sql",
        "data analysis",
        "excel",
        "data visualization"
    ],
    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "statistics"
    ],
    "Software Developer": [
        "java",
        "data structures",
        "algorithms"
    ],
    "Frontend Developer": [
        "html",
        "css",
        "javascript"
    ]
}

def recommend_career(skills):
    if "python" in skills and "sql" in skills and "data analysis" in skills:
        return "Data Analyst"
    elif "python" in skills and "machine learning" in skills:
        return "Machine Learning Engineer"
    elif "java" in skills:
        return "Software Developer"
    elif "html" in skills and "css" in skills and "javascript" in skills:
        return "Frontend Developer"
    else:
        return "General IT Role"


def find_skill_gap(career, skills):
    """
    Career ke required skills aur
    student ke skills ka difference nikalta hai
    """

    required_skills = career_required_skills.get(career, [])
    missing_skills = []

    for skill in required_skills:
        if skill not in skills:
            missing_skills.append(skill)

    return missing_skills


# Skill ke hisaab se learning resources
learning_resources = {
    "excel": {
        "course": "Excel for Data Analysis (Coursera / YouTube)",
        "project": "Sales Data Analysis using Excel"
    },
    "data visualization": {
        "course": "Data Visualization with Python (Matplotlib)",
        "project": "Build a Sales Dashboard"
    },
    "statistics": {
        "course": "Statistics for Data Science",
        "project": "Analyze Survey Data"
    },
    "algorithms": {
        "course": "DSA Algorithms Basics",
        "project": "Implement Sorting Algorithms"
    }
}

def generate_learning_roadmap(missing_skills):
    """
    Missing skills ke base pe
    learning roadmap generate karega
    """
    roadmap = []

    for skill in missing_skills:
        if skill in learning_resources:
            roadmap.append({
                "skill": skill,
                "course": learning_resources[skill]["course"],
                "project": learning_resources[skill]["project"]
            })

    return roadmap

# Internship opportunities (industry-aligned)
internships = {
    "Data Analyst": [
        {
            "company": "Google",
            "role": "Data Analyst Intern",
            "skills": ["python", "sql", "data analysis"]
        },
        {
            "company": "Amazon",
            "role": "Business Data Analyst Intern",
            "skills": ["excel", "sql"]
        },
        {
            "company": "Deloitte",
            "role": "Data Analytics Intern",
            "skills": ["data analysis", "statistics"]
        }
    ],
    "Software Developer": [
        {
            "company": "Microsoft",
            "role": "Software Engineer Intern",
            "skills": ["java", "data structures"]
        },
        {
            "company": "TCS",
            "role": "Software Developer Intern",
            "skills": ["java", "python"]
        }
    ],
    "Machine Learning Engineer": [
        {
            "company": "IBM",
            "role": "Machine Learning Intern",
            "skills": ["python", "machine learning"]
        }
    ]
}

def match_internships(career, skills):
    matched = []

    for internship in internships.get(career, []):
        for skill in skills:
            if skill in internship["skills"]:
                matched.append(internship)
                break

    return matched

def calculate_readiness_score(career, skills):
    """
    Industry benchmark ke hisaab se
    Career Readiness Score calculate karta hai
    """
    required_skills = career_required_skills.get(career, [])

    if not required_skills:
        return 50  # safe fallback for General IT Role

    matched_skills = [s for s in skills if s in required_skills]

    score = int((len(matched_skills) / len(required_skills)) * 100)
    return score
