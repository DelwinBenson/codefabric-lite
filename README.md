# CodeFabric Lite

**Project Evolution & Decision Intelligence Platform**

---

## Overview

Modern engineering teams lose context as projects grow.

Important architectural decisions, trade-offs, and discussions get buried across:
- GitHub commits  
- Pull requests  
- Issues  
- Ongoing repository activity  

When new developers join a project, understanding *why* certain decisions were made becomes difficult.

**CodeFabric Lite is an early-stage attempt to reduce context loss in project engineering.**

It explores how raw repository activity can be transformed into structured project understanding.

---

## What This Version Does

CodeFabric Lite connects to a GitHub repository and provides:

- Project metadata  
- Recent commits  
- Pull requests  
- Issues  
- Decision summaries  
- Interactive decision timeline visualization  

The timeline view helps surface how a project evolved over time, making decision history easier to interpret.

---

## Tech Stack

- **Backend:** FastAPI  
- **Frontend:** HTML, CSS, JavaScript  
- **Data Source:** GitHub REST API  

---

## How to Run

1. Install dependencies:
pip install fastapi uvicorn requests

2. Start the backend server:
uvicorn backend:app --reload

3. Open `index.html` in your browser.

---

## Vision

The broader goal is to build an intelligence layer on top of engineering workflows that:

- Reduces onboarding friction  
- Preserves project decision history  
- Minimizes context loss  
- Converts development activity into actionable insights  

This project represents the foundational step toward a more comprehensive engineering intelligence platform.

---

## Author

Delwin Benson
Mrinank
