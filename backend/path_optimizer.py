COURSE_MAP = {
    "python": "Python for Beginners – Coursera",
    "statistics": "Statistics Basics – Udemy",
    "ml": "Machine Learning – Andrew Ng",
    "sql": "SQL Fundamentals – Coursera"
}

def generate_learning_path(skill_gaps, time_per_week):
    path = []
    weeks = 1

    for skill in skill_gaps:
        path.append({
            "week": weeks,
            "skill": skill,
            "course": COURSE_MAP.get(skill),
            "estimated_hours": min(6, time_per_week)
        })
        weeks += 1

    return {
        "total_weeks": weeks - 1,
        "learning_path": path
    }

