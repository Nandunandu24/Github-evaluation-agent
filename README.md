# 🚀 GitHub Portfolio Evaluation Agent

A Streamlit-based tool that analyzes a candidate's GitHub repository, scores the portfolio, and generates AI-style feedback to help both candidates and recruiters quickly gauge project quality and developer activity.

The app has two views: a **User Dashboard** where candidates submit a repo for evaluation, and an **HR Dashboard** where recruiters can review all submitted candidates and their scores in one place.

---

Deployed link : https://github-evaluation-agent.onrender.com/

## ✨ Features

- **Repository Analysis** — Pulls live data from the GitHub API: languages used, stars, forks, open issues, and project files.
- **Framework Detection** — Scans source files (`.py`, `.js`, `.ts`) for signs of popular frameworks (Streamlit, Flask, FastAPI, PyTorch, TensorFlow).
- **Developer Profile Insights** — Looks up the repo owner's GitHub profile to surface total repository count and total stars earned across all repos.
- **Portfolio Scoring Engine** — Calculates a 0–100 score based on stars, forks, language diversity, framework usage, file count, and presence of a project description.
- **AI-Style Evaluation** — Generates a structured feedback report covering code quality, project complexity, strengths, and concrete improvement suggestions.
- **Candidate Eligibility Tagging** — Automatically marks each submission as `Eligible` (score ≥ 60) or `Needs Improvement`.
- **HR Dashboard** — A simple recruiter view listing all evaluated candidates with their score and eligibility status, backed by a lightweight local JSON store.

---

## 🛠️ Tech Stack

- **Frontend / App Framework:** Streamlit
- **Data Handling:** Pandas
- **GitHub Integration:** GitHub REST API via `requests`
- **Storage:** JSON file-based persistence (no external database required)

---

## 📁 Project Structure

```
├── app.py                # Streamlit app: User Dashboard + HR Dashboard
├── github_analyzer.py    # Fetches repo metadata, languages, files, and detects frameworks
├── profile_analyzer.py   # Fetches GitHub profile-level stats (repo count, total stars)
├── scoring_engine.py     # Calculates the 0–100 portfolio score
├── hf_evaluator.py        # Generates the AI-style evaluation and improvement suggestions
├── database.py            # Reads/writes candidate records to a local JSON file
├── candidates.json         # Stores submitted candidate records
├── results.json            # Reserved for evaluation output/results
└── requirements.txt         # Python dependencies
```

---

## ⚙️ How It Works

1. A candidate enters their name, email, phone number, and a public GitHub repository URL on the **User Dashboard**.
2. `github_analyzer.py` calls the GitHub API to pull repo metadata (languages, stars, forks, files) and scans source files for framework usage.
3. `profile_analyzer.py` fetches the owner's overall GitHub stats (total repos and stars).
4. `scoring_engine.py` combines these signals into a single portfolio score out of 100.
5. `hf_evaluator.py` generates a readable evaluation summary with strengths and improvement suggestions based on the same signals.
6. The candidate's score and eligibility (`Eligible` if score ≥ 60, otherwise `Needs Improvement`) are saved via `database.py`.
7. Recruiters can switch to the **HR Dashboard** to view all submitted candidates, their scores, and eligibility status in a single table.

---

## 📊 Scoring Breakdown

| Factor | Contribution |
|---|---|
| Base score | 20 points (so beginner portfolios aren't scored zero) |
| Stars | up to 15 points (2 points per star) |
| Forks | up to 10 points (2 points per fork) |
| Language diversity | up to 20 points (8 points per language) |
| Frameworks detected | up to 20 points (10 points per framework) |
| Project files | up to 15 points (3 points per file) |
| Has a repo description | +10 points |

Final score is capped at 100.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+

### Installation
```bash
git clone https://github.com/Nandunandu24/Github-evaluation-agent.git
cd Github-evaluation-agent
pip install -r requirements.txt
```

### Run the App
```bash
streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`.

---

## 🧭 Usage

**As a Candidate (User Dashboard):**
1. Select **User Dashboard** from the sidebar.
2. Enter your name, email, phone number, and GitHub repository URL.
3. Click **Analyze Portfolio** to view repository insights, your portfolio score, and AI-generated feedback.

**As a Recruiter (HR Dashboard):**
1. Select **HR Dashboard** from the sidebar.
2. View all submitted candidates with their score and eligibility status in a sortable table.

---

## 🔭 Future Improvements

- Replace keyword-based framework detection with deeper static analysis
- Add authentication for the HR Dashboard
- Move candidate storage from a local JSON file to a proper database
- Expand AI evaluation with a real LLM-backed code review instead of rule-based suggestions
- Add unit tests across scoring and analysis modules

---

## 📄 License

This project is currently unlicensed. All rights reserved by the author.
