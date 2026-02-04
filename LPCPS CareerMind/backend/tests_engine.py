# ==========================
# TEST QUESTION BANK
# ==========================

TEST_QUESTIONS = [
    {
        "id": 1,
        "question": "What does SQL stand for?",
        "options": [
            "Structured Query Language",
            "Simple Query Language",
            "System Query Logic",
            "Sequential Query List"
        ],
        "answer": "Structured Query Language"
    },
    {
        "id": 2,
        "question": "Which Python library is best for data analysis?",
        "options": [
            "NumPy",
            "Pandas",
            "TensorFlow",
            "Flask"
        ],
        "answer": "Pandas"
    },
    {
        "id": 3,
        "question": "Which skill is essential for Machine Learning?",
        "options": [
            "HTML",
            "Statistics",
            "Photoshop",
            "MS Word"
        ],
        "answer": "Statistics"
    }
]
# ==========================
# TEST EVALUATION LOGIC
# ==========================

def evaluate_test(user_answers):
    """
    user_answers = {
        "1": "Pandas",
        "2": "Statistics"
    }
    """
    score = 0

    for question in TEST_QUESTIONS:
        qid = str(question["id"])
        correct_answer = question["answer"]

        if user_answers.get(qid) == correct_answer:
            score += 1

    return score
