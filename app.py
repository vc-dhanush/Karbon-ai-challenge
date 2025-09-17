import os
from pathlib import Path
import streamlit as st

# ==========================
# App Configuration
# ==========================
st.set_page_config(page_title="Bank Statement Parser", layout="wide")
st.title("📄 Bank Statement Parser")

# Upload area
uploaded_file = st.file_uploader("Upload a bank statement (PDF)", type=["pdf"])

if uploaded_file is not None:
    # Create directory if not exists
    data_dir = Path("data/icici")
    data_dir.mkdir(parents=True, exist_ok=True)

    # Save uploaded file
    file_path = data_dir / uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Rename uploaded file to a standard name
    dest = data_dir / "sample.pdf"
    try:
        file_path.replace(dest)   # overwrites if dest exists
        st.success(f"✅ File saved as: {dest}")
    except Exception as e:
        st.error(f"⚠️ Error while moving file: {e}")

    # ==========================
    # Process the PDF (dummy for now)
    # ==========================
    st.info("📊 Processing the bank statement...")
    # TODO: Replace this with your parser logic
    st.write("Parsed data will appear here once implemented.")

else:
    st.warning("👆 Please upload a PDF file to continue.")
