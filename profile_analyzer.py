import requests


def analyze_profile(username):

    profile_api = f"https://api.github.com/users/{username}/repos"

    repos = requests.get(profile_api).json()

    total_repos = len(repos)

    total_stars = sum(repo["stargazers_count"] for repo in repos)

    return {
        "repos": total_repos,
        "stars": total_stars
    }