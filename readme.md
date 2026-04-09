# AI Resume Analyzer

<p align="center">
  <b>AI-powered Resume Screening using NLP, Semantic Matching, and Intelligent Scoring</b>
</p>

<p align="center">
  <a href="https://github.com/Nirrmitt/AI-Resume-Analyzer-plus-EDA/stargazers">
    <img src="https://img.shields.io/github/stars/Nirrmitt/AI-Resume-Analyzer-plus-EDA?style=for-the-badge" />
  </a>
  <a href="https://github.com/Nirrmitt/AI-Resume-Analyzer-plus-EDA/network/members">
    <img src="https://img.shields.io/github/forks/Nirrmitt/AI-Resume-Analyzer-plus-EDA?style=for-the-badge" />
  </a>
  <a href="https://github.com/Nirrmitt/AI-Resume-Analyzer-plus-EDA/issues">
    <img src="https://img.shields.io/github/issues/Nirrmitt/AI-Resume-Analyzer-plus-EDA?style=for-the-badge" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/NLP-spaCy-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Model-SentenceTransformers-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/UI-Streamlit-red?style=for-the-badge" />
</p>

---

## Live Demo

Run the application locally with:

```bash
git clone https://github.com/Nirrmitt/AI-Resume-Analyzer-plus-EDA.git
cd AI-Resume-Analyzer-plus-EDA
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```

Then upload a resume or use `data/sample_resume.txt`, and paste a job description in the web UI.

---


## Overview

AI Resume Analyzer is a production-grade system designed to evaluate resume–job alignment using advanced Natural Language Processing techniques.

The system combines:
- Semantic similarity using SentenceTransformers  
- Named Entity Recognition (NER) using spaCy  
- Hybrid rule-based and machine learning extraction  
- Configurable weighted scoring  

It generates accurate match scores, identifies missing skills, and provides actionable insights for both candidates and recruiters.

---

## Features

- Supports PDF, DOCX, and TXT formats  
- Semantic similarity matching using transformer models  
- NLP-based extraction of skills, experience, and education  
- Weighted scoring system (semantic, skills, experience)  
- Skill gap detection with actionable feedback  
- Command-line interface (CLI) and Streamlit web application  
- Fully configurable using `config.yaml`  

---

## Tech Stack

- Python  
- spaCy  
- SentenceTransformers  
- Streamlit  
- scikit-learn  

---

## Installation

```bash
git clone https://github.com/Nirrmitt/AI-Resume-Analyzer-plus-EDA.git
cd AI-Resume-Analyzer-plus-EDA
pip install -r requirements.txt
python -m spacy download en_core_web_sm

Usage
Run via CLI

python main.py --resume sample_resume.pdf --job "Senior Python Developer role requiring AWS, Docker, FastAPI, and CI/CD experience..."

Run Web Application
streamlit run app.py

Architecture
Resume Input → Text Extraction → NLP Parsing (spaCy + Rules)
                                ↓
Job Description → Embedding Model → Semantic + Skill + Experience Scoring
                                ↓
                    Final Score + Feedback + Skill Gap Analysis

                    Accuracy and Optimization

The system is engineered for high precision and recall through:

Domain-specific embedding fine-tuning
Custom-trained NER models for skill extraction
Context-aware parsing using section detection
Threshold and weight optimization
Evaluation using precision, recall, F1-score, and ranking metrics

Evaluation Example

from sklearn.metrics import precision_score, recall_score, f1_score

precision = precision_score(y_true, y_pred_binary)
recall = recall_score(y_true, y_pred_binary)
f1 = f1_score(y_true, y_pred_binary)

Project Structure
ai-resume-analyzer/
├── requirements.txt
├── config.yaml
├── src/
│   ├── extractor.py
│   ├── parser.py
│   ├── analyzer.py
│   └── utils.py
├── main.py
├── app.py
└── README.md

Customization
Modify scoring weights and thresholds in config.yaml
Extend skill dictionaries or integrate external datasets
Replace embedding models (e.g., BAAI/bge-large-en-v1.5)

Use Cases
Resume screening automation
Candidate-job matching systems
Recruitment analytics and HR intelligence
Personal resume optimization tools

Contributing

Contributions are welcome. Potential areas include:

Layout-aware parsing improvements
Model fine-tuning pipelines
Benchmark datasets and evaluation frameworks
REST API integration (FastAPI)
UI/UX enhancements

License

MIT License

Keywords

AI Resume Analyzer, Resume Matching, NLP, Semantic Similarity, Skill Extraction, Recruitment AI, Resume Screening, Machine Learning, HR Tech

Support

If you found this project useful, consider giving it a star!
