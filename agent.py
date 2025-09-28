import argparse
from custom_parsers import icici_parser

def main():
    parser = argparse.ArgumentParser(description="Bank Statement Parser Agent")
    parser.add_argument("--target", required=True, help="Target bank name (e.g., icici)")
    args = parser.parse_args()

    if args.target.lower() == "icici":
        pdf_path = "data/icici/icici_sample.pdf"  # change to your actual PDF path
        print(f"[INFO] Parsing ICICI PDF from: {pdf_path}")
        try:
            df = icici_parser.parse(pdf_path)
            print("[✅ SUCCESS] Parsing completed!\n")
            print(df.head())
        except Exception as e:
            print(f"[❌ ERROR] Parsing failed: {e}")
    else:
        print(f"[⚠️ ERROR] No parser available for bank: {args.target}")


if __name__ == "__main__":
    main()
