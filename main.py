import pandas as pd
import re
import os
from datetime import datetime

LOG_FILE = 'data/server.log'
REPORT_DIR = 'reports'
REPORT_FILE = os.path.join(REPORT_DIR, 'log_analysis_report.csv')

ERROR_PATTERNS = {
    'Packet Loss': r'packet loss',
    'Auth Failure': r'authentication failure',
    'DNS Timeout': r'dns timeout',
    'Connection Drop': r'connection drop|disconnected'
}

def parse_logs(file_path):
    log_data = []
    log_pattern = re.compile(r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (?P<level>\w+) - (?P<message>.*)')

    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return pd.DataFrame()

    with open(file_path, 'r') as f:
        for line in f:
            match = log_pattern.match(line.strip())
            if match:
                log_data.append(match.groupdict())

    return pd.DataFrame(log_data)

def categorize_issue(message):
    for category, pattern in ERROR_PATTERNS.items():
        if re.search(pattern, message, re.IGNORECASE):
            return category
    return 'Other'

def analyze_logs(df):
    if df.empty:
        return None

    df['issue_type'] = df['message'].apply(categorize_issue)
    
    critical_issues = df[df['issue_type'] != 'Other'].copy()
    
    summary = critical_issues['issue_type'].value_counts()
    
    return critical_issues, summary

def save_report(df, summary):
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

    with open(REPORT_FILE, 'w') as f:
        f.write("NETWORK LOG ANALYSIS SUMMARY\n")
        f.write("="*30 + "\n")
        f.write(summary.to_string())
        f.write("\n\n" + "="*30 + "\nDETAILED ERROR LOGS\n")
        df.to_csv(f, index=False)
    
    print(f"Analysis complete. Report saved to {REPORT_FILE}")
    print("\n--- Summary ---")
    print(summary)

if __name__ == "__main__":
    print("Starting Network Log Analyzer...")
    
    df_logs = parse_logs(LOG_FILE)
    
    if not df_logs.empty:
        details, stats = analyze_logs(df_logs)
        if details is not None:
            save_report(details, stats)
        else:
            print("No issues found.")
    else:
        print("No logs to process.")