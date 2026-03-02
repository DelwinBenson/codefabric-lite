from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GITHUB_API = "https://api.github.com/repos"


def github_get(url):
    response = requests.get(url, headers=headers)

    if response.status_code == 403:
        return {"error": "Rate limit exceeded. Try again later."}

    if response.status_code != 200:
        return {"error": response.json()}

    return response.json()


def parse_repo_url(url):
    parts = url.rstrip("/").split("/")
    return parts[-2], parts[-1]


@app.get("/analyze")
def analyze_repo(repo_url: str):
    owner, repo = parse_repo_url(repo_url)

    repo_data = github_get(f"{GITHUB_API}/{owner}/{repo}")
    commits = github_get(f"{GITHUB_API}/{owner}/{repo}/commits")[:5]
    prs = github_get(f"{GITHUB_API}/{owner}/{repo}/pulls")[:5]
    issues = github_get(f"{GITHUB_API}/{owner}/{repo}/issues")[:5]

    commit_list = [
        {
            "message": c["commit"]["message"],
            "author": c["commit"]["author"]["name"]
        }
        for c in commits
    ]

    pr_list = [
        {
            "title": p["title"],
            "author": p["user"]["login"]
        }
        for p in prs
    ]

    issue_list = [
        {
            "title": i["title"],
            "author": i["user"]["login"]
        }
        for i in issues
    ]

    decisions = [
        p["title"]
        for p in pr_list
        if any(word in p["title"].lower()
               for word in ["fix", "add", "update", "remove", "change", "implement", "improve"])
    ]

    timeline = []

    for p in pr_list:
        timeline.append({
            "date": "N/A",
            "event": f"PR: {p['title']}",
            "author": p["author"]
        })

    for c in commit_list:
        timeline.append({
            "date": "N/A",
            "event": f"Commit: {c['message']}",
            "author": c["author"]
        })

    return {
        "project": repo_data.get("full_name"),
        "description": repo_data.get("description"),
        "commits": commit_list,
        "pull_requests": pr_list,
        "issues": issue_list,
        "decision_summary": decisions,
        "decision_timeline": timeline,
    }