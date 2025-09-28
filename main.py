# backend/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import sqlite3
import pandas as pd
from bank_detector import detect_bank
from categorizer import categorize
from custom_parsers.icici_parser import parse_pdf  # example parser

app = FastAPI()

DB_PATH = "karbon_ai.db"

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bank TEXT,
            date TEXT,
            description TEXT,
            debit REAL,
            credit REAL,
            balance REAL,
            category TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Upload PDF and parse
@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    pdf_path = f"temp_{file.filename}"
    with open(pdf_path, "wb") as f:
        f.write(contents)
    
    bank = detect_bank(pdf_path)
    if bank == "icici":
        df = parse_pdf(pdf_path)
    else:
        return JSONResponse(content={"error": "Bank not supported"}, status_code=400)
    
    df['Category'] = df['Description'].apply(categorize)

    # Save to DB
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("transactions", conn, if_exists="append", index=False)
    conn.close()

    return {"status": "success", "bank": bank, "rows_saved": len(df)}

# Fetch transactions
@app.get("/transactions/")
def get_transactions(bank: str = None):
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * FROM transactions"
    if bank:
        query += f" WHERE bank='{bank}'"
    df = pd.read_sql(query, conn)
    conn.close()
    return df.to_dict(orient="records")
