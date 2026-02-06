def match_peers(learner_skill, learner_pool):
    matches = []
    for learner in learner_pool:
        if learner["skill"] == learner_skill:
            matches.append(learner["name"])
    return matches

