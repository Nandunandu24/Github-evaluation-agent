def evaluate_project(repo_data, profile_data):

    languages = repo_data.get("languages", [])
    frameworks = repo_data.get("frameworks", [])
    files = repo_data.get("files", [])

    repo_count = profile_data.get("repos", 0)
    stars = profile_data.get("stars", 0)

    improvements = []

    if repo_count < 5:
        improvements.append("Create more GitHub repositories to strengthen your portfolio")

    if len(languages) < 2:
        improvements.append("Use multiple programming languages to demonstrate versatility")

    if len(frameworks) == 0:
        improvements.append("Consider using frameworks such as React, FastAPI, or Streamlit")

    if len(files) < 5:
        improvements.append("Increase project complexity by adding more modules")

    improvements.append("Add a detailed README explaining project setup and usage")
    improvements.append("Include unit tests to improve reliability")

    evaluation = f"""
### Code Quality
Moderate structure detected with {len(files)} project files.

### Project Complexity
Intermediate level project.

### Strengths
- Uses technologies: {', '.join(languages)}

### Improvements
"""

    evaluation += "\n".join([f"- {i}" for i in improvements])

    return evaluation
