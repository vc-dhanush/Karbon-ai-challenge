import pandas as pd
from fpdf import FPDF

def export_reports(df, bank_name):
    # CSV
    df.to_csv(f'{bank_name}_report.csv', index=False)

    # Excel
    df.to_excel(f'{bank_name}_report.xlsx', index=False)

    # PDF Summary
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"{bank_name.upper()} Financial Report", ln=True, align='C')
    
    # Add top 5 transactions
    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    for idx, row in df.head(5).iterrows():
        pdf.cell(0, 8, f"{row['Date']} | {row['Description']} | Debit: {row['Debit']} | Credit: {row['Credit']} | Category: {row['Category']}", ln=True)
    
    # Add charts
    pdf.image(f'{bank_name}_expenses_chart.png', x=10, y=80, w=90)
    pdf.image(f'{bank_name}_monthly_trend.png', x=110, y=80, w=90)
    
    pdf.output(f'{bank_name}_report.pdf')
    print(f"Reports exported: {bank_name}_report.csv, {bank_name}_report.xlsx, {bank_name}_report.pdf")