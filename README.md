# 🚀 Carbon AI – Bank Statement Parser Agent

<p align="center">
  <img src="https://img.shields.io/badge/Project-Carbon%20AI-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python" />
</p>

---

## 📖 Introduction

**Carbon AI** is an intelligent **Bank Statement Parser Agent** designed to automate data extraction from PDF bank statements and transform them into structured formats (CSV/JSON).  
This project leverages **LangGraph + Groq**, integrates **self-debugging loops**, and provides a modular architecture suitable for financial automation.

---

## 🌟 Overview

Bank statement analysis is a repetitive yet critical task in finance.  
This project solves it by building an **autonomous agent** that:

- Reads bank statements (PDFs)  
- Parses & validates extracted data  
- Uses modular parser generation for different banks  
- Ensures high accuracy with **retry/self-correction loops**  

---

## 🎯 Objective

- ✅ Automate financial data parsing  
- ✅ Build a scalable agent architecture  
- ✅ Provide clean, validated outputs  
- ✅ Minimize manual human effort in statement analysis  

---

## 🛠️ Tech Stack

- **Programming Language**: Python 🐍  
- **Framework**: Streamlit (for UI), LangGraph (for Agent Workflow)  
- **Libraries**:  
  - `camelot` / `pdfplumber` → PDF parsing  
  - `pandas` → Data handling  
  - `pytest` → Testing  
- **Version Control**: Git + GitHub  
- **Deployment**: Localhost / Cloud Ready  

---

## 🔄 Flow of Work

```mermaid
flowchart TD
    A[User Uploads PDF] --> B[Parser Generator]
    B --> C[Extract Transactions]
    C --> D[Validation against CSV]
    D --> E{Success?}
    E -- Yes --> F[Save Clean Data]
    E -- No --> G[Self-Debug & Retry Loop]
    G --> B
