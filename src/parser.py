import spacy
import re
from typing import Dict, List, Any
from .utils import load_config, setup_logging

logger = setup_logging()

# Pre-load spacy model (run: python -m spacy download en_core_web_sm)
nlp = spacy.load(load_config()["model"]["spacy"])

class ResumeParser:
    COMMON_SKILLS = {
        "python", "javascript", "java", "c++", "sql", "aws", "azure", "gcp",
        "docker", "kubernetes", "terraform", "git", "ci/cd", "agile", "scrum",
        "react", "vue", "angular", "node.js", "express", "flask", "django", "fastapi",
        "machine learning", "deep learning", "nlp", "computer vision", "data science",
        "pandas", "numpy", "tensorflow", "pytorch", "scikit-learn", "excel", "power bi",
        "tableau", "project management", "communication", "leadership", "problem solving"
    }

    @staticmethod
    def parse(resume_text: str) -> Dict[str, Any]:
        doc = nlp(resume_text)
        text_lower = resume_text.lower()

        # 1. Skills extraction (NER + keyword matching)
        skills = set()
        for ent in doc.ents:
            if ent.label_ in ("PRODUCT", "ORG", "WORK_OF_ART", "EVENT", "LANGUAGE"):
                cleaned = ent.text.lower().strip()
                if len(cleaned) > 2:
                    skills.add(cleaned)
        
        for skill in ResumeParser.COMMON_SKILLS:
            if re.search(rf'\b{re.escape(skill)}\b', text_lower):
                skills.add(skill)

        # 2. Experience extraction (date + role pattern)
        experience = []
        date_pat = re.compile(r'\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s*-?\s*\d{2,4}\b', re.I)
        lines = [l.strip() for l in resume_text.split('\n') if l.strip()]
        
        for i, line in enumerate(lines):
            if date_pat.search(line) and len(line.split()) <= 10:
                entry = {"title": line, "description": []}
                for j in range(i+1, min(i+5, len(lines))):
                    if date_pat.search(lines[j]) or len(lines[j]) > 120:
                        break
                    entry["description"].append(lines[j])
                experience.append(entry)

        # 3. Education extraction
        edu_keywords = ["university", "college", "institute", "bachelor", "master", "phd", "bsc", "msc", "ba", "bs", "ma", "ms"]
        education = [l for l in lines if any(k in l.lower() for k in edu_keywords)]

        return {
            "skills": sorted(list(skills)),
            "experience": experience,
            "education": education,
            "full_text": resume_text,
            "word_count": len(resume_text.split())
        }