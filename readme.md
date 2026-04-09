# 🤖 AI Resume Analyzer

A production-grade, open-source resume analyzer that uses **semantic embeddings**, **NER-based skill extraction**, and **weighted scoring** to evaluate resume-job alignment. Built for accuracy, extensibility, and real-world HR/recruiting workflows.

## ✨ Features
- 📄 Supports PDF, DOCX, TXT
- 🧠 Semantic similarity via `sentence-transformers`
- 🔍 Rule + NLP hybrid skill/experience/education extraction
- 📊 Weighted scoring (semantic, skills, experience)
- 💡 Actionable feedback & missing skill detection
- 🌐 Streamlit UI + CLI interface
- ⚙️ Fully configurable via `config.yaml`

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 2. Run CLI
```bash
python main.py --resume sample_resume.pdf --job "Senior Python Developer role requiring AWS, Docker, FastAPI, and CI/CD experience..."
```

### 3. Run Web UI
```bash
streamlit run app.py
```

## 📐 Architecture
```
[Upload/Text] → [Text Extractor] → [Resume Parser (spaCy + Regex)]
                                      ↓
[Job Description] → [Embedding Model] → [Semantic + Skill + Exp Scoring]
                                      ↓
                          [Weighted Final Score + Feedback]
```

## 🎯 How to Achieve "10x Accuracy"

"10x accuracy" isn't a standard ML metric, but you can dramatically improve precision/recall with these engineering practices:

| Strategy | Implementation |
|----------|----------------|
| **Domain-Specific Embeddings** | Fine-tune `all-MiniLM-L6-v2` on HR/resume data using `sentence-transformers` + contrastive learning |
| **Custom NER for Skills** | Train spaCy NER on annotated resume data (Prodigy, Label Studio) |
| **OCR for Scanned PDFs** | Integrate `pytesseract` + `pdf2image` fallback |
| **Evaluation Pipeline** | Use `precision`, `recall`, `F1`, `HR@K` on labeled dataset |
| **Threshold Calibration** | Optimize weights/thresholds via grid search on validation set |
| **Context-Aware Parsing** | Add section detection (Experience, Education, Skills) via layout models (`layoutparser`, `docling`) |

### 📊 Evaluation Example
```python
from sklearn.metrics import precision_score, recall_score, f1_score
# y_true = binary match labels, y_pred = model scores > threshold
precision = precision_score(y_true, y_pred_binary)
recall = recall_score(y_true, y_pred_binary)
f1 = f1_score(y_true, y_pred_binary)
```

## 📂 Project Structure
```
ai-resume-analyzer/
├── requirements.txt
├── config.yaml
├── src/
│   ├── extractor.py   # File parsing
│   ├── parser.py      # NLP extraction
│   ├── analyzer.py    # Scoring engine
│   └── utils.py       # Config/logging
├── main.py            # CLI
├── app.py             # Streamlit UI
└── README.md
```

## 🔧 Customization
- Edit `config.yaml` to adjust weights/thresholds
- Extend `COMMON_SKILLS` in `parser.py` or load from JSON/DB
- Swap embedding model in `config.yaml` (e.g., `BAAI/bge-large-en-v1.5`)

## 📜 License
MIT License. Free for personal & commercial use.

## 🤝 Contributing
PRs welcome! Focus on:
- Better layout parsing
- Domain-specific fine-tuning scripts
- Evaluation benchmarks
- API endpoint (`FastAPI`)

---
**Built with ❤️ using Python, spaCy, SentenceTransformers & Streamlit**