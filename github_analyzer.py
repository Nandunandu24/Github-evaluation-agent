import requests


def get_repo_data(repo_url):

    # Normalize URL
    repo_url = repo_url.strip()

    if "github.com" not in repo_url:
        return None

    # Extract owner and repo safely
    parts = repo_url.replace("https://", "").replace("http://", "").split("/")

    # parts example:
    # ['github.com', 'username', 'repository']

    if len(parts) < 3:
        return None

    owner = parts[1]
    repo = parts[2]

    repo = repo.replace(".git", "")

    repo_api = f"https://api.github.com/repos/{owner}/{repo}"
    contents_api = f"https://api.github.com/repos/{owner}/{repo}/contents"
    languages_api = f"https://api.github.com/repos/{owner}/{repo}/languages"

    repo_response = requests.get(repo_api)

    if repo_response.status_code != 200:
        return None

    repo_info = repo_response.json()

    languages = requests.get(languages_api).json()

    contents_response = requests.get(contents_api)

    files = []
    frameworks = []
    code_snippets = []

    if contents_response.status_code == 200:

        contents = contents_response.json()

        for item in contents:

            if item["type"] == "file":

                filename = item["name"]
                files.append(filename)

                if filename.endswith((".py", ".js", ".ts")):

                    code = requests.get(item["download_url"]).text[:300]

                    code_snippets.append(code)

                    code_lower = code.lower()

                    if "streamlit" in code_lower:
                        frameworks.append("Streamlit")

                    if "flask" in code_lower:
                        frameworks.append("Flask")

                    if "fastapi" in code_lower:
                        frameworks.append("FastAPI")

                    if "torch" in code_lower:
                        frameworks.append("PyTorch")

                    if "tensorflow" in code_lower:
                        frameworks.append("TensorFlow")

    repo_data = {
        "description": repo_info.get("description"),
        "stars": repo_info.get("stargazers_count"),
        "forks": repo_info.get("forks_count"),
        "issues": repo_info.get("open_issues_count"),
        "languages": list(languages.keys()),
        "files": files,
        "frameworks": list(set(frameworks)),
        "code_snippets": code_snippets[:2]
    }

    return repo_data