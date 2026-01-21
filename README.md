# JD → Resume Fix Copilot 🚀

A lightweight ATS optimization tool that analyzes a resume against a job description and provides instant, actionable feedback to improve job application success.

---

## 🔍 Problem
Most job seekers blindly apply to roles without knowing:
- How well their resume matches the job description
- Which important keywords are missing
- Why their resume gets rejected by ATS systems

---

## 💡 Solution
JD → Resume Fix Copilot helps users:
- Calculate an **ATS match score**
- Identify **missing keywords** from the job description
- See **matched skills** already present in the resume
- Get quick suggestions to improve resume relevance

All in real time, with a simple web interface.

---

## ⚙️ How It Works
1. User pastes a **Job Description**
2. User pastes their **Resume**
3. The system:
   - Converts text into vectors using **TF-IDF**
   - Computes similarity using **cosine similarity**
   - Extracts missing and matched keywords
4. Displays results instantly

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** – Web UI
- **scikit-learn** – TF-IDF & similarity
- **NLP (basic preprocessing)**

---

## 📊 Features
- ATS Match Score (%)
- Missing Keywords Detection
- Matched Keywords Highlight
- Fast, lightweight MVP
- Easy to extend with advanced NLP or LLMs

