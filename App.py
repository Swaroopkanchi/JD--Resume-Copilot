import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="JD → Resume Fix Copilot")

st.title("JD → Resume Fix Copilot")
st.write("Analyze resume against a job description and improve ATS match")

jd = st.text_area("Paste Job Description")
resume = st.text_area("Paste Resume")

if st.button("Analyze"):
    if jd and resume:
        vectorizer = TfidfVectorizer(stop_words='english')
        vectors = vectorizer.fit_transform([jd, resume])

        score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        match_score = round(score * 100, 2)

        jd_words = set(jd.lower().split())
        resume_words = set(resume.lower().split())
        missing_keywords = jd_words - resume_words

        st.subheader("ATS Match Score")
        st.progress(match_score / 100)
        st.write(f"{match_score}% match")

        st.subheader("Missing Keywords")
        st.write(", ".join(list(missing_keywords)[:20]))

        st.subheader("Suggestions")
        st.write("Add missing keywords naturally into resume bullet points.")
    else:
        st.warning("Please paste both JD and Resume")
