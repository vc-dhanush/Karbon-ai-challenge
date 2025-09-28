def categorize(description):
    desc = description.lower()
    if "salary" in desc:
        return "Income"
    elif "amazon" in desc or "flipkart" in desc:
        return "Shopping"
    elif "upi" in desc or "payment" in desc:
        return "Payments"
    elif "electricity" in desc or "water" in desc:
        return "Bills"
    else:
        return "Others"
import pdfplumber