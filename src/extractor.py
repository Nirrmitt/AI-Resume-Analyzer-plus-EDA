import os
import pdfplumber
from docx import Document
from pathlib import Path

class ResumeExtractor:
    @staticmethod
    def extract_text(file_path: str | Path) -> str:
        path = Path(file_path)
        ext = path.suffix.lower()
        
        if ext == ".pdf":
            return ResumeExtractor._extract_pdf(path)
        elif ext in (".docx", ".doc"):
            return ResumeExtractor._extract_docx(path)
        elif ext == ".txt":
            return path.read_text(encoding="utf-8").strip()
        else:
            raise ValueError(f"Unsupported file format: {ext}")

    @staticmethod
    def _extract_pdf(path: Path) -> str:
        text = []
        try:
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text.append(page_text)
        except Exception as e:
            raise RuntimeError(f"PDF extraction failed: {e}")
        return "\n".join(text).strip()

    @staticmethod
    def _extract_docx(path: Path) -> str:
        try:
            doc = Document(path)
            return "\n".join([p.text for p in doc.paragraphs if p.text.strip()]).strip()
        except Exception as e:
            raise RuntimeError(f"DOCX extraction failed: {e}")