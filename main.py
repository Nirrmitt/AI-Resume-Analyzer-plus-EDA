import argparse
import json
from src.analyzer import ResumeAnalyzer
from src.utils import setup_logging

logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(description="AI Resume Analyzer CLI")
    parser.add_argument("--resume", required=True, help="Path to resume (PDF/DOCX/TXT)")
    parser.add_argument("--job", required=True, help="Path to job description (TXT) or paste directly")
    parser.add_argument("--output", help="Output JSON file path")
    args = parser.parse_args()

    job_desc = args.job
    if not args.job.endswith(".txt"):
        job_desc = args.job  # Assume pasted text

    analyzer = ResumeAnalyzer()
    result = analyzer.analyze(args.resume, job_desc)

    if "error" in result:
        logger.error(result["error"])
        return

    print(f"\n🎯 Match Level: {result['match_level']}")
    print(f"📊 Overall Score: {result['overall_score']}%")
    print(f"\n📈 Breakdown:")
    for k, v in result["breakdown"].items():
        print(f"  • {k.replace('_', ' ').title()}: {v}%")
    
    if result["feedback"]:
        print(f"\n💡 Feedback:")
        for f in result["feedback"]:
            print(f"  → {f}")

    if args.output:
        with open(args.output, "w") as f:
            json.dump(result, f, indent=2)
        logger.info(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()