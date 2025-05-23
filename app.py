import streamlit as st
import re
from resume_parser import extract_resume_text
from job_parser import extract_job_description
from llm_client import get_llm_analysis
from pdf_generator import generate_pdf

# 📊 Extract match score
def extract_score(text):
    match = re.search(r"Match Score:\s*(\d+)", text)
    if match:
        return int(match.group(1))
    return None

# 🔍 Extract missing skills
def extract_missing_skills(text):
    start = text.lower().find("missing but required skills:")
    if start == -1:
        return []

    lines = text[start:].split("\n")[1:10]
    skills = []
    for line in lines:
        clean = line.strip("-•:* \n").strip()
        if not clean or clean.lower().startswith("suggestions"):
            break
        skills.append(clean.split(":")[0])
    return skills

# 📚 Extract LLM-recommended learning resources
def extract_learning_resources(text):
    start = text.lower().find("learning resources")
    if start == -1:
        return []

    lines = text[start:].split("\n")[1:10]
    resources = []
    for line in lines:
        clean = line.strip("-•:* \n").strip()
        if not clean or clean.lower().startswith("match score"):
            break
        resources.append(clean)
    return resources

# 🏁 Streamlit App
st.title("🔍 Resume vs Job Matcher with LLM")

uploaded_resume = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the job description here")

if uploaded_resume and job_description:
    with st.spinner("Analyzing resume and job description..."):
        resume_text = extract_resume_text(uploaded_resume)
        job_text = extract_job_description(job_description)
        result = get_llm_analysis(resume_text, job_text)

    # 🐞 Print raw result to console for debug
    print("LLM RAW RESULT:\n", result)

    # ⚠️ Warn if result looks incomplete
    if "match score" not in result.lower():
        st.warning("⚠️ The LLM response may be incomplete. Try submitting again or simplifying the input.")

    # ✅ Display full result
    st.subheader("✅ Match Analysis")
    st.text_area("📋 Full LLM Response", value=result, height=400)

    # 📊 Show match score and progress bar
    score = extract_score(result)
    if score is not None:
        st.subheader(f"📊 Match Score: {score}%")
        st.progress(score / 100.0)

    # 📚 Show learning resources
    learning_links = extract_learning_resources(result)
    if learning_links:
        st.subheader("📚 Suggested Learning Resources")
        for item in learning_links:
            st.markdown(f"- {item}")

    # 📄 Download result as PDF
    pdf_bytes = generate_pdf(result)
    st.download_button(
        label="📄 Download Match Report as PDF",
        data=pdf_bytes,
        file_name="match_report.pdf",
        mime="application/pdf"
    )
