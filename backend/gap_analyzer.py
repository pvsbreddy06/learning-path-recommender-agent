ROLE_SKILLS = {
    "data_scientist": ["python", "statistics", "ml", "sql"],
    "web_developer": ["html", "css", "javascript", "react"]
}

def analyze_gap(current_skills, target_role):
    required = ROLE_SKILLS.get(target_role, [])
    gaps = []

    for skill in required:
        if skill not in current_skills or current_skills[skill] < 3:
            gaps.append(skill)

    return gaps

