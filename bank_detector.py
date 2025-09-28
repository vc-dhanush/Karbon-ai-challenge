import pdfplumber

def detect_bank(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0].extract_text().lower()
        if "icici" in first_page:
            return "icici"
        elif "hdfc" in first_page:
            return "hdfc"
        elif "sbi" in first_page:
            return "sbi"
        elif "axis" in first_page:
            return "axis"
        else:
            return "unknown"
