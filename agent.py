#!/usr/bin/env python3
"""
Bank Statement Parser Agent with LangGraph + Groq
Automates: plan → generate parser → run pytest → self-fix (≤3 attempts).
"""

import os
import subprocess
from pathlib import Path
import pandas as pd
from langgraph.graph import StateGraph, END

# --- Groq Setup ---
from groq import Groq

# ⚠️ Insert your API key here
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# --- Templates ---
DEFAULT_TEMPLATE = """\
import pandas as pd
import pdfplumber

def parse(file_path: str) -> pd.DataFrame:
    df = pd.DataFrame()
    if file_path.lower().endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.lower().endswith('.pdf'):
        rows = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    header = table[0]
                    for row in table[1:]:
                        if row == header or all((cell is None or str(cell).strip() == '') for cell in row):
                            continue
                        rows.append(row)
        if rows:
            df = pd.DataFrame(rows, columns=header)

    # Clean numeric columns
    numeric_cols = ["Debit Amt", "Credit Amt", "Balance"]
    for col in df.columns:
        if any(nc.lower() in col.lower() for nc in numeric_cols):
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Normalize NaN to 0.0
    for col in df.columns:
        if df[col].dtype != 'object':
            df[col] = df[col].fillna(0.0)
        else:
            df[col] = df[col].fillna("")

    return df
"""

# --- Parser Generation ---
def generate_parser(bank: str, attempt: int = 1) -> str:
    """Generate parser code using Groq LLM or fallback template."""
    if attempt > 1:
        try:
            prompt = f"""
            Generate a Python parser function parse(file_path:str)->pd.DataFrame for {bank} bank PDF/CSV.
            - Handle repeated headers, empty rows, numeric cleaning (Debit Amt, Credit Amt, Balance).
            - Ensure NaN is replaced with 0.0.
            - Return valid Python code only (no markdown fences).
            """
            resp = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
            )
            code = resp.choices[0].message.content
            code = code.replace("```python", "").replace("```", "").strip()
            if "def parse(" not in code:
                return DEFAULT_TEMPLATE
            return code
        except Exception as e:
            print(f"❌ LLM failed, fallback to default. {e}")
            return DEFAULT_TEMPLATE
    return DEFAULT_TEMPLATE

def write_parser(bank: str, code: str):
    parser_dir = Path("custom_parsers")
    parser_dir.mkdir(exist_ok=True)
    parser_path = parser_dir / f"{bank}_parser.py"
    with open(parser_path, "w", encoding="utf-8") as f:
        f.write(code)
    return parser_path

# --- Pytest Creation ---
def write_pytest(bank: str):
    tests_dir = Path("tests")
    tests_dir.mkdir(exist_ok=True)
    test_path = tests_dir / f"test_{bank}_parser.py"

    pytest_code = f"""
import pandas as pd
import importlib.util
from pathlib import Path

def load_parser(bank):
    spec = importlib.util.spec_from_file_location(f"{{bank}}_parser", Path(f"custom_parsers/{{bank}}_parser.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.parse

def test_parser_output_matches_csv():
    bank = "{bank}"
    parse = load_parser(bank)

    csv_path = Path(f"data/{{bank}}/result.csv")
    pdf_path = Path(f"data/{{bank}}/sample.pdf")

    file_to_parse = csv_path if csv_path.exists() else pdf_path
    df_out = parse(str(file_to_parse))
    assert not df_out.empty, "Parser returned empty DataFrame"

    if csv_path.exists():
        df_ref = pd.read_csv(csv_path)

        # Normalize NaN → 0.0
        for df in [df_out, df_ref]:
            for col in df.columns:
                if df[col].dtype != 'object':
                    df[col] = df[col].fillna(0.0)

        # Check row count
        assert len(df_out) == len(df_ref), f"Row count mismatch: Parsed={{len(df_out)}}, Reference={{len(df_ref)}}"

        # Check column values
        common_cols = set(df_ref.columns).intersection(set(df_out.columns))
        mismatches = []
        for col in common_cols:
            try:
                pd.testing.assert_series_equal(
                    df_out[col].reset_index(drop=True),
                    df_ref[col].reset_index(drop=True),
                    check_dtype=False
                )
                print(f"OK Column '{{col}}' matches")
            except AssertionError:
                mismatches.append(col)
                print(f"X Column '{{col}}' does NOT match")
        if mismatches:
            assert False, f"Mismatched columns: {{mismatches}}"
"""
    with open(test_path, "w", encoding="utf-8") as f:
        f.write(pytest_code)
    return test_path

# --- Run Pytest ---
def run_pytest(test_path: Path) -> tuple[bool, list[str]]:
    """Run pytest on given test file. Return (success, mismatched_columns)."""
    result = subprocess.run(
    ["python", "-m", "pytest", "-s", str(test_path)],
    capture_output=True,
    text=True
)
    
    print(result.stdout)

    mismatches = []
    if "Mismatched columns:" in result.stdout:
        start = result.stdout.find("Mismatched columns:") + len("Mismatched columns:")
        mismatches = result.stdout[start:].strip().strip("[]").replace("'", "").split(", ")
        mismatches = [m for m in mismatches if m]

    if "Row count mismatch" in result.stdout:
        mismatches.append("Row count mismatch")

    return result.returncode == 0, mismatches

# --- LangGraph Workflow ---
def plan_node(state: dict) -> dict:
    bank = state["bank"]
    attempt = state["attempt"]
    print(f"\n🧭 Planning (attempt {attempt}) for {bank}...")
    code = generate_parser(bank, attempt)
    parser_path = write_parser(bank, code)
    test_path = write_pytest(bank)
    return {"bank": bank, "attempt": attempt, "parser_path": parser_path, "test_path": test_path}

def test_node(state: dict) -> dict:
    bank = state["bank"]
    test_path = state["test_path"]
    print(f"🧪 Running pytest...")
    success, mismatches = run_pytest(test_path)
    return {
        "bank": bank,
        "attempt": state["attempt"],
        "success": success,
        "mismatches": mismatches,
        "parser_path": state["parser_path"],
        "test_path": test_path,
    }

def decide_node(state: dict) -> str:
    if state["success"]:
        print(f"✅ Attempt {state['attempt']} succeeded. All rows & columns match!")
        return END
    elif state["attempt"] >= 3:
        print(f"❌ Max attempts reached. Final mismatches: {state['mismatches']}")
        return END
    else:
        print(f"🔄 Attempt {state['attempt']} failed. Mismatches: {state['mismatches']}. Retrying...")
        state["attempt"] += 1
        return "plan"

# --- Main ---
def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, help="Bank target (e.g., icici)")
    args = parser.parse_args()

    workflow = StateGraph(dict)
    workflow.add_node("plan", plan_node)
    workflow.add_node("test", test_node)

    workflow.add_edge("plan", "test")
    workflow.add_conditional_edges("test", decide_node)

    workflow.set_entry_point("plan")

    app = workflow.compile()
    init_state = {"bank": args.target, "attempt": 1, "success": False, "mismatches": []}
    app.invoke(init_state)

if __name__ == "__main__":
    main()
