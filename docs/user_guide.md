# SCADA Automation User Guide
This guide explains how to use the SCADA automation scripts.

##  How to Run the Script
1. Ensure Python is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/joshuaannor/scada-automation.git
   cd scada-automation
Run the script:
bash

python scripts/historian_extraction.py
The script will extract historian tag data and trigger alerts if abnormal values are detected.

## 📂 Folder Structure

/scripts     # Automation scripts
/configs     # Configuration files
/docs        # Documentation

## Features
Extracts SCADA historian tags from CSV data.
Processes and filters the extracted data.
Detects anomalies (high temperature, high flow rate) and generates alerts.
