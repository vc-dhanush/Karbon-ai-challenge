# 🌟 Carbon AI – Intelligent Bank Statement Parser Agent

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Framework-LangGraph%20%7C%20Streamlit-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Focus-AI%20%26%20Automation-orange?style=for-the-badge" />
</p>

---

## 📖 Introduction  

Bank statements are one of the most common documents in finance, but **manually extracting, validating, and formatting the data is slow and error-prone**.  

**Carbon AI** is my solution to this problem: an **autonomous parsing agent** that can:  

- Read PDF statements (bank-specific formats)  
- Extract structured transaction data  
- Validate it against expected schema/CSV  
- Retry automatically if errors occur  

This project demonstrates **AI workflow design, clean software architecture, and practical automation skills**, making it ideal for HRs or interviewers to assess problem-solving abilities.

---

## 🌟 Project Overview  

Rather than building a parser for a single bank, I created an **extensible, modular architecture**:  

- Each bank has its **own parser module** (plug-and-play).  
- If parsing fails, the agent retries using different strategies (`camelot`, `pdfplumber`, fallback methods).  
- A **validation layer** ensures extracted data matches expectations.  
- Streamlit UI provides a **simple and interactive interface**.  

This makes the project **scalable, robust, and production-ready**.

---

## 🎯 Objectives  

- Automate repetitive financial data extraction  
- Demonstrate AI agent capabilities with **self-debugging loops**  
- Deliver a clean, modular architecture  
- Build a project that HRs & Interviewers can quickly understand and appreciate  

---

## 🛠 Tech Stack  

- **Language:** Python **3.13**  
- **Frameworks:** LangGraph (workflow/agent), Streamlit (UI)  
- **Libraries:**  
  - `camelot`, `pdfplumber` → PDF parsing  
  - `pandas` → Data handling & validation  
  - `pytest` → Testing  
- **Version Control:** Git + GitHub  
- **Editor:** VS Code  

---

## 🔄 Flow of Work  

```mermaid
flowchart TD
    style A fill:#7FFFD4,stroke:#333,stroke-width:2px,color:#000
    style B fill:#FFD700,stroke:#333,stroke-width:2px,color:#000
    style C fill:#FFB6C1,stroke:#333,stroke-width:2px,color:#000
    style D fill:#87CEFA,stroke:#333,stroke-width:2px,color:#000
    style E fill:#98FB98,stroke:#333,stroke-width:2px,color:#000
    style F fill:#FFA07A,stroke:#333,stroke-width:2px,color:#000
    style G fill:#DA70D6,stroke:#333,stroke-width:2px,color:#000
    style H fill:#FF69B4,stroke:#333,stroke-width:2px,color:#000

    A[User Uploads Bank Statement PDF] --> B[Parser Generator]
    B --> C[Extract Transactions using Camelot/pdfplumber]
    C --> D[Validation Layer (Check Schema/CSV)]
    D --> E{Parsing Successful?}
    E -- Yes --> F[Save & Export Clean Data (CSV/JSON)]
    E -- No --> G[Retry with Self-Debug Loop]
    G --> H[Adjust Parser Parameters / Fallback Method]
    H --> B
