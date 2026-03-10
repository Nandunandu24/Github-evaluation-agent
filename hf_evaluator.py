import streamlit as st
from transformers import pipeline


@st.cache_resource
def load_model():

    # using a stable text-generation model
    return pipeline(
        "text-generation",
        model="microsoft/DialoGPT-medium",
        max_new_tokens=200
    )


generator = load_model()


def evaluate_project(repo_data, profile_data):

    languages = repo_data.get("languages", [])
    frameworks = repo_data.get("frameworks", [])
    files = repo_data.get("files", [])

    repo_count = profile_data.get("repos", 0)
    stars = profile_data.get("stars", 0)

    prompt = f"""
You are a senior software engineering recruiter.

Evaluate this GitHub portfolio and give suggestions.

Repository:
Languages: {languages}
Frameworks: {frameworks}
Files: {len(files)}

Profile:
Repositories: {repo_count}
Stars: {stars}

Provide the evaluation in this structure:

Code Quality:
Project Complexity:
Strengths:
- point
- point

Improvements:
- suggestion
- suggestion
- suggestion
"""

    try:

        result = generator(
            prompt,
            do_sample=True,
            temperature=0.7
        )

        output = result[0]["generated_text"]

        # remove prompt echo
        if prompt in output:
            output = output.replace(prompt, "")

        if len(output.strip()) < 30:
            raise Exception("weak generation")

        return output

    except:

        # fallback improvements based on repo signals
        improvements = []

        if repo_count < 5:
            improvements.append("Create more GitHub repositories to strengthen your portfolio")

        if len(languages) < 2:
            improvements.append("Use multiple programming languages to show versatility")

        if len(frameworks) == 0:
            improvements.append("Consider using frameworks like React, FastAPI, or Streamlit")

        if len(files) < 5:
            improvements.append("Increase project complexity by adding more modules")

        improvements.append("Add a detailed README explaining project setup and usage")
        improvements.append("Deploy the project online using Vercel, Streamlit Cloud, or Docker")

        return f"""
**Code Quality:** Moderate structure detected.

**Project Complexity:** Beginner to Intermediate.

**Strengths:**
- Uses technologies: {', '.join(languages)}

**Improvements:**

""" + "\n".join([f"- {i}" for i in improvements])