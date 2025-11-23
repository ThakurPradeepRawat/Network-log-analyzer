# 📡 Network Log Analyzer

![Python](https://img.shields.io/badge/Python-3.13+-blue)
![Library](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 🚀 Overview
**Network Log Analyzer** is an automated Python tool designed to process raw server logs and extract critical network health metrics. 

In large-scale network environments, debugging through thousands of log lines manually is inefficient. This tool utilizes **Pandas** and **Regex (Regular Expressions)** to instantly parse log files, detect patterns like **Packet Loss**, **DNS Timeouts**, and **Authentication Failures**, and generate a summarized executive report for network administrators.

---

## ⚡ Key Features
- **Regex-Based Parsing:** Efficiently extracts timestamps, log levels, and messages from unstructured text files.
- **Automated Error Categorization:** Automatically classifies logs into:
  - 🔴 Packet Loss
  - 🔒 Authentication Failures
  - 🌐 DNS Timeouts
  - 🔌 Connection Drops
- **Pandas DataFrame Processing:** High-performance filtering and data manipulation.
- **Actionable Reporting:** Exports a clean summary and detailed error logs to a CSV file.

---

## 🛠️ Tech Stack
| Component | Technology | Usage |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Core Logic |
| **Data Processing** | Pandas | Data Frames & Analytics |
| **Pattern Matching** | Re (Regex) | Log Parsing |
| **File Handling** | OS Module | Directory & File Management |

---

## 📂 Project Structure
```text
Network_Log_Analyzer/
│
├── data/
│   └── server.log          # Input: Raw log file containing server activity
│
├── reports/
│   └── log_analysis_report.csv  # Output: Generated summary report
│
├── main.py                 # Source code for analysis logic
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation