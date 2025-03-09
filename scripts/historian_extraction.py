import csv

# File path for sample data
DATA_FILE = "configs/sample_historian_data.csv"


def extract_tags():
    """Reads SCADA historian data from a CSV file."""
    try:
        with open(DATA_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print("Error: Sample data file not found.")
        return []

def process_data(data):
    """Processes SCADA data: Filters abnormal values."""
    processed = []
    for row in data:
        value = float(row['value'])
        if row['tag'] == "FlowRate" and value > 180:
            print(f"⚠ Alert: High FlowRate detected at {row['timestamp']} ({value} L/min)")
        elif row['tag'] == "Temperature" and value > 90:
            print(f"⚠ Alert: High Temperature detected at {row['timestamp']} ({value}°C)")
        processed.append(row)
    return processed

if __name__ == "__main__":
    print("🔄 Extracting SCADA historian tags...")
    extracted_data = extract_tags()
    if extracted_data:
        print("✅ Data successfully extracted.")
        print("🔄 Processing SCADA data...")
        processed_data = process_data(extracted_data)
        print("✅ Data processing complete.")
