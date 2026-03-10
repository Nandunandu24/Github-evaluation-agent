import streamlit as st
import pandas as pd

from database import save_candidate, load_candidates
from github_analyzer import get_repo_data
from scoring_engine import calculate_score
from hf_evaluator import evaluate_project
from profile_analyzer import analyze_profile


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="GitHub Portfolio Evaluation Agent",
    layout="wide"
)

st.title("🚀 GitHub Portfolio Evaluation Agent")


# ---------------- SIDEBAR ----------------

role = st.sidebar.selectbox(
    "Select Dashboard",
    ["User Dashboard", "HR Dashboard"]
)


# ---------------- USER DASHBOARD ----------------

if role == "User Dashboard":

    st.header("User Dashboard")

    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    repo = st.text_input("GitHub Repository URL")

    if st.button("Analyze Portfolio"):

        if repo == "":
            st.warning("Please enter a GitHub repository URL")
            st.stop()

        with st.spinner("Analyzing repository..."):

            repo_data = get_repo_data(repo)

        if not repo_data:
            st.error("Invalid GitHub repository.")
            st.stop()

        # ---------------- REPOSITORY INSIGHTS ----------------

        st.subheader("📂 Repository Insights")

        languages = repo_data.get("languages", [])
        frameworks = repo_data.get("frameworks", [])
        files = repo_data.get("files", [])

        st.markdown("**Languages Used:**")
        for lang in languages:
            st.markdown(f"- {lang}")

        st.markdown("**Frameworks Detected:**")
        if frameworks:
            for fw in frameworks:
                st.markdown(f"- {fw}")
        else:
            st.markdown("- None detected")

        st.markdown("**Project Files:**")
        for f in files[:10]:
            st.markdown(f"- {f}")

        # ---------------- PROFILE INSIGHTS ----------------

        try:

            username = repo.replace("https://github.com/", "").split("/")[0]

            profile_data = analyze_profile(username)

            st.subheader("👨‍💻 Developer Profile Insights")

            st.markdown(f"- Total Repositories: **{profile_data['repos']}**")
            st.markdown(f"- Total Stars Earned: **{profile_data['stars']}**")

        except:

            st.warning("Could not fetch GitHub profile insights")

        # ---------------- SCORING ----------------

        score = calculate_score(repo_data)

        st.subheader("📊 Portfolio Score")
        st.metric("Score", score)

        # ---------------- SCORING BREAKDOWN ----------------

        st.subheader("Score Explanation")

        st.markdown(f"- Stars: **{repo_data.get('stars')}**")
        st.markdown(f"- Forks: **{repo_data.get('forks')}**")
        st.markdown(f"- Languages Used: **{len(languages)}**")
        st.markdown(f"- Frameworks Detected: **{len(frameworks)}**")
        st.markdown(f"- Project Files: **{len(files)}**")

        # ---------------- AI EVALUATION ----------------

        with st.spinner("Generating AI evaluation..."):

            evaluation = evaluate_project(repo_data,profile_data)

        st.subheader("🤖 AI Evaluation & Improvements")

        if evaluation:
            st.markdown(evaluation)
        else:
            st.warning("Evaluation unavailable.")

        # ---------------- ELIGIBILITY ----------------

        eligibility = "Eligible" if score >= 60 else "Needs Improvement"

        candidate = {
            "name": name,
            "email": email,
            "phone": phone,
            "repo": repo,
            "score": score,
            "eligibility": eligibility
        }

        save_candidate(candidate)


# ---------------- HR DASHBOARD ----------------

if role == "HR Dashboard":

    st.header("HR Consultant Dashboard")

    data = load_candidates()

    if data:

        df = pd.DataFrame(data)

        df = df[
            [
                "name",
                "repo",
                "email",
                "phone",
                "score",
                "eligibility"
            ]
        ]

        st.dataframe(df, use_container_width=True)

    else:

        st.info("No candidates submitted yet.")