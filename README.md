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

This project, **Carbon AI**, is my attempt to solve that pain point by building an **autonomous parsing agent**.  
The agent is capable of:  

- Reading PDF statements (bank-specific formats)  
- Extracting structured transaction data  
- Validating it against expected schema/CSV  
- Self-correcting errors through retry loops  

I built this project as a **coding challenge**, but more importantly as a way to **demonstrate my problem-solving skills, AI workflow design, and ability to deliver production-ready tools**.  

---

## 🌟 Project Overview  

Instead of creating a one-time parser for a single bank, I designed an **extensible architecture**:  

- Each bank can have its **own parser module** (plug-and-play design).  
- If parsing fails, the agent retries using different strategies (`camelot`, `pdfplumber`, fallback methods).  
- A **validation layer** ensures extracted data matches expectations.  
- Streamlit UI was added for a **simple and interactive experience**.  

This approach makes the project not just a **working solution**, but a **scalable system** that can adapt to multiple formats.  

---

## 🎯 Objectives  

- Automate repetitive financial data extraction  
- Showcase AI agent capabilities with **self-debugging loops**  
- Deliver a clean architecture suitable for real-world use  
- Build something HRs & Interviewers can **look at and immediately see impact**  

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

    A[📂 User Uploads Bank Statement PDF] --> B[⚙️ Parser Generator]
    B --> C[🔍 Extract Transactions using Camelot/pdfplumber]
    C --> D[📊 Validation Layer (Check Schema/CSV)]
    D --> E{✅ Success?}
    E -- Yes --> F[💾 Save & Export Clean Data (CSV/JSON)]
    E -- No --> G[🔄 Retry with Self-Debug Loop]
    G --> B
