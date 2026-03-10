def calculate_score(repo_data):

    score = 20  # base score so beginners don't get 0

    stars = repo_data.get("stars", 0)
    forks = repo_data.get("forks", 0)

    score += min(stars * 2, 15)
    score += min(forks * 2, 10)

    languages = repo_data.get("languages", [])
    score += min(len(languages) * 8, 20)

    frameworks = repo_data.get("frameworks", [])
    score += min(len(frameworks) * 10, 20)

    files = repo_data.get("files", [])
    score += min(len(files) * 3, 15)

    if repo_data.get("description"):
        score += 10

    return min(score, 100)