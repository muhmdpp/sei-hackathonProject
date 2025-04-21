import pandas as pd
from datetime import datetime
from app.anomaly_detection import AnomalyDetectionModel

def append_new_data(new_data, csv_path, json_path):
    # Load existing data
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])

    # Append new data
    new_df = pd.DataFrame([new_data])
    df = pd.concat([df, new_df], ignore_index=True)

    # Save updated CSV
    df.to_csv(csv_path, index=False)

    # Detect anomalies and update JSON
    model = AnomalyDetectionModel()
    anomalies = model.detect_anomalies(df)
    model.save_to_json(anomalies, json_path)

# Example new data
new_data = {
    "Date": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "Close": 0.95,
    "MarketCap": 2400000000,
    "Volume": 300000000
}

# Paths
csv_path = "data/sei-usd-max.csv"
json_path = "data/anomalies.json"

# Update data and JSON
append_new_data(new_data, csv_path, json_path)