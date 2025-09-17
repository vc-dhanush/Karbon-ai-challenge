# Carbon AI – Intelligent Bank Statement Parser Agent

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Framework-LangGraph%20%7C%20Streamlit-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Focus-AI%20and%20Automation-orange?style=for-the-badge" />
</p>

---

## Introduction  

Bank statements are one of the most common documents in finance, but manually extracting, validating, and formatting the data is slow and error-prone.  

**Carbon AI** is an autonomous parsing agent that can:  

- Read PDF statements (bank-specific formats)  
- Extract structured transaction data  
- Validate it against expected schema or CSV  
- Retry automatically if errors occur  

This project demonstrates AI workflow design, clean software architecture, and practical automation skills.

---

## Project Overview  

Rather than building a parser for a single bank, an **extensible modular architecture** was created:  

- Each bank has its **own parser module** (plug-and-play).  
- If parsing fails, the agent retries using different strategies (`camelot`, `pdfplumber`, fallback methods).  
- A **validation layer** ensures extracted data matches expectations.  
- Streamlit UI provides a simple and interactive interface.  

This makes the project scalable, robust, and production-ready.

---

## Objectives  

- Automate repetitive financial data extraction  
- Demonstrate AI agent capabilities with self-debugging loops  
- Deliver a clean, modular architecture  
- Build a project that HRs and interviewers can quickly understand and appreciate  

---

## Tech Stack  

- **Language:** Python 3.13  
- **Frameworks:** LangGraph (workflow/agent), Streamlit (UI)  
- **Libraries:**  
  - `camelot`, `pdfplumber` → PDF parsing  
  - `pandas` → Data handling and validation  
  - `pytest` → Testing  
- **Version Control:** Git and GitHub  
- **Editor:** VS Code  

---



    





```
Requirements
Python 3.13

Virtual environment recommended
Install dependencies:
pip install -r requirements.txt

How to Run
Clone the repository:

git clone https://github.com/your-username/Carbon-AI.git
cd Carbon-AI


Run the agent:
python agent.py --target icici


Launch the Streamlit UI (optional):
streamlit run app.py


Run tests:
pytest

Demo
Key Learnings
Designing autonomous agents with retry/self-correcting loops
Handling inconsistent PDF layouts
Building extensible, modular architectures
Importance of validation, testing, and clean documentation

Conclusion

Carbon AI showcases practical AI workflow design, modular architecture, and automation skills.
It demonstrates the ability to plan, implement, and deliver real-world solutions, making it a strong project for HRs and interviewers to evaluate.
Built with dedication by    
                           `~Vc Dhanush
