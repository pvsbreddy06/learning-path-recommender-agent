def assess_skills(learner_data):
    """
    Input: learner profile
    Output: skill score mapping
    """
    skills = learner_data.get("skills", {})
    assessed = {}

    for skill, level in skills.items():
        assessed[skill] = level  # already rated by learner

    return assessed

