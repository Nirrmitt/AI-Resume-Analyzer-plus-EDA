import sys
import os

print("Python version:", sys.version)
print("Current folder:", os.getcwd())
print("Files in src:", os.listdir("src") if os.path.exists("src") else "src/ not found")
print("Files in data:", os.listdir("data") if os.path.exists("data") else "data/ not found")

try:
    import spacy
    print("✅ spaCy loaded")
except Exception as e:
    print(f"❌ spaCy error: {e}")

try:
    from sentence_transformers import SentenceTransformer
    print("✅ sentence-transformers loaded")
except Exception as e:
    print(f"❌ sentence-transformers error: {e}")

try:
    from src.analyzer import ResumeAnalyzer
    print("✅ src.analyzer imported successfully")
except Exception as e:
    print(f"❌ Import error: {e}")
    import traceback
    traceback.print_exc()