import numpy as np
import re
from sentence_transformers import SentenceTransformer, util
from typing import Dict, Any
from .extractor import ResumeExtractor
from .parser import ResumeParser
from .utils import load_config, setup_logging
import json
import os
from datetime import datetime

logger = setup_logging()
CONFIG = load_config()

class ResumeAnalyzer:
    def __init__(self, model_name: str = CONFIG["model"]["embedding"]):
        logger.info(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)
        self.parser = ResumeParser()

    def analyze(self, resume_path: str, job_description: str) -> Dict[str, Any]:
        logger.info("Extracting & parsing resume...")
        resume_text = ResumeExtractor.extract_text(resume_path)
        parsed = self.parser.parse(resume_text)

        if parsed["word_count"] < 50:
            return {"error": "Resume too short or extraction failed."}

        # 1. Semantic similarity (overall)
        resume_emb = self.model.encode(parsed["full_text"], convert_to_tensor=True)
        jd_emb = self.model.encode(job_description, convert_to_tensor=True)
        semantic_sim = float(util.cos_sim(resume_emb, jd_emb)[0][0])

        # 2. Skill match score
        jd_lower = job_description.lower()
        jd_skills = [s for s in ResumeParser.COMMON_SKILLS if re.search(rf'\b{re.escape(s)}\b', jd_lower)]
        matched_skills = [s for s in parsed["skills"] if s in jd_skills]
        missing_skills = [s for s in jd_skills if s not in parsed["skills"]]
        
        skill_score = len(matched_skills) / max(len(jd_skills), 1) if jd_skills else 0.5

        # 3. Experience relevance
        exp_score = 0.5
        if parsed["experience"]:
            exp_text = " ".join([e["title"] + " " + " ".join(e["description"]) for e in parsed["experience"][:3]])
            exp_emb = self.model.encode(exp_text, convert_to_tensor=True)
            exp_score = float(util.cos_sim(exp_emb, jd_emb)[0][0])

        # 4. Weighted final score
        w = CONFIG["weights"]
        final_score = (w["semantic"] * semantic_sim + w["skills"] * skill_score + w["experience"] * exp_score) * 100

        # 5. Feedback generation
        feedback = []
        if final_score < CONFIG["thresholds"]["good_match"]:
            feedback.append("Resume lacks strong alignment with the target role.")
        if missing_skills:
            feedback.append(f"Consider adding these key skills: {', '.join(missing_skills[:4])}")
        if exp_score < 0.4:
            feedback.append("Highlight measurable achievements and role-specific responsibilities.")
        if parsed["word_count"] < 300:
            feedback.append("Resume is too brief. Add quantifiable metrics and project details.")

        # Determine match level
        match_level = "Strong"
        if final_score < CONFIG["thresholds"]["good_match"]: match_level = "Good"
        if final_score < CONFIG["thresholds"]["weak_match"]: match_level = "Weak"
        # Log results for Data Analysis
        log_entry = {
            "overall_score": round(final_score, 1),
            "match_level": match_level,
            "missing_skills": missing_skills,
            "timestamp": datetime.now().isoformat(),
            "word_count": parsed["word_count"]
        }
        os.makedirs("data", exist_ok=True)
        with open("data/results.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")
        return {
            "overall_score": round(final_score, 1),del notebooks\eda_resume_analysis.ipynb
            "match_level": match_level,
            "breakdown": {
                "semantic_similarity": round(semantic_sim * 100, 1),
                "skill_match": round(skill_score * 100, 1),
                "experience_relevance": round(exp_score * 100, 1)
            },
            "extracted_skills": parsed["skills"],
            "missing_skills": missing_skills,
            "feedback": feedback[:CONFIG["limits"]["max_feedback_items"]],
            "metadata": {
                "word_count": parsed["word_count"],
                "experience_entries": len(parsed["experience"]),
                "education_entries": len(parsed["education"])
            }
        }