import streamlit as st
import json
from src.analyzer import ResumeAnalyzer
from src.utils import setup_logging

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
logger = setup_logging()

st.title("🤖 AI Resume Analyzer")
st.markdown("Upload a resume and paste a job description to get an AI-powered match score & actionable feedback.")

col1, col2 = st.columns(2)
with col1:
    resume_file = st.file_uploader("Upload Resume (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
with col2:
    job_desc = st.text_area("Paste Job Description", height=250)

if st.button("Analyze", disabled=not (resume_file and job_desc)):
    with st.spinner("Analyzing resume..."):
        # Save temp file
        import tempfile
        from pathlib import Path
        tmp_path = Path(tempfile.gettempdir()) / resume_file.name
        tmp_path.write_bytes(resume_file.read())
        
        analyzer = ResumeAnalyzer()
        result = analyzer.analyze(str(tmp_path), job_desc)
        
        if "error" in result:
            st.error(result["error"])
        else:
            st.success(f"✅ Match Level: {result['match_level']}")
            st.metric("Overall Score", f"{result['overall_score']}%")
            
            st.subheader("📊 Score Breakdown")
            st.bar_chart({
                "Semantic": result["breakdown"]["semantic_similarity"],
                "Skills": result["breakdown"]["skill_match"],
                "Experience": result["breakdown"]["experience_relevance"]
            })
            
            st.subheader("💡 AI Feedback")
            for fb in result["feedback"]:
                st.warning(fb)
                
            st.subheader("🔍 Extracted Skills")
            st.write(", ".join(result["extracted_skills"]))
            
            if result["missing_skills"]:
                st.subheader("⚠️ Missing Key Skills")
                st.error(", ".join(result["missing_skills"]))
                
            with st.expander("📦 Raw JSON Output"):
                st.json(result)