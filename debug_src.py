import sys
import os

print("=== Checking src folder ===")
print("Current directory:", os.getcwd())
print("src exists:", os.path.exists("src"))
print("src contents:", os.listdir("src") if os.path.exists("src") else "NOT FOUND")

print("\n=== Checking __init__.py ===")
init_path = "src/__init__.py"
print("__init__.py exists:", os.path.exists(init_path))
if os.path.exists(init_path):
    with open(init_path, 'r', encoding='utf-8') as f:
        print("__init__.py content:", f.read())

print("\n=== Checking analyzer.py ===")
analyzer_path = "src/analyzer.py"
print("analyzer.py exists:", os.path.exists(analyzer_path))
if os.path.exists(analyzer_path):
    print("analyzer.py size:", os.path.getsize(analyzer_path), "bytes")
    with open(analyzer_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print("First 200 chars:", content[:200])

print("\n=== Trying import ===")
sys.path.insert(0, os.getcwd())
try:
    import src
    print("✅ src module imported")
except Exception as e:
    print(f"❌ src import failed: {e}")

try:
    from src import analyzer
    print("✅ src.analyzer imported")
except Exception as e:
    print(f"❌ src.analyzer import failed: {e}")
    import traceback
    traceback.print_exc()