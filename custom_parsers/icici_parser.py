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
